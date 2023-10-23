#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.cat_sch_platform_interfaces.sch_list_of_bst_rs import SchListOfBSTRs
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.cat_sch_platform_interfaces.sch_app_connectable import SchAppConnectable
    from pycatia.cat_sch_platform_interfaces.sch_app_connection import SchAppConnection


class SchAppConnector(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppConnector
                | 
                | Manage a schematic connector.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_connector = com_object

    def app_connect(self, i_cntr_to_connect: 'SchAppConnector') -> 'SchAppConnection':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppConnect(SchAppConnector iCntrToConnect) As
                | SchAppConnection
                | 
                |     Connect to an input connector.
                | 
                |     Parameters:
                | 
                |         iCntrToConnect
                |             A schematic connector object to connect to 
                |         oConnection
                |             Connection created 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnector
                |          Dim objArg1 As SchAppConnector
                |          Dim objArg2 As SchAppConnection
                |           ...
                |          Set objArg2 = objThisIntf.AppConnect(objArg1)

        :param SchAppConnector i_cntr_to_connect:
        :rtype: SchAppConnection
        """

        from pycatia.cat_sch_platform_interfaces.sch_app_connection import SchAppConnection
        return SchAppConnection(self.sch_app_connector.AppConnect(i_cntr_to_connect.com_object))

    def app_connect_branch(self, i_cntr_to_connect: 'SchAppConnector') -> 'SchAppConnection':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppConnectBranch(SchAppConnector iCntrToConnect) As
                | SchAppConnection
                | 
                |     Connect to an input connector for Branch.
                | 
                |     Parameters:
                | 
                |         iCntrToConnect
                |             A schematic connector object to connect to 
                |         oConnection
                |             Connection created 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchAppConnector
                |          Dim objArg1 As SchAppConnector
                |          Dim objArg2 As SchAppConnection
                |           ...
                |          Set objArg2 = objThisIntf.AppConnectBranch(objArg1)

        :param SchAppConnector i_cntr_to_connect:
        :rtype: SchAppConnection
        """

        from pycatia.cat_sch_platform_interfaces.sch_app_connection import SchAppConnection
        return SchAppConnection(self.sch_app_connector.AppConnectBranch(i_cntr_to_connect.com_object))

    def app_disconnect(self, i_cntr_to_dis_connect: 'SchAppConnector') -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppDisconnect(SchAppConnector iCntrToDisConnect)
                | 
                |     Disconnect from an input connector.
                | 
                |     Parameters:
                | 
                |         iCntrToDisconnect
                |             A schematic connector object to disconnect from 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnector
                |          Dim objArg1 As SchAppConnector
                |           ...
                |          objThisIntf.AppDisconnectobjArg1

        :param SchAppConnector i_cntr_to_dis_connect:
        :rtype: None
        """
        return self.sch_app_connector.AppDisconnect(i_cntr_to_dis_connect.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_disconnect'
        # # vba_code = """
        # # Public Function app_disconnect(sch_app_connector)
        # #     Dim iCntrToDisConnect (2)
        # #     sch_app_connector.AppDisconnect iCntrToDisConnect
        # #     app_disconnect = iCntrToDisConnect
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_get_associated_connectable(self) -> 'SchAppConnectable':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppGetAssociatedConnectable() As SchAppConnectable
                | 
                |     Find the application object that owns this connector.
                | 
                |     Parameters:
                | 
                |         oConnectable
                |             An application object that the connector belongs to.
                |             
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnector
                |          Dim objArg1 As SchAppConnectable
                |           ...
                |          Set objArg1 = objThisIntf.AppGetAssociatedConnectable

        :rtype: SchAppConnectable
        """

        from pycatia.cat_sch_platform_interfaces.sch_app_connectable import SchAppConnectable
        return SchAppConnectable(self.sch_app_connector.AppGetAssociatedConnectable())

    def app_is_cntr_connected(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppIsCntrConnected(boolean oBYes)
                | 
                |     Query whether the connector has been connected.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then it is connected 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnector
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.AppIsCntrConnectedbVar1

        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_connector.AppIsCntrConnected(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_is_cntr_connected'
        # # vba_code = """
        # # Public Function app_is_cntr_connected(sch_app_connector)
        # #     Dim oBYes (2)
        # #     sch_app_connector.AppIsCntrConnected oBYes
        # #     app_is_cntr_connected = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_list_compatible_types(self) -> SchListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppListCompatibleTypes() As SchListOfBSTRs
                | 
                |     Find all the class types of connector that are compatible with this
                |     connector for connections.
                | 
                |     Parameters:
                | 
                |         oLCntrCompatClassTypes
                |             A list of all the class types of connectors that are compatible
                |             with this connector for connections. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnector
                |          Dim objArg1 As SchListOfBSTRs
                |           ...
                |          Set objArg1 = objThisIntf.AppListCompatibleTypes

        :rtype: SchListOfBSTRs
        """
        return SchListOfBSTRs(self.sch_app_connector.AppListCompatibleTypes())

    def app_list_connections(self, i_l_cntn_class_filter: SchListOfBSTRs) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppListConnections(SchListOfBSTRs iLCntnClassFilter) As
                | SchListOfObjects
                | 
                |     Find all the connections that include this connector.
                | 
                |     Parameters:
                | 
                |         oLCntnClassFilter
                |             A list of all the class types for filtering the output connection
                |             list. 
                |         oLConnections
                |             A list of connections that include this connector (members are
                |             CATISchAppConnection interface pointers). 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnector
                |          Dim objArg1 As SchListOfBSTRs
                |          Dim objArg2 As SchListOfObjects
                |           ...
                |          Set objArg2 = objThisIntf.AppListConnections(objArg1)

        :param SchListOfBSTRs i_l_cntn_class_filter:
        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_app_connector.AppListConnections(i_l_cntn_class_filter.com_object))

    def app_ok_to_no_show_connected_cntr(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToNoShowConnectedCntr(boolean oBYes)
                | 
                |     Query whether it is OK to no show the connector after it is
                |     connected.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then it is OK to no show. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnector
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.AppOKToNoShowConnectedCntrbVar1

        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_connector.AppOKToNoShowConnectedCntr(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_no_show_connected_cntr'
        # # vba_code = """
        # # Public Function app_ok_to_no_show_connected_cntr(sch_app_connector)
        # #     Dim oBYes (2)
        # #     sch_app_connector.AppOKToNoShowConnectedCntr oBYes
        # #     app_ok_to_no_show_connected_cntr = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchAppConnector(name="{self.name}")'
