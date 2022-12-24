import os
from pathlib import Path

from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.enumeration.enumeration_types import cat_paper_size
from tests.common_vars import caa
from tests.common_vars import test_files
from tests.create_source_parts import get_cat_part_measurable

source_cat_drawing = Path(os.getcwd(), test_files, "drawing.CATDrawing")


def create_cat_drawing():
    documents = caa.documents
    documents.add("Drawing")
    drawing_document = caa.active_document
    drawing_document.save_as(source_cat_drawing)
    drawing = DrawingDocument(drawing_document.com_object).drawing_root
    sheets = drawing.sheets

    # open the cat part from which we'll be creating a front view.
    documents.open(str(get_cat_part_measurable()))
    document_product = caa.active_document

    # ################## #
    # Create a new Sheet #
    # ################## #

    sheet_2 = sheets.add("Sheet.2")
    sheet_2.paper_size = cat_paper_size.index("catPaperA1")

    # ############################## #
    # Create a front view on sheet 1 #
    # ############################## #

    sheet_1 = sheets.item(1)
    sheet_1.activate()
    sheet_1_views = sheet_1.views
    front_view = sheet_1_views.add("AutomaticNaming")

    generative_behaviour = front_view.generative_behavior
    generative_behaviour.document = document_product
    generative_behaviour.define_front_view(0, 1, 0, 0, 0, 1)

    # position the view
    front_view.x = 50
    front_view.y = 50
    front_view.scale = 1

    generative_behaviour.update()

    drawing_document.save()

    document_product.close()


def get_cat_drawing():
    if not source_cat_drawing.exists():
        caa.logger.info(f"Creating {source_cat_drawing}")
        create_cat_drawing()
    return source_cat_drawing
