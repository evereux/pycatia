#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.resource import Resource
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ResourceCollection(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ResourceCollection
                | 
                | Interface representing collection of Resources.
                | 
                | Role: Components that implement CATIAResourceCollection are
                | ...
                | 
                | Do not use the CATIAResourceCollection interface for such and such
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.resource_collection = com_object

    def item(self, i_index: cat_variant) -> Resource:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Resource
                | 
                |     This method gets the specified resource from the given resource collection
                |     management.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The resource identifier 
                | 
                |     Returns:
                |         oResource The resource

        :param cat_variant i_index:
        :rtype: Resource
        """
        return Resource(self.resource_collection.Item(i_index))

    def __repr__(self):
        return f'ResourceCollection(name="{self.name}")'
