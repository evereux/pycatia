#! /usr/bin/python3.8

from pycatia.drafting_interfaces.drawing_sheet import DrawingSheet
from pycatia.enumeration.enumeration_types import cat_paper_size

from .settings import sheet_sizes


def get_sheet_size_info(sheet: DrawingSheet) -> dict:
    """

    :param DrawingSheet sheet:
    :return:
    """

    paper_size = sheet.paper_size
    enum_paper_size = cat_paper_size[paper_size]
    legible_paper_size = enum_paper_size.strip('catPaper')

    if legible_paper_size not in sheet_sizes:
        raise ValueError('Failed to reconcile paper size')

    sheet_x = sheet_sizes[legible_paper_size][0][0]
    sheet_y = sheet_sizes[legible_paper_size][0][1]

    return {"paper_size": paper_size,
            "enum_paper_size": enum_paper_size,
            "legible_paper_size": legible_paper_size,
            "sheet_x": sheet_x,
            "sheet_y": sheet_y}
