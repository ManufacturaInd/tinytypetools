Transpacing
===========

This script transplants spacing information from one font to another.

We wrote this while working on PropCourier Sans, a proportional version of the monospaced font [NotCourier Sans](http://ospublish.constantvzw.org/foundry/notcouriersans/). At first we re-adjusted the spacings by hand, but soon realized it would be handy to have a tool to get spacings from an existing libre font and apply them to another. Thus, the transpacing script was born.

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

For example, in order to take the spacings from `dejavusans.ttf`, apply them to `notcourier.ttf` and output `propcourier.ttf`, the command would be:

    transpacing dejavusans.ttf notcourier.ttf propcourier.ttf
    
Font licensing issues
---------------------

In their EULAs, most proprietary fonts explicitly forbid redistribution of modified versions. Some might also restrict analysis of the source code. You are responsible for ensuring you are not violating the font's license by using this tool.

Or you can just use libre fonts and live without worries.

License
-------

Transpacing is (c) 2012 [Manufactura Independente](http://manufacturaindependente.org) (Ana Carvalho & Ricardo Lafuente)
Licensed under the GPL v3 or later version.
