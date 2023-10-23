#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_app_route import SchAppRoute
from pycatia.system_interfaces.any_object import AnyObject


class SchAppObjectFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppObjectFactory
                | 
                | Application factory to create application objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_object_factory = com_object

    def app_create_comp_ref(self, i_app_comp_class_type: str, o_app_comp: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppCreateCompRef(CATBSTR iAppCompClassType,
                | AnyObject oAppComp)
                | 
                |     Create an Application Component reference.
                | 
                |     Parameters:
                | 
                |         iAppCompClassType
                |             Class type of the Application Component reference.
                |             
                |         oAppComp
                |             The new Application Component object created (CATISchAppComponent
                |             interface pointer). 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppObjectFactory
                |          Dim strVar1 As String
                |          Dim objArg2 As AnyObject
                |           ...
                |          objThisIntf.AppCreateCompRefstrVar1,objArg2

        :param str i_app_comp_class_type:
        :param AnyObject o_app_comp:
        :rtype: None
        """
        return self.sch_app_object_factory.AppCreateCompRef(i_app_comp_class_type, o_app_comp.com_object)

    def app_create_connection(self, i_app_cntn_class_type: str, o_app_connection: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppCreateConnection(CATBSTR iAppCntnClassType,
                | AnyObject oAppConnection)
                | 
                |     Create an Application Connection object.
                | 
                |     Parameters:
                | 
                |         iAppCntnClassType
                |             Class type of the Application Connection object. 
                |         oAppConnection
                |             The new Application Connection object created (CATISchAppConnection
                |             interface pointer). 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppObjectFactory
                |          Dim strVar1 As String
                |          Dim objArg2 As AnyObject
                |           ...
                |          objThisIntf.AppCreateConnectionstrVar1,objArg2

        :param str i_app_cntn_class_type:
        :param AnyObject o_app_connection:
        :rtype: None
        """
        return self.sch_app_object_factory.AppCreateConnection(i_app_cntn_class_type, o_app_connection.com_object)

    def app_create_group(self, i_app_group_class_type: str, o_app_group: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppCreateGroup(CATBSTR iAppGroupClassType,
                | AnyObject oAppGroup)
                | 
                |     Create an Application Group object.
                | 
                |     Parameters:
                | 
                |         iAppGroupClassType
                |             Class type of the Application Group object. 
                |         oAppGroup
                |             The new Application Group object created (CATISchAppGroup interface
                |             pointer). 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppObjectFactory
                |          Dim strVar1 As String
                |          Dim objArg2 As AnyObject
                |           ...
                |          objThisIntf.AppCreateGroupstrVar1,objArg2

        :param str i_app_group_class_type:
        :param AnyObject o_app_group:
        :rtype: None
        """
        return self.sch_app_object_factory.AppCreateGroup(i_app_group_class_type, o_app_group.com_object)

    def app_create_route(self, i_app_route_class_type: str, o_app_route: AnyObject, i_log_line_id: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppCreateRoute(CATBSTR iAppRouteClassType,
                | AnyObject oAppRoute,
                | CATBSTR iLogLineID)
                | 
                |     Create an Application Route object.
                | 
                |     Parameters:
                | 
                |         iAppRouteClassType
                |             Class type of the Application Route object. 
                |         oAppRoute
                |             The new Application Route object created (CATISchAppRoute interface
                |             pointer). 
                |         iLogLineID
                |             The logical line ID that will contain the new route. This is an
                |             optional input. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppObjectFactory
                |          Dim strVar1 As String
                |          Dim objArg2 As AnyObject
                |          Dim strVar3 As String
                |           ...
                |          objThisIntf.AppCreateRoutestrVar1,objArg2,strVar3

        :param str i_app_route_class_type:
        :param AnyObject o_app_route:
        :param str i_log_line_id:
        :rtype: None
        """
        return self.sch_app_object_factory.AppCreateRoute(i_app_route_class_type, o_app_route.com_object, i_log_line_id)

    def app_create_route_from_ref(
            self,
            i_route_reference: SchAppRoute,
            o_app_route: AnyObject,
            i_log_line_id: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppCreateRouteFromRef(SchAppRoute iRouteReference,
                | AnyObject oAppRoute,
                | CATBSTR iLogLineID)
                | 
                |     Create an Application Route object with a specific
                |     reference.
                | 
                |     Parameters:
                | 
                |         iAppRouteRef
                |             Route reference to creaet the output route from 
                |         oAppRoute
                |             The new Application Route object created (CATISchAppRoute interface
                |             pointer). 
                |         iLogLineID
                |             The logical line ID that will contain the new route. This is an
                |             optional input. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppObjectFactory
                |          Dim objArg1 As SchAppRoute
                |          Dim objArg2 As AnyObject
                |          Dim strVar3 As String
                |           ...
                |         objThisIntf.AppCreateRouteFromRefobjArg1,objArg2,strVar3

        :param SchAppRoute i_route_reference:
        :param AnyObject o_app_route:
        :param str i_log_line_id:
        :rtype: None
        """
        return self.sch_app_object_factory.AppCreateRouteFromRef(
            i_route_reference.com_object,
            o_app_route.com_object,
            i_log_line_id
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_create_route_from_ref'
        # # vba_code = """
        # # Public Function app_create_route_from_ref(sch_app_object_factory)
        # #     Dim iRouteReference (2)
        # #     sch_app_object_factory.AppCreateRouteFromRef iRouteReference
        # #     app_create_route_from_ref = iRouteReference
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_create_zone(self, i_app_zone_class_type: str, o_app_zone: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppCreateZone(CATBSTR iAppZoneClassType,
                | AnyObject oAppZone)
                | 
                |     Create an Application Zone object.
                | 
                |     Parameters:
                | 
                |         iAppZoneClassType
                |             Class type of the Application Zone object. 
                |         oAppZone
                |             The new Application Zone object created (CATISchAppZone interface
                |             pointer). 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppObjectFactory
                |          Dim strVar1 As String
                |          Dim objArg2 As AnyObject
                |           ...
                |          objThisIntf.AppCreateZonestrVar1,objArg2

        :param str i_app_zone_class_type:
        :param AnyObject o_app_zone:
        :rtype: None
        """
        return self.sch_app_object_factory.AppCreateZone(i_app_zone_class_type, o_app_zone.com_object)

    def __repr__(self):
        return f'SchAppObjectFactory(name="{self.name}")'
