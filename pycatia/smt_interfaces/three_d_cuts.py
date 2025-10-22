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


class ThreeDCuts(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ThreeDCuts
                |
                | Interface to compute 3D cuts

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.three_d_cuts = com_object

    def compute_3d_cut(self, group_of_selected_products: Group) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub Compute3DCut(Group GroupOfSelectedProducts,
                | Document ThreeDCutDocument)
                |
                |     Computes the 3DCut on the selected products.
                |
                |     Parameters:
                |
                |         GroupOfSelectedProducts
                |             The selected products on which you want to perform the 3D cut.
                |
                |
                |     Returns:
                |         ThreeDCutDocument: Document containing the result.

        :param Group group_of_selected_products:
        :rtype: Document
        """
        return Document(self.three_d_cuts.Compute3DCut(group_of_selected_products.com_object))

    def compute_3d_cut_with_reference(
            self,
            group_of_selected_products: Group,
            i_reference_product: Product,
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub Compute3DCutWithAReference(Group
                | GroupOfSelectedProducts,
                | Product iReferenceProduct,
                | Document ThreeDCutDocument)
                |
                |     Computes the 3DCut on the selected products, according to a reference
                |     product.
                |
                |     Parameters:
                |
                |         GroupOfSelectedProducts
                |             The selected products on which you want to perform the 3D cut.
                |
                |         iReferenceProduct
                |             Product taken as a reference.
                |
                |     Returns:
                |         ThreeDCutDocument: Document containing the result.

        :param Group group_of_selected_products:
        :param Product i_reference_product:
        :rtype: Document
        """
        return Document(
            self.three_d_cuts.Compute3DCutWithAReference(
                group_of_selected_products.com_object,
                i_reference_product.com_object,
            )
        )

    def get_compute_3d_cut(self, group_of_selected_products: Group) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetCompute3DCut(Group GroupOfSelectedProducts) As
                | Document
                |
                |     Computes the 3DCut on the selected products (better
                |     signature).
                |
                |     Parameters:
                |
                |         GroupOfSelectedProducts
                |             The selected products on which you want to perform the 3D cut.
                |
                |
                |     Returns:
                |         ThreeDCutDocument: Document containing the result.

        :param Group group_of_selected_products:
        :rtype: Document
        """
        return Document(self.three_d_cuts.GetCompute3DCut(group_of_selected_products.com_object))

    def get_compute_3d_cut_with_a_reference(
            self,
            group_of_selected_products: Group,
            i_reference_product: Product
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetCompute3DCutWithAReference(Group
                | GroupOfSelectedProducts,
                | Product iReferenceProduct) As Document
                |
                |     Computes the 3DCut on the selected products, according to a reference
                |     product (better signature).
                |
                |     Parameters:
                |
                |         GroupOfSelectedProducts
                |             The selected products on which you want to perform the 3D cut.
                |
                |         iReferenceProduct
                |             Product taken as a reference.
                |
                |     Returns:
                |         ThreeDCutDocument: Document containing the result.

        :param Group group_of_selected_products:
        :param Product i_reference_product:
        :rtype: Document
        """
        return Document(
            self.three_d_cuts.GetCompute3DCutWithAReference(
                group_of_selected_products.com_object,
                i_reference_product.com_object
            )
        )

    def set_box(self, origin_x: float, origin_y: float, origin_z: float, vx: float, vy: float, vz: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetBox(double OriginX,
                | double OriginY,
                | double OriginZ,
                | double VX,
                | double VY,
                | double VZ)
                |
                |     Sets the RELATIVE box used for the 3D cut computation.
                |     Be aware of the behavior:
                |
                |             Vz
                |            ^_________________
                |           /|               /|
                |          /                / |
                |         /  |             /  |
                |        /                /   |
                |       /----+-----------/    |
                |       |                |    |
                |       |    |       *   |    |
                |       |            O   |    |
                |       |    |           |    |
                |       |                |    |
                |       |    |           |    |
                |       |    * - - - - - + - -|> Vy
                |       |    Origin      |   /
                |       |  /             |  /
                |       |                | /
                |       |/               |/
                |       /----------------/
                |      <
                |       Vx
                |
                |     In the relative referential, O is (0,0,0)
                |
                |     This method sets the RELATIVE box : the rotation and translation matrix will then set the absolute position of O.
                |     Remember where the center of the relative referential lies!
                |     Can have unexpected results if you don't use it properly.
                |
                |     Parameters:
                |
                |         OriginX
                |             Origin coordinate (X)
                |         OriginY
                |             Origin coordinate (Y)
                |         OriginZ
                |             Origin coordinate (Z)
                |         VX
                |             Length of the box (along X)
                |         VY
                |             Length of the box (along Y)
                |         VZ
                |             Length of the box (along Z)

        :param float origin_x:
        :param float origin_y:
        :param float origin_z:
        :param float vx:
        :param float vy:
        :param float vz:
        :rtype: None
        """
        return self.three_d_cuts.SetBox(origin_x, origin_y, origin_z, vx, vy, vz)

    def set_matrix(self, i_components: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetMatrix(CATSafeArrayVariant iComponents)
                |
                |     Sets the rotation AND translation matrix.
                |     Beware : After a SetBox, the matrix is not changed.
                |
                |     Parameters:
                |
                |         iComponents
                |             Components of the 4x4 matrix, placed in rows.

        :param tuple i_components:
        :rtype: None
        """
        return self.three_d_cuts.SetMatrix(i_components)

    def set_on_borders(self, on_borders: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetOnBorders(long OnBorders)
                |
                |     Sets the behavior on borders.
                |
                |     Parameters:
                |
                |         Type
                |             0 : We keep partially included triangles
                |             1 : We keep entirely included triangles

        :param int on_borders:
        :rtype: None
        """
        return self.three_d_cuts.SetOnBorders(on_borders)

    def set_type(self, type_: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetType(long Type)
                |
                |     Sets the type of cut we're doing.
                |
                |     Parameters:
                |
                |         Type
                |             0 : We keep the inner triangles
                |             1 : We keep the outer triangles

        :param int type_:
        :rtype: None
        """
        return self.three_d_cuts.SetType(type_)

    def three_d_cut_shape_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub ThreeDCutShapeName(CATBSTR Name)
                |
                |     Returns the name of the associated shape.

        :rtype: str
        """
        return self.three_d_cuts.ThreeDCutShapeName()

    def __repr__(self):
        return f'ThreeDCuts(name="{self.name}")'
