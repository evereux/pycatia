#! /usr/bin/python3.11
"""
    Example - Selection - 002:
    Prompt the user to select 2 vertexes and create line in selected geometrical set
    .. warning:
        Catia must be run and document open and active.
        Document must be content 2 vertex(points) and geometrical set!
"""
from pycatia import catia
# import headers
caa = catia()
documents = caa.documents
# active document 
document = caa.active_document
# current part
part = document.part
# hybrid bodies for Geom set
HybridBodies=part.hybrid_bodies

# create selection
sel=document.selection
# Tuple selection 1-D Vertex
iot=("Vertex",)
# Status=Normal is vertex selected
# True= pre-select is allow
status=sel.select_element2(iot,"Select the first vertex",True)
# Get first vertex
FirstVertex = sel.item(1).value
# Clear selection
sel.clear()
# Status=Normal is vertex selected
# True= pre-select is allow
status=sel.select_element2(iot,"Select the second vertex",True)
# Get second vertex
SecondVertex = sel.item(1).value
# Clear selection
sel.clear()

#hybryd shape factory
hsf = part.hybrid_shape_factory

# select geometrical set. Preselect is allow
# Tuple selection Geometrical set
iot=("HybridBody",)
status=sel.select_element2(iot,"Select Geometrical set",True)

# set pointer to selected geometrical set 
hb_construction_geometry = HybridBodies.item(sel.item(1).value.name)

#create line
line = hsf.add_new_line_pt_pt(FirstVertex, SecondVertex)

# add line to geom set
hb_construction_geometry.append_hybrid_shape(line)
# update part.
part.update()
