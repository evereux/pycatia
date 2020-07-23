#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.drafting_interfaces.drawing_sheet import DrawingSheet
from pycatia.drafting_interfaces.drawing_sheets import DrawingSheets
from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.knowledge_interfaces.relations import Relations
from pycatia.system_interfaces.any_object import AnyObject


class DrawingRoot(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingRoot
                | 
                | Represents the drawing object in drawing documents.
                | 
                | Warning: This interface is not available with 2D Layout for 3D
                | Design.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_root = com_object

    @property
    def active_sheet(self) -> DrawingSheet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ActiveSheet() As DrawingSheet
                | 
                |     Retrieves or sets the active sheet of the drawing.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves the active sheet in the drawing of the active
                |         document, supposed to be a drawing document.
                | 
                |          CATIA.ActiveDocument.DrawingRoot.GetActiveSheet

        :return: DrawingSheet
        :rtype: DrawingSheet
        """

        return DrawingSheet(self.drawing_root.ActiveSheet)

    @active_sheet.setter
    def active_sheet(self, value: DrawingSheet):
        """
        :param DrawingSheet value:
        """

        self.drawing_root.ActiveSheet = value

    @property
    def parameters(self) -> Parameters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Parameters() As Parameters (Read Only)
                | 
                |     Returns the collection of parameters of the drawing
                |     document.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |           This example retrieves in DrawingParameters the collection
                |           of
                |          parameters currently managed by the active document, supposed to be
                |          a
                |          drawing document.
                |          
                | 
                |          Dim DrawingParameters As Parameters
                |          Set DrawingParameters = CATIA.ActiveDocument.Parameters

        :return: Parameters
        :rtype: Parameters
        """

        return Parameters(self.drawing_root.Parameters)

    @property
    def relations(self) -> Relations:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Relations() As Relations (Read Only)
                | 
                |     Returns the collection of relations of the drawing
                |     document.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |           This example retrieves in DrawingRelations the collection
                |           of
                |          relations currently managed by the active document, supposed to be
                |          a
                |          drawing document.
                |          
                | 
                |          Dim DrawingRelations As Relations
                |          Set DrawingRelations = CATIA.ActiveDocument.Relations

        :return: Relations
        :rtype: Relations
        """

        return Relations(self.drawing_root.Relations)

    @property
    def sheets(self) -> DrawingSheets:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Sheets() As DrawingSheets (Read Only)
                | 
                |     Returns the collection of drawing sheets of the drawing
                |     document.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in SheetCollection the collection of sheets
                |         currently managed by the active document, supposed to be a drawing
                |         document.
                | 
                |          Dim SheetCollection As DrawingSheets
                |          Set SheetCollection = CATIA.ActiveDocument.Sheets

        :return: DrawingSheets
        :rtype: DrawingSheets
        """

        return DrawingSheets(self.drawing_root.Sheets)

    @property
    def standard(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Standard() As CatDrawingStandard
                | 
                |     Returns or sets the drawing standard of the drawing
                |     document.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example sets the drawing standard of the active document, supposed
                |         to be a drawing document, to ISO.
                | 
                |          CATIA.ActiveDocument.Standard = catISO

        :return: int
        :rtype: int
        """

        return self.drawing_root.Standard

    @standard.setter
    def standard(self, value: int):
        """
        :param int value:
        """

        self.drawing_root.Standard = value

    def isolate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Isolate()
                | 
                |     Isolates all the drawing views of all the drawing sheets of the drawing
                |     document.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example isolates all the drawing views of all the drawing sheets
                |         of the active document, supposed to be a drawing
                |         document.
                | 
                |          CATIA.ActiveDocument.Isolate

        :return: None
        :rtype: None
        """
        return self.drawing_root.Isolate()

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Update()
                | 
                |     Updates all the drawing sheets of the drawing document.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example updates the active document, supposed to be a drawing
                |         document.
                | 
                |          CATIA.ActiveDocument.Update

        :return: None
        :rtype: None
        """
        return self.drawing_root.Update()

    def reorder_sheets(self, i_ordered_sheets: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub reorder_Sheets(CATSafeArrayVariant iOrderedSheets)
                | 
                |     Changes the positions of the sheets in this drawing according to the given
                |     ordered list. iOrderedSheets is the result of a permutation applied to the list
                |     of all the sheets of this drawing, with the following constraint: For every
                |     non-detail sheet, there is not any detail sheet appearing before in
                |     iOrderedSheets.
                | 
                |     Example:
                |         This example inverts the sheet order of a drawing made of exactly two
                |         regular sheets.
                | 
                |          Set drwsheets = CATIA.ActiveDocument.Sheets
                |          Set drwsheetsorder =  CATIA.ActiveDocument.DrawingRoot
                |          Set sheet1 = drwsheets.item(1)
                |          Set sheet2 = drwsheets.item(2)
                |          newsheetorder = Array(sheet2, sheet1)
                |          drwsheetsorder.reorder_Sheets(newsheetorder)

        :param tuple i_ordered_sheets:
        :return: None
        :rtype: None
        """
        i_ordered_sheets = [x.com_object for x in i_ordered_sheets]
        return self.drawing_root.reorder_Sheets(i_ordered_sheets)

    def __repr__(self):
        return f'DrawingRoot(name="{self.name}")'
