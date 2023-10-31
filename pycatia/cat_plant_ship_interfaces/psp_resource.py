#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PSPResource(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspResource
                | 
                | Represents the PspResource.
                | Role: It is used to get application resources.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_resource = com_object

    def get_resource_path(self, i_resource_name: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetResourcePath(CATBSTR iResourceName) As CATBSTR
                | 
                |     Returns the path value defined for a resource.
                | 
                |     Parameters:
                | 
                |         iResourceName
                |             Resource Name 
                | 
                |     Returns:
                |         Resource Path
                |
                |     Example:
                |
                |          Dim objThisIntf As PspResource
                |          Dim strResourcePath As String
                |          Dim iResourceName As String 
                |           ...
                |          strResourcePath = objThisIntf.GetResourcePath (iResourceName)

        :param str i_resource_name:
        :rtype: str
        """
        return self.psp_resource.GetResourcePath(i_resource_name)

    def get_resource_value(self, i_resource_name: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetResourceValue(CATBSTR iResourceName) As CATBSTR
                | 
                |     Returns the value defined for a resource.
                | 
                |     Parameters:
                | 
                |         iResourceName
                |             Resource Name 
                | 
                |     Returns:
                |         Resource Value
                |
                |     Example:
                |
                |          Dim objThisIntf As PspResource
                |          Dim strResourceVal As String
                |           ...
                |          strResourceVal = objThisIntf.GetResourceValue (iResourceName)

        :param str i_resource_name:
        :rtype: str
        """
        return self.psp_resource.GetResourceValue(i_resource_name)

    def __repr__(self):
        return f'PSPResource(name="{self.name}")'
