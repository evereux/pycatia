#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeSpiral(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape Spiral feature object.Role: Allows to
                | access data of the Spiral feature.   This data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_spiral = com_object     

    @property
    def axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Axis
                | o Property Axis(    ) As
                | 
                | Reads / Changes the Spiral axis (Reference direction).

        :return:
        """
        return self.hybrid_shape_spiral.Axis

    @property
    def center_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CenterPoint
                | o Property CenterPoint(    ) As
                | 
                | Reads / Changes the center point of the Spiral.

        :return:
        """
        return self.hybrid_shape_spiral.CenterPoint

    @property
    def clockwise_revolution(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ClockwiseRevolution
                | o Property ClockwiseRevolution(    ) As
                | 
                | Reads / Modifies the sense of revolutions . FALSE means that
                | revolutions are counter-clockwise. TRUE means that
                | revolutions are clockwise.

        :return:
        """
        return self.hybrid_shape_spiral.ClockwiseRevolution

    @property
    def ending_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndingAngle
                | o Property EndingAngle(    ) As
                | 
                | Reads / Changes the Ending Angle of the Spiral.

        :return:
        """
        return self.hybrid_shape_spiral.EndingAngle

    @property
    def ending_radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndingRadius
                | o Property EndingRadius(    ) As
                | 
                | Reads / Changes the ending radius of the Spiral.

        :return:
        """
        return self.hybrid_shape_spiral.EndingRadius

    @property
    def invert_axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertAxis
                | o Property InvertAxis(    ) As
                | 
                | Reads / Modifies the orientation . FALSE means that there is
                | no invertion (natural orientation). TRUE to invert this
                | orientation.

        :return:
        """
        return self.hybrid_shape_spiral.InvertAxis

    @property
    def pitch(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Pitch
                | o Property Pitch(    ) As
                | 
                | Reads / Changes the pitch of the Spiral.

        :return:
        """
        return self.hybrid_shape_spiral.Pitch

    @property
    def revol_number(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RevolNumber
                | o Property RevolNumber(    ) As
                | 
                | Reads / Changes the revolution number of the Spiral.

        :return:
        """
        return self.hybrid_shape_spiral.RevolNumber

    @property
    def starting_radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | StartingRadius
                | o Property StartingRadius(    ) As
                | 
                | Reads / Changes the starting radius of the Spiral.

        :return:
        """
        return self.hybrid_shape_spiral.StartingRadius

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Reads / Changes the spiral plane support.

        :return:
        """
        return self.hybrid_shape_spiral.Support

    @property
    def type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Type
                | o Property Type(    ) As
                | 
                | Reads / Changes the spiral type.

        :return:
        """
        return self.hybrid_shape_spiral.Type

    def set_angle_pitch_param(self, i_end_angle, i_revol_number, i_pitch):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAnglePitchParam
                | o Sub SetAnglePitchParam(        iEndAngle,
                |                                  iRevolNumber,
                |                                  iPitch)
                | 
                | Sets Angle pitch parameter.
                |
                | Parameters:


        :param i_end_angle:
        :param i_revol_number:
        :param i_pitch:
        :return:
        """
        return self.hybrid_shape_spiral.SetAnglePitchParam(i_end_angle, i_revol_number, i_pitch)

    def set_angle_radius_param(self, i_end_angle, i_revol_number, i_end_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAngleRadiusParam
                | o Sub SetAngleRadiusParam(        iEndAngle,
                |                                   iRevolNumber,
                |                                   iEndRadius)
                | 
                | Sets Angle radius parameters.
                |
                | Parameters:


        :param i_end_angle:
        :param i_revol_number:
        :param i_end_radius:
        :return:
        """
        return self.hybrid_shape_spiral.SetAngleRadiusParam(i_end_angle, i_revol_number, i_end_radius)

    def set_radius_pitch_param(self, i_end_radius, i_pitch):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetRadiusPitchParam
                | o Sub SetRadiusPitchParam(        iEndRadius,
                |                                   iPitch)
                | 
                | Sets Radius pitch parameter.
                |
                | Parameters:


        :param i_end_radius:
        :param i_pitch:
        :return:
        """
        return self.hybrid_shape_spiral.SetRadiusPitchParam(i_end_radius, i_pitch)

    def __repr__(self):
        return f'HybridShapeSpiral()'
