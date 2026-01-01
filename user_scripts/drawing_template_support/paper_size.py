from pycatia import CatPaperSize
from pycatia.drafting_interfaces.drawing_sheet import DrawingSheet

from .settings import sheet_sizes


def get_sheet_size_info(sheet: DrawingSheet) -> dict:
    """

    :param DrawingSheet sheet:
    :return:
    """

    enum_paper_size = sheet.paper_size
    legible_paper_size = CatPaperSize(enum_paper_size).name

    if legible_paper_size not in sheet_sizes:
        raise ValueError('Failed to reconcile paper size')

    sheet_x = sheet_sizes[legible_paper_size][0][0]
    sheet_y = sheet_sizes[legible_paper_size][0][1]

    return {"paper_size": enum_paper_size,
            "enum_paper_size": enum_paper_size,
            "legible_paper_size": legible_paper_size,
            "sheet_x": sheet_x,
            "sheet_y": sheet_y}
