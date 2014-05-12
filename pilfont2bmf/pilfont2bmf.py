#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
from PIL import ImageFont
import unicodedata

FONTFILE = sys.argv[1]
DIRNAME = os.path.basename(FONTFILE).split('.')[0]

from string import digits, ascii_uppercase, ascii_lowercase, punctuation
extra_uppercase = u"ÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÔÖØÚÙÛÜÇÑÝŸÆÞ"
extra_lowercase = u"áàãâäéèêëíìîïóòõôöøúùûüçñýÿæþ"
extra_punctuation = u"¿¡ºª€£§½¨¶øßð«»¢“”¸µ·— "
# FIXME: en-dash, capital eth
chars = unicode(digits + ascii_uppercase + ascii_lowercase + punctuation + extra_uppercase + extra_lowercase + extra_punctuation)

charnames = {' ': '_space',}

font = ImageFont.load(FONTFILE)

if not os.path.exists(DIRNAME):
    os.mkdir(DIRNAME)

for char in chars:
    # fetch HTML entity name if applicable
    from htmlentitydefs import codepoint2name
    try:
        entityname = codepoint2name[ord(char)]
    except KeyError:
        entityname = None

    # digits and ascii lowercase get one-letter names, simple
    if char in ascii_lowercase + digits:
        filename = char
    # for punctuation, deal with it specifically with the unicode name
    elif char in punctuation:
        # FIXME: There are some entity names we could use instead,
        # but some are too short for clarity
        charname = '_' + unicodedata.name(char)
        filename = charname.lower().replace(' ', '').replace('-', '')
    # use Cap suffix for capitals (e.g. "aCap" for A)
    elif char in ascii_uppercase:
        filename = char.lower() + "Cap"
    # special case for accented characters
    elif char in extra_uppercase:
        if char in u"ÞÆ":
            # thorn and aelig need manual filename setting, otherwise they're overwritten
            # since they don't have capital names
            filename = entityname.lower() + "Cap"
        else:
            # split codepoint name, e.g. "agrave" into "aCapgrave"
            basechar = entityname[0]
            accentname = entityname[1:]
            filename = basechar.lower() + "Cap" + accentname
    elif char in extra_lowercase:
        try:
            filename = codepoint2name[ord(char)]
        except KeyError:
            print char
            raise
    elif char in charnames:
        filename = charnames[char]
    else:
        # we use the HTML entities definition for these
        try:
            filename = '_' + entityname
        except KeyError:
            filename = char
        except TypeError:
            print char
            raise

    txtfile = open(os.path.join(DIRNAME, "%s.txt" % filename), 'w')
    char = char.encode('cp1252')
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
