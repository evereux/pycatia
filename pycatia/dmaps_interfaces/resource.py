#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.dmaps_interfaces.activities import Activities
from pycatia.dmaps_interfaces.items import Items
from pycatia.dmaps_interfaces.outputs import Outputs
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.dmaps_interfaces.resource_collection import ResourceCollection


class Resource(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Resource
                | 
                | The object that represents a resource.
                | 
                | It also allows to get the real resource object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.resource = com_object

    @property
    def children_ts_as(self) -> Activities:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ChildrenTSAs() As Activities (Read Only)
                | 
                |     This property returns the interface which manages the children TSA of the
                |     given resource/system.

        :rtype: Activities
        """

        return Activities(self.resource.ChildrenTSAs)

    @property
    def input_products(self) -> Items:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InputProducts() As Items (Read Only)
                | 
                |     This property returns the interface which manages the items or input
                |     products/components assigned to the given resource/system

        :rtype: Items
        """

        return Items(self.resource.InputProducts)

    @property
    def next_resources(self) -> 'ResourceCollection':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NextResources() As ResourceCollection (Read Only)
                | 
                |     This property returns the interface which manages the downstream product
                |     flow hierarchy on the given resource. This returns the collection of resources
                |     which are "Next" to the given resource in the resource product flow links

        :rtype: ResourceCollection
        """

        from pycatia.dmaps_interfaces.resource_collection import ResourceCollection
        return ResourceCollection(self.resource.NextResources)

    @property
    def output_products(self) -> Outputs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OutputProducts() As Outputs (Read Only)
                | 
                |     This property returns the interface which manages the output
                |     products/components of the given resource/system

        :rtype: Outputs
        """

        return Outputs(self.resource.OutputProducts)

    @property
    def previous_resources(self) -> 'ResourceCollection':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PreviousResources() As ResourceCollection (Read
                | Only)
                | 
                |     This property returns the interface which manages the upstream product flow
                |     hierarchy on the given resource. This returns the collection of resources which
                |     are "Previous" to the given resource in the resource product flow links

        :rtype: ResourceCollection
        """
        
        from pycatia.dmaps_interfaces.resource_collection import ResourceCollection
        return ResourceCollection(self.resource.PreviousResources)

    def get_object(self, i_interface_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetObject(CATBSTR iInterfaceName) As AnyObject
                | 
                |     This method returns the IDL Interface for the specified interface
                |     identifier.
                | 
                |     Parameters:
                | 
                |         iInterfaceName
                |             The name of the interface to query. 
                |         oObject
                |             The pointer to the queried interface.

        :param str i_interface_name:
        :rtype: AnyObject
        """
        return AnyObject(self.resource.GetObject(i_interface_name))

    def __repr__(self):
        return f'Resource(name="{self.name}")'
