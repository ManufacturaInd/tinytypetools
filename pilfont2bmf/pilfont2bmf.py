#!/usr/bin/env python
import os
from PIL import ImageFont

from string import digits, ascii_uppercase, ascii_lowercase
chars = digits + ascii_uppercase + ascii_lowercase
print chars


FONTFILE = "6x10.pil"
DIRNAME = os.path.basename(FONTFILE).split('.')[0]
print DIRNAME
font = ImageFont.load(FONTFILE)

if not os.path.exists(DIRNAME):
    os.mkdir(DIRNAME)

for char in chars:
    txtfile = open(os.path.join(DIRNAME, "%s.txt" % char), 'w')
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
    print char
