#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.line import Line
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length


class HybridShapeLineAngle(Line):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLineAngle
                | 
                | Line defined from a reference curve, a plane or a surface, a point and an
                | angle.
                | Role: Allows to access data of the the line feature created with an angle to a
                | curve.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_angle = com_object

    @property
    def angle(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Angle() As Angle (Read Only)
                | 
                |     Role: Get the angle to the reference curve of the line.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             angle

        :return: Angle
        """

        return Angle(self.hybrid_shape_line_angle.Angle)

    @property
    def begin_offset(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property BeginOffset() As Length (Read Only)
                | 
                |     Role: Get the start length of the line.
                | 
                |     Parameters:
                | 
                |         oStart
                |             start length

        :return: Length
        """

        return Length(self.hybrid_shape_line_angle.BeginOffset)

    @property
    def curve(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Curve() As Reference
                | 
                |     Role: Get the reference curve.
                | 
                |     Parameters:
                | 
                |         oCurve
                |             reference curve.

        :return: Reference
        """

        return Reference(self.hybrid_shape_line_angle.Curve)

    @curve.setter
    def curve(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_line_angle.Curve = value

    @property
    def end_offset(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property EndOffset() As Length (Read Only)
                | 
                |     Role: Get the end length of the line.
                | 
                |     Parameters:
                | 
                |         oEnd
                |             end length

        :return: Length
        """

        return Length(self.hybrid_shape_line_angle.EndOffset)

    @property
    def geodesic(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Geodesic() As boolean
                | 
                |     Role: Get geodesic mode. If geodesic, the line lies on the support surface,
                |     otherwise the surface is only used to compute the line
                |     direction.
                | 
                |     Parameters:
                | 
                |         oGeod
                |             Geodesic boolean

        :return: bool
        """

        return self.hybrid_shape_line_angle.Geodesic

    @geodesic.setter
    def geodesic(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_line_angle.Geodesic = value

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Orientation() As long
                | 
                |     Role: Get the line orientation. Orientation allows to reverse the line
                |     direction from the reference point. For a line of L length, it is the same as
                |     creating this line with -L length.
                | 
                |     Parameters:
                | 
                |         oOrientation
                |             orientation : can be 1 or -1

        :return: int
        """

        return self.hybrid_shape_line_angle.Orientation

    @orientation.setter
    def orientation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_line_angle.Orientation = value

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Point() As Reference
                | 
                |     Role: Get the starting point of the line.
                | 
                |     Parameters:
                | 
                |         oPoint
                |             starting point.

        :return: Reference
        """

        return Reference(self.hybrid_shape_line_angle.Point)

    @point.setter
    def point(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_line_angle.Point = value

    @property
    def surface(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Surface() As Reference
                | 
                |     Role: Get the support surface.
                | 
                |     Parameters:
                | 
                |         oSurface
                |             support surface.

        :return: Reference
        """

        return Reference(self.hybrid_shape_line_angle.Surface)

    @surface.setter
    def surface(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_line_angle.Surface = value

    def get_length_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetLengthType() As long
                | 
                |     Gets the length type Default is 0.
                | 
                |     Parameters:
                | 
                |         oType
                |             The length type = 0 : length - the line is limited by its extremities = 1 : infinite - the line is infinite = 2 : infinite start point - the line is infinite on the side of the start point = 3 : infinite end point - the line is infinite on the side of the end point

        :return: int
        """
        return int(self.hybrid_shape_line_angle.GetLengthType())

    def get_symmetrical_extension(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetSymmetricalExtension() As boolean
                | 
                |     Gets whether the symmetrical extension of the line is
                |     active.
                | 
                |     Parameters:
                | 
                |         oSym
                |             Symetry flag

        :return: bool
        """
        return bool(self.hybrid_shape_line_angle.GetSymmetricalExtension())

    def set_length_type(self, i_type=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetLengthType(long iType)
                | 
                |     Sets the length type Default is 0.
                | 
                |     Parameters:
                | 
                |         iType
                |             The length type = 0 : length - the line is limited by its extremities = 1 : infinite - the line is infinite = 2 : infinite start point - the line is infinite on the side of the start point = 3 : infinite end point - the line is infinite on the side of the end point

        :param int i_type:
        :return: None
        """
        return self.hybrid_shape_line_angle.SetLengthType(i_type)

    def set_symmetrical_extension(self, i_sym=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetSymmetricalExtension(boolean iSym)
                | 
                |     Sets the symmetrical extension of the line (start = -end).
                | 
                |     Parameters:
                | 
                |         iSym
                |             Symetry flag

        :param bool i_sym:
        :return: None
        """
        return self.hybrid_shape_line_angle.SetSymmetricalExtension(i_sym)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_symmetrical_extension'
        # # vba_code = """
        # # Public Function set_symmetrical_extension(hybrid_shape_line_angle)
        # #     Dim iSym (2)
        # #     hybrid_shape_line_angle.SetSymmetricalExtension iSym
        # #     set_symmetrical_extension = iSym
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeLineAngle(name="{ self.name }")'
