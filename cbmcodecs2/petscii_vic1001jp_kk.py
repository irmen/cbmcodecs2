"""
Python Character Mapping Codec petscii_vic1001jp_kk generated from 'mappings/petscii_vic1001jp_kk.txt' with gencodec.py.
"""

import codecs

### Codec APIs

class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]

class StreamWriter(Codec, codecs.StreamWriter):
    pass

class StreamReader(Codec, codecs.StreamReader):
    pass

### encodings module API

def getregentry():
    return codecs.CodecInfo(
        name='petscii_vic1001jp_kk',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


### Decoding Table

decoding_table = (
    '\ufffe'    #  0x00 -> UNDEFINED
    '\ufffe'    #  0x01 -> UNDEFINED
    '\ufffe'    #  0x02 -> UNDEFINED
    '\ufffe'    #  0x03 -> UNDEFINED
    '\ufffe'    #  0x04 -> UNDEFINED
    '\uf100'    #  0x05 -> WHITE COLOR SWITCH (CUS)
    '\ufffe'    #  0x06 -> UNDEFINED
    '\ufffe'    #  0x07 -> UNDEFINED
    '\ufffe'    #  0x08 -> UNDEFINED
    '\ufffe'    #  0x09 -> UNDEFINED
    '\ufffe'    #  0x0A -> UNDEFINED
    '\ufffe'    #  0x0B -> UNDEFINED
    '\ufffe'    #  0x0C -> UNDEFINED
    '\r'        #  0x0D -> CARRIAGE RETURN
    '\x0e'      #  0x0E -> SHIFT OUT
    '\ufffe'    #  0x0F -> UNDEFINED
    '\ufffe'    #  0x10 -> UNDEFINED
    '\uf11c'    #  0x11 -> CURSOR DOWN (CUS)
    '\uf11a'    #  0x12 -> REVERSE VIDEO ON (CUS)
    '\uf120'    #  0x13 -> HOME (CUS)
    '\x7f'      #  0x14 -> DELETE
    '\ufffe'    #  0x15 -> UNDEFINED
    '\ufffe'    #  0x16 -> UNDEFINED
    '\ufffe'    #  0x17 -> UNDEFINED
    '\ufffe'    #  0x18 -> UNDEFINED
    '\ufffe'    #  0x19 -> UNDEFINED
    '\ufffe'    #  0x1A -> UNDEFINED
    '\ufffe'    #  0x1B -> UNDEFINED
    '\uf101'    #  0x1C -> RED COLOR SWITCH (CUS)
    '\uf11d'    #  0x1D -> CURSOR RIGHT (CUS)
    '\uf102'    #  0x1E -> GREEN COLOR SWITCH (CUS)
    '\uf103'    #  0x1F -> BLUE COLOR SWITCH (CUS)
    ' '         #  0x20 -> SPACE
    '!'         #  0x21 -> EXCLAMATION MARK
    '"'         #  0x22 -> QUOTATION MARK
    '#'         #  0x23 -> NUMBER SIGN
    '$'         #  0x24 -> DOLLAR SIGN
    '%'         #  0x25 -> PERCENT SIGN
    '&'         #  0x26 -> AMPERSAND
    "'"         #  0x27 -> APOSTROPHE
    '('         #  0x28 -> LEFT PARENTHESIS
    ')'         #  0x29 -> RIGHT PARENTHESIS
    '*'         #  0x2A -> ASTERISK
    '+'         #  0x2B -> PLUS SIGN
    ','         #  0x2C -> COMMA
    '-'         #  0x2D -> HYPHEN-MINUS
    '.'         #  0x2E -> FULL STOP
    '/'         #  0x2F -> SOLIDUS
    '0'         #  0x30 -> DIGIT ZERO
    '1'         #  0x31 -> DIGIT ONE
    '2'         #  0x32 -> DIGIT TWO
    '3'         #  0x33 -> DIGIT THREE
    '4'         #  0x34 -> DIGIT FOUR
    '5'         #  0x35 -> DIGIT FIVE
    '6'         #  0x36 -> DIGIT SIX
    '7'         #  0x37 -> DIGIT SEVEN
    '8'         #  0x38 -> DIGIT EIGHT
    '9'         #  0x39 -> DIGIT NINE
    ':'         #  0x3A -> COLON
    ';'         #  0x3B -> SEMICOLON
    '<'         #  0x3C -> LESS-THAN SIGN
    '='         #  0x3D -> EQUALS SIGN
    '>'         #  0x3E -> GREATER-THAN SIGN
    '?'         #  0x3F -> QUESTION MARK
    '@'         #  0x40 -> COMMERCIAL AT
    'A'         #  0x41 -> LATIN CAPITAL LETTER A
    'B'         #  0x42 -> LATIN CAPITAL LETTER B
    'C'         #  0x43 -> LATIN CAPITAL LETTER C
    'D'         #  0x44 -> LATIN CAPITAL LETTER D
    'E'         #  0x45 -> LATIN CAPITAL LETTER E
    'F'         #  0x46 -> LATIN CAPITAL LETTER F
    'G'         #  0x47 -> LATIN CAPITAL LETTER G
    'H'         #  0x48 -> LATIN CAPITAL LETTER H
    'I'         #  0x49 -> LATIN CAPITAL LETTER I
    'J'         #  0x4A -> LATIN CAPITAL LETTER J
    'K'         #  0x4B -> LATIN CAPITAL LETTER K
    'L'         #  0x4C -> LATIN CAPITAL LETTER L
    'M'         #  0x4D -> LATIN CAPITAL LETTER M
    'N'         #  0x4E -> LATIN CAPITAL LETTER N
    'O'         #  0x4F -> LATIN CAPITAL LETTER O
    'P'         #  0x50 -> LATIN CAPITAL LETTER P
    'Q'         #  0x51 -> LATIN CAPITAL LETTER Q
    'R'         #  0x52 -> LATIN CAPITAL LETTER R
    'S'         #  0x53 -> LATIN CAPITAL LETTER S
    'T'         #  0x54 -> LATIN CAPITAL LETTER T
    'U'         #  0x55 -> LATIN CAPITAL LETTER U
    'V'         #  0x56 -> LATIN CAPITAL LETTER V
    'W'         #  0x57 -> LATIN CAPITAL LETTER W
    'X'         #  0x58 -> LATIN CAPITAL LETTER X
    'Y'         #  0x59 -> LATIN CAPITAL LETTER Y
    'Z'         #  0x5A -> LATIN CAPITAL LETTER Z
    '['         #  0x5B -> LEFT SQUARE BRACKET
    '\xa5'      #  0x5C -> YEN SIGN
    ']'         #  0x5D -> RIGHT SQUARE BRACKET
    '\u2191'    #  0x5E -> UPWARDS ARROW
    '\u2190'    #  0x5F -> LEFTWARDS ARROW
    '\u2500'    #  0x60 -> BOX DRAWINGS LIGHT HORIZONTAL
    '\u30c1'    #  0x61 -> KATAKANA LETTER TI
    '\u30c4'    #  0x62 -> KATAKANA LETTER TU
    '\u30c6'    #  0x63 -> KATAKANA LETTER TE
    '\u30c8'    #  0x64 -> KATAKANA LETTER TO
    '\u30ca'    #  0x65 -> KATAKANA LETTER NA
    '\u30cb'    #  0x66 -> KATAKANA LETTER NI
    '\u30cc'    #  0x67 -> KATAKANA LETTER NU
    '\u30cd'    #  0x68 -> KATAKANA LETTER NE
    '\u30ce'    #  0x69 -> KATAKANA LETTER NO
    '\u30cf'    #  0x6A -> KATAKANA LETTER HA
    '\u30d2'    #  0x6B -> KATAKANA LETTER HI
    '\u30d5'    #  0x6C -> KATAKANA LETTER HU
    '\u30d8'    #  0x6D -> KATAKANA LETTER HE
    '\u30db'    #  0x6E -> KATAKANA LETTER HO
    '\u30de'    #  0x6F -> KATAKANA LETTER MA
    '\u30df'    #  0x70 -> KATAKANA LETTER MI
    '\u30e0'    #  0x71 -> KATAKANA LETTER MU
    '\u30e1'    #  0x72 -> KATAKANA LETTER ME
    '\u30e2'    #  0x73 -> KATAKANA LETTER MO
    '\u30e4'    #  0x74 -> KATAKANA LETTER YA
    '\u30e6'    #  0x75 -> KATAKANA LETTER YU
    '\u30e8'    #  0x76 -> KATAKANA LETTER YO
    '\u30e9'    #  0x77 -> KATAKANA LETTER RA
    '\u30ea'    #  0x78 -> KATAKANA LETTER RI
    '\u30eb'    #  0x79 -> KATAKANA LETTER RU
    '\u30ec'    #  0x7A -> KATAKANA LETTER RE
    '\u253c'    #  0x7B -> BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    '\u30ef'    #  0x7C -> KATAKANA LETTER WA
    '\u2502'    #  0x7D -> BOX DRAWINGS LIGHT VERTICAL
    '\u03c0'    #  0x7E -> GREEK SMALL LETTER PI
    '\u30f2'    #  0x7F -> KATAKANA LETTER WO
    '\ufffe'    #  0x80 -> UNDEFINED
    '\ufffe'    #  0x81 -> UNDEFINED
    '\ufffe'    #  0x82 -> UNDEFINED
    '\ufffe'    #  0x83 -> UNDEFINED
    '\u259a'    #  0x84 -> QUADRANT UPPER LEFT AND LOWER RIGHT
    '\uf110'    #  0x85 -> FUNCTION KEY 1 (CUS)
    '\uf112'    #  0x86 -> FUNCTION KEY 3 (CUS)
    '\uf114'    #  0x87 -> FUNCTION KEY 5 (CUS)
    '\uf116'    #  0x88 -> FUNCTION KEY 7 (CUS)
    '\uf111'    #  0x89 -> FUNCTION KEY 2 (CUS)
    '\uf113'    #  0x8A -> FUNCTION KEY 4 (CUS)
    '\uf115'    #  0x8B -> FUNCTION KEY 6 (CUS)
    '\uf117'    #  0x8C -> FUNCTION KEY 8 (CUS)
    '\n'        #  0x8D -> LINE FEED
    '\x0f'      #  0x8E -> SHIFT IN
    '\ufffe'    #  0x8F -> UNDEFINED
    '\uf105'    #  0x90 -> BLACK COLOR SWITCH (CUS)
    '\uf11e'    #  0x91 -> CURSOR UP (CUS)
    '\uf11b'    #  0x92 -> REVERSE VIDEO OFF (CUS)
    '\x0c'      #  0x93 -> FORM FEED
    '\uf121'    #  0x94 -> INSERT (CUS)
    '\ufffe'    #  0x95 -> UNDEFINED
    '\ufffe'    #  0x96 -> UNDEFINED
    '\ufffe'    #  0x97 -> UNDEFINED
    '\ufffe'    #  0x98 -> UNDEFINED
    '\ufffe'    #  0x99 -> UNDEFINED
    '\ufffe'    #  0x9A -> UNDEFINED
    '\ufffe'    #  0x9B -> UNDEFINED
    '\uf10d'    #  0x9C -> PURPLE COLOR SWITCH (CUS)
    '\uf11d'    #  0x9D -> CURSOR LEFT (CUS)
    '\uf10e'    #  0x9E -> YELLOW COLOR SWITCH (CUS)
    '\uf10f'    #  0x9F -> CYAN COLOR SWITCH (CUS)
    '\xa0'      #  0xA0 -> NO-BREAK SPACE
    '\u309c'    #  0xA1 -> SEMI-VOICED SOUND MARK
    '\u30a4'    #  0xA2 -> KATAKANA LETTER I
    '\u30a6'    #  0xA3 -> KATAKANA LETTER U
    '\u30a8'    #  0xA4 -> KATAKANA LETTER E
    '\u30aa'    #  0xA5 -> KATAKANA LETTER O
    '\u30f2'    #  0xA6 -> KATAKANA LETTER WO
    '\u30ad'    #  0xA7 -> KATAKANA LETTER KI
    '\u30af'    #  0xA8 -> KATAKANA LETTER KU
    '\u30b1'    #  0xA9 -> KATAKANA LETTER KE
    '\u309b'    #  0xAA -> VOICED SOUND MARK
    '\u251c'    #  0xAB -> BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    '\u30b9'    #  0xAC -> KATAKANA LETTER SU
    '\u2514'    #  0xAD -> BOX DRAWINGS LIGHT UP AND RIGHT
    '\u2510'    #  0xAE -> BOX DRAWINGS LIGHT DOWN AND LEFT
    '\u309c'    #  0xAF -> SEMI-VOICED SOUND MARK
    '\u250c'    #  0xB0 -> BOX DRAWINGS LIGHT DOWN AND RIGHT
    '\u30a2'    #  0xB1 -> KATAKANA LETTER A
    '\u30a4'    #  0xB2 -> KATAKANA LETTER I
    '\u30a6'    #  0xB3 -> KATAKANA LETTER U
    '\u30a8'    #  0xB4 -> KATAKANA LETTER E
    '\u30aa'    #  0xB5 -> KATAKANA LETTER O
    '\u30ab'    #  0xB6 -> KATAKANA LETTER KA
    '\u30ad'    #  0xB7 -> KATAKANA LETTER KI
    '\u30af'    #  0xB8 -> KATAKANA LETTER KU
    '\u30b1'    #  0xB9 -> KATAKANA LETTER KE
    '\u30b3'    #  0xBA -> KATAKANA LETTER KO
    '\u30b5'    #  0xBB -> KATAKANA LETTER SA
    '\u30b7'    #  0xBC -> KATAKANA LETTER SI
    '\u30b9'    #  0xBD -> KATAKANA LETTER SU
    '\u30bb'    #  0xBE -> KATAKANA LETTER SE
    '\u30bd'    #  0xBF -> KATAKANA LETTER SO
    '\u30bf'    #  0xC0 -> KATAKANA LETTER TA
    '\u30c1'    #  0xC1 -> KATAKANA LETTER TI
    '\u30c4'    #  0xC2 -> KATAKANA LETTER TU
    '\u30c6'    #  0xC3 -> KATAKANA LETTER TE
    '\u30c8'    #  0xC4 -> KATAKANA LETTER TO
    '\u30ca'    #  0xC5 -> KATAKANA LETTER NA
    '\u30cb'    #  0xC6 -> KATAKANA LETTER NI
    '\u30cc'    #  0xC7 -> KATAKANA LETTER NU
    '\u30cd'    #  0xC8 -> KATAKANA LETTER NE
    '\u30ce'    #  0xC9 -> KATAKANA LETTER NO
    '\u30cf'    #  0xCA -> KATAKANA LETTER HA
    '\u30d2'    #  0xCB -> KATAKANA LETTER HI
    '\u30d5'    #  0xCC -> KATAKANA LETTER HU
    '\u30d8'    #  0xCD -> KATAKANA LETTER HE
    '\u30db'    #  0xCE -> KATAKANA LETTER HO
    '\u30de'    #  0xCF -> KATAKANA LETTER MA
    '\u30df'    #  0xD0 -> KATAKANA LETTER MI
    '\u30e0'    #  0xD1 -> KATAKANA LETTER MU
    '\u30e1'    #  0xD2 -> KATAKANA LETTER ME
    '\u30e2'    #  0xD3 -> KATAKANA LETTER MO
    '\u30e4'    #  0xD4 -> KATAKANA LETTER YA
    '\u30e6'    #  0xD5 -> KATAKANA LETTER YU
    '\u30e8'    #  0xD6 -> KATAKANA LETTER YO
    '\u30e9'    #  0xD7 -> KATAKANA LETTER RA
    '\u30ea'    #  0xD8 -> KATAKANA LETTER RI
    '\u30eb'    #  0xD9 -> KATAKANA LETTER RU
    '\u30ec'    #  0xDA -> KATAKANA LETTER RE
    '\u30ed'    #  0xDB -> KATAKANA LETTER RO
    '\u305c'    #  0xDC -> KATAKANA LETTER WA
    '\u30f3'    #  0xDD -> KATAKANA LETTER N
    '\u309b'    #  0xDE -> VOICED SOUND MARK
    '\u30f2'    #  0xDF -> KATAKANA LETTER WO
    '\u30c0'    #  0xE0 -> GREEK SMALL LETTER PI
    '\u253c'    #  0xE1 -> BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    '\u2502'    #  0xE2 -> BOX DRAWINGS LIGHT VERTICAL
    '\u30a6'    #  0xE3 -> KATAKANA LETTER U
    '\u30a8'    #  0xE4 -> KATAKANA LETTER E
    '\u30aa'    #  0xE5 -> KATAKANA LETTER O
    '\u30f2'    #  0xE6 -> KATAKANA LETTER WO
    '\u30ad'    #  0xE7 -> KATAKANA LETTER KI
    '\u30af'    #  0xE8 -> KATAKANA LETTER KU
    '\u30b1'    #  0xE9 -> KATAKANA LETTER KE
    '\u309b'    #  0xEA -> VOICED SOUND MARK
    '\u251c'    #  0xEB -> BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    '\u30b9'    #  0xEC -> KATAKANA LETTER SU
    '\u2514'    #  0xED -> BOX DRAWINGS LIGHT UP AND RIGHT
    '\u2510'    #  0xEE -> BOX DRAWINGS LIGHT DOWN AND LEFT
    '\u309c'    #  0xEF -> SEMI-VOICED SOUND MARK
    '\u250c'    #  0xF0 -> BOX DRAWINGS LIGHT DOWN AND RIGHT
    '\u2534'    #  0xF1 -> BOX DRAWINGS LIGHT UP AND HORIZONTAL
    '\u252c'    #  0xF2 -> BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    '\u2524'    #  0xF3 -> BOX DRAWINGS LIGHT VERTICAL AND LEFT
    '\u5e74'    #  0xF4 -> YEAR, PERSON'S AGE
    '\u6708'    #  0xF5 -> MONTH
    '\u65e5'    #  0xF6 -> DAY, DAYTIME
    '\u30bf'    #  0xF7 -> KATAKANA LETTER TA
    '\u30ed'    #  0xF8 -> KATAKANA LETTER RO
    '\u30f3'    #  0xF9 -> KATAKANA LETTER N
    '\u30b3'    #  0xFA -> KATAKANA LETTER KO
    '\u30b5'    #  0xFB -> KATAKANA LETTER SA
    '\u30b7'    #  0xFC -> KATAKANA LETTER SI
    '\u2518'    #  0xFD -> BOX DRAWINGS LIGHT UP AND LEFT
    '\u30bb'    #  0xFE -> KATAKANA LETTER SE
    '\u03c0'    #  0xFF -> GREEK SMALL LETTER PI
)

### Encoding table
encoding_table = codecs.charmap_build(decoding_table)

