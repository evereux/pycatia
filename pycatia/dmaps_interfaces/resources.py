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


class Resources(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Resources
                | 
                | The collection of resources related to the current activity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.resources = com_object

    def add(self, i_resource: Resource) -> Resource:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(Resource iResource) As Resource
                | 
                |     This method add the specified item in the current list
                | 
                |     Parameters:
                | 
                |         iItem
                |             The item to add 
                | 
                |     Returns:
                |         oitem The item

        :param Resource i_resource:
        :rtype: Resource
        """
        return Resource(self.resources.Add(i_resource.com_object))

    def add_by_assignment_type(self, i_resource: Resource, i_assignment_type: str) -> Resource:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddByAssignmentType(Resource iResource,
                | DNBResourceAssignmentType iAssignmentType) As Resource
                | 
                |     This method Assigns/Adds the specified resource with the specified
                |     assignment type
                | 
                |     Parameters:
                | 
                |         iResource
                |             The resource to be assigned 
                |         iAssignmentType
                |             Type of the Assignment (Resource to the Process). Only the
                |             following four types are supported at the moment: Process_Uses_Resource,
                |             Process_Runs_On_Resource, Process_Attaches_Resource, Process_Detaches_Resource
                |             
                | 
                |     Returns:
                |         oResource The resource when Add succeeds, unchanged otherwise

        :param Resource i_resource:
        :param str i_assignment_type:
        :rtype: Resource
        """
        return Resource(self.resources.AddByAssignmentType(i_resource.com_object, i_assignment_type))

    def item(self, i_index: cat_variant) -> Resource:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Resource
                | 
                |     This method returns the idl object Resource for the specified resource
                |     identifier.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The resource identifier 
                | 
                |     Returns:
                |         oResource The idl resource

        :param cat_variant i_index:
        :rtype: Resource
        """
        return Resource(self.resources.Item(i_index))

    def remove_by_assignment_type(self, i_resource: Resource, i_assignment_type: str) -> Resource:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func RemoveByAssignmentType(Resource iResource,
                | DNBResourceAssignmentType iAssignmentType) As Resource
                | 
                |     This method Unassigns/Removes the specified resource if the assignement
                |     exists and is of the given type
                | 
                |     Parameters:
                | 
                |         iResource
                |             The resource to be Unassigned 
                |         iAssignmentType
                |             Type of the Assignment (Resource to the Process) to be removed
                |             
                | 
                |     Returns:
                |         oResource The resource when Remove succeeds, unchanged otherwise

        :param Resource i_resource:
        :param str i_assignment_type:
        :rtype: Resource
        """
        return Resource(self.resources.RemoveByAssignmentType(i_resource.com_object, i_assignment_type))

    def __repr__(self):
        return f'Resources(name="{self.name}")'
