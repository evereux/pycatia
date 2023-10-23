#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.cat_sch_platform_interfaces.sch_grr_route import SchGRRRoute


class SchRouteSymbol(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchRouteSymbol
                | 
                | Manage a symbol placed on a route.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_route_symbol = com_object

    def flip_over_line(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub FlipOverLine()
                | 
                |     Mirror the symbol over the route segment line on which the symbol is
                |     positioned.
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchRouteSymbol
                |           ...
                |          objThisIntf.FlipOverLine

        :rtype: None
        """
        return self.sch_route_symbol.FlipOverLine()

    def flip_over_orthogonal_line(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub FlipOverOrthogonalLine()
                | 
                |     Mirror the symbol over the line orthogonal to the route segment line on
                |     which the symbol is positioned and going through the symbol's position point on
                |     that segment line.
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchRouteSymbol
                |           ...
                |          objThisIntf.FlipOverOrthogonalLine

        :rtype: None
        """
        return self.sch_route_symbol.FlipOverOrthogonalLine()

    def get_grr_route(self) -> 'SchGRRRoute':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetGRRRoute() As SchGRRRoute
                | 
                |     Get the graphical representation of a schematic route that owns this
                |     symbol.
                | 
                |     Parameters:
                | 
                |         oGRRRoute
                |             The graphical representation that owns this symbol.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchRouteSymbol
                |          Dim objArg1 As SchGRRRoute
                |           ...
                |          Set objArg1 = objThisIntf.GetGRRRoute

        :rtype: SchGRRRoute
        """

        from pycatia.cat_sch_platform_interfaces.sch_grr_route import SchGRRRoute
        return SchGRRRoute(self.sch_route_symbol.GetGRRRoute())

    def get_position(self, o_seg_num: int, o_seg_parm: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetPosition(long oSegNum,
                | double oSegParm)
                | 
                |     Get the symbol's position on the route that own it.
                | 
                |     Parameters:
                | 
                |         oSegNum
                |             The route segment number. 
                |         oSegParm
                |             The parameter along the segment. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchRouteSymbol
                |          Dim intVar1 As Integer
                |          Dim dbVar2 As Double
                |           ...
                |          objThisIntf.GetPositionintVar1,dbVar2

        :param int o_seg_num:
        :param float o_seg_parm:
        :rtype: None
        """
        return self.sch_route_symbol.GetPosition(o_seg_num, o_seg_parm)

    def scale(self, i_db_scale_factor: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Scale(double iDbScaleFactor)
                | 
                |     Scale the symbol.
                | 
                |     Parameters:
                | 
                |         iDbScaleFactor
                |             The scale factor to scale the symbol by. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchRouteSymbol
                |          Dim dbVar1 As Double
                |           ...
                |          objThisIntf.ScaledbVar1

        :param float i_db_scale_factor:
        :rtype: None
        """
        return self.sch_route_symbol.Scale(i_db_scale_factor)

    def set_position(self, i_seg_num: int, i_seg_parm: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPosition(long iSegNum,
                | double iSegParm)
                | 
                |     Set the symbol's position on the route that own it.
                | 
                |     Parameters:
                | 
                |         iSegNum
                |             The route segment number (<= number of segments in the route).
                |             
                |         iSegParm
                |             The parameter along the segment (0.<=iSegParm<=1.).
                |
                |     Example:
                |
                |          Dim objThisIntf As SchRouteSymbol
                |          Dim intVar1 As Integer
                |          Dim dbVar2 As Double
                |           ...
                |          objThisIntf.SetPositionintVar1,dbVar2

        :param int i_seg_num:
        :param float i_seg_parm:
        :rtype: None
        """
        return self.sch_route_symbol.SetPosition(i_seg_num, i_seg_parm)

    def __repr__(self):
        return f'SchRouteSymbol(name="{self.name}")'
