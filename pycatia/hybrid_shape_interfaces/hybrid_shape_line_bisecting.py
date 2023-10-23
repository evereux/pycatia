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


class HybridShapeLineBisecting(Line):
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
                |                             HybridShapeLineBisecting
                | 
                | Represents the hybrid shape bisecting line feature object.
                | Role: To access the data of the hybrid shape bisecting line feature object.
                | This data includes:
                | 
                |     The two lines used to create the bisecting line
                |     The reference point
                |     The support
                |     The start and end offsets
                |     The orientation
                |     The solution type
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeAffinity
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_bisecting = com_object

    @property
    def begin_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BeginOffset() As Length (Read Only)
                | 
                |     Returns the start offset of the line.

        :rtype: Length
        """

        return Length(self.hybrid_shape_line_bisecting.BeginOffset)

    @property
    def elem1(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Elem1() As Reference
                | 
                |     Returns or sets the first line used to create the bisecting
                |     line.
                | 
                |     Sub-element(s) supported (see Boundary object): see
                |     RectilinearTriDimFeatEdge or RectilinearBiDimFeatEdge.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_bisecting.Elem1)

    @elem1.setter
    def elem1(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_line_bisecting.Elem1 = reference_element.com_object

    @property
    def elem2(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Elem2() As Reference
                | 
                |     Returns or sets the second line used to create the bisecting
                |     line.
                |     Sub-element(s) supported (see Boundary object): see
                |     RectilinearTriDimFeatEdge or RectilinearBiDimFeatEdge.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_bisecting.Elem2)

    @elem2.setter
    def elem2(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_line_bisecting.Elem2 = reference_element.com_object

    @property
    def end_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EndOffset() As Length (Read Only)
                | 
                |     Returns the end offset of the line.

        :rtype: Length
        """

        return Length(self.hybrid_shape_line_bisecting.EndOffset)

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation() As long
                | 
                |     Returns or sets the orientation used to compute the bisecting
                |     line.
                |     Role: the orientation specifies bisecting line position
                |     Legal values: The orientation can be the same(1) or the inverse(-1)

        :rtype: int
        """

        return self.hybrid_shape_line_bisecting.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_line_bisecting.Orientation = value

    @property
    def ref_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RefPoint() As Reference
                | 
                |     Returns or sets the reference point used to create the bisecting
                |     line.
                |     Sub-element(s) supported (see Boundary object): see Vertex.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_bisecting.RefPoint)

    @ref_point.setter
    def ref_point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_line_bisecting.RefPoint = reference_point.com_object

    @property
    def solution_type(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SolutionType() As boolean
                | 
                |     Returns or sets the solution type.
                |     Role: The solution type allows you to know where is the bisecting line.

        :rtype: bool
        """

        return self.hybrid_shape_line_bisecting.SolutionType

    @solution_type.setter
    def solution_type(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_line_bisecting.SolutionType = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or sets the support used to create the bisecting
                |     line.
                | 
                |     Parameters:
                | 
                |         oElem
                |             retrieve the support of the bisecting line.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): see Face.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_bisecting.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_line_bisecting.Support = reference_support.com_object

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
                |              of the end point

        :rtype: int
        """
        return self.hybrid_shape_line_bisecting.GetLengthType()

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
        return self.hybrid_shape_line_bisecting.GetSymmetricalExtension()

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
        return self.hybrid_shape_line_bisecting.SetLengthType(i_type)

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
        return self.hybrid_shape_line_bisecting.SetSymmetricalExtension(i_sym)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_symmetrical_extension'
        # # vba_code = """
        # # Public Function set_symmetrical_extension(hybrid_shape_line_bisecting)
        # #     Dim iSym (2)
        # #     hybrid_shape_line_bisecting.SetSymmetricalExtension iSym
        # #     set_symmetrical_extension = iSym
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeLineBisecting(name="{self.name}")'
