#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingToolMotion(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingToolMotion
                | 
                | A ManufacturingToolMotion for a Manufacturing Document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_tool_motion = com_object

    def get_attribute(self, i_attribute: str) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttribute(CATBSTR iAttribut) As Parameter
                | 
                |     Retrieve by is name the attribute of a Manufacturing
                |     ToolMotion.
                |     Each attribute is a CKE object.
                | 
                |     Example:
                |         The following example retreives in Diameter the attribute MfgDiameter
                |         of the Manufacturing ToolMotion firstToolmotion
                | 
                |          Set Diameter = firstToolmotion.GetAttribute(MfgDiameter)

        :param str i_attribute:
        :rtype: Parameter
        """
        return Parameter(self.manufacturing_tool_motion.GetAttribute(i_attribute))

    def get_feedrate(self, o_feedrate: float) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFeedrate(double oFeedrate) As CATBSTR
                | 
                |     Retrieves the Feedrate of a Manufacturing Point to point
                |     ToolMotion.
                |     If the ToolMotion is not a Manufacturing Point to point, nothing is
                |     done.
                | 
                |     Parameters:
                | 
                |         oFeedrateType
                |             Legal values: oFeedrateType can be:
                | 
                |             "RAPID"
                |             "LOCAL"
                |             "NONE"
                | 
                |         oFeedrate
                |             Feedrate value. (expressed in MKS units : m/s if linear feedrate, or m/turn if angular feedrate)
                |             Feedrate value has a meaning only if oFeedrateType is "LOCAL"
                |
                |     Example:
                |         The following example gets the feedrate type of a Manufacturing Point
                |         To Point Toolmotion submotion1
                | 
                |          dim FeedVal as double
                |          dim FeedType as CATBSTR
                |          FeedType=SubMotion1.GetFeedrate(FeedVal)

        :param float o_feedrate:
        :rtype: str
        """
        return self.manufacturing_tool_motion.GetFeedrate(o_feedrate)

    def get_goto_pt_point_coordinates(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetGotoPtPointCoordinates(double oX,
                | double oY,
                | double oZ)
                | 
                |     Retrieves coordinates on the ToolMotion.
                |     If the type of the ToolMotion is not MfgSeqMotionPoint, nothing is
                |     done.
                |     These coordinates are expressed in the current axis
                |     system.
                |     Coordinates units are millimeters.
                | 
                |     Example:
                |         The following example gets coordinates on a Manufacturing Point To
                |         Point Toolmotion submotion1
                | 
                |          dim XCoord as double
                |          dim YCoord as double
                |          dim ZCoord as double
                |          Call SubMotion1.GetGotoPtPointCoordinates(XCoord, YCoord,
                |          ZCoord)

        :param float o_x:
        :param float o_y:
        :param float o_z:
        :rtype: None
        """
        return self.manufacturing_tool_motion.GetGotoPtPointCoordinates()

    def get_pp_word(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPPWord() As CATBSTR
                | 
                |     Retrieves the content of a Manufacturing PP Word
                |     ToolMotion.
                | 
                |     Example:
                |         The following example retrieves in Message the content of the
                |         Manufacturing PPWord Toolmotion firstToolmotion
                | 
                |          dim Message as CATBSTR
                |          Message = firstToolmotion.GetPPWord

        :rtype: str
        """
        return self.manufacturing_tool_motion.GetPPWord()

    def get_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetType() As CATBSTR
                | 
                |     Retrieves the type of a Manufacturing ToolMotion.
                | 
                |     Parameters:
                | 
                |         oType
                |             Legal values: oType can be:
                | 
                |             "MfgSeqMotionPoint"
                |             "MfgSeqMotionPosition"
                |             "MfgSeqMotionDelta"
                | 
                |     Example:
                |         The following example retrieves in ThisType the type of the
                |         Manufacturing Toolmotion firstToolMotion
                | 
                |          dim ThisType as CATBSTR
                |          Set ThisType = firstToolMotion.GetType

        :rtype: str
        """
        return self.manufacturing_tool_motion.GetType()

    def set_feedrate(self, i_feedrate: float, i_feedrate_type: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetFeedrate(double iFeedrate,
                | CATBSTR iFeedrateType)
                | 
                |     Defines the feedrate of a Manufacturing Point to point
                |     ToolMotion.
                |     If the ToolMotion is not a Manufacturing Point to point, nothing is
                |     done.
                | 
                |     Parameters:
                | 
                |         iFeedrateType
                |             Legal values: iFeedrateType can be:
                | 
                |             "RAPID"
                |             "LOCAL"
                |             "NONE"
                | 
                |         oFeedrate
                |             Feedrate value. (expressed in MKS units : m/s if linear feedrate, or m/turn if angular feedrate)
                |             Feedrate value is taken into account only if iFeedrateType is
                |             "LOCAL" 
                | 
                |     Example:
                |         The following example sets a local feedrate on a Manufacturing Point To
                |         Point Toolmotion submotion1
                | 
                |          dim FeedVal as double
                |          dim FeedType as CATBSTR
                |          FeedVal = 169.0
                |          FeedType="LOCAL"
                |          Call SubMotion1.SetFeedrate(FeedVal, FeedType)

        :param float i_feedrate:
        :param str i_feedrate_type:
        :rtype: None
        """
        return self.manufacturing_tool_motion.SetFeedrate(i_feedrate, i_feedrate_type)

    def set_goto_pt_point_coordinates(self, i_x: float, i_y: float, i_z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGotoPtPointCoordinates(double iX,
                | double iY,
                | double iZ)
                | 
                |     Defines coordinates on the ToolMotion.
                |     If the type of the ToolMotion is not MfgSeqMotionPoint, nothing is
                |     done.
                |     These coordinates are expressed in the current axis
                |     system.
                |     Coordinates units are millimeters.
                | 
                |     Example:
                |         The following example sets coordinates on a Manufacturing Point To
                |         Point Toolmotion submotion1
                | 
                |          dim XCoord as double
                |          dim YCoord as double
                |          dim ZCoord as double
                |          XCoord = 10.0
                |          YCoord = 20.0
                |          ZCoord = 5.0
                |          Call SubMotion1.SetGotoPtPointCoordinates(XCoord, YCoord,
                |          ZCoord)

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :rtype: None
        """
        return self.manufacturing_tool_motion.SetGotoPtPointCoordinates(i_x, i_y, i_z)

    def set_pp_word(self, i_message: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPPWord(CATBSTR iMessage)
                | 
                |     Adds a line containing iMessage to a Manufacturing PP Word
                |     ToolMotion.
                | 
                |     Example:
                |         The following example adds the line Message to the content of the
                |         Manufacturing PPWord Toolmotion firstToolmotion
                | 
                |          firstToolmotion.SetPPWord("Message")

        :param str i_message:
        :rtype: None
        """
        return self.manufacturing_tool_motion.SetPPWord(i_message)

    def __repr__(self):
        return f'ManufacturingToolMotion(name="{self.name}")'
