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


class ManufacturingSetup2(ManufacturingActivity):
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
                |                             ManufacturingSetup2
                | 
                | A ManufacturingSetup 2 for a Manufacturing Document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_setup2 = com_object

    def create_resource_from_catalog(
            self,
            i_tool_resource_name: str,
            i_resource_type: str,
            i_catalog_path: str
    ) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateResourceFromCatalog(CATBSTR iToolResourceName,
                | CATBSTR iResourceType,
                | CATBSTR iCatalogPath) As AnyObject
                | 
                |     This method is used to create a new manufacturing resource from
                |     catalog.

        :param str i_tool_resource_name:
        :param str i_resource_type:
        :param str i_catalog_path:
        :rtype: AnyObject
        """
        return AnyObject(
            self.manufacturing_setup2.CreateResourceFromCatalog(
                i_tool_resource_name,
                i_resource_type,
                i_catalog_path
            )
        )

    def __repr__(self):
        return f'ManufacturingSetup2(name="{self.name}")'
