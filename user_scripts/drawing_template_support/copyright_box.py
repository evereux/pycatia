#! /usr/bin/python3.6

import datetime

from pycatia.drafting_interfaces.drawing_sheet import DrawingSheet
from pycatia.drafting_interfaces.drawing_texts import DrawingTexts
from pycatia.enumeration.enumeration_types import cat_text_anchor_position
from pycatia.enumeration.enumeration_types import cat_text_frame_type
from pycatia.enumeration.enumeration_types import cat_text_property
from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.sketcher_interfaces.factory_2D import Factory2D

from .background_view import get_background_view_and_factory
from .settings import border_offset
from .settings import company_details
from .text_properties import set_text_properties


def create_copyright_box(sheet: DrawingSheet, parameters: Parameters):
    """
    x and y denote the bottom left hand corner of the box
    :param DrawingSheet sheet:
    :param Parameters parameters:
    :return:
    """

    background_view, factory_2d, _ = get_background_view_and_factory(sheet)

    texts = background_view.texts

    box_height = 30
    box_width = 130
    top_line = factory_2d.create_line(border_offset, border_offset + box_height, border_offset + box_width,
                                      border_offset + box_height)
    right_line = factory_2d.create_line(border_offset + box_width, border_offset, border_offset + box_width,
                                        border_offset + box_height)

    datetime.datetime.now()
    current_year = datetime.datetime.now().strftime('%Y')

    text_l1 = f"COPYRIGHT OF THIS DRAWING SPECIFICATION DOCUMENT, WHICH IS SUPPLIED"
    text_l2 = f"IN CONFIDENCE AND WHICH, WITHOUT THE EXPRESS WRITTEN CONSENT OF"
    text_l3 = f"{company_details['name']} MUST NOT BE USED FOR ANY PURPOSE OTHER THAN "
    text_l4 = f"THAT FOR WHICH IT IS SUPPLIED, MUST NOT BE REPRODUCED IN ANY WAY IN "
    text_l5 = f"WHOLE OR IN PART NOR LOANED TO ANY THIRD PARTY NOR MUST THE "
    text_l6 = f"INFORMATION CONTAINED THEREIN BE REPRODUCED OR LOANED IN WHOLE OR "
    text_l7 = f"IN PART. "
    text_l8 = f"ALL RIGHTS RESERVED. COPYRIGHT ."

    text_list = [text_l1, text_l2, text_l3, text_l4, text_l5, text_l6, text_l7, text_l8]

    text_x = border_offset + 2
    text_y = border_offset + 2

    copyright_texts = []

    for text in reversed(text_list):
        add_text = texts.add(text, text_x, text_y)
        anchor_position = cat_text_anchor_position.index('catBottomLeft')
        add_text.anchor_position = anchor_position
        set_text_properties(add_text, size=2)
        text_y = text_y + 3.27
        copyright_texts.append(add_text)

    # # add copyright symbol
    # # todo: this doesn't seem to work?
    # copyright = "c"
    # add_text = texts.add(copyright, 50.9, 12)
    # anchor_position = cat_text_anchor_position.index('catBottomLeft')
    # add_text.anchor_position = anchor_position
    # frame_type = cat_text_frame_type.index('catCircle')
    # add_text.frame_type = frame_type
    # set_text_properties(add_text, size=2)

    # link year to parameters
    p_year = parameters.get_item(f'Drawing\YEAR')
    bottom_line = copyright_texts[0]
    bottom_line.insert_variable(32, 0, p_year)
    property_colour = cat_text_property.index('catColor')
    bottom_line.set_parameter_on_sub_string(property_colour, 32, 8, 65535)
