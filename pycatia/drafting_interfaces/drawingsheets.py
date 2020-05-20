#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:56:40.651039

from pycatia.system_interfaces.collection import Collection
from .drawingsheet import DrawingSheet


class DrawingSheets(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | A collection of all the drawing sheets currently managed by the
                | drawing document.Warning: This interface is not available with 2D
                | Layout for 3D Design.

    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingSheet)
        self.drawing_sheets = com_object

    @property
    def active_sheet(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ActiveSheet
                | o Property ActiveSheet(    ) As   (Read Only)
                |
                | Returns the active drawing sheet of the drawing document.
                | Warning: This method is not available with 2D Layout for 3D
                | Design. Example: The following example retrieves in
                | SheetToWorkIn the active drawing sheet of the drawing
                | document named CATDrawing1. Dim MyDrawingDoc As Document Set
                | MyDrawingDoc = CATIA.Documents.Item("CATDrawing1") Dim
                | SheetToWorkIn As DrawingSheet Set SheetToWorkIn =
                | MyDrawingDoc.Sheets.ActiveSheet
                |

        :return:
        """
        return self.child_object(self.drawing_sheets.ActiveSheet)

    def add(self, i_drawing_sheet_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | Add
                | o Func Add(        iDrawingSheetName) As
                |
                | Creates a drawing sheet and adds it to the DrawingSheets
                | collection. This drawing sheet becomes the active one.
                | Warning: This method is not available with 2D Layout for 3D
                | Design.
                |
                | Parameters:
                | iDrawingSheetName
                |    The name to assign to the created DrawingSheet object
                |
                |
                |  Returns:
                |   The created drawing sheet

                |                | Examples:
                | The following example creates a drawing sheet named
                | FirstSheet and retrieved in MySheet in the drawing sheet
                | collection of the document named CATDrawing1. Dim
                | MyDrawingDoc As Document Set MyDrawingDoc =
                | CATIA.Documents.Item("CATDrawing1") Dim MySheet As
                | DrawingSheet Set MySheet =
                | MyDrawingDoc.Sheets.Add("FirstSheet")

        :param i_drawing_sheet_name:
        :return:
        """
        return self.drawing_sheets.Add(i_drawing_sheet_name)

    def add_detail(self, i_drawing_sheet_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddDetail
                | o Func AddDetail(        iDrawingSheetName) As
                |
                | Creates a detail drawing sheet and adds it to the
                | DrawingSheets collection. This detail drawing sheet becomes
                | the active one. Warning: This method is not available with
                | 2D Layout for 3D Design.
                |
                | Parameters:
                | iDrawingSheetName
                |    The name to assign to the created detail DrawingSheet object
                |
                |
                |  Returns:
                |   The created drawing sheet

                |                | Examples:
                | The following example creates a detail drawing sheet named
                | FirstSheet and retrieved in MySheet in the drawing sheet
                | collection of the document named CATDrawing1. Dim
                | MyDrawingDoc As Document Set MyDrawingDoc =
                | CATIA.Documents.Item("CATDrawing1") Dim MySheet As
                | DrawingSheet Set MySheet =
                | MyDrawingDoc.Sheets.Add("FirstSheet")

        :param i_drawing_sheet_name:
        :return:
        """
        return self.drawing_sheets.AddDetail(i_drawing_sheet_name)

    def item(self, i_index):
        """
        .. warning::

            The index when not a string must be it's python index (indexes in python start from 0).
            collection. The COM interface index starts at 1.

        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(        iIndex) As
                |
                | Returns a drawing sheet using its index or its name from the
                | DrawingSheets collection. Warning: This method is not
                | available with 2D Layout for 3D Design.
                |
                | Parameters:
                | iIndex
                |    The index or the name of the drawing sheet to retrieve from
                |    the collection of drawing sheets.
                |    As a numeric, this index is the rank of the drawing sheet
                |    in the collection.
                |    The index of the first drawing sheet in the collection is 1, and
                |    the index of the last drawing sheet is Count.
                |    As a string, it is the name you assigned to the drawing sheet using
                |    the
                |
                |  property or when creating it using   the
                |  method.
                |    Returns:
                |   The retrieved drawing sheet

                |                | Examples:
                | This example retrieves in ThisDrawingSheet the third drawing
                | sheet, and in ThatDrawingSheet the drawing sheet named
                | MySheet in the drawing sheet collection of the active
                | document, supposed to be a drawing document. Dim
                | ThisDrawingSheet As DrawingSheet Set ThisDrawingSheet =
                | CATIA.ActiveDocument.Sheets.Item(3) Dim ThatDrawingSheet As
                | DrawingSheet Set ThatDrawingSheet =
                | CATIA.ActiveDocument.Sheets.Item("MySheet")

        :param i_index:
        :return:
        """

        if isinstance(i_index, int):
            i_index += 1

        return self.child_object(self.drawing_sheets.Item(i_index))

    def remove(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | Remove
                | o Sub Remove(        iIndex)
                |
                | Removes a drawing sheet from the DrawingSheets collection.
                | Warning: This method is not available with 2D Layout for 3D
                | Design.
                |
                | Parameters:
                | iIndex
                |    The index or the name of the drawing sheet to remove from
                |    the collection of drawing sheets.
                |    As a numeric, this index is the rank of the drawing sheet
                |    in the collection.
                |    The index of the first drawing sheet in the collection is 1, and
                |    the index of the last drawing sheet is Count.
                |    As a string, it is the name you assigned to the drawing sheet using
                |    the
                |
                |  property or when creating it using   the
                |  method.

                |                | Examples:
                | The following example removes the second drawing sheet and
                | the drawing sheet named SheetToBeRemoved in the drawing
                | sheet collection of the active document, supposed to be a
                | drawing document.
                | CATIA.ActiveDocument.DrawingSheets.Remove(2) CATIA.ActiveDoc
                | ument.DrawingSheets.Remove("SheetToBeRemoved")

        :param i_index:
        :return:
        """
        return self.drawing_sheets.Remove(i_index)

    def __repr__(self):
        return f'DrawingSheets(name="{self.name}")'
