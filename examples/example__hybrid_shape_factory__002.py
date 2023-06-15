#! /usr/bin/python3.9

"""
    Example - Hybrid Shape Factory - 002:

    Creates a new CATIA file.

    Reads a csv file containing point data and adds to the new catia part.


    Formatting of csv data should be:
        <point_name>,<x coordinate>,<y coordinate>,<z coordinate>

    There should be no column name headers, just raw point data.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.mec_mod_interfaces.part import Part
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.scripts.csv_tools import create_points

caa = catia()
# # disable display refreshing to try tp speed up point generation.
# catia.refresh_display = False
# # hide catia window
# catia.visible = False

documents = caa.documents
# create a new part.
documents.add("Part")

document = PartDocument(caa.active_document.com_object)
part = Part(document.part.com_object)
# Note: It's not necessary to explicitly use the PartDocument or the Part class
# with the com_object. It's perfectly fine to write it like this:
#   document = caa.active_document
#   part = document.part
# But declaring 'document' and 'part' this way, your linter can't resolve the
# product reference, see https://github.com/evereux/pycatia/issues/107#issuecomment-1336195688

# full path name to csv file.
file = r"tests\Sample_Point_CSV_File1_small.csv"

# create the points.
create_points(part, file, units="mm", geometry_set_name="Points_Construction")

# if you can't see the points hide your origin planes and refram window.

# # re-enable display refresh
# catia.refresh_display = True
# # unhide catia window
# catia.visible = True
