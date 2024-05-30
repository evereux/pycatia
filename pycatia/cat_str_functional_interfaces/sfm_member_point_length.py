#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_member import SFMMember
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length


class SFMMemberPointLength(SFMMember):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATStrFunctionalInterfaces.SfmObject
                |                         CATStrFunctionalInterfaces.SfmProfile
                |                            CATStrFunctionalInterfaces.SfmMember
                |                                 SfmMemberPointLength
                | 
                | Interface to manage Member created with one point, one direction and a
                | length.
                | Role: To manage member created with one point, one direction and a
                | length.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_member_point_length = com_object

    @property
    def direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Direction() As Reference
                | 
                |     Returns or sets the direction.
                | 
                |     Example:
                |         This example retrieves in Direction the direction for the
                |         SfmMemberPointLength feature.
                | 
                |          Dim Direction As Reference
                |          Set Direction = SfmMemberPointLength.Direction

        :rtype: Reference
        """

        return Reference(self.sfm_member_point_length.Direction)

    @direction.setter
    def direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_point_length.Direction = value.com_object

    @property
    def direction_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DirectionOrientation() As long
                | 
                |     Returns or sets the direction orientation.
                | 
                |     Example:
                |         This example retrieves in DirectionOrientation the direction
                |         orientation for the SfmMemberPointLength feature.
                | 
                |          Dim DirectionOrientation As Integer
                |          Set DirectionOrientation = SfmMemberPointLength.DirectionOrientation

        :rtype: int
        """

        return self.sfm_member_point_length.DirectionOrientation

    @direction_orientation.setter
    def direction_orientation(self, value: int):
        """
        :param int value:
        """

        self.sfm_member_point_length.DirectionOrientation = value

    @property
    def length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Length() As double
                | 
                |     Returns or sets the member's length.
                | 
                |     Example:
                |         This example retrieves in Length the length of the SfmMemberPointLength
                |         feature.
                | 
                |          Dim Length As Double
                |          Set Length = SfmMember.Length

        :rtype: float
        """

        return self.sfm_member_point_length.Length

    @length.setter
    def length(self, value: float):
        """
        :param float value:
        """

        self.sfm_member_point_length.Length = value

    @property
    def length_param(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LengthParam() As Length (Read Only)

        :rtype: Length
        """

        return Length(self.sfm_member_point_length.LengthParam)

    @property
    def point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Point() As Reference
                | 
                |     Returns or sets the point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in Point the point for the SfmMemberPointLength
                |         feature.
                | 
                |          Dim Point As Reference
                |          Set Point = SfmMemberPointLength.Point

        :rtype: Reference
        """

        return Reference(self.sfm_member_point_length.Point)

    @point.setter
    def point(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_point_length.Point = value.com_object

    def invert_direction(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub InvertDirection()
                | 
                |     Inverts the direction orientation.
                | 
                |     Example:
                |         This example inverts the orientation of the direction for the
                |         SfmMemberPointLength feature.
                | 
                |          SfmMemberPointLength.InvertDirection

        :rtype: None
        """
        return self.sfm_member_point_length.InvertDirection()

    def __repr__(self):
        return f'SFMMemberPointLength(name="{self.name}")'
