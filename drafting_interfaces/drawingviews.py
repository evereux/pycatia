#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 09:45:39.224078

from pycatia.system_interfaces.collection import Collection
from .drawingview import DrawingView


class DrawingViews(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | A collection of all the drawing views currently managed by a drawing
                | sheet in a drawing document.Warning: This interface is not available
                | with 2D Layout for 3D Design.

    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingView)
        self.drawing_views = com_object

    @property
    def active_view(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ActiveView
                | o Property ActiveView(    ) As   (Read Only)
                | 
                | Returns the active drawing view of the active drawing sheet.
                | Warning: This method is not available with 2D Layout for 3D
                | Design.
                |
                | Example:
                | The following example retrieves in
                | ViewToWorkIn the active drawing view in the DrawingSheets
                | collection of the document named CATDrawing1
                |
                | Dim MyDrawingDoc As Document
                | Set MyDrawingDoc = CATIA.Documents.Item("CATDrawing1")
                | Dim ViewToWorkIn As DrawingView
                | Set ViewToWorkIn = MyDrawingDoc.Sheets.ActiveSheet.DrawingViews.ActiveView

        :return:
        """
        return self.child_object(self.drawing_views.ActiveView)

    def add(self, i_drawing_view_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | Add
                | o Func Add(        iDrawingViewName) As
                | 
                | Creates a drawing view and adds it to the drawing view
                | collection. This drawing view becomes the active one.
                | Warning: This method is not available with 2D Layout for 3D
                | Design.
                |
                | Parameters:
                | iDrawingViewName
                |   The name to assign to the created drawing view
                |
                | Returns:
                |   The created drawing view
                |
                | Examples:
                | The following example creates a drawing view named LeftView
                | and retrieved in MyView in the drawing view collection of
                | the MySheet drawing sheet. This sheet belongs to the drawing
                | sheet collection of the drawing document named CATDrawing1.
                | Dim MyDrawingDoc As Document
                | Set MyDrawingDoc = CATIA.Documents.Item("CATDrawing1")
                | Dim MySheet As DrawingSheet
                | Set MySheet = MyDrawingDoc.Sheets.Item("FirstSheet")
                | Dim MyView As DrawingView
                | Set MyView = MySheet.Views.Add("LeftView")

        :param str i_drawing_view_name:
        :return:
        """
        return self.drawing_views.Add(i_drawing_view_name)

    def item(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(        iIndex) As
                | 
                | Returns a drawing view using its index or its name from the
                | DrawingViews collection. Warning: This method is not
                | available with 2D Layout for 3D Design.
                |
                | Parameters:
                | iIndex
                |    The index or the name of the drawing view to retrieve from
                |    the collection of drawing views.
                |    As a numeric, this index is the rank of the drawing view
                |    in the collection.
                |    The index of the first drawing view in the collection is 1, and
                |    the index of the last drawing view is Count.
                |    As a string, it is the name you assigned to the drawing view using
                |    the 
                | 
                |  property or when creating it using   the 
                |  method. 
                |    Returns:
                |   The retrieved drawing view
                |
                | Examples:
                | This example retrieves in ThisDrawingView the second drawing
                | view, and in ThatDrawingView the drawing view named MyView
                | in the drawing view collection of the active sheet in the
                | active document, supposed to be a drawing document. Dim
                | MySheet As DrawingSheet Set MySheet =
                | CATIA.ActiveDocument.Sheets.ActiveSheet Dim ThisDrawingView
                | As DrawingView Set ThisDrawingView =
                | MySheet.Views.ActiveView.Item(2) Dim ThatDrawingView As
                | DrawingView Set ThatDrawingView =
                | MySheet.Views.ActiveView.Item("MyView")

        :param i_index:
        :return:
        """
        return self.child_object(self.drawing_views.Item(i_index))

    def remove(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | Remove
                | o Sub Remove(        iIndex)
                | 
                | Removes a drawing view from the DrawingViews collection.
                | Warning: This method is not available with 2D Layout for 3D
                | Design and it's forbidden and not possible to delete main
                | view and background view contained in this collection.
                |
                | Parameters:
                | iIndex
                |    The index or the name of the drawing view to remove from
                |    the collection of drawing views.
                |    As a numeric, this index is the rank of the drawing view
                |    in the collection.
                |    The index of the first drawing view in the collection is 1, and
                |    the index of the last drawing view is Count.
                |    As a string, it is the name you assigned to the drawing view using
                |    the 
                | 
                |  property or when creating it using   the 
                |  method.

                |                | Examples:
                | The following example removes the third drawing view and the
                | drawing view named TopView in the drawing view collection of
                | the active sheet of the active document, supposed to be a
                | drawing document. Dim MySheet As DrawingSheet Set MySheet =
                | CATIA.ActiveDocument.Sheets.ActiveSheet
                | MySheet.ActiveViews.Remove(3)
                | MySheet.ActiveViews.Remove("TopView")

        :param i_index:
        :return:
        """
        return self.drawing_views.Remove(i_index)

    def __repr__(self):
        return f'DrawingViews(name="{self.name}")'
