#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeAffinity(HybridShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeAffinity
                | 
                | Represents the hybrid shape affinity feature object.
                | Role: To access the data of the hybrid shape affinity feature object. This data
                | includes:
                | 
                |     The element to transform using the affinity
                |     The affinity reference coordinate system origin
                |     The affinity reference coordinate system reference plane
                |     The affinity reference coordinate system first direction
                |     The affinity ratio along the x, y and z directions of the reference
                |     coordinate system
                |     The element to transform using the affinity
                | 
                | The reference coordinate system is always a direct one.
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeAffinity
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_affinity = com_object

    @property
    def axis_first_direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AxisFirstDirection() As Reference
                | 
                |     Returns or sets the first direction of the reference coordinate
                |     system.
                |     Sub-element(s) supported (see Boundary object): RectilinearTriDimFeatEdge,
                |     RectilinearBiDimFeatEdge or RectilinearMonoDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in FirstDir the first direction of the reference
                |         coordinate system used by the Affinity hybrid shape
                |         feature.
                | 
                |          Dim FirstDir As Reference 
                |          Set FirstDir = Affinity.AxisFirstDirection

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_affinity.AxisFirstDirection)

    @axis_first_direction.setter
    def axis_first_direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_affinity.AxisFirstDirection = value.com_object

    @property
    def axis_origin(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AxisOrigin() As Reference
                | 
                |     Returns or sets the origin of the reference coordinate
                |     system.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in Origin the origin of the reference coordinate
                |         system used by the Affinity hybrid shape feature.
                | 
                |          Dim Origin As Reference 
                |          Set Origin = Affinity.AxisOrigin

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_affinity.AxisOrigin)

    @axis_origin.setter
    def axis_origin(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_affinity.AxisOrigin = value.com_object

    @property
    def axis_plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AxisPlane() As Reference
                | 
                |     Returns or sets the reference plane of the reference coordinate
                |     system.
                |     Sub-element(s) supported (see Boundary object):
                |     PlanarFace.
                | 
                |     Example:
                |         This example retrieves in RefPlane the reference plane of the reference
                |         coordinate system used by the Affinity hybrid shape
                |         feature.
                | 
                |          Dim RefPlane As Reference 
                |          Set RefPlane = Affinity.AxisPlane

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_affinity.AxisPlane)

    @axis_plane.setter
    def axis_plane(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_affinity.AxisPlane = value.com_object

    @property
    def creation_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CreationMode() As boolean
                | 
                |     Returns or sets the creation mode(creation or
                |     modification).
                |     Legal values: True if the result is a creation feature and False if the
                |     result is a modification feature.
                | 
                |     Example:
                | 
                |           This example sets that the mode of
                |          the hybShpAffinity hybrid shape affinity to creation
                |          
                | 
                |          hybShpAffinity.CreationMode = True

        :rtype: bool
        """

        return self.hybrid_shape_affinity.CreationMode

    @creation_mode.setter
    def creation_mode(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_affinity.CreationMode = value

    @property
    def elem_to_transform(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ElemToTransform() As Reference
                | 
                |     Returns or sets the element to transform using the
                |     affinity.
                | 
                |     Example:
                |         This example retrieves in ElementToTransform the element to transform
                |         for the Affinity hybrid shape feature.
                | 
                |          Dim ElementToTransform As Reference 
                |          Set ElementToTransform = Affinity.ElemToTransform

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_affinity.ElemToTransform)

    @elem_to_transform.setter
    def elem_to_transform(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_affinity.ElemToTransform = value.com_object

    @property
    def volume_result(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property VolumeResult() As boolean
                | 
                |     Returns or sets the volume result.
                |     Legal values: True if the result of affinity is required as volume (option
                |     is effective only in case of volumes,requires GSO License) and False if it is
                |     needed as surface .
                | 
                |     Example:
                | 
                |           This example sets that the result of
                |          the hybShpAffinity hybrid shape affinity is volume.
                |          
                | 
                |          hybShpAffinity.VolumeResult = True

        :rtype: bool
        """

        return self.hybrid_shape_affinity.VolumeResult

    @volume_result.setter
    def volume_result(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_affinity.VolumeResult = value

    @property
    def x_ratios(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property XRatios() As RealParam (Read Only)
                | 
                |     Returns the affinity ratio along the X Direction of the reference
                |     coordinate system.
                | 
                |     Example:
                |         This example retrieves in X the ratio of the affinity along the X
                |         Direction of the reference coordinate system used by the Affinity hybrid shape
                |         feature.
                | 
                |          Dim X As RealParam 
                |          Set X = Affinity.XRatios

        :rtype: RealParam
        """

        return RealParam(self.hybrid_shape_affinity.XRatios)

    @property
    def y_ratios(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property YRatios() As RealParam (Read Only)
                | 
                |     Returns the affinity ratio along the Y Direction of the reference
                |     coordinate system.
                | 
                |     Example:
                |         This example retrieves in Y the ratio of the affinity along the Y
                |         Direction of the reference coordinate system used by the Affinity hybrid shape
                |         feature.
                | 
                |          Dim Y As RealParam 
                |          Set Y = Affinity.YRatios

        :rtype: RealParam
        """

        return RealParam(self.hybrid_shape_affinity.YRatios)

    @property
    def z_ratios(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ZRatios() As RealParam (Read Only)
                | 
                |     Returns the affinity ratio along the Z Direction of the reference
                |     coordinate system.
                | 
                |     Example:
                |         This example retrieves in Z the ratio of the affinity along the Z
                |         Direction of the reference coordinate system used by the Affinity hybrid shape
                |         feature.
                | 
                |          Dim Z As RealParam 
                |          Set Z = Affinity.ZRatios

        :rtype: RealParam
        """

        return RealParam(self.hybrid_shape_affinity.ZRatios)

    def __repr__(self):
        return f'HybridShapeAffinity(name="{self.name}")'
