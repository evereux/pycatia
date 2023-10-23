#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.hybrid_shape_interfaces.line import Line
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length


class HybridShapeLinePtDir(Line):
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
                |                             HybridShapeLinePtDir
                | 
                | Line defined by a point and a direction.
                | Role: To access data of the line feature created by using a passing point and a
                | direction.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeLinePtDir
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
        self.hybrid_shape_line_pt_dir = com_object

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
                |         LinePtDir hybrid shape feature.
                | 
                |          Dim oStart As  CATIALength 
                |          Set oStart = LinePtDir.BeginOffset

        :rtype: Length
        """

        return Length(self.hybrid_shape_line_pt_dir.BeginOffset)

    @property
    def dir(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Dir() As HybridShapeDirection
                | 
                |     Returns or Sets the direction of the line.
                | 
                |     Example:
                |         This example retrieves in oDir the direction for the LinePtDir hybrid
                |         shape feature.
                | 
                |          Dim oDir As CATIAHybridShapeDirection
                |          Set oDir = LinePtDir.Dir

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_line_pt_dir.Dir)

    @dir.setter
    def dir(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_line_pt_dir.Dir = direction.com_object

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
                |         This example retrieves in oEnd the starting length for the LinePtDir
                |         hybrid shape feature.
                | 
                |          Dim oEnd As  CATIALength 
                |          Set oEnd = LinePtDir.EndOffset

        :rtype: Length
        """

        return Length(self.hybrid_shape_line_pt_dir.EndOffset)

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
                |         LinePtDir hybrid shape feature.
                | 
                |          Dim oOrientation As long
                |          Set oOrientation = LinePtDir.Orientation

        :rtype: int
        """

        return self.hybrid_shape_line_pt_dir.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_line_pt_dir.Orientation = value

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
                |         This example retrieves in oPoint the starting point for the LinePtDir
                |         hybrid shape feature.
                | 
                |          Dim oPoint As Reference
                |          Set oPoint = LinePtDir.Point

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_pt_dir.Point)

    @point.setter
    def point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_line_pt_dir.Point = reference_point

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or Sets the supporting surface.
                |     Note: the support surface is not mandatory for LinePtDir
                | 
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in oSurface the supporting surface (if it exist)
                |         for the LinePtDir hybrid shape feature.
                | 
                |          Dim oSurface As Reference 
                |          Set oSurface = LinePtDir.Surface

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_pt_dir.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_line_pt_dir.Support = reference_support

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
        return self.hybrid_shape_line_pt_dir.GetLengthType()

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
        return self.hybrid_shape_line_pt_dir.GetSymmetricalExtension()

    def remove_support(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveSupport()
                | 
                |     Removes the support surface.

        :rtype: None
        """
        return self.hybrid_shape_line_pt_dir.RemoveSupport()

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
                |             1 : infinite - the line is infinite = 2 : infinite start point - the line is infinite on
                |             the side of the start point = 3 : infinite end point - the line is infinite on the side
                |             of the end point

        :param int i_type:
        :rtype: None
        """
        return self.hybrid_shape_line_pt_dir.SetLengthType(i_type)

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
        return self.hybrid_shape_line_pt_dir.SetSymmetricalExtension(i_sym)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_symmetrical_extension'
        # # vba_code = """
        # # Public Function set_symmetrical_extension(hybrid_shape_line_pt_dir)
        # #     Dim iSym (2)
        # #     hybrid_shape_line_pt_dir.SetSymmetricalExtension iSym
        # #     set_symmetrical_extension = iSym
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeLinePtDir(name="{self.name}")'
