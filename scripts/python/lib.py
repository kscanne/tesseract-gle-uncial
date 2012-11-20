# -*- coding: utf-8 -*-

#TODO this could probably just be a list.
digits = {
    "0" :  True,
    "1" :  True,
    "2" :  True,
    "3" :  True,
    "4" :  True,
    "5" :  True,
    "6" :  True,
    "7" :  True,
    "8" :  True,
    "9" :  True
}


#TODO this could probably just be a list.
lowercaseletters = {
    "a" :  True,
    "b" :  True,
    "c" :  True,
    "d" :  True,
    "e" :  True,
    "f" : True,
    "g" : True,
    "h" : True,
    "i" : True,
    "j" : True,
    "k" : True,
    "l" : True,
    "m" : True,
    "n" : True,
    "o" : True,
    "p" : True,
    "q" : True,
    "r" : True,
    "s" : True,
    "t" : True,
    "u" : True,
    "v" : True,
    "w" : True,
    "x" : True,
    "y" : True,
    "z" : True,
    "á" :  True,
    "é" :  True,
    "í" :  True,
    "ó" :  True,
    "ú" :  True,
    "ḃ" : True,
    "ċ" : True,
    "ḋ" : True,
    "ḟ" : True,
    "ġ" : True,
    "ṁ" : True,
    "ṗ" : True,
    "ṡ" : True,
    "ṫ" : True,
    "ɼ" : True,
    "ſ" : True,
    "ẛ" : True
}

alternatelowercaseletters = {
    "ɼ" : True,
    "ſ" : True,
    "ẛ" : True
}


de_punc = {
    ":" :  "colon",
    ";" :  "semicolon",
    "," :  "comma",
    "." :  "period",
    "?" :  "question",
    "!" :  "exclamation",
    "-" :  "dash",
    "'" :  "apostrophe",
    "’" :  "rightsinglequote",
    '"' :  "doublequote",
    '“' :  "leftdoublequote",
    '”' :  "rightdoublequote",
    '⁊' : "Tironian-et",
    '(' :  "leftparen",
    ')' :  "rightparen",
    '[' :  "leftbracket",
    ']' :  "righbracket",
}


de_accent = {
    "á" :  "a",
    "é" :  "e",
    "í" :  "i",
    "ó" :  "o",
    "ú" :  "u",
    "Á" :  "A",
    "É" :  "E",
    "Í" :  "I",
    "Ó" :  "O",
    "Ú" :  "U"
}

de_dot = {
    "ḃ" : "b",
    "ċ" : "c",
    "ḋ" : "d",
    "ḟ" : "f",
    "ġ" : "g",
    "ṁ" : "m",
    "ṗ" : "p",
    "ṡ" : "s",
    "ṫ" : "t",
    "Ḃ" : "B",
    "Ċ" : "C",
    "Ḋ" : "D",
    "Ḟ" : "F",
    "Ġ" : "G",
    "Ṁ" : "M",
    "Ṗ" : "P",
    "Ṡ" : "S",
    "Ṫ" : "T",
    "ẛ" : "ſ"
}

de_alternatelc = {
    "ɼ" : "r",
    "ſ" : "s",
    "ẛ" : "ṡ"
}



def isdigit(c):
    if c in digits:
        return True
    else:
        return False

def islowercase(c):
    if c in lowercaseletters:
        return True
    else:
        return False

def isalternatelowercase(c):
    if c in alternatelowercaseletters:
        return True
    else:
        return False

def punctuation(c):
    if c in de_punc:
        return True
    else:
        return False

def dotted(c):
    if c in de_dot:
        return True
    else:
        return False

def accented(c):
    if c in de_accent:
        return True
    else:
        return False

def lettername(c):
    letter = c
    diacritical = ""
    size = ""
    alternate = ""
    if isalternatelowercase(c):
        alternate = "-alt"
        c = de_alternatelc[c]
        letter = c
    if accented(c):
        diacritical = "-accent"
        letter = de_accent[c]
    if dotted(c):
        diacritical = "-dot"
        letter = de_dot[c]
    if punctuation(c):
        letter = de_punc[c]
    else:
        if islowercase(c):
            size = "-small"
        else:
            if not isdigit(c):
                size = "-caps"
    return letter+size+alternate+diacritical

