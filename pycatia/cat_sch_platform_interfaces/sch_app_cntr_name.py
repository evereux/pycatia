#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_list_of_bst_rs import SchListOfBSTRs
from pycatia.system_interfaces.any_object import AnyObject


class SchAppCntrName(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppCntrName
                | 
                | Manage a schematic connector.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_cntr_name = com_object

    def app_list_names(self) -> SchListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppListNames() As SchListOfBSTRs
                | 
                |     List connector names allowed.
                | 
                |     Parameters:
                | 
                |         oLConnectorNamesAllowed
                |             A list of connector names allowed. The caller must allocate memory
                |             for the first level pointer (i.e. oLConnectorNamesAllowed) and release the
                |             second level pointer (i.e. \\*oLConnectorNamesAllowed) after usage.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchAppCntrName
                |          Dim objArg1 As SchListOfBSTRs
                |           ...
                |          Set objArg1 = objThisIntf.AppListNames

        :rtype: SchListOfBSTRs
        """
        return SchListOfBSTRs(self.sch_app_cntr_name.AppListNames())

    def get_name(self, o_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetName(CATBSTR oName)
                | 
                |     Get the application connector name.
                | 
                |     Parameters:
                | 
                |         oName
                |             The connector name. The caller must allocate memory for the first
                |             level pointer (i.e. oName) and release the second level pointer (i.e. \\*oName)
                |             after usage. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchAppCntrName
                |          Dim strVar1 As String
                |           ...
                |          objThisIntf.GetNamestrVar1

        :param str o_name:
        :rtype: None
        """
        return self.sch_app_cntr_name.GetName(o_name)

    def set_name(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetName(CATBSTR iName)
                | 
                |     Set the application connector name.
                | 
                |     Parameters:
                | 
                |         oName
                |             The connector name. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppCntrName
                |          Dim strVar1 As String
                |           ...
                |          objThisIntf.SetNamestrVar1

        :param str i_name:
        :rtype: None
        """
        return self.sch_app_cntr_name.SetName(i_name)

    def __repr__(self):
        return f'SchAppCntrName(name="{self.name}")'
