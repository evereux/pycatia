#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.behavior_interfaces.behaviors import Behaviors


class Behavior(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Behavior
                | 
                | Represents a behavior.
                | Role: A behavior is a set of tasks performed on a technological object. It can
                | be V5 command, CAA command, VBA command, external application or behavior
                | defined into the BKT product. A behavior contains a set of variables: the
                | inputs entered by the user and the outputs produced by the behavior. This
                | interface manipulates the characteristics of a behavior: children behaviors,
                | inputs/outputs and activity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.behavior = com_object

    @property
    def behaviors(self) -> 'Behaviors':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Behaviors() As Behaviors (Read Only)
                | 
                |     Returns the collection of children behaviors.
                | 
                |     Example:
                |         This example retrieves in BehCollection the collection of Behaviors
                |         currently managed by a Behavior Beh.
                | 
                |          Dim BehCollection As Behaviors
                |          Set BehCollection = Beh.Behaviors

        :rtype: Behaviors
        """

        from pycatia.behavior_interfaces.behaviors import Behaviors
        return Behaviors(self.behavior.Behaviors)

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Activate()
                | 
                |     Activates a behavior.
                | 
                |     Example:
                |         This example activates a Behavior Beh.
                | 
                |          Beh.Activate

        :rtype: None
        """
        return self.behavior.Activate()

    def deactivate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Deactivate()
                | 
                |     Deactivates a behavior.
                | 
                |     Example:
                |         This example deactivates a Behavior Beh.
                | 
                |          Beh.Deactivate

        :rtype: None
        """
        return self.behavior.Deactivate()

    def get_input(self, p_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetInput(CATBSTR pName) As AnyObject
                | 
                |     Returns the value of one available input of the behavior.
                | 
                |     Parameters:
                | 
                |         pName
                |             the name of the input 
                | 
                |     Example:
                |         This example retrieves in BehParameter the published input
                |         CATIAParameter Nb_Cylinder currently managed by a Behavior
                |         Beh.
                | 
                |          Dim BehParameter as Parameter
                |          Set BehParameter = Beh.GetInput("Nb_Cylinder")

        :param str p_name:
        :rtype: AnyObject
        """
        return AnyObject(self.behavior.GetInput(p_name))

    def get_output(self, p_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOutput(CATBSTR pName) As AnyObject
                | 
                |     Returns the value of one available output of the behavior.
                | 
                |     Parameters:
                | 
                |         pName
                |             the name of the output 
                | 
                |     Example:
                |         This example retrieves in BehPower the published output CATIAParameter
                |         Power currently managed by a Behavior Beh.
                | 
                |          Dim BehPower as Parameter
                |          Set BehPower = Beh.GetOutput("Power")

        :param str p_name:
        :rtype: AnyObject
        """
        return AnyObject(self.behavior.GetOutput(p_name))

    def put_output(self, p_name: str, o_value: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutOutput(CATBSTR pName,
                | AnyObject oValue)
                | 
                |     Valuates an available output of the behavior. The behavior must be in
                |     operating state, otherwise it fails.
                |     It can be applicable from a CATIABehaviorVBScript Execution for
                |     instance.
                | 
                |     Parameters:
                | 
                |         pName
                |             the name of the output 
                |         oValue
                |             the value of the output 
                | 
                |     Example:
                |         This example assigns to the published CATIAParameter Power of a
                |         Behavior Beh. the value of BehPower
                | 
                |          Dim BehPower as Parameter
                |          ...
                |          Beh.PutOutput "Power", BehPower

        :param str p_name:
        :param AnyObject o_value:
        :rtype: None
        """
        return self.behavior.PutOutput(p_name, o_value.com_object)

    def test_input(self, p_name: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func TestInput(CATBSTR pName) As long
                | 
                |     Tests if the behavior's input is set or not.
                | 
                |     Parameters:
                | 
                |         pName
                |             the name of the input 
                | 
                |     Example:
                |         This example tests the existence of the value of the published
                |         CATIAParameter Nb_Cylinder currently managed by a Behavior
                |         Beh.
                | 
                |          if (Beh.TestInput("Nb_Cylinder"))

        :param str p_name:
        :rtype: int
        """
        return self.behavior.TestInput(p_name)

    def test_output(self, p_name: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func TestOutput(CATBSTR pName) As long
                | 
                |     Tests if the behavior's output is set or not.
                | 
                |     Parameters:
                | 
                |         pName
                |             the name of the output 
                | 
                |     Example:
                |         This example tests the existence of the value of the published
                |         CATIAParameter Power currently managed by a Behavior
                |         Beh.
                | 
                |          if (Beh.TestOutput("Power"))

        :param str p_name:
        :rtype: int
        """
        return self.behavior.TestOutput(p_name)

    def __repr__(self):
        return f'Behavior(name="{self.name}")'
