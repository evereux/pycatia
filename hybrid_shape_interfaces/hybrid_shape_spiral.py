#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length
from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSpiral(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeSpiral
                | 
                | Represents the hybrid shape Spiral feature object.
                | Role: Allows to access data of the Spiral feature. This data
                | includes:
                | 
                |     type
                |     support
                |     centre point
                |     axis
                |     starting radius
                |     orientation
                |     ending angle
                |     ending radius
                |     revolution
                |     pitch
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_spiral = com_object

    @property
    def axis(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Axis() As HybridShapeDirection
                | 
                |     Reads / Changes the Spiral axis (Reference direction).

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_spiral.Axis)

    @axis.setter
    def axis(self, value):
        """
        :param HybridShapeDirection value:
        """

        self.hybrid_shape_spiral.Axis = value

    @property
    def center_point(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CenterPoint() As Reference
                | 
                |     Reads / Changes the center point of the Spiral.

        :return: Reference
        """

        return Reference(self.hybrid_shape_spiral.CenterPoint)

    @center_point.setter
    def center_point(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_spiral.CenterPoint = value

    @property
    def clockwise_revolution(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ClockwiseRevolution() As boolean
                | 
                |     Reads / Modifies the sense of revolutions .
                |     FALSE means that revolutions are counter-clockwise.
                |     TRUE means that revolutions are clockwise.

        :return: bool
        """

        return self.hybrid_shape_spiral.ClockwiseRevolution

    @clockwise_revolution.setter
    def clockwise_revolution(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_spiral.ClockwiseRevolution = value

    @property
    def ending_angle(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property EndingAngle() As Angle
                | 
                |     Reads / Changes the Ending Angle of the Spiral.

        :return: Angle
        """

        return Angle(self.hybrid_shape_spiral.EndingAngle)

    @ending_angle.setter
    def ending_angle(self, value):
        """
        :param Angle value:
        """

        self.hybrid_shape_spiral.EndingAngle = value

    @property
    def ending_radius(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property EndingRadius() As Length
                | 
                |     Reads / Changes the ending radius of the Spiral.

        :return: Length
        """

        return Length(self.hybrid_shape_spiral.EndingRadius)

    @ending_radius.setter
    def ending_radius(self, value):
        """
        :param Length value:
        """

        self.hybrid_shape_spiral.EndingRadius = value

    @property
    def invert_axis(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property InvertAxis() As boolean
                | 
                |     Reads / Modifies the orientation .
                |     FALSE means that there is no invertion (natural
                |     orientation).
                |     TRUE to invert this orientation.

        :return: bool
        """

        return self.hybrid_shape_spiral.InvertAxis

    @invert_axis.setter
    def invert_axis(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_spiral.InvertAxis = value

    @property
    def pitch(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Pitch() As Length
                | 
                |     Reads / Changes the pitch of the Spiral.

        :return: Length
        """

        return Length(self.hybrid_shape_spiral.Pitch)

    @pitch.setter
    def pitch(self, value):
        """
        :param Length value:
        """

        self.hybrid_shape_spiral.Pitch = value

    @property
    def revol_number(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property RevolNumber() As RealParam
                | 
                |     Reads / Changes the revolution number of the Spiral.

        :return: RealParam
        """

        return RealParam(self.hybrid_shape_spiral.RevolNumber)

    @revol_number.setter
    def revol_number(self, value):
        """
        :param RealParam value:
        """

        self.hybrid_shape_spiral.RevolNumber = value

    @property
    def starting_radius(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property StartingRadius() As Length
                | 
                |     Reads / Changes the starting radius of the Spiral.

        :return: Length
        """

        return Length(self.hybrid_shape_spiral.StartingRadius)

    @starting_radius.setter
    def starting_radius(self, value):
        """
        :param Length value:
        """

        self.hybrid_shape_spiral.StartingRadius = value

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Support() As Reference
                | 
                |     Reads / Changes the spiral plane support.

        :return: Reference
        """

        return Reference(self.hybrid_shape_spiral.Support)

    @support.setter
    def support(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_spiral.Support = value

    @property
    def type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Type() As long
                | 
                |     Reads / Changes the spiral type.

        :return: int
        """

        return self.hybrid_shape_spiral.Type

    @type.setter
    def type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_spiral.Type = value

    def set_angle_pitch_param(self, i_end_angle=None, i_revol_number=None, i_pitch=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetAnglePitchParam(double iEndAngle,
                | double iRevolNumber,
                | double iPitch)
                | 
                |     Sets Angle pitch parameter.

        :param float i_end_angle:
        :param float i_revol_number:
        :param float i_pitch:
        :return: None
        """
        return self.hybrid_shape_spiral.SetAnglePitchParam(i_end_angle, i_revol_number, i_pitch)

    def set_angle_radius_param(self, i_end_angle=None, i_revol_number=None, i_end_radius=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetAngleRadiusParam(double iEndAngle,
                | double iRevolNumber,
                | double iEndRadius)
                | 
                |     Sets Angle radius parameters.

        :param float i_end_angle:
        :param float i_revol_number:
        :param float i_end_radius:
        :return: None
        """
        return self.hybrid_shape_spiral.SetAngleRadiusParam(i_end_angle, i_revol_number, i_end_radius)

    def set_radius_pitch_param(self, i_end_radius=None, i_pitch=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetRadiusPitchParam(double iEndRadius,
                | double iPitch)
                | 
                |     Sets Radius pitch parameter.

        :param float i_end_radius:
        :param float i_pitch:
        :return: None
        """
        return self.hybrid_shape_spiral.SetRadiusPitchParam(i_end_radius, i_pitch)

    def __repr__(self):
        return f'HybridShapeSpiral(name="{ self.name }")'
