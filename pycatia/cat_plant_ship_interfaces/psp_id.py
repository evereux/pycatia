#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PSPId(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspID
                | 
                | Represents the interface to generate and set IDs for the Distributive System
                | Objects.
                | Role: This is the interface for Plant Ship object ID
                | generation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_id = com_object

    def gen_and_put_id(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GenAndPutID() As CATBSTR
                | 
                |     Returns the Generated ID with the sequence number and is stored on the
                |     object.
                | 
                |     Returns:
                |         ID generated
                |
                |     Example:
                |
                |          Dim objThisIntf As PspID
                |          Dim iStrVar1 As String
                |           ...
                |          iStrVar1 =objThisIntf.GenAndPutID

        :rtype: str
        """
        return self.psp_id.GenAndPutID()

    def gen_and_put_id_no_gen_seq_num(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GenAndPutIDNoGenSeqNum() As CATBSTR
                | 
                |     Generates ID without the sequence number and is stored on the
                |     object.
                | 
                |     Returns:
                |         ID generated
                |
                |     Example:
                |
                |          Dim objThisIntf As PspID
                |          Dim iStrVar1 As String
                |           ...
                |          iStrVar1 =objThisIntf.GenAndPutIDNoGenSeqNum

        :rtype: str
        """
        return self.psp_id.GenAndPutIDNoGenSeqNum()

    def gen_id_no_gen_seq_num(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GenIDNoGenSeqNum() As CATBSTR
                | 
                |     Generates ID without the sequence number( if not set previously) and is not
                |     stored on the object.
                | 
                |     Parameters:
                | 
                |         oGeneratedID
                |             ID generated 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspID
                |          Dim iStrVar1 As String
                |           ...
                |          iStrVar1 =objThisIntf.GenIDNoGenSeqNum

        :rtype: str
        """
        return self.psp_id.GenIDNoGenSeqNum()

    def get_id(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetID() As CATBSTR
                | 
                |     Gets ID for the object.
                | 
                |     Returns:
                |         ID of the object. 
                |     Example:
                |
                |          Dim objThisIntf As PspID
                |          Dim iStrVar1 As String
                |           ...
                |          iStrVar1 =objThisIntf.GetID

        :rtype: str
        """
        return self.psp_id.GetID()

    def get_local_id(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLocalID() As CATBSTR
                | 
                |     Retrieves local ID of the object.
                | 
                |     Returns:
                |         Local ID generated
                |
                |     Example:
                |
                |          Dim objThisIntf As PspID
                |          Dim iStrVar1 As String
                |           ...
                |          iStrVar1 =objThisIntf.GetLocalID

        :rtype: str
        """
        return self.psp_id.GetLocalID()

    def is_id_generated(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsIDGenerated() As boolean
                | 
                |     Checks if the ID on the object is generated( based on the ID
                |     Schema).
                | 
                |     Parameters:
                | 
                |         oBIsGenerated
                |             TRUE if ID is generated from the ID schema 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspID
                |          Dim bVar1 As boolean
                |           ...
                |          bVar1 =objThisIntf.IsIDGenerated

        :rtype: bool
        """
        return self.psp_id.IsIDGenerated()

    def set_id(self, i_id: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetID(CATBSTR iID)
                | 
                |     Sets ID for the object.
                | 
                |     Parameters:
                | 
                |         oID
                |             ID to be set. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspID
                |          Dim iStrVar1 As String
                |           ...
                |          objThisIntf.SetID iStrVar1

        :param str i_id:
        :rtype: None
        """
        return self.psp_id.SetID(i_id)

    def __repr__(self):
        return f'PSPId(name="{self.name}")'
