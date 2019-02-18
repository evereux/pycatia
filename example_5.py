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


from pycatia import CATIAApplication
from pycatia import create_points

catia = CATIAApplication()
# disable display refreshing to try tp speed up point generation.
catia.refresh_display(False)
# hide catia window
catia.visible(False)

documents = catia.documents()
# create a new part.
documents.add('Part')

document = catia.document()
part = document.part()

# full path name to csv file.
file = r'tests\Sample_Point_CSV_File3_medium.csv'

# create the points in currently open CATIA part.
create_points(catia, part, file)

# re-enable display refresh
catia.refresh_display(True)
# unhide catia window
catia.visible(True)
