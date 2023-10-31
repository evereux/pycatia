#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchGRRRouteAlternate(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchGRRRouteAlternate
                | 
                | Manage the graphical styles for alternative route graphics.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_grr_route_alternate = com_object

    def get_alternate_style(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAlternateStyle(CatSchIDLRouteAlternateGraphicStyle
                | oEGraphicStyle)
                | 
                |     Returns the graphicl style of the alternate graphic
                |     object.
                | 
                |     Parameters:
                | 
                |         oEGraphicStyle
                |             Enum describing the graphic style of the object. (see
                |             CATSchGeneralEnum.h for descriptions) 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRouteAlternate
                | 
                |           ...
                |          objThisIntf.GetAlternateStyleCatSchIDLRouteAlternateGraphicStyle_Enum

        :return: enum cat_sch_idl_route_alternate_graphic_style
        :rtype: int
        """
        return self.sch_grr_route_alternate.GetAlternateStyle()

    def __repr__(self):
        return f'SchGRRRouteAlternate(name="{self.name}")'
