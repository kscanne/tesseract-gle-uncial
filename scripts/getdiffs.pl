#!/usr/bin/perl

use strict;
use warnings;
use utf8;
use Memoize;

binmode STDIN, ":utf8";
binmode STDOUT, ":utf8";
binmode STDERR, ":utf8";

my @boxwords;
my @transwords;
my $curr='';


# x,y are refs to strings like "baila","balla",
# and @$aref is an array containing lcs of x and y  ("ba", "la") 
# this replaces the common substrings with strings of *'s,
# thereby leaving only the bits that are changed
sub subber
{
	(my $x, my $y, my $aref) = @_;
	if ($$x eq '^ííí' and $$y eq '^Ní') {  # temp hack
		$$x = 'íí*'; $$y = 'N*'; return;
	}
	my $first = shift @$aref;
	if (defined($first)) {
		my $stars = $first; 
		$stars =~ s/./*/g;
		$first =~ s/(.)/[$1]/g;  # escape ?, parens, etc. b4 search
		(my $xs, my $xt) = $$x =~ /^(.*?)$first(.*)$/;
		(my $ys, my $yt) = $$y =~ /^(.*?)$first(.*)$/;
		subber(\$xt, \$yt, $aref);
		$$x = $xs.$stars.$xt;
		$$y = $ys.$stars.$yt;
	}
}

# computes longest common subsequence of x and y
# returns the total length of the LCS
# a boolean that gets filled in depending on which case 
# we end up in, used in the recursion
# and an array with the substrings forming the LCS
sub lcs
{
	(my $x, my $y) = @_;
	return (0, 0, ()) if (length($x)==0 or length($y)==0);
	(my $xstart, my $xlast) = $x =~ /^(.*)(.)$/;
	(my $ystart, my $ylast) = $y =~ /^(.*)(.)$/;
	if ($ylast eq $xlast) {
		my ($sublen, $end_p, @common) = lcs($xstart, $ystart);
		if ($end_p) {
			my $lastone = pop @common;
			push @common, $lastone.$xlast;
		}
		else {
			push @common, $xlast;
		}
		return ($sublen+1,1,@common);
	}
	else {
		my ($subans1, $subatend1, @subarr1) = lcs($x, $ystart);
		my ($subans2, $subatend2, @subarr2) = lcs($xstart, $y);
		if ($subans2 > $subans1) {
			return ($subans2, 0, @subarr2);
		}
		else {
			return ($subans1, 0, @subarr1);
		}
	}
}

memoize('lcs');

open(BOXFILE, "<:utf8", $ARGV[0]) or die "Could not open $ARGV[0]: $!\n";
while (<BOXFILE>) {
	chomp;
	if ($_ eq '<w>') {
		if ($curr ne '') {
			push @boxwords, $curr;	
			$curr = '';
		}
	}
	else {
		$curr .= $_;
	}
}
close BOXFILE;

$curr='';
open(TRANSCRIPTION, "<:utf8", $ARGV[1]) or die "Could not open $ARGV[1]: $!\n";
while (<TRANSCRIPTION>) {
	chomp;
	if ($_ eq '<w>') {
		if ($curr ne '') {
			push @transwords, $curr;	
			$curr = '';
		}
	}
	else {
		$curr .= $_;
	}
}
close TRANSCRIPTION;

if (scalar @boxwords != scalar @transwords) {
	die "Different number of words in files!";
}

# only single char on RHS for now...
my %changes = ("si:r" => 1,
		"sí:r" => 1,
		"ii:n" => 1,
		"ii:r" => 1,
		"íi:u" => 1,
		"íí:N" => 1,
		"íí:R" => 1,
		'íí:"' => 1,
		'"":"' => 1,
		'É":"' => 1,
		'"É:"' => 1,
		"iii:m" => 1,
		"in:m" => 1,
		"ni:m" => 1,
		"ni:ṁ" => 1,
		"in:ṁ" => 1,
		"ih:ṁ" => 1,
		"iíi:ṁ" => 1,
		"íN:M" => 1,
		"ííí:M" => 1,
		"so:p" => 1,
		"sb:p" => 1,
		"s-:s" => 1,
		"sc:s" => 1,
		"ss:s" => 1,
		);


my $windex = 0;
my $box_cindex = 0;
my @queue;
my $pending = 0;
my $pendingcorr;
my $startc;
my $endc;
open(REALBOX, "<:utf8", $ARGV[2]) or die "Could not open $ARGV[2]: $!\n";
while (<REALBOX>) {
	chomp;
	(my $ocr) = /^([^ ]+)/;
	if ($pending) {
		if ($box_cindex >= $startc and $box_cindex <= $endc) {
			push @queue, $_;
		}
		else {
			print "$_\n";
		}
		if ($box_cindex == $endc) {
			$pending = 0;
			my $bestminx=20000;
			my $bestminy=20000;
			my $bestmaxx=-1;
			my $bestmaxy=-1;
			foreach my $ln (@queue) {
				(my $o, my $minx, my $miny, my $maxx, my $maxy) = $ln =~ m/^([^ ]+) ([0-9]+) ([0-9]+) ([0-9]+) ([0-9]+)$/;
				$bestminx = $minx if ($minx < $bestminx);
				$bestminy = $miny if ($miny < $bestminy);
				$bestmaxx = $maxx if ($maxx > $bestmaxx);
				$bestmaxy = $maxy if ($maxy > $bestmaxy);
			}
			print "$pendingcorr $bestminx $bestminy $bestmaxx $bestmaxy\n";
			@queue = ();
		}
	}
	else {
		print "$_\n";
	}
	$box_cindex += length($ocr);  # usually 1
	if ($box_cindex >= length($boxwords[$windex])) {
		$windex++;
		$box_cindex = 0;
		exit 0 if ($windex == scalar @boxwords);
		if ($boxwords[$windex] ne $transwords[$windex]) {
			foreach my $change (keys %changes) {
				(my $l, my $r) = $change =~ /^([^:]+):(.+)$/;
				my $temp = $boxwords[$windex];
				$temp =~ s/$l/$r/;
				if ($temp eq $transwords[$windex]) {
					$pending = 1;
					$pendingcorr = $r;
					(my $st) = $boxwords[$windex] =~ /^(.*?)$l/;
					$startc = length($st);
					$endc = $startc + length($l) - 1;
				}
			}
		}
	}
}
close REALBOX;

exit 0;
