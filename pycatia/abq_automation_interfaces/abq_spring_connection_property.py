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


class ABQSpringConnectionProperty(ABQProperty):
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
                |                         ABQSpringConnectionProperty
                | 
                | Represents an Abaqus spring connection property (ABQSpring)
                | object.
                | Role:Access an Abaqus spring connection property object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_spring_connection_property = com_object

    @property
    def axis_sys(self) -> AxisSystem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Axis_sys() As AxisSystem
                | 
                |     Sets or returns the axis system in the spring connection
                |     property.
                | 
                |     Returns:
                |         The object of axis system.

        :rtype: AxisSystem
        """

        return AxisSystem(self.abq_spring_connection_property.Axis_sys)

    @axis_sys.setter
    def axis_sys(self, value: AxisSystem):
        """
        :param AxisSystem value:
        """

        self.abq_spring_connection_property.Axis_sys = value

    @property
    def spring_definition(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SpringDef() As SpringDef_Type
                | 
                |     Sets or returns the definition of spring.
                | 
                |     Returns:
                |         the Definition of spring.
                | 
                |         Legal values:
                |         ABQ_LINE
                |         ABQ_NON_LINEAR

        :rtype: int
        """

        return self.abq_spring_connection_property.SpringDef

    @spring_definition.setter
    def spring_definition(self, value: int):
        """
        :param int value:
        """

        self.abq_spring_connection_property.SpringDef = value

    @property
    def spring_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SpringType() As SpringType_Type
                | 
                |     Sets or returns the type of spring.
                | 
                |     Returns:
                |         The type of spring.
                | 
                |         Legal values:
                |         AXIAL
                |         GENERAL

        :return: enum spring_type_type
        :rtype: int
        """

        return self.abq_spring_connection_property.SpringType

    @spring_type.setter
    def spring_type(self, value: int):
        """
        :param int value: enum spring_type_type
        """

        self.abq_spring_connection_property.SpringType = value

    def add_support_from_reference(self, i_reference: Reference, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromReference(Reference iReference,
                | Reference iSupport)
                | 
                |     Adds support to the spring connection property.
                | 
                |     Parameters:
                | 
                |         iReference
                |             The CATIA Reference specifying the region to which the spring
                |             connection property is applied.
                |         iSupport
                |             The CATIA Reference specifying the region to which the spring
                |             connection property is applied.
                | 
                |             Refer: CATIAReference

        :param Reference i_reference:
        :param Reference i_support:
        :rtype: None
        """
        return self.abq_spring_connection_property.AddSupportFromReference(i_reference.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_reference'
        # # vba_code = """
        # # Public Function add_support_from_reference(abq_spring_connection_property)
        # #     Dim iReference (2)
        # #     abq_spring_connection_property.AddSupportFromReference iReference
        # #     add_support_from_reference = iReference
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_linear_stiffness(self, i_dof: int) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLinearStiffness(SpringDof_Type iDof) As double
                | 
                |     Gets the linear stiffness of the spring given the degree of
                |     freedom.
                | 
                |     Parameters:
                | 
                |         iDof
                |             The degree of freedom for which stiffness is
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
                |         oStiffnessValue
                |             The stiffnessvalue.

        :param int i_dof: enum spring_dof_type
        :rtype: float
        """
        return self.abq_spring_connection_property.GetLinearStiffness(i_dof)

    def get_non_linear_stiffness(self, i_dof: int, o_force_array: tuple, o_disp_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetNonLinearStiffness(SpringDof_Type iDof,
                | CATSafeArrayVariant oForceArray,
                | CATSafeArrayVariant oDispArray)
                | 
                |     Gets the non-linear stiffness of the spring in the form of array, given the
                |     degree of freedom.
                | 
                |     Parameters:
                | 
                |         iDof
                |             The degree of freedom for which stiffness is
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
                |         oForceArray
                |             The array of force values.
                |         oDispArray
                |             The array of displacement values.
                | 
                |             Refer: CATSafeArrayVariant

        :param int i_dof: enum spring_dof_type
        :param tuple o_force_array:
        :param tuple o_disp_array:
        :rtype: None
        """
        return self.abq_spring_connection_property.GetNonLinearStiffness(i_dof, o_force_array, o_disp_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_non_linear_stiffness'
        # # vba_code = """
        # # Public Function get_non_linear_stiffness(abq_spring_connection_property)
        # #     Dim iDof (2)
        # #     abq_spring_connection_property.GetNonLinearStiffness iDof
        # #     get_non_linear_stiffness = iDof
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def read_stiffness_data_from_file(self, i_dof: int, i_file_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ReadStiffnessDataFromFile(SpringDof_Type iDof,
                | CATBSTR iFileName)
                | 
                |     Reads stiffness data from a text file for a spring connection
                |     property.
                | 
                |     Parameters:
                | 
                |         iDof
                |             The degree of freedom for which stiffness is
                |             asked.
                | 
                |             Legal values:
                |             U1_DOF
                |             U2_DOF
                |             U3_DOF
                |             UR1_DOF
                |             UR2_DOF
                |             UR3_DOF
                | 
                |         iFileName
                |             The complete path of the text file which contains the stiffness
                |             data.

        :param int i_dof: enum spring_dof_type
        :param str i_file_name:
        :rtype: None
        """
        return self.abq_spring_connection_property.ReadStiffnessDataFromFile(i_dof, i_file_name)

    def remove_axis_system(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveAxisSystem()

        :rtype: None
        """
        return self.abq_spring_connection_property.RemoveAxisSystem()

    def remove_dof(self, i_dof: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveDof(SpringDof_Type iDof)
                | 
                |     Unsets the stiffness of the spring for given degree of
                |     freedom.
                | 
                |     Parameters:
                | 
                |         iDof
                |             The degree of freedom for which stiffness is set.
                | 
                |             Legal values:
                |             U1_DOF
                |             U2_DOF
                |             U3_DOF
                |             UR1_DOF
                |             UR2_DOF
                |             UR3_DOF

        :param int i_dof: enum spring_dof_type
        :rtype: None
        """
        return self.abq_spring_connection_property.RemoveDof(i_dof)

    def set_linear_stiffness(self, i_dof: int, i_stiffness_value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLinearStiffness(SpringDof_Type iDof,
                | double iStiffnessValue)
                | 
                |     Sets the linear stiffness of the spring given the degree of
                |     freedom.
                | 
                |     Parameters:
                | 
                |         iDof
                |             The degree of freedom for which stiffness is set.
                | 
                |             Legal values:
                |             U1_DOF
                |             U2_DOF
                |             U3_DOF
                |             UR1_DOF
                |             UR2_DOF
                |             UR3_DOF
                | 
                |         iStiffnessValue
                |             The stiffnessvalue.

        :param int i_dof: enum spring_dof_type
        :param float i_stiffness_value:
        :rtype: None
        """
        return self.abq_spring_connection_property.SetLinearStiffness(i_dof, i_stiffness_value)

    def set_non_linear_stiffness(self, i_dof: int, i_force_array: tuple, i_disp_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetNonLinearStiffness(SpringDof_Type iDof,
                | CATSafeArrayVariant iForceArray,
                | CATSafeArrayVariant iDispArray)
                | 
                |     Sets the non-linear stiffness of the spring in the form of array, given the
                |     degree of freedom.
                | 
                |     Parameters:
                | 
                |         iDof
                |             The degree of freedom for which stiffness is
                |             asked.
                |
                |             Legal values:
                |             U1_DOF
                |             U2_DOF
                |             U3_DOF
                |             UR1_DOF
                |             UR2_DOF
                |             UR3_DOF
                | 
                |         iForceArray
                |             The array of force values.
                |         iDispArray
                |             The array of displacement values.
                |             The value in displacement array must be greater than previous value.
                | 
                |             Refer: CATSafeArrayVariant

        :param int i_dof: enum spring_dof_type
        :param tuple i_force_array:
        :param tuple i_disp_array:
        :rtype: None
        """
        return self.abq_spring_connection_property.SetNonLinearStiffness(i_dof, i_force_array, i_disp_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_non_linear_stiffness'
        # # vba_code = """
        # # Public Function set_non_linear_stiffness(abq_spring_connection_property)
        # #     Dim iDof (2)
        # #     abq_spring_connection_property.SetNonLinearStiffness iDof
        # #     set_non_linear_stiffness = iDof
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQSpringConnectionProperty(name="{self.name}")'
