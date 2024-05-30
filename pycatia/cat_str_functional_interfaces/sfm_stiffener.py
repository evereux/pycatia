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
from pycatia.knowledge_interfaces.length import Length


class SFMStiffener(SFMProfile):
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
                |                             SfmStiffener
                | 
                | Interface to manage the structure frame modeling Stiffener object Role: Allows
                | accessing and setting of Stiffener's data.
                | 
                | See also:
                |     SfmFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_stiffener = com_object

    @property
    def angle_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AngleMode() As long
                | 
                |     Returns or sets the angle mode.
                | 
                |     Example:
                |         This example retrieves in AngleMode the angle mode of the SfmStiffener
                |         feature.
                | 
                |          Dim AngleMode As Integer
                |          Set AngleMode = SfmStiffener.AngleMode

        :rtype: int
        """

        return self.sfm_stiffener.AngleMode

    @angle_mode.setter
    def angle_mode(self, value: int):
        """
        :param int value:
        """

        self.sfm_stiffener.AngleMode = value

    @property
    def section_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectionOrientation() As long
                | 
                |     Returns or sets the section orientation.
                | 
                |     Example:
                |         This example retrieves section orientation of the
                |         Stiffener.
                | 
                |          Dim Orient As Long
                |          Orient = SfmStiffener.SectionOrientation

        :rtype: int
        """

        return self.sfm_stiffener.SectionOrientation

    @section_orientation.setter
    def section_orientation(self, value: int):
        """
        :param int value:
        """

        self.sfm_stiffener.SectionOrientation = value

    @property
    def side_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SideOrientation() As long
                | 
                |     Returns or sets the side orientation. iOrientation value can be selected from InvertOrientation = -1, UnknownOrientation = 0, SameOrientation = 1, GlobalOrientation(Xp) = 2, GlobalOrientation(Xm) = 3, GlobalOrientation(Yp) = 4, GlobalOrientation(Ym) = 5, GlobalOrientation(Zp) = 6, GlobalOrientation(Zm) = 7, GlobalOrientation_Inside = 8, [SameOrientation ] GlobalOrientation_Outside = 9, [InvertOrientation ] GlobalOrientation_LInboard = 10 [Toward center line] GlobalOrientation_LOutboard = 11 [Opposite of previous one ] GlobalOrientation_TInboard = 12 [Toward midship ] GlobalOrientation_TOutboard = 13 [Opposite of previous one]
                | 
                |     Example:
                |         This example retrieves side orientation of the
                |         Stiffener.
                | 
                |          Dim Orient As Long
                |          Orient = SfmStiffener.SideOrientation

        :rtype: int
        """

        return self.sfm_stiffener.SideOrientation

    @side_orientation.setter
    def side_orientation(self, value: int):
        """
        :param int value:
        """

        self.sfm_stiffener.SideOrientation = value

    @property
    def web_support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WebSupport() As Reference
                | 
                |     Returns or sets the web support.
                | 
                |     Example:
                |         This example retrieves in WebSupport the web support of the
                |         SfmStiffener feature.
                | 
                |          Dim WebSupport As Reference
                |          Set WebSupport = SfmStiffener.WebSupport

        :rtype: Reference
        """

        return Reference(self.sfm_stiffener.WebSupport)

    @web_support.setter
    def web_support(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_stiffener.WebSupport = value.com_object

    @property
    def web_support_offset(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WebSupportOffset() As double
                | 
                |     Returns or sets the Stiffener's web support offset.
                | 
                |     Example:
                |         This example retrieves in Offset the web support offset of the
                |         SfmStiffener feature.
                | 
                |          Dim Offset As Double
                |          Set Offset = SfmStiffener.WebSupportOffset

        :rtype: float
        """

        return self.sfm_stiffener.WebSupportOffset

    @web_support_offset.setter
    def web_support_offset(self, value: float):
        """
        :param float value:
        """

        self.sfm_stiffener.WebSupportOffset = value

    @property
    def web_support_offset_param(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WebSupportOffsetParam() As Length (Read Only)

        :rtype: Length
        """

        return Length(self.sfm_stiffener.WebSupportOffsetParam)

    def get_molded_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMoldedSurface() As Reference
                | 
                |     Returns or sets the molded surface.
                | 
                |     Example:
                |         This example retrieves in MoldedSurface the molded surface of the
                |         SfmStiffener feature.
                | 
                |          Dim MoldedSurface As Reference
                |          Set MoldedSurface = SfmStiffener.GetMoldedSurface

        :rtype: Reference
        """
        return Reference(self.sfm_stiffener.GetMoldedSurface())

    def get_welds(self, i_operating_ele: Reference) -> SFMWelds:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetWelds(Reference iOperatingEle) As SfmWelds
                | 
                |     Returns the weld features on the Existing Stiffener.
                | 
                |     Example:
                |         This example retrieves the number of weld features on the Existing
                |         Stiffener.
                | 
                |          Dim OperatedStiffenerObject  As SfmStiffenerObject
                |          Dim Welds As SfmWelds
                |          Set Welds = OperatedStiffenerObject.GetWelds(Nothing)

        :param Reference i_operating_ele:
        :rtype: SFMWelds
        """
        return SFMWelds(self.sfm_stiffener.GetWelds(i_operating_ele.com_object))

    def is_angle_mode_valid(self, i_angle_mode: int) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsAngleModeValid(long iAngleMode) As boolean
                | 
                |     Gets the status about the validity of the angle mode regarding the nature
                |     of the web support (curve or surface).
                | 
                |     Example:
                |         This example retrieves in IsAngleModeValid the angle mode of the
                |         SfmStiffener feature.
                | 
                |          Dim IsAngleModeValid As Bool
                |          Set IsAngleModeValid = SfmStiffener.IsAngleModeValid

        :param int i_angle_mode:
        :rtype: bool
        """
        return self.sfm_stiffener.IsAngleModeValid(i_angle_mode)

    def __repr__(self):
        return f'SFMStiffener(name="{self.name}")'
