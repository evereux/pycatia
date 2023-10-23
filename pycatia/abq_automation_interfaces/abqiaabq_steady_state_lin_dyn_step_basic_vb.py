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


class ABQIAABQSteadyStateLinDynStepBasicVB(ABQStep):
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
                |                         ABQIAABQSteadyStateLinDynStepBasicVB
                | 
                | Interface representing xxx.
                | 
                | Role: Components that implement ABQIAABQSteadyStateLinDynStepBasic are
                | ...
                | 
                | Do not use the ABQIAABQSteadyStateLinDynStepBasic interface for such and such
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abqiaabq_steady_state_lin_dyn_step_basic_vb = com_object

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
                |          Dim abqSSDStep As ABQSteadStateStep 
                |          Dim abqBCs As ABQBoundaryConditions
                |          Set abqBCs = abqSSDStep.BoundaryConditions

        :rtype: ABQBoundaryConditions
        """

        return ABQBoundaryConditions(self.abqiaabq_steady_state_lin_dyn_step_basic_vb.BoundaryConditions)

    @property
    def description(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Description() As CATBSTR
                | 
                |     Returns or sets the description of the Abaqus steady state dynamic
                |     step.
                | 
                |     Returns:
                |         The description of the Abaqus steady state dynamic
                |         step.

        :rtype: str
        """

        return self.abqiaabq_steady_state_lin_dyn_step_basic_vb.Description

    @description.setter
    def description(self, value: str):
        """
        :param str value:
        """

        self.abqiaabq_steady_state_lin_dyn_step_basic_vb.Description = value

    @property
    def interval_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IntervalType() As short
                | 
                |     Returns or sets Interval Type.
                | 
                |     Returns:
                |         The Interval Type.
                |
                |         Legal values:
                |          1 - Eigenvalue.
                |          2 - Range.
                |
                |         Example:
                |             This example sets the Interval Type as Eigenvalue for
                |             abqSSDStep
                |             abqSSDStep.IntervalType = 1

        :rtype: int
        """

        return self.abqiaabq_steady_state_lin_dyn_step_basic_vb.IntervalType

    @interval_type.setter
    def interval_type(self, value: int):
        """
        :param int value:
        """

        self.abqiaabq_steady_state_lin_dyn_step_basic_vb.IntervalType = value

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
                |          Dim abqSSDStep As ABQSteadStateStep 
                |          Dim abqLoads As ABQLoads
                |          Set abqLoads = abqSSDStep.Loads

        :rtype: ABQLoads
        """

        return ABQLoads(self.abqiaabq_steady_state_lin_dyn_step_basic_vb.Loads)

    @property
    def scale_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ScaleType() As short
                | 
                |     Returns or sets Scale Type.
                | 
                |     Returns:
                |         The Scale Type.
                |
                |         Legal values:
                |          1 - Logarithmic.
                |          2 - Linear.
                |
                |         Example:
                |             This example sets the Scale Type as Logarithmic for
                |             abqSSDStep
                |             abqSSDStep.ScaleType = 1

        :rtype: int
        """

        return self.abqiaabq_steady_state_lin_dyn_step_basic_vb.ScaleType

    @scale_type.setter
    def scale_type(self, value: int):
        """
        :param int value:
        """

        self.abqiaabq_steady_state_lin_dyn_step_basic_vb.ScaleType = value

    def add_frequency_data_table(
            self,
            i_lwr_frequency: tuple,
            i_upr_frequency: tuple,
            i_nb_points: tuple,
            i_bias: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddFrequencyDataTable(CATSafeArrayVariant
                | iLwrFrequency,
                | CATSafeArrayVariant iUprFrequency,
                | CATSafeArrayVariant iNbPoints,
                | CATSafeArrayVariant iBias)
                | 
                |     Adds a list of frequency, real and imaginary The number of values in all
                |     the four of the parameters must match. If either list contains extra values,
                |     the extra values are discarded.
                | 
                |     Parameters:
                | 
                |         iLwrFrequency
                |             The list of lower frequencies.
                |         iUprFrequency
                |             The list of upper frequencies.
                |         iNbPoints
                |             The list of number of points.
                |         iBias
                |             The list of bias.

        :param tuple i_lwr_frequency:
        :param tuple i_upr_frequency:
        :param tuple i_nb_points:
        :param tuple i_bias:
        :rtype: None
        """
        return self.abqiaabq_steady_state_lin_dyn_step_basic_vb.AddFrequencyDataTable(
            i_lwr_frequency,
            i_upr_frequency,
            i_nb_points,
            i_bias
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_frequency_data_table'
        # # vba_code = """
        # # Public Function add_frequency_data_table(abqiaabq_steady_state_lin_dyn_step_basic_vb)
        # #     Dim iLwrFrequency (2)
        # #     abqiaabq_steady_state_lin_dyn_step_basic_vb.AddFrequencyDataTable iLwrFrequency
        # #     add_frequency_data_table = iLwrFrequency
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_global_damping(self, i_alpha: float, i_beta: float, i_structural: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddGlobalDamping(double iAlpha,
                | double iBeta,
                | double iStructural)
                | 
                |     Returns or sets Global Damping values.
                | 
                |     Returns:
                |         Global Damping values.

        :param float i_alpha:
        :param float i_beta:
        :param float i_structural:
        :rtype: None
        """
        return self.abqiaabq_steady_state_lin_dyn_step_basic_vb.AddGlobalDamping(i_alpha, i_beta, i_structural)

    def __repr__(self):
        return f'ABQIAABQSteadyStateLinDynStepBasicVB(name="{self.name}")'
