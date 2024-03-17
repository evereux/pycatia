#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.drafting_interfaces.drawing_sheet import DrawingSheet
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class DrawingSheets(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingSheets
                | 
                | A collection of all the drawing sheets currently managed by the drawing
                | document.
                | 
                | Warning: This interface is not available with 2D Layout for 3D
                | Design.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingSheet)
        self.drawing_sheets = com_object

    @property
    def active_sheet(self) -> DrawingSheet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ActiveSheet() As DrawingSheet (Read Only)
                | 
                |     Returns the active drawing sheet of the drawing document.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         The following example retrieves in SheetToWorkIn the active drawing
                |         sheet of the drawing document named CATDrawing1.
                | 
                |          Dim MyDrawingDoc As Document
                |          Set MyDrawingDoc = CATIA.Documents.Item("CATDrawing1")
                |          Dim SheetToWorkIn As DrawingSheet
                |          Set SheetToWorkIn =  MyDrawingDoc.Sheets.ActiveSheet

        :rtype: DrawingSheet
        """

        return DrawingSheet(self.drawing_sheets.ActiveSheet)

    def add(self, i_drawing_sheet_name: str) -> DrawingSheet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add(CATBSTR iDrawingSheetName) As DrawingSheet
                | 
                |     Creates a drawing sheet and adds it to the DrawingSheets collection. This
                |     drawing sheet becomes the active one.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iDrawingSheetName
                |             The name to assign to the created DrawingSheet object
                |             
                | 
                |     Returns:
                |         The created drawing sheet 
                |     Example:
                |         The following example creates a drawing sheet named FirstSheet and
                |         retrieved in MySheet in the drawing sheet collection of the document named
                |         CATDrawing1.
                | 
                |          Dim MyDrawingDoc As Document
                |          Set MyDrawingDoc = CATIA.Documents.Item("CATDrawing1")
                |          Dim MySheet As DrawingSheet
                |          Set MySheet = MyDrawingDoc.Sheets.Add("FirstSheet")

        :param str i_drawing_sheet_name:
        :rtype: DrawingSheet
        """
        return DrawingSheet(self.drawing_sheets.Add(i_drawing_sheet_name))

    def add_detail(self, i_drawing_sheet_name: str) -> DrawingSheet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func AddDetail(CATBSTR iDrawingSheetName) As DrawingSheet
                | 
                |     Creates a detail drawing sheet and adds it to the DrawingSheets collection.
                |     This detail drawing sheet becomes the active one.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iDrawingSheetName
                |             The name to assign to the created detail DrawingSheet object
                |             
                | 
                |     Returns:
                |         The created drawing sheet 
                |     Example:
                |         The following example creates a detail drawing sheet named FirstSheet
                |         and retrieved in MySheet in the drawing sheet collection of the document named
                |         CATDrawing1.
                | 
                |          Dim MyDrawingDoc As Document
                |          Set MyDrawingDoc = CATIA.Documents.Item("CATDrawing1")
                |          Dim MySheet As DrawingSheet
                |          Set MySheet = MyDrawingDoc.Sheets.Add("FirstSheet")

        :param str i_drawing_sheet_name:
        :rtype: DrawingSheet
        """
        return DrawingSheet(self.drawing_sheets.AddDetail(i_drawing_sheet_name))

    def item(self, i_index: cat_variant) -> DrawingSheet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As DrawingSheet
                | 
                |     Returns a drawing sheet using its index or its name from the DrawingSheets
                |     collection.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the drawing sheet to retrieve from the
                |             collection of drawing sheets. As a numerics, this index is the rank of the
                |             drawing sheet in the collection. The index of the first drawing sheet in the
                |             collection is 1, and the index of the last drawing sheet is Count. As a string,
                |             it is the name you assigned to the drawing sheet using the
                |             
                | 
                |         AnyObject.Name property or when creating it using the Add method.
                |         
                |     Returns:
                |         The retrieved drawing sheet 
                |     Example:
                |         This example retrieves in ThisDrawingSheet the third drawing sheet, and
                |         in ThatDrawingSheet the drawing sheet named MySheet in the drawing sheet
                |         collection of the active document, supposed to be a drawing
                |         document.
                | 
                |          Dim ThisDrawingSheet As DrawingSheet
                |          Set ThisDrawingSheet = CATIA.ActiveDocument.Sheets.Item(3)
                |          Dim ThatDrawingSheet As DrawingSheet
                |          Set ThatDrawingSheet = CATIA.ActiveDocument.Sheets.Item("MySheet")

        :param cat_variant i_index:
        :rtype: DrawingSheet
        """
        return DrawingSheet(self.drawing_sheets.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a drawing sheet from the DrawingSheets collection.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the drawing sheet to remove from the
                |             collection of drawing sheets. As a numerics, this index is the rank of the
                |             drawing sheet in the collection. The index of the first drawing sheet in the
                |             collection is 1, and the index of the last drawing sheet is Count. As a string,
                |             it is the name you assigned to the drawing sheet using the
                |             
                | 
                |         AnyObject.Name property or when creating it using the Add method.
                |         
                |     Example:
                |         The following example removes the second drawing sheet and the drawing
                |         sheet named SheetToBeRemoved in the drawing sheet collection of the active
                |         document, supposed to be a drawing document.
                | 
                |         CATIA.ActiveDocument.DrawingSheets.Remove(2)
                |         CATIA.ActiveDocument.DrawingSheets.Remove("SheetToBeRemoved")

        :param cat_variant i_index:
        :return: None
        """
        return self.drawing_sheets.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingSheet:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingSheet(self.drawing_sheets.Item(n + 1))

    def __iter__(self) -> Iterator[DrawingSheet]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DrawingSheets(name="{self.name}")'
