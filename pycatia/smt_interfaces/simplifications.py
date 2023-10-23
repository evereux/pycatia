#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.document import Document
from pycatia.navigator_interfaces.group import Group
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.collection import Collection


class Simplifications(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Simplifications
                | 
                | Interface to compute Simplifications.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.simplifications = com_object

    def compute_simplification(self, group_of_selected_products: Group, i_accuracy: float) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeSimplification(Group GroupOfSelectedProducts,
                | double iAccuracy) As Document
                | 
                |     Computes a simplification on the selected products.
                | 
                |     Parameters:
                | 
                |         GroupOfSelectedProducts
                |             The selected products on which you want to perform the
                |             simplification. 
                |         iAccuracy
                |             Accuracy for simplification. 
                | 
                |     Returns:
                |         SimplificationDocument: Document containing the result.

        :param Group group_of_selected_products:
        :param float i_accuracy:
        :rtype: Document
        """
        return Document(self.simplifications.ComputeSimplification(group_of_selected_products.com_object, i_accuracy))

    def compute_simplification_with_a_reference(
            self,
            i_group_of_selected_products: Group,
            i_reference_product: Product,
            i_accuracy: float
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeSimplificationWithAReference(Group
                | iGroupOfSelectedProducts,
                | Product iReferenceProduct,
                | double iAccuracy) As Document
                | 
                |     Computes a simplification on the selected products, according to a
                |     reference product.
                | 
                |     Parameters:
                | 
                |         iGroupOfSelectedProducts
                |             The selected products on which you want to perform the
                |             simplification. 
                |         iReferenceProduct
                |             Product taken as a reference. 
                |         iAccuracy
                |             Accuracy for simplification. 
                | 
                |     Returns:
                |         SimplificationDocument: Document containing the result.

        :param Group i_group_of_selected_products:
        :param Product i_reference_product:
        :param float i_accuracy:
        :rtype: Document
        """
        return Document(
            self.simplifications.ComputeSimplificationWithAReference(
                i_group_of_selected_products.com_object,
                i_reference_product.com_object,
                i_accuracy
            )
        )

    def simplification_shape_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func SimplificationShapeName() As CATBSTR
                | 
                |     Returns the name of the associated shape.

        :rtype: str
        """
        return self.simplifications.SimplificationShapeName()

    def __repr__(self):
        return f'Simplifications(name="{self.name}")'
