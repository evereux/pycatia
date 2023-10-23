#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from pycatia.in_interfaces.document import Document
from pycatia.mec_mod_interfaces.part import Part
from pycatia.product_structure_interfaces.product import Product


class PartDocument(Document):

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
                |                         PartDocument
                |
                | Represents the Document object for parts.
                |
                | Role: When a PartDocument object is created, a Part object is also created.
                | This Part object is the root object of the Part structure.
                |
                | A reference Product object is also created in each PartDocument. It is used to
                | access Publications, PartNumber.
                |
                | See also:
                |     Product, Part

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.part_document = com_object

    @property
    def part(self) -> Part:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Part() As Part (Read Only)
                | 
                |     Returns the root Part object from the current part
                |     document.
                | 
                |     Example:
                |         The following example retrieves in RootPart the root Part object of the
                |         active document, assumed to be a part document:
                | 
                |          Set RootPart = CATIA.ActiveDocument.Part

        :rtype: Part
        """

        return Part(self.part_document.Part)

    @property
    def product(self) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Product() As Product (Read Only)
                | 
                |     Returns the root Product object from the current part
                |     document.
                | 
                |     Example:
                |         The following example retrieves in RootProd the root Product object of
                |         the active document, assumed to be a part document:
                | 
                |          Set RootProd = CATIA.ActiveDocument.Part

        :rtype: Product
        """

        return Product(self.part_document.Product)

    def __repr__(self):
        return f'PartDocument(name="{ self.name }")'
