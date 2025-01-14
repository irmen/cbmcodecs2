"""CBM "encodings" Package

Encodings for PETSCII generated with gencodec.py from the Unicode mappings
defined by Linus Walleij, see
http://www.df.lth.se/~triad/krad/recode/petscii.html

The screencode mappings were written by hand by Irmen de Jong.

The following encodings are defined by this package:

petscii_c64en_lc - Mixed-case mapping used by the Commodore 64
petscii_c64en_uc - Upper-case/graphics mapping used by the Commodore 64
petscii_vic1001jp_gr - Latin upper-case/graphics character set used by the VIC-1001
petscii_vic1001jp_kk - Latin upper-case/katakana character set used by the VIC-1001
petscii_vic20en_lc - Mixed-case mapping used by the Commodore VIC-20
petscii_vic20en_uc - Upper-case/graphics mapping used by the VIC-20
screencode_c64_lc - Mixed-case mapping to screencodes (POKE) used by the Commodore 64 and Vic20
screencode_c64_uc - Upper-case/graphics mapping to screencodes (POKE) used by the Commodore 64 and Vic20
"""
import codecs

from . import petscii_c64en_lc
from . import petscii_c64en_uc
from . import petscii_vic1001jp_gr
from . import petscii_vic1001jp_kk
from . import petscii_vic20en_lc
from . import petscii_vic20en_uc
from . import screencode_c64_lc
from . import screencode_c64_uc

__version__ = '1.3'
__all__ = []

petscii_codecs = {
    # backwards compatibility encoding names:
    'petscii-c64en-lc': petscii_c64en_lc.getregentry(),
    'petscii-c64en-uc': petscii_c64en_uc.getregentry(),
    'petscii-vic1001jp-gr': petscii_vic1001jp_gr.getregentry(),
    'petscii-vic1001jp-kk': petscii_vic1001jp_kk.getregentry(),
    'petscii-vic20en-lc': petscii_vic20en_lc.getregentry(),
    'petscii-vic20en-uc': petscii_vic20en_uc.getregentry(),
    'screencode-c64-lc': screencode_c64_lc.getregentry(),
    'screencode-c64-uc': screencode_c64_uc.getregentry(),
    # normalized encoding names since python 3.9:
    'petscii_c64en_lc': petscii_c64en_lc.getregentry(),
    'petscii_c64en_uc': petscii_c64en_uc.getregentry(),
    'petscii_vic1001jp_gr': petscii_vic1001jp_gr.getregentry(),
    'petscii_vic1001jp_kk': petscii_vic1001jp_kk.getregentry(),
    'petscii_vic20en_lc': petscii_vic20en_lc.getregentry(),
    'petscii_vic20en_uc': petscii_vic20en_uc.getregentry(),
    'screencode_c64_lc': screencode_c64_lc.getregentry(),
    'screencode_c64_uc': screencode_c64_uc.getregentry()
}


def search_fn(encoding):
    return petscii_codecs.get(encoding, None)


codecs.register(search_fn)
