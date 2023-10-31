#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchGRRRoute2(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchGRRRoute2
                | 
                | Manage the graphical representation of a schematic route.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_grr_route2 = com_object

    def get_reshape_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetReshapeMode(CatSchIDLGRRRouteReshapeMode
                | oReshapeMode)
                | 
                |     Get the reshape mode.
                | 
                |     Parameters:
                | 
                |         oReshapeMode
                |             Whether or not the route shape is fixed for the purpose of reshaping the route.
                |             = SchFixedShapeOff : no restriction on how to reshape the route.
                |             = SchFixedShapeOn : reshape only the route's extremity (the segment directly connected to
                |             the object that's being moved).
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute2
                | 
                |           ...
                |          objThisIntf.GetReshapeModeCatSchIDLGRRRouteReshapeMode_Enum

        :return: enum cat_sch_idlgrr_route_reshape_mode
        :rtype: None
        """
        return self.sch_grr_route2.GetReshapeMode()

    def set_reshape_mode(self, i_reshape_mode: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetReshapeMode(CatSchIDLGRRRouteReshapeMode
                | iReshapeMode)
                | 
                |     Set the reshape mode.
                | 
                |     Parameters:
                | 
                |         iReshapeMode
                |             Whether or not the route shape is fixed for the purpose of reshaping the route.
                |             = SchFixedShapeOff : no restriction on how to reshape the route.
                |             = SchFixedShapeOn : reshape only the route's extremity (the segment directly connected
                |               to the object that's being moved).
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute2
                | 
                |           ...
                |          objThisIntf.SetReshapeModeCatSchIDLGRRRouteReshapeMode_Enum

        :param int i_reshape_mode: enum cat_sch_idlgrr_route_reshape_mode
        :rtype: None
        """
        return self.sch_grr_route2.SetReshapeMode(i_reshape_mode)

    def __repr__(self):
        return f'SchGRRRoute2(name="{self.name}")'
