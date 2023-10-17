#! /usr/bin/python3.8

from pycatia import catia
from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.enumeration.enumeration_types import cat_drawing_standard
from pycatia.enumeration.enumeration_types import cat_paper_size
from pycatia.enumeration.enumeration_types import cat_paper_orientation

from .caa import documents
from .views import resize_active_view
from .settings import sheet_names


def create_drawing(sheet_size: str):
    document = documents.add("Drawing")
    drawing_document = DrawingDocument(document.com_object)

    # apply the catISO drawing standard.
    drawing_document.standard = cat_drawing_standard.index('catISO')
    sheets = drawing_document.sheets
    sheet_1 = sheets.item(sheet_names[0])
    sheet_1.paper_size = cat_paper_size.index(f'catPaper{sheet_size}')
    sheet_1.scale = 1
    sheet_1.Orientation = cat_paper_orientation.index('catPaperLandscape')

    resize_active_view()

    # create new sheet 2
    sheet_2 = sheets.add(sheet_names[1])
    sheet_2.paper_size = cat_paper_size.index(f'catPaper{sheet_size}')
    sheet_2.scale = 1
    sheet_1.Orientation = cat_paper_orientation.index('catPaperLandscape')

    resize_active_view()

    return drawing_document
