#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchApp2DZoneFrom3DZone(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchApp2DZoneFrom3DZone
                | 
                | Manage a 2D zone that is dropped off from 3D counterpart.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_2d_zone_from_3d_zone = com_object

    def create_2d_app_zone(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Create2DAppZone() As AnyObject
                | 
                |     Create an Application Zone.
                | 
                |     Parameters:
                | 
                |         i3DZone
                |             The Bounded Zone (3D) object 
                |         oAppZone
                |             The new Application zone object created (CATISchAppZone interface
                |             pointer). 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchApp2DZoneFrom3DZone
                |          Dim objArg1 As AnyObject
                |           ...
                |          Set objArg1 = objThisIntf.Create2DAppZone

        :rtype: AnyObject
        """
        return AnyObject(self.sch_app_2d_zone_from_3d_zone.Create2DAppZone())

    def __repr__(self):
        return f'SchApp2DZoneFrom3DZone(name="{self.name}")'
