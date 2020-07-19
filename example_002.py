#! /usr/bin/python3.6

"""

    Example 2:

    Get all the points in the geometrical set 'Points' and output co-ordinate to console.

    Create your own CATPart with a Geometrical Set called construction_points. Add some points to the Geometrical Set.

"""
from pycatia import catia

documents = catia.documents
# this should be the path to your file.
documents.open(r'tests\cat_files\part_measurable.CATPart')

document = catia.active_document
part = document.part()
spa_workbench = document.spa_workbench()

hybrid_bodies = part.hybrid_bodies
hybrid_body = hybrid_bodies.get_item_by_name('construction_points')
shapes = hybrid_body.hybrid_shapes.items()

for point in shapes:
    reference = part.create_reference_from_object(point)
    measurable = spa_workbench.get_measurable(reference)
    coordinates = measurable.get_point()
    print(f'{point.name}: {coordinates}')
