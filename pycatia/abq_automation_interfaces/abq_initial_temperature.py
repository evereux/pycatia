#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_temperature import ABQTemperature


class ABQInitialTemperature(ABQTemperature):
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
                |                         ABQInitialTemperature
                | 
                | Represents an Abaqus initial temperature object
                | (ABQInitialTemperature).
                | Role: Access an Abaqus initial temperature object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_initial_temperature = com_object

    @property
    def step_num(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StepNum() As short
                | 
                |     Sets or returns the step number from which to read the temperature data.

        :rtype: int
        """

        return self.abq_initial_temperature.StepNum

    @step_num.setter
    def step_num(self, value: int):
        """
        :param int value:
        """

        self.abq_initial_temperature.StepNum = value

    def __repr__(self):
        return f'ABQInitialTemperature(name="{self.name}")'
