#!/usr/bin/env python

from PIL import ImageFont

FONTFILE = "6x10.pil"

font = ImageFont.load(FONTFILE)

w,h = font.getsize('a')
im = font.getmask('a')
for y in xrange(h):
    line = ""
    for x in xrange(w):
        if im.getpixel((x,y)):
            line += "#"
        else:
            line += "."
    print line
