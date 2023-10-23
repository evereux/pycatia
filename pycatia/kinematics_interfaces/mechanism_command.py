#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class MechanismCommand(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MechanismCommand
                | 
                | Interface to access the Command object (in Kinematics
                | context).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mechanism_command = com_object

    @property
    def current_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CurrentValue() As double (Read Only)
                | 
                |     Returns the current value for a command.
                | 
                |     Parameters:
                | 
                |         oCurrentValue
                |             The current value This property is read only because current value
                |             modification is done by solver

        :rtype: float
        """

        return self.mechanism_command.CurrentValue

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Orientation() As short
                | 
                |     Deprecated:
                |         V5R18 Not implemented - will be deprecated Returns or sets the command
                |         orientation. 
                |     Parameters:
                | 
                |         oOrientation
                |             The orientation of the command; only the sign is important (+: same
                |             as relying joint/-: opposite)

        :rtype: int
        """

        return self.mechanism_command.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.mechanism_command.Orientation = value

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the command type.
                | 
                |     Parameters:
                | 
                |         oType
                |             The type of the command 
                | 
                |     See also:
                |         Mechanism

        :rtype: str
        """

        return self.mechanism_command.Type

    def __repr__(self):
        return f'MechanismCommand(name="{ self.name }")'
