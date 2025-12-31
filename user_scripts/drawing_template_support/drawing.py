from pycatia import CatDrawingStandard
from pycatia import CatPaperSize
from pycatia import CatPaperOrientation
from pycatia.drafting_interfaces.drawing_document import DrawingDocument

from .caa import documents
from .views import resize_active_view
from .settings import sheet_names


def create_drawing(sheet_size: str):
    document = documents.add("Drawing")
    drawing_document = DrawingDocument(document.com_object)

    # apply the catISO drawing standard.
    drawing_document.standard = CatDrawingStandard.catISO.value
    sheets = drawing_document.sheets
    sheet_1 = sheets.item(sheet_names[0])
    sheet_1.paper_size = getattr(CatPaperSize, 'catPaperA0').value
    sheet_1.scale = 1
    sheet_1.Orientation = CatPaperOrientation.catPaperLandscape.value

    resize_active_view()

    # create new sheet 2
    sheet_2 = sheets.add(sheet_names[1])
    sheet_2.paper_size = getattr(CatPaperSize, 'catPaperA0').value
    sheet_2.scale = 1
    sheet_1.Orientation = CatPaperOrientation.catPaperLandscape.value

    resize_active_view()

    return drawing_document
