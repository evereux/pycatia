#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.behavior_interfaces.behavior import Behavior
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Behaviors(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Behaviors
                | 
                | Represents the Behaviors collection currently managed by the
                | application.
                | These behaviors belong to one objet and can be reached by the GetItem method of
                | CATIABase. For Instance onto a Part using
                | Part.GetItem("CATGetBehaviorExtension") .
                | 
                | Example:
                | 
                |      Set RootPart = CATIA.ActiveDocument.Part
                |      Set MyExtension = RootPart.GetItem("CATGetBehaviorExtensions")
                |      Set listBehaviors = MyExtension.Behaviors
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Behavior)
        self.behaviors = com_object

    def item(self, i_index: cat_variant) -> Behavior:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Behavior
                | 
                |     Returns a Behavior using its index or its name from the Behaviors
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Behavior to retrieve from the
                |             collection of Behaviors. As a numerics, this index is the rank of the Behavior
                |             in the collection. The index of the first Behavior in the collection is 1, and
                |             the index of the last Behavior is Count. As a string, it is the name you
                |             assigned to the Behavior using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved Behavior 
                |     Example:
                |         This example retrieves in ThisBeh the fifth Behavior in the collection
                |         and in ThatBeh the Behavior named MyBeh.
                | 
                |          Dim ThisBeh As Behavior
                |          Set ThisBeh = listBehaviors.Item(5)
                |          Dim ThatBeh As Behavior
                |          Set ThatBeh = listBehaviors.Item("MyBeh")

        :param cat_variant i_index:
        :rtype: Behavior
        """
        return Behavior(self.behaviors.Item(i_index))

    def __repr__(self):
        return f'Behaviors(name="{self.name}")'
