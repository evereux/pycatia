#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.document import Document
from pycatia.product_structure_interfaces.product import Product
from pycatia.simulation_interfaces.replay import Replay
from pycatia.smt_interfaces.swept_volume import SweptVolume
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection


class SweptVolumes(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SweptVolumes
                | 
                | Interface to compute swept volumes.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SweptVolume)
        self.swept_volumes = com_object

    def add(
            self,
            replay: Replay,
            i_products_to_swept: tuple,
            i_product_reference: Product,
            i_lod_mode: int,
            i_accuracy: float,
            i_shape_name: str,
            i_activated_shape: int,
            i_default_shape: int
    ) -> SweptVolume:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(Replay replay,
                | CATSafeArrayVariant iProductsToSwept,
                | Product iProductReference,
                | long iLODMode,
                | double iAccuracy,
                | CATBSTR iShapeName,
                | long iActivatedShape,
                | long iDefaultShape) As SweptVolume
                | 
                |     Creates a new SweptVolume and adds it to the SweptVolumes collection. This
                |     function is deprecated.
                | 
                |     Returns:
                |         The created SweptVolume 
                |     Example:
                |         The following example creates a SweptVolume newSweptVolume in the
                |         SweptVolume collection.
                | 
                |          Set SweptVolume = SweptVolumes.Add

        :param Replay replay:
        :param tuple i_products_to_swept:
        :param Product i_product_reference:
        :param int i_lod_mode:
        :param float i_accuracy:
        :param str i_shape_name:
        :param int i_activated_shape:
        :param int i_default_shape:
        :rtype: SweptVolume
        """
        return SweptVolume(
            self.swept_volumes.Add(
                replay.com_object,
                i_products_to_swept,
                i_product_reference.com_object,
                i_lod_mode,
                i_accuracy,
                i_shape_name,
                i_activated_shape,
                i_default_shape
            )
        )

    def add_from_swept_able(
            self,
            i_swept_able: AnyObject,
            i_products_to_swept: tuple,
            i_product_reference: Product,
            i_lod_mode: int,
            i_accuracy: float,
            i_shape_name: str,
            i_activated_shape: int,
            i_default_shape: int
    ) -> SweptVolume:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddFromSweptAble(CATBaseDispatch iSweptAble,
                | CATSafeArrayVariant iProductsToSwept,
                | Product iProductReference,
                | long iLODMode,
                | double iAccuracy,
                | CATBSTR iShapeName,
                | long iActivatedShape,
                | long iDefaultShape) As SweptVolume
                | 
                |     Creates a new SweptVolume and adds it to the SweptVolumes collection. This
                |     function is deprecated.
                | 
                |     Returns:
                |         The created SweptVolume

        :param AnyObject i_swept_able:
        :param tuple i_products_to_swept:
        :param Product i_product_reference:
        :param int i_lod_mode:
        :param float i_accuracy:
        :param str i_shape_name:
        :param int i_activated_shape:
        :param int i_default_shape:
        :rtype: SweptVolume
        """
        return SweptVolume(
            self.swept_volumes.AddFromSweptAble(
                i_swept_able.com_object,
                i_products_to_swept,
                i_product_reference.com_object,
                i_lod_mode,
                i_accuracy,
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
        return self.swept_volumes.CleanUp()

    def compute_a_swept_volume(
            self,
            i_replay: Replay,
            i_swept_able: AnyObject,
            i_products_to_swept: tuple,
            i_product_reference: Product,
            i_lod_mode: int,
            i_accuracy: float,
            i_wrapping_grain: float,
            i_wrapping_ratio: float,
            i_simplify_accuracy: float
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeASweptVolume(Replay iReplay,
                | CATBaseDispatch iSweptAble,
                | CATSafeArrayVariant iProductsToSwept,
                | Product iProductReference,
                | long iLODMode,
                | double iAccuracy,
                | double iWrappingGrain,
                | double iWrappingRatio,
                | double iSimplifAccuracy) As Document
                | 
                |     Computes a swept volume. This function is deprecated.
                | 
                |     Returns:
                |         The created SweptVolume

        :param Replay i_replay:
        :param AnyObject i_swept_able:
        :param tuple i_products_to_swept:
        :param Product i_product_reference:
        :param int i_lod_mode:
        :param float i_accuracy:
        :param float i_wrapping_grain:
        :param float i_wrapping_ratio:
        :param float i_simplify_accuracy:
        :rtype: Document
        """
        return Document(
            self.swept_volumes.ComputeASweptVolume(
                i_replay.com_object,
                i_swept_able.com_object,
                i_products_to_swept,
                i_product_reference.com_object,
                i_lod_mode,
                i_accuracy,
                i_wrapping_grain,
                i_wrapping_ratio,
                i_simplify_accuracy
            )
        )

    def compute_a_swept_volume_from_replay(
            self,
            i_replay: Replay,
            i_products_to_swept: tuple,
            i_product_reference: Product,
            i_lod_mode: int,
            i_accuracy: float,
            i_wrapping_grain: float,
            i_wrapping_ratio: float,
            i_simplif_accuracy: float
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeASweptVolumeFromReplay(Replay iReplay,
                | CATSafeArrayVariant iProductsToSwept,
                | Product iProductReference,
                | long iLODMode,
                | double iAccuracy,
                | double iWrappingGrain,
                | double iWrappingRatio,
                | double iSimplifAccuracy) As Document
                | 
                |     Computes a swept volume. This function is deprecated.
                | 
                |     Returns:
                |         The created SweptVolume

        :param Replay i_replay:
        :param tuple i_products_to_swept:
        :param Product i_product_reference:
        :param int i_lod_mode:
        :param float i_accuracy:
        :param float i_wrapping_grain:
        :param float i_wrapping_ratio:
        :param float i_simplif_accuracy:
        :rtype: Document
        """
        return Document(
            self.swept_volumes.ComputeASweptVolumeFromReplay(
                i_replay.com_object,
                i_products_to_swept,
                i_product_reference.com_object,
                i_lod_mode,
                i_accuracy,
                i_wrapping_grain,
                i_wrapping_ratio,
                i_simplif_accuracy
            )
        )

    def compute_a_swept_volume_from_sweptable(
            self,
            i_swept_able: AnyObject,
            i_products_to_swept: tuple,
            i_product_reference: Product,
            i_lod_mode: int,
            i_accuracy: float,
            i_wrapping_grain: float,
            i_wrapping_ratio: float,
            i_simplify_accuracy: float
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeASweptVolumeFromSweptable(CATBaseDispatch
                | iSweptAble,
                | CATSafeArrayVariant iProductsToSwept,
                | Product iProductReference,
                | long iLODMode,
                | double iAccuracy,
                | double iWrappingGrain,
                | double iWrappingRatio,
                | double iSimplifAccuracy) As Document
                | 
                |     Computes a swept volume. This function is deprecated.
                | 
                |     Returns:
                |         The created SweptVolume

        :param AnyObject i_swept_able:
        :param tuple i_products_to_swept:
        :param Product i_product_reference:
        :param int i_lod_mode:
        :param float i_accuracy:
        :param float i_wrapping_grain:
        :param float i_wrapping_ratio:
        :param float i_simplify_accuracy:
        :rtype: Document
        """
        return Document(
            self.swept_volumes.ComputeASweptVolumeFromSweptable(
                i_swept_able.com_object,
                i_products_to_swept,
                i_product_reference.com_object,
                i_lod_mode,
                i_accuracy,
                i_wrapping_grain,
                i_wrapping_ratio,
                i_simplify_accuracy
            )
        )

    def compute_swept_volumes(
            self,
            i_replay: Replay,
            i_swept_able: AnyObject,
            i_products_to_swept: tuple,
            i_product_reference: Product,
            i_lod_mode: int,
            i_accuracy: float,
            i_perform_wrapping: int,
            i_perform_simplif: int,
            i_wrapping_grain: float,
            i_wrapping_ratio: float,
            i_simplify_accuracy: float,
            o_swept_volume_documents: tuple
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ComputeSweptVolumes(Replay iReplay,
                | CATBaseDispatch iSweptAble,
                | CATSafeArrayVariant iProductsToSwept,
                | Product iProductReference,
                | long iLODMode,
                | double iAccuracy,
                | long iPerformWrapping,
                | long iPerformSimplif,
                | double iWrappingGrain,
                | double iWrappingRatio,
                | double iSimplifAccuracy,
                | CATSafeArrayVariant oSweptVolumeDocuments)
                | 
                |     Computes a swept volume, from a replay or a track.
                | 
                |     Parameters:
                | 
                |         iReplay
                |             Replay on which we perfom the swept volume. Can be NULL.
                |             
                |         iSweptAble
                |             Track (or any other thing that implements CATISweptAble) on which
                |             we perfom the swept volume. Can be NULL. 
                |         iProductsToSwept
                |             Selection of products to sweep. 
                |         iProductReference
                |             Product taken as a reference. 
                |         iLODMode
                |             Do we want levels of details or not? 
                |         iAccuracy
                |             Filtering positions parameter. 
                |         iPerformWrapping
                |             Do we perform a wrapping? 
                |         iPerformSimplif
                |             Do we perform a simplification? 
                |         iWrappingGrain
                |             Grain for wrapping. 
                |         iWrappingRatio
                |             Offset ratio for wrapping. 
                |         iSimplifAccuracy
                |             Accuracy for simplification. 
                | 
                |     Returns:
                |         oSweptVolumeDocuments: Documents containing the results.

        :param Replay i_replay:
        :param AnyObject i_swept_able:
        :param tuple i_products_to_swept:
        :param Product i_product_reference:
        :param int i_lod_mode:
        :param float i_accuracy:
        :param int i_perform_wrapping:
        :param int i_perform_simplify:
        :param float i_wrapping_grain:
        :param float i_wrapping_ratio:
        :param float i_simplif_accuracy:
        :param tuple o_swept_volume_documents:
        :rtype: None
        """
        return self.swept_volumes.ComputeSweptVolumes(
            i_replay.com_object,
            i_swept_able.com_object,
            i_products_to_swept,
            i_product_reference.com_object,
            i_lod_mode,
            i_accuracy,
            i_perform_wrapping,
            i_perform_simplif,
            i_wrapping_grain,
            i_wrapping_ratio,
            i_simplify_accuracy,
            o_swept_volume_documents
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'compute_swept_volumes'
        # # vba_code = """
        # # Public Function compute_swept_volumes(swept_volumes)
        # #     Dim iReplay (2)
        # #     swept_volumes.ComputeSweptVolumes iReplay
        # #     compute_swept_volumes = iReplay
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def compute_swept_volumes_from_replay(
            self,
            i_replay: Replay,
            i_products_to_swept: tuple,
            i_product_reference: Product,
            i_lod_mode: int,
            i_accuracy: float,
            i_perform_wrapping: int,
            i_perform_simplify: int,
            i_wrapping_grain: float,
            i_wrapping_ratio: float,
            i_simplif_accuracy: float,
            o_swept_volume_documents: tuple
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ComputeSweptVolumesFromReplay(Replay iReplay,
                | CATSafeArrayVariant iProductsToSwept,
                | Product iProductReference,
                | long iLODMode,
                | double iAccuracy,
                | long iPerformWrapping,
                | long iPerformSimplif,
                | double iWrappingGrain,
                | double iWrappingRatio,
                | double iSimplifAccuracy,
                | CATSafeArrayVariant oSweptVolumeDocuments)
                | 
                |     Computes a swept volume from a replay.
                | 
                |     Parameters:
                | 
                |         iReplay
                |             Replay on which we perfom the swept volume. 
                |         iProductsToSwept
                |             Selection of products to sweep. 
                |         iProductReference
                |             Product taken as a reference. 
                |         iLODMode
                |             Do we want levels of details or not? 
                |         iAccuracy
                |             Filtering positions parameter. 
                |         iPerformWrapping
                |             Do we perform a wrapping? 
                |         iPerformSimplif
                |             Do we perform a simplification? 
                |         iWrappingGrain
                |             Grain for wrapping. 
                |         iWrappingRatio
                |             Offset ratio for wrapping. 
                |         iSimplifAccuracy
                |             Accuracy for simplification. 
                | 
                |     Returns:
                |         oSweptVolumeDocuments: Documents containing the results.

        :param Replay i_replay:
        :param tuple i_products_to_swept:
        :param Product i_product_reference:
        :param int i_lod_mode:
        :param float i_accuracy:
        :param int i_perform_wrapping:
        :param int i_perform_simplify:
        :param float i_wrapping_grain:
        :param float i_wrapping_ratio:
        :param float i_simplif_accuracy:
        :param tuple o_swept_volume_documents:
        :rtype: None
        """
        return self.swept_volumes.ComputeSweptVolumesFromReplay(
            i_replay.com_object,
            i_products_to_swept,
            i_product_reference.com_object,
            i_lod_mode,
            i_accuracy,
            i_perform_wrapping,
            i_perform_simplify,
            i_wrapping_grain,
            i_wrapping_ratio,
            i_simplif_accuracy,
            o_swept_volume_documents
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'compute_swept_volumes_from_replay'
        # # vba_code = """
        # # Public Function compute_swept_volumes_from_replay(swept_volumes)
        # #     Dim iReplay (2)
        # #     swept_volumes.ComputeSweptVolumesFromReplay iReplay
        # #     compute_swept_volumes_from_replay = iReplay
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def compute_swept_volumes_from_sweptable(
            self,
            i_swept_able: AnyObject,
            i_products_to_swept: tuple,
            i_product_reference: Product,
            i_lod_mode: int,
            i_accuracy: float,
            i_perform_wrapping: int,
            i_perform_simplify: int,
            i_wrapping_grain: float,
            i_wrapping_ratio: float,
            i_simplify_accuracy: float,
            o_swept_volume_documents: tuple
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ComputeSweptVolumesFromSweptable(CATBaseDispatch
                | iSweptAble,
                | CATSafeArrayVariant iProductsToSwept,
                | Product iProductReference,
                | long iLODMode,
                | double iAccuracy,
                | long iPerformWrapping,
                | long iPerformSimplif,
                | double iWrappingGrain,
                | double iWrappingRatio,
                | double iSimplifAccuracy,
                | CATSafeArrayVariant oSweptVolumeDocuments)
                | 
                |     Computes a swept volume from a track.
                | 
                |     Parameters:
                | 
                |         iSweptAble
                |             Track (or any other thing that implements CATISweptAble) on which
                |             we perfom the swept volume. 
                |         iProductsToSwept
                |             Selection of products to sweep. 
                |         iProductReference
                |             Product taken as a reference. 
                |         iLODMode
                |             Do we want levels of details or not? 
                |         iAccuracy
                |             Filtering positions parameter. 
                |         iPerformWrapping
                |             Do we perform a wrapping? 
                |         iPerformSimplif
                |             Do we perform a simplification? 
                |         iWrappingGrain
                |             Grain for wrapping. 
                |         iWrappingRatio
                |             Offset ratio for wrapping. 
                |         iSimplifAccuracy
                |             Accuracy for simplification. 
                | 
                |     Returns:
                |         oSweptVolumeDocuments: Documents containing the results.

        :param AnyObject i_swept_able:
        :param tuple i_products_to_swept:
        :param Product i_product_reference:
        :param int i_lod_mode:
        :param float i_accuracy:
        :param int i_perform_wrapping:
        :param int i_perform_simplify:
        :param float i_wrapping_grain:
        :param float i_wrapping_ratio:
        :param float i_simplify_accuracy:
        :param tuple o_swept_volume_documents:
        :rtype: None
        """
        return self.swept_volumes.ComputeSweptVolumesFromSweptable(
            i_swept_able.com_object,
            i_products_to_swept,
            i_product_reference.com_object,
            i_lod_mode,
            i_accuracy,
            i_perform_wrapping,
            i_perform_simplify,
            i_wrapping_grain,
            i_wrapping_ratio,
            i_simplify_accuracy,
            o_swept_volume_documents
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'compute_swept_volumes_from_sweptable'
        # # vba_code = """
        # # Public Function compute_swept_volumes_from_sweptable(swept_volumes)
        # #     Dim iSweptAble (2)
        # #     swept_volumes.ComputeSweptVolumesFromSweptable iSweptAble
        # #     compute_swept_volumes_from_sweptable = iSweptAble
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_silhouette(self, on_off: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSilhouette(long OnOff)
                | 
                |     Adds the possibility to make a silhouette before the swept volume

        :param int on_off:
        :rtype: None
        """
        return self.swept_volumes.SetSilhouette(on_off)

    def set_spatial_split(self, on_off: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSpatialSplit(long OnOff)
                | 
                |     Adds the possibility to parallelize swept&wrapping after a spatial split.
                |     This gains in memory but not in CPU usage (takes longer.)

        :param int on_off:
        :rtype: None
        """
        return self.swept_volumes.SetSpatialSplit(on_off)

    def __repr__(self):
        return f'SweptVolumes(name="{self.name}")'
