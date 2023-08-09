#! /usr/bin/python3.6
"""
    Example - Selection - 002:
    Prompt the user to select 2 vertexes and create line in selected geometrical set
    .. warning:
        Catia must be run and document open and active.
        Document must be content 2 vertex(points) and geometrical set!
"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.

import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

from pycatia.mec_mod_interfaces.part import Part
from pycatia import catia
# import headers
caa = catia()
documents = caa.documents
document = caa.active_document
part = Part(document.part.com_object)
HybridBodies = part.hybrid_bodies

# create selection
sel = document.selection
# Tuple selection 1-D Vertex
iot = ("Vertex",)
# Status=Normal is vertex selected
# True= pre-select is allow
status = sel.select_element2(iot, "Select the first vertex", True)
if status=="Cancel":
    caa.message_box("Canceled",16)
    exit()
FirstVertex = sel.item(1).value
sel.clear()

status = sel.select_element2(iot, "Select the second vertex", True)
if status=="Cancel":
    caa.message_box("Canceled",16)
    exit()
SecondVertex = sel.item(1).value
sel.clear()


hsf = part.hybrid_shape_factory

# select geometrical set. Preselect is allow
iot = ("HybridBody",)
status = sel.select_element2(iot, "Select Geometrical set", True)
if status=="Cancel":
    caa.message_box("Canceled",16)
    exit()

# set pointer to selected geometrical set
hb_construction_geometry = HybridBodies.item(sel.item(1).value.name)

# create line
line = hsf.add_new_line_pt_pt(FirstVertex, SecondVertex)
hb_construction_geometry.append_hybrid_shape(line)
part.update()
caa.message_box("Line is created!", 0, "Congratulation")
