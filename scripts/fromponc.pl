#!/usr/bin/perl

use strict;
use warnings;
use utf8;

binmode STDIN, ":utf8";
binmode STDOUT, ":utf8";
binmode STDERR, ":utf8";

# ignore ’ for now...
while (<STDIN>) {
	s/ḃ/bh/g;
	s/ċ/ch/g;
	s/ḋ/dh/g;
	s/ḟ/fh/g;
	s/ġ/gh/g;
	s/ṁ/mh/g;
	s/ṗ/ph/g;
	s/ṡ/sh/g;
	s/ṫ/th/g;
	s/Ḃ/Bh/g;
	s/Ċ/Ch/g;
	s/Ḋ/Dh/g;
	s/Ḟ/Fh/g;
	s/Ġ/Gh/g;
	s/Ṁ/Mh/g;
	s/Ṗ/Ph/g;
	s/Ṡ/Sh/g;
	s/Ṫ/Th/g;
	s/([A-ZÁÉÍÓÚ]{2})h/$1H/g;
	s/([A-ZÁÉÍÓÚ])h([A-ZÁÉÍÓÚ])/$1H$2/g;
	print;
}

exit 0;
