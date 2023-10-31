#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.product_structure_interfaces.product import Product
from pycatia.smt_interfaces.free_space import FreeSpace
from pycatia.system_interfaces.collection import Collection


class FreeSpaces(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     FreeSpaces
                | 
                | Interface to compute Free Spaces.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=FreeSpace)
        self.free_spaces = com_object

    def add(
            self,
            i_product_for_free_space: Product,
            i_accuracy: float,
            i_xmin: float,
            i_xmax: float,
            i_ymin: float,
            i_ymax: float,
            i_zmin: float,
            i_zmax: float,
            i_type_free_space: int,
            i_xpt: float,
            i_ypt: float,
            i_zpt: float,
            i_holes: tuple,
            i_shape_name: str,
            i_activated_shape: int,
            i_default_shape: int
    ) -> FreeSpace:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(Product iProductForFreeSpace,
                | double iAccuracy,
                | double iXmin,
                | double iXmax,
                | double iYmin,
                | double iYmax,
                | double iZmin,
                | double iZmax,
                | long iTypeFreeSpace,
                | double iXpt,
                | double iYpt,
                | double iZpt,
                | CATSafeArrayVariant iHoles,
                | CATBSTR iShapeName,
                | long iActivatedShape,
                | long iDefaultShape) As FreeSpace
                | 
                |     Compute a free space around a selected product.

        :param Product i_product_for_free_space:
        :param float i_accuracy:
        :param float i_xmin:
        :param float i_xmax:
        :param float i_ymin:
        :param float i_ymax:
        :param float i_zmin:
        :param float i_zmax:
        :param int i_type_free_space:
        :param float i_xpt:
        :param float i_ypt:
        :param float i_zpt:
        :param tuple i_holes:
        :param str i_shape_name:
        :param int i_activated_shape:
        :param int i_default_shape:
        :rtype: FreeSpace
        """
        return FreeSpace(
            self.free_spaces.Add(
                i_product_for_free_space.com_object,
                i_accuracy,
                i_xmin,
                i_xmax,
                i_ymin,
                i_ymax,
                i_zmin,
                i_zmax,
                i_type_free_space,
                i_xpt,
                i_ypt,
                i_zpt,
                i_holes,
                i_shape_name,
                i_activated_shape,
                i_default_shape
            )
        )

    def add_around_any(
            self,
            i_accuracy: float,
            i_xmin: float,
            i_xmax: float,
            i_ymin: float,
            i_ymax: float,
            i_zmin: float,
            i_zmax: float,
            i_shape_name: str,
            i_type_free_space: int,
            i_holes: tuple
    ) -> FreeSpace:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddAroundAny(double iAccuracy,
                | double iXmin,
                | double iXmax,
                | double iYmin,
                | double iYmax,
                | double iZmin,
                | double iZmax,
                | CATBSTR iShapeName,
                | long iTypeFreeSpace,
                | CATSafeArrayVariant iHoles) As FreeSpace
                | 
                |     Compute a free space around any products.

        :param float i_accuracy:
        :param float i_xmin:
        :param float i_xmax:
        :param float i_ymin:
        :param float i_ymax:
        :param float i_zmin:
        :param float i_zmax:
        :param str i_shape_name:
        :param int i_type_free_space:
        :param tuple i_holes:
        :rtype: FreeSpace
        """
        return FreeSpace(
            self.free_spaces.AddAroundAny(
                i_accuracy,
                i_xmin,
                i_xmax,
                i_ymin,
                i_ymax,
                i_zmin,
                i_zmax,
                i_shape_name,
                i_type_free_space,
                i_holes
            )
        )

    def add_around_products(
            self,
            i_accuracy: float,
            i_xmin: float,
            i_xmax: float,
            i_ymin: float,
            i_ymax: float,
            i_zmin: float,
            i_zmax: float,
            i_shape_name: str,
            i_type_free_space: int,
            i_holes: tuple,
            i_reference_selection: tuple
    ) -> FreeSpace:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddAroundProducts(double iAccuracy,
                | double iXmin,
                | double iXmax,
                | double iYmin,
                | double iYmax,
                | double iZmin,
                | double iZmax,
                | CATBSTR iShapeName,
                | long iTypeFreeSpace,
                | CATSafeArrayVariant iHoles,
                | CATSafeArrayVariant iReferenceSelection) As FreeSpace
                | 
                |     Compute a free space around a reference selection

        :param float i_accuracy:
        :param float i_xmin:
        :param float i_xmax:
        :param float i_ymin:
        :param float i_ymax:
        :param float i_zmin:
        :param float i_zmax:
        :param str i_shape_name:
        :param int i_type_free_space:
        :param tuple i_holes:
        :param tuple i_reference_selection:
        :rtype: FreeSpace
        """
        return FreeSpace(
            self.free_spaces.AddAroundProducts(
                i_accuracy,
                i_xmin,
                i_xmax,
                i_ymin,
                i_ymax,
                i_zmin,
                i_zmax,
                i_shape_name,
                i_type_free_space,
                i_holes,
                i_reference_selection
            )
        )

    def add_from_file(self, i_file_name: str, i_shape_name: str) -> FreeSpace:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddFromFile(CATBSTR iFileName,
                | CATBSTR iShapeName) As FreeSpace
                | 
                |     Compute a free space from a file.

        :param str i_file_name:
        :param str i_shape_name:
        :rtype: FreeSpace
        """
        return FreeSpace(self.free_spaces.AddFromFile(i_file_name, i_shape_name))

    def add_inflating_from_file(self, i_file_name: str, i_shape_name: str) -> FreeSpace:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddInflatingFromFile(CATBSTR iFileName,
                | CATBSTR iShapeName) As FreeSpace
                | 
                |     Compute an inflating free space from a file.

        :param str i_file_name:
        :param str i_shape_name:
        :rtype: FreeSpace
        """
        return FreeSpace(self.free_spaces.AddInflatingFromFile(i_file_name, i_shape_name))

    def add_split_from_file(
            self,
            i_x: float,
            i_y: float,
            i_z: float,
            i_nx: float,
            i_ny: float,
            i_nz: float,
            i_file_name: str,
            i_shape_name: str
    ) -> FreeSpace:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddSplitFromFile(double iX,
                | double iY,
                | double iZ,
                | double iNx,
                | double iNy,
                | double iNz,
                | CATBSTR iFileName,
                | CATBSTR iShapeName) As FreeSpace
                | 
                |     Compute a split free space from a file.

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :param float i_nx:
        :param float i_ny:
        :param float i_nz:
        :param str i_file_name:
        :param str i_shape_name:
        :rtype: FreeSpace
        """
        return FreeSpace(self.free_spaces.AddSplitFromFile(i_x, i_y, i_z, i_nx, i_ny, i_nz, i_file_name, i_shape_name))

    def __repr__(self):
        return f'FreeSpaces(name="{self.name}")'
