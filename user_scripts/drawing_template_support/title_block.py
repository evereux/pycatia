#! /usr/bin/python3.8

from pycatia.drafting_interfaces.drawing_sheet import DrawingSheet
from pycatia.drafting_interfaces.drawing_text import DrawingText
from pycatia.drafting_interfaces.drawing_texts import DrawingTexts
from pycatia.enumeration.enumeration_types import cat_text_anchor_position
from pycatia.exception_handling.exceptions import CATIAApplicationException
from pycatia.knowledge_interfaces.parameters import Parameters

from .background_view import get_background_view_and_factory
from .settings import border_offset
from .settings import company_details
from .settings import logo
from .settings import tolerances
from .settings import units
from .text_properties import set_text_properties


def add_title_block_text(texts: DrawingTexts,
                         text: str,
                         text_x: float,
                         text_y: float,
                         font: str = "SSS1",
                         size: float = 2.5) -> DrawingText:
    """

    :param DrawingTexts texts:
    :param str text:
    :param float text_x:
    :param float text_y:
    :param str font:
    :param float size:
    :return:
    """
    add_text = texts.add(text, text_x, text_y)
    anchor_position = cat_text_anchor_position.index('catBottomLeft')
    add_text.anchor_position = anchor_position
    set_text_properties(add_text, size=size, font=font)

    return add_text


def add_param_text(texts: DrawingTexts,
                   parameters: Parameters,
                   param_variable: str,
                   x: float,
                   y: float,
                   colour: int = 65535,
                   text: str = "",
                   size: float = 2.5):
    """

    :param DrawingTexts texts:
    :param Parameters parameters:
    :param str param_variable:
    :param float x:
    :param float y:
    :param int colour:
    :param str text:
    :param float size:
    :return:
    """

    p_ticket = parameters.get_item(f'Drawing\{param_variable}')
    param_text = add_title_block_text(texts, text, x, y, size=size)
    param_text.insert_variable(0, 0, p_ticket)
    # change text colour to blue
    # todo: build function that generates long integer from rgba value.
    #  reference: german https://ww3.cad.de/foren/ubb/Forum137/HTML/006362.shtml
    param_text.text_properties.color = colour

    return param_text


def create_title_block(sheet: DrawingSheet,
                       size_info: dict,
                       parameters: Parameters,
                       sheet_number: int,
                       ):
    """

    :param DrawingSheet sheet:
    :param dict size_info:
    :param Parameters parameters:
    :param int sheet_number:
    :return:
    """

    background_view, factory_2d, _ = get_background_view_and_factory(sheet)
    texts = background_view.texts
    paper_size = size_info['sheet_x'], size_info['sheet_y']

    title_block_width = 271
    title_block_height = 45.5

    # determine the bottom left corner of title block
    bottom_left_hand_corner_x = paper_size[0] - border_offset - title_block_width
    bottom_left_hand_corner_y = border_offset

    line_height = 6.5

    # dims for complete horizontal lines
    h1 = {"x_start": bottom_left_hand_corner_x, "x_end": bottom_left_hand_corner_x + title_block_width,
          "y": bottom_left_hand_corner_y}
    h2 = {"x_start": bottom_left_hand_corner_x, "x_end": bottom_left_hand_corner_x + title_block_width,
          "y": bottom_left_hand_corner_y + line_height}
    h3 = {"x_start": bottom_left_hand_corner_x, "x_end": bottom_left_hand_corner_x + title_block_width,
          "y": bottom_left_hand_corner_y + line_height * 3}
    h4 = {"x_start": bottom_left_hand_corner_x, "x_end": bottom_left_hand_corner_x + title_block_width,
          "y": bottom_left_hand_corner_y + line_height * 5}
    h5 = {"x_start": bottom_left_hand_corner_x, "x_end": bottom_left_hand_corner_x + title_block_width,
          "y": bottom_left_hand_corner_y + line_height * 7}  # top horizontal line

    # dims for complete vertical lines
    v1 = {"x": bottom_left_hand_corner_x, "y_start": bottom_left_hand_corner_y,
          "y_end": bottom_left_hand_corner_y + title_block_height}  # first vertical line
    v2_x_offset = 65
    v2 = {"x": bottom_left_hand_corner_x + v2_x_offset, "y_start": bottom_left_hand_corner_y,
          "y_end": bottom_left_hand_corner_y + title_block_height}
    v3_x_offset = 138
    v3 = {"x": bottom_left_hand_corner_x + v3_x_offset, "y_start": bottom_left_hand_corner_y,
          "y_end": bottom_left_hand_corner_y + title_block_height}
    v4 = {"x": bottom_left_hand_corner_x + title_block_width, "y_start": bottom_left_hand_corner_y,
          "y_end": bottom_left_hand_corner_y + title_block_height}

    # dims for partial vertical lines
    v1_1_x_offset = bottom_left_hand_corner_x + 28
    v1_1 = {"x": v1_1_x_offset, "y_start": bottom_left_hand_corner_y + line_height * 3,
            "y_end": bottom_left_hand_corner_y + title_block_height}

    v2_1_x_offset = v2['x'] + 46
    v2_1 = {"x": v2_1_x_offset, "y_start": bottom_left_hand_corner_y + line_height * 3,
            "y_end": bottom_left_hand_corner_y + line_height * 5}

    v2_2_x_offset = v2_1_x_offset + 13.5
    v2_2 = {"x": v2_2_x_offset, "y_start": bottom_left_hand_corner_y + line_height * 3,
            "y_end": bottom_left_hand_corner_y + line_height * 5}

    v3_1_x_offset = v3['x'] + 12
    v3_1 = {"x": v3_1_x_offset, "y_start": bottom_left_hand_corner_y + line_height,
            "y_end": bottom_left_hand_corner_y + line_height * 3}

    v3_2_x_offset = v3['x'] + 40
    v3_2 = {"x": v3_2_x_offset, "y_start": bottom_left_hand_corner_y, "y_end": bottom_left_hand_corner_y + line_height}

    v3_3_x_offset = v3['x'] + 95
    v3_3 = {"x": v3_3_x_offset, "y_start": bottom_left_hand_corner_y, "y_end": bottom_left_hand_corner_y + line_height}

    v3_4_x_offset = v3['x'] + 123
    v3_4 = {"x": v3_4_x_offset, "y_start": bottom_left_hand_corner_y + line_height,
            "y_end": bottom_left_hand_corner_y + line_height * 3}

    # dims for partial horizontal lines
    h2_1_y_offset = bottom_left_hand_corner_y + line_height * 2
    h2_1 = {"x_start": v2["x"], "x_end": v3["x"], "y": h2_1_y_offset}

    h3_1_y_offset = bottom_left_hand_corner_y + line_height * 4
    h3_1 = {"x_start": bottom_left_hand_corner_x, "x_end": v2['x'], "y": h3_1_y_offset}

    h3_2_y_offset = bottom_left_hand_corner_y + (line_height * 3) + ((line_height * 2) / 3)
    h3_2 = {"x_start": v2_1["x"], "x_end": v3['x'], "y": h3_2_y_offset}

    h3_3_y_offset = h3_2_y_offset + ((line_height * 2) / 3)
    h3_3 = {"x_start": v2_1["x"], "x_end": v3['x'], "y": h3_3_y_offset}

    h4_1_y_offset = bottom_left_hand_corner_y + (line_height * 6)
    h4_1 = {"x_start": bottom_left_hand_corner_x, "x_end": v2['x'], "y": h4_1_y_offset}

    # draw outer box lines
    # first vertical line, lhs
    line_obfv_1 = factory_2d.create_line(v1['x'], v1['y_start'], v1['x'], v1['y_end'])
    line_obfv_1.name = f'{line_obfv_1=}'.split('=')[0]

    # top horizontal line
    line_obfh_1 = factory_2d.create_line(h5['x_start'], h5['y'], h5['x_end'], h5['y'])
    line_obfh_1.name = f'{line_obfh_1=}'.split('=')[0]

    # internal full vertical lines
    offset_from_first = 65
    line_ifv_1 = factory_2d.create_line(v2['x'], v2['y_start'], v2['x'], v2['y_end'])
    line_ifv_1.name = f'{line_ifv_1=}'.split('=')[0]

    offset_from_first = offset_from_first + 73
    line_ifv_2 = factory_2d.create_line(v3['x'], v3['y_start'], v3['x'], v3['y_end'])
    line_ifv_2.name = f'{line_ifv_2=}'.split('=')[0]

    # internal full horizontal lines
    line_ifh_1 = factory_2d.create_line(h1['x_start'], h1['y'], h1['x_end'], h1['y'])
    line_ifh_1.name = f'{line_ifh_1=}'.split('=')[0]

    line_ifh_2 = factory_2d.create_line(h2['x_start'], h2['y'], h2['x_end'], h2['y'])
    line_ifh_2.name = f'{line_ifh_2=}'.split('=')[0]

    line_ifh_3 = factory_2d.create_line(h3['x_start'], h3['y'], h3['x_end'], h3['y'])
    line_ifh_3.name = f'{line_ifh_3=}'.split('=')[0]

    line_ifh_4 = factory_2d.create_line(h4['x_start'], h4['y'], h4['x_end'], h4['y'])

    # create internal partial horizontal lines
    line_iph_2_1 = factory_2d.create_line(h2_1['x_start'], h2_1["y"], h2_1['x_end'], h2_1["y"])
    line_iph_2_1.name = f'{line_iph_2_1=}'.split('=')[0]

    line_iph_3_1 = factory_2d.create_line(h3_1['x_start'], h3_1["y"], h3_1['x_end'], h3_1["y"])
    line_iph_3_1.name = f'{line_iph_3_1=}'.split('=')[0]

    line_iph_3_2 = factory_2d.create_line(h3_2['x_start'], h3_2["y"], h3_2['x_end'], h3_2["y"])
    line_iph_3_2.name = f'{line_iph_3_2=}'.split('=')[0]

    line_iph_3_3 = factory_2d.create_line(h3_3['x_start'], h3_3["y"], h3_3['x_end'], h3_3["y"])
    line_iph_3_3.name = f'{line_iph_3_3=}'.split('=')[0]

    line_iph_4_1 = factory_2d.create_line(h4_1['x_start'], h4_1["y"], h4_1['x_end'], h4_1["y"])
    line_iph_4_1.name = f'{line_iph_4_1=}'.split('=')[0]

    line_ifh_4.name = f'{line_ifh_4=}'.split('=')[0]

    # create the internal partial vertical lines
    line_ipv_1_1 = factory_2d.create_line(v1_1['x'], v1_1['y_start'], v1_1['x'], v1_1['y_end'])
    line_ipv_1_1.name = f'{line_ipv_1_1=}'.split('=')[0]

    line_ipv_2_1 = factory_2d.create_line(v2_1['x'], v2_1['y_start'], v2_1['x'], v2_1['y_end'])
    line_ipv_2_1.name = f'{line_ipv_2_1=}'.split('=')[0]

    line_ipv_2_2 = factory_2d.create_line(v2_2['x'], v2_2['y_start'], v2_2['x'], v2_2['y_end'])
    line_ipv_2_2.name = f'{line_ipv_2_2=}'.split('=')[0]

    line_ipv_3_1 = factory_2d.create_line(v3_1['x'], v3_1['y_start'], v3_1['x'], v3_1['y_end'])
    line_ipv_3_1.name = f'{line_ipv_3_1=}'.split('=')[0]

    line_ipv_3_2 = factory_2d.create_line(v3_2['x'], v3_2['y_start'], v3_2['x'], v3_2['y_end'])
    line_ipv_3_2.name = f'{line_ipv_3_2=}'.split('=')[0]

    line_ipv_3_3 = factory_2d.create_line(v3_3['x'], v3_3['y_start'], v3_3['x'], v3_3['y_end'])
    line_ipv_3_3.name = f'{line_ipv_3_3=}'.split('=')[0]

    line_ipv_3_4 = factory_2d.create_line(v3_4['x'], v3_4['y_start'], v3_4['x'], v3_4['y_end'])
    line_ipv_3_4.name = f'{line_ipv_3_4=}'.split('=')[0]

    # add text field names
    text_x_offset = 1.5
    text_y_offset = 1
    text_x = v1['x'] + text_x_offset
    text_y = h4_1["y"] + text_y_offset
    add_title_block_text(texts, 'TICKET REF', text_x, text_y)

    text_y = h4['y'] + text_y_offset
    add_title_block_text(texts, 'DRAWN BY', text_x, text_y)

    text_y = h3_1['y'] + text_y_offset
    add_title_block_text(texts, 'APPROVED BY', text_x, text_y)

    text_y = h3['y'] + text_y_offset
    add_title_block_text(texts, 'DATE', text_x, text_y)

    text_y = h2_1['y'] + text_y_offset
    add_title_block_text(texts, 'CAD DRAWING', text_x, text_y)

    text_x = v1['x'] + 1
    text_y = bottom_left_hand_corner_y + text_y_offset
    add_title_block_text(texts, 'INTERPRET DRAWING PER BS 8888:2011', text_x, text_y, size=2)

    text_x = v2['x'] + text_x_offset
    text_y = h2_1['y'] + text_y_offset
    add_title_block_text(texts, 'ANGULAR TOLERANCE ± 0° 30\'', text_x, text_y)

    text_y = h2['y'] + text_y_offset
    add_title_block_text(texts, 'SURFACE PROFILE TOLERANCE', text_x, text_y)

    text_x = v3['x'] + text_x_offset
    text_y = h2_1['y'] + text_y_offset
    add_title_block_text(texts, 'SIZE', text_x, text_y)

    text_x = v3['x'] + text_x_offset
    text_y = h3_1['y'] + text_y_offset
    add_title_block_text(texts, 'TITLE', text_x, text_y)

    text_x = v3_1['x'] + text_x_offset
    text_y = h2_1['y'] + text_y_offset
    add_title_block_text(texts, 'DWG No.', text_x, text_y)

    text_x = v3_4['x'] + text_x_offset
    text_y = h2_1['y'] + text_y_offset
    add_title_block_text(texts, 'REV', text_x, text_y)

    text_x = v3_2['x'] + text_x_offset
    text_y = bottom_left_hand_corner_y + 1
    add_title_block_text(texts, 'SCALE: ', text_x, text_y)

    text_x = v3_3['x'] + text_x_offset
    text_y = h1['y'] + text_y_offset
    add_title_block_text(texts, 'SHT     OF', text_x, text_y)

    # company address details
    # company name
    text_x = v3['x'] + 50
    text_y = h4['y'] + 9
    add_title_block_text(texts, company_details['name'], text_x, text_y, size=2.2)
    # loop through company address details
    for text in company_details['address']:
        text_y = text_y - 3
        add_title_block_text(texts, text, text_x, text_y, size=2.2)

    # add the logo
    if not logo.is_file():
        raise CATIAApplicationException(f'Could not locate logo: "{logo}".')
    logo_x = v3["x"] + 12.5
    logo_y = h4['y'] + 1.5
    pictures = background_view.pictures
    pictures.add(logo, logo_x, logo_y)

    # units
    text_x = v2['x'] + text_x_offset
    text_y = h4_1['y'] + text_y_offset - 1
    unit_text_1 = add_title_block_text(texts, 'UNLESS OTHERWISE SPECIFIED', text_x, text_y)
    text_y = h4['y'] + text_y_offset + 1
    unit_text_1 = add_title_block_text(texts, f'DIMENSIONS ARE IN {units[1]}', text_x, text_y)

    # linear tolerances
    text_x = v2['x'] + text_x_offset
    text_y = h3_1['y'] + text_y_offset - 1
    unit_text_1 = add_title_block_text(texts, f'{units[0]} LINEAR', text_x, text_y)
    text_y = h3['y'] + text_y_offset + 1
    unit_text_1 = add_title_block_text(texts, 'TOLERANCES.', text_x, text_y)

    # tolerances
    tol_1_text_key = ",X"
    text_x = v2_1['x'] + 3
    text_y = h3_3['y'] - .15
    tol_1_text = add_title_block_text(texts, tol_1_text_key, text_x, text_y)
    text_x = v2_2['x'] + 2.5
    tol_2_text_value = tolerances[tol_1_text_key][1:]
    tol_2_text = add_title_block_text(texts, tol_2_text_value, text_x, text_y)

    tol_3_text_key = ",XX"
    text_x = v2_1['x'] + 3
    text_y = h3_2['y'] - .15
    tol_3_text = add_title_block_text(texts, tol_3_text_key, text_x, text_y)
    text_x = v2_2['x'] + 2.5
    tol_3_text_value = tolerances[tol_3_text_key][1:]
    tol_3_text = add_title_block_text(texts, tol_3_text_value, text_x, text_y)

    tol_4_text_key = ",XXX"
    text_x = v2_1['x'] + 3
    text_y = h3['y'] - .15
    tol_4_text = add_title_block_text(texts, tol_4_text_key, text_x, text_y)
    text_x = v2_2['x'] + 2.5
    tol_4_text_value = tolerances[tol_4_text_key][1:]
    tol_3_text = add_title_block_text(texts, tol_4_text_value, text_x, text_y)

    # add text input fields that are linked to a parameter
    add_param_text(texts, parameters, "TICKET", v1_1["x"] + text_x_offset, h4_1['y'] + text_y_offset)
    add_param_text(texts, parameters, "DRAWN-BY", v1_1["x"] + text_x_offset, h4['y'] + text_y_offset)
    add_param_text(texts, parameters, "APPROVED-BY", v1_1["x"] + text_x_offset, h3_1['y'] + text_y_offset)
    add_param_text(texts, parameters, "DATE", v1_1["x"] + text_x_offset, h3['y'] + text_y_offset)
    # title
    title_x = (v3_1["x"] + v4['x']) / 2
    title_text = add_param_text(texts, parameters, "TITLE", title_x, h3['y'] + text_y_offset, size=4)
    anchor_position = cat_text_anchor_position.index('catBottomCenter')
    title_text.anchor_position = anchor_position
    # sheet size
    add_param_text(texts, parameters, "SIZE", v3['x'] + text_x_offset + 1.5, h2['y'] + text_y_offset, size=4)
    add_param_text(texts, parameters, "DRAWING-NUMBER", v3_1['x'] + 19, h2['y'] + text_y_offset, size=4)
    add_param_text(texts, parameters, "REVISION", v3_4['x'] + text_x_offset + .25, h2['y'] + text_y_offset, size=4)
    add_param_text(texts, parameters, "SCALE", v3_2['x'] + 15, h1['y'] + text_y_offset)
    add_param_text(texts, parameters, "TOTAL-SHEETS", v3_3['x'] + 25, h1['y'] + text_y_offset)
    # sheet number
    sheet_number_text = add_title_block_text(texts, str(sheet_number), v3_3['x'] + 11, h1['y'] + text_y_offset)
    sheet_number_text.text_properties.color = 65535
