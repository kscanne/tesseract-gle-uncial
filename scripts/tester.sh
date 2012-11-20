#!/bin/bash
if [ $# -ne 2 ]
then
	echo "Usage: bash tester.sh TESSMODEL IMAGENOEXTENSION"
	echo "e.g.: bash tester.sh gle-test20 001"
	echo "Assuming gle-test20.traineddata is in /usr/share/tesseract-ocr/tessdata"
	echo "and 001.tif and 001.box are in the current directory"
	exit 1
fi
tesseract "${2}.tif" tempocroutput -l "${1}"
cat tempocroutput.txt | sed 's/./\n&/g' | egrep '[^ ]' > outputchars.txt
echo "OCR output:"
cat tempocroutput.txt
#echo "Changes to fix OCR output:"
#cat "${2}.box" | sed 's/ .*//' | diff -u outputchars.txt -
if [ -e "${2}.box" ]
then
	echo "Edit distance:"
	cat "${2}.box" | sed 's/ .*//' | diff -d -e outputchars.txt - | wc -l
else
	echo "No box file for this .tif"
fi
rm -f tempocroutput.txt outputchars.txt
