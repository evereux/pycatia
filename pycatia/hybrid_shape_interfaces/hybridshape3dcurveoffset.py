#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShape3DCurveOffset(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape 3DCurve Offset operation feature.Role:
                | Allows you to access data of the 3D Curve Offset feature created by
                | using  a curve, a direction and three litteral parameters

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape3_d_curve_offset = com_object

    @property
    def corner_radius_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CornerRadiusValue
                | o Property CornerRadiusValue(    ) As
                | 
                | Returns or sets the Corner Radius Value.

        :return: Length
        """
        return Length(self.hybrid_shape3_d_curve_offset.CornerRadiusValue)

    @corner_radius_value.setter
    def corner_radius_value(self, value):
        """
            :param float value:
        """
        self.hybrid_shape3_d_curve_offset.CornerRadiusValue = value

    @property
    def corner_tension_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CornerTensionValue
                | o Property CornerTensionValue(    ) As
                | 
                | Returns or sets the Corner Tension Value.

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
            CAA V5 Visual Basic help

                | CurveToOffset
                | o Property CurveToOffset(    ) As
                | 
                | Returns or sets the curve to offset.

        :return: Reference
        """
        return Reference(self.hybrid_shape3_d_curve_offset.CurveToOffset)

    @curve_to_offset.setter
    def curve_to_offset(self, value):
        """
            :param Reference() value:
        """
        self.hybrid_shape3_d_curve_offset.CurveToOffset = value

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction
                | o Property Direction(    ) As
                | 
                | Returns or sets the direction.

        :return:
        """
        return self.hybrid_shape3_d_curve_offset.Direction

    @direction.setter
    def direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape3_d_curve_offset.Direction = value

    @property
    def invert_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertDirection
                | o Property InvertDirection(    ) As
                | 
                | Returns or sets the direction orientation.

        :return:
        """
        return self.hybrid_shape3_d_curve_offset.InvertDirection

    @invert_direction.setter
    def invert_direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape3_d_curve_offset.InvertDirection = value

    @property
    def offset_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OffsetValue
                | o Property OffsetValue(    ) As
                | 
                | Returns or sets the OffsetValue.

        :return:
        """
        return self.hybrid_shape3_d_curve_offset.OffsetValue

    @offset_value.setter
    def offset_value(self, value):
        """
            :param type value:
        """
        self.hybrid_shape3_d_curve_offset.OffsetValue = value

    def __repr__(self):
        return f'HybridShape3DCurveOffset(name="{self.name}")'
