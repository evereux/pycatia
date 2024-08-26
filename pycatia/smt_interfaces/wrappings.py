#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.in_interfaces.document import Document
from pycatia.navigator_interfaces.group import Group
from pycatia.product_structure_interfaces.product import Product
from pycatia.smt_interfaces.wrapping import Wrapping
from pycatia.system_interfaces.collection import Collection


class Wrappings(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Wrappings
                | 
                | Interface to compute Wrappings
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Wrapping)
        self.wrappings = com_object

    def add(
            self,
            i_product_to_wrapping: Product,
            i_accuracy: float,
            i_ratio: float,
            i_shape_name: str,
            i_activated_shape: int,
            i_default_shape: int
    ) -> Wrapping:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(Product iProductToWrapping,
                | double iAccuracy,
                | double iRatio,
                | CATBSTR iShapeName,
                | long iActivatedShape,
                | long iDefaultShape) As Wrapping
                | 
                |     Compute a wrapping on the selected products. This method is
                |     deprecated!
                | 
                |     Parameters:
                | 
                |         iProductToWrapping
                |             The selected products on which you want to perform a wrapping.
                |             
                |         iAccuracy
                |             The grain accuracy. 
                |         iRatio
                |             The ratio. 
                |         iShapeName
                |             The associated shape name. 
                |         iActivatedShape
                |             Do we activate the shape ? 
                |         iDefaultShape
                |             Do we activate the shape as default shape ? 
                | 
                |     Returns:
                |         oWrapping: Document containing the result.

        :param Product i_product_to_wrapping:
        :param float i_accuracy:
        :param float i_ratio:
        :param str i_shape_name:
        :param int i_activated_shape:
        :param int i_default_shape:
        :rtype: Wrapping
        """
        return Wrapping(
            self.wrappings.Add(
                i_product_to_wrapping.com_object,
                i_accuracy,
                i_ratio,
                i_shape_name,
                i_activated_shape,
                i_default_shape
            )
        )

    def clean_up(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CleanUp()
                | 
                |     Cleans up.

        :rtype: None
        """
        return self.wrappings.CleanUp()

    def compute_a_wrapping(
            self,
            group_of_selected_products: Group,
            i_accuracy: float,
            i_ration: float,
            i_accuracy_for_simplification: float
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeAWrapping(Group GroupOfSelectedProducts,
                | double iAccuracy,
                | double iRation,
                | double iAccuracyForSimplification) As Document
                | 
                |     Compute a wrapping on the selected products.
                | 
                |     Parameters:
                | 
                |         GroupOfSelectedProducts
                |             The selected products on which you want to perform a wrapping.
                |             
                |         iAccuracy
                |             The grain accuracy. 
                |         iRation
                |             The ratio. 
                |         iAccuracyForSimplification
                |             The accuracy for the simplification. equals -1 if no simplification
                |             is to be performed. 
                | 
                |     Returns:
                |         WrappingDocument: Document containing the result.

        :param Group group_of_selected_products:
        :param float i_accuracy:
        :param float i_ration:
        :param float i_accuracy_for_simplification:
        :rtype: Document
        """
        return Document(
            self.wrappings.ComputeAWrapping(
                group_of_selected_products.com_object,
                i_accuracy,
                i_ration,
                i_accuracy_for_simplification
            )
        )

    def compute_a_wrapping_with_a_reference(
            self,
            i_group_of_selected_products: Group,
            i_reference_product: Product,
            i_accuracy: float,
            i_ration: float,
            i_accuracy_for_simplification: float
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeAWrappingWithAReference(Group
                | iGroupOfSelectedProducts,
                | Product iReferenceProduct,
                | double iAccuracy,
                | double iRation,
                | double iAccuracyForSimplification) As Document
                | 
                |     Compute a wrapping on the selected products, according to a reference
                |     product.
                | 
                |     Parameters:
                | 
                |         GroupOfSelectedProducts
                |             The selected products on which you want to perform a wrapping.
                |             
                |         iReferenceProduct
                |             Product taken as a reference. 
                |         iAccuracy
                |             The grain accuracy. 
                |         iRation
                |             The ratio. 
                |         iAccuracyForSimplification
                |             The accuracy for the simplification. equals -1 if no simplification
                |             is to be performed. 
                | 
                |     Returns:
                |         WrappingDocument: Document containing the result.

        :param Group i_group_of_selected_products:
        :param Product i_reference_product:
        :param float i_accuracy:
        :param float i_ration:
        :param float i_accuracy_for_simplification:
        :rtype: Document
        """
        return Document(
            self.wrappings.ComputeAWrappingWithAReference(
                i_group_of_selected_products.com_object,
                i_reference_product.com_object,
                i_accuracy,
                i_ration,
                i_accuracy_for_simplification
            )
        )

    def compute_wrapping_with_convex_hull(
            self,
            i_group_of_selected_products: Group,
            i_reference_product: Product,
            i_accuracy: float,
            i_perform_simplification: bool,
            i_accuracy_for_simplification: float
    ) -> Document:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func ComputeWrappingWithConvexHull(Group iGroupOfSelectedProducts,Product
                | iReferenceProduct,double iAccuracy,boolean iPerformSimplification,double
                | iAccuracyForSimplification) As Document
                |     Compute a wrapping using convex hull algorithm on the selected products,
                |     according to a reference product.
                |
                |     Parameters:
                |
                |         iGroupOfSelectedProducts
                |             The selected products to wrap.
                |         iReferenceProduct
                |             Product taken as a reference.
                |         iAccuracy
                |             The grain accuracy (accuracy value > 0 and units in mm).
                |
                |         iPerformSimplification
                |             set to true for simplification and set to false for no
                |             simplification
                |         iAccuracyForSimplification
                |             The accuracy for the simplification (accuracy value > 0 and units
                |             in mm). The accuracy value is taken into account only if the @param
                |             iPerformSimplification is set to true.
                |
                |     Returns:
                |         WrappingDocument: Document containing the result.

        :param Group i_group_of_selected_products:
        :param Product i_reference_product:
        :param float i_accuracy:
        :param bool i_perform_simplification:
        :param float i_accuracy_for_simplification:
        :rtype: Document
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return Document(
            self.wrappings.ComputeWrappingWithConvexHull(
                i_group_of_selected_products.com_object,
                i_reference_product.com_object,
                i_accuracy,
                i_perform_simplification,
                i_accuracy_for_simplification
            )
        )

    def wrapping_shape_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func WrappingShapeName() As CATBSTR
                | 
                |     Returns the name of the associated shape.

        :rtype: str
        """
        return self.wrappings.WrappingShapeName()

    def __repr__(self):
        return f'Wrappings(name="{self.name}")'
