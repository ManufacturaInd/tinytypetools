
Transpacing
===========

This script transplants spacing information from one font to another.

We wrote this while working on PropCourier Sans, a proportional version of the monospaced font NotCourier Sans. At first we re-adjusted the spacings by hand, but soon realized it would be handy to have a tool to get spacings from an existing libre font and apply them to another. Thus, the transpacing script was born.

Dependencies
------------

You need Fontforge compiled with Python support. 
Most distros will come with this out of the box through their package manager.

Supported formats
-----------------

Transpacing can work with any formats that Fontforge supports.

  http://en.wikipedia.org/wiki/FontForge#Supported_font_formats

Usage
-----

Transpacing requires three arguments:
- The font to get the spacings from
- The font to apply the spacings to (will not be modified)
- The resulting font file name

So, in order to take the spacings from dejavusans.ttf, apply them to notcourier.ttf and output propcourier.ttf, the command would be:

  transpacing dejavusans.ttf notcourier.ttf propcourier.ttf


License
-------

Transpacing is (c) 2012 [Manufactura Independente](http://manufacturaindependente.org) (Ana Carvalho & Ricardo Lafuente)
Licensed under the GPL v3 or later version.
