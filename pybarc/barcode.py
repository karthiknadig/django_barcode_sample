import sys

from pybarc.constants import (
    EAN_STYLE_PRODUCT_CODE, EAN_STYLES_TEXT_Y, EAN_STYLES_SHOW_NUMBERS, EAN_STYLES_MODULE_Y,
    EAN_13_LENGTH, EAN_13_CHECK_DIGIT_POSITION,
    EAN_13_STRUCTURE, EAN_8_STRUCTURE,
    EAN_L_CODE, EAN_R_CODE, EAN_G_CODE,
    EAN_STYLES_MODULE_HEIGHTS, EAN_START, EAN_MIDDLE, EAN_END,
    EAN_8_LENGTH, EAN_8_CHECK_DIGIT_POSITION
)
from pybarc.utils import ean_13_check_digit, ean_8_check_digit
from pybarc.svg_helper import svg_main_tag, svg_group_tag, svg_rect_tag
from pybarc.svg_text import get_char_svg


def ean_13_svg(
    value,
    out_file=sys.stdout,
    buffer=(7, 7),
    width='2.5cm',
    height='1.5cm',
    view_box=(0, 0, 95, 65),
    background='#ffffff',
    line='#000000',
    force=False,
    style=EAN_STYLE_PRODUCT_CODE):

    if len(value) != EAN_13_LENGTH:
        raise Exception()

    if value[EAN_13_CHECK_DIGIT_POSITION] == 'x':
        value = value[0:EAN_13_CHECK_DIGIT_POSITION] + ean_13_check_digit(value)
    else:
        # validate
        if not force and value[12] != ean_13_check_digit(value):
            raise Exception()

    svg_print = lambda s: print(s, file=out_file)

    if not isinstance(buffer, tuple) or not all(isinstance(b, int) for b in buffer):
        raise Exception()

    if not isinstance(view_box, tuple) or not all(isinstance(b, int) for b in view_box):
        raise Exception()

    view_box = list(view_box)
    view_box[2] += sum(buffer)

    val = [int(v) for v in value]
    left, right = EAN_13_STRUCTURE[int(val[0])]

    with svg_main_tag(svg_print, width, height, view_box):
        svg_print('    <!-- EAN-13 for %s -->' % value)

        with svg_rect_tag(svg_print, x=0, y=0, width='100%', height='100%', style="fill:#ffffff;stroke:none;", indent_level=1):
            pass

        fill_back = 'fill:%s;stroke:none;' % background
        fill_fore = 'fill:%s;stroke:none;' % line
        fill = [fill_back, fill_fore]
        with svg_group_tag(svg_print, indent_level=1):
            x, w = 0, 1

            style_h = EAN_STYLES_MODULE_HEIGHTS[style]
            style_y = EAN_STYLES_MODULE_Y[style]
            style_text_y = EAN_STYLES_TEXT_Y[style]
            show_num = EAN_STYLES_SHOW_NUMBERS[style]
            # Left side buffer space
            if show_num:
                svg_print(get_char_svg(val[0], x+1, style_text_y[0], w*6, '10%'))
            for p in (0 for i in range(buffer[0])):
                with svg_rect_tag(svg_print, x=x, y=style_y[0], width=w, height=style_h[0], style=fill[p], indent_level=2):
                    pass
                x += w

            # EAN-13 start pattern
            for p in EAN_START:
                with svg_rect_tag(svg_print, x=x, y=style_y[1], width=w, height=style_h[1], style=fill[p], indent_level=2):
                    pass
                x += w

            # EAN-13 Left side numbers
            for i, v in enumerate(val[1:7]):
                if show_num:
                    svg_print(get_char_svg(v, x+1, style_text_y[2], w*6, '10%'))
                for p in (EAN_L_CODE[v] if left[i] == 'L' else EAN_G_CODE[v]):
                    with svg_rect_tag(svg_print, x=x, y=style_y[2], width=w, height=style_h[2], style=fill[p], indent_level=2):
                        pass
                    x += w

            # EAN-13 middle pattern
            for p in EAN_MIDDLE:
                with svg_rect_tag(svg_print, x=x, y=style_y[3], width=w, height=style_h[3], style=fill[p], indent_level=2):
                    pass
                x += w

            # EAN-13 Right side numbers
            assert right == ('R', 'R', 'R', 'R', 'R', 'R')
            for v in val[7:]:
                if show_num:
                    svg_print(get_char_svg(v, x+1, style_text_y[4], w*6, '10%'))
                for p in (EAN_R_CODE[v]):
                    with svg_rect_tag(svg_print, x=x, y=style_y[4], width=w, height=style_h[4], style=fill[p], indent_level=2):
                        pass
                    x += w

            # EAN-13 End pattern
            for p in EAN_END:
                with svg_rect_tag(svg_print, x=x, y=style_y[5], width=w, height=style_h[5], style=fill[p], indent_level=2):
                    pass
                x += w

            # Right side buffer space
            for p in (0 for i in range(buffer[1])):
                with svg_rect_tag(svg_print, x=x, y=style_y[6], width=w, height=style_h[6], style=fill[p], indent_level=2):
                    pass
                x += w


def ean_8_svg(
    value,
    out_file=sys.stdout,
    buffer=(5, 5),
    width='2.5cm',
    height='1.5cm',
    view_box=(0, 0, 95, 63),
    background='#ffffff',
    line='#000000',
    force=False,
    style=EAN_STYLE_PRODUCT_CODE):
    if len(value) != EAN_8_LENGTH:
        raise Exception()

    if value[EAN_8_CHECK_DIGIT_POSITION] == 'x':
        value = value[0:EAN_8_CHECK_DIGIT_POSITION] + ean_8_check_digit(value)
    else:
        # validate
        if not force and value[EAN_8_CHECK_DIGIT_POSITION] != ean_8_check_digit(value):
            raise Exception()

    svg_print = lambda s: print(s, file=out_file)

    if not isinstance(buffer, tuple) or not all(isinstance(b, int) for b in buffer):
        raise Exception()

    if not isinstance(view_box, tuple) or not all(isinstance(b, int) for b in view_box):
        raise Exception()

    view_box = list(view_box)
    view_box[2] += sum(buffer)

    val = [int(v) for v in value]
    left, right = EAN_8_STRUCTURE

    with svg_main_tag(svg_print, width, height, view_box):
        svg_print('    <!-- EAN-8 for %s -->' % value)

        with svg_rect_tag(svg_print, x=0, y=0, width='100%', height='100%', style="fill:#ffffff;stroke:none;", indent_level=1):
            pass

        fill_back = 'fill:%s;stroke:none;' % background
        fill_fore = 'fill:%s;stroke:none;' % line
        fill = [fill_back, fill_fore]
        with svg_group_tag(svg_print, indent_level=1):
            x, w = 0, 1

            style_h = EAN_STYLES_MODULE_HEIGHTS[style]
            style_y = EAN_STYLES_MODULE_Y[style]
            style_text_y = EAN_STYLES_TEXT_Y[style]
            show_num = EAN_STYLES_SHOW_NUMBERS[style]
            # Left side buffer space
            for p in (0 for i in range(buffer[0])):
                with svg_rect_tag(svg_print, x=x, y=style_y[0], width=w, height=style_h[0], style=fill[p], indent_level=2):
                    pass
                x += w

            # EAN-8 start pattern
            for p in EAN_START:
                with svg_rect_tag(svg_print, x=x, y=style_y[1], width=w, height=style_h[1], style=fill[p], indent_level=2):
                    pass
                x += w

            # EAN-8 Left side numbers
            assert left == ('L', 'L', 'L', 'L')
            for i, v in enumerate(val[0:4]):
                if show_num:
                    svg_print(get_char_svg(v, x+1, style_text_y[2], w*6, '10%'))
                for p in EAN_L_CODE[v]:
                    with svg_rect_tag(svg_print, x=x, y=style_y[2], width=w, height=style_h[2], style=fill[p], indent_level=2):
                        pass
                    x += w

            # EAN-8 middle pattern
            for p in EAN_MIDDLE:
                with svg_rect_tag(svg_print, x=x, y=style_y[3], width=w, height=style_h[3], style=fill[p], indent_level=2):
                    pass
                x += w

            # EAN-8 Right side numbers
            assert right == ('R', 'R', 'R', 'R')
            for v in val[4:]:
                if show_num:
                    svg_print(get_char_svg(v, x+1, style_text_y[4], w*6, '10%'))
                for p in EAN_R_CODE[v]:
                    with svg_rect_tag(svg_print, x=x, y=style_y[4], width=w, height=style_h[4], style=fill[p], indent_level=2):
                        pass
                    x += w

            # EAN-8 End pattern
            for p in EAN_END:
                with svg_rect_tag(svg_print, x=x, y=style_y[5], width=w, height=style_h[5], style=fill[p], indent_level=2):
                    pass
                x += w

            # Right side buffer space
            for p in (0 for i in range(buffer[1])):
                with svg_rect_tag(svg_print, x=x, y=style_y[6], width=w, height=style_h[6], style=fill[p], indent_level=2):
                    pass
                x += w


def handle_rendering(image_name: str):
    parts = image_name.split(sep='_')
    assert len(parts) == 2
    form, code, image = [parts[0]] + parts[1].split('.')
    import io
    strobj = io.StringIO('')
    if image.lower() == 'svg':
        if form.lower() == 'ean13':
            ean_13_svg(code, out_file=strobj)
        elif form.lower() == 'ean8':
            ean_8_svg(code, out_file=strobj)
        return strobj.getvalue()
    return b''

#eans = ['6439000158963', '3363680376214', '3761112928404', '9407297299321', '6389704134728', '9299210752859', '6125691735858', '5104714327585', '3487248819064', '8874788167031']
#eans = ['30352810', '49124606', '54178335', '56559385', '95163994', '88677439', '54641686', '33243603', '83879319', '10669600']
#for ean in eans:
#    with open(ean + '.svg', 'w') as f:
#        ean_13_svg(ean, out_file=f)
