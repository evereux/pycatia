#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShape3DCurveOffset(HybridShape):
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
                |                         HybridShape3DCurveOffset
                | 
                | Represents the hybrid shape 3DCurve Offset operation feature.
                | Role: Allows you to access data of the 3D Curve Offset feature created by using
                | a curve, a direction and three literal parameters
                | 
                | Use the HybridShapeFactory.AddNew3DCurveOffset to create a
                | HybridShape3DCurveOffset object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_3d_curve_offset = com_object

    @property
    def corner_radius_value(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CornerRadiusValue() As Length
                | 
                |     Returns or sets the Corner Radius Value.

        :rtype: Length
        """

        return Length(self.hybrid_shape_3d_curve_offset.CornerRadiusValue)

    @corner_radius_value.setter
    def corner_radius_value(self, length: Length):
        """
        :param Length length:
        """

        self.hybrid_shape_3d_curve_offset.CornerRadiusValue = length.com_object

    @property
    def corner_tension_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CornerTensionValue() As double
                | 
                |     Returns or sets the Corner Tension Value.

        :rtype: float
        """

        return self.hybrid_shape_3d_curve_offset.CornerTensionValue

    @corner_tension_value.setter
    def corner_tension_value(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_3d_curve_offset.CornerTensionValue = value

    @property
    def curve_to_offset(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CurveToOffset() As Reference
                | 
                |     Returns or sets the curve to offset.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_3d_curve_offset.CurveToOffset)

    @curve_to_offset.setter
    def curve_to_offset(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_3d_curve_offset.CurveToOffset = reference_curve.com_object

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Direction() As HybridShapeDirection
                | 
                |     Returns or sets the direction.

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_3d_curve_offset.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_3d_curve_offset.Direction = direction.com_object

    @property
    def invert_direction(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InvertDirection() As boolean
                | 
                |     Returns or sets the direction orientation.

        :rtype: bool
        """

        return self.hybrid_shape_3d_curve_offset.InvertDirection

    @invert_direction.setter
    def invert_direction(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_3d_curve_offset.InvertDirection = value

    @property
    def offset_value(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OffsetValue() As Length
                | 
                |     Returns or sets the OffsetValue.

        :rtype: Length
        """

        return Length(self.hybrid_shape_3d_curve_offset.OffsetValue)

    @offset_value.setter
    def offset_value(self, length: Length):
        """
        :param Length length:
        """

        self.hybrid_shape_3d_curve_offset.OffsetValue = length

    def __repr__(self):
        return f'HybridShape3DCurveOffset(name="{self.name}")'
