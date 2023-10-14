#! /usr/bin/python3.9

"""

    Example - Hybrid Shape Factory - 006

    Description:
        How to add a new sphere when a reference axis system isn't required.

    Requirements:
        - A geometrical set named "ConstructionGeometry".
        - A point within the ConstructionGeometry named "Point.1".

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################
from pycatia import catia
from pycatia.mec_mod_interfaces.part import Part
from pycatia.hybrid_shape_interfaces.hybrid_shape_factory import HybridShapeFactory
import pythoncom

from pycatia.scripts.vba import vba_nothing

caa = catia()
document = caa.active_document
part = Part(document.part.com_object)
# Note: It's not necessary to explicitly use the PartDocument or the Part class
# with the com_object. It's perfectly fine to write it like this:
#   document = caa.active_document
#   part = document.part
# But declaring 'document' and 'part' this way, your linter can't resolve the
# product reference, see https://github.com/evereux/pycatia/issues/107#issuecomment-1336195688

hybrid_bodies = part.hybrid_bodies
construction_geometry = hybrid_bodies.item("ConstructionGeometry")

hybrid_shapes = construction_geometry.hybrid_shapes
centre_point = hybrid_shapes.item("Point.1")
reference_centre_point = part.create_reference_from_object(centre_point)

hybrid_shape_factory = part.hybrid_shape_factory
radius = 100
begin_parallel_angle = -45
end_parallel_angle = 45
begin_meridian_angle = 0
end_meridian_angle = 180
hybrid_shape_sphere = hybrid_shape_factory.add_new_sphere(
    reference_centre_point,
    vba_nothing,
    radius,
    begin_parallel_angle,
    end_parallel_angle,
    begin_meridian_angle,
    end_meridian_angle
)

# set limitation to 0 for a partial sphere, 1 for a complete sphere.
hybrid_shape_sphere.limitation = 0

construction_geometry.append_hybrid_shape(hybrid_shape_sphere)

part.update()
