#! /usr/bin/python3.6

"""

    Example - Space Analysis - 002:

    Get all the points in the geometrical set 'Points' and output co-ordinate to console.

    Create your own CATPart with a Geometrical Set called construction_points. Add some points to the Geometrical Set.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

from pycatia import catia

caa = catia()
documents = caa.documents
# this should be the path to your file.
documents.open(r'tests\cat_files\part_measurable.CATPart')

document = caa.active_document
part = document.part
spa_workbench = document.spa_workbench()

hybrid_bodies = part.hybrid_bodies
hybrid_body = hybrid_bodies.get_item_by_name('construction_points')
shapes = hybrid_body.hybrid_shapes

for point in shapes:
    reference = part.create_reference_from_object(point)
    measurable = spa_workbench.get_measurable(reference)
    coordinates = measurable.get_point()
    print(f'{point.name}: {coordinates}')
