#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_list_of_doubles import SchListOfDoubles
from pycatia.system_interfaces.any_object import AnyObject


class SchGRRRouteEllipse(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchGRRRouteEllipse
                | 
                | Manage the graphical representation of a schematic route.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_grr_route_ellipse = com_object

    def get_seed_point(self, o_db2_xy: SchListOfDoubles) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetSeedPoint(SchListOfDoubles oDb2XY)
                | 
                |     Get the seed point of the route graphic ellipse.
                | 
                |     Parameters:
                | 
                |         oDb2XY
                |             X-Y coordinates of the seed point for the ellipse.
                |             
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRouteEllipse
                |          Dim objArg1 As SchListOfDoubles
                |           ...
                |          objThisIntf.GetSeedPointobjArg1

        :param SchListOfDoubles o_db2_xy:
        :return: None
        :rtype: None
        """
        return self.sch_grr_route_ellipse.GetSeedPoint(o_db2_xy.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_seed_point'
        # # vba_code = """
        # # Public Function get_seed_point(sch_grr_route_ellipse)
        # #     Dim oDb2XY (2)
        # #     sch_grr_route_ellipse.GetSeedPoint oDb2XY
        # #     get_seed_point = oDb2XY
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def has_seed_point(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub HasSeedPoint(boolean oBYes)
                | 
                |     Check to see if the Seed point has been set.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             TRUE if the seed point has been initialized. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRouteEllipse
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.HasSeedPointbVar1

        :param bool o_b_yes:
        :return: None
        :rtype: None
        """
        return self.sch_grr_route_ellipse.HasSeedPoint(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'has_seed_point'
        # # vba_code = """
        # # Public Function has_seed_point(sch_grr_route_ellipse)
        # #     Dim oBYes (2)
        # #     sch_grr_route_ellipse.HasSeedPoint oBYes
        # #     has_seed_point = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_seed_point(self, i_db2_xy: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSeedPoint(CATSafeArrayVariant iDb2XY)
                | 
                |     Set the seed point of the route graphic ellipse.
                | 
                |     Parameters:
                | 
                |         iDb2EndPt
                |             X-Y coordinates of the seed point for the ellipse.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRouteEllipse
                |          Dim dbVar1(2) As CATSafeArrayVariant
                |           ...
                |          objThisIntf.SetSeedPointdbVar1

        :param tuple i_db2_xy:
        :return: tuple
        :rtype: tuple
        """
        return self.sch_grr_route_ellipse.SetSeedPoint(i_db2_xy)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_seed_point'
        # # vba_code = """
        # # Public Function set_seed_point(sch_grr_route_ellipse)
        # #     Dim iDb2XY (2)
        # #     sch_grr_route_ellipse.SetSeedPoint iDb2XY
        # #     set_seed_point = iDb2XY
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchGRRRouteEllipse(name="{self.name}")'