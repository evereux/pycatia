#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_property import ABQProperty


class ABQMechConnBehavior(ABQProperty):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQProperty
                |                         ABQMechConnBehavior
                | 
                | Represents an Abaqus mechanical connection behavior (ABQMechConnBehavior)
                | object.
                | Role: Access an Abaqus mechanical connection behaviour object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_mech_conn_behavior = com_object

    @property
    def allow_separation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AllowSeparation() As boolean
                | 
                |     Sets or returns the seperation status for the hard contact pressure
                |     overclosure.
                | 
                |     Returns:
                |         A boolean specifying whether seperation status is on or
                |         off.

        :rtype: bool
        """

        return self.abq_mech_conn_behavior.AllowSeparation

    @allow_separation.setter
    def allow_separation(self, value: bool):
        """
        :param bool value:
        """

        self.abq_mech_conn_behavior.AllowSeparation = value

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

        return self.abq_mech_conn_behavior.ApplyUserSubroutine

    @apply_user_subroutine.setter
    def apply_user_subroutine(self, value: bool):
        """
        :param bool value:
        """

        self.abq_mech_conn_behavior.ApplyUserSubroutine = value

    @property
    def augmented_lagrange(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AugmentedLagrange() As boolean
                | 
                |     Sets or returns the augmented lagrange formulation in a mechanical
                |     connection.
                | 
                |     Returns:
                |         A boolean specifying whether augmented lagrange formulation is
                |         applied.

        :rtype: bool
        """

        return self.abq_mech_conn_behavior.AugmentedLagrange

    @augmented_lagrange.setter
    def augmented_lagrange(self, value: bool):
        """
        :param bool value:
        """

        self.abq_mech_conn_behavior.AugmentedLagrange = value

    @property
    def clearance_contact_pressure_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ClearanceContactPressureValue() As double
                | 
                |     Sets or returns the clearance at which contact pressure is zero in a
                |     mechanical connection.
                | 
                |     Returns:
                |         clearance at which contact pressure is zero.

        :rtype: float
        """

        return self.abq_mech_conn_behavior.ClearanceContactPressureValue

    @clearance_contact_pressure_value.setter
    def clearance_contact_pressure_value(self, value: float):
        """
        :param float value:
        """

        self.abq_mech_conn_behavior.ClearanceContactPressureValue = value

    @property
    def contact_stiffness(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ContactStiffness() As ContactStiffness_Type
                | 
                |     Sets or returns the contact stiffness type hard contact pressure
                |     overclosure.
                | 
                |     Returns:
                |         The contact stiffness
                | 
                |         Legal values:
                | 
                |         DEFAULT
                |         STIFF_VALUE

        :rtype: int
        """

        return self.abq_mech_conn_behavior.ContactStiffness

    @contact_stiffness.setter
    def contact_stiffness(self, value: int):
        """
        :param int value:
        """

        self.abq_mech_conn_behavior.ContactStiffness = value

    @property
    def contact_stiffness_scale_factor_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ContactStiffnessScaleFactorValue() As double
                | 
                |     Sets or returns the contact stiffness scale factor value in a mechanical
                |     connection.
                | 
                |     Returns:
                |         contact stiffness scale factor value.

        :rtype: float
        """

        return self.abq_mech_conn_behavior.ContactStiffnessScaleFactorValue

    @contact_stiffness_scale_factor_value.setter
    def contact_stiffness_scale_factor_value(self, value: float):
        """
        :param float value:
        """

        self.abq_mech_conn_behavior.ContactStiffnessScaleFactorValue = value

    @property
    def contact_stiffness_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ContactStiffnessValue() As double
                | 
                |     Sets or returns the contact stiffness value for hard contact pressure
                |     overclosure.
                | 
                |     Returns:
                |         The stiffness value.

        :rtype: float
        """

        return self.abq_mech_conn_behavior.ContactStiffnessValue

    @contact_stiffness_value.setter
    def contact_stiffness_value(self, value: float):
        """
        :param float value:
        """

        self.abq_mech_conn_behavior.ContactStiffnessValue = value

    @property
    def description(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Description() As CATBSTR
                | 
                |     Sets or returns the description.
                | 
                |     Returns:
                |         The description of the step.

        :rtype: str
        """

        return self.abq_mech_conn_behavior.Description

    @description.setter
    def description(self, value: str):
        """
        :param str value:
        """

        self.abq_mech_conn_behavior.Description = value

    @property
    def formulation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Formulation() As Formulation_Type
                | 
                |     Sets or returns the formulation in a mechanical
                |     connection.
                | 
                |     Returns:
                |         The formulation.
                | 
                |         Legal values:
                | 
                |         FRICTIONLESS
                |         PENALTY

        :return: enum formulation_type
        :rtype: int
        """

        return self.abq_mech_conn_behavior.Formulation

    @formulation.setter
    def formulation(self, value: int):
        """
        :param int value: enum formulation_type
        """

        self.abq_mech_conn_behavior.Formulation = value

    @property
    def friction_coefficient(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FrictionCoefficient() As double
                | 
                |     Sets or returns the friction coefficient if the formulation is
                |     PENALTY.
                | 
                |     Returns:
                |         The friction coefficient.

        :rtype: float
        """

        return self.abq_mech_conn_behavior.FrictionCoefficient

    @friction_coefficient.setter
    def friction_coefficient(self, value: float):
        """
        :param float value:
        """

        self.abq_mech_conn_behavior.FrictionCoefficient = value

    @property
    def max_stiffness(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxStiffness() As MaxStiffness_Type
                | 
                |     Sets or returns the contact stiffness type hard contact pressure
                |     overclosure.
                | 
                |     Returns:
                |         The contact stiffness
                | 
                |         Legal values:
                | 
                |         DEFAULT
                |         STIFF_VALUE

        :return: enum max_stiffness_type
        :rtype: int
        """

        return self.abq_mech_conn_behavior.MaxStiffness

    @max_stiffness.setter
    def max_stiffness(self, value: int):
        """
        :param int value: enum max_stiffness_type
        """

        self.abq_mech_conn_behavior.MaxStiffness = value

    @property
    def max_stiffness_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxStiffnessValue() As double
                | 
                |     Sets or returns the max stiffness value for mechanical
                |     connection.
                | 
                |     Returns:
                |         The stiffness value.

        :rtype: float
        """

        return self.abq_mech_conn_behavior.MaxStiffnessValue

    @max_stiffness_value.setter
    def max_stiffness_value(self, value: float):
        """
        :param float value:
        """

        self.abq_mech_conn_behavior.MaxStiffnessValue = value

    @property
    def penalty_method(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PenaltyMethod() As boolean
                | 
                |     Sets or returns the penalty method formulation in a mechanical
                |     connection.
                | 
                |     Returns:
                |         A boolean specifying whether penalty method formulation is applied.

        :rtype: bool
        """

        return self.abq_mech_conn_behavior.PenaltyMethod

    @penalty_method.setter
    def penalty_method(self, value: bool):
        """
        :param bool value:
        """

        self.abq_mech_conn_behavior.PenaltyMethod = value

    @property
    def pressure_overclosure(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PressureOverclosure() As PressureOverclosure_Type
                | 
                |     Sets or returns the pressure overclosure in a mechanical
                |     connection.
                | 
                |     Returns:
                |         The pressure overclosure.
                | 
                |         Legal values:
                | 
                |         HARD
                |         EXPONENTIAL
                |         LINEAR
                |         TABULAR

        :return: enum pressure_overclosure_type
        :rtype: int
        """

        return self.abq_mech_conn_behavior.PressureOverclosure

    @pressure_overclosure.setter
    def pressure_overclosure(self, value: int):
        """
        :param int value: enum pressure_overclosure_type
        """

        self.abq_mech_conn_behavior.PressureOverclosure = value

    def add_pressure_overclosure_table(self, i_pressure: tuple, i_overclosure: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddPressureOverclosureTable(CATSafeArrayVariant
                | iPressure,
                | CATSafeArrayVariant iOverclosure)
                | 
                |     Adds a list of tabular pressure overclosure in the connection behavior. The
                |     number of values in both of the parameters should match. If either list
                |     contains extra values, the extra values are discarded.
                | 
                |     Parameters:
                | 
                |         iPressure
                |             The list of pressure values.
                |         iOverclosure
                |             The list of overclosures.

        :param tuple i_pressure:
        :param tuple i_overclosure:
        :rtype: None
        """
        return self.abq_mech_conn_behavior.AddPressureOverclosureTable(i_pressure, i_overclosure)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_pressure_overclosure_table'
        # # vba_code = """
        # # Public Function add_pressure_overclosure_table(abq_mech_conn_behavior)
        # #     Dim iPressure (2)
        # #     abq_mech_conn_behavior.AddPressureOverclosureTable iPressure
        # #     add_pressure_overclosure_table = iPressure
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_pressure_overclosure_table(self, o_pressure: tuple, o_overclosure: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetPressureOverclosureTable(CATSafeArrayVariant
                | oPressure,
                | CATSafeArrayVariant oOverclosure)
                | 
                |     Returns a list of tabular pressure overclosure in connection
                |     behavior.
                | 
                |     Parameters:
                | 
                |         oPressure
                |             The list of pressure values.
                |         oOverclosure
                |             The list of overclosures.

        :param tuple o_pressure:
        :param tuple o_overclosure:
        :rtype: None
        """
        return self.abq_mech_conn_behavior.GetPressureOverclosureTable(o_pressure, o_overclosure)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_pressure_overclosure_table'
        # # vba_code = """
        # # Public Function get_pressure_overclosure_table(abq_mech_conn_behavior)
        # #     Dim oPressure (2)
        # #     abq_mech_conn_behavior.GetPressureOverclosureTable oPressure
        # #     get_pressure_overclosure_table = oPressure
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQMechConnBehavior(name="{self.name}")'
