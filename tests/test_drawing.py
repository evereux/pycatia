#! /usr/bin/python3.6

import pytest

from pycatia.base_interfaces import CATIADocHandler
from pycatia.drafting_interfaces import DrawingRoot
from pycatia.exception_handling import CATIAApplicationException

cat_drawing = r'tests/CF_Drawing1.CATDrawing'


# todo: tests for parameters and relations


def test_active_drawing():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        drawing = DrawingRoot(catia)

        assert drawing.active_sheet.Name == 'Sheet.1'


def test_orientation():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        drawing = DrawingRoot(catia)
        sheets = drawing.sheets
        sheet_1 = sheets[0]
        assert sheet_1.orientation == 'catPaperLandscape'
        sheet_1.orientation = 0
        assert sheet_1.orientation == 'catPaperPortrait'


def test_paper_size():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        drawing = DrawingRoot(catia)
        sheet_1 = drawing.sheets[0]
        assert sheet_1.paper_size == 2
        sheet_1.paper_size = 5
        assert sheet_1.paper_size == 5

    with pytest.raises(CATIAApplicationException):
        with CATIADocHandler(cat_drawing) as handler:
            catia = handler.catia
            drawing = DrawingRoot(catia)
            sheet_1 = drawing.sheets[0]
            sheet_1.paper_size = 10


def test_sheets():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        drawing = DrawingRoot(catia)
        sheets = drawing.sheets
        assert sheets[2].name == 'Sheet.3 (Detail)'


def test_standard():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        drawing = DrawingRoot(catia)
        assert drawing.standard == 'ISO'


def test_reorder():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        drawing = DrawingRoot(catia)
        sheets = drawing.sheets
        sheet_1 = sheets[0]
        sheet_2 = sheets[1]
        sheet_3 = sheets[2]

        new_order = [sheet_2.sheet, sheet_1.sheet, sheet_3.sheet]
        drawing.reorder_sheets(new_order)

        assert not drawing.sheets[0].name == 'Sheet.1'
        assert drawing.sheets[0].name == 'Sheet.2'


def test_scale():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        drawing = DrawingRoot(catia)
        sheets = drawing.sheets
        sheet_1 = sheets[0]
        assert sheet_1.scale == 1.0
        sheet_1.scale = 2.0
        assert sheet_1.scale == 2.0


def test_views():
    with CATIADocHandler(cat_drawing) as handler:
        sheets = DrawingRoot(handler.catia).sheets
        sheet_1 = sheets[0]

        assert sheet_1.views.active_view.name == 'Main View'


def test_projection_method():
    with CATIADocHandler(cat_drawing) as handler:
        sheets = DrawingRoot(handler.catia).sheets
        sheet_1 = sheets[0]

        assert sheet_1.project_method == 'FirstAngle'


def test_view_scale():
    with CATIADocHandler(cat_drawing) as handler:
        sheets = DrawingRoot(handler.catia).sheets
        sheet_1 = sheets[0]
        views = sheet_1.views
        view = views.get_view_by_name('Isometric view')
        assert view.scale == 1.0
        view.scale = 2.0
        assert view.scale == 2.0
