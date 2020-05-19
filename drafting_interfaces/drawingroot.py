#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25

from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.knowledge_interfaces.relations import Relations
from pycatia.system_interfaces.base_object import AnyObject
from .drawingsheet import DrawingSheet
from .drawingsheets import DrawingSheets


class DrawingRoot(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the drawing object in drawing documents.Warning: This
                | interface is not available with 2D Layout for 3D Design.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_root = com_object

    @property
    def active_sheet(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ActiveSheet
                | o Property ActiveSheet(    ) As
                | 
                | Retrieves or sets the active sheet of the drawing. Warning: This
                | method is not available with 2D Layout for 3D Design. Example: This
                | example retrieves the active sheet in the drawing of the active
                | document, supposed to be a drawing document.
                | CATIA.ActiveDocument.DrawingRoot.GetActiveSheet


        :return: DrawingSheet()
        """
        return DrawingSheet(self.drawing_root.ActiveSheet)

    @property
    def parameters(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Parameters
                | o Property Parameters(    ) As   (Read Only)
                | 
                | Returns the collection of parameters of the drawing document. Warning:
                | This method is not available with 2D Layout for 3D Design.  Example:
                | This example retrieves in DrawingParameters the collection of
                | parameters currently managed by the active document, supposed to be a
                | drawing document.  Dim DrawingParameters As Parameters Set
                | DrawingParameters = CATIA.ActiveDocument.Parameters

        :return: Parameters()
        """
        return Parameters(self.drawing_root.Parameters)

    @property
    def relations(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Relations
                | o Property Relations(    ) As   (Read Only)
                | 
                | Returns the collection of relations of the drawing document. Warning:
                | This method is not available with 2D Layout for 3D Design.  Example:
                | This example retrieves in DrawingRelations the collection of relations
                | currently managed by the active document, supposed to be a drawing
                | document.  Dim DrawingRelations As Relations Set DrawingRelations =
                | CATIA.ActiveDocument.Relations


        :return: Relations()
        """
        return Relations(self.drawing_root.Relations)

    @property
    def sheets(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Sheets
                | o Property Sheets(    ) As   (Read Only)
                | 
                | Returns the collection of drawing sheets of the drawing document.
                | Warning: This method is not available with 2D Layout for 3D Design.
                | Example: This example retrieves in SheetCollection the collection of
                | sheets currently managed by the active document, supposed to be a
                | drawing document.  Dim SheetCollection As DrawingSheets Set
                | SheetCollection = CATIA.ActiveDocument.Sheets


        :return:
        """
        return DrawingSheets(self.drawing_root.Sheets)

    @property
    def standard(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Standard
                | o Property Standard(    ) As
                | 
                | Returns or sets the drawing standard of the drawing document. Warning:
                | This method is not available with 2D Layout for 3D Design. Example:
                | This example sets the drawing standard of the active document,
                | supposed to be a drawing document, to ISO.
                | CATIA.ActiveDocument.Standard = catISO

        :return: int enumeration_type
        """
        return self.drawing_root.Standard

    @standard.setter
    def standard(self, value):
        """
            :param int value:
        """
        self.drawing_root.Standard = value

    def isolate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Isolate
                | o Sub Isolate(    )
                | 
                | Isolates all the drawing views of all the drawing sheets of the
                | drawing document. Warning: This method is not available with 2D Layout
                | for 3D Design. Example: This example isolates all the drawing views of
                | all the drawing sheets of the active document, supposed to be a
                | drawing document.  CATIA.ActiveDocument.Isolate

        :return:
        """
        self.drawing_root.Isolate()

    def update(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Update
                | o Sub Update(    )
                | 
                | Updates all the drawing sheets of the drawing document. Warning: This
                | method is not available with 2D Layout for 3D Design. Example: This
                | example updates the active document, supposed to be a drawing
                | document.  CATIA.ActiveDocument.Update

      |
                | Parameters:

      |

        :return:
        """
        return self.drawing_root.Update()

    def reorder_sheets(self, i_ordered_sheets):
        """
        .. note::
            CAA V5 Visual Basic help

                | reorder_Sheets
                | o Sub reorder_Sheets(        iOrderedSheets)
                | 
                | Changes the positions of the sheets in this drawing according to the
                | given  ordered list. iOrderedSheets is the result of a permutation
                | applied to  the list of all the sheets of this drawing, with the
                | following  constraint: For every non-detail sheet, there is not any
                | detail sheet  appearing before in iOrderedSheets.
                |
                | Example: This example inverts the sheet order of a drawing made of exactly two
                | regular sheets.
                | Set drwsheets = CATIA.ActiveDocument.Sheets
                | Set drwsheetsorder =  CATIA.ActiveDocument.DrawingRoot
                | Set sheet1 = drwsheets.item(1)
                | Set sheet2 = drwsheets.item(2)
                | newsheetorder = Array(sheet2, sheet1)
                | drwsheetsorder.reorder_Sheets(newsheetorder)


        :param tuple i_ordered_sheets:
        :return:
        """
        order = [x.com_object for x in i_ordered_sheets]
        return self.drawing_root.reorder_Sheets(order)

    def __repr__(self):
        return f'DrawingRoot(name="{self.name}")'
