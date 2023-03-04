#! /usr/bin/python3.9

"""

    Example - Space Analysis - 003:

    Find all points in the CATPart and print to console -> and export to csv.

    This will only work if you have language set to English. Further reading:
    https://github.com/evereux/pycatia/issues/93

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

import csv

from pycatia import catia

caa = catia()
documents = caa.documents
documents.open(r'tests/cat_files/part_measurable.CATPart')

document = caa.active_document

spa_workbench = document.spa_workbench()
part = document.part

selected = document.search_for_items(['Point'])

# export the points to a csv file.
csv_file_name = '__junk__\\exported_points.csv'
with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    for selection in selected:
        reference = part.create_reference_from_object(selection)
        measurable = spa_workbench.get_measurable(reference)

        # print to console.
        print(selection.name, measurable.get_point())

        x, y, z = measurable.get_point()
        csv_writer.writerow([selection.name, x, y, z])
