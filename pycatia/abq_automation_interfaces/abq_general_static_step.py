#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_boundary_conditions import ABQBoundaryConditions
from pycatia.abq_automation_interfaces.abq_fields import ABQFields
from pycatia.abq_automation_interfaces.abq_loads import ABQLoads
from pycatia.abq_automation_interfaces.abq_step import ABQStep


class ABQGeneralStaticStep(ABQStep):
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
                |                         ABQGeneralStaticStep
                | 
                | Represents an Abaqus general static step (ABQGeneralStaticStep)
                | object.
                | Role: Access an Abaqus general static step object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_general_static_step = com_object

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
                |          Dim abqGenStep As ABQGeneralStaticStep 
                |          Dim abqBCs As ABQBoundaryConditions
                |          Set abqBCs = abqGenStep.BoundaryConditions

        :rtype: ABQBoundaryConditions
        """

        return ABQBoundaryConditions(self.abq_general_static_step.BoundaryConditions)

    @property
    def description(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Description() As CATBSTR
                | 
                |     Returns or sets the description of the Abaqus general static
                |     step.
                | 
                |     Returns:
                |         The description of the Abaqus general static step.

        :rtype: str
        """

        return self.abq_general_static_step.Description

    @description.setter
    def description(self, value: str):
        """
        :param str value:
        """

        self.abq_general_static_step.Description = value

    @property
    def energy_fraction(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EnergyFraction() As double
                | 
                |     Returns or sets the EnergyFraction if the stabilization method is
                |     DISSIPATION.
                | 
                |     Returns:
                |         The energy fraction.

        :rtype: float
        """

        return self.abq_general_static_step.EnergyFraction

    @energy_fraction.setter
    def energy_fraction(self, value: float):
        """
        :param float value:
        """

        self.abq_general_static_step.EnergyFraction = value

    @property
    def fields(self) -> ABQFields:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Fields() As ABQFields (Read Only)
                | 
                |     Returns the ABQFields container associated with the step.
                | 
                |     Example:
                |         This example retrieves the ABQFields container
                |         abqFields.
                | 
                |          Dim abqGenStep As ABQGeneralStaticStep 
                |          Dim abqFields As ABQFields
                |          Set abqFields = abqGenStep.Fields

        :rtype: ABQFields
        """

        return ABQFields(self.abq_general_static_step.Fields)

    @property
    def initial_inc(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InitialInc() As double
                | 
                |     Returns or sets the size of the initial increment.
                | 
                |     Returns:
                |         The initial increment size.

        :rtype: float
        """

        return self.abq_general_static_step.InitialInc

    @initial_inc.setter
    def initial_inc(self, value: float):
        """
        :param float value:
        """

        self.abq_general_static_step.InitialInc = value

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
                |          Dim abqGenStep As ABQGeneralStaticStep 
                |          Dim abqLoads As ABQLoads
                |          Set abqLoads = abqGenStep.Loads

        :rtype: ABQLoads
        """

        return ABQLoads(self.abq_general_static_step.Loads)

    @property
    def max_inc(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxInc() As double
                | 
                |     Returns or sets the maximum increment if the type of the incrementation is
                |     set to AUTO_INCREMENT.
                | 
                |     Returns:
                |         The maximum increment.

        :rtype: float
        """

        return self.abq_general_static_step.MaxInc

    @max_inc.setter
    def max_inc(self, value: float):
        """
        :param float value:
        """

        self.abq_general_static_step.MaxInc = value

    @property
    def max_num_inc(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxNumInc() As short
                | 
                |     Returns or sets the maximum number of increments if the type of the
                |     incremention is set to AUTO_INCREMENT.
                | 
                |     Returns:
                |         The maximum number of increments.

        :rtype: int
        """

        return self.abq_general_static_step.MaxNumInc

    @max_num_inc.setter
    def max_num_inc(self, value: int):
        """
        :param int value:
        """

        self.abq_general_static_step.MaxNumInc = value

    @property
    def min_inc(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MinInc() As double
                | 
                |     Returns or sets the minimum increment if the type of the incrementation is
                |     set to AUTO_INCREMENT.
                | 
                |     Returns:
                |         The minimum increment.

        :rtype: float
        """

        return self.abq_general_static_step.MinInc

    @min_inc.setter
    def min_inc(self, value: float):
        """
        :param float value:
        """

        self.abq_general_static_step.MinInc = value

    @property
    def nl_geom(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NLGeom() As boolean
                | 
                |     Returns or sets whether the geometry remains linear during the analysis. A
                |     value of true indicates that the geometry remains linear.
                | 
                |     Returns:
                |         A boolean specifying whether the geometry remains linear during the
                |         analysis.

        :rtype: bool
        """

        return self.abq_general_static_step.NLGeom

    @nl_geom.setter
    def nl_geom(self, value: bool):
        """
        :param bool value:
        """

        self.abq_general_static_step.NLGeom = value

    @property
    def stabilization(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Stabilization() As boolean (Read Only)
                | 
                |     Returns a boolean indicating whether the stabilization option was
                |     selected.
                | 
                |     Returns:
                |         The stabilization status. 
                |     Example:
                |         The following example returns the status of the stabilization option
                |         bFlag in the general static step generalstaticstep.
                | 
                |          Dim generalstaticstep As ABQGeneralStaticStep
                |          Dim bFlag As boolean
                |          Set bFlag =  generalstaticstep.Stabilization

        :rtype: bool
        """

        return self.abq_general_static_step.Stabilization

    @property
    def stabilization_magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StabilizationMagnitude() As double
                | 
                |     Sets and Returns the damping factor if the stabilization method is
                |     FACTOR.
                | 
                |     Returns:
                |         The damping factor.

        :rtype: float
        """

        return self.abq_general_static_step.StabilizationMagnitude

    @stabilization_magnitude.setter
    def stabilization_magnitude(self, value: float):
        """
        :param float value:
        """

        self.abq_general_static_step.StabilizationMagnitude = value

    @property
    def stabilization_method(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StabilizationMethod() As Stabilization_Type
                | 
                |     Returns or sets the stabilization method if the Stabilization option is
                |     selected.
                | 
                |     Returns:
                |         The stabilization method
                | 
                |           
                |         Legal values:
                |           DISSIPATION
                |           FACTOR

        :rtype: enum stabilization_type
        :rtype: int
        """

        return self.abq_general_static_step.StabilizationMethod

    @stabilization_method.setter
    def stabilization_method(self, value: int):
        """
        :param int value: enum stabilization_type
        """

        self.abq_general_static_step.StabilizationMethod = value

    @property
    def time_incrementation_method(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TimeIncrementationMethod() As Incrementation_Type
                | 
                |     Returns or sets the type of the incrementation during the
                |     step.
                | 
                |     Returns:
                |         The type of the incrementation.
                | 
                |           
                |         Legal values:
                |           AUTO_INCREMENT
                |           FIXED_INCREMENT

        :return: enum incrementation_type
        :rtype: int
        """

        return self.abq_general_static_step.TimeIncrementationMethod

    @time_incrementation_method.setter
    def time_incrementation_method(self, value: int):
        """
        :param int value: enum incrementation_type
        """

        self.abq_general_static_step.TimeIncrementationMethod = value

    @property
    def time_period(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TimePeriod() As double
                | 
                |     Returns or sets the total time period of the Abaqus general static
                |     step.
                | 
                |     Returns:
                |         The total time period of the Abaqus general static step.

        :rtype: float
        """

        return self.abq_general_static_step.TimePeriod

    @time_period.setter
    def time_period(self, value: float):
        """
        :param float value:
        """

        self.abq_general_static_step.TimePeriod = value

    def __repr__(self):
        return f'ABQGeneralStaticStep(name="{self.name}")'
