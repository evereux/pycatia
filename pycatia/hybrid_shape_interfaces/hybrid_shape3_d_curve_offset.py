#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

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
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

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
        self.hybrid_shape3_d_curve_offset = com_object

    @property
    def corner_radius_value(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property CornerRadiusValue() As Length
                | 
                |     Returns or sets the Corner Radius Value.

        :return: Length
        """

        return Length(self.hybrid_shape3_d_curve_offset.CornerRadiusValue)

    @corner_radius_value.setter
    def corner_radius_value(self, value):
        """
        :param Length value:
        """

        self.hybrid_shape3_d_curve_offset.CornerRadiusValue = value

    @property
    def corner_tension_value(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property CornerTensionValue() As double
                | 
                |     Returns or sets the Corner Tension Value.

        :return: float
        """

        return self.hybrid_shape3_d_curve_offset.CornerTensionValue

    @corner_tension_value.setter
    def corner_tension_value(self, value):
        """
        :param float value:
        """

        self.hybrid_shape3_d_curve_offset.CornerTensionValue = value

    @property
    def curve_to_offset(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property CurveToOffset() As Reference
                | 
                |     Returns or sets the curve to offset.

        :return: Reference
        """

        return Reference(self.hybrid_shape3_d_curve_offset.CurveToOffset)

    @curve_to_offset.setter
    def curve_to_offset(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape3_d_curve_offset.CurveToOffset = value

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Direction() As HybridShapeDirection
                | 
                |     Returns or sets the direction.

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape3_d_curve_offset.Direction)

    @direction.setter
    def direction(self, value):
        """
        :param HybridShapeDirection value:
        """

        self.hybrid_shape3_d_curve_offset.Direction = value

    @property
    def invert_direction(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property InvertDirection() As boolean
                | 
                |     Returns or sets the direction orientation.

        :return: bool
        """

        return self.hybrid_shape3_d_curve_offset.InvertDirection

    @invert_direction.setter
    def invert_direction(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape3_d_curve_offset.InvertDirection = value

    @property
    def offset_value(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property OffsetValue() As Length
                | 
                |     Returns or sets the OffsetValue.

        :return: Length
        """

        return Length(self.hybrid_shape3_d_curve_offset.OffsetValue)

    @offset_value.setter
    def offset_value(self, value):
        """
        :param Length value:
        """

        self.hybrid_shape3_d_curve_offset.OffsetValue = value

    def __repr__(self):
        return f'HybridShape3DCurveOffset(name="{ self.name }")'
