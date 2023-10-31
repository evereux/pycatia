#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_boundary_conditions import ABQBoundaryConditions
from pycatia.abq_automation_interfaces.abq_loads import ABQLoads
from pycatia.abq_automation_interfaces.abq_step import ABQStep


class ABQHeatTransferStep(ABQStep):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQStep
                |                         ABQHeatTransferStep
                | 
                | Represents an Abaqus heat transfer step (ABQHeatTransferStep)
                | object.
                | Role: Access an Abaqus heat transfer step object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_heat_transfer_step = com_object

    @property
    def boundary_conditions(self) -> ABQBoundaryConditions:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BoundaryConditions() As ABQBoundaryConditions (Read
                | Only)
                | 
                |     Returns the ABQBoundaryConditions container associated with the
                |     step.
                | 
                |     Example:
                |         This example retrieves the ABQBoundaryConditions container
                |         abqBCs.
                | 
                |          Dim abqHeatStep As ABQHeatTransferStep 
                |          Dim abqBCs As ABQBoundaryConditions
                |          Set abqBCs = abqHeatStep.BoundaryConditions

        :rtype: ABQBoundaryConditions
        """

        return ABQBoundaryConditions(self.abq_heat_transfer_step.BoundaryConditions)

    @property
    def delta_maximum(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Deltmx() As double
                | 
                |     Sets or returns the maximum temperature change to be allowed in an
                |     increment during a transient heat transfer analysis.
                | 
                |     Returns:
                |         Maximum temperature change to be allowed in an
                |         increment

        :rtype: float
        """

        return self.abq_heat_transfer_step.Deltmx

    @delta_maximum.setter
    def delta_maximum(self, value: float):
        """
        :param float value:
        """

        self.abq_heat_transfer_step.Deltmx = value

    @property
    def description(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Description() As CATBSTR
                | 
                |     Sets or returns the description of the step.
                | 
                |     Returns:
                |         The description of the step

        :rtype: str
        """

        return self.abq_heat_transfer_step.Description

    @description.setter
    def description(self, value: str):
        """
        :param str value:
        """

        self.abq_heat_transfer_step.Description = value

    @property
    def end_step_on_temp_change(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndStepOnTempChange() As boolean
                | 
                |     Sets or returns whether the step should end when steady state is reached. A
                |     value of true indicates that the step will end.
                | 
                |     Returns:
                |         A boolean indicating whether the step will end when steady state is
                |         reached

        :rtype: bool
        """

        return self.abq_heat_transfer_step.EndStepOnTempChange

    @end_step_on_temp_change.setter
    def end_step_on_temp_change(self, value: bool):
        """
        :param bool value:
        """

        self.abq_heat_transfer_step.EndStepOnTempChange = value

    @property
    def initial_inc(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InitialInc() As double
                | 
                |     Sets or returns the initial increment size.
                | 
                |     Returns:
                |         The initial increment size

        :rtype: float
        """

        return self.abq_heat_transfer_step.InitialInc

    @initial_inc.setter
    def initial_inc(self, value: float):
        """
        :param float value:
        """

        self.abq_heat_transfer_step.InitialInc = value

    @property
    def loads(self) -> ABQLoads:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Loads() As ABQLoads (Read Only)
                | 
                |     Returns the ABQLoads container associated with the step.
                | 
                |     Example:
                |         The following example retrieves the ABQLoads container
                |         abqLoads:
                | 
                |          Dim abqHeatStep As ABQHeatTransferStep
                |          Dim abqLoads As ABQLoads
                |          Set abqLoads = abqHeatStep.Loads

        :rtype: ABQLoads
        """

        return ABQLoads(self.abq_heat_transfer_step.Loads)

    @property
    def max_inc(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxInc() As double
                | 
                |     Sets or returns the maximum increment size if
                |     TimeIncrementationMethod=AUTO_INCREMENT.
                | 
                |     Returns:
                |         The maximum increment size

        :rtype: float
        """

        return self.abq_heat_transfer_step.MaxInc

    @max_inc.setter
    def max_inc(self, value: float):
        """
        :param float value:
        """

        self.abq_heat_transfer_step.MaxInc = value

    @property
    def max_num_inc(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxNumInc() As short
                | 
                |     Sets or returns the maximum number of increments if
                |     TimeIncrementationMethod=AUTO_INCREMENT.
                | 
                |     Returns:
                |         The maximum number of increments

        :rtype: int
        """

        return self.abq_heat_transfer_step.MaxNumInc

    @max_num_inc.setter
    def max_num_inc(self, value: int):
        """
        :param int value:
        """

        self.abq_heat_transfer_step.MaxNumInc = value

    @property
    def min_inc(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MinInc() As double
                | 
                |     Sets or returns the minimum increment size if
                |     TimeIncrementationMethod=AUTO_INCREMENT.
                | 
                |     Returns:
                |         The minimum increment size

        :rtype: float
        """

        return self.abq_heat_transfer_step.MinInc

    @min_inc.setter
    def min_inc(self, value: float):
        """
        :param float value:
        """

        self.abq_heat_transfer_step.MinInc = value

    @property
    def maximum_delta_emission(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Mxdem() As double
                | 
                |     Sets or returns the maximum allowable emissivity change with temperature
                |     and field variables during an increment.
                | 
                |     Returns:
                |         The maximum allowable emissivity change

        :rtype: float
        """

        return self.abq_heat_transfer_step.Mxdem

    @maximum_delta_emission.setter
    def maximum_delta_emission(self, value: float):
        """
        :param float value:
        """

        self.abq_heat_transfer_step.Mxdem = value

    @property
    def response(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Response() As Response_Type
                | 
                |     Sets or returns the response type.
                | 
                |     Returns:
                |         The response type
                | 
                |          
                |          
                |         Legal values:
                |           STEADY_STATE  
                |           TRANSIENT

        :return: enum response_type
        :rtype: int
        """

        return self.abq_heat_transfer_step.Response

    @response.setter
    def response(self, value: int):
        """
        :param int value: enum response_type
        """

        self.abq_heat_transfer_step.Response = value

    @property
    def time_incrementation_method(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TimeIncrementationMethod() As Incrementation_Type
                | 
                |     Sets or returns the incrementation type.
                | 
                |     Returns:
                |         The incrementation type
                | 
                |          
                |          
                |         Legal values:
                |           AUTO_INCREMENT
                |           FIXED_INCREMENT

        :return: enum incrementation_type
        :rtype: int
        """

        return self.abq_heat_transfer_step.TimeIncrementationMethod

    @time_incrementation_method.setter
    def time_incrementation_method(self, value: int):
        """
        :param int value: enum incrementation_type
        """

        self.abq_heat_transfer_step.TimeIncrementationMethod = value

    @property
    def time_period(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TimePeriod() As double
                | 
                |     Sets or returns the step time.
                | 
                |     Returns:
                |         The step time

        :rtype: float
        """

        return self.abq_heat_transfer_step.TimePeriod

    @time_period.setter
    def time_period(self, value: float):
        """
        :param float value:
        """

        self.abq_heat_transfer_step.TimePeriod = value

    def __repr__(self):
        return f'ABQHeatTransferStep(name="{self.name}")'
