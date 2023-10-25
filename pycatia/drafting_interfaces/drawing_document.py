#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import TYPE_CHECKING

from pycatia.drafting_interfaces.drawing_sheets import DrawingSheets
from pycatia.in_interfaces.document import Document
from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.knowledge_interfaces.relations import Relations

if TYPE_CHECKING:
    from pycatia.drafting_interfaces.drawing_root import DrawingRoot


class DrawingDocument(Document):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Document
                |                         DrawingDocument
                | 
                | Represents the Document object for drawings.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_document = com_object

    @property
    def drawing_root(self) -> 'DrawingRoot':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DrawingRoot() As DrawingRoot (Read Only)
                | 
                |     Retrieves the drawing root in the drawing document.
                | 
                |     Example:
                |         This example retrieves the drawing from the active document, supposed
                |         to be a drawing document.
                | 
                |          CATIA.ActiveDocument.DrawingRoot

        :rtype: DrawingRoot
        """
        from pycatia.drafting_interfaces.drawing_root import DrawingRoot
        return DrawingRoot(self.drawing_document.DrawingRoot)

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

        :rtype: Parameters
        """

        return Parameters(self.drawing_document.Parameters)

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

        :rtype: Relations
        """

        return Relations(self.drawing_document.Relations)

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
                | 
                |     Example:
                |         This example retrieves in SheetCollection the collection of sheets
                |         currently managed by the active document, supposed to be a drawing
                |         document.
                | 
                |          Dim SheetCollection As DrawingSheets
                |          Set SheetCollection = CATIA.ActiveDocument.Sheets

        :rtype: DrawingSheets
        """

        return DrawingSheets(self.drawing_document.Sheets)

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
                | 
                |     Example:
                |         This example sets the drawing standard of the active document, supposed
                |         to be a drawing document, to ISO.
                | 
                |          CATIA.ActiveDocument.Standard = catISO

        :return: enum cat_drawing_standard
        :rtype: int
        """

        return self.drawing_document.Standard

    @standard.setter
    def standard(self, value: int):
        """
        :param int value: enum cat_drawing_standard
        """

        self.drawing_document.Standard = value

    def isolate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Isolate()
                | 
                |     Isolates all the drawing views of all the drawing sheets of the drawing
                |     document.
                | 
                |     Example:
                |         This example isolates all the drawing views of all the drawing sheets
                |         of the active document, supposed to be a drawing
                |         document.
                | 
                |          CATIA.ActiveDocument.Isolate

        :rtype: None
        """
        return self.drawing_document.Isolate()

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Update()
                | 
                |     Updates all the drawing sheets of the drawing document.
                | 
                |     Example:
                |         This example updates the active document, supposed to be a drawing
                |         document.
                | 
                |          CATIA.ActiveDocument.Update

        :rtype: None
        """
        return self.drawing_document.Update()

    def __repr__(self):
        return f'DrawingDocument(name="{self.name}")'
