#!/usr/bin/perl

use strict;
use warnings;
use utf8;

binmode STDIN, ":utf8";
binmode STDOUT, ":utf8";
binmode STDERR, ":utf8";

my $prevr = -100;
my $prevc = '';
while (<STDIN>) {
	chomp;
	(my $c, my $l, my $r) = /^([^ ]+) ([0-9]+) [^ ]+ ([0-9]+) [^ ]+$/;
	my $gap = $l - $prevr;
	print "<w>\n" if ($gap < -100);
	print "<w>\n" if ($gap > 12 and $c !~ /^[!?;:,]$/ and ($prevc ne '"' or $gap > 20)); 
	print "$_\n";
	$prevr = $r;
	$prevc = $c
}
print "<w>\n";

exit 0;
