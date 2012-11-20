# -*- coding: utf-8 -*-

import string,time
import codecs
from os import curdir, sep, mkdir, makedirs, path, linesep
from os.path import basename, splitext
from subprocess import Popen, PIPE, STDOUT
import argparse
import lib  # my local test lib.py


def readInputText():
    #READ A UTF8 input text FILE
    inputCharInfoName =  args.inputText
    f = codecs.open(inputCharInfoName, 'r', "utf-8-sig")
    if not f:
        print("Unable to open utf8 input text file " + inputCharInfoName)
        exit(1)
    text = f.read()
    f.close
    text = text.replace('\r','')   # get rid of windows carriage-returns in the input
    return text


def readCharInfo(charInfo):
    #READ A charinfo FILE
    inputCharInfoName =  args.bitmapsDir + '/charinfo.utf8'
    f = codecs.open(inputCharInfoName, 'r', "utf-8-sig")
    if not f:
        print("Input file " + inputCharInfoName + " not found!")
        exit(1)
    linecount = 0
    while True:
        line = f.readline()
        if not line: break
        linecount = linecount + 1
        #print(line)
        c,w,h,y = line.split()
        width = int(w)
        height = int(h)
        yoffset = int(y)
        charInfo[c] = width, height, yoffset
        width, height, yoffset = charInfo[c]
        #print(lib.lettername(c) + " " + str(width) + " " + str(height) + " " + str(yoffset))
    f.close
    #print("linecount = " + str(linecount))

yoffsets = {
    "f" : -20,
    "ḟ" : -20,
    "g" : -20,
    "ġ" : -20,
    "F" : -20,
    "Ḟ" : -20,
    "G" : -20,
    "Ġ" : -20,
    "p" : -20,
    "ṗ" : -20,
    "P" : -20,
    "Ṗ" : -20,
    ":" :  0,
    ";" :  -18,
    "," :  -18,
    "." :  0,
    "?" :  0,
    "!" :  0,
    "-" :  20,
    "'" :  40,
    "’" :  40,
    '"' :  40,
    '“' :  40,
    '”' :  40,
    'ɼ' : -20,
    'ſ' : -20,
    'ẛ' : -20,
    '⁊' : -20,
    '(' :  -20,
    ')' :  -20,
    '[' :  -20,
    ']' :  -20
}

def getYoff(c):
    if c in yoffsets:
        return yoffsets[c]
    else:
        return 0


def main():
    print("Hello!")

    charInfo = {}

    readCharInfo(charInfo)


    inputText0 = "An bhfuil tusa ag laḃairt liomsa?\nIs mise an t-aon duine atá anseo.\n"

    inputText1 = """
  Ḃí bradán ann fadó.  Bradán feasa a ḃí
ann.  An ċéad duine a ḃlaisfeaḋ é beaḋ
fios aige.
  Ṁaraiġ an draoi an bradán agus ċuir sé
os cionn na tine é ċun é róstaḋ.
  Ṫáinig Fionn mac Cuṁaill an treo.  Ní
raiḃ i ḃFionn aċ buaċaill óg an uair sin.
  “ Tar i leiṫ, a ḃuaċaill,” arsa an draoi
leis.  “ Taḃair aire don ḃradán so faid a
ḃead féin ag dul ċun an tobair.  Ar do ḃás
ná dóiġ é.”
13
    """

    inputText2 = """
aeiou.
áéíóú:
bcdfgmpst?
ḃċḋḟġṁṗṡṫ-
lnrh’
1234567890,
AEIOU!
ÁÉÍÓÚ
BCDFGMPST
ḂĊḊḞĠṀṖṠṪ
“LNRH”
    """

    inputText3 = """
aeiou.
áéíóú:
bcdfgmpst?
ḃċḋḟġṁṗṡṫ-
lnrh’
1234567890,
AEIOU!
ÁÉÍÓÚ
BCDFGMPST
ḂĊḊḞĠṀṖṠṪ
“LNRH”
I ’ould lice to put some
sentences in.  This is someuhat
lice mi other font-generated tecst.
It uorcs OC maibe? 
Cén fáṫ naċ ḃfuil sé seo 
go maiṫ?
Línte gearra, sin an rud, 
a ṁic!  Ná lig sinn i
gCaṫú? Aċ saor sinn ó olc.
Níl ionamsa aċ amadán:
Naċ ndéanfaiḋ sé sin an cúis?
Laḃair anois nó bígí ciúin 
go deo na ndeoir.  Mise Éire.
Sine mé ná an Ċailleaċ Ḃéarra.
    """
    inputText4 = """
an ġairdín. Ḃíoḋ bláṫanna bána ar an
gcrann san earraċ. Ḃíoḋ silíní dearga air
sa tsaṁraḋ.
  “ Trua gan crann silín agam im ġairdín
beag féin !” arsa Síle léi féin.
  Ḃí lon duḃ ina ṡeasaṁ ar an gclaí. Níl
ḟios agam ar ṫuig an lon duḃ an rud a
dúirt sí.  B’ḟéidir gur ṫuig agus b’ḟéidir
nár ṫuig.  Aċ an lá ina ḋiaiḋ san ṫáinig sé
agus silín ina ġob aige.
  Ṡeas an lon duḃ ar an gclaí agus d’iṫ sé
an silín.  Ṫit cloċ an tsiín anuas i ngairdín
ṠíLe.  D’ḟan an ċloċ sa ċré nó go dtáinig
an t-earraċ.
  Lá breá earraiġ ċonaic Síle planda beag
glas ag fás ina gairdín.  Crann beag silín
a ḃí ann.  D’ḟás an crann beag nó go raiḃ
sé ina ċrann ṁór.
  Ḃíoḋ bláṫanna bána ar an gcrann san
earraċ.  Ḃíoḋ silíní dearga air sa tsaṁraḋ.
  Ḃí áṫas ar Ṡíle.
  “Is é mo ċrann silín féin an crann is
fearr in Éirinn,” adeireaḋ sí.
II
    """
    inputText5 = """
AN CIRCÍN RUA
Fuair an Circín rua cúpla gráinne coirce,
lá.
  “ Cé ċuirfiḋ an coirce seo ? ” ar sise.
  “ Ní ċuirfead-sa é,’’ arsa an madra.
  “ Ní ċuirfead-sa é,” arsa an cat.
  “ Ní ċuirfead-sa é,” arsa an ṁuc.
  “ Cuirfead féin é,” arsa an Circín rua.
  Scríob sí an talaṁ, agus ċuir sí an coirce
sa ġort. D’ḟás an coirce nó go raiḃ sé
aibiḋ.
  “Cé ḃainfiḋ an coirce seo ?” arsa an
Circín rua.
  “ Ní ḃainfead-sa é,” arsa an madra.
  “ Ní ḃainfead-sa é,’’ arsa an cat.
  “ Ní ḃainfead-sa é,” arsa an ṁuc.
  “ Bainfead féin é,’’ arsa an Circín rua.
Ḃain sí an coirce lena gob.
  “ Cé ḃuailfiḋ an coirce seo ? ’’ ar sise.
  “ Ní ḃuailfead-sa é,” arsa an madra.
  “ Ní ḃuailfead-sa é,’’ arsa an cat.
  “ Ní ḃuailfead-sa é,” arsa -an ṁuc.
  “ Buailfead féin é,’’ arsa an Circín rua.
Ḃuail sí an coirce lena ḋá sciaṫán.
  “ Cé ṁeilfiḋ an coirce seo ? ” ar sise.
  “ Ní ṁeilfead-sa é,” arsa an madra.
4
    """


    #inputText =  inputText5
    inputText = readInputText()

    trainingMode = args.training


    #outputName = "page5"
    if args.outputBase:
        outputName == args.outputBase
    else:
        outputName = splitext(basename(args.inputText))[0]  # basename makes it safer so you don't clobber something elsewhere with output

    #outputBoxPage = 5
    outputBoxPage = args.boxPageNumber



    g = codecs.open(outputName+".box", 'w', "utf-8-sig")
    if not g:
        print("Cannot write output file " + outputName + ".tif")
        exit(1)

    totalWidth = 0
    totalHeight = 0
    spaceWidth = 50
    interLetterWidth = 7  #20 is nicely spaced for training?
    if trainingMode:
        interLetterWidth *= 3  # increase spacing 
    leftMargin = 360
    rightMargin = 360
    topMargin = 0  # TODO increase this later
    interLineHeight = 140
    justifiedSpaceLimit = 90  # TODO this will need a tweak
    lines = {}
    lineNumber = 0

    # handle fixed-width justified text
    #justifiedWidth = 2985  #kind of an odd number, but ok

    justifiedWidth = args.justifiedWidth   # defaults to 2985 the size of the Gort an Oir book
    
    textWidth = justifiedWidth - leftMargin - rightMargin

    for myPass in [1, 2]:
        print("pass="+str(myPass)) # DEBUG
        x = leftMargin
        y = topMargin
        lineNumber = 0
        if myPass == 1:
            spaceCount = 0
        if myPass == 2:
            # create blank page big enough
            cmdline = "convert -monochrome -density 600 -size " + str(justifiedWidth) + "x" + str(totalHeight) + " xc:white " + outputName + ".tif"  
            print("cmdline=["+cmdline+"]")
            p1 = Popen(cmdline, shell=True, stdout=PIPE, stderr=STDOUT)
            output = p1.communicate()[0].decode()
            if p1.returncode != 0:
                print("returncode="+str(p1.returncode))
                print(output)

        for c in inputText:
            if c == "\n":
                if myPass == 1:
                    lines[lineNumber] = x - leftMargin, spaceCount
                    if totalWidth < x:
                        totalWidth = x
                    totalHeight = y
                spaceCount = 0
                x = leftMargin
                y += interLineHeight
                lineNumber += 1
            else:
                if c == " ":
                    spaceCount += 1
                    if myPass == 2:
                        lineWidth, numSpaces = lines[lineNumber]  # TODO move this out of the line loop?
                        justifiedSpace = int((textWidth - lineWidth)/numSpaces)   # TODO this is approx right
                        if justifiedSpace < justifiedSpaceLimit:
                            x += justifiedSpace
                        else:
                            x += spaceWidth
                else:
                    width, height, yoffset = charInfo[c]
                    if myPass == 2:
                        # print the letter
                        bitmapName = args.bitmapsDir +"/"+lib.lettername(c)+".tif"
                        cmdline = "convert " +  outputName + ".tif " + bitmapName + " -geometry +" + str(x) + "+" + str(y + 110 - height - getYoff(c)) + " -composite " +  outputName + ".tif"
                        print("cmdline=["+cmdline+"]")
                        p1 = Popen(cmdline, shell=True, stdout=PIPE, stderr=STDOUT)
                        output = p1.communicate()[0].decode()
                        if p1.returncode != 0:
                            print("returncode="+str(p1.returncode))
                            print(output)
                        # write the .box file row
                        x1 = x
                        x2 = x + width
                        #   subtract y from totalHeight 
                        #   since .box files have origin at lower left corner
                        y1 = totalHeight - (y + 110 - getYoff(c))
                        y2 = y1 + height
                        g.write(c + " " + str(x1) + " " +str( y1) + " " + str(x2) + " " + str(y2) + " " + str(outputBoxPage) + "\n")
                        # Note - the boxes look PERFECT, 
                        #  but may need to shift top and left border down and right by one pixel
                        #  to match the lame boxes that Tess makes?  For now, trying it without a hack.
                        #  Note that because the makeBitmaps.py adds 1 as a hack to 
                        #  adjust for it so we do grab the entire letter image?
                    x += width
                x += interLetterWidth

        if myPass == 1:
            if x != leftMargin:  # means we have not already processed the info with newline
                if totalWidth < x:
                    totalWidth = x
                lines[lineNumber] = x - leftMargin, spaceCount
                y += interLineHeight # account for the last full line
            totalHeight = y
            totalWidth += rightMargin
            print("totalWidth = " + str(totalWidth) + "  totalHeight = " + str(totalHeight))

    g.close    # close .box file

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate output .tif and .box from input text and bitmaps font')
    #parser.add_argument('-i', '--inputText', required=True)
    #parser.add_argument('--version', action='version', version='%(prog)s 2.0')
    #type=file or type=argparse.FileType('w'). would be cool for inputText, but would not handle the utf8 option probably.
    # trick for debugging or just cool parsing capability: parser.parse_args('1 2 3 4 --sum'.split())
    parser.add_argument('inputText')
    parser.add_argument('-j', '--justifiedWidth', type=int, default=2985, help='justified page width in pixels, default 2985')
    parser.add_argument('-o', '--outputBase', help='defaults to inputText with no extension')
    parser.add_argument('-t', '--training', action='store_true')
    parser.add_argument('-p', '--boxPageNumber', type=int, default=0, help='page number used in box file output, default: 0')
    parser.add_argument('-b', '--bitmapsDir', default="./bitmaps", help='location of bitmaps directory, default: bitmaps')
    args = parser.parse_args()  # since no args string is specified, it uses the sys.argv
    # you can do: mydict=vars(args) to create a dictionary from your arguments
    # more: print args.accumulate(args.integers)   {this assumes your args and a list of integers}
    # simply access args.{argumentName} e.g. args.inputText or args.training or args.outputBase
    main()

