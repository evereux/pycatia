#! /usr/bin/python3.6

"""

    Example 3:

    Find all points in the CATPart and print to console -> and export to csv.

"""

import csv

from pycatia import CATIAApplication
from pycatia import CATIAMeasurable
from pycatia import create_measurable
from pycatia import create_spa_workbench

catia = CATIAApplication()

documents = catia.documents()
documents.open(r'tests\CF_catia_measurable_part.CATPart')

document = catia.document()

spa_workbench = create_spa_workbench(document.document)
part = document.part()

selected = document.search_for_items(document, ['Point'])

# export the points to a csv file.
csv_file_name = '__junk__\\exported_points.csv'
with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    for selection in selected:
        reference = part.create_reference(selection)
        selection_measurable = create_measurable(spa_workbench, reference)
        measurable = CATIAMeasurable(selection_measurable)

        # print to console.
        print(selection.Name, measurable.get_point(catia))

        point_name = selection.Name
        x, y, z = measurable.get_point(catia)
        csv_writer.writerow([point_name, x, y, z])
