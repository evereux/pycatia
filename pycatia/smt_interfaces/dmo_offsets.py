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
from pycatia.smt_interfaces.dmo_offset import DMOOffset
from pycatia.system_interfaces.collection import Collection


class DMOOffsets(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DMOOffsets
                | 
                | Interface to access a CATIADMOOffsets and compute Offsets
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DMOOffset)
        self.dmo_offsets = com_object

    def add(
            self,
            i_product_to_offset: Product,
            i_offset1: float,
            i_use_constraints: int,
            i_constraints: tuple,
            i_shape_name: str,
            i_activated_shape: int,
            i_default_shape: int
    ) -> DMOOffset:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(Product iProductToOffset,
                | double iOffset1,
                | long iUseConstraints,
                | CATSafeArrayVariant iConstraints,
                | CATBSTR iShapeName,
                | long iActivatedShape,
                | long iDefaultShape) As DMOOffset
                | 
                |     Creates a new Offset and adds it to the DMOOffsets collection. This
                |     function is deprecated.
                | 
                |     Returns:
                |         The created offset 
                |     Example:
                |         The following example creates an offset newOffset in the Offset
                |         collection.
                | 
                |          Set newOffset = DMOOffsets.Add

        :param Product i_product_to_offset:
        :param float i_offset1:
        :param int i_use_constraints:
        :param tuple i_constraints:
        :param str i_shape_name:
        :param int i_activated_shape:
        :param int i_default_shape:
        :rtype: DMOOffset
        """
        return DMOOffset(
            self.dmo_offsets.Add(
                i_product_to_offset.com_object,
                i_offset1,
                i_use_constraints,
                i_constraints,
                i_shape_name,
                i_activated_shape,
                i_default_shape
            )
        )

    def add_offset_from_vectors(
            self,
            i_product_to_offset: Product,
            i_offset_vectors: tuple,
            i_offset_values: tuple,
            i_shape_name: str,
            i_activated_shape: int,
            i_default_shape: int
    ) -> DMOOffset:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddOffsetFromVectors(Product iProductToOffset,
                | CATSafeArrayVariant iOffsetVectors,
                | CATSafeArrayVariant iOffsetValues,
                | CATBSTR iShapeName,
                | long iActivatedShape,
                | long iDefaultShape) As DMOOffset
                | 
                |     Creates a new Offset from a set of vectors, and adds it to the DMOOffsets
                |     collection. This function is deprecated.
                | 
                |     Returns:
                |         The created offset 
                |     Example:
                |         The following example creates an offset newOffset in the Offset
                |         collection.
                | 
                |          Set newOffset = DMOOffsets.Add

        :param Product i_product_to_offset:
        :param tuple i_offset_vectors:
        :param tuple i_offset_values:
        :param str i_shape_name:
        :param int i_activated_shape:
        :param int i_default_shape:
        :rtype: DMOOffset
        """
        return DMOOffset(
            self.dmo_offsets.AddOffsetFromVectors(
                i_product_to_offset.com_object,
                i_offset_vectors,
                i_offset_values,
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
        return self.dmo_offsets.CleanUp()

    def compute_an_offset(
            self,
            group_of_selected_products: Group,
            i_offset: float,
            i_use_constraints: int,
            i_constraints: tuple
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeAnOffset(Group GroupOfSelectedProducts,
                | double iOffset,
                | long iUseConstraints,
                | CATSafeArrayVariant iConstraints) As Document
                | 
                |     Compute a offset on the selected products.
                | 
                |     Parameters:
                | 
                |         GroupOfSelectedProducts
                |             The selected products on which you want to perform the offset.
                |             
                |         iOffset
                |             Offset value. 
                |         iUseConstraints
                |             Do we use normals constraints or not ? 
                |         iConstraints
                |             Constraints array. 
                | 
                |     Returns:
                |         OffsetDocument: Document containing the result.

        :param Group group_of_selected_products:
        :param float i_offset:
        :param int i_use_constraints:
        :param tuple i_constraints:
        :rtype: Document
        """
        return Document(
            self.dmo_offsets.ComputeAnOffset(
                group_of_selected_products.com_object,
                i_offset,
                i_use_constraints,
                i_constraints
            )
        )

    def compute_an_offset_from_vectors(
            self,
            group_of_selected_products: Group,
            i_offset_vectors: tuple,
            i_offset_values: tuple
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeAnOffsetFromVectors(Group
                | GroupOfSelectedProducts,
                | CATSafeArrayVariant iOffsetVectors,
                | CATSafeArrayVariant iOffsetValues) As Document
                | 
                |     Compute an offset on the selected products, according to some
                |     vectors
                | 
                |     Parameters:
                | 
                |         GroupOfSelectedProducts
                |             The selected products on which you want to perform the offset.
                |             
                |         iOffsetVectors
                |             Vectors taken into account for the computation 
                |         iOffsetValues
                |             Offset values. 
                | 
                |     Returns:
                |         OffsetDocument: Document containing the result.

        :param Group group_of_selected_products:
        :param tuple i_offset_vectors:
        :param tuple i_offset_values:
        :rtype: Document
        """
        return Document(
            self.dmo_offsets.ComputeAnOffsetFromVectors(
                group_of_selected_products.com_object,
                i_offset_vectors,
                i_offset_values
            )
        )

    def compute_an_offset_from_vectors_with_a_reference(
            self,
            i_group_of_selected_products: Group,
            i_reference_product: Product,
            i_offset_vectors: tuple,
            i_offset_values: tuple
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeAnOffsetFromVectorsWithAReference(Group
                | iGroupOfSelectedProducts,
                | Product iReferenceProduct,
                | CATSafeArrayVariant iOffsetVectors,
                | CATSafeArrayVariant iOffsetValues) As Document
                | 
                |     Compute an offset on the selected products, according to some vectors and a
                |     reference product.
                | 
                |     Parameters:
                | 
                |         iGroupOfSelectedProducts
                |             The selected products on which you want to perform the offset.
                |             
                |         iReferenceProduct
                |             The reference product. 
                |         iOffsetVectors
                |             Vectors taken into account for the computation 
                |         iOffsetValues
                |             Offset values. 
                | 
                |     Returns:
                |         OffsetDocument: Document containing the result.

        :param Group i_group_of_selected_products:
        :param Product i_reference_product:
        :param tuple i_offset_vectors:
        :param tuple i_offset_values:
        :rtype: Document
        """
        return Document(
            self.dmo_offsets.ComputeAnOffsetFromVectorsWithAReference(
                i_group_of_selected_products.com_object,
                i_reference_product.com_object,
                i_offset_vectors,
                i_offset_values
            )
        )

    def compute_an_offset_with_a_reference(
            self,
            i_group_of_selected_products: Group,
            i_reference_product: Product,
            i_offset: float,
            i_use_constraints: int,
            i_constraints: tuple
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeAnOffsetWithAReference(Group
                | iGroupOfSelectedProducts,
                | Product iReferenceProduct,
                | double iOffset,
                | long iUseConstraints,
                | CATSafeArrayVariant iConstraints) As Document
                | 
                |     Compute an offset on the selected products, according to a reference
                |     product.
                | 
                |     Parameters:
                | 
                |         iGroupOfSelectedProducts
                |             The selected products on which you want to perform the offset.
                |             
                |         iReferenceProduct
                |             The reference product. 
                |         iOffset
                |             Offset value. 
                |         iUseConstraints
                |             Do we use normals constraints or not ? 
                |         iConstraints
                |             Constraints array. 
                | 
                |     Returns:
                |         OffsetDocument: Document containing the result.

        :param Group i_group_of_selected_products:
        :param Product i_reference_product:
        :param float i_offset:
        :param int i_use_constraints:
        :param tuple i_constraints:
        :rtype: Document
        """
        return Document(
            self.dmo_offsets.ComputeAnOffsetWithAReference(
                i_group_of_selected_products.com_object,
                i_reference_product.com_object,
                i_offset,
                i_use_constraints,
                i_constraints
            )
        )

    def offset_shape_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func OffsetShapeName() As CATBSTR
                | 
                |     Returns the name of the associated shape.

        :rtype: str
        """
        return self.dmo_offsets.OffsetShapeName()

    def __repr__(self):
        return f'DmoOffsets(name="{self.name}")'
