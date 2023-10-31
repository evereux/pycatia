#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_grr_cntr import SchGRRCntr
from pycatia.cat_sch_platform_interfaces.sch_grr_route import SchGRRRoute
from pycatia.cat_sch_platform_interfaces.sch_grr_route_ellipse import SchGRRRouteEllipse
from pycatia.cat_sch_platform_interfaces.sch_grr_zone import SchGRRZone
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class SchGRRFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchGRRFactory
                | 
                | Factory to create graphical representations of schematic
                | objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_grr_factory = com_object

    def create_grr_cntr(self) -> SchGRRCntr:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateGRRCntr() As SchGRRCntr
                | 
                |     Create the graphical representation of a Schematic
                |     Connector.
                | 
                |     Parameters:
                | 
                |         oGRRCntr
                |             The graphical representation of the connector 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRFactory
                |          Dim objArg1 As SchGRRCntr
                |           ...
                |          Set objArg1 = objThisIntf.CreateGRRCntr

        :rtype: SchGRRCntr
        """
        return SchGRRCntr(self.sch_grr_factory.CreateGRRCntr())

    def create_grr_group(self, i_l_primitive: SchListOfObjects) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateGRRGroup(SchListOfObjects iLPrimitive) As
                | AnyObject
                | 
                |     Create the graphical representation of a Schematic Group.
                | 
                |     Parameters:
                | 
                |         iLPrimitives
                |             A list of 2D drafting detail pointers Members are CATI2DDetail
                |             interface poiners. 
                |         oGRRGroup
                |             The graphical representation of the Group 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRFactory
                |          Dim objArg1 As SchListOfObjects
                |          Dim objArg2 As AnyObject
                |           ...
                |          Set objArg2 = objThisIntf.CreateGRRGroup(objArg1)

        :param SchListOfObjects i_l_primitive:
        :rtype: AnyObject
        """
        return AnyObject(self.sch_grr_factory.CreateGRRGroup(i_l_primitive.com_object))

    def create_grr_route(self, i_l_db_line_path: tuple, o_grr_route: SchGRRRoute) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateGRRRoute(CATSafeArrayVariant iLDbLinePath,
                | SchGRRRoute oGRRRoute)
                | 
                |     Create the graphical representation of a Schematic Route.
                | 
                |     Parameters:
                | 
                |         iLDbPtPath
                |             A list of X-Y coordinates of points defining the Route. 2 doubles
                |             per point. 
                |         oGRRRoute
                |             The graphical representation of the Route 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRFactory
                |          Dim dbVar1(x) As CATSafeArrayVariant
                |          Dim objArg3 As SchGRRRoute
                |           ...
                |          objThisIntf.CreateGRRRoutedbVar1,objArg3

        :param tuple i_l_db_line_path:
        :param SchGRRRoute o_grr_route:
        :rtype: tuple
        """
        return self.sch_grr_factory.CreateGRRRoute(i_l_db_line_path, o_grr_route.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_grr_route'
        # # vba_code = """
        # # Public Function create_grr_route(sch_grr_factory)
        # #     Dim iLDbLinePath (2)
        # #     sch_grr_factory.CreateGRRRoute iLDbLinePath
        # #     create_grr_route = iLDbLinePath
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_grr_route_ellipse(self, i_db_xy_seed_pt: tuple, o_grr_route_ellipse: SchGRRRouteEllipse) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateGRRRouteEllipse(CATSafeArrayVariant iDbXYSeedPt,
                | SchGRRRouteEllipse oGRRRouteEllipse)
                | 
                |     Create the graphical representation of a Schematic Route
                |     Ellipse.
                | 
                |     Parameters:
                | 
                |         iDbXYSeedPt
                |             X-Y coordinate of the seed point for the ellipse. If NULL, the seed
                |             point will not be set. 
                |         oGRRRouteEllipse
                |             The graphical representation of the Route Ellipse 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRFactory
                |          Dim dbVar1(X) As CATSafeArrayVariant
                |          Dim objArg2 As SchGRRRouteEllipse
                |           ...
                |          objThisIntf.CreateGRRRouteEllipsedbVar1,objArg2

        :param tuple i_db_xy_seed_pt:
        :param SchGRRRouteEllipse o_grr_route_ellipse:
        :rtype: tuple
        """
        return self.sch_grr_factory.CreateGRRRouteEllipse(i_db_xy_seed_pt, o_grr_route_ellipse.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_grr_route_ellipse'
        # # vba_code = """
        # # Public Function create_grr_route_ellipse(sch_grr_factory)
        # #     Dim iDbXYSeedPt (2)
        # #     sch_grr_factory.CreateGRRRouteEllipse iDbXYSeedPt
        # #     create_grr_route_ellipse = iDbXYSeedPt
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_grr_zone(self, i_l_primitive: SchListOfObjects) -> SchGRRZone:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateGRRZone(SchListOfObjects iLPrimitive) As
                | SchGRRZone
                | 
                |     Create the graphical representation of a Schematic Zone.
                | 
                |     Parameters:
                | 
                |         iLPrimitives
                |             A list of 2D drafting object pointers defining the zone boundaries.
                |             
                |         oGRRZone
                |             The graphical representation of the Zone 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRFactory
                |          Dim objArg1 As SchListOfObjects
                |          Dim objArg2 As SchGRRZone
                |           ...
                |          Set objArg2 = objThisIntf.CreateGRRZone(objArg1)

        :param SchListOfObjects i_l_primitive:
        :rtype: SchGRRZone
        """
        return SchGRRZone(self.sch_grr_factory.CreateGRRZone(i_l_primitive.com_object))

    def __repr__(self):
        return f'SchGRRFactory(name="{self.name}")'
