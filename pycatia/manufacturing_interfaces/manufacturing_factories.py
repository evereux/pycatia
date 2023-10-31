#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingFactories(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingFactories
                | 
                | Interface to manage manufacturing factories.
                | 
                | Role: CATIAMfgManufacturingFactories has methods to manage manufacturing
                | factories.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_factories = com_object

    def get_manufacturing_resource_factory(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetManufacturingResourceFactory() As AnyObject
                | 
                |     Retrieves the manufacturing resource factory from the given
                |     object.
                | 
                |     Parameters:
                | 
                |         oResourceFactory
                |             The manufacturing resource factory.

        :rtype: AnyObject
        """
        return AnyObject(self.manufacturing_factories.GetManufacturingResourceFactory())

    def __repr__(self):
        return f'ManufacturingFactories(name="{ self.name }")'
