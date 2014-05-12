#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from PIL import ImageFont
import unicodedata
from htmlentitydefs import codepoint2name

from string import digits, ascii_uppercase, ascii_lowercase, punctuation
chars = unicode(digits + ascii_uppercase + ascii_lowercase + punctuation)

# FIXME: Add PT relevant characters (pillow doesn't output them properly)
# chars += u"áàãâéèêíìóòõôúùçÁÀÃÂÉÈÊÍÌÓÒÕÔÚÙÇ"

print chars


FONTFILE = "6x10.pil"
DIRNAME = os.path.basename(FONTFILE).split('.')[0]
font = ImageFont.load(FONTFILE)

if not os.path.exists(DIRNAME):
    os.mkdir(DIRNAME)

for char in chars:
    # use ascii for the file name
    # for punctuation, deal with it specifically with the unicode name
    if char in punctuation:
        charname = '_' + unicodedata.name(char)
        filename = charname.lower().replace(' ', '').replace('-', '')
    # use Cap suffix for capitals (e.g. "aCap" for A)
    elif char in ascii_uppercase:
        filename = char.lower() + "Cap"
    else:
        # we use the HTML entities definition for these
        try:
            filename = '_' + codepoint2name[ord(char)]
        except KeyError:
            filename = char

    print filename + ".txt"
    txtfile = open(os.path.join(DIRNAME, "%s.txt" % filename), 'w')
    char = char.encode('utf-8')
    lines = []
    w,h = font.getsize(char)
    im = font.getmask(char)
    for y in xrange(h):
        line = ""
        for x in xrange(w):
            if im.getpixel((x,y)):
                line += "#"
            else:
                line += "."
        lines.append(line + "\n")
    txtfile.writelines(lines)
    txtfile.close()
