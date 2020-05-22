#! /usr/bin/python3.6

"""

    Example 13:

    3D Points, Lines ...

"""

from pycatia import catia

from tests.source_files import cat_part_blank

documents = catia.documents
documents.open(cat_part_blank)
part = catia.active_document.part()
factory = part.hybrid_shape_factory
hybrid_bodes = part.hybrid_bodies
# get the hybrid body to add the items too.
hybrid_body = hybrid_bodes.item("Geometrical Set.1")
# define the points
point_1 = factory.add_new_point_coord(1, 2, 3)
point_2 = factory.add_new_point_coord(100, 200, 300)
# add the points
hybrid_body.append_hybrid_shape(point_1)
hybrid_body.append_hybrid_shape(point_2)

hybrid_shapes = hybrid_body.hybrid_shapes
point_1 = hybrid_shapes.item(0)
point_2 = hybrid_shapes.item(1)
# create references to use to draw line with.
ref_point_1 = part.create_reference_from_object(point_1)
ref_point_2 = part.create_reference_from_object(point_2)
# define the line
line_1 = factory.add_new_line_pt_pt(ref_point_1, ref_point_2)
hybrid_body.append_hybrid_shape(line_1)
