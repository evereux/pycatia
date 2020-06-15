#! /usr/bin/python3.6

"""

    Example 2:

    Get all the points in the geometrical set 'Points' and output co-ordinate to console.

"""
from pycatia import catia

documents = catia.documents
documents.open(r'tests\CF_catia_measurable_part.CATPart')

document = catia.active_document
part = document.part()
spa_workbench = document.spa_workbench()

hybrid_bodies = part.hybrid_bodies
hybrid_body = hybrid_bodies.get_item_by_name('Points')
shapes = hybrid_body.hybrid_shapes.items()

for point in shapes:
    reference = part.create_reference_from_object(point)
    measurable = spa_workbench.get_measurable(reference)
    coordinates = measurable.get_point()
    print(f'{point.name}: {coordinates}')
