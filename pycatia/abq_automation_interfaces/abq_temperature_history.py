#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_tabular_amplitude import ABQTabularAmplitude
from pycatia.abq_automation_interfaces.abq_temperature import ABQTemperature


class ABQTemperatureHistory(ABQTemperature):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQTemperature
                |                         ABQTemperatureHistory
                | 
                | Represents an Abaqus temperature history object
                | (ABQTemperatureHistory).
                | Role: Access an Abaqus temperature history object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_temperature_history = com_object

    @property
    def activation_status(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActivationStatus() As boolean
                | 
                |     Sets or returns the activation status.
                | 
                |     Returns:
                |         A boolean specifying whether the feature is activated.

        :rtype: bool
        """

        return self.abq_temperature_history.ActivationStatus

    @activation_status.setter
    def activation_status(self, value: bool):
        """
        :param bool value:
        """

        self.abq_temperature_history.ActivationStatus = value

    @property
    def amplitude(self) -> ABQTabularAmplitude:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Amplitude() As ABQTabularAmplitude
                | 
                |     Sets or returns the amplitude of the temperature field.
                | 
                |     Example:
                |         This example retrieves the ABQTabularAmplitude
                |         abqAmplitude.
                | 
                |          Dim abqTemperature As ABQTemperature
                |          Dim abqAmplitude As ABQTabularAmplitude 
                |          Set abqAmplitude = abqTemperature.Amplitude

        :rtype: ABQTabularAmplitude
        """

        return ABQTabularAmplitude(self.abq_temperature_history.Amplitude)

    @amplitude.setter
    def amplitude(self, value: ABQTabularAmplitude):
        """
        :param ABQTabularAmplitude value:
        """

        self.abq_temperature_history.Amplitude = value

    @property
    def begin_step_num(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BeginStepNum() As short
                | 
                |     Sets or returns the step number at which to start reading the temperature
                |     data.

        :rtype: int
        """

        return self.abq_temperature_history.BeginStepNum

    @begin_step_num.setter
    def begin_step_num(self, value: int):
        """
        :param int value:
        """

        self.abq_temperature_history.BeginStepNum = value

    @property
    def end_step_num(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndStepNum() As short
                | 
                |     Sets or returns the step number at which to stop reading the temperature
                |     data.

        :rtype: int
        """

        return self.abq_temperature_history.EndStepNum

    @end_step_num.setter
    def end_step_num(self, value: int):
        """
        :param int value:
        """

        self.abq_temperature_history.EndStepNum = value

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

        return self.abq_temperature_history.UseAmplitude

    @use_amplitude.setter
    def use_amplitude(self, value: bool):
        """
        :param bool value:
        """

        self.abq_temperature_history.UseAmplitude = value

    def __repr__(self):
        return f'ABQTemperatureHistory(name="{self.name}")'
