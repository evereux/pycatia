#! /usr/bin/python3.9

"""

    Example - Hybrid Shape Factory - 005:

    GSD: Split a surface using a plane.

    Requirements: Geometrical set named "ConstructionGeometry". A surface
    within the geometrical set called "Surface.1" that can be split by the
    origin ZX plane.

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
from pycatia.mec_mod_interfaces.part_document import PartDocument

caa = catia()
document = PartDocument(caa.active_document.com_object)
part = Part(document.part.com_object)
bodies = part.bodies
# Note: It's not necessary to explicitly use the PartDocument or the Part class
# with the com_object. It's perfectly fine to write it like this:
#   document = caa.active_document
#   part = document.part
# But declaring 'document' and 'part' this way, your linter can't resolve the
# product reference, see https://github.com/evereux/pycatia/issues/107#issuecomment-1336195688

hsf = part.hybrid_shape_factory
hbs = part.hybrid_bodies

hb_construction_geometry = hbs.item("ConstructionGeometry")
hs_construction_geometry = hb_construction_geometry.hybrid_shapes
hs_surface = hs_construction_geometry.item("Surface.1")
ref_hs_surface = part.create_reference_from_object(hs_surface)

origin_elements = part.origin_elements
hs_plane_zx = origin_elements.plane_zx
ref_hs_plane_zx = part.create_reference_from_object(hs_plane_zx)

hs_split = hsf.add_new_hybrid_split(ref_hs_surface, ref_hs_plane_zx, -1)
hb_construction_geometry.append_hybrid_shape(hs_split)

hsf.gsm_visibility(ref_hs_surface, 0)

part.in_work_object = hs_split
part.update()
