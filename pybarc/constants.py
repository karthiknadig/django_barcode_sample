
SUPPORTED_CODING = {
    'EAN-13',
    'EAN-8'
}

# EAN-13 structure
# first digit: ((left 6 digits), (right 6 digits))
# L = Odd party pattern
# G = Even parity pattern
# R = Right pattern
EAN_13_STRUCTURE = {
    0: (('L', 'L', 'L', 'L', 'L', 'L'), ('R', 'R', 'R', 'R', 'R', 'R')),
    1: (('L', 'L', 'G', 'L', 'G', 'G'), ('R', 'R', 'R', 'R', 'R', 'R')),
    2: (('L', 'L', 'G', 'G', 'L', 'G'), ('R', 'R', 'R', 'R', 'R', 'R')),
    3: (('L', 'L', 'G', 'G', 'G', 'L'), ('R', 'R', 'R', 'R', 'R', 'R')),
    4: (('L', 'G', 'L', 'L', 'G', 'G'), ('R', 'R', 'R', 'R', 'R', 'R')),
    5: (('L', 'G', 'G', 'L', 'L', 'G'), ('R', 'R', 'R', 'R', 'R', 'R')),
    6: (('L', 'G', 'G', 'G', 'L', 'L'), ('R', 'R', 'R', 'R', 'R', 'R')),
    7: (('L', 'G', 'L', 'G', 'L', 'G'), ('R', 'R', 'R', 'R', 'R', 'R')),
    8: (('L', 'G', 'L', 'G', 'G', 'L'), ('R', 'R', 'R', 'R', 'R', 'R')),
    9: (('L', 'G', 'G', 'L', 'G', 'L'), ('R', 'R', 'R', 'R', 'R', 'R')),
}
EAN_13_LENGTH = 13
EAN_13_CHECK_DIGIT_POSITION = 12

EAN_8_STRUCTURE = (('L', 'L', 'L', 'L'), ('R', 'R', 'R', 'R'))
EAN_8_LENGTH = 8
EAN_8_CHECK_DIGIT_POSITION = 7

EAN_START = (1, 0, 1)
EAN_MIDDLE = (0, 1, 0, 1, 0)
EAN_END = (1, 0, 1)
EAN_L_CODE = {
    0: (0, 0, 0, 1, 1, 0, 1),
    1: (0, 0, 1, 1, 0, 0, 1),
    2: (0, 0, 1, 0, 0, 1, 1),
    3: (0, 1, 1, 1, 1, 0, 1),
    4: (0, 1, 0, 0, 0, 1, 1),
    5: (0, 1, 1, 0, 0, 0, 1),
    6: (0, 1, 0, 1, 1, 1, 1),
    7: (0, 1, 1, 1, 0, 1, 1),
    8: (0, 1, 1, 0, 1, 1, 1),
    9: (0, 0, 0, 1, 0, 1, 1),
}

EAN_G_CODE = {
    0: (0, 1, 0, 0, 1, 1, 1),
    1: (0, 1, 1, 0, 0, 1, 1),
    2: (0, 0, 1, 1, 0, 1, 1),
    3: (0, 1, 0, 0, 0, 0, 1),
    4: (0, 0, 1, 1, 1, 0, 1),
    5: (0, 1, 1, 1, 0, 0, 1),
    6: (0, 0, 0, 0, 1, 0, 1),
    7: (0, 0, 1, 0, 0, 0, 1),
    8: (0, 0, 0, 1, 0, 0, 1),
    9: (0, 0, 1, 0, 1, 1, 1),
}

EAN_R_CODE = {
    0: (1, 1, 1, 0, 0, 1, 0),
    1: (1, 1, 0, 0, 1, 1, 0),
    2: (1, 1, 0, 1, 1, 0, 0),
    3: (1, 0, 0, 0, 0, 1, 0),
    4: (1, 0, 1, 1, 1, 0, 0),
    5: (1, 0, 0, 1, 1, 1, 0),
    6: (1, 0, 1, 0, 0, 0, 0),
    7: (1, 0, 0, 0, 1, 0, 0),
    8: (1, 0, 0, 1, 0, 0, 0),
    9: (1, 1, 1, 0, 1, 0, 0),
}

EAN_WEIGHTS = (3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3)


# UPC-A Constants
UPC_A_START = (1, 0, 1)
UPC_A_MIDDLE = (0, 1, 0, 1, 0)
UPC_A_END = (1, 0, 1)
UPC_A_QUIET_ZONE = (0, 0, 0, 0, 0, 0, 0, 0, 0)
UPC_A_MODULE_WIDTH = '0.33mm'
UPC_A_SYMBOL_HEIGHT = '25.9mm'
UPC_A_GUARD_HEIGHT = '27.55mm'

# Note this is same as EAN_L_CODE
UPC_A_L_CODE = {
    0: (0, 0, 0, 1, 1, 0, 1),
    1: (0, 0, 1, 1, 0, 0, 1),
    2: (0, 0, 1, 0, 0, 1, 1),
    3: (0, 1, 1, 1, 1, 0, 1),
    4: (0, 1, 0, 0, 0, 1, 1),
    5: (0, 1, 1, 0, 0, 0, 1),
    6: (0, 1, 0, 1, 1, 1, 1),
    7: (0, 1, 1, 1, 0, 1, 1),
    8: (0, 1, 1, 0, 1, 1, 1),
    9: (0, 0, 0, 1, 0, 1, 1),
}

# Note this is same as EAN_R_CODE
UPC_A_R_CODE = {
    0: (1, 1, 1, 0, 0, 1, 0),
    1: (1, 1, 0, 0, 1, 1, 0),
    2: (1, 1, 0, 1, 1, 0, 0),
    3: (1, 0, 0, 0, 0, 1, 0),
    4: (1, 0, 1, 1, 1, 0, 0),
    5: (1, 0, 0, 1, 1, 1, 0),
    6: (1, 0, 1, 0, 0, 0, 0),
    7: (1, 0, 0, 0, 1, 0, 0),
    8: (1, 0, 0, 1, 0, 0, 0),
    9: (1, 1, 1, 0, 1, 0, 0),
}

TAB_TO_SPACE = 4


EAN_STYLE_BARCODE_ONLY = 0
EAN_STYLE_BARCODE_WITH_NUMBERS_BELOW = 1
EAN_STYLE_BARCODE_WITH_NUMBERS_ABOVE = 2
EAN_STYLE_PRODUCT_CODE = 3
EAN_STYLE_BOOK_STYLE = 4

# (left-buffer, start, left, mid, right, end, right-buffer)
EAN_STYLES_MODULE_HEIGHTS = {
    EAN_STYLE_BARCODE_ONLY: ('100%', '100%', '100%', '100%', '100%', '100%', '100%'),
    EAN_STYLE_BARCODE_WITH_NUMBERS_BELOW: ('85%', '85%', '85%', '85%', '85%', '85%', '85%'),
    EAN_STYLE_BARCODE_WITH_NUMBERS_ABOVE: ('85%', '85%', '85%', '85%', '85%', '85%', '85%'),
    EAN_STYLE_PRODUCT_CODE: ('85%', '100%', '85%', '100%', '85%', '100%', '85%'),
    EAN_STYLE_BOOK_STYLE: ('85%', '85%', '85%', '85%', '85%', '85%', '85%'),
}

# (left-buffer, start, left, mid, right, end, right-buffer)
EAN_STYLES_MODULE_Y = {
    EAN_STYLE_BARCODE_ONLY: ('0%', '0%', '0%', '0%', '0%', '0%', '0%'),
    EAN_STYLE_BARCODE_WITH_NUMBERS_BELOW: ('0%', '0%', '0%', '0%', '0%', '0%', '0%'),
    EAN_STYLE_BARCODE_WITH_NUMBERS_ABOVE: ('15%', '15%', '15%', '15%', '15%', '15%', '15%'),
    EAN_STYLE_PRODUCT_CODE: ('0%', '0%', '0%', '0%', '0%', '0%', '0%'),
    EAN_STYLE_BOOK_STYLE: ('0%', '0%', '0%', '0%', '0%', '0%', '0%'),
}

# (left-buffer, start, left, mid, right, end, right-buffer)
EAN_STYLES_TEXT_Y = {
    EAN_STYLE_BARCODE_ONLY: None,
    EAN_STYLE_BARCODE_ONLY: (0, 0, 0, 0, 0, 0, 0),
    EAN_STYLE_BARCODE_WITH_NUMBERS_BELOW: ('88%', '88%', '88%', '88%', '88%', '88%', '88%'),
    EAN_STYLE_BARCODE_WITH_NUMBERS_ABOVE: ('3%', '3%', '3%', '3%', '3%', '3%', '3%'),
    EAN_STYLE_PRODUCT_CODE: ('88%', '100%', '88%', '100%', '88%', '100%', '88%'),
    EAN_STYLE_BOOK_STYLE: ('88%', '88%', '88%', '88%', '88%', '88%', '88%'),
}

EAN_STYLES_SHOW_NUMBERS = {
    EAN_STYLE_BARCODE_ONLY: False,
    EAN_STYLE_BARCODE_WITH_NUMBERS_BELOW: True,
    EAN_STYLE_BARCODE_WITH_NUMBERS_ABOVE: True,
    EAN_STYLE_PRODUCT_CODE: True,
    EAN_STYLE_BOOK_STYLE: True,
}