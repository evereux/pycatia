#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_plant_ship_interfaces.psp_functional import PSPFunctional
from pycatia.cat_plant_ship_interfaces.psp_spatial import PSPSpatial
from pycatia.system_interfaces.any_object import AnyObject


class PSPPhysical(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspPhysical
                | 
                | Represents the object to access Plant Ship physical object
                | information.
                | Role: To access access Plant Ship physical object information.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_physical = com_object

    def get_functional(self) -> PSPFunctional:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFunctional() As PspFunctional
                | 
                |     Returns the Function object.
                | 
                |     Returns:
                |         Functional object associated with the physical object
                |
                |     Example:
                |
                |          Dim objThisIntf As PspPhysical
                |          Dim objArg1 As PspFunctional
                |           ...
                |          Set objArg1 = objThisIntf.GetFunctional

        :rtype: PSPFunctional
        """
        return PSPFunctional(self.psp_physical.GetFunctional())

    def get_spatial(self) -> PSPSpatial:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSpatial() As PspSpatial
                | 
                |     Returns the Spatial object.
                | 
                |     Returns:
                |         Spatial object associated with the physical object
                |
                |     Example:
                |
                |          Dim objThisIntf As PspPhysical
                |          Dim objArg1 As PspSpatial
                |           ...
                |          Set objArg1 = objThisIntf.GetSpatial

        :rtype: PSPSpatial
        """
        return PSPSpatial(self.psp_physical.GetSpatial())

    def __repr__(self):
        return f'PSPPhysical(name="{self.name}")'
