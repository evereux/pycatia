#! /usr/bin/python3.9

from pycatia import CATIADocHandler
from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.enumeration.enumeration_types import (
    cat_drawing_standard,
    cat_paper_orientation,
    cat_paper_size,
    cat_sheet_projection_method,
)
from tests.source_files import cat_drawing

# todo: tests for parameters and relations


def test_active_drawing():
    with CATIADocHandler(cat_drawing) as caa:
        drawing_root = DrawingDocument(caa.catia.active_document.com_object).drawing_root

        assert drawing_root.active_sheet.name in ["Sheet.1", "Blatt .1"]  # TODO: Add more languages


def test_orientation():
    with CATIADocHandler(cat_drawing) as caa:
        drawing_root = DrawingDocument(caa.catia.active_document.com_object).drawing_root
        sheets = drawing_root.sheets
        sheet_1 = sheets.item(1)
        assert sheet_1.orientation == cat_paper_orientation.index("catPaperLandscape")
        sheet_1.orientation = 0
        assert sheet_1.orientation == cat_paper_orientation.index("catPaperPortrait")


def test_paper_size():
    with CATIADocHandler(cat_drawing) as caa:
        drawing_root = DrawingDocument(caa.catia.active_document.com_object).drawing_root
        sheets = drawing_root.sheets
        sheet_1 = sheets.item(1)
        assert sheet_1.paper_size == cat_paper_size.index("catPaperA0")
        sheet_1.paper_size = cat_paper_size.index("catPaperA1")
        assert sheet_1.paper_size == cat_paper_size.index("catPaperA1")


def test_sheets():
    with CATIADocHandler(cat_drawing) as caa:
        drawing_root = DrawingDocument(caa.catia.active_document.com_object).drawing_root
        sheets = drawing_root.sheets
        assert sheets.item(2).name == "Sheet.2"


def test_standard():
    with CATIADocHandler(cat_drawing) as caa:
        drawing_root = DrawingDocument(caa.catia.active_document.com_object).drawing_root
        assert drawing_root.standard == cat_drawing_standard.index("catISO")


def test_reorder():
    with CATIADocHandler(cat_drawing) as caa:
        drawing_root = DrawingDocument(caa.catia.active_document.com_object).drawing_root
        sheets = drawing_root.sheets
        sheet_1 = sheets.item(1)
        sheet_2 = sheets.item(2)

        new_order = (sheet_2, sheet_1)
        drawing_root.reorder_sheets(new_order)

        sheets = drawing_root.sheets

        assert not sheets.item(1).name == "Sheet.1"
        assert sheets.item(1).name == "Sheet.2"


def test_scale():
    with CATIADocHandler(cat_drawing) as caa:
        drawing_root = DrawingDocument(caa.catia.active_document.com_object).drawing_root
        sheets = drawing_root.sheets
        sheet_1 = sheets.item(1)
        assert sheet_1.scale == 1.0
        sheet_1.scale = 2.0
        assert sheet_1.scale == 2.0


def test_projection_method():
    with CATIADocHandler(cat_drawing) as caa:
        drawing_root = DrawingDocument(caa.catia.active_document.com_object).drawing_root
        sheets = drawing_root.sheets
        sheet_1 = sheets.item(1)

        assert sheet_1.projection_method == cat_sheet_projection_method.index("catFirstAngle")
