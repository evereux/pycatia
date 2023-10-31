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
from pycatia.smt_interfaces.dmo_thickness import DMOThickness
from pycatia.system_interfaces.collection import Collection


class DMOThicknesses(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DMOThicknesses
                | 
                | Interface to access a CATIADMOThicknesses and compute
                | Thicknesses
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dmo_thicknesses = com_object

    def add(
            self,
            i_product_to_thickness: Product,
            i_thickness1: float,
            i_thickness2: float,
            i_use_constraints: int,
            i_constraints: tuple,
            i_shape_name: str,
            i_activated_shape: int,
            i_default_shape: int
    ) -> DMOThickness:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(Product iProductToThickness,
                | double iThickness1,
                | double iThickness2,
                | long iUseConstraints,
                | CATSafeArrayVariant iConstraints,
                | CATBSTR iShapeName,
                | long iActivatedShape,
                | long iDefaultShape) As DMOThickness
                | 
                |     Creates a new Silhouette and adds it to the DMOThicknesses collection. This
                |     function is deprecated.

        :param Product i_product_to_thickness:
        :param float i_thickness1:
        :param float i_thickness2:
        :param int i_use_constraints:
        :param tuple i_constraints:
        :param str i_shape_name:
        :param int i_activated_shape:
        :param int i_default_shape:
        :rtype: DMOThickness
        """
        return DMOThickness(
            self.dmo_thicknesses.Add(
                i_product_to_thickness.com_object,
                i_thickness1,
                i_thickness2,
                i_use_constraints,
                i_constraints,
                i_shape_name,
                i_activated_shape,
                i_default_shape
            )
        )

    def compute_a_thickness(
            self,
            group_of_selected_products: Group,
            i_thickness1: float,
            i_thickness2: float,
            i_use_constraints: int,
            i_constraints: tuple
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeAThickness(Group GroupOfSelectedProducts,
                | double iThickness1,
                | double iThickness2,
                | long iUseConstraints,
                | CATSafeArrayVariant iConstraints) As Document
                | 
                |     Compute a thickness on the selected products. This method is
                |     deprecated.
                | 
                |     Parameters:
                | 
                |         GroupOfSelectedProducts
                |             The selected products on which you want to perform the thickness.
                |             
                |         iThickness1
                |             First thickness value. 
                |         iThickness2
                |             Second thickness value. Old way 
                |         iUseConstraints
                |             Do we use normals constraints or not ? 
                |         iConstraints
                |             Constraints array. 
                | 
                |     Returns:
                |         ThicknessDocument: Document containing the result.

        :param Group group_of_selected_products:
        :param float i_thickness1:
        :param float i_thickness2:
        :param int i_use_constraints:
        :param tuple i_constraints:
        :rtype: Document
        """
        return Document(
            self.dmo_thicknesses.ComputeAThickness(
                group_of_selected_products.com_object,
                i_thickness1,
                i_thickness2,
                i_use_constraints,
                i_constraints
            )
        )

    def compute_a_thickness_with_a_reference(
            self,
            i_group_of_selected_products: Group,
            i_reference_product: Product,
            i_thickness1: float,
            i_thickness2: float,
            i_use_constraints: int,
            i_constraints: tuple
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeAThicknessWithAReference(Group
                | iGroupOfSelectedProducts,
                | Product iReferenceProduct,
                | double iThickness1,
                | double iThickness2,
                | long iUseConstraints,
                | CATSafeArrayVariant iConstraints) As Document
                | 
                |     Compute a thickness on the selected products, according to a reference
                |     product. This method is deprecated.
                | 
                |     Parameters:
                | 
                |         iGroupOfSelectedProducts
                |             The selected products on which you want to perform the thickness.
                |             
                |         iReferenceProduct
                |             The reference product. 
                |         iThickness1
                |             First thickness value. 
                |         iThickness2
                |             Second thickness value. Old way 
                |         iUseConstraints
                |             Do we use normals constraints or not ? 
                |         iConstraints
                |             Constraints array. 
                | 
                |     Returns:
                |         ThicknessDocument: Document containing the result.

        :param Group i_group_of_selected_products:
        :param Product i_reference_product:
        :param float i_thickness1:
        :param float i_thickness2:
        :param int i_use_constraints:
        :param tuple i_constraints:
        :rtype: Document
        """
        return Document(
            self.dmo_thicknesses.ComputeAThicknessWithAReference(
                i_group_of_selected_products.com_object,
                i_reference_product.com_object,
                i_thickness1,
                i_thickness2,
                i_use_constraints,
                i_constraints
            )
        )

    def compute_thickness(
            self,
            group_of_selected_products: Group,
            i_thickness1: float,
            i_thickness2: float,
            i_use_constraints: int,
            i_constraints: tuple
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeThickness(Group GroupOfSelectedProducts,
                | double iThickness1,
                | double iThickness2,
                | long iUseConstraints,
                | CATSafeArrayVariant iConstraints) As Document
                | 
                |     Compute a thickness on the selected products.
                | 
                |     Parameters:
                | 
                |         GroupOfSelectedProducts
                |             The selected products on which you want to perform the thickness.
                |             
                |         iThickness1
                |             First thickness value. 
                |         iThickness2
                |             Second thickness value. 
                |         iUseConstraints
                |             Do we use normals constraints or not ? 
                |         iConstraints
                |             Constraints array. 
                | 
                |     Returns:
                |         ThicknessDocument: Document containing the result.

        :param Group group_of_selected_products:
        :param float i_thickness1:
        :param float i_thickness2:
        :param int i_use_constraints:
        :param tuple i_constraints:
        :rtype: Document
        """
        return Document(
            self.dmo_thicknesses.ComputeThickness(
                group_of_selected_products.com_object,
                i_thickness1,
                i_thickness2,
                i_use_constraints,
                i_constraints
            )
        )

    def compute_thickness_with_reference(
            self,
            i_group_of_selected_products: Group,
            i_reference_product: Product,
            i_thickness1: float,
            i_thickness2: float,
            i_use_constraints: int,
            i_constraints: tuple
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeThicknessWithReference(Group
                | iGroupOfSelectedProducts,
                | Product iReferenceProduct,
                | double iThickness1,
                | double iThickness2,
                | long iUseConstraints,
                | CATSafeArrayVariant iConstraints) As Document
                | 
                |     Compute a thickness on the selected products, according to a reference
                |     product.
                | 
                |     Parameters:
                | 
                |         iGroupOfSelectedProducts
                |             The selected products on which you want to perform the thickness.
                |             
                |         iReferenceProduct
                |             The reference product. 
                |         iThickness1
                |             First thickness value. 
                |         iThickness2
                |             Second thickness value. 
                |         iUseConstraints
                |             Do we use normals constraints or not ? 
                |         iConstraints
                |             Constraints array. 
                | 
                |     Returns:
                |         ThicknessDocument: Document containing the result.

        :param Group i_group_of_selected_products:
        :param Product i_reference_product:
        :param float i_thickness1:
        :param float i_thickness2:
        :param int i_use_constraints:
        :param tuple i_constraints:
        :rtype: Document
        """
        return Document(self.dmo_thicknesses.ComputeThicknessWithReference(i_group_of_selected_products.com_object,
                                                                           i_reference_product.com_object, i_thickness1,
                                                                           i_thickness2, i_use_constraints,
                                                                           i_constraints))

    def thickness_shape_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ThicknessShapeName() As CATBSTR
                | 
                |     Returns the name of the associated shape.

        :rtype: str
        """
        return self.dmo_thicknesses.ThicknessShapeName()

    def __repr__(self):
        return f'DMOThicknesses(name="{self.name}")'
