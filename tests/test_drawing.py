#! /usr/bin/python3.6

import pytest

from pycatia.base_interfaces.context import CATIADocHandler
from pycatia.drafting_interfaces.drawingroot import DrawingRoot
from pycatia.drafting_interfaces.enumeration_types import drawing_standard
from pycatia.drafting_interfaces.enumeration_types import paper_orientation
from pycatia.drafting_interfaces.enumeration_types import sheet_projection_method
from pycatia.in_interfaces.enumeration_types import paper_size
from tests.source_files import cat_drawing


# todo: tests for parameters and relations


def test_active_drawing():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        drawing_root = catia.active_document.drawing_root()

        assert drawing_root.active_sheet.name == 'Sheet.1'


def test_orientation():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        drawing_root = catia.active_document.drawing_root()
        sheets = drawing_root.sheets
        sheet_1 = sheets.item(0)
        assert sheet_1.orientation == paper_orientation.index('catPaperLandscape')
        sheet_1.orientation = 0
        assert sheet_1.orientation == paper_orientation.index('catPaperPortrait')


def test_paper_size():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        drawing_root = catia.active_document.drawing_root()
        sheets = drawing_root.sheets
        sheet_1 = sheets.item(0)
        assert sheet_1.paper_size == paper_size.index('catPaperA0')
        sheet_1.paper_size = 5
        assert sheet_1.paper_size == paper_size.index('catPaperA3')


def test_sheets():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        drawing_root = catia.active_document.drawing_root()
        sheets = drawing_root.sheets
        assert sheets.item(2).name == 'Sheet.3 (Detail)'


def test_standard():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        root = catia.active_document.drawing_root()
        assert root.standard == drawing_standard.index('catISO')


def test_reorder():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        root = catia.active_document.drawing_root()
        sheets = root.sheets
        sheet_1 = sheets.item(0)
        sheet_2 = sheets.item(1)
        sheet_3 = sheets.item(2)

        new_order = [sheet_2, sheet_1, sheet_3]
        root.reorder_sheets(new_order)

        sheets = root.sheets

        assert not sheets.item(0).name == 'Sheet.1'
        assert sheets.item(0).name == 'Sheet.2'


def test_scale():
    with CATIADocHandler(cat_drawing) as handler:
        catia = handler.catia
        root = catia.active_document.drawing_root()
        sheets = root.sheets
        sheet_1 = sheets.item(0)
        assert sheet_1.scale == 1.0
        sheet_1.scale = 2.0
        assert sheet_1.scale == 2.0


def test_projection_method():
    with CATIADocHandler(cat_drawing) as handler:
        sheets = handler.catia.active_document.drawing_root().sheets
        sheet_1 = sheets.item(1)

        assert sheet_1.projection_method == sheet_projection_method.index('catFirstAngle')
