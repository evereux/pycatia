#! /usr/bin/python3.9

"""

    Example - Space Analysis - 002

    Description:
        Get all the points in the geometrical set 'Points' and output co-ordinate to console.
        Create your own CATPart with a Geometrical Set called construction_points.
        Add some points to the Geometrical Set.

    Requirements:
        - A part document with the above described setup.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.mec_mod_interfaces.hybrid_body import HybridBody
from pycatia.mec_mod_interfaces.part import Part
from pycatia.mec_mod_interfaces.part_document import PartDocument

caa = catia()
documents = caa.documents
# this should be the path to your file.
documents.open(r"tests\cat_files\part_measurable.CATPart")

document = PartDocument(caa.active_document.com_object)
part = Part(document.part.com_object)
# Note: It's not necessary to explicitly use the PartDocument or the Part class
# with the com_object. It's perfectly fine to write it like this:
#   document = caa.active_document
#   part = document.part
# But declaring 'document' and 'part' this way, your linter can't resolve the
# product reference, see https://github.com/evereux/pycatia/issues/107#issuecomment-1336195688
spa_workbench = document.spa_workbench()

hybrid_bodies = part.hybrid_bodies
hybrid_body_item = hybrid_bodies.get_item_by_name("construction_points")
assert hybrid_body_item is not None
hybrid_body = HybridBody(hybrid_body_item.com_object)

shapes = hybrid_body.hybrid_shapes

for point in shapes:
    reference = part.create_reference_from_object(point)
    measurable = spa_workbench.get_measurable(reference)
    coordinates = measurable.get_point()
    print(f"{point.name}: {coordinates}")
