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


class HybridShapeLinePtPt(Line):
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
                |                             HybridShapeLinePtPt
                | 
                | Represents the hybrid shape line between two points feature
                | object.
                | Role: To access the data of the line feature created between two
                | points.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeLinePtPt
                | object.
                | 
                | See also:
                |     Reference 
                | See also:
                |     Length 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_pt_pt = com_object

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
                |         LinePtPt hybrid shape feature.
                | 
                |          Dim oStart As  CATIALength 
                |          Set oStart = LinePtPt.BeginOffset

        :rtype: Length
        """

        return Length(self.hybrid_shape_line_pt_pt.BeginOffset)

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
                |         This example retrieves in oEnd the starting length for the LinePtPt
                |         hybrid shape feature.
                | 
                |          Dim oEnd As  CATIALength 
                |          Set oEnd = LinePtPt.EndOffset

        :rtype: Length
        """

        return Length(self.hybrid_shape_line_pt_pt.EndOffset)

    @property
    def pt_extremity(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PtExtremity() As Reference
                | 
                |     Returns or Sets the extremity point of the LinePtPt(Second
                |     Point).
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in oPtExtremity the ending point for the
                |         LinePtPt hybrid shape feature.
                | 
                |          Dim oPtExtremity As Reference 
                |          Set oPtExtremity = LinePtPt.PtExtremity

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_pt_pt.PtExtremity)

    @pt_extremity.setter
    def pt_extremity(self, pt_reference: Reference):
        """
        :param Reference pt_reference:
        """

        self.hybrid_shape_line_pt_pt.PtExtremity = pt_reference.com_object

    @property
    def pt_origin(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PtOrigine() As Reference
                | 
                |     Returns or Sets the origin point of the LinePtPt(First
                |     point).
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in oPtOrigine the initial point for the LinePtPt
                |         hybrid shape feature.
                | 
                |          Dim oPtOrigine As Reference 
                |          Set oPtOrigine = LinePtPt.PtOrigine

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_pt_pt.PtOrigine)

    @pt_origin.setter
    def pt_origin(self, pt_reference: Reference):
        """
        :param Reference pt_reference:
        """

        self.hybrid_shape_line_pt_pt.PtOrigine = pt_reference.com_object

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or Sets the supporting surface.
                |     Note: the support surface is not mandatory for LinePtPt
                | 
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in oSurface the supporting surface (if it exist)
                |         for the LinePtPt hybrid shape feature.
                | 
                |          Dim oSurface As Reference 
                |          Set oSurface = LinePtPt.Surface

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_pt_pt.Support)

    @support.setter
    def support(self, support_reference: Reference):
        """
        :param Reference support_reference:
        """

        self.hybrid_shape_line_pt_pt.Support = support_reference.com_object

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
                |             the side of the start point = 3 : infinite end point - the line is infinite on the side of
                |             the end point

        :rtype: int
        """
        return self.hybrid_shape_line_pt_pt.GetLengthType()

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
        return self.hybrid_shape_line_pt_pt.GetSymmetricalExtension()

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
        return self.hybrid_shape_line_pt_pt.RemoveSupport()

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
        return self.hybrid_shape_line_pt_pt.SetLengthType(i_type)

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
        return self.hybrid_shape_line_pt_pt.SetSymmetricalExtension(i_sym)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_symmetrical_extension'
        # # vba_code = """
        # # Public Function set_symmetrical_extension(hybrid_shape_line_pt_pt)
        # #     Dim iSym (2)
        # #     hybrid_shape_line_pt_pt.SetSymmetricalExtension iSym
        # #     set_symmetrical_extension = iSym
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeLinePtPt(name="{self.name}")'
