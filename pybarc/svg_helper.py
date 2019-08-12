from contextlib import contextmanager
from pybarc.constants import TAB_TO_SPACE


@contextmanager
def svg_main_tag(print_func, width='2.5cm', height='1.5cm', view_box=(0, 0, 95, 20), header=True):
    if header:
        print_func('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
        print_func('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">')
    print_func('<svg width="%s" height="%s" viewBox="%s" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg">'
               % (width, height, ' '.join(str(v) for v in view_box)))
    yield
    print_func('</svg>')


@contextmanager
def svg_group_tag(print_func, style=None, indent_level=0):
    indent = ' ' * (indent_level * TAB_TO_SPACE)
    if style is not None:
        print_func('%s<g style="%s">' % (indent, style))
    else:
        print_func('%s<g>' % indent)
    yield
    print_func('%s</g>' % indent)


@contextmanager
def svg_rect_tag(print_func, x=0, y=0, width=0, height=0, style=None, indent_level=0):
    indent = ' ' * (indent_level * TAB_TO_SPACE)
    x_str = x if isinstance(x, str) else str(x)
    y_str = y if isinstance(y, str) else str(y)
    w_str = width if isinstance(width, str) else str(width)
    h_str = height if isinstance(height, str) else str(height)
    if style is not None:
        print_func('%s<rect x="%s"  y="%s" width="%s" height="%s" style="%s" >' % (indent, x_str, y_str, w_str, h_str, style))
    else:
        print_func('%s<rect x="%s"  y="%s" width="%s" height="%s" >' % (indent, x_str, y_str, w_str, h_str))
    yield
    print_func('%s</rect>' % indent)
