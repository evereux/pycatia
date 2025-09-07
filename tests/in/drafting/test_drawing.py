#! /usr/bin/python3.9
import pytest

from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.enumeration.enumeration_types import cat_drawing_standard
from pycatia.enumeration.enumeration_types import cat_paper_orientation
from pycatia.enumeration.enumeration_types import cat_paper_size
from pycatia.enumeration.enumeration_types import cat_sheet_projection_method
from tests.conftest import application
from tests.source_files import cat_drawing


# todo: tests for parameters and relations

@pytest.mark.parametrize('file_name', [cat_drawing])
def test_drawing_doc_type(document_close_all_open):
    drawing_document: DrawingDocument = application.active_document
    assert type(drawing_document) is DrawingDocument


@pytest.mark.parametrize('file_name', [cat_drawing])
def test_active_drawing(document_open):
    drawing_document: DrawingDocument = application.active_document
    drawing_root = drawing_document.drawing_root
    assert drawing_root.active_sheet.name in ["Sheet.1", "Blatt.1"]  # TODO: Add more languages


@pytest.mark.parametrize('file_name', [cat_drawing])
def test_orientation(document_open):
    drawing_document: DrawingDocument = application.active_document
    sheets = drawing_document.sheets
    sheet_1 = sheets.item(1)
    assert sheet_1.orientation == cat_paper_orientation.index("catPaperLandscape")
    sheet_1.orientation = 0
    assert sheet_1.orientation == cat_paper_orientation.index("catPaperPortrait")


@pytest.mark.parametrize('file_name', [cat_drawing])
def test_paper_size(document_open):
    drawing_document: DrawingDocument = application.active_document
    sheets = drawing_document.sheets
    sheet_1 = sheets.item(1)
    assert sheet_1.paper_size == cat_paper_size.index("catPaperA0")
    sheet_1.paper_size = cat_paper_size.index("catPaperA1")
    assert sheet_1.paper_size == cat_paper_size.index("catPaperA1")


@pytest.mark.parametrize('file_name', [cat_drawing])
def test_sheets(document_open):
    drawing_document = application.active_document
    sheets = drawing_document.sheets
    assert sheets.item(2).name == "Sheet.2"


@pytest.mark.parametrize('file_name', [cat_drawing])
def test_standard(document_open):
    drawing_document: DrawingDocument = application.active_document
    standard = drawing_document.standard
    assert standard == cat_drawing_standard.index("catISO")


@pytest.mark.parametrize('file_name', [cat_drawing])
def test_reorder(document_open_test_close_all):
    drawing_document: DrawingDocument = application.active_document
    drawing_root = drawing_document.drawing_root
    sheets = drawing_document.sheets
    sheet_1 = sheets.item(1)
    sheet_2 = sheets.item(2)

    new_order = (sheet_2, sheet_1)
    drawing_root.reorder_sheets(new_order)

    sheets = drawing_document.sheets

    assert not sheets.item(1).name == "Sheet.1"
    assert sheets.item(1).name == "Sheet.2"


@pytest.mark.parametrize('file_name', [cat_drawing])
def test_scale(document_open_test_close_all):
    drawing_document: DrawingDocument = application.active_document
    sheets = drawing_document.sheets
    sheet_1 = sheets.item(1)
    assert sheet_1.scale == 1.0
    sheet_1.scale = 2.0
    assert sheet_1.scale == 2.0


@pytest.mark.parametrize('file_name', [cat_drawing])
def test_projection_method(document_open_test_close_all):
    drawing_document = application.active_document
    drawing_root = drawing_document.drawing_root
    sheets = drawing_root.sheets
    sheet_1 = sheets.item(1)

    assert sheet_1.projection_method == cat_sheet_projection_method.index("catFirstAngle")
