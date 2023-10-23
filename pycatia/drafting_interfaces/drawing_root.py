#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.drafting_interfaces.drawing_sheet import DrawingSheet
from pycatia.drafting_interfaces.drawing_document import DrawingDocument


class DrawingRoot(DrawingDocument):
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
        self.drawing_root_com = com_object

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

        :rtype: DrawingSheet
        """

        return DrawingSheet(self.drawing_root_com.ActiveSheet)

    @active_sheet.setter
    def active_sheet(self, value: DrawingSheet):
        """
        :param DrawingSheet value:
        """

        self.drawing_root_com.ActiveSheet = value

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
        :rtype: None
        """
        sheets = [x.com_object for x in i_ordered_sheets]
        return self.drawing_root_com.reorder_Sheets(sheets)

    def __repr__(self):
        return f'DrawingRoot(name="{self.name}")'
