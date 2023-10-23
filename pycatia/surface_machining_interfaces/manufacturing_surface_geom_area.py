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


class ManufacturingSurfaceGeomArea(ManufacturingMachinableArea):
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
                |                                 ManufacturingSurfaceGeomArea
                | 
                | Represents the Manufacturing Surface NCGeometry.
                | Role: Allows you to associate geometries with a NCGeometry.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_surface_geom_area = com_object

    def remove_all_geometry(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveAllGeometry()
                | 
                |     Removes all the geometry linked to a Manufacturing Surface NCGeometry
                |     feature.
                | 
                | 
                |     Example: The following example removes the geometry of the manufacturing
                |     surface NCGeometry feature CurrentNCGeomArea
                | 
                |      Call CurrentNCGeomArea.RemoveAllGeometry()

        :rtype: None
        """
        return self.manufacturing_surface_geom_area.RemoveAllGeometry()

    def set_geometry(self, i_reference: AnyObject, i_product: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGeometry(AnyObject iReference,
                | AnyObject iProduct)
                | 
                |     Sets a geometry of a Manufacturing Surface NCGeometry
                |     feature.
                | 
                |     Parameters:
                | 
                |         iReference
                |             The geometry to be set. 
                |         iProduct
                |             The product containing the geometry to be set. 
                |
                |         Example: The following example sets a geometry Geometry1 to the
                |         manufacturing surface NCGeometry feature
                |         CurrentNCGeomArea
                | 
                |          Call
                |          CurrentNCGeomArea.SetGeometry(Geometry1,PartMachined)

        :param AnyObject i_reference:
        :param AnyObject i_product:
        :rtype: None
        """
        return self.manufacturing_surface_geom_area.SetGeometry(i_reference.com_object, i_product.com_object)

    def __repr__(self):
        return f'ManufacturingSurfaceGeomArea(name="{self.name}")'
