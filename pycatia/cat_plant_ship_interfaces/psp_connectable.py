#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_plant_ship_interfaces.psp_connector import PSPConnector
from pycatia.cat_plant_ship_interfaces.psp_list_of_bstrs import PSPListOfBSTRs
from pycatia.cat_plant_ship_interfaces.psp_list_of_objects import PSPListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class PSPConnectable(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspConnectable
                | 
                | Represents an Interface to manage object behaviors in making
                | connections.
                | Role: To specify object behaviors such as adding a connector and removing a
                | connector.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_connectable = com_object

    @property
    def connectors(self) -> PSPListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Connectors() As PspListOfObjects (Read Only)
                | 
                |     Returns a list of connectors of the object.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspConnectable
                |          Dim objArg1 As CatPspIDLDomainID
                |          Dim objArg2 As PspListOfBSTRs
                |           ...
                |          Set objArg2 = objThisIntf.Connectors

        :rtype: PSPListOfObjects
        """

        return PSPListOfObjects(self.psp_connectable.Connectors)

    @property
    def valid_connector_types(self) -> PSPListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ValidConnectorTypes() As PspListOfBSTRs (Read
                | Only)
                | 
                |     Returns a list of Valid connector types on this object.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspConnectable
                |          Dim objArg1 As PspListOfBSTRs  
                |           ...
                |          Set objArg1 = objThisIntf.ValidConnectorTypes

        :rtype: PSPListOfBSTRs
        """

        return PSPListOfBSTRs(self.psp_connectable.ValidConnectorTypes)

    def get_connector_by_name(self, iu_connector_name: str) -> PSPConnector:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetConnectorByName(CATBSTR iuConnectorName) As
                | PspConnector
                | 
                |     Retrieves a connector with the given name.
                | 
                |     Parameters:
                | 
                |         iConnectorName
                |             Connector name to look for. 
                | 
                |     Returns:
                |         Connector with given name.
                |
                |     Example:
                |
                |          Dim objThisIntf As PspConnectable
                |          Dim strVar1 As PspListOfBSTRs
                |          Dim objArg2 As PspConnector
                |           ...
                |          Set objArg2 = objThisIntf.GetConnectorByName (strVar1)

        :param str iu_connector_name:
        :rtype: PSPConnector
        """
        return PSPConnector(self.psp_connectable.GetConnectorByName(iu_connector_name))

    def list_connectables(
            self,
            iu_class_filter: PSPListOfBSTRs,
            o_l_cntbles: PSPListOfObjects,
            o_l_cntrs_on_this_obj: PSPListOfObjects,
            o_l_cntrs_on_connected: PSPListOfObjects
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListConnectables(PspListOfBSTRs iuClassFilter,
                | PspListOfObjects oLCntbles,
                | PspListOfObjects oLCntrsOnThisObj,
                | PspListOfObjects oLCntrsOnConnected)
                | 
                |     Retrieve a list of connectors of the object.
                | 
                |     Parameters:
                | 
                |         iuClassFilter
                |             Class filter list. If iuClassFilter is an empty list then it will
                |             get connectors for all the application connector types.
                |             
                |         oLCntbles
                |             a list of CATIAPspConnectable objects that connect this object
                |             
                |         oLCntrsOnThisObj
                |             a list of connectors on "this" object in the connections ( A list
                |             of CATIAPspConnector) 
                |         oLCntrsOnConnected
                |             a list of connectors on the other objects that the member of the
                |             former list is connected to (positions in oLCntrsOnThisObj and
                |             oLCntrsOnConnected corresponds to each other) ( A list of CATIAPspConnector)
                |
                |     Example:
                |
                |          Dim objThisIntf As PspConnectable
                |          Dim objArg1 As PspListOfBSTRs
                |          Dim objArg2 As PspListofObjects
                |          Dim objArg3 As PspListofObjects
                |          Dim objArg4 As PspListofObjects
                |           ...
                |          objThisIntf.ListConnectables
                |          objArg1,objArg2,objArg3,objArg4

        :param PSPListOfBSTRs iu_class_filter:
        :param PSPListOfObjects o_l_cntbles:
        :param PSPListOfObjects o_l_cntrs_on_this_obj:
        :param PSPListOfObjects o_l_cntrs_on_connected:
        :rtype: None
        """
        return self.psp_connectable.ListConnectables(
            iu_class_filter.com_object,
            o_l_cntbles.com_object,
            o_l_cntrs_on_this_obj.com_object,
            o_l_cntrs_on_connected.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_connectables'
        # # vba_code = """
        # # Public Function list_connectables(psp_connectable)
        # #     Dim iuClassFilter (2)
        # #     psp_connectable.ListConnectables iuClassFilter
        # #     list_connectables = iuClassFilter
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PSPConnectable(name="{self.name}")'
