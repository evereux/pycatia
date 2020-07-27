#! /usr/bin/python3.6

from pycatia import CATIADocHandler
from pycatia.enumeration.enumeration_types import cat_drawing_standard
from pycatia.enumeration.enumeration_types import cat_paper_orientation
from pycatia.enumeration.enumeration_types import cat_sheet_projection_method
from pycatia.enumeration.enumeration_types import cat_paper_size
from tests.source_files import cat_drawing


# todo: tests for parameters and relations


def test_active_drawing():
    with CATIADocHandler(cat_drawing) as caa:
        catia = handler.catia
        drawing_root = catia.active_document.drawing_root()

        assert drawing_root.active_sheet.name == 'Sheet.1'


def test_orientation():
    with CATIADocHandler(cat_drawing) as caa:
        catia = handler.catia
        drawing_root = catia.active_document.drawing_root()
        sheets = drawing_root.sheets
        sheet_1 = sheets.item(1)
        assert sheet_1.orientation == cat_paper_orientation.index('catPaperLandscape')
        sheet_1.orientation = 0
        assert sheet_1.orientation == cat_paper_orientation.index('catPaperPortrait')


def test_paper_size():
    with CATIADocHandler(cat_drawing) as caa:
        catia = handler.catia
        drawing_root = catia.active_document.drawing_root()
        sheets = drawing_root.sheets
        sheet_1 = sheets.item(1)
        assert sheet_1.paper_size == cat_paper_size.index('catPaperA0')
        sheet_1.paper_size = cat_paper_size.index("catPaperA1")
        assert sheet_1.paper_size == cat_paper_size.index('catPaperA1')


def test_sheets():
    with CATIADocHandler(cat_drawing) as caa:
        catia = handler.catia
        drawing_root = catia.active_document.drawing_root()
        sheets = drawing_root.sheets
        assert sheets.item(2).name == 'Sheet.2'


def test_standard():
    with CATIADocHandler(cat_drawing) as caa:
        catia = handler.catia
        root = catia.active_document.drawing_root()
        assert root.standard == cat_drawing_standard.index('catISO')


def test_reorder():
    with CATIADocHandler(cat_drawing) as caa:
        catia = handler.catia
        root = catia.active_document.drawing_root()
        sheets = root.sheets
        sheet_1 = sheets.item(1)
        sheet_2 = sheets.item(2)

        new_order = (sheet_2, sheet_1)
        root.reorder_sheets(new_order)

        sheets = root.sheets

        assert not sheets.item(1).name == 'Sheet.1'
        assert sheets.item(1).name == 'Sheet.2'


def test_scale():
    with CATIADocHandler(cat_drawing) as caa:
        catia = handler.catia
        root = catia.active_document.drawing_root()
        sheets = root.sheets
        sheet_1 = sheets.item(1)
        assert sheet_1.scale == 1.0
        sheet_1.scale = 2.0
        assert sheet_1.scale == 2.0


def test_projection_method():
    with CATIADocHandler(cat_drawing) as caa:
        sheets = handler.catia.active_document.drawing_root().sheets
        sheet_1 = sheets.item(1)

        assert sheet_1.projection_method == cat_sheet_projection_method.index('catFirstAngle')
