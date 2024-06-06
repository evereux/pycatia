#! /usr/bin/python3.9

"""
    
    Example - Drafting - 001

    Description:
        Drafting: Create a border template in the background view of the currently opened A0 landscape CATDrawing.

    Requirements:
        - An open empty drafting document (landscape, A0).

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.drafting_interfaces.drawing_root import DrawingRoot
from pycatia.drafting_interfaces.drawing_view import DrawingView
from pycatia.enumeration.enumeration_types import cat_paper_orientation
from pycatia.enumeration.enumeration_types import cat_paper_size
from pycatia.enumeration.enumeration_types import cat_text_anchor_position
from pycatia.exception_handling import CATIAApplicationException
from pycatia.system_interfaces.any_object import AnyObject

# A0 sheet size
a0_x = 1189
a0_y = 841

caa = catia()
# if the active document is a CATDrawing this will return a DrawingDocument
drawing_document: DrawingDocument = caa.active_document
drawing = DrawingRoot(drawing_document.drawing_root.com_object)

sheets = drawing.sheets
sheet = sheets.active_sheet

if cat_paper_orientation[sheet.orientation] != "catPaperLandscape":
    raise CATIAApplicationException("Sheet orientation is not landscape.")

if cat_paper_size[sheet.paper_size] != "catPaperA0":
    raise CATIAApplicationException("Sheet size is not A0.")

views = sheet.views
main_view_item = views.get_item_by_name("Main View")
assert isinstance(main_view_item, AnyObject)
main_view = DrawingView(main_view_item.com_object)

background_view_item = views.get_item_by_name("Background View")
assert isinstance(background_view_item, AnyObject)
background_view = DrawingView(background_view_item.com_object)

background_view.activate()
factory_2d = background_view.factory_2d

# create the outside border at page limits.
# bottom
ob_line_1 = factory_2d.create_line(0, 0, a0_x, 0)
ob_line_2 = factory_2d.create_line(a0_x, 0, a0_x, a0_y)
ob_line_3 = factory_2d.create_line(a0_x, a0_y, 0, a0_y)
ob_line_4 = factory_2d.create_line(0, a0_y, 0, 0)

# create inner border offset by 10mm
offset = 10
ib_line_1 = factory_2d.create_line(offset, offset, a0_x - offset, offset)
ib_line_2 = factory_2d.create_line(a0_x - offset, offset, a0_x - offset, a0_y - offset)
ib_line_3 = factory_2d.create_line(a0_x - offset, a0_y - offset, offset, a0_y - offset)
ib_line_4 = factory_2d.create_line(offset, a0_y - offset, offset, offset)

# add some lines for grid referencing
h_splits = 5
v_splits = 4
h_offset = a0_x / h_splits
v_offset = a0_y / v_splits

h_split_1 = factory_2d.create_line(h_offset, 0, h_offset, offset)
h_split_2 = factory_2d.create_line(h_offset * 2, 0, h_offset * 2, offset)
h_split_3 = factory_2d.create_line(h_offset * 3, 0, h_offset * 3, offset)
h_split_4 = factory_2d.create_line(h_offset * 4, 0, h_offset * 4, offset)

h_split_5 = factory_2d.create_line(h_offset, a0_y - offset, h_offset, a0_y)
h_split_6 = factory_2d.create_line(h_offset * 2, a0_y - offset, h_offset * 2, a0_y)
h_split_7 = factory_2d.create_line(h_offset * 3, a0_y - offset, h_offset * 3, a0_y)
h_split_8 = factory_2d.create_line(h_offset * 4, a0_y - offset, h_offset * 4, a0_y)

v_split_1 = factory_2d.create_line(0, v_offset, offset, v_offset)
v_split_2 = factory_2d.create_line(0, v_offset * 2, offset, v_offset * 2)
v_split_3 = factory_2d.create_line(0, v_offset * 3, offset, v_offset * 3)

v_split_4 = factory_2d.create_line(a0_x, v_offset, a0_x - offset, v_offset)
v_split_5 = factory_2d.create_line(a0_x, v_offset * 2, a0_x - offset, v_offset * 2)
v_split_6 = factory_2d.create_line(a0_x, v_offset * 2, a0_x - offset, v_offset * 2)

# add some text to the border

anchor_position = cat_text_anchor_position.index("catMiddleCenter")

texts = background_view.texts


# create a function to change the font by using the DrawingTextProperties class of DrawingText.
def change_text_properties(text):
    """

    :param text: DrawingText
    :return:
    """
    text_properties = text.text_properties
    text_properties.font_name = "SSS1"
    text_properties.font_size = 3.5

    return text


text_e_l = texts.add("E", h_offset / 2, offset / 2)
text_e_l.anchor_position = anchor_position
text_e_l = change_text_properties(text_e_l)

text_d_l = texts.add("D", h_offset / 2 + h_offset, offset / 2)
text_d_l.anchor_position = anchor_position
text_d_l = change_text_properties(text_d_l)

text_c_l = texts.add("C", h_offset / 2 + (h_offset * 2), offset / 2)
text_c_l.anchor_position = anchor_position
text_c_l = change_text_properties(text_c_l)

text_b_l = texts.add("B", h_offset / 2 + (h_offset * 3), offset / 2)
text_b_l.anchor_position = anchor_position
text_b_l = change_text_properties(text_b_l)

text_a_l = texts.add("A", h_offset / 2 + (h_offset * 4), offset / 2)
text_a_l.anchor_position = anchor_position
text_a_l = change_text_properties(text_a_l)

text_e_u = texts.add("E", h_offset / 2, a0_y - (offset / 2))
text_e_u.anchor_position = anchor_position
text_e_u = change_text_properties(text_e_u)

text_d_u = texts.add("D", h_offset / 2 + h_offset, a0_y - (offset / 2))
text_d_u.anchor_position = anchor_position
text_d_u = change_text_properties(text_d_u)

text_c_u = texts.add("C", h_offset / 2 + (h_offset * 2), a0_y - (offset / 2))
text_c_u.anchor_position = anchor_position
text_c_u = change_text_properties(text_c_u)

text_b_u = texts.add("B", h_offset / 2 + (h_offset * 3), a0_y - (offset / 2))
text_b_u.anchor_position = anchor_position
text_b_u = change_text_properties(text_b_u)

text_a_u = texts.add("A", h_offset / 2 + (h_offset * 4), a0_y - (offset / 2))
text_a_u.anchor_position = anchor_position
text_a_u = change_text_properties(text_a_u)

text_1_l = texts.add("1", offset / 2, v_offset / 2)
text_1_l.anchor_position = anchor_position
text_1_l = change_text_properties(text_1_l)

text_2_l = texts.add("2", offset / 2, v_offset / 2 + v_offset)
text_2_l.anchor_position = anchor_position
text_2_l = change_text_properties(text_2_l)

text_3_l = texts.add("3", offset / 2, v_offset / 2 + (v_offset * 2))
text_3_l.anchor_position = anchor_position
text_3_l = change_text_properties(text_3_l)

text_4_l = texts.add("3", offset / 2, v_offset / 2 + (v_offset * 3))
text_4_l.anchor_position = anchor_position
text_4_l = change_text_properties(text_4_l)

text_1_r = texts.add("1", a0_x - (offset / 2), v_offset / 2)
text_1_r.anchor_position = anchor_position
text_1_r = change_text_properties(text_1_r)

text_2_r = texts.add("2", a0_x - (offset / 2), v_offset / 2 + v_offset)
text_2_r.anchor_position = anchor_position
text_2_r = change_text_properties(text_2_r)

text_3_r = texts.add("3", a0_x - (offset / 2), v_offset / 2 + (v_offset * 2))
text_3_r.anchor_position = anchor_position
text_3_r = change_text_properties(text_3_r)

text_4_r = texts.add("3", a0_x - (offset / 2), v_offset / 2 + (v_offset * 3))
text_4_r.anchor_position = anchor_position
text_4_r = change_text_properties(text_4_r)

main_view.activate()

sheet.force_update()
