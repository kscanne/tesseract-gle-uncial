# N.B. This makefile should be symbolically linked in all of the pages/* directories with the
# .tif images that have been checked into SVN, so I can work in those dirs directly
# TESSLANG=eng
# TESSLANG=gle
TESSLANG=gle-uncial
MY_TESSDATA_PREFIX=/usr/local/share

%.txt : %.tif
	TESSDATA_PREFIX=$(MY_TESSDATA_PREFIX)/ tesseract $< kpsocrtemp -l $(TESSLANG)
	mv -f kpsocrtemp.txt $@


# See "Bootstrapping a new character set" in the training documentation:
# http://code.google.com/p/tesseract-ocr/wiki/TrainingTesseract
# For this, we're bootstrapping, so want -l $(TESSLANG) and 
# TESSDATA_PREFIX set to tesseract-gle-uncial in SVN 
%.box : %.tif
	TESSDATA_PREFIX=$(MY_TESSDATA_PREFIX)/ tesseract $< kpsocrboxtemp -l $(TESSLANG) batch.nochop makebox
	mv kpsocrboxtemp.txt $@

SVN_TESSDATA=$(HOME)/ocr/tesseract-gle-uncial/tessdata
# training requires .tif and *correct* .box files and generates
# inttemp, normproto, pffmtable; doesn't use a pre-existing language model
# for this, so no need to specify -l $(TESSLANG), and want 
# TESSDATA_PREFIX to be unset
train :
	tesseract 001.tif junk nobatch box.train
	cat tesseract.log
	tesseract 002.tif junk nobatch box.train
	cat tesseract.log
	tesseract 004.tif junk nobatch box.train
	cat tesseract.log
	tesseract 005.tif junk nobatch box.train
	cat tesseract.log
	tesseract 006.tif junk nobatch box.train
	cat tesseract.log
	tesseract 010.tif junk nobatch box.train
	cat tesseract.log
	tesseract 011.tif junk nobatch box.train
	cat tesseract.log
	tesseract 012.tif junk nobatch box.train
	cat tesseract.log
	mftraining 001.tr 002.tr 004.tr 005.tr 006.tr 010.tr 011.tr 012.tr
	cntraining 001.tr 002.tr 004.tr 005.tr 006.tr 010.tr 011.tr 012.tr
	unicharset_extractor 001.box 002.box 004.box 005.box 006.box 010.box 011.box 012.box
	mv -f inttemp $(SVN_TESSDATA)/gle-uncial.inttemp
	rm -f junk.txt Microfeat
	mv -f normproto $(SVN_TESSDATA)/gle-uncial.normproto
	mv -f pffmtable $(SVN_TESSDATA)/gle-uncial.pffmtable
	mv -f unicharset $(SVN_TESSDATA)/gle-uncial.unicharset
	rm -f tesseract.log
