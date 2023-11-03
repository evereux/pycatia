#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import TYPE_CHECKING

from pycatia.navigator_interfaces.annotated_views import AnnotatedViews
from pycatia.navigator_interfaces.group import Group
from pycatia.navigator_interfaces.marker_3Ds import Marker3Ds
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.system_service import SystemService

if TYPE_CHECKING:
    from pycatia.in_interfaces.document import Document


class Section(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Section
                | 
                | Represents the Section object.
                | The Section object is a specification of a sectioning display and
                | computationwith a section plane, section slice or section box.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.section = com_object

    @property
    def annotated_views(self) -> AnnotatedViews:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AnnotatedViews() As AnnotatedViews (Read Only)
                | 
                |     Returns the AnnotatedViews collection of the section.
                | 
                |     Example:
                | 
                |              This example retrieves the AnnotatedViews collection of NewSection
                |              Section.
                |
                |             Dim TheAnnotatedViewsList As AnnotatedViews
                |             Set TheAnnotatedViewsList = NewSection.AnnotatedViews

        :rtype: AnnotatedViews
        """

        return AnnotatedViews(self.section.AnnotatedViews)

    @property
    def behavior(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Behavior() As CatSectionBehavior
                | 
                |     Returns or sets the general behavior of the section: Freeze, Automatic
                |     update, manual update
                | 
                |     The behavior value are defined in CatSectionBehavior.
                | 
                |     Example:
                | 
                |              The first example retrieves the behavior of NewSection
                |              Section.
                |
                |             Dim SectionBehavior As CatSectionBehavior
                |             Behavior = NewSection.Behavior
                |
                |                 The second example sets the behavior of NewSection
                |                 Section.
                |
                |                 NewSection.Behavior = catSectionBehaviorAutomatic

        :return: enum cat_section_behavior
        :rtype: int
        """

        return self.section.Behavior

    @behavior.setter
    def behavior(self, value: int):
        """
        :param int value: enum cat_section_behavior
        """

        self.section.Behavior = value

    @property
    def cut_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CutMode() As long
                | 
                |     Returns or sets the cutting mode of the section.
                | 
                |     The cutting mode value is 1 for clipping or 0 without
                |     clipping.
                | 
                |     Example:
                | 
                |              The first example retrieves the cutting mode of NewSection
                |              Section.
                |
                |             Dim SectionMode As Integer
                |             SectionMode = NewSection.CutMode
                |
                |                 The second example sets the cutting mode of NewSection
                |                 Section.
                |
                |                 NewSection.CutMode = 1

        :rtype: int
        """

        return self.section.CutMode

    @cut_mode.setter
    def cut_mode(self, value: int):
        """
        :param int value:
        """

        self.section.CutMode = value

    @property
    def group(self) -> Group:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Group() As Group
                | 
                |     Returns or sets the sectioned group.
                | 
                |     By default, it is the all leaves group.
                | 
                |     Example:
                | 
                |              The first example retrieves the group of NewSection
                |              Section.
                |
                |             Dim AGroup As Group
                |             AGroup = NewSection.Group
                |
                |                 The second example sets the group of NewSection
                |                 Section.
                |
                |                 Dim AGroup As Group
                |                 NewSection.Group = AGroup

        :rtype: Group
        """

        return Group(self.section.Group)

    @group.setter
    def group(self, value: Group):
        """
        :param Group value:
        """

        self.section.Group = value

    @property
    def height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Height() As double
                | 
                |     Returns or sets the height of the section.
                | 
                |     The height value must be greater than 0.
                | 
                |     Example:
                | 
                |              The first example retrieves the height of NewSection
                |              Section.
                |
                |             Dim SectionHeight As double
                |             SectionHeight = NewSection.Height
                |
                |                 The second example sets the height value of NewSection
                |                 Section.
                |
                |                 NewSection.Height = 100.

        :rtype: float
        """

        return self.section.Height

    @height.setter
    def height(self, value: float):
        """
        :param float value:
        """

        self.section.Height = value

    @property
    def marker_3ds(self) -> Marker3Ds:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Marker3Ds() As Marker3Ds (Read Only)
                | 
                |     Returns the Marker3Ds collection of the section.
                | 
                |     Example:
                | 
                |              This example retrieves the Marker3Ds collection of NewSection
                |              Section.
                |
                |             Dim TheMarker3DsList As Marker3Ds
                |             Set TheMarker3DsList = NewSection.Marker3Ds

        :rtype: Marker3Ds
        """

        return Marker3Ds(self.section.Marker3Ds)

    @property
    def thickness(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Thickness() As double
                | 
                |     Returns or sets the thickness of the section.
                | 
                |     The thickness value must be greater than 0.
                | 
                |     Example:
                | 
                |              The first example retrieves the thickness of NewSection
                |              Section.
                |
                |             Dim SectionThickness As double
                |             SectionThickness = NewSection.Thickness
                |
                |                 The second example sets the thickness value of NewSection
                |                 Section.
                |
                |                 NewSection.Thickness = 100.

        :rtype: float
        """

        return self.section.Thickness

    @thickness.setter
    def thickness(self, value: float):
        """
        :param float value:
        """

        self.section.Thickness = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Type() As CatSectionType
                | 
                |     Returns or sets the type of the section.
                | 
                |     The type value are defined in CatSectionType.
                | 
                |     Example:
                | 
                |              The first example retrieves the type of NewSection
                |              Section.
                |
                |             Dim SectionType As CatSectionType
                |             SectionType = NewSection.Type
                |
                |                 The second example sets the type of NewSection
                |                 Section.
                |
                |                 NewSection.Type = catSectionTypeSlice

        :return: enum cat_section_type
        :rtype: int
        """

        return self.section.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value: enum cat_section_type
        """

        self.section.Type = value

    @property
    def width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Width() As double
                | 
                |     Returns or sets the width of the section.
                | 
                |     The width value must be greater than 0.
                | 
                |     Example:
                | 
                |              The first example retrieves the width of NewSection
                |              Section.
                |
                |             Dim SectionWidth As double
                |             SectionWidth = NewSection.Width
                |
                |                 The second example sets the width value of NewSection
                |                 Section.
                |
                |                 NewSection.Width = 100.

        :rtype: float
        """

        return self.section.Width

    @width.setter
    def width(self, value: float):
        """
        :param float value:
        """

        self.section.Width = value

    def export(self) -> 'Document':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Export() As Document
                | 
                |     Exports the sections curves of the section in a document.
                | 
                |     Returns:
                |         The document 
                |     Example:
                | 
                |              This example exports the section curves of NewSection Section in
                |              PartDoc document.
                |
                |             Dim PartDoc As Document
                |             PartDoc = NewSection.Export

        :rtype: Document
        """
        from pycatia.in_interfaces.document import Document
        return Document(self.section.Export())

    def get_position(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetPosition(CATSafeArrayVariant oComponents)
                | 
                |     Retrieves the position of the section.
                | 
                |     The position of the section is made of a coordinate system whose origin is
                |     the center of the section, and X and Y axes lie on the section. It is retrieved
                |     in an array of the X, Y, Z axes components and the origin components with
                |     respect to the absolute coordinate system.
                | 
                |     Parameters:
                | 
                |         oComponents
                |             The position of the section
                | 
                |                 oComponents( 0) is the X component of the
                |                 X-axis
                |                 oComponents( 1) is the Y component of the
                |                 X-axis
                |                 oComponents( 2) is the Z component of the
                |                 X-axis
                |                 oComponents( 3) is the X component of the
                |                 Y-axis
                |                 oComponents( 4) is the Y component of the
                |                 Y-axis
                |                 oComponents( 5) is the Z component of the
                |                 Y-axis
                |                 oComponents( 6) is the X component of the
                |                 Z-axis
                |                 oComponents( 7) is the Y component of the
                |                 Z-axis
                |                 oComponents( 8) is the Z component of the
                |                 Z-axis
                |                 oComponents( 9) is the X component of the
                |                 origin
                |                 oComponents(10) is the Y component of the
                |                 origin
                |                 oComponents(11) is the Z component of the origin
                |                 
                | 
                |     Example:
                | 
                |              This example retrieves the position of NewSection
                |              Section.
                |
                |             Dim Components (11)
                |             NewSection.GetPosition Components

        :rtype: tuple
        """

        vba_function_name = 'get_position'
        vba_code = """
        Public Function get_position(section)
            Dim oComponents(11)
            section.GetPosition oComponents
            get_position = oComponents
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def is_empty(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func IsEmpty() As long
                | 
                |     Indicates whether the section is empty.
                | 
                |     The indicator value is 0 if the section is empty or 1 if the section
                |     comprise at least one segment.
                | 
                |     Example:
                | 
                |              This example retrieves the information on NewSection
                |              Section.
                |
                |             Dim Indicator
                |             Indicator = NewSection.IsEmpty

        :rtype: int
        """
        return self.section.IsEmpty()

    def set_position(self, i_components: tuple):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPosition(CATSafeArrayVariant iComponents)
                | 
                |     Sets the position of the section.
                | 
                |     Parameters:
                | 
                |         oComponents
                |             The position of the section with respect to the absolute coordinate
                |             system
                | 
                |                 iComponents( 0) is the X component of the
                |                 X-axis
                |                 iComponents( 1) is the Y component of the
                |                 X-axis
                |                 iComponents( 2) is the Z component of the
                |                 X-axis
                |                 iComponents( 3) is the X component of the
                |                 Y-axis
                |                 iComponents( 4) is the Y component of the
                |                 Y-axis
                |                 iComponents( 5) is the Z component of the
                |                 Y-axis
                |                 iComponents( 6) is the X component of the
                |                 Z-axis
                |                 iComponents( 7) is the Y component of the
                |                 Z-axis
                |                 iComponents( 8) is the Z component of the
                |                 Z-axis
                |                 iComponents( 9) is the X component of the
                |                 origin
                |                 iComponents(10) is the Y component of the
                |                 origin
                |                 iComponents(11) is the Z component of the origin
                |
                |     Example:
                | 
                |              This example sets the position of NewSection
                |              Section.
                |
                |             Dim MatrixPos (11) As Double
                |             MatrixPos( 0) = 1.0
                |             MatrixPos( 1) = 0.0
                |             MatrixPos( 2) = 0.0
                |             MatrixPos( 3) = 0.0
                |             MatrixPos( 4) = 1.0
                |             MatrixPos( 5) = 0.0
                |             MatrixPos( 6) = 0.0
                |             MatrixPos( 7) = 0.0
                |             MatrixPos( 8) = 1.0
                |             MatrixPos( 9) = 1000.0
                |             MatrixPos(10) = 0.0
                |             MatrixPos(11) = 0.0
                |             NewSection.SetPosition MatrixPos

        :param tuple i_components:
        """
        return self.section.SetPosition(i_components)

    def __repr__(self):
        return f'Section(name="{self.name}")'
