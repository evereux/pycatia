#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.behavior_interfaces.behavior import Behavior


class BehaviorExtension(Behavior):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATBehaviorInterfaces.Behavior
                |                         BehaviorExtension
                | 
                | Manages the behaviors of a technological object.
                | Role: This interface allows to select and perform the behaviors (tasks)
                | associated to a technological object. A behavior extension is obtained from an
                | object using the method GetItem of CATIABase with in argument the keyword
                | "CATGetBehaviorExtension".
                | 
                | Example:
                | 
                |      Set RootPart = CATIA.ActiveDocument.Part
                |      Set MyExtension = RootPart.GetItem("CATGetBehaviorExtensions")
                |      Set listBehavior = MyExtension.Behaviors
                |      MyExtension.SelectBehavior("MyBehavior")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.behavior_extension = com_object

    @property
    def extension_class(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExtensionClass() As CATBSTR (Read Only)
                | 
                |     Returns the type of the technological object associated to this behavior
                |     extension.

        :rtype: str
        """

        return self.behavior_extension.ExtensionClass

    def select_behavior(self, behavior_name: str) -> Behavior:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func SelectBehavior(CATBSTR BehaviorName) As Behavior
                | 
                |     Selects and executes a behavior of the technological object. The wanted
                |     behavior is specified by its name.
                | 
                |     Parameters:
                | 
                |         BehaviorName
                |             the name of the behavior.

        :param str behavior_name:
        :rtype: Behavior
        """
        return Behavior(self.behavior_extension.SelectBehavior(behavior_name))

    def __repr__(self):
        return f'BehaviorExtension(name="{self.name}")'
