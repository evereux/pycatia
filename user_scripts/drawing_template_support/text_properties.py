#! /usr/bin/python3.8

from pycatia.drafting_interfaces.drawing_text import DrawingText
from pycatia.enumeration.enumeration_types import cat_text_property


def set_text_properties(text: DrawingText,
                        font: str = 'SSS1',
                        font_spacing: float = 20,
                        line_spacing: float = 1.27,
                        size: float = 3.5,
                        ) -> DrawingText:
    """

    :param text:
    :param font:
    :param font_spacing:
    :param line_spacing:
    :param float size:
    :return: DrawingText:
    """
    text_properties = text.text_properties
    text_properties.font_name = font
    text_properties.font_size = size

    # drwText.SetParameterOnsubString catCharSpacing,0,0,25
    # drwText.SetParameterOnsubString catCharRatio,0,0,55
    char_spacing = cat_text_property.index('catCharSpacing')
    char_test = cat_text_property.index('catParagraph')
    text.set_parameter_on_sub_string(char_spacing, 0, 0, 20)
    text.set_parameter_on_sub_string(char_test, 0, 0, 0)

    return text
