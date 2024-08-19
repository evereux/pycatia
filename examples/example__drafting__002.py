"""

    Example - Drafting - 002

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
from pycatia.enumeration.enumeration_types import cat_dim_type
from pycatia.enumeration.enumeration_types import cat_dim_line_rep
from pycatia.drafting_interfaces.drawing_document import DrawingDocument

caa = catia()
drawing_document: DrawingDocument = caa.active_document
sheets = drawing_document.sheets
sheet = sheets.active_sheet
views = sheet.views
active_view = views.active_view
factory_2d = active_view.factory_2d

line_1 = factory_2d.create_line(50, 10, 150, 10)
line_2 = factory_2d.create_line(50, 10, 120, 100)
elipse = factory_2d.create_ellipse(-40, 100, 120, 180, 120, 90, 0, 3)
point_1 = factory_2d.create_point(-10, 190)
point_2 = factory_2d.create_point(-120, 190)

catDimAngle = cat_dim_type.index('catDimAngle')
catDimAuto = cat_dim_line_rep.index('catDimAuto')

line_elements = (line_1, line_2)
selection_points_1 = (150, 10, 120, 100)

active_view.dimensions.add(catDimAngle, line_elements, selection_points_1, catDimAuto)

catDimLengthCurvilinear = cat_dim_type.index('catDimLengthCurvilinear')
catDimOffset = cat_dim_line_rep.index('catDimOffset')

var_elements = (point_1, point_2, elipse)
selection_points_2 = (0, 0, 0, 0)
active_view.dimensions.add(catDimLengthCurvilinear, var_elements, selection_points_2, catDimOffset)
