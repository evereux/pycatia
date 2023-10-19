from pywintypes import com_error

from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.drafting_interfaces.drawing_sheet import DrawingSheet
from pycatia.drafting_interfaces.drawing_view import DrawingView

from .background_view import get_background_view_and_factory


def delete_all(drawing: DrawingDocument, sheet: DrawingSheet, query: str, type: str):
    """

    :param drawing:
    :param sheet:
    :param query:
    :param type:
    :return:
    """

    views = sheet.views
    background_view = DrawingView(views.get_item_by_name('Background View').com_object)

    sel = drawing.selection
    sel.clear()
    sel.add(background_view)
    query = f'{query},sel'
    sel.search(query)
    if sel.count > 0:
        print(f'Deleting {sel.count} {type} elements.')
        sel.delete()
    else:
        print('Couldn\'t find anything to delete.')
    sel.clear()


def purge_background_view(drawing: DrawingDocument, sheet: DrawingSheet):
    queries = [
        'Drafting.Line',
        'Drafting.Text',
        'Drafting.Picture',
    ]

    for query in queries:
        delete_all(drawing, sheet, query, query[9:])
