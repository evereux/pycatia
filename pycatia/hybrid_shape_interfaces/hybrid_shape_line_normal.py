#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.line import Line
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length


class HybridShapeLineNormal(Line):
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
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLineNormal
                | 
                | Line defined by a point and a direction normal to a surface.
                | Role: To access data of the line feature created by using the normal direction
                | of a surface
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeLineNormal
                | object.
                | 
                | See also:
                |     Reference 
                | See also:
                |     Length 
                | See also:
                |     HybridShapeDirection 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_normal = com_object

    @property
    def begin_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BeginOffset() As Length (Read Only)
                | 
                |     Returns the start length of the line.
                |     Start length : extension of the line, beginning at the starting point
                | 
                |     Example:
                |         This example retrieves in oStart the beginning offset length for the
                |         LineNormal hybrid shape feature.
                | 
                |          Dim oStart As  CATIALength 
                |          Set oStart = LineNormal.BeginOffset

        :rtype: Length
        """

        return Length(self.hybrid_shape_line_normal.BeginOffset)

    @property
    def end_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EndOffset() As Length (Read Only)
                | 
                |     Returns the end length of the line.
                |     End length : extension of the line, beginning at the ending point
                | 
                |     Example:
                |         This example retrieves in oEnd the starting length for the LineNormal
                |         hybrid shape feature.
                | 
                |          Dim oEnd As  CATIALength 
                |          Set oEnd = LineNormal.EndOffset

        :rtype: Length
        """

        return Length(self.hybrid_shape_line_normal.EndOffset)

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation() As long
                | 
                |     Returns or Sets the line orientation.
                |     Orientation allows to reverse the line direction from the reference
                |     point.
                |     For a line of L length, it is the same as creating this line with -L length :
                |     Orientation : can be 1 or -1
                | 
                |     Example:
                |         This example retrieves in oOrientation the starting length for the
                |         LineNormal hybrid shape feature.
                | 
                |          Dim oOrientation As long
                |          Set oOrientation = LineNormal.Orientation

        :rtype: int
        """

        return self.hybrid_shape_line_normal.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_line_normal.Orientation = value

    @property
    def point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Point() As Reference
                | 
                |     Returns or Sets the starting point of the line.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in oPoint the starting point for the LineNormal
                |         hybrid shape feature.
                | 
                |          Dim oPoint As Reference
                |          Set oPoint = LineNormal.Point

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_normal.Point)

    @point.setter
    def point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_line_normal.Point = reference_point.com_object

    @property
    def surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Surface() As Reference
                | 
                |     Returns or Sets the surface to which the line will be
                |     normal.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in oSurface the surface for the LineNormal
                |         hybrid shape feature.
                | 
                |          Dim oSurface As Reference 
                |          Set oSurface = LineNormal.Surface

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_normal.Surface)

    @surface.setter
    def surface(self, surface_reference: Reference):
        """
        :param Reference surface_reference:
        """

        self.hybrid_shape_line_normal.Surface = surface_reference.com_object

    def get_length_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLengthType() As long
                | 
                |     Gets the length type Default is 0.
                | 
                |     Parameters:
                | 
                |         oType
                |             The length type = 0 : length - the line is limited by its extremities =
                |             1 : infinite - the line is infinite = 2 : infinite start point - the line is infinite on
                |             the side of the start point = 3 : infinite end point - the line is infinite on the side
                |             of the end point

        :rtype: int
        """
        return self.hybrid_shape_line_normal.GetLengthType()

    def get_symmetrical_extension(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetSymmetricalExtension() As boolean
                | 
                |     Gets whether the symmetrical extension of the line is
                |     active.
                | 
                |     Parameters:
                | 
                |         oSym
                |             Symetry flag

        :rtype: bool
        """
        return self.hybrid_shape_line_normal.GetSymmetricalExtension()

    def set_length_type(self, i_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLengthType(long iType)
                | 
                |     Sets the length type Default is 0.
                | 
                |     Parameters:
                | 
                |         iType
                |             The length type = 0 : length - the line is limited by its extremities =
                |             1 : infinite - the line is infinite =
                |             2 : infinite start point - the line is infinite on the side of the start point =
                |             3 : infinite end point - the line is infinite on the side of the end point

        :param int i_type:
        :rtype: None
        """
        return self.hybrid_shape_line_normal.SetLengthType(i_type)

    def set_symmetrical_extension(self, i_sym: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSymmetricalExtension(boolean iSym)
                | 
                |     Sets the symmetrical extension of the line (start = -end).
                | 
                |     Parameters:
                | 
                |         iSym
                |             Symetry flag

        :param bool i_sym:
        :rtype: None
        """
        return self.hybrid_shape_line_normal.SetSymmetricalExtension(i_sym)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_symmetrical_extension'
        # # vba_code = """
        # # Public Function set_symmetrical_extension(hybrid_shape_line_normal)
        # #     Dim iSym (2)
        # #     hybrid_shape_line_normal.SetSymmetricalExtension iSym
        # #     set_symmetrical_extension = iSym
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeLineNormal(name="{self.name}")'
