#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeLineAngle(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Line defined from a reference curve, a plane or a surface, a point and
                | an angle.Role: Allows to access data of the the line feature created
                | with  an angle to a curve.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_angle = com_object     

    @property
    def angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Angle
                | o Property Angle(    ) As   (Read Only)
                | 
                | Role: Get the angle to the reference curve of the line.

        :return:
        """
        return self.hybrid_shape_line_angle.Angle

    @property
    def begin_offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BeginOffset
                | o Property BeginOffset(    ) As   (Read Only)
                | 
                | Role: Get the start length of the line.

        :return:
        """
        return self.hybrid_shape_line_angle.BeginOffset

    @property
    def curve(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Curve
                | o Property Curve(    ) As
                | 
                | Role: Get the reference curve.

        :return:
        """
        return self.hybrid_shape_line_angle.Curve

    @property
    def end_offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndOffset
                | o Property EndOffset(    ) As   (Read Only)
                | 
                | Role: Get the end length of the line.

        :return:
        """
        return self.hybrid_shape_line_angle.EndOffset

    @property
    def geodesic(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Geodesic
                | o Property Geodesic(    ) As
                | 
                | Role: Get geodesic mode. If geodesic, the line lies on the
                | support surface, otherwise the surface is only used to
                | compute the line direction.

        :return:
        """
        return self.hybrid_shape_line_angle.Geodesic

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(    ) As
                | 
                | Role: Get the line orientation. Orientation allows to
                | reverse the line direction from the reference point. For a
                | line of L length, it is the same as creating this line with
                | -L length.

        :return:
        """
        return self.hybrid_shape_line_angle.Orientation

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Point
                | o Property Point(    ) As
                | 
                | Role: Get the starting point of the line.

        :return:
        """
        return self.hybrid_shape_line_angle.Point

    @property
    def surface(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Surface
                | o Property Surface(    ) As
                | 
                | Role: Get the support surface.

        :return:
        """
        return self.hybrid_shape_line_angle.Surface

    def get_length_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLengthType
                | o Func GetLengthType(    ) As
                | 
                | Gets the length type Default is 0.
                |
                | Parameters:
                | oType
                |    The length type = 0 : length               - the line is limited by its extremities
                |                    = 1 : infinite             - the line is infinite
                |                    = 2 : infinite start point - the line is infinite on the side of the start point
                |                    = 3 : infinite end point   - the line is infinite on the side of the end point


        :return:
        """
        return self.hybrid_shape_line_angle.GetLengthType()

    def get_symmetrical_extension(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSymmetricalExtension
                | o Func GetSymmetricalExtension(    ) As
                | 
                | Gets whether the symmetrical extension of the line is
                | active.
                |
                | Parameters:
                | oSym
                |        Symetry flag


        :return:
        """
        return self.hybrid_shape_line_angle.GetSymmetricalExtension()

    def set_length_type(self, i_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetLengthType
                | o Sub SetLengthType(        iType)
                | 
                | Sets the length type Default is 0.
                |
                | Parameters:
                | iType
                |    The length type = 0 : length               - the line is limited by its extremities
                |                    = 1 : infinite             - the line is infinite
                |                    = 2 : infinite start point - the line is infinite on the side of the start point
                |                    = 3 : infinite end point   - the line is infinite on the side of the end point


        :param i_type:
        :return:
        """
        return self.hybrid_shape_line_angle.SetLengthType(i_type)

    def set_symmetrical_extension(self, i_sym):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSymmetricalExtension
                | o Sub SetSymmetricalExtension(        iSym)
                | 
                | Sets the symmetrical extension of the line (start = -end).
                |
                | Parameters:
                | iSym
                |        Symetry flag


        :param i_sym:
        :return:
        """
        return self.hybrid_shape_line_angle.SetSymmetricalExtension(i_sym)

    def __repr__(self):
        return f'HybridShapeLineAngle()'
