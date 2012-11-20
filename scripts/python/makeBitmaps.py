# -*- coding: utf-8 -*-

import string,time
import codecs
from os import curdir, sep, mkdir, makedirs, path
from subprocess import Popen, PIPE, STDOUT
import lib  # my local test lib.py

def main():
    print("Hello!")
    inputFileName =  'aibitir.box' #'semicolon.box'  #'gle-test2.testfont.box'
    inputWidth = 1200 #2985  #924
    inputHeight = 1800 #4269  #1600
    if not path.exists("bitmaps"):
      	mkdir("bitmaps")

    #READ A .BOX FILE
    f = codecs.open(inputFileName, 'r', "utf-8-sig")
    if not f:
        print("Input file " + inputFileName + " not found!")
        exit(1)

    g = codecs.open("bitmaps/charinfo.utf8", 'w', "utf-8-sig")
    if not g:
        print("Unable to open output file bitmaps/charinfo.utf8")
        exit(1)

    linecount = 0
    while True:
        line = f.readline()
        if not line: break
        linecount = linecount + 1
        #print(line)
        c,x1,y1,x2,y2,pageNum = line.split()
        #print("x1="+x1+" y1="+y1+" x2="+x2+" y2="+y2)

        width = int(x2) - int(x1)
        height = int(y2) - int(y1)
        xoff = int(x1) - 1  # -1 is weird, does it work for all? TODO check
        yoff = inputHeight - 1 - int(y2)
        #print("width="+str(width)+" height="+str(height))

        outname = "bitmaps" +"/"+lib.lettername(c)+".tif"
        #print("outname="+outname)
        #cmdline = "convert gle-test2.testfont.tif -crop "+str(width)+"x"+str(height)+"+"+str(xoff)+"+"+str(yoff)+" "+outname
        #cmdline = "convert semicolon.tif -crop "+str(width)+"x"+str(height)+"+"+str(xoff)+"+"+str(yoff)+" "+outname
        cmdline = "convert aibitir.tif -crop "+str(width)+"x"+str(height)+"+"+str(xoff)+"+"+str(yoff)+" "+outname
        print("cmdline=["+cmdline+"]")

        p1 = Popen(cmdline, shell=True, stdout=PIPE, stderr=STDOUT)
        output = p1.communicate()[0].decode()
        if p1.returncode != 0:
            print("returncode="+str(p1.returncode))
            print(output)

        g.write(c + " " + str(width) + " " + str(height) + " " + "0" + "\n")  # 0 is just a default y-offset

    f.close
    g.close

    print("linecount = " + str(linecount))

if __name__ == '__main__':
    main()

