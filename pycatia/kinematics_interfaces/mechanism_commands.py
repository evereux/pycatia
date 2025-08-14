#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.kinematics_interfaces.mechanism_command import MechanismCommand
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class MechanismCommands(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     MechanismCommands
                | 
                | A collection of all MechanismCommand entities currently managed by the
                | application.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=MechanismCommand)
        self.mechanism_commands = com_object

    def add(self) -> MechanismCommand:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add() As MechanismCommand
                | 
                |     Creates a new MechanismCommand and adds it to the MechanismCommands
                |     collection.
                | 
                |     Returns:
                |         The created MechanismCommand 
                |     Example:
                |         This example creates a new MechanismCommand in the TheCommands
                |         collection.
                | 
                |             Dim NewCommand As MechanismCommand
                |             Set NewCommand = TheCommands.Add()

        :rtype: MechanismCommand
        """
        return MechanismCommand(self.mechanism_commands.Add())

    def item(self, i_index: cat_variant) -> MechanismCommand:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As MechanismCommand
                | 
                |     Returns a MechanismCommand using its index or its name from the Commands
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the MechanismCommand to retrieve from the
                |             collection of Commands. As a numerics, this index is the rank of the
                |             MechanismCommand in the collection. The index of the first MechanismCommand in
                |             the collection is 1, and the index of the last MechanismCommand is Count. As a
                |             string, it is the name you assigned to the MechanismCommand using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved MechanismCommand 
                |     Example:
                |         This example returns in ThisCommand the third MechanismCommand in the
                |         collection, and in ThatCommand the MechanismCommand named
                |         MyCommand.
                | 
                |          Dim ThisCommand As MechanismCommand
                |          Set ThisCommand = TheCommands.Item(3)
                |          Dim ThatCommand As MechanismCommand
                |          Set ThatCommand = CATIA.MechanismCommands.Item("MyCommand")

        :param cat_variant i_index:
        :rtype: MechanismCommand
        """
        return MechanismCommand(self.mechanism_commands.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Remove a MechanismCommand from the MechanismCommands
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the MechanismCommand to retrieve from the
                |             collection of MechanismCommands. As a numerics, this index is the rank of the
                |             MechanismCommand in the collection. The index of the first MechanismCommand in
                |             the collection is 1, and the index of the last MechanismCommand is Count. As a
                |             string, it is the name you assigned to the MechanismCommand.
                |             
                | 
                |     Returns:
                |         Nothing 
                |     Example:
                |         The following example removes the tenth MechanismCommand and the
                |         MechanismCommand named CommandTwo from the TheCommands
                |         collection.
                | 
                |             TheCommands.Remove(10)
                |             TheCommands.Remove("CommandTwo")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.mechanism_commands.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(mechanism_commands)
        # #     Dim iIndex (2)
        # #     mechanism_commands.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MechanismCommands(name="{self.name}")'
