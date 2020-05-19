#! /usr/bin/python3.6

"""
    Example 5:

    Creates a new CATIA file.

    Reads a csv file containing point data and adds to the new catia part.

    .. note::

        Please see :class:`HybridShapeFactory` and method add_new_point_coord()
        for caveats regarding large csv files.


    Formatting of csv data should be:
        <point_name>,<x coordinate>,<y coordinate>,<z coordinate>

"""

from pycatia.in_interfaces.application import catia_application as catia
from pycatia.scripts import create_points

# disable display refreshing to try tp speed up point generation.
catia.refresh_display = False
# hide catia window
catia.visible = False

documents = catia.documents
# create a new part.
documents.add('Part')

document = catia.active_document
part = document.part()

# full path name to csv file.
file = r'tests\Sample_Point_CSV_File1_small.csv'

# create the points.
create_points(catia, part, file, 'in', 'Points_Construction')

# re-enable display refresh
catia.refresh_display = True
# unhide catia window
catia.visible = True
