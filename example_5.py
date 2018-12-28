#! /usr/bin/python3.6

"""

    Example 5:

    Reads a csv file containing point data and adds to the active catia part.

    Formatting should be:
        <point_name>,<x coordinate>,<y coordinate>,<z coordimate>

    A CATPart must be open in CATIA.

"""

from pycatia import CATIAApplication
from pycatia import Document
from pycatia import create_points

catia = CATIAApplication()
document = Document(catia.catia)
part = document.part

# full path name to csv file.
file = r'tests\Sample_Point_CSV_File1_small.csv'

# create the points in currently open CATIA part.
create_points(part, file)
