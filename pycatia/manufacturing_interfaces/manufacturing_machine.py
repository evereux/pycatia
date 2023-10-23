#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingMachine(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingMachine
                | 
                | Machine in machining domain.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_machine = com_object

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Comment() As CATBSTR (Read Only)
                | 
                |     Return the Comment of a Machine.
                | 
                |     Example:
                |         The following example return the comment MachineComment of to the
                |         manufacturing Machine CurrentMachine
                | 
                |          MachineComment = CurrentMachine.Comment

        :rtype: str
        """

        return self.manufacturing_machine.Comment

    @property
    def machine_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MachineType() As CATBSTR (Read Only)
                | 
                |     Return the Type of a Machine.
                | 
                |     Example:
                |         The following example return the type MachineType of to the
                |         manufacturing Machine CurrentMachine
                | 
                |          MachineType = CurrentMachine.Type

        :rtype: str
        """

        return self.manufacturing_machine.MachineType

    @property
    def number_of_attributes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumberOfAttributes() As short (Read Only)
                | 
                |     Gives the number of attributes of a ManufacturingMachine.
                | 
                |     Example:
                |         The following example returns the Number of attributes of the
                |         ManufacturingMachine CurrentMachine
                | 
                |          Number = CurrentMachine.NumberOfAttributes

        :rtype: int
        """

        return self.manufacturing_machine.NumberOfAttributes

    @property
    def number_of_numerical_control_attributes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumberOfNumericalControlAttributes() As short (Read
                | Only)
                | 
                |     This property returns the number of Numerical Control attributes of a
                |     Manufacturing Machine.

        :rtype: int
        """

        return self.manufacturing_machine.NumberOfNumericalControlAttributes

    @property
    def number_of_rotary_table_attributes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumberOfRotaryTableAttributes() As short (Read
                | Only)
                | 
                |     This property returns the number of rotary table attributes of a
                |     Manufacturing Machine. The machine is upposed to accept Rotary table (type is
                |     Mfg3AxisWithTableRotationMachine).

        :rtype: int
        """

        return self.manufacturing_machine.NumberOfRotaryTableAttributes

    @property
    def number_of_spindle_attributes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumberOfSpindleAttributes() As short (Read Only)
                | 
                |     This property returns the number of Spindle attributes of a Manufacturing
                |     Machine.

        :rtype: int
        """

        return self.manufacturing_machine.NumberOfSpindleAttributes

    @property
    def number_of_tool_change_attributes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumberOfToolChangeAttributes() As short (Read
                | Only)
                | 
                |     This property returns the number of Tool change attributes of a
                |     Manufacturing Machine.

        :rtype: int
        """

        return self.manufacturing_machine.NumberOfToolChangeAttributes

    @property
    def pp_table_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PPTableName() As CATBSTR
                | 
                |     Give the PPTableName linked to a Manufacturing Machine.
                | 
                |     Example:
                |         The following example returns the PPTableName ThisPPTable linked to the
                |         Manufacturing Machine CurrentMachine
                | 
                |          Set ThisPPTable = CurrentMachine.PPTableName

        :rtype: str
        """

        return self.manufacturing_machine.PPTableName

    @pp_table_name.setter
    def pp_table_name(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_machine.PPTableName = value

    @property
    def post_processor_file(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PostProcessorFile() As CATBSTR
                | 
                |     This property returns the post processor file of a Manufacturing Machine
                |     Machine.PostProcessorFile

        :rtype: str
        """

        return self.manufacturing_machine.PostProcessorFile

    @post_processor_file.setter
    def post_processor_file(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_machine.PostProcessorFile = value

    @property
    def preferred_tool_catalog_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PreferedToolCatalogName() As CATBSTR
                | 
                |     Give the PreferedToolCatalogName linked to a Manufacturing
                |     Machine.
                | 
                |     Example:
                |         The following example returns the PreferedToolCatalogName ThisCatalog
                |         linked to the Manufacturing Machine CurrentMachine
                | 
                |          Set ThisCatalog = CurrentMachine.PreferedToolCatalogName

        :rtype: str
        """

        return self.manufacturing_machine.PreferedToolCatalogName

    @preferred_tool_catalog_name.setter
    def preferred_tool_catalog_name(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_machine.PreferedToolCatalogName = value

    @property
    def rotary_axis(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RotaryAxis() As CATBSTR
                | 
                |     Give the MfgRotaryAxis linked to a Manufacturing Machine.
                | 
                |     Example:
                |         The following example returns the MfgRotaryAxis ThisAxis linked to the
                |         Manufacturing Machine CurrentMachine
                | 
                |          Set ThisAxis = CurrentMachine.RotaryAxis

        :rtype: str
        """

        return self.manufacturing_machine.RotaryAxis

    @rotary_axis.setter
    def rotary_axis(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_machine.RotaryAxis = value

    def default_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DefaultName() As CATBSTR
                | 
                |     Return the string the Type of a Machine.
                | 
                |     Example:
                |         The following example return the type MachineType of to the
                |         manufacturing Machine CurrentMachine
                | 
                |          MachineType = CurrentMachine.Type

        :rtype: str
        """
        return self.manufacturing_machine.DefaultName()

    def get_attribute(self, i_attribute: str) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttribute(CATBSTR iAttribut) As Parameter
                | 
                |     Retrieve the Attribute of a Manufacturing Machine.
                | 
                |     Example:
                |         The following example retreives in HomePosX the attribute
                |         MFG_HOME_POS_X of Manufacturing Machine MyMachine
                | 
                |           Set HomePosX = MyMachine.GetAttribute(MFG_HOME_POS_X)

        :param str i_attribute:
        :rtype: Parameter
        """
        return Parameter(self.manufacturing_machine.GetAttribute(i_attribute))

    def get_attribute_nls_name(self, i_attribute_name: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttributeNLSName(CATBSTR iAttributName) As CATBSTR
                | 
                |     Retrieve the NLS name from the attribute name of a Manufacturing
                |     Machine.

        :param str i_attribute_name:
        :rtype: str
        """
        return self.manufacturing_machine.GetAttributeNLSName(i_attribute_name)

    def get_list_of_attribute_units(self, o_list_of_attribute_units: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfAttributeUnits(CATSafeArrayVariant
                | oListOfAttributeUnits)
                | 
                |     Retrieve the list of attribute units of a
                |     ManufacturingMachine.
                |     The number of items in the output array is equal to the number of
                |     attributes of the machine.
                |     When an attribute has no unit definition, the corresponding unit item in
                |     the output array is a blank string.
                | 
                |     Example:
                |         The following example retrieves in TabAttributeUnits the list of
                |         attribute units of the ManufacturingMachine
                |         CurrentMachine
                | 
                |          call CurrentMachine.GetListOfAttributeUnits(TabAttributeUnits)

        :param tuple o_list_of_attribute_units:
        :rtype: None
        """
        return self.manufacturing_machine.GetListOfAttributeUnits(o_list_of_attribute_units)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_attribute_units'
        # # vba_code = """
        # # Public Function get_list_of_attribute_units(manufacturing_machine)
        # #     Dim oListOfAttributeUnits (2)
        # #     manufacturing_machine.GetListOfAttributeUnits oListOfAttributeUnits
        # #     get_list_of_attribute_units = oListOfAttributeUnits
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_list_of_attributes(self, o_list_of_attributes: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfAttributes(CATSafeArrayVariant
                | oListOfAttributes)
                | 
                |     Retrieve the list of all attributes of a
                |     ManufacturingMachine.
                |     Each attribute is returned as the name of a CKE object.
                | 
                |     Example:
                |         The following example retrieves in TabAttributes the list of attributes
                |         of the ManufacturingMachine CurrentMachine
                | 
                |          call
                |          CurrentMachine.GetListOfAttributes(TabAttributes)

        :param tuple o_list_of_attributes:
        :rtype: None
        """
        return self.manufacturing_machine.GetListOfAttributes(o_list_of_attributes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_attributes'
        # # vba_code = """
        # # Public Function get_list_of_attributes(manufacturing_machine)
        # #     Dim oListOfAttributes (2)
        # #     manufacturing_machine.GetListOfAttributes oListOfAttributes
        # #     get_list_of_attributes = oListOfAttributes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_list_of_numerical_control_attributes(self, o_list_of_attributes: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfNumericalControlAttributes(CATSafeArrayVariant
                | oListOfAttributes)
                | 
                |     Retrieve the list of Numerical Control attributes of a Manufacturing
                |     Machine.
                |     Each attribute is returned as the name of a CKE object.
                | 
                |     Example:
                |         The following example retrieves in oListOfAttributes the list of
                |         Numerical Control attributes of the Manufacturing Machine
                |         myMachine
                | 
                |          call myMachine.GetListOfNumericalControlAttributes(oListOfAttributes)

        :param tuple o_list_of_attributes:
        :rtype: None
        """
        return self.manufacturing_machine.GetListOfNumericalControlAttributes(o_list_of_attributes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_numerical_control_attributes'
        # # vba_code = """
        # # Public Function get_list_of_numerical_control_attributes(manufacturing_machine)
        # #     Dim oListOfAttributes (2)
        # #     manufacturing_machine.GetListOfNumericalControlAttributes oListOfAttributes
        # #     get_list_of_numerical_control_attributes = oListOfAttributes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_list_of_rotary_table_attributes(self, o_list_of_attributes: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfRotaryTableAttributes(CATSafeArrayVariant
                | oListOfAttributes)
                | 
                |     Retrieve the list of Rotary table attributes of a Manufacturing
                |     Machine.
                |     Each attribute is returned as the name of a CKE object.
                | 
                |     Example:
                |         The following example retrieves in oListOfAttributes the list of Tool
                |         Change attributes of the Manufacturing Machine
                |         myMachine
                | 
                |          call myMachine.GetListOfRotaryTableAttributes(oListOfAttributes)

        :param tuple o_list_of_attributes:
        :rtype: None
        """
        return self.manufacturing_machine.GetListOfRotaryTableAttributes(o_list_of_attributes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_rotary_table_attributes'
        # # vba_code = """
        # # Public Function get_list_of_rotary_table_attributes(manufacturing_machine)
        # #     Dim oListOfAttributes (2)
        # #     manufacturing_machine.GetListOfRotaryTableAttributes oListOfAttributes
        # #     get_list_of_rotary_table_attributes = oListOfAttributes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_list_of_spindle_attributes(self, o_list_of_attributes: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfSpindleAttributes(CATSafeArrayVariant
                | oListOfAttributes)
                | 
                |     Retrieve the list of Spindle attributes of a Manufacturing
                |     Machine.
                |     Each attribute is returned as the name of a CKE object.
                | 
                |     Example:
                |         The following example retrieves in oListOfAttributes the list of
                |         Spindle attributes of the Manufacturing Machine
                |         myMachine
                | 
                |          call myMachine.GetListOfSpindleAttributes(oListOfAttributes)

        :param tuple o_list_of_attributes:
        :rtype: None
        """
        return self.manufacturing_machine.GetListOfSpindleAttributes(o_list_of_attributes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_spindle_attributes'
        # # vba_code = """
        # # Public Function get_list_of_spindle_attributes(manufacturing_machine)
        # #     Dim oListOfAttributes (2)
        # #     manufacturing_machine.GetListOfSpindleAttributes oListOfAttributes
        # #     get_list_of_spindle_attributes = oListOfAttributes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_list_of_tool_change_attributes(self, o_list_of_attributes: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfToolChangeAttributes(CATSafeArrayVariant
                | oListOfAttributes)
                | 
                |     Retrieve the list of Tool Change attributes of a Manufacturing
                |     Machine.
                |     Each attribute is returned as the name of a CKE object.
                | 
                |     Example:
                |         The following example retrieves in oListOfAttributes the list of Tool
                |         Change attributes of the Manufacturing Machine
                |         myMachine
                | 
                |          call myMachine.GetListOfToolChangeAttributes(oListOfAttributes)

        :param tuple o_list_of_attributes:
        :rtype: None
        """
        return self.manufacturing_machine.GetListOfToolChangeAttributes(o_list_of_attributes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_tool_change_attributes'
        # # vba_code = """
        # # Public Function get_list_of_tool_change_attributes(manufacturing_machine)
        # #     Dim oListOfAttributes (2)
        # #     manufacturing_machine.GetListOfToolChangeAttributes oListOfAttributes
        # #     get_list_of_tool_change_attributes = oListOfAttributes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_default_values(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_DefaultValues()
                | 
                |     Initialise the Manufacturing Machine parameters.
                | 
                |     Example:
                |         The following example make the init of the parameter of the Machine
                |         ThisMachine .
                | 
                |          call ThisMachine.set_DefaultValues

        :rtype: None
        """
        return self.manufacturing_machine.set_DefaultValues()

    def __repr__(self):
        return f'ManufacturingMachine(name="{self.name}")'
