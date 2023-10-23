#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abqiaabq_steady_state_lin_dyn_step_basic_vb import \
    ABQIAABQSteadyStateLinDynStepBasicVB


class ABQIAABQSteadyStateLinDynStepModalVB(ABQIAABQSteadyStateLinDynStepBasicVB):
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
                |                         ABQAutomationItf.ABQIAABQSteadyStateLinDynStepBasicVB
                |                            ABQIAABQSteadyStateLinDynStepModalVB
                | 
                | Interface representing xxx.
                | 
                | Role: Components that implement ABQIAABQSteadyStateLinDynStepModal are
                | ...
                | 
                | Do not use the ABQIAABQSteadyStateLinDynStepModal interface for such and such
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abqiaabq_steady_state_lin_dyn_step_modal_vb = com_object

    @property
    def use_composite_damping_data(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UseCompositeDampingData() As boolean
                | 
                |     Sets or returns if the composite damping data is ued.
                | 
                |     Returns:
                |         A boolean specifying whether the composite damping data is ued.

        :rtype: bool
        """

        return self.abqiaabq_steady_state_lin_dyn_step_modal_vb.UseCompositeDampingData

    @use_composite_damping_data.setter
    def use_composite_damping_data(self, value: bool):
        """
        :param bool value:
        """

        self.abqiaabq_steady_state_lin_dyn_step_modal_vb.UseCompositeDampingData = value

    @property
    def use_direct_damping_data(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UseDirectDampingData() As boolean
                | 
                |     Sets or returns if the direct damping data is ued.
                | 
                |     Returns:
                |         A boolean specifying whether the direct damping data is ued.

        :rtype: bool
        """

        return self.abqiaabq_steady_state_lin_dyn_step_modal_vb.UseDirectDampingData

    @use_direct_damping_data.setter
    def use_direct_damping_data(self, value: bool):
        """
        :param bool value:
        """

        self.abqiaabq_steady_state_lin_dyn_step_modal_vb.UseDirectDampingData = value

    @property
    def use_rayleigh_damping_data(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UseRayleighDampingData() As boolean
                | 
                |     Sets or returns if the rayleigh damping data is ued.
                | 
                |     Returns:
                |         A boolean specifying whether the rayleigh damping data is ued.

        :rtype: bool
        """

        return self.abqiaabq_steady_state_lin_dyn_step_modal_vb.UseRayleighDampingData

    @use_rayleigh_damping_data.setter
    def use_rayleigh_damping_data(self, value: bool):
        """
        :param bool value:
        """

        self.abqiaabq_steady_state_lin_dyn_step_modal_vb.UseRayleighDampingData = value

    @property
    def use_structural_damping_data(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UseStructuralDampingData() As boolean
                | 
                |     Sets or returns if the structural damping data is ued.
                | 
                |     Returns:
                |         A boolean specifying whether the structural damping data is ued.

        :rtype: bool
        """

        return self.abqiaabq_steady_state_lin_dyn_step_modal_vb.UseStructuralDampingData

    @use_structural_damping_data.setter
    def use_structural_damping_data(self, value: bool):
        """
        :param bool value:
        """

        self.abqiaabq_steady_state_lin_dyn_step_modal_vb.UseStructuralDampingData = value

    def add_composite_damping_data_table(self, i_column1: tuple, i_column2: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddCompositeDampingDataTable(CATSafeArrayVariant
                | iColumn1,
                | CATSafeArrayVariant iColumn2)
                | 
                |     Adds a composite damping data over ranges of Modes or Frequencies The
                |     number of values in both the parameters must match. If either list contains
                |     extra values, the extra values are discarded. Valid only for damping over
                |     ranges of Modes.
                | 
                |     Parameters:
                | 
                |         iColumn1
                |             The list of start modes.
                |         iColumn2
                |             The list of end modes.

        :param tuple i_column1:
        :param tuple i_column2:
        :rtype: None
        """
        return self.abqiaabq_steady_state_lin_dyn_step_modal_vb.AddCompositeDampingDataTable(i_column1, i_column2)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_composite_damping_data_table'
        # # vba_code = """
        # # Public Function add_composite_damping_data_table(abqiaabq_steady_state_lin_dyn_step_modal_vb)
        # #     Dim iColumn1 (2)
        # #     abqiaabq_steady_state_lin_dyn_step_modal_vb.AddCompositeDampingDataTable iColumn1
        # #     add_composite_damping_data_table = iColumn1
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_direct_damping_data_table(
            self,
            i_damping_range: str,
            i_column1: tuple,
            i_column2: tuple,
            i_column3: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddDirectDampingDataTable(CATBSTR iDampingRange,
                | CATSafeArrayVariant iColumn1,
                | CATSafeArrayVariant iColumn2,
                | CATSafeArrayVariant iColumn3)
                | 
                |     Adds a direct damping data over ranges of Modes or Frequencies The number
                |     of values in all the three of the parameters must match. If either list
                |     contains extra values, the extra values are discarded.
                | 
                |     Parameters:
                | 
                |         iDampingRange
                |             The range over which damping is defined.
                | 
                |               
                |             Legal values:
                |              MODES.
                |              FREQUENCIES.
                |              
                | 
                |         iColumn1
                |             For daming range = MODES - The list of start modes.
                |             For daming range = FREQUENCIES - The list of frequencies.
                |         iColumn2
                |             For daming range = MODES - The list of end modes.
                |             For daming range = FREQUENCIES - The list of critical damping fraction.
                |         iColumn3
                |             For daming range = MODES - The list of critical damping fraction.
                |             For daming range = FREQUENCIES - iColumn3 will be ignored if the damping range is FREQUENCIES.

        :param str i_damping_range:
        :param tuple i_column1:
        :param tuple i_column2:
        :param tuple i_column3:
        :rtype: None
        """
        return self.abqiaabq_steady_state_lin_dyn_step_modal_vb.AddDirectDampingDataTable(
            i_damping_range,
            i_column1,
            i_column2,
            i_column3
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_direct_damping_data_table'
        # # vba_code = """
        # # Public Function add_direct_damping_data_table(abqiaabq_steady_state_lin_dyn_step_modal_vb)
        # #     Dim iDampingRange (2)
        # #     abqiaabq_steady_state_lin_dyn_step_modal_vb.AddDirectDampingDataTable iDampingRange
        # #     add_direct_damping_data_table = iDampingRange
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_rayleigh_damping_data_table(
            self,
            i_damping_range: str,
            i_column1:
            tuple,
            i_column2: tuple,
            i_column3: tuple,
            i_column4: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddRayleighDampingDataTable(CATBSTR iDampingRange,
                | CATSafeArrayVariant iColumn1,
                | CATSafeArrayVariant iColumn2,
                | CATSafeArrayVariant iColumn3,
                | CATSafeArrayVariant iColumn4)
                | 
                |     Adds a rayleigh damping data over ranges of Modes or Frequencies The number
                |     of values in all the four of the parameters must match. If either list contains
                |     extra values, the extra values are discarded.
                | 
                |     Parameters:
                | 
                |         iDampingRange
                |             The range over which damping is defined.
                | 
                |               
                |             Legal values:
                |              MODES.
                |              FREQUENCIES.
                |              
                | 
                |         iColumn1
                |             For daming range = MODES - The list of start modes.
                |             For daming range = FREQUENCIES - The list of frequencies.
                |         iColumn2
                |             For daming range = MODES - The list of end modes.
                |             For daming range = FREQUENCIES - The list of alpha coefficients.
                |         iColumn3
                |             For daming range = MODES - The list of alpha coefficients.
                |             For daming range = FREQUENCIES - The list of beta coefficients.
                |         iColumn4
                |             For daming range = MODES - The list of beta coefficients.
                |             For daming range = FREQUENCIES - iColumn4 will be ignored if the damping range is FREQUENCIES.

        :param str i_damping_range:
        :param tuple i_column1:
        :param tuple i_column2:
        :param tuple i_column3:
        :param tuple i_column4:
        :rtype: None
        """
        return self.abqiaabq_steady_state_lin_dyn_step_modal_vb.AddRayleighDampingDataTable(
            i_damping_range,
            i_column1,
            i_column2,
            i_column3,
            i_column4
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_rayleigh_damping_data_table'
        # # vba_code = """
        # # Public Function add_rayleigh_damping_data_table(abqiaabq_steady_state_lin_dyn_step_modal_vb)
        # #     Dim iDampingRange (2)
        # #     abqiaabq_steady_state_lin_dyn_step_modal_vb.AddRayleighDampingDataTable iDampingRange
        # #     add_rayleigh_damping_data_table = iDampingRange
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_structural_damping_data_table(
            self,
            i_damping_range: str,
            i_column1: tuple,
            i_column2: tuple,
            i_column3: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddStructuralDampingDataTable(CATBSTR iDampingRange,
                | CATSafeArrayVariant iColumn1,
                | CATSafeArrayVariant iColumn2,
                | CATSafeArrayVariant iColumn3)
                | 
                |     Adds a structural damping data over ranges of Modes or Frequencies The
                |     number of values in all the three of the parameters must match. If either list
                |     contains extra values, the extra values are discarded.
                | 
                |     Parameters:
                | 
                |         iDampingRange
                |             The range over which damping is defined.
                |
                |             Legal values:
                |              MODES.
                |              FREQUENCIES.
                |         iColumn1
                |             For daming range = MODES - The list of start modes.
                |             For daming range = FREQUENCIES - The list of frequencies.
                |         iColumn2
                |             For daming range = MODES - The list of end modes.
                |             For daming range = FREQUENCIES - The list of damping constant.
                |         iColumn3
                |             For daming range = MODES - The list of damping constant.
                |             For daming range = FREQUENCIES - iColumn3 will be ignored if the damping range is FREQUENCIES.

        :param str i_damping_range:
        :param tuple i_column1:
        :param tuple i_column2:
        :param tuple i_column3:
        :rtype: None
        """
        return self.abqiaabq_steady_state_lin_dyn_step_modal_vb.AddStructuralDampingDataTable(
            i_damping_range,
            i_column1,
            i_column2,
            i_column3
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_structural_damping_data_table'
        # # vba_code = """
        # # Public Function add_structural_damping_data_table(abqiaabq_steady_state_lin_dyn_step_modal_vb)
        # #     Dim iDampingRange (2)
        # #     abqiaabq_steady_state_lin_dyn_step_modal_vb.AddStructuralDampingDataTable iDampingRange
        # #     add_structural_damping_data_table = iDampingRange
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQIAABQSteadyStateLinDynStepModalVB(name="{self.name}")'
