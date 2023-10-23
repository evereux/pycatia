#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_profile import SFMProfile
from pycatia.cat_str_functional_interfaces.sfm_welds import SFMWelds
from pycatia.in_interfaces.reference import Reference


class SFMMember(SFMProfile):
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
                |                             SfmMember
                | 
                | Interface to manage the structure frame modeling member object Role: Allows
                | accessing and setting of member's data.
                | 
                | See also:
                |     SfmFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_member = com_object

    def flip(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Flip()
                | 
                |     Flip the member's section according to X axis.
                | 
                |     Example:
                |         This example flips the section of the SfmMember
                |         feature.
                | 
                |          SfmMember.Flip

        :rtype: None
        """
        return self.sfm_member.Flip()

    def get_member_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMemberType() As CATBSTR
                | 
                |     Returns the Type of Member (SfmMemberPointLength, SfmMemberPointLimit, SfmMember2Points,
                |                                 SfmMemberCurve,SfmMemberMembersPlane,SfmMemberSurfSurf)
                |
                |     Example:
                |         This example retrieves the Type of Existing Member.
                | 
                |          Dim Name As String
                |          Name = SfmMemberObj.GetMemberType

        :rtype: str
        """
        return self.sfm_member.GetMemberType()

    def get_welds(self, i_operating_ele: Reference) -> SFMWelds:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetWelds(Reference iOperatingEle) As SfmWelds
                | 
                |     Returns the weld features on the Existing Member.
                | 
                |     Example:
                |         This example retrieves the number of weld features on the Existing
                |         Member.
                | 
                |          Dim DeckMember1 As SfmMember
                |          Set DeckMember1 = SelctionObj.FindObject("CATIASfmMember")
                |          Dim OperatedMemberObject As SfmMemberObject
                |          Set OperatedMemberObject = DeckMember1.GetItem("SfmMemberObject")
                |          Dim Welds As SfmWelds
                |          Set Welds = OperatedMemberObject.GetWelds(Nothing)

        :param Reference i_operating_ele:
        :rtype: SFMWelds
        """
        return SFMWelds(self.sfm_member.GetWelds(i_operating_ele.com_object))

    def is_flip(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsFlip() As boolean
                | 
                |     Get the flip status of the member's section.
                | 
                |     Example:
                |         This example retrieves in FlipStatus the flip status of the SfmMember
                |         feature.
                | 
                |          Dim FlipStatus As Boolean
                |          Set FlipStatus = SfmMember.IsFlip

        :rtype: bool
        """
        return self.sfm_member.IsFlip()

    def __repr__(self):
        return f'SFMMember(name="{self.name}")'
