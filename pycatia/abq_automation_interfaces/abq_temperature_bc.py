#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_boundary_condition import ABQBoundaryCondition


class ABQTemperatureBC(ABQBoundaryCondition):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQBoundaryCondition
                |                         ABQTemperatureBC
                | 
                | Represents an Abaqus Temperature boundary condition (ABQTemperatureBC)
                | feature.
                | Role:Access an Abaqus Temperature boundary condition feature or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_temperature_bc = com_object

    @property
    def magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Magnitude() As double
                | 
                |     Sets or returns the magnitude of the temperature boundary
                |     condition.
                | 
                |     Returns:
                |         The magnitude of the temperature boundary condition.

        :rtype: float
        """

        return self.abq_temperature_bc.Magnitude

    @magnitude.setter
    def magnitude(self, value: float):
        """
        :param float value:
        """

        self.abq_temperature_bc.Magnitude = value

    @property
    def use_amplitude(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UseAmplitude() As boolean
                | 
                |     Sets or returns the UseAmplitude flag.
                | 
                |     Returns:
                |         A boolean specifying whether an amplitude will be
                |         used.

        :rtype: bool
        """

        return self.abq_temperature_bc.UseAmplitude

    @use_amplitude.setter
    def use_amplitude(self, value: bool):
        """
        :param bool value:
        """

        self.abq_temperature_bc.UseAmplitude = value

    def __repr__(self):
        return f'ABQTemperatureBC(name="{self.name}")'
