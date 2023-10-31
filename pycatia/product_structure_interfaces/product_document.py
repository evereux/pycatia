#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.document import Document
from pycatia.product_structure_interfaces.product import Product


class ProductDocument(Document):

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
                |                         ProductDocument
                | 
                | Represents the Document object for product structures.
                | When a ProductDocument is created, a root product is created whose parent is
                | the ProductDocument object. Its default name is RootProduct, which can be
                | overwritten thanks to the the AnyObject.Name property. This root product is at
                | the top of the product tree structure contained in the document. It has no
                | difference with the other contained products, except it has no father product
                | in the product tree structure within the document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.product_document = com_object

    @property
    def product(self) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Product() As Product (Read Only)
                | 
                |     Returns the root product.
                | 
                |     Example:
                | 
                |           This example retrieves the root product of the
                |           MyProductDoc
                |          ProductDocument in RootProduct.
                |          
                | 
                |          Dim RootProduct As Product
                |          Set RootProduct = MyProductDoc.Product

        :rtype: Product
        """

        return Product(self.product_document.Product)

    def __repr__(self):
        return f'ProductDocument(name="{ self.name }")'
