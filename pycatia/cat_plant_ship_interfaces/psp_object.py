#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PSPObject(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspObject
                | 
                | Represents PspObject.
                | Role: To access Plant Ship object information.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_object = com_object

    @property
    def application_id(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ApplicationID() As CatPspIDLApplicationID (Read
                | Only)
                | 
                |     Returns the ApplicationID of the object.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspObject
                |          Dim eApplID As CatPSPIDLApplicationID
                |           ...
                |          eApplID = objThisIntf.ApplicationID

        :return: enum cat_psp_idl_application_id
        :rtype: int
        """

        return self.psp_object.ApplicationID

    @property
    def domain_id(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DomainID() As CatPspIDLDomainID (Read Only)
                | 
                |     Returns the DomainID of the object.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspObject
                |          Dim eDomanID As CatPspIDLDomainID
                |           ...
                |          eDomanID = objThisIntf.DomainID

        :return: enum cat_psp_idl_domain_id
        :rtype: int
        """

        return self.psp_object.DomainID

    @property
    def startup_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StartupType() As CATBSTR (Read Only)
                | 
                |     Returns the Startup type of the object.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspObject
                |          Dim strStartUp As String
                |          ...
                |          strStartUp = objThisIntf.StartupType

        :rtype: str
        """

        return self.psp_object.StartupType

    def __repr__(self):
        return f'PSPObject(name="{self.name}")'
