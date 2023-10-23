#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class StrNibblingFeature(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrNibblingFeature
                | 
                | Represents a Nibbling Feature.
                | Type, SubType and Extrapolation Offset can be defined for this nibbling
                | feature.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.str_nibbling_feature = com_object

    @property
    def sub_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SubType() As CATBSTR
                | 
                |     Returns or Sets Nibbling SubType on Current Nibbling.
                | 
                |     Example:
                | 
                |           
                | 
                |           Dim NibblingFeature As StrNibblingFeature
                |           Set NibblingFeature = FeatureFactory.AddNibbling(List, "Remove")
                |           Dim NibbSubType As String
                |           NibbSubType = NibblingFeature1.SubType
                |          'Set the SubType
                |           NibblingFeature1.SubType ="ButtButt"

        :rtype: str
        """

        return self.str_nibbling_feature.SubType

    @sub_type.setter
    def sub_type(self, value: str):
        """
        :param str value:
        """

        self.str_nibbling_feature.SubType = value

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR
                | 
                |     Returns or Sets Nibbling Type on Current Nibbling.
                | 
                |     Example:
                | 
                |           
                | 
                |           Dim NibblingFeature As StrNibblingFeature
                |           Set NibblingFeature = FeatureFactory.AddNibbling(List, "Remove")
                |           Dim NibbType As String
                |           NibbType = NibblingFeature1.Type
                |           'Set the Type
                |           NibblingFeature1.Type ="LongPoint"

        :rtype: str
        """

        return self.str_nibbling_feature.Type

    @type.setter
    def type(self, value: str):
        """
        :param str value:
        """

        self.str_nibbling_feature.Type = value

    def get_offset_for_extrapolate(self, i_offset_for_extrapolate: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOffsetForExtrapolate(CATBSTR iOffsetForExtrapolate)
                | 
                |     Sets the Extrapolation offset value on Current Nibbling
                |     Feature.
                | 
                |     Parameters:
                | 
                |         iOffsetForExtrapolate
                |             [in] Default Value:"5mm" 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example
                |         :
                |             This example Applies Extrapolation offset.
                | 
                |               Dim NibblingFeature As StrNibblingFeature
                |               Set NibblingFeature = FeatureFactory.AddNibbling(List, "Remove")
                |               NibblingFeature.GetOffsetForExtrapolate("0mm")
                |              
                | 
                |     Copyright © 1999-2011, Dassault Systèmes. All rights
                |     reserved.

        :param str i_offset_for_extrapolate:
        :rtype: None
        """
        return self.str_nibbling_feature.GetOffsetForExtrapolate(i_offset_for_extrapolate)

    def __repr__(self):
        return f'StrNibblingFeature(name="{ self.name }")'
