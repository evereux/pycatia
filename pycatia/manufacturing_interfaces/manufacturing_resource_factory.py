#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingResourceFactory(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingResourceFactory
                | 
                | Interface to create manufacturing resources.
                | Role: This interface offers services to create manufacturing
                | resources
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_resource_factory = com_object

    def create_resource(self, i_type: str, i_add_list: bool) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateResource(CATBSTR iType,
                | boolean iAddList) As AnyObject
                | 
                |     This method is used to create a new manufacturing
                |     resource.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of the resource to create. 
                |         iAddList
                |             Flag to add the resource into the resource List. 
                |         oResource
                |             Handler on the newly created resource of given type.
                |             
                | 
                |     See also:
                |         DELIMAMfgResource

        :param str i_type:
        :param bool i_add_list:
        :rtype: AnyObject
        """
        return AnyObject(self.manufacturing_resource_factory.CreateResource(i_type, i_add_list))

    def __repr__(self):
        return f'ManufacturingResourceFactory(name="{ self.name }")'
