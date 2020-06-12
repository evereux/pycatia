#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.in_interfaces.document import Document
from pycatia.product_structure_interfaces.product import Product
from .part import Part


class PartDocument(Document):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the Document object for parts.Role: When a PartDocument
                | object is created, a Part object is also created. This Part object is
                | the root object  of the Part structure.A reference Product object is
                | also created in each PartDocument. It is used to access Publications,
                | PartNumber.

    """

    def __init__(self, part_document_com_object):
        super().__init__(part_document_com_object)
        self.partdocument = part_document_com_object

    @property
    def part(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Part
                | o Property Part() As Part
                | 
                | Returns the root Part object from the current part document.
                | Example:The following example retrieves in RootPart the root Part
                | object of the active document, assumed to be a part document:  Set
                | RootPart = CATIA.ActiveDocument.Part


                | Parameters:


        """
        return Part(self.partdocument.Part)

    @property
    def product(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Product
                | o Property Product() As Product
                | 
                | Returns the root Product object from the current part document.
                | Example:The following example retrieves in RootProd the root Product
                | object of the active document, assumed to be a part document:  Set
                | RootProd = CATIA.ActiveDocument.Part


                | Parameters:


        """
        return Product(self.partdocument.Product)

    def __repr__(self):
        return f'PartDocument'
