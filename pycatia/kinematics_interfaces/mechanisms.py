#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.kinematics_interfaces.mechanism import Mechanism
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Mechanisms(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Mechanisms
                | 
                | A collection of all Mechanism entities currently managed by the
                | application.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Mechanism)
        self.mechanisms = com_object

    def add(self) -> Mechanism:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add() As Mechanism
                | 
                |     Creates a new Mechanism and adds it to the Mechanisms
                |     collection.
                | 
                |     Returns:
                |         The created Mechanism 
                |     Example:
                |         This example creates a new Mechanism in the TheMechanisms
                |         collection.
                | 
                |             Dim NewMechanism As Mechanism
                |             Set NewMechanism = TheMechanisms.Add()

        :rtype: Mechanism
        """
        return Mechanism(self.mechanisms.Add())

    def item(self, i_index: cat_variant) -> Mechanism:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Mechanism
                | 
                |     Returns a Mechanism using its index or its name from the Mechanisms
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Mechanism to retrieve from the
                |             collection of Mechanisms. As a numerics, this index is the rank of the
                |             Mechanism in the collection. The index of the first Mechanism in the collection
                |             is 1, and the index of the last Mechanism is Count. As a string, it is the name
                |             you assigned to the Mechanism using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved Mechanism 
                |     Example:
                |         This example returns in ThisMechanism the third Mechanism in the
                |         collection, and in ThatMechanism the Mechanism named
                |         MyMechanism.
                | 
                |          Dim ThisMechanism As Mechanism
                |          Set ThisMechanism = TheMechanisms.Item(3)
                |          Dim ThatMechanism As Mechanism
                |          Set ThatMechanism = CATIA.Mechanisms.Item("MyMechanism")

        :param cat_variant i_index:
        :rtype: Mechanism
        """
        return Mechanism(self.mechanisms.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a Mechanism from the Mechanisms collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Mechanism to retrieve from the
                |             collection of mechanisms. As a numerics, this index is the rank of the
                |             Mechanism in the collection. The index of the first Mechanism in the collection
                |             is 1, and the index of the last Mechanism is Count. As a string, it is the name
                |             you assigned to the Mechanism. 
                | 
                |     Returns:
                |         Nothing 
                |     Example:
                |         The following example removes the tenth Mechanism and the Mechanism
                |         named MechanismTwo from the TheMechanisms collection.
                | 
                |             TheMechanisms.Remove(10)
                |             TheMechanisms.Remove("MechanismTwo")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.mechanisms.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(mechanisms)
        # #     Dim iIndex (2)
        # #     mechanisms.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Mechanisms(name="{self.name}")'
