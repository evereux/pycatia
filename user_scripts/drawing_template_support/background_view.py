#! /usr/bin/python3.8

from pycatia.drafting_interfaces.drawing_sheet import DrawingSheet
from pycatia.drafting_interfaces.drawing_view import DrawingView
from pycatia.sketcher_interfaces.factory_2D import Factory2D


def get_background_view_and_factory(sheet: DrawingSheet) -> tuple[DrawingView, Factory2D, DrawingView]:

    views = sheet.views
    main_view = views.get_item_by_name('Main View')
    background_view = DrawingView(views.get_item_by_name('Background View').com_object)
    background_view.activate()
    factory_2d = background_view.factory_2d

    return background_view, factory_2d, main_view
