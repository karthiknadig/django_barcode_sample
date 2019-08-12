import os
import os.path

SVG_FONTS_DIR = os.path.join(os.path.dirname(__file__), 'fonts')
SVG_FONTS1_DIR = os.path.join(SVG_FONTS_DIR, 'font1')

def _get_svg_char_data(svg_file):
    with open(svg_file, 'r') as f:
        text = f.readlines()
    text = text[1:]
    text[0] = text[0].replace('<svg ', r'<svg x="{}" y="{}" width="{}" height="{}" ')
    return ''.join(text)


SVG_FONT1 = {
    0: _get_svg_char_data(os.path.join(SVG_FONTS1_DIR, '0.svg')),
    1: _get_svg_char_data(os.path.join(SVG_FONTS1_DIR, '1.svg')),
    2: _get_svg_char_data(os.path.join(SVG_FONTS1_DIR, '2.svg')),
    3: _get_svg_char_data(os.path.join(SVG_FONTS1_DIR, '3.svg')),
    4: _get_svg_char_data(os.path.join(SVG_FONTS1_DIR, '4.svg')),
    5: _get_svg_char_data(os.path.join(SVG_FONTS1_DIR, '5.svg')),
    6: _get_svg_char_data(os.path.join(SVG_FONTS1_DIR, '6.svg')),
    7: _get_svg_char_data(os.path.join(SVG_FONTS1_DIR, '7.svg')),
    8: _get_svg_char_data(os.path.join(SVG_FONTS1_DIR, '8.svg')),
    9: _get_svg_char_data(os.path.join(SVG_FONTS1_DIR, '9.svg')),
}

SVG_FONTS = {
    'font1': SVG_FONT1
}

SVG_FONT_NAMES = ['font1']
SVG_DEFAULT_FONT = SVG_FONT_NAMES[0]


def get_char_svg(character, x, y, width, height, **kwargs):
    font_family = kwargs.get('font_family', 'font1')
    font_style = kwargs.get('font_style', None)
    font_weight = kwargs.get('font_weight', None)

    if font_style is not None:
        pass

    if font_weight is not None:
        pass

    return SVG_FONTS[font_family][character].format(x, y, width, height)
