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
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection


class VibrationVolumes(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VibrationVolumes
                | 
                | Interface to compute vibration volumes
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.vibration_volumes = com_object

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
        return self.vibration_volumes.CleanUp()

    def compute_vibration_volume(
            self,
            group_of_selected_products: Group,
            positions_file_path: str,
            i_accuracy: float,
            i_simplif_accuracy: float
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeVibrationVolume(Group GroupOfSelectedProducts,
                | CATBSTR PositionsFilePath,
                | double iAccuracy,
                | double iSimplifAccuracy) As Document
                | 
                |     Computes a vibration volume, from a position input file.
                | 
                |     Parameters:
                | 
                |         GroupOfSelectedProducts
                |             Selection of products to make vibrate. 
                |         PositionsFilePath
                |             Positions file path. 
                |         iAccuracy
                |             Grain for wrapping. 
                |         iSimplifAccuracy
                |             Accuracy for simplification. A non positive value makes the
                |             simplification inactive. 
                | 
                |     Returns:
                |         VibrationVolumeDocument: Document containing the result.

        :param Group group_of_selected_products:
        :param str positions_file_path:
        :param float i_accuracy:
        :param float i_simplif_accuracy:
        :rtype: Document
        """
        return Document(
            self.vibration_volumes.ComputeVibrationVolume(
                group_of_selected_products.com_object,
                positions_file_path,
                i_accuracy,
                i_simplif_accuracy
            )
        )

    def compute_vibration_volume_from_track(
            self,
            group_of_selected_products: Group,
            i_swept_able: AnyObject,
            i_accuracy: float,
            i_simplify_accuracy: float
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeVibrationVolumeFromTrack(Group
                | GroupOfSelectedProducts,
                | CATBaseDispatch iSweptAble,
                | double iAccuracy,
                | double iSimplifAccuracy) As Document
                | 
                |     Computes a vibration volume, from a track.
                | 
                |     Parameters:
                | 
                |         GroupOfSelectedProducts
                |             Selection of products to make vibrate. 
                |         iSweptAble
                |             Track containing the positions. 
                |         iAccuracy
                |             Grain for wrapping. 
                |         iSimplifAccuracy
                |             Accuracy for simplification. A non positive value makes the
                |             simplification inactive. 
                | 
                |     Returns:
                |         VibrationVolumeDocument: Document containing the result.

        :param Group group_of_selected_products:
        :param AnyObject i_swept_able:
        :param float i_accuracy:
        :param float i_simplify_accuracy:
        :rtype: Document
        """
        return Document(
            self.vibration_volumes.ComputeVibrationVolumeFromTrack(
                group_of_selected_products.com_object,
                i_swept_able.com_object,
                i_accuracy,
                i_simplify_accuracy
            )
        )

    def compute_vibration_volume_from_track_with_a_reference(
            self,
            group_of_selected_products: Group,
            i_reference_product: Product,
            i_swept_able: AnyObject,
            i_accuracy: float,
            i_simplify_accuracy: float
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeVibrationVolumeFromTrackWithAReference(Group
                | GroupOfSelectedProducts,
                | Product iReferenceProduct,
                | CATBaseDispatch iSweptAble,
                | double iAccuracy,
                | double iSimplifAccuracy) As Document
                | 
                |     Computes a vibration volume, from a track, according to a reference
                |     product.
                | 
                |     Parameters:
                | 
                |         GroupOfSelectedProducts
                |             Selection of products to make vibrate. 
                |         iReferenceProduct
                |             Product taken as a reference. 
                |         iSweptAble
                |             Track containing the positions. 
                |         iAccuracy
                |             Grain for wrapping. 
                |         iSimplifAccuracy
                |             Accuracy for simplification. A non positive value makes the
                |             simplification inactive. 
                | 
                |     Returns:
                |         VibrationVolumeDocument: Document containing the result.

        :param Group group_of_selected_products:
        :param Product i_reference_product:
        :param AnyObject i_swept_able:
        :param float i_accuracy:
        :param float i_simplify_accuracy:
        :rtype: Document
        """
        return Document(
            self.vibration_volumes.ComputeVibrationVolumeFromTrackWithAReference(
                group_of_selected_products.com_object,
                i_reference_product.com_object,
                i_swept_able.com_object,
                i_accuracy,
                i_simplify_accuracy
            )
        )

    def compute_vibration_volume_with_a_reference(
            self,
            i_group_of_selected_products: Group,
            i_reference_product: Product,
            positions_file_path: str,
            i_accuracy: float,
            i_simplify_accuracy: float
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeVibrationVolumeWithAReference(Group
                | iGroupOfSelectedProducts,
                | Product iReferenceProduct,
                | CATBSTR PositionsFilePath,
                | double iAccuracy,
                | double iSimplifAccuracy) As Document
                | 
                |     Computes a vibration volume, from a position input file, according to a
                |     reference product.
                | 
                |     Parameters:
                | 
                |         iGroupOfSelectedProducts
                |             Selection of products to make vibrate. 
                |         iReferenceProduct
                |             Product taken as a reference. 
                |         PositionsFilePath
                |             Positions file path. 
                |         iAccuracy
                |             Grain for wrapping. 
                |         iSimplifAccuracy
                |             Accuracy for simplification. A non positive value makes the
                |             simplification inactive. 
                | 
                |     Returns:
                |         VibrationVolumeDocument: Document containing the result.

        :param Group i_group_of_selected_products:
        :param Product i_reference_product:
        :param str positions_file_path:
        :param float i_accuracy:
        :param float i_simplify_accuracy:
        :rtype: Document
        """
        return Document(
            self.vibration_volumes.ComputeVibrationVolumeWithAReference(
                i_group_of_selected_products.com_object,
                i_reference_product.com_object,
                positions_file_path,
                i_accuracy,
                i_simplify_accuracy
            )
        )

    def vibration_volume_shape_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func VibrationVolumeShapeName() As CATBSTR
                | 
                |     Returns the name of the associated shape.

        :rtype: str
        """
        return self.vibration_volumes.VibrationVolumeShapeName()

    def __repr__(self):
        return f'VibrationVolumes(name="{self.name}")'
