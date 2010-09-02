gle.freq-dawg:	gle.freq-text
	wordlist2dawg gle.freq-text gle.freq-dawg

gle-uncial.freq-dawg:	gle-uncial.freq-text
	wordlist2dawg gle-uncial.freq-text gle-uncial.freq-dawg
	
gle-uncial.word-dawg:	gle-uncial.word-text
	wordlist2dawg gle-uncial.word-text gle-uncial.word-dawg

DATADIR=/usr/local/share/tessdata
INSTALL=/usr/bin/install
install:
	$(INSTALL) -m 444 gle-uncial.DangAmbigs $(DATADIR)
	$(INSTALL) -m 444 gle-uncial.freq-dawg $(DATADIR)
	$(INSTALL) -m 444 gle-uncial.inttemp $(DATADIR)
	$(INSTALL) -m 444 gle-uncial.normproto $(DATADIR)
	$(INSTALL) -m 444 gle-uncial.pffmtable $(DATADIR)
	$(INSTALL) -m 444 gle-uncial.unicharset $(DATADIR)
	$(INSTALL) -m 444 gle-uncial.user-words $(DATADIR)
	$(INSTALL) -m 444 gle-uncial.word-dawg $(DATADIR)
