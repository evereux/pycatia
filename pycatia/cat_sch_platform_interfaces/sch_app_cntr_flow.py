#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchAppCntrFlow(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppCntrFlow
                | 
                | Manage the technical attributes of a schematic connector.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_cntr_flow = com_object

    def app_get_flow_capability(self, o_e_flow_capability: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppGetFlowCapability(CatSchIDLCntrFlowCapability
                | oEFlowCapability)
                | 
                |     Query the application Flow Capability property of this
                |     connector.
                | 
                |     Parameters:
                | 
                |         oEFlowCapability
                |             Flow Capability. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppCntrFlow
                | 
                |           ...
                |         objThisIntf.AppGetFlowCapabilityCatSchIDLCntrFlowCapability_Enum

        :param int o_e_flow_capability: enum cat_sch_idl_cntr_flow_capability
        :rtype: None
        """
        return self.sch_app_cntr_flow.AppGetFlowCapability(o_e_flow_capability)

    def app_get_flow_reality(self, o_e_flow_reality: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppGetFlowReality(CatSchIDLCntrFlowReality
                | oEFlowReality)
                | 
                |     Query the application Flow Reality property of this
                |     connector.
                | 
                |     Parameters:
                | 
                |         oEFlowReality
                |             Flow Reality. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchAppCntrFlow
                | 
                |           ...
                |         objThisIntf.AppGetFlowRealityCatSchIDLCntrFlowReality_Enum

        :param int o_e_flow_reality: enum cat_sch_idl_cntr_flow_reality
        :rtype: None
        """
        return self.sch_app_cntr_flow.AppGetFlowReality(o_e_flow_reality)

    def app_set_flow_capability(self, i_e_flow_capability: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppSetFlowCapability(CatSchIDLCntrFlowCapability
                | iEFlowCapability)
                | 
                |     Set the application Flow Capability property of this
                |     connector.
                | 
                |     Parameters:
                | 
                |         iEFlowCapability
                |             Flow Capability property to be set. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppCntrFlow
                | 
                |           ...
                |         objThisIntf.AppSetFlowCapabilityCatSchIDLCntrFlowCapability_Enum

        :param int i_e_flow_capability: enum cat_sch_idl_cntr_flow_capability
        :rtype: None
        """
        return self.sch_app_cntr_flow.AppSetFlowCapability(i_e_flow_capability)

    def app_set_flow_reality(self, i_e_flow_reality: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppSetFlowReality(CatSchIDLCntrFlowReality
                | iEFlowReality)
                | 
                |     Set the application Flow Reality property of this
                |     connector.
                | 
                |     Parameters:
                | 
                |         iEFlowReality
                |             Flow Reality property to be set. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppCntrFlow
                | 
                |           ...
                |         objThisIntf.AppSetFlowRealityCatSchIDLCntrFlowReality_Enum

        :param int i_e_flow_reality: enum cat_sch_idl_cntr_flow_reality
        :rtype: None
        """
        return self.sch_app_cntr_flow.AppSetFlowReality(i_e_flow_reality)

    def __repr__(self):
        return f'SchAppCntrFlow(name="{self.name}")'
