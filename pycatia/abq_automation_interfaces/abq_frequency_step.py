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
from pycatia.in_interfaces.reference import Reference
from pycatia.product_structure_interfaces.product import Product


class ABQFrequencyStep(ABQStep):
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
                |                         ABQFrequencyStep
                | 
                | Represents an Abaqus frequency step (ABQFrequencyStep) object.
                | Role: Access an Abaqus frequency step object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_frequency_step = com_object

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
                |          Dim abqFreqStep As ABQFrequencyStep 
                |          Dim abqBCs As ABQBoundaryConditions
                |          Set abqBCs = abqFreqStep.BoundaryConditions

        :rtype: ABQBoundaryConditions
        """

        return ABQBoundaryConditions(self.abq_frequency_step.BoundaryConditions)

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

        return self.abq_frequency_step.Description

    @description.setter
    def description(self, value: str):
        """
        :param str value:
        """

        self.abq_frequency_step.Description = value

    @property
    def eigensolver_value(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EigensolverValue() As short
                | 
                |     Returns or sets Eigensolver Value.
                | 
                |     Returns:
                |         The Eigensolver Value.
                | 
                |           
                |         Legal values:
                |          1 - Lanczos.
                |          2 - AMS.
                |          
                | 
                |         Example:
                |             This example sets eigensolver as Lanczos
                |             abqFreqStep
                | 
                |              abqFreqStep.EigensolverValue = 1

        :rtype: int
        """

        return self.abq_frequency_step.EigensolverValue

    @eigensolver_value.setter
    def eigensolver_value(self, value: int):
        """
        :param int value:
        """

        self.abq_frequency_step.EigensolverValue = value

    @property
    def frequency_shift(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FrequencyShift() As short
                | 
                |     Returns or sets frequency shift value.
                | 
                |     Returns:
                |         The frequency shift value.
                | 
                |         Example:
                |             This example sets the maximum frequency for
                |             abqFreqStep
                | 
                |              abqFreqStep.FrequencyShift = 10

        :rtype: int
        """

        return self.abq_frequency_step.FrequencyShift

    @frequency_shift.setter
    def frequency_shift(self, value: int):
        """
        :param int value:
        """

        self.abq_frequency_step.FrequencyShift = value

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
                |          Dim abqFreqStep As ABQFrequencyStep 
                |          Dim abqLoads As ABQLoads
                |          Set abqLoads = abqFreqStep.Loads

        :rtype: ABQLoads
        """

        return ABQLoads(self.abq_frequency_step.Loads)

    @property
    def maximum_frequency(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaximumFrequency() As short
                | 
                |     Returns or sets maximum frequency value.
                | 
                |     Returns:
                |         The maximum frequency value.
                | 
                |         Example:
                |             This example sets the maximum frequency for
                |             abqFreqStep
                | 
                |              abqFreqStep.MaximumFrequency = 100

        :rtype: int
        """

        return self.abq_frequency_step.MaximumFrequency

    @maximum_frequency.setter
    def maximum_frequency(self, value: int):
        """
        :param int value:
        """

        self.abq_frequency_step.MaximumFrequency = value

    @property
    def minimum_frequency(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MinimumFrequency() As short
                | 
                |     Returns or sets minimum frequency value.
                | 
                |     Returns:
                |         The minimum frequency value.
                | 
                |         Example:
                |             This example sets the minimum frequency for
                |             abqFreqStep
                | 
                |              abqFreqStep.MinimumFrequency = 10

        :rtype: int
        """

        return self.abq_frequency_step.MinimumFrequency

    @minimum_frequency.setter
    def minimum_frequency(self, value: int):
        """
        :param int value:
        """

        self.abq_frequency_step.MinimumFrequency = value

    @property
    def normalization_value(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NormalizationValue() As short
                | 
                |     Returns or sets Normalization Value.
                | 
                |     Returns:
                |         The Normalization Value.
                | 
                |           
                |         Legal values:
                |          1 - Displacement.
                |          2 - Mass.
                |          
                | 
                |         Example:
                |             This example sets Normalization as Displacement
                |             abqFreqStep
                | 
                |              abqFreqStep.NormalizationValue = 1

        :rtype: int
        """

        return self.abq_frequency_step.NormalizationValue

    @normalization_value.setter
    def normalization_value(self, value: int):
        """
        :param int value:
        """

        self.abq_frequency_step.NormalizationValue = value

    @property
    def requested_modes_option(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RequestedModesOption() As short
                | 
                |     Sets or returns the requested modes option.
                | 
                |     Returns:
                |         The option of requested modes.
                | 
                |           
                |         Legal values:
                |          ABQ_ALL - All modes.
                |          ABQ_VALUE - Specify the no of modes to be requested.
                |          
                | 
                |         Example:
                |             This example sets the requested modes option for abqFreqStep job to
                |             every increment.
                | 
                |              abqFreqStep.RequestedModesOption = ABQ_ALL

        :return: enum abq_requested_modes_option
        :rtype: int
        """

        return self.abq_frequency_step.RequestedModesOption

    @requested_modes_option.setter
    def requested_modes_option(self, value: int):
        """
        :param int value: enum abq_requested_modes_option
        """

        self.abq_frequency_step.RequestedModesOption = value

    @property
    def requested_modes_value(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RequestedModesValue() As short
                | 
                |     Returns or sets requested modes value. This is only valid if
                |     RestartRequestOption is ABQ_VALUE
                | 
                |     Returns:
                |         The requested modes value.
                | 
                |         Example:
                |             This example sets the requested modes for
                |             abqFreqStep
                | 
                |              abqFreqStep.RequestedModesValue = 10

        :rtype: int
        """

        return self.abq_frequency_step.RequestedModesValue

    @requested_modes_value.setter
    def requested_modes_value(self, value: int):
        """
        :param int value:
        """

        self.abq_frequency_step.RequestedModesValue = value

    @property
    def residual_mode_req_boolean(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ResidualModeReqBoolean() As boolean
                | 
                |     Returns or sets Residual Mode Request Boolean Value.
                | 
                |     Returns:
                |         The Residual Mode Request Boolean Value.

        :rtype: bool
        """

        return self.abq_frequency_step.ResidualModeReqBoolean

    @residual_mode_req_boolean.setter
    def residual_mode_req_boolean(self, value: bool):
        """
        :param bool value:
        """

        self.abq_frequency_step.ResidualModeReqBoolean = value

    @property
    def sim_architecture_req_boolean(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SIMArchitectureReqBoolean() As boolean
                | 
                |     Returns or sets SIM Architecture Request Boolean Value.
                | 
                |     Returns:
                |         The SIM Architecture Request Boolean Value.

        :rtype: bool
        """

        return self.abq_frequency_step.SIMArchitectureReqBoolean

    @sim_architecture_req_boolean.setter
    def sim_architecture_req_boolean(self, value: bool):
        """
        :param bool value:
        """

        self.abq_frequency_step.SIMArchitectureReqBoolean = value

    def add_residual_mode_region(self, i_product: Product, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddResidualModeRegion(Product iProduct,
                | Reference iSupport)
                | 
                |     Adds the Residual Mode Region.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The CATIAProduct specifying the positioning
                |             object.
                |         iSupport
                |             The CATIAReference specifying the object that is being pointed
                |             to.

        :param Product i_product:
        :param Reference i_support:
        :rtype: None
        """
        return self.abq_frequency_step.AddResidualModeRegion(i_product.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_residual_mode_region'
        # # vba_code = """
        # # Public Function add_residual_mode_region(abq_frequency_step)
        # #     Dim iProduct (2)
        # #     abq_frequency_step.AddResidualModeRegion iProduct
        # #     add_residual_mode_region = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_residual_mode_region_dof(self, i_dof: int, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddResidualModeRegionDOF(short iDOF,
                | short iIndex)
                | 
                |     Adds the Residual Mode Region DOF.
                | 
                |     Parameters:
                | 
                |         iDOF
                |             The DOF.
                |         iIndex
                |             The index at which the DOF is being set.

        :param int i_dof:
        :param int i_index:
        :rtype: None
        """
        return self.abq_frequency_step.AddResidualModeRegionDOF(i_dof, i_index)

    def __repr__(self):
        return f'ABQFrequencyStep(name="{self.name}")'
