DATADIR=/usr/share/tesseract-ocr/tessdata
#DATADIR=/usr/local/share/tessdata
INSTALL=/usr/bin/install

all: gle-uncial.traineddata gle.freq-dawg

gle-uncial.traineddata: gle-uncial.DangAmbigs gle-uncial.freq-dawg gle-uncial.inttemp gle-uncial.normproto gle-uncial.pffmtable gle-uncial.unicharset gle-uncial.user-words gle-uncial.word-dawg
	combine_tessdata ./gle-uncial.

gle.freq-dawg:	gle.freq-text gle-uncial.unicharset
	wordlist2dawg gle.freq-text gle.freq-dawg gle-uncial.unicharset

gle-uncial.freq-dawg:	gle-uncial.freq-text gle-uncial.unicharset
	wordlist2dawg gle-uncial.freq-text gle-uncial.freq-dawg gle-uncial.unicharset
	
gle-uncial.word-dawg:	gle-uncial.word-text gle-uncial.unicharset
	wordlist2dawg gle-uncial.word-text gle-uncial.word-dawg gle-uncial.unicharset

install:
	$(INSTALL) -m 444 gle-uncial.traineddata $(DATADIR)

clean:
	rm -f gle-uncial.word-dawg gle-uncial.freq-dawg gle.freq-dawg gle-uncial.traineddata
