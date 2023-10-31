#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PSPCntrFlow(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspCntrFlow
                | 
                | Represents Interface to manage Connector Flow property.
                | Role: To query and modify Plant-Ship Connector Flow property.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_cntr_flow = com_object

    @property
    def flow_capability(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FlowCapability() As CatPspIDLFlowCapability
                | 
                |     Returns or sets Flow capability of the connector.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspCntrFlow
                |          Dim ojArg1 As CatPspIDLFlowCapability
                |           ...
                |          Set ojArg1 = objThisIntf.FlowCapability

        :return: enum cat_psp_idl_flow_capability
        :rtype: int
        """

        return self.psp_cntr_flow.FlowCapability

    @flow_capability.setter
    def flow_capability(self, value: int):
        """
        :param int value:
        """

        self.psp_cntr_flow.FlowCapability = value

    @property
    def flow_reality(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FlowReality() As CatPspIDLFlowReality
                | 
                |     Returns or sets Flow reality of the connector.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspCntrFlow
                |          Dim ojArg1 As CatPspIDLFlowReality
                |           ...
                |          Set ojArg1 = objThisIntf.FlowReality

        :return: enum cat_psp_idl_flow_reality
        :rtype: int
        """

        return self.psp_cntr_flow.FlowReality

    @flow_reality.setter
    def flow_reality(self, value: int):
        """
        :param int value: enum cat_psp_idl_flow_reality
        """

        self.psp_cntr_flow.FlowReality = value

    def __repr__(self):
        return f'PSPCntrFlow(name="{self.name}")'
