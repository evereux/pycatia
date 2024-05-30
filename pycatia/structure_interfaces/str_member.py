#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.structure_interfaces.str_cutback import StrCutback
from pycatia.structure_interfaces.str_member_extremity import StrMemberExtremity
from pycatia.structure_interfaces.str_object import StrObject
from pycatia.structure_interfaces.str_section import StrSection


class StrMember(StrObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ProductStructureInterfaces.Product
                |                         StructureInterfaces.StrObject
                |                             StrMember
                | 
                | Represents a member object.
                | The member object aggregates a section coming from a catalog, a support and two
                | extremities. The member object inherits all methods from the structure object
                | and the product object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.str_member = com_object

    @property
    def angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Angle() As double
                | 
                |     Returns or set the orientation of the section on the support
                |     object.
                | 
                |     Example:
                | 
                |           
                | 
                |          angle = Member_1.Angle

        :rtype: float
        """

        return self.str_member.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.str_member.Angle = value

    @property
    def angle_parameter(self) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AngleParameter() As Parameter (Read Only)
                | 
                |     Returns the parameter used to define the orientation of the section on the
                |     support object.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim angle As Parameter
                |          Set angle = Member_1.AngleParameter

        :rtype: Parameter
        """

        return Parameter(self.str_member.AngleParameter)

    @property
    def current_anchor_point_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CurrentAnchorPointName() As CATBSTR
                | 
                |     Returns or sets the current anchor point used to locate the section on the
                |     support object.
                | 
                |     Example:
                | 
                |           
                | 
                |          name = Member_1.CurrentAnchorPointName

        :rtype: str
        """

        return self.str_member.CurrentAnchorPointName

    @current_anchor_point_name.setter
    def current_anchor_point_name(self, value: str):
        """
        :param str value:
        """

        self.str_member.CurrentAnchorPointName = value

    @property
    def end_extremity(self) -> StrMemberExtremity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndExtremity() As StrMemberExtremity (Read Only)
                | 
                |     Returns the member's end extremity object.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim extremity As StrMemberExtremity
                |          Set extremity = Member_1.EndExtremity

        :rtype: StrMemberExtremity
        """

        return StrMemberExtremity(self.str_member.EndExtremity)

    @property
    def input_support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InputSupport() As Reference (Read Only)
                | 
                |     Retrieves the input support. The input support is the given support at the
                |     creation of the member.

        :rtype: Reference
        """

        return Reference(self.str_member.InputSupport)

    @property
    def section(self) -> StrSection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Section() As StrSection (Read Only)
                | 
                |     Returns or sets the section object.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim section As StrSection
                |          Set section = Member_1.Section

        :rtype: StrSection
        """

        return StrSection(self.str_member.Section)

    @property
    def start_extremity(self) -> StrMemberExtremity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StartExtremity() As StrMemberExtremity (Read Only)
                | 
                |     Returns the member's start extremity object.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim extremity As StrMemberExtremity
                |          Set extremity = Member_1.StartExtremity

        :rtype: StrMemberExtremity
        """

        return StrMemberExtremity(self.str_member.StartExtremity)

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Support() As Reference (Read Only)
                | 
                |     Retrieves the result support object. For example, if your member object is
                |     created using two points, the result support object will be the line joining
                |     these two points.

        :rtype: Reference
        """

        return Reference(self.str_member.Support)

    @property
    def surface_reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SurfaceReference() As Reference
                | 
                |     Retrieves or sets the surface reference object for the member. The section
                |     will be oriented using this surface reference object if one is set.
                |     Nevertheless, the surface reference object can be null.
                | 
                |     Example:
                |         This example sets the reference object to null.
                | 
                |          myMember.SurfaceReference = Nothing

        :rtype: Reference
        """

        return Reference(self.str_member.SurfaceReference)

    @surface_reference.setter
    def surface_reference(self, value: Reference):
        """
        :param Reference value:
        """

        self.str_member.SurfaceReference = value.com_object

    def create_cutback(self, i_member: 'StrMember', i_cutback: int, i_offset: float) -> StrCutback:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateCutback(StrMember iMember,
                | CatStrCutbackType iCutback,
                | double iOffset) As StrCutback
                | 
                |     Creates a cutback object between two member objects.
                | 
                |     Parameters:
                | 
                |         iMember
                |             The relimiting member 
                |         iCutback
                |             The type of the cutback. 
                |         iOffset
                |             The offset used in the cutback. 
                | 
                |     Example:
                | 
                |           The following example create a cutback 
                |          
                |          
                | 
                |          Dim cutback As StrCutback
                |          Set cutback = Member_1.CreateCutback(Member_2, catStrWeldedType, 0.05)

        :param StrMember i_member:
        :param int i_cutback: enum cat_str_cutback_type
        :param float i_offset:
        :rtype: StrCutback
        """
        return StrCutback(self.str_member.CreateCutback(i_member.com_object, i_cutback, i_offset))

    def flip(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Flip()
                | 
                |     Flips the section. Useful for asymetric section as the angle section, or
                |     the channel section.
                | 
                |     Example:
                | 
                |           
                | 
                |          Member_1.Rotate(1,25)

        :rtype: None
        """
        return self.str_member.Flip()

    def rotate(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Rotate(double iAngle)
                | 
                |     Rotates the section on its support object. The given angle is applied using
                |     the current orientation of the section.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim extremity As StrMemberExtremity
                |          Set extremity = Member_1.StartExtremity

        :param float i_angle:
        :rtype: None
        """
        return self.str_member.Rotate(i_angle)

    def __repr__(self):
        return f'StrMember(name="{self.name}")'
