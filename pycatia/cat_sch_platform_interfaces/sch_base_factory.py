#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_app_connector import SchAppConnector
from pycatia.cat_sch_platform_interfaces.sch_comp_group_ext import SchCompGroupExt
from pycatia.cat_sch_platform_interfaces.sch_component import SchComponent
from pycatia.cat_sch_platform_interfaces.sch_grr_comp import SchGRRComp
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.cat_sch_platform_interfaces.sch_route import SchRoute
from pycatia.cat_sch_platform_interfaces.sch_zone import SchZone
from pycatia.system_interfaces.any_object import AnyObject


class SchBaseFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchBaseFactory
                | 
                | Factory to create basic schematic objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_base_factory = com_object

    def create_network(self, i_l_cntbls: SchListOfObjects, i_lgr_rs: SchListOfObjects) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateNetwork(SchListOfObjects iLCntbls,
                | SchListOfObjects iLGRRs) As SchListOfObjects
                | 
                |     Create schematic networks for query. These are volatile objects and will
                |     not be saved in the model.
                | 
                |     Parameters:
                | 
                |         iLCntbl
                |             A list of related objects that belong to the network
                |             (CATISchAppConnectable pointers). These objects do not need to be connected.
                |             This method will do the analysis and returns the network(s) containing these
                |             objects. 
                |         iLCntbl
                |             A list of graphical images interface (CATISchGRR) pointers. Each
                |             member corresponds to the members in iLCntbl. 
                |         oNetwork
                |             [out, IUnknown#Release] Pointer to the network analysis interface
                |             pointers. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchBaseFactory
                |          Dim objArg1 As SchListOfObjects
                |          Dim objArg2 As SchListOfObjects
                |          Dim objArg3 As SchListOfObjects
                |           ...
                |          Set objArg3 = objThisIntf.CreateNetwork(objArg1,objArg2)

        :param SchListOfObjects i_l_cntbls:
        :param SchListOfObjects i_lgr_rs:
        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_base_factory.CreateNetwork(i_l_cntbls.com_object, i_lgr_rs.com_object))

    def create_route_and_connect_to_objects(
            self,
            i_app_route: AnyObject,
            i_cntr_comp_from: SchAppConnector,
            i_cntr_comp_to: SchAppConnector,
            i_grr_comp_from: SchGRRComp,
            i_grr_comp_to: SchGRRComp,
            i_l_db2_pt_path: tuple,
            i_e_route_mode: int,
            o_sch_route: SchRoute
    ) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateRouteAndConnectToObjects(AnyObject iAppRoute,
                | SchAppConnector iCntrCompFrom,
                | SchAppConnector iCntrCompTo,
                | SchGRRComp iGRRCompFrom,
                | SchGRRComp iGRRCompTo,
                | CATSafeArrayVariant iLDb2PtPath,
                | CatSchIDLRouteMode iERouteMode,
                | SchRoute oSchRoute)
                | 
                |     Create a route and connect its extremity connectors to input
                |     objects.
                | 
                |     Parameters:
                | 
                |         iAppRoute
                |             Application route (at least a feature) 
                |         iCntrCompFrom
                |             Pointer to component connector to connect starting end of the route
                |             to If NULL, no connection is made at this end. 
                |         iCntrCompTo
                |             Pointer to component connector to connect end of the route to If
                |             NULL, no connection is made at this end. 
                |         iGRRCompFrom
                |             Pointer to first component graphical image, if NULL, the PRIMARY
                |             image associated with component will be used 
                |         iGRRCompTo
                |             Pointer to second component graphical image, if NULL, the PRIMARY
                |             image associated with component will be used 
                |         iLDb2PtPath
                |             A list of X-Y coordinates of points to be used for the route image.
                |             2 doubles per point. Not used if iERouteMode=SchRouteMode_AroundObject input a
                |             NULL for this case 
                |         iERouteMode
                |             Route mode to use. Only used when iLDb2PtPath is NULL.
                |             
                |         oSchRoute
                |             Pointer to the new route 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchBaseFactory
                |          Dim objArg1 As AnyObject
                |          Dim objArg2 As SchAppConnector
                |          Dim objArg3 As SchAppConnector
                |          Dim objArg4 As SchGRRComp
                |          Dim objArg5 As SchGRRComp
                |          Dim dbVar6(x) As CATSafeArrayVariant
                | 
                |          Dim objArg9 As SchRoute
                |           ...
                |         objThisIntf.CreateRouteAndConnectToObjectsobjArg1,objArg2,objArg3,objArg4,objArg5,dbVar6,CatSchIDLRouteMode_Enum,objArg9

        :param AnyObject i_app_route:
        :param SchAppConnector i_cntr_comp_from:
        :param SchAppConnector i_cntr_comp_to:
        :param SchGRRComp i_grr_comp_from:
        :param SchGRRComp i_grr_comp_to:
        :param tuple i_l_db2_pt_path:
        :param int i_e_route_mode: enum cat_sch_idl_route_mode
        :param SchRoute o_sch_route:
        :rtype: tuple
        """
        return self.sch_base_factory.CreateRouteAndConnectToObjects(
            i_app_route.com_object,
            i_cntr_comp_from.com_object,
            i_cntr_comp_to.com_object,
            i_grr_comp_from.com_object,
            i_grr_comp_to.com_object,
            i_l_db2_pt_path,
            i_e_route_mode, o_sch_route.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_route_and_connect_to_objects'
        # # vba_code = """
        # # Public Function create_route_and_connect_to_objects(sch_base_factory)
        # #     Dim iAppRoute (2)
        # #     sch_base_factory.CreateRouteAndConnectToObjects iAppRoute
        # #     create_route_and_connect_to_objects = iAppRoute
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_sch_comp_group(
            self,
            i_app_group: AnyObject,
            i_lgrr: SchListOfObjects,
            i_l_member: SchListOfObjects
    ) -> SchCompGroupExt:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateSchCompGroup(AnyObject iAppGroup,
                | SchListOfObjects iLGRR,
                | SchListOfObjects iLMember) As SchCompGroupExt
                | 
                |     Create a Schematic Component Group object.
                | 
                |     Parameters:
                | 
                |         iAppGroup
                |             Application group object (at least a feature) Optional, it could be
                |             NULL. If NULL, one will be created by the platform
                |             
                |         iLGRR
                |             A list of graphical representation. Optional, it could be NULL.
                |             
                |         iLMembers
                |             A list of initial members. Optional, it could be NULL.
                |             
                |         oSchGroup
                |             Pointer to the new group. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchBaseFactory
                |          Dim objArg1 As AnyObject
                |          Dim objArg2 As SchListOfObjects
                |          Dim objArg3 As SchListOfObjects
                |          Dim objArg4 As SchCompGroupExt
                |           ...
                |          Set objArg4 = objThisIntf.CreateSchCompGroup(objArg1,objArg2,objArg3)

        :param AnyObject i_app_group:
        :param SchListOfObjects i_lgrr:
        :param SchListOfObjects i_l_member:
        :rtype: SchCompGroupExt
        """
        return SchCompGroupExt(
            self.sch_base_factory.CreateSchCompGroup(
                i_app_group.com_object,
                i_lgrr.com_object,
                i_l_member.com_object
            )
        )

    def create_sch_component(
            self,
            i_app_component_ref: AnyObject,
            i_lgrr: SchListOfObjects
    ) -> SchComponent:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateSchComponent(AnyObject iAppComponentRef,
                | SchListOfObjects iLGRR) As SchComponent
                | 
                |     Create a Schematic Component reference.
                | 
                |     Parameters:
                | 
                |         iAppComponentRef
                |             Application component reference (at least a feature)
                |             
                |         iLGRR
                |             A list of graphical representations. 
                |         oSchComp
                |             Pointer to the new component. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchBaseFactory
                |          Dim objArg1 As AnyObject
                |          Dim objArg2 As SchListOfObjects
                |          Dim objArg3 As SchComponent
                |           ...
                |          Set objArg3 = objThisIntf.CreateSchComponent(objArg1,objArg2)

        :param AnyObject i_app_component_ref:
        :param SchListOfObjects i_lgrr:
        :rtype: SchComponent
        """
        return SchComponent(self.sch_base_factory.CreateSchComponent(i_app_component_ref.com_object, i_lgrr.com_object))

    def create_sch_route_by_points(self, i_app_route: AnyObject, i_l_db_pt: tuple, o_sch_route: SchRoute) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateSchRouteByPoints(AnyObject iAppRoute,
                | CATSafeArrayVariant iLDbPt,
                | SchRoute oSchRoute)
                | 
                |     Create a Schematic Route object with a list of points.
                | 
                |     Parameters:
                | 
                |         iAppRoute
                |             Application route (at least a feature) 
                |         iLDbPt
                |             A list of X-Y coordinates of points. 2 doubles per point.
                |             
                |         oSchRoute
                |             Pointer to the new route 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchBaseFactory
                |          Dim objArg1 As AnyObject
                |          Dim dbVar2(x) As CATSafeArrayVariant
                |          Dim objArg4 As SchRoute
                |           ...
                |         objThisIntf.CreateSchRouteByPointsobjArg1,dbVar2,objArg4

        :param AnyObject i_app_route:
        :param tuple i_l_db_pt:
        :param SchRoute o_sch_route:
        :rtype: tuple
        """
        return self.sch_base_factory.CreateSchRouteByPoints(i_app_route.com_object, i_l_db_pt, o_sch_route.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_sch_route_by_points'
        # # vba_code = """
        # # Public Function create_sch_route_by_points(sch_base_factory)
        # #     Dim iAppRoute (2)
        # #     sch_base_factory.CreateSchRouteByPoints iAppRoute
        # #     create_sch_route_by_points = iAppRoute
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_sch_route_by_prim(self, i_app_route: AnyObject, i_lgrr: SchListOfObjects) -> SchRoute:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateSchRouteByPrim(AnyObject iAppRoute,
                | SchListOfObjects iLGRR) As SchRoute
                | 
                |     Create a Schematic Route object with primitives.
                | 
                |     Parameters:
                | 
                |         iAppRoute
                |             Application route (at least a feature) 
                |         iLGRR
                |             A list of graphical primitives. pointer). 
                |         oSchRoute
                |             Pointer to the new route 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchBaseFactory
                |          Dim objArg1 As AnyObject
                |          Dim objArg2 As SchListOfObjects
                |          Dim objArg3 As SchRoute
                |           ...
                |          Set objArg3 = objThisIntf.CreateSchRouteByPrim(objArg1,objArg2)

        :param AnyObject i_app_route:
        :param SchListOfObjects i_lgrr:
        :rtype: SchRoute
        """
        return SchRoute(self.sch_base_factory.CreateSchRouteByPrim(i_app_route.com_object, i_lgrr.com_object))

    def create_sch_zone(self, i_app_zone: AnyObject, i_lgrr: SchListOfObjects) -> SchZone:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateSchZone(AnyObject iAppZone,
                | SchListOfObjects iLGRR) As SchZone
                | 
                |     Create a Schematic Zone object.
                | 
                |     Parameters:
                | 
                |         iAppZone
                |             Application zone object (at least a feature) 
                |         iLGRR
                |             A list of graphical representation. 
                |         oSchZone
                |             Pointer to the new zone. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchBaseFactory
                |          Dim objArg1 As AnyObject
                |          Dim objArg2 As SchListOfObjects
                |          Dim objArg3 As SchZone
                |           ...
                |          Set objArg3 = objThisIntf.CreateSchZone(objArg1,objArg2)

        :param AnyObject i_app_zone:
        :param SchListOfObjects i_lgrr:
        :rtype: SchZone
        """
        return SchZone(self.sch_base_factory.CreateSchZone(i_app_zone.com_object, i_lgrr.com_object))

    def delete_object(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub DeleteObject(AnyObject iObject)
                | 
                |     Delete a schematic object.
                | 
                |     Parameters:
                | 
                |         iObject
                |             interface pointer to the object to be deleted 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchBaseFactory
                |          Dim objArg1 As AnyObject
                |           ...
                |          objThisIntf.DeleteObjectobjArg1

        :param AnyObject i_object:
        :rtype: None
        """
        return self.sch_base_factory.DeleteObject(i_object.com_object)

    def __repr__(self):
        return f'SchBaseFactory(name="{self.name}")'
