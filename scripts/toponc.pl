#!/usr/bin/perl

use strict;
use warnings;
use utf8;

binmode STDIN, ":utf8";
binmode STDOUT, ":utf8";
binmode STDERR, ":utf8";

# ignore ’ for now...
while (<STDIN>) {
	s/bh/ḃ/g;
	s/ch/ċ/g;
	s/dh/ḋ/g;
	s/fh/ḟ/g;
	s/gh/ġ/g;
	s/mh/ṁ/g;
	s/ph/ṗ/g;
	s/sh/ṡ/g;
	s/th/ṫ/g;
	s/B[Hh]/Ḃ/g;
	s/C[Hh]/Ċ/g;
	s/D[Hh]/Ḋ/g;
	s/F[Hh]/Ḟ/g;
	s/G[Hh]/Ġ/g;
	s/M[Hh]/Ṁ/g;
	s/P[Hh]/Ṗ/g;
	s/S[Hh]/Ṡ/g;
	s/T[Hh]/Ṫ/g;
	s/{h}/h/g;   # should transcribe explicit h's (e.g. "Sheffield", "Shakespeare") as "S{h}effield", etc.
	s/{H}/H/g;
	s/7/⁊/g;
	print;
}

exit 0;
