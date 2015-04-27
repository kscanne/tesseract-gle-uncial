#!/bin/bash
if [ $# -ne 3 ]
then
	echo "Usage: bash trainer.sh DIRECTORY_WITH_TIF_BOX_PAIRS LANGNAME REPO_TESSDATA"
	echo "Dirs are relative to base dir of git clone:"
	echo "e.g. $ bash trainer.sh pages/besidethefire gle-uncial tessdata"
	exit 1
fi
GITHOME=${HOME}/seal/tesseract-gle-uncial
THERE="${GITHOME}/${3}"
cd "${GITHOME}/${1}"
BOXFILES=`find . -name '*.box' | sort | tr "\n" " "`
TRFILES=`echo "${BOXFILES}" | sed 's/\.box/.tr/g'`
TXTFILES=`echo "${BOXFILES}" | sed 's/\.box/.txt/g'`

# turn box/tif pairs into .tr files (features for the given page)
find . -name '*.box' | sort | sed 's/\.box//' |
while read x
do
	tesseract $x.tif "${THERE}/$x" nobatch box.train.stderr
done
unicharset_extractor ${BOXFILES}
mv unicharset "${THERE}"
cd "${THERE}"
rm -f font_properties
echo "UnknownFont 0 0 0 1 0" > font_properties
shapeclustering -F font_properties -U unicharset ${TRFILES}
mftraining -F font_properties -U unicharset -O "${2}.unicharset" ${TRFILES}
cntraining ${TRFILES}
mv -f normproto "${2}.normproto"
mv -f inttemp "${2}.inttemp"
mv -f pffmtable "${2}.pffmtable"
mv -f shapetable "${2}.shapetable"
# call: combine_tessdata "${2}."
# By doing it in ../tessdata, we bundle dawg files in there too
make "${2}.traineddata"
rm -f font_properties unicharset
rm -f ${TRFILES} ${TXTFILES}
