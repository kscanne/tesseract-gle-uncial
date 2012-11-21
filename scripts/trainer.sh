#!/bin/bash
if [ $# -ne 2 ]
then
	echo "Usage: bash trainer DIRECTORY_WITH_TIF_BOX_PAIRS LANGNAME"
	exit 1
fi
HERE=`pwd`
cd "${1}"
BOXFILES=`find . -name '*.box' | sort | tr "\n" " "`
TRFILES=`echo "${BOXFILES}" | sed 's/\.box/.tr/g'`
TXTFILES=`echo "${BOXFILES}" | sed 's/\.box/.txt/g'`
find . -name '*.box' | sort | sed 's/\.box//' |
while read x
do
	tesseract $x.tif "${HERE}/$x" nobatch box.train.stderr
done
unicharset_extractor ${BOXFILES}
mv unicharset "${HERE}"
cd "${HERE}"
rm -f font_properties
echo "UnknownFont 0 0 0 1 0" > font_properties
shapeclustering -F font_properties -U unicharset ${TRFILES}
mftraining -F font_properties -U unicharset -O "${2}.unicharset" ${TRFILES}
cntraining ${TRFILES}
mv -f normproto "${2}.normproto"
mv -f inttemp "${2}.inttemp"
mv -f pffmtable "${2}.pffmtable"
mv -f shapetable "${2}.shapetable"
combine_tessdata "${2}."
rm -f font_properties unicharset
rm -f ${TRFILES} ${TXTFILES}
