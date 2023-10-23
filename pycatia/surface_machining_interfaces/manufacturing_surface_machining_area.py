#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_machinable_area import ManufacturingMachinableArea
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingSurfaceMachiningArea(ManufacturingMachinableArea):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    ManufacturingInterfaces.ManufacturingFeature
                |                        ManufacturingInterfaces.ManufacturingMachinableFeature
                |                            ManufacturingInterfaces.ManufacturingMachinableArea
                |                                ManufacturingSurfaceMachiningArea
                | 
                | Represents the Manufacturing Surface Machining Area.
                | Role: Allows you to associate NCGeometries with a Machining
                | Area.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_surface_machining_area = com_object

    def remove_nc_geometry(self, i_geometry_type: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveNCGeometry(CATBSTR iGeometryType)
                | 
                |     Removes all the NCGeometry of a specified type linked to a Manufacturing
                |     Surface Machining Area.
                | 
                |     Parameters:
                | 
                |         iGeometryType
                |             Legal values: iGeometryType can be
                | 
                |             GuidingElements
                |                 to remove the limiting contour 
                |             Parts
                |                 to remove the part to machine 
                |             Checks
                |                 to remove the check elements 
                | 
                | 
                |         Example: The following example removes the part of the manufacturing
                |         surface machining area CurrentSMA
                | 
                |          Call CurrentSMA.RemoveNCGeometry("Parts")

        :param str i_geometry_type:
        :rtype: None
        """
        return self.manufacturing_surface_machining_area.RemoveNCGeometry(i_geometry_type)

    def set_nc_geometry(self, i_geometry_type: str, i_nc_geometry: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetNCGeometry(CATBSTR iGeometryType,
                | AnyObject iNCGeometry)
                | 
                |     Sets a NCGeometry of a specified type to a Manufacturing Surface Machining
                |     Area.
                | 
                |     Parameters:
                | 
                |         iGeometryType
                |             Legal values: iGeometryType can be
                | 
                |             GuidingElements
                |                 to set the limiting contour 
                |             Parts
                |                 to set the part to machine 
                |             Checks
                |                 to set a check element 
                | 
                |         iNCGeometry
                |             The NCGeometry to be set. 
                | 
                | 
                |         Example: The following example sets the NCGeometry NCGeomPart to the
                |         manufacturing surface machining area CurrentSMA
                | 
                |          Call CurrentSMA.SetNCGeometry("Parts",NCGeomPart)

        :param str i_geometry_type:
        :param AnyObject i_nc_geometry:
        :rtype: None
        """
        return self.manufacturing_surface_machining_area.SetNCGeometry(i_geometry_type, i_nc_geometry.com_object)

    def __repr__(self):
        return f'ManufacturingSurfaceMachiningArea(name="{self.name}")'
