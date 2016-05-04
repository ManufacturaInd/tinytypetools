#!/usr/bin/env python

import sys, os
import fontforge
import optparse

# print 'ARGV      :', sys.argv[1:]
parser = optparse.OptionParser()
parser.add_option('-w', '--woff', 
                  dest="woff", 
                  action="store_true",
                  default=False,
                  help='Save in WOFF format (.woff)'
                  )
parser.add_option('-o', '--otf', 
                  dest="otf", 
                  action="store_true",
                  default=False,
                  help='Save in OpenType format (.otf)'
                  )
parser.add_option('-t', '--ttf', 
                  dest="ttf", 
                  action="store_true",
                  default=False,
                  help='Save in TrueType format (.ttf)'
                  )
parser.add_option('-s', '--svg', 
                  dest="svg", 
                  action="store_true",
                  default=False,
                  help='Save in SVG Font format (.svg)'
                  )
parser.add_option('-e', '--eot', 
                  dest="eot", 
                  action="store_true",
                  default=False,
                  help='Save in Embedded OpenType format (.eot)'
                  )
parser.add_option('-u', '--ufo', 
                  dest="ufo", 
                  action="store_true",
                  default=False,
                  help='Save in UFO format (.ufo)'
                  )
parser.add_option('--no-hinting',
                  dest="no_hinting",
                  action="store_true",
                  default=False,
                  help='Include TrueType hinting data'
                  )
parser.add_option('--unlink-reference',
                  dest="unlink_reference",
                  action="store_true",
                  default=False,
                  help='Unlink references in glyphs'
                  )
parser.add_option('--round-points',
                  dest="round_points",
                  action="store_true",
                  default=False,
                  help='"Round points to int values'
                  )
parser.add_option('--remove-overlap',
                  dest="remove_overlap",
                  action="store_true",
                  default=False,
                  help='Remove Overlap before generation'
                  )
parser.add_option('--add-extrema',
                  dest="add_extrema",
                  action="store_true",
                  default=False,
                  help='Add extrema'
                  )
parser.add_option('--simplify',
                  dest="simplify",
                  action="store_true",
                  default=False,
                  help='Simplify'
                  )
parser.add_option('--correct-directions',
                  dest="correct_directions",
                  action="store_true",
                  default=False,
                  help='Correct directions'
                  )

options, remainder = parser.parse_args()

if not len(remainder) == 1:
    print "Only one non-keyword argument allowed."
    sys.exit()

fontname = remainder[0]
font = fontforge.open(fontname)

d = os.path.dirname(os.path.abspath(fontname)) + '/'
filename = os.path.basename(fontname)
basename, ext = os.path.splitext(filename)

print d
print filename
print basename

woff_filename = d + basename + '.woff'
otf_filename = d + basename + '.otf'
ttf_filename = d + basename + '.ttf'
svg_filename = d + basename + '.svg'
eot_filename = d + basename + '.eot'
ufo_filename = d + basename + '.ufo'

if options.unlink_reference:
    print "Unlinking references..."
    for glyph in font.glyphs():
        glyph.unlinkRef()
if options.round_points:
    print "Rounding points to int values..."
    for glyph in font.glyphs():
        glyph.round()
if options.remove_overlap:
    print "Removing overlaps..."
    for glyph in font.glyphs():
        glyph.removeOverlap()
if options.add_extrema:
    print "Adding extrema..."
    for glyph in font.glyphs():
        glyph.addExtrema()
if options.simplify:
    print "Simplifying..."
    for glyph in font.glyphs():
        glyph.simplify()
if options.correct_directions:
    print "Correcting directions..."
    for glyph in font.glyphs():
        glyph.correctDirection()

# hard set flags to always 
# - output GPOS/GSUB tables if existing 
# - use short post table format
# - include dummy dsig
flags = ('opentype','short-post','dummy-dsig')
if options.no_hinting:
    print "Not including TrueType hinting"
    flags += ('omit-instructions',)

if options.woff:
    print woff_filename
    font.generate(woff_filename)
if options.otf:
    print otf_filename
    font.generate(otf_filename, flags = flags)
if options.ttf:
    print ttf_filename
    font.generate(ttf_filename, flags = flags)
if options.svg:
    print svg_filename
    font.generate(svg_filename)
if options.ufo:
    print ufo_filename
    font.generate(ufo_filename)
if options.eot:
    print eot_filename
    if options.ttf:
        cmd = 'ttf2eot < %s > %s' % (ttf_filename, eot_filename)
        os.system(cmd)
    else:
        font.generate(ttf_filename)
        cmd = 'ttf2eot < %s > %s' % (ttf_filename, eot_filename)
        os.system(cmd)
        os.remove(ttf_filename)
