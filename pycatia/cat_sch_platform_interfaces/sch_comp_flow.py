#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_internal_flow import SchInternalFlow
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class SchCompFlow(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchCompFlow
                | 
                | Manage the internal flow of a schematic component.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_comp_flow = com_object

    def add_internal_flow(self, i_l_flow_cntrs: SchListOfObjects) -> SchInternalFlow:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddInternalFlow(SchListOfObjects iLFlowCntrs) As
                | SchInternalFlow
                | 
                |     Add an internal flow to a component.
                | 
                |     Parameters:
                | 
                |         iLFlowCntrs
                |             List of connectors (2) to be connected by the flow. (members should
                |             be CATISchAppConnector interface pointer) 
                |         oInternalFlowAdded
                |             Internal flow object added/created (CATISchInternalFlow interface
                |             pointer). 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchCompFlow
                |          Dim objArg1 As SchListOfObjects
                |          Dim objArg2 As SchInternalFlow
                |           ...
                |          Set objArg2 = objThisIntf.AddInternalFlow(objArg1)

        :param SchListOfObjects i_l_flow_cntrs:
        :rtype: SchInternalFlow
        """
        return SchInternalFlow(self.sch_comp_flow.AddInternalFlow(i_l_flow_cntrs.com_object))

    def add_internal_flow_specify_grr(
            self,
            i_l_flow_cntrs: SchListOfObjects,
            i_l_owner_grr: SchListOfObjects
    ) -> SchInternalFlow:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddInternalFlowSpecifyGRR(SchListOfObjects
                | iLFlowCntrs,
                | SchListOfObjects iLOwnerGRR) As SchInternalFlow
                | 
                |     Add an internal flow to a component. Specifying which graphical images the
                |     connector graphics are on.
                | 
                |     Parameters:
                | 
                |         iLFlowCntrs
                |             List of connectors (2) to be connected by the flow. (members should
                |             be CATISchAppConnector interface pointer) 
                |         iLOwnerImages
                |             List of CATISchGRRComp interface pointers 
                |         oInternalFlowAdded
                |             Internal flow object added/created (CATISchInternalFlow interface
                |             pointer). 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchCompFlow
                |          Dim objArg1 As SchListOfObjects
                |          Dim objArg2 As SchListOfObjects
                |          Dim objArg3 As SchInternalFlow
                |           ...
                |          Set objArg3 = objThisIntf.AddInternalFlowSpecifyGRR(objArg1,objArg2)

        :param SchListOfObjects i_l_flow_cntrs:
        :param SchListOfObjects i_l_owner_grr:
        :rtype: SchInternalFlow
        """
        return SchInternalFlow(
            self.sch_comp_flow.AddInternalFlowSpecifyGRR(
                i_l_flow_cntrs.com_object,
                i_l_owner_grr.com_object
            )
        )

    def list_internal_flows(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListInternalFlows() As SchListOfObjects
                | 
                |     List all internal flow objects of a component.
                | 
                |     Parameters:
                | 
                |         oLInternalFlow
                |             A list of internal flow objects (members are CATISchInternalFlow
                |             interface pointers). 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchCompFlow
                |          Dim objArg1 As SchListOfObjects
                |           ...
                |          Set objArg1 = objThisIntf.ListInternalFlows

        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_comp_flow.ListInternalFlows())

    def remove_internal_flow(self, i_internal_flow_to_remove: SchInternalFlow) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveInternalFlow(SchInternalFlow
                | iInternalFlowToRemove)
                | 
                |     Remove an internal flow from a component.
                | 
                |     Parameters:
                | 
                |         iInternalFlowToRemove
                |             Internal flow object to be removed. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchCompFlow
                |          Dim objArg1 As SchInternalFlow
                |           ...
                |          objThisIntf.RemoveInternalFlowobjArg1

        :param SchInternalFlow i_internal_flow_to_remove:
        :rtype: None
        """
        return self.sch_comp_flow.RemoveInternalFlow(i_internal_flow_to_remove.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_internal_flow'
        # # vba_code = """
        # # Public Function remove_internal_flow(sch_comp_flow)
        # #     Dim iInternalFlowToRemove (2)
        # #     sch_comp_flow.RemoveInternalFlow iInternalFlowToRemove
        # #     remove_internal_flow = iInternalFlowToRemove
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchCompFlow(name="{self.name}")'
