#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class SchInternalFlow(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchInternalFlow
                | 
                | Represents the internal flow object in a schematic component.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_internal_flow = com_object

    def get_insertion_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetInsertionType(CatSchIDLInternalFlowType
                | oEInternalFlowType)
                | 
                |     Get insertion flow type.
                | 
                |     Parameters:
                | 
                |         oEInternalFlowType
                |             Internal flow type. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchInternalFlow
                | 
                |           ...
                |          objThisIntf.GetInsertionTypeCatSchIDLInternalFlowType_Enum

        :return: enum cat_sch_idl_internal_flow_type
        :rtype: None
        """
        return self.sch_internal_flow.GetInsertionType()

    def get_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetStatus(CatSchIDLInternalFlowStatus
                | oEInternalFlowStatus)
                | 
                |     Get insertion flow status.
                | 
                |     Parameters:
                | 
                |         oEInternalFlowStatus
                |             Internal flow status. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchInternalFlow
                | 
                |           ...
                |          objThisIntf.GetStatusCatSchIDLInternalFlowStatus_Enum

        :return: enum cat_sch_idl_internal_flow_status
        :rtype: int
        """
        return self.sch_internal_flow.GetStatus()

    def list_sch_connectors(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListSchConnectors() As SchListOfObjects
                | 
                |     List all schematic connectors associated with an internal
                |     flow.
                | 
                |     Parameters:
                | 
                |         oLSchCntrs
                |             A list of schematic connector objects (members are
                |             CATISchCntrLocation interface pointers). 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchInternalFlow
                |          Dim objArg1 As SchListOfObjects
                |           ...
                |          Set objArg1 = objThisIntf.ListSchConnectors

        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_internal_flow.ListSchConnectors())

    def set_status(self, i_e_internal_flow_status: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStatus(CatSchIDLInternalFlowStatus
                | iEInternalFlowStatus)
                | 
                |     Set insertion flow status.
                | 
                |     Parameters:
                | 
                |         iEInternalFlowStatus
                |             Internal flow status. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchInternalFlow
                | 
                |           ...
                |          objThisIntf.SetStatusCatSchIDLInternalFlowStatus_Enum

        :param int i_e_internal_flow_status: enum cat_sch_idl_internal_flow_status
        :rtype: None
        """
        return self.sch_internal_flow.SetStatus(i_e_internal_flow_status)

    def __repr__(self):
        return f'SchInternalFlow(name="{self.name}")'
