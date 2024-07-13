#! /usr/bin/python3.9

"""
    Example - Hybrid Shape Factory - 002

    Description:
        Creates a new CATIA file and reads a csv file containing point data and adds to the new catia part.
        Formatting of csv data should be:
            <point_name>,<x coordinate>,<y coordinate>,<z coordinate>
        There should be no column name headers, just raw point data.

    Requirements:
        - CATIA running.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.scripts.csv_tools import create_points

caa = catia()
# # disable display refreshing to try tp speed up point generation.
# catia.refresh_display = False
# # hide catia window
# catia.visible = False

documents = caa.documents
# create a new part.
part_document: PartDocument = documents.add("Part")
part = part_document.part

# full path name to csv file.
file = r"..\tests\Sample_Point_CSV_File1_small.csv"

# create the points.
create_points(part, file, units="mm", geometry_set_name="Points_Construction")

# if you can't see the points hide your origin planes and refram window.

# # re-enable display refresh
# catia.refresh_display = True
# # unhide catia window
# catia.visible = True
