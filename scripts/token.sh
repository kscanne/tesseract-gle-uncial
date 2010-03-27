#!/bin/bash
TMP1=temp-trans
TMP2=temp-box
cat "${1}.txt" | sed "s/'/’/g" | tr -d "\015" | tr -s " " "~" | tr -s "\n" "~" | sed 's/./&>/g' | tr ">" "\n" | sed 's/^~$/<w>/' | sed '1s/.*/<w>~&/' | tr "~" "\n"  > $TMP1
cat "${1}.box" | perl breaks.pl | sed 's/ .*//' > $TMP2 
vimdiff $TMP2 $TMP1
#perl getdiffs.pl $TMP2 $TMP1 "${1}.box" > "${1}.box.2"
