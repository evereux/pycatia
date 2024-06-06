#! /usr/bin/python3.9

"""

    Example - Selection - 002

    Description:
        Prompt the user to select 2 vertexes and create line in selected geometrical set

    Requirements:
        - CATIA must be running with part document open and active.
        - Part document must contain 2 vertex (points) and a geometrical set.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.

import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia import catia

caa = catia()
# if the active document is a CATPart this will return a PartDocument
part_document: PartDocument = caa.active_document
part = part_document.part
hybrid_bodies = part.hybrid_bodies
hsf = part.hybrid_shape_factory

# create selection object
selection = part_document.selection

filter_type = ("Vertex",)

# i_object_selection_before_command_use_possibility - True = pre-selection is allowed.
status = selection.select_element2(filter_type, "Select the first vertex", True)

# status==Normal is vertex selected
if status == "Cancel":
    caa.message_box("Canceled", 16)
    exit()
first_vertex = selection.item(1).reference
selection.clear()

status = selection.select_element2(filter_type, "Select the second vertex", True)
if status == "Cancel":
    caa.message_box("Cancelled", 16)
    exit()
second_vertex = selection.item(1).reference
selection.clear()

filter_type = ("HybridBody",)
status = selection.select_element2(filter_type, "Select Geometrical set", True)
if status == "Cancel":
    caa.message_box("Cancelled", 16)
    exit()

# set pointer to selected geometrical set
hb_construction_geometry = hybrid_bodies.get_item_by_name(selection.item(1).value.name)

# create line
line = hsf.add_new_line_pt_pt(first_vertex, second_vertex)
hb_construction_geometry.append_hybrid_shape(line)
part.update()
caa.message_box("Line is created!", 0, "Congratulations!")
