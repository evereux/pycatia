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


class SFMMemberPointUpToLimit(SFMMember):
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
                |                                 SfmMemberPointUpToLimit
                | 
                | Interface to manage Member created with one point, one direction and one
                | limit.
                | Role: To manage member created with one point, one direction and one
                | limit.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_member_point_up_to_limit = com_object

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
                |         SfmMemberPointUpToLimit feature.
                | 
                |          Dim Direction As Reference
                |          Set Direction = SfmMemberPointUpToLimit.Direction

        :rtype: Reference
        """

        return Reference(self.sfm_member_point_up_to_limit.Direction)

    @direction.setter
    def direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_point_up_to_limit.Direction = value.com_object

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
                |         orientation for the SfmMemberPointUpToLimit feature.
                | 
                |          Dim DirectionOrientation As Integer
                |          Set DirectionOrientation = SfmMemberPointUpToLimit.DirectionOrientation

        :rtype: int
        """

        return self.sfm_member_point_up_to_limit.DirectionOrientation

    @direction_orientation.setter
    def direction_orientation(self, value: int):
        """
        :param int value:
        """

        self.sfm_member_point_up_to_limit.DirectionOrientation = value

    @property
    def limit(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Limit() As Reference
                | 
                |     Returns or sets the limit.
                | 
                |     Example:
                |         This example retrieves in Limit the limit for the
                |         SfmMemberPointUpToLimit feature.
                | 
                |          Dim Limit As Reference
                |          Set Limit = SfmMemberPointUpToLimit.Limit

        :rtype: Reference
        """

        return Reference(self.sfm_member_point_up_to_limit.Limit)

    @limit.setter
    def limit(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_point_up_to_limit.Limit = value.com_object

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
                |         This example retrieves in Point the point for the
                |         SfmMemberPointUpToLimit feature.
                | 
                |          Dim Point As Reference
                |          Set Point = SfmMemberPointUpToLimit.Point

        :rtype: Reference
        """

        return Reference(self.sfm_member_point_up_to_limit.Point)

    @point.setter
    def point(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_member_point_up_to_limit.Point = value.com_object

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
                |         SfmMemberPointUpToLimit feature.
                | 
                |          SfmMemberPointUpToLimit.InvertDirection

        :rtype: None
        """
        return self.sfm_member_point_up_to_limit.InvertDirection()

    def __repr__(self):
        return f'SFMMemberPointUpToLimit(name="{self.name}")'
