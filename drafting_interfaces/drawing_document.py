#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.drafting_interfaces.drawing_root import DrawingRoot
from pycatia.drafting_interfaces.drawing_sheets import DrawingSheets
from pycatia.in_interfaces.document import Document
from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.knowledge_interfaces.relations import Relations


class DrawingDocument(Document):

    """
        .. note::
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
    def drawing_root(self):
        """
        .. note::
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

        :return: DrawingRoot
        """

        return DrawingRoot(self.drawing_document.DrawingRoot)

    @property
    def parameters(self):
        """
        .. note::
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

        :return: Parameters
        """

        return Parameters(self.drawing_document.Parameters)

    @property
    def relations(self):
        """
        .. note::
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

        :return: Relations
        """

        return Relations(self.drawing_document.Relations)

    @property
    def sheets(self):
        """
        .. note::
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

        :return: DrawingSheets
        """

        return DrawingSheets(self.drawing_document.Sheets)

    @property
    def standard(self):
        """
        .. note::
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
        """

        return self.drawing_document.Standard

    @standard.setter
    def standard(self, value):
        """
        :param enum cat_drawing_standard value:
        """

        self.drawing_document.Standard = value

    def isolate(self):
        """
        .. note::
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

        :return: None
        """
        return self.drawing_document.Isolate()

    def update(self):
        """
        .. note::
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

        :return: None
        """
        return self.drawing_document.Update()

    def __repr__(self):
        return f'DrawingDocument(name="{ self.name }")'
