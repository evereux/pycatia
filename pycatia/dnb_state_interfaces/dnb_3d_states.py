#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_state_interfaces.dnb_3d_state import DNB3DState
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class DNB3DStates(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DNB3DStates
                | 
                | Interface representing the collection of 3D State objects.
                | 
                | Role: Provides access to 3D State objects
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DNB3DState)
        self.dnb3_d_states = com_object

    @property
    def states_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StatesCount() As long (Read Only)
                | 
                |     Returns the number of 3D State objects in the collection.
                | 
                |     Example:
                |         This example fetches the Number of 3D states in the
                |         collection
                | 
                |          Dim list3DStates as DNB3DStates
                |          Set list3DStates = stateMgt.ListAll3DStates  
                |          stateCount = list3DStates.StatesCount

        :rtype: int
        """

        return self.dnb3_d_states.StatesCount

    def item(self, i_index: cat_variant) -> DNB3DState:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As DNB3DState
                | 
                |     Returns the 3D state object.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index to the item to be returned 
                | 
                |     Returns:
                |         The 3D State object
                | 
                |         Example:
                |             This example returns the first item from the collection 3D
                |             states
                | 
                |              Dim list3DStates as DNB3DStates
                |              Set list3DStates = positionMgt.ListAll3DStates
                |              Dim my3DState As DNB3DState
                |              Set my3DState = list3DStates.Item(1)

        :param cat_variant i_index:
        :rtype: DNB3DState
        """
        return DNB3DState(self.dnb3_d_states.Item(i_index))

    def __repr__(self):
        return f'DNB3DStates(name="{self.name}")'
