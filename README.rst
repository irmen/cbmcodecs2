===========================================================================
cbmcodecs2 - Python encodings for handling PETSCII and C64 Screencode text.
===========================================================================

Introduction
============

The cbmcodecs2 package provides a number of encodings for handling text from
Commodore 8-bit systems. Much of the credit for this package must go to
Linus Walleij of Triad, as these codecs were built from his PETSCII to Unicode
mappings which can be found at http://www.df.lth.se/~triad/krad/recode/petscii.html
The screencodes codec was created by hand later and borrows from them.

This package is an updated fork of the original cbmcodecs package, which now seems unmaintained.


Installation
============

Easiest is to install the latest version directly `from Pypi <https://pypi.org/project/cbmcodecs2/>`_ :

``pip install cbmcodecs2``


Usage
=====

Currently there are four codecs defined for variations of the PETSCII encoding:

petscii_c64en_lc
    The English version of the Commodore 64 mixed-case character set

petscii_c64en_uc
    The English version of the Commodore 64 upper-case/graphics character set

petscii_vic1001jp_gr
    The Japanese version of the VIC-1001 Latin upper-case/graphics character set

petscii_vic1001jp_kk
    The Japanese version of the VIC-1001 Latin upper-case/katakana character set

petscii_vic20en_lc
    The English version of the VIC-20 mixed-case character set

petscii_vic20en_uc
    The English version of the VIC-20 upper-case/graphics character set


There are two codecs defined to handle the Screencode (POKE) encoding:

screencode_c64_lc
    Mixed-case mapping to screencodes (POKE) used by the Commodore 64 and Vic20

screencode_c64_uc
    Upper-case/graphics mapping to screencodes (POKE) used by the Commodore 64 and Vic20


Simply import the cbmcodecs2 package and you will then be able to use them as
with any of the encodings from the standard library::

    import cbmcodecs2


    with open('file.seq', encoding='petscii_c64en_lc') as f:
        for line in f:
            print(line)


Python Version Note
===================

Currently only Python 3 is supported (tested on 3.5+). May or may not work on older versions.


License
=======

As with the original PETSCII to Unicode mapping files, the cbmcodecs2 package
is Licensed under the GNU GPL Version 2, see the ``LICENSE.txt`` file for the
full text.


Unicode symbols used
====================
Aside from the regular alphanumerics and symbols, the unicode mapping uses the
following unicode block drawing and other symbols to mimic a bunch of PETSCII characters:

£ π ✓ ← ↑ ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼ ╭ ╮ ╯ ╰
╱ ╲ ╳ ▁ ▂ ▃ ▄ ▌ ▍ ▎ ▏ ▒ ▔ ▕ ▖ ▗ ▘ ▚ ▝
○ ● ◤ ◥ ♠ ♣ ♥ ♦


Credits
=======

Linus Walleij - Original C64 and VIC-20 mappings

Dan Johnson - Translation of C64 & VIC-20 mappings to python codecs

Irmen de Jong - Screencode mappings, bug fixes and unit tests. Updated to cbmcodecs2 package.
