#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_activity import ManufacturingActivity
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingSetup3(ManufacturingActivity):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMAPSInterfaces.Activity
                |                        ManufacturingInterfaces.ManufacturingActivity
                |                             ManufacturingSetup3
                | 
                | A ManufacturingSetup 3 for a Manufacturing Document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_setup3 = com_object

    def add_fixture(self, i_geometry: AnyObject, i_product: AnyObject, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddFixture(AnyObject iGeometry,
                | AnyObject iProduct,
                | short iPosition)
                | 
                |     Add Fixture to part operation
                | 
                |     Parameters:
                | 
                |         iGeometry
                |             Geometry to assign 
                |         iProduct
                |             Product containing the geometry to assign. 
                |         iPosition
                |             Position of the geometry in the list (0 to append at the end of the
                |             list).

        :param AnyObject i_geometry:
        :param AnyObject i_product:
        :param int i_position:
        :rtype: None
        """
        return self.manufacturing_setup3.AddFixture(i_geometry.com_object, i_product.com_object, i_position)

    def __repr__(self):
        return f'ManufacturingSetup3(name="{self.name}")'
