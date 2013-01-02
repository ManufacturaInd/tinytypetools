
FFFilters
=========

This is a set of scripts that apply simple Fontforge commands to all glyphs in a font.

Currently, the available operations are:

  * Shadow
  * Wireframe
  * Outline
  * Inline
  * Interpolation

Dependencies
------------

You need Fontforge compiled with Python support. 
Most distros will come with this out of the box through their package manager.

Supported formats
-----------------

FFfilters can be applied to fonts in any format that Fontforge supports.

  http://en.wikipedia.org/wiki/FontForge#Supported_font_formats


Usage
-----

Each filter requires specific parameters. The first parameter should be the input file; the output file will be based on the name of the input file and the filter used. Here's the available scripts, their expected parameters and some example usage.


fffshadow.pe
-----------

This applies a 3D shadow effect along with an outline.

Parameters:
  * Input file name
  * Output file name
  * Shadow angle
  * Outline width
  * Shadow depth

Example:

    fffshadow.pe Douar.sfd Douar-Shadow.ttf 45 30 50 


fffwireframe.pe
---------------

This applies an outline version of the shadow effect.

Parameters:
  * Input file name
  * Output file name
  * Shadow angle
  * Outline width
  * Shadow depth

Example:

    fffshadow.pe Douar.sfd Douar-Wireframe.ttf 85 20 35 


fffinline.pe
------------

This applies an inline fill along with an outline.

Parameters:
  * Input file name
  * Output file name
  * Outline width
  * Gap

Example:

    fffinline.pe Douar.sfd Douar-Inline.ttf 20 40


fffoutline.pe
-----------

This applies an inline fill along with an outline.

Parameters:
  * Input file name
  * Output file name
  * Outline width

Example:
 
    fffoutline.pe Douar.sfd Douar-Inline.ttf 25


fffinterpolate.pe
-----------

This is an experimental script which will only work if both input files are ready for interpolation; otherwise, it greets you with a surge of Fontforge errors. If you can get this to work with whichever fonts, we'd love to know :-)

Parameters:
  * First file name
  * Second file name
  * Output file name
  * Percentage (50% is a halfway interpolation, negative or over 100% values apply extrapolation)

Example:

    fffinterpolate.pe Douar.sfd Douar-Bold.sfd Douar-Semibold.ttf 50


License
-------

All the FFfilters are (c) 2012 [Manufactura Independente](http://manufacturaindependente.org) (Ana Carvalho & Ricardo Lafuente)
Licensed under the GPL v3 or later version.
