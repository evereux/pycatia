#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SWKErgoRULA(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SWKErgoRULA
                | 
                | This interface deals the RULA ergonomic analysis.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_ergo_rula = com_object

    @property
    def arm_abducted(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ArmAbducted() As boolean (Read Only)
                | 
                |     This property is True if the arm of the manikin is abducted, given the
                |     manikin's current posture.

        :rtype: bool
        """

        return self.swk_ergo_rula.ArmAbducted

    @property
    def arm_out_to_side(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ArmOutToSide() As boolean (Read Only)
                | 
                |     This property is True if the arm of the manikin is out to the side, given
                |     the manikin's current posture.

        :rtype: bool
        """

        return self.swk_ergo_rula.ArmOutToSide

    @property
    def neck_side_bending(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NeckSideBending() As boolean (Read Only)
                | 
                |     This property is True if the neck of the manikin is bent, given the
                |     manikin's current posture.

        :rtype: bool
        """

        return self.swk_ergo_rula.NeckSideBending

    @property
    def neck_twisted(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NeckTwisted() As boolean (Read Only)
                | 
                |     This property is True if the neck of the manikin is twisted, given the
                |     manikin's current posture.

        :rtype: bool
        """

        return self.swk_ergo_rula.NeckTwisted

    @property
    def object_weight(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ObjectWeight() As CATBSTR
                | 
                |     Returns or sets the weight of the object being carried.

        :rtype: str
        """

        return self.swk_ergo_rula.ObjectWeight

    @object_weight.setter
    def object_weight(self, value: str):
        """
        :param str value:
        """

        self.swk_ergo_rula.ObjectWeight = value

    @property
    def overall_score(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OverallScore() As long (Read Only)
                | 
                |     This field is the overall RULA score, given the manikin's current posture.

        :rtype: int
        """

        return self.swk_ergo_rula.OverallScore

    @property
    def shoulder_raised(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ShoulderRaised() As boolean (Read Only)
                | 
                |     This property is True if the shoulder of the manikin is raised, given the
                |     manikin's current posture.

        :rtype: bool
        """

        return self.swk_ergo_rula.ShoulderRaised

    @property
    def trunk_side_bending(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TrunkSideBending() As boolean (Read Only)
                | 
                |     This property is True if the trunk of the manikin is bent, given the
                |     manikin's current posture.

        :rtype: bool
        """

        return self.swk_ergo_rula.TrunkSideBending

    @property
    def trunk_twisted(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TrunkTwisted() As boolean (Read Only)
                | 
                |     This property is True if the trunk of the manikin is twisted, given the
                |     manikin's current posture.

        :rtype: bool
        """

        return self.swk_ergo_rula.TrunkTwisted

    @property
    def verdict(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Verdict() As CATBSTR (Read Only)
                | 
                |     This field gives a text string which represents the interpretaton of the
                |     overall RULA score.

        :rtype: str
        """

        return self.swk_ergo_rula.Verdict

    @property
    def wrist_bent(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WristBent() As boolean (Read Only)
                | 
                |     This property is True if the wrist of the manikin is bent, given the
                |     manikin's current posture.

        :rtype: bool
        """

        return self.swk_ergo_rula.WristBent

    @property
    def wrist_twisted(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WristTwisted() As boolean (Read Only)
                | 
                |     This property is True if the wrist of the manikin is twisted, given the
                |     manikin's current posture.

        :rtype: bool
        """

        return self.swk_ergo_rula.WristTwisted

    def __repr__(self):
        return f'SWKErgoRula(name="{self.name}")'
