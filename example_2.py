#! /usr/bin/python3.6

"""

    Example 2:

    Shows how to get all the points in the geometrical set 'Points' and get the co-ordinate.

"""
from pycatia import CATIAMeasurable
from pycatia import create_reference, create_measurable
from pycatia import get_document_part_object
from pycatia import create_spa_workbench

document, part = get_document_part_object()
spa_workbench = create_spa_workbench(document)

hybrid_body = part.get_hybrid_body_by_name('Points')
points = part.get_hybrid_shapes_from_hybrid_body(hybrid_body)

for point in points:
    reference = create_reference(part.part, point)
    measurable = create_measurable(spa_workbench, reference)
    point_measurable = CATIAMeasurable(measurable)
    coordinates = point_measurable.get_point()
    print(f'{point.name}: {coordinates}')
