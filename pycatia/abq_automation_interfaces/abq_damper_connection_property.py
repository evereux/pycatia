#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_property import ABQProperty
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.axis_system import AxisSystem


class ABQDamperConnectionProperty(ABQProperty):
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
                |                         ABQDamperConnectionProperty
                | 
                | Represents an Abaqus Damper connection property (ABQDamper)
                | object.
                | Role:Access an Abaqus Damper connection property object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_damper_connection_property = com_object

    @property
    def axis_sys(self) -> AxisSystem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Axis_sys() As AxisSystem
                | 
                |     Sets or returns the axis system in the Damper connection
                |     property.
                | 
                |     Returns:
                |         The object of axis system.

        :rtype: AxisSystem
        """

        return AxisSystem(self.abq_damper_connection_property.Axis_sys)

    @axis_sys.setter
    def axis_sys(self, value: AxisSystem):
        """
        :param AxisSystem value:
        """

        self.abq_damper_connection_property.Axis_sys = value

    @property
    def damper_def(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DamperDef() As SpringDef_Type
                | 
                |     Sets or returns the definition of Damper.
                | 
                |     Returns:
                |         the Definition of Damper.
                | 
                |         Legal values:
                | 
                |         ABQ_LINE
                |         ABQ_NON_LINEAR

        :return: enum spring_def_type
        :rtype: int
        """

        return self.abq_damper_connection_property.DamperDef

    @damper_def.setter
    def damper_def(self, value: int):
        """
        :param int value: enum spring_def_type
        """

        self.abq_damper_connection_property.DamperDef = value

    @property
    def damper_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DamperType() As SpringType_Type
                | 
                |     Sets or returns the type of Damper.
                | 
                |     Returns:
                |         The type of Damper.
                | 
                |         Legal values:
                | 
                |         AXIAL
                |         GENERAL

        :return: enum spring_type_type
        :rtype: int
        """

        return self.abq_damper_connection_property.DamperType

    @damper_type.setter
    def damper_type(self, value: int):
        """
        :param int value: enum spring_type_type
        """

        self.abq_damper_connection_property.DamperType = value

    def add_support_from_reference(self, i_reference: Reference, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromReference(Reference iReference,
                | Reference iSupport)
                | 
                |     Adds support to the Damper connection property.
                | 
                |     Parameters:
                | 
                |         iReference
                |             The CATIA Reference specifying the region to which the Damper
                |             connection property is applied.
                |         iSupport
                |             The CATIA Reference specifying the region to which the Damper
                |             connection property is applied.
                | 
                |             Refer: CATIAReference

        :param Reference i_reference:
        :param Reference i_support:
        :rtype: None
        """
        return self.abq_damper_connection_property.AddSupportFromReference(i_reference.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_reference'
        # # vba_code = """
        # # Public Function add_support_from_reference(abq_damper_connection_property)
        # #     Dim iReference (2)
        # #     abq_damper_connection_property.AddSupportFromReference iReference
        # #     add_support_from_reference = iReference
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_linear_damping(self, i_dof: int) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLinearDamping(SpringDof_Type iDof) As double
                | 
                |     Gets the linear damping value of the Damper given the degree of
                |     freedom.
                | 
                |     Parameters:
                | 
                |         iDof
                |             The degree of freedom for which damping is asked.
                | 
                | 
                |             Legal values:
                | 
                |             U1_DOF
                |             U2_DOF
                |             U3_DOF
                |             UR1_DOF
                |             UR2_DOF
                |             UR3_DOF
                | 
                |         oDampingValue
                |             The Dampingvalue.

        :param int i_dof: enum spring_dof_type
        :rtype: float
        """
        return self.abq_damper_connection_property.GetLinearDamping(i_dof)

    def get_non_linear_damping(self, i_dof: int, o_force_array: tuple, o_velocity_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetNonLinearDamping(SpringDof_Type iDof,
                | CATSafeArrayVariant oForceArray,
                | CATSafeArrayVariant oVelocityArray)
                | 
                |     Gets the non-linear damping value of the Damper in the form of array, given
                |     the degree of freedom.
                | 
                |     Parameters:
                | 
                |         iDof
                |             The degree of freedom for which damping is asked.
                | 
                | 
                |             Legal values:
                | 
                |             U1_DOF
                |             U2_DOF
                |             U3_DOF
                |             UR1_DOF
                |             UR2_DOF
                |             UR3_DOF
                | 
                |         oForceArray
                |             The array of force values.
                |         oVelocityArray
                |             The array of velocity values.
                | 
                |             Refer: CATSafeArrayVariant

        :param int i_dof: enum spring_dof_type
        :param tuple o_force_array:
        :param tuple o_velocity_array:
        :rtype: None
        """
        return self.abq_damper_connection_property.GetNonLinearDamping(i_dof, o_force_array, o_velocity_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_non_linear_damping'
        # # vba_code = """
        # # Public Function get_non_linear_damping(abq_damper_connection_property)
        # #     Dim iDof (2)
        # #     abq_damper_connection_property.GetNonLinearDamping iDof
        # #     get_non_linear_damping = iDof
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def read_damping_data_from_file(self, i_dof: int, i_file_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ReadDampingDataFromFile(SpringDof_Type iDof,
                | CATBSTR iFileName)
                | 
                |     Reads damping data from a text file for a damper connection
                |     property.
                | 
                |     Parameters:
                | 
                |         iDof
                |             The degree of freedom for which damping data is
                |             asked.
                | 
                | 
                |             Legal values:
                | 
                |             U1_DOF
                |             U2_DOF
                |             U3_DOF
                |             UR1_DOF
                |             UR2_DOF
                |             UR3_DOF
                | 
                |         iFileName
                |             The complete path of the text file which contains the damping
                |             data.

        :param int i_dof: enum spring_dof_type
        :param str i_file_name:
        :rtype: None
        """
        return self.abq_damper_connection_property.ReadDampingDataFromFile(i_dof, i_file_name)

    def remove_axis_system(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveAxisSystem()

        :rtype: None
        """
        return self.abq_damper_connection_property.RemoveAxisSystem()

    def remove_dof(self, i_dof: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveDof(SpringDof_Type iDof)
                | 
                |     Unsets the linear damping value of the Damper for given degree of
                |     freedom.
                | 
                |     Parameters:
                | 
                |         iDof
                |             The degree of freedom for which damping is set.
                | 
                | 
                |             Legal values:
                | 
                |             U1_DOF
                |             U2_DOF
                |             U3_DOF
                |             UR1_DOF
                |             UR2_DOF
                |             UR3_DOF

        :param int i_dof: enum spring_dof_type
        :rtype: None
        """
        return self.abq_damper_connection_property.RemoveDof(i_dof)

    def set_linear_damping(self, i_dof: int, i_damping_value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLinearDamping(SpringDof_Type iDof,
                | double iDampingValue)
                | 
                |     Sets the linear damping value of the Damper given the degree of
                |     freedom.
                | 
                |     Parameters:
                | 
                |         iDof
                |             The degree of freedom for which damping is set.
                | 
                | 
                |             Legal values:
                | 
                |             U1_DOF
                |             U2_DOF
                |             U3_DOF
                |             UR1_DOF
                |             UR2_DOF
                |             UR3_DOF
                | 
                |         iDampingValue
                |             The Dampingvalue.

        :param int i_dof: enum spring_dof_type
        :param float i_damping_value:
        :rtype: None
        """
        return self.abq_damper_connection_property.SetLinearDamping(i_dof, i_damping_value)

    def set_non_linear_damping(self, i_dof: int, i_force_array: tuple, i_velocity_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetNonLinearDamping(SpringDof_Type iDof,
                | CATSafeArrayVariant iForceArray,
                | CATSafeArrayVariant iVelocityArray)
                | 
                |     Sets the non-linear damping value of the Damper in the form of array, given
                |     the degree of freedom.
                | 
                |     Parameters:
                | 
                |         iDof
                |             The degree of freedom for which damping is asked.
                | 
                | 
                |             Legal values:
                | 
                |             U1_DOF
                |             U2_DOF
                |             U3_DOF
                |             UR1_DOF
                |             UR2_DOF
                |             UR3_DOF
                | 
                |         iForceArray
                |             The array of force values.
                |         iVelocityArray
                |             The array of displacement values.
                |             The value in velocity array must be greater than previous value
                |             .
                | 
                |             Refer: CATSafeArrayVariant

        :param int i_dof: enum spring_dof_type
        :param tuple i_force_array:
        :param tuple i_velocity_array:
        :rtype: None
        """
        return self.abq_damper_connection_property.SetNonLinearDamping(i_dof, i_force_array, i_velocity_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_non_linear_damping'
        # # vba_code = """
        # # Public Function set_non_linear_damping(abq_damper_connection_property)
        # #     Dim iDof (2)
        # #     abq_damper_connection_property.SetNonLinearDamping iDof
        # #     set_non_linear_damping = iDof
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQDamperConnectionProperty(name="{self.name}")'
