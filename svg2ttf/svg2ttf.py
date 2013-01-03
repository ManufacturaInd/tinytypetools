# svg2ttf v0.1
# 
# copyleft 2008-2009 ricardo lafuente
#
# generate a .ttf file from a set of .svg files with the lowercase alphabet
#
# before running this script, create a blank font file in Fontforge
# (make a New font and save it as it is) and change the BLANK_FONT location
# 
# you might also want to edit the metadata (title, license, etc.) before 
# saving it, or just edit the blank.sfd file afterwards
#
# finally, change the LETTERS_DIR value to the folder where your .svg 
# files are; they ought to be named [a-z].svg

LETTERS_DIR = '~/Desktop/svgletters/'
BLANK_FONT = '~/Desktop/blank.sfd'

letters = 'abcdefghijklmnopqrstuvwxyz'

# right-o, here we go
import fontforge

# open a blank font template
# TODO: dynamically generate the space character
font = fontforge.open(BLANK_FONT)

for letter in letters:
    # make new glyph
    font.createMappedChar(letter)
    # import outline file
    # notice that font[glyphname] returns the appropriate glyph
    # fontforge is awesome :o)
    font[letter].importOutlines(LETTERS_DIR + '/' + letter + '.svg')
    # same spacing for each letter, this is a hack after all
    font[letter].left_side_bearing = 15
    font[letter].right_side_bearing = 15
    # generate TrueType hints
    # font[letter].autoInstr()

# create the output truetype file
font.generate('output.ttf')
