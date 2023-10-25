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


class ABQExplicitDynamicsStep(ABQStep):
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
                |                         ABQExplicitDynamicsStep
                | 
                | Represents an Abaqus explicit dynamics step (ABQExplicitDynamicsStep)
                | object.
                | Role: Access an Abaqus explicit dynamics step object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_explicit_dynamics_step = com_object

    @property
    def auto_time_increment_method(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AutoTimeIncrementMethod() As
                | AutoTimeIncrementMethod
                | 
                |     Sets or returns the automatic time increment estimator method. Applies only
                |     when TimeIncrementationMethod is AUTO_INCREMENT.
                | 
                |       
                |     Legal values:
                |         ABQ_ATI_GLOBAL
                |         ABQ_ATI_ELEMENT_BY_ELEMENT

        :return: enum auto_time_increment_method
        :rtype: int
        """

        return self.abq_explicit_dynamics_step.AutoTimeIncrementMethod

    @auto_time_increment_method.setter
    def auto_time_increment_method(self, value: int):
        """
        :param int value: enum auto_time_increment_method
        """

        self.abq_explicit_dynamics_step.AutoTimeIncrementMethod = value

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
                |          Dim abqStep As ABQExplicitDynamicsStep 
                |          Dim abqBCs As ABQBoundaryConditions
                |          Set abqBCs = abqStep.BoundaryConditions

        :rtype: ABQBoundaryConditions
        """

        return ABQBoundaryConditions(self.abq_explicit_dynamics_step.BoundaryConditions)

    @property
    def description(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Description() As CATBSTR
                | 
                |     Sets or returns the description of the Abaqus explicit dynamics
                |     step.
                | 
                |     Returns:
                |         The description of the Abaqus explicit dynamics step.

        :rtype: str
        """

        return self.abq_explicit_dynamics_step.Description

    @description.setter
    def description(self, value: str):
        """
        :param str value:
        """

        self.abq_explicit_dynamics_step.Description = value

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
                |          Dim abqStep As ABQExplicitDynamicsStep 
                |          Dim abqFields As ABQFields
                |          Set abqFields = abqStep.Fields

        :rtype: ABQFields
        """

        return ABQFields(self.abq_explicit_dynamics_step.Fields)

    @property
    def fixed_time_increment_method(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FixedTimeIncrementMethod() As
                | FixedTimeIncrementMethod
                | 
                |     Sets or returns the fixed time increment method. Applies only when
                |     TimeIncrementationMethod is FIXED_INCREMENT. If the method is set to
                |     ABQ_FTI_USER_DEFINED, the UserDefinedTimeIncrementValue property must be set to
                |     specifiy the time increment value.

        :return: enum fixed_time_increment_method
        :rtype: int
        """

        return self.abq_explicit_dynamics_step.FixedTimeIncrementMethod

    @fixed_time_increment_method.setter
    def fixed_time_increment_method(self, value: int):
        """
        :param int value: enum fixed_time_increment_method
        """

        self.abq_explicit_dynamics_step.FixedTimeIncrementMethod = value

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
                |          Dim abqStep As ABQExplicitDynamicsStep 
                |          Dim abqLoads As ABQLoads
                |          Set abqLoads = abqStep.Loads

        :rtype: ABQLoads
        """

        return ABQLoads(self.abq_explicit_dynamics_step.Loads)

    @property
    def maximum_time_increment_limit(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaximumTimeIncrementLimit() As double
                | 
                |     Sets or returns the maximum time increment limit. Applies only when
                |     TimeIncrementationMethod is AUTO_INCREMENT. Zero specifies that the maximum
                |     time increment is unlimited.
                | 
                |     Returns:
                |         The maximum time increment limit.

        :rtype: float
        """

        return self.abq_explicit_dynamics_step.MaximumTimeIncrementLimit

    @maximum_time_increment_limit.setter
    def maximum_time_increment_limit(self, value: float):
        """
        :param float value:
        """

        self.abq_explicit_dynamics_step.MaximumTimeIncrementLimit = value

    @property
    def nl_geom(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NLGeom() As boolean
                | 
                |     Sets or returns whether the geometry remains linear during the analysis. A
                |     value of true indicates that the geometry remains linear.
                | 
                |     Returns:
                |         A boolean specifying whether the geometry remains linear during the
                |         analysis.

        :rtype: bool
        """

        return self.abq_explicit_dynamics_step.NLGeom

    @nl_geom.setter
    def nl_geom(self, value: bool):
        """
        :param bool value:
        """

        self.abq_explicit_dynamics_step.NLGeom = value

    @property
    def time_incrementation_method(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TimeIncrementationMethod() As Incrementation_Type
                | 
                |     Sets or returns the type of the incrementation during the
                |     step.
                | 
                |     Returns:
                |         The type of the incrementation
                | 
                |           
                |         Legal values:
                |           AUTO_INCREMENT
                |           FIXED_INCREMENT

        :return: enum incrementation_type
        :rtype: int
        """

        return self.abq_explicit_dynamics_step.TimeIncrementationMethod

    @time_incrementation_method.setter
    def time_incrementation_method(self, value: int):
        """
        :param int value: enum incrementation_type
        """

        self.abq_explicit_dynamics_step.TimeIncrementationMethod = value

    @property
    def time_period(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TimePeriod() As double
                | 
                |     Sets or returns the total time period of the Abaqus explicit dynamics
                |     step.
                | 
                |     Returns:
                |         The total time period of the Abaqus explicit dynamics step.

        :rtype: float
        """

        return self.abq_explicit_dynamics_step.TimePeriod

    @time_period.setter
    def time_period(self, value: float):
        """
        :param float value:
        """

        self.abq_explicit_dynamics_step.TimePeriod = value

    @property
    def time_scaling_factor(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TimeScalingFactor() As double
                | 
                |     Sets or returns the time scaling factor.

        :rtype: float
        """

        return self.abq_explicit_dynamics_step.TimeScalingFactor

    @time_scaling_factor.setter
    def time_scaling_factor(self, value: float):
        """
        :param float value:
        """

        self.abq_explicit_dynamics_step.TimeScalingFactor = value

    @property
    def user_defined_time_increment_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UserDefinedTimeIncrementValue() As double
                | 
                |     Sets or returns the user-defined time increment value. Applies only when
                |     FixedTimeIncrementMethod is set to ABQ_FTI_USER_DEFINED.

        :rtype: float
        """

        return self.abq_explicit_dynamics_step.UserDefinedTimeIncrementValue

    @user_defined_time_increment_value.setter
    def user_defined_time_increment_value(self, value: float):
        """
        :param float value:
        """

        self.abq_explicit_dynamics_step.UserDefinedTimeIncrementValue = value

    def __repr__(self):
        return f'ABQExplicitDynamicsStep(name="{self.name}")'
