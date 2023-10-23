#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_load import ABQLoad


class ABQPressure(ABQLoad):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQLoad
                |                         ABQPressure
                | 
                | Represents an Abaqus pressure (ABQPressure) object.
                | Role: Access an Abaqus pressure object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_pressure = com_object

    @property
    def apply_user_subroutine(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ApplyUserSubroutine() As boolean
                | 
                |     Sets or returns the user subroutine flag.
                | 
                |     Returns:
                |         A boolean specifying whether a user subroutine will be applied.

        :rtype: bool
        """

        return self.abq_pressure.ApplyUserSubroutine

    @apply_user_subroutine.setter
    def apply_user_subroutine(self, value: bool):
        """
        :param bool value:
        """

        self.abq_pressure.ApplyUserSubroutine = value

    @property
    def magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Magnitude() As double
                | 
                |     Sets or returns the magnitude of the pressure load.
                | 
                |     Returns:
                |         The magnitude of the pressure load.

        :rtype: float
        """

        return self.abq_pressure.Magnitude

    @magnitude.setter
    def magnitude(self, value: float):
        """
        :param float value:
        """

        self.abq_pressure.Magnitude = value

    def __repr__(self):
        return f'ABQPressure(name="{self.name}")'
