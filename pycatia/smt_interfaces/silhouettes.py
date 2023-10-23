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
from pycatia.smt_interfaces.silhouette import Silhouette
from pycatia.system_interfaces.collection import Collection


class Silhouettes(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Silhouettes
                | 
                | Interface to compute Silhouettes.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Silhouette)
        self.silhouettes = com_object

    def add(
            self,
            i_product_to_silhouette: Product,
            i_accuracy: float,
            i_azimuts: tuple,
            i_shape_name: str,
            i_activated_shape: int,
            i_default_shape: int
    ) -> Silhouette:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(Product iProductToSilhouette,
                | double iAccuracy,
                | CATSafeArrayVariant iAzimuts,
                | CATBSTR iShapeName,
                | long iActivatedShape,
                | long iDefaultShape) As Silhouette
                | 
                |     Creates a new Silhouette and adds it to the Silhouettes collection. This
                |     function is deprecated.
                | 
                |     Returns:
                |         The created Silhouette 
                |     Example:
                |         The following example creates a Silhouette newSilhouette in the
                |         Silhouette collection.
                | 
                |          Set newSilhouette = Silhouettes.Add

        :param Product i_product_to_silhouette:
        :param float i_accuracy:
        :param tuple i_azimuts:
        :param str i_shape_name:
        :param int i_activated_shape:
        :param int i_default_shape:
        :rtype: Silhouette
        """
        return Silhouette(
            self.silhouettes.Add(
                i_product_to_silhouette.com_object,
                i_accuracy,
                i_azimuts,
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
                |     Performs some clean-up.

        :rtype: None
        """
        return self.silhouettes.CleanUp()

    def compute_a_silhouette(
            self,
            group_of_selected_products: Group,
            i_view_points: tuple,
            i_accuracy: float,
            i_accuracy_for_simplification: float
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeASilhouette(Group GroupOfSelectedProducts,
                | CATSafeArrayVariant iViewPoints,
                | double iAccuracy,
                | double iAccuracyForSimplification) As Document
                | 
                |     Computes a silhouette on the selected products.
                | 
                |     Parameters:
                | 
                |         GroupOfSelectedProducts
                |             The selected products on which you want to perform the silhouette.
                |             
                |         iViewPoints
                |             Array containing the viewpoints (cameras) used to perform the
                |             silhouette. 
                |         iAccuracy
                |             Grain value for the voxels. 
                |         iAccuracyForSimplification
                |             Accuracy for simplification of the silhouette. Let it null for no
                |             simplification. 
                | 
                |     Returns:
                |         SilhouetteDocument: Document containing the result.

        :param Group group_of_selected_products:
        :param tuple i_view_points:
        :param float i_accuracy:
        :param float i_accuracy_for_simplification:
        :rtype: Document
        """
        return Document(
            self.silhouettes.ComputeASilhouette(
                group_of_selected_products.com_object,
                i_view_points,
                i_accuracy,
                i_accuracy_for_simplification
            )
        )

    def compute_a_silhouette_with_a_reference(
            self,
            i_group_of_selected_products: Group,
            i_reference_product: Product,
            i_view_points: tuple,
            i_accuracy: float,
            i_accuracy_for_simplification: float
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeASilhouetteWithAReference(Group
                | iGroupOfSelectedProducts,
                | Product iReferenceProduct,
                | CATSafeArrayVariant iViewPoints,
                | double iAccuracy,
                | double iAccuracyForSimplification) As Document
                | 
                |     Computes a silhouette on the selected products, according to a reference
                |     product.
                | 
                |     Parameters:
                | 
                |         iGroupOfSelectedProducts
                |             The selected products on which you want to perform the silhouette.
                |             
                |         iReferenceProduct
                |             Product taken as a reference. 
                |         iViewPoints
                |             Array containing the viewpoints (cameras) used to perform the
                |             silhouette. 
                |         iAccuracy
                |             Grain value for the voxels. 
                |         iAccuracyForSimplification
                |             Accuracy for simplification of the silhouette. Let it null for no
                |             simplification. 
                | 
                |     Returns:
                |         SilhouetteDocument: Document containing the result.

        :param Group i_group_of_selected_products:
        :param Product i_reference_product:
        :param tuple i_view_points:
        :param float i_accuracy:
        :param float i_accuracy_for_simplification:
        :rtype: Document
        """
        return Document(
            self.silhouettes.ComputeASilhouetteWithAReference(
                i_group_of_selected_products.com_object,
                i_reference_product.com_object,
                i_view_points,
                i_accuracy,
                i_accuracy_for_simplification
            )
        )

    def silhouette_shape_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func SilhouetteShapeName() As CATBSTR
                | 
                |     Returns the name of the associated shape.

        :rtype: str
        """
        return self.silhouettes.SilhouetteShapeName()

    def __repr__(self):
        return f'Silhouettes(name="{self.name}")'
