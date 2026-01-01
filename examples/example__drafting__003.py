"""

    Example - Drafting - 003

    Description:
        Drafting: Create a dimension in the active view.

    Requirements:
        - An open CATDrawing with a view active.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia import CatDimType
from pycatia.drafting_interfaces.drawing_document import DrawingDocument

application = catia()
drawing_document: DrawingDocument = application.active_document
sheets = drawing_document.sheets
sheet = sheets.active_sheet
views = sheet.views
active_view = views.active_view
factory_2d = active_view.factory_2d

point_1 = factory_2d.create_point(40, 230)
point_2 = factory_2d.create_point(80, 210)
line_1 = factory_2d.create_line(50, 10, 150, 10)

catDimDistance = CatDimType.catDimDistance

point_elements = (point_1, point_2)
selection_points = (0, 0, 0, 0)

dimension = active_view.dimensions.add2(catDimDistance, point_elements, selection_points, line_1, 0)
