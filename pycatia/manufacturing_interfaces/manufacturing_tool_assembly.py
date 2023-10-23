#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.manufacturing_interfaces.manufacturing_insert import ManufacturingInsert
from pycatia.manufacturing_interfaces.manufacturing_tool import ManufacturingTool
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingToolAssembly(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingToolAssembly
                | 
                | Represents the tool assembly.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_tool_assembly = com_object

    @property
    def assembly_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AssemblyType() As CATBSTR (Read Only)
                | 
                |     Returns the type of the tool assembly.
                |     Legal values: the type of the tool assembly can be either
                |     MfgMillAndDrillToolAssembly or MfgLatheToolAssembly.
                | 
                |     Example:
                | 
                |           The following example returns the assembly type Type of the assembly
                |           CurrentAssembly:
                |          
                | 
                |          Set Type=CurrentAssembly.AssemblyType

        :rtype: str
        """

        return self.manufacturing_tool_assembly.AssemblyType

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Comment() As CATBSTR (Read Only)
                | 
                |     Returns the default comment of a tool assembly.
                | 
                |     Example:
                | 
                |           The following example returns the comment Comment of the tool
                |           assembly CurrentAssembly:
                |          
                | 
                |          Comment=CurrentAssembly.Comment

        :rtype: str
        """

        return self.manufacturing_tool_assembly.Comment

    @property
    def insert(self) -> ManufacturingInsert:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Insert() As ManufacturingInsert (Read Only)
                | 
                |     Returns the insert of an assembly.
                | 
                |     Example:
                | 
                |           The following example retrieves in Insert the insert
                |           
                |          of the assembly CurrentAssembly:
                |          
                | 
                |          Set Insert = CurrentAssembly.Insert

        :rtype: ManufacturingInsert
        """

        return ManufacturingInsert(self.manufacturing_tool_assembly.Insert)

    @property
    def number_of_attributes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumberOfAttributes() As short (Read Only)
                | 
                |     Returns the number of attributes of a tool assembly.
                | 
                |     Example:
                | 
                |           The following example returns the Number of attributes of the tool
                |           assembly CurrentAssembly:
                |          
                | 
                |          Number = CurrentAssembly.NumberOfAttributes

        :rtype: int
        """

        return self.manufacturing_tool_assembly.NumberOfAttributes

    @property
    def tool(self) -> ManufacturingTool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Tool() As ManufacturingTool (Read Only)
                | 
                |     Returns the tool of an assembly.
                | 
                |     Example:
                | 
                |           The following example retrieves in Tool the manufacturing tool
                |           
                |          of the assembly CurrentAssembly:
                |          
                | 
                |          Set Tool = CurrentAssembly.Tool

        :rtype: ManufacturingTool
        """

        return ManufacturingTool(self.manufacturing_tool_assembly.Tool)

    @property
    def tool_number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ToolNumber() As long (Read Only)
                | 
                |     Returns the number linked to a tool assembly.
                | 
                |     Example:
                | 
                |           The following example returns the Number linked to the tool assembly
                |           CurrentAssembly:
                |          
                | 
                |          Number = CurrentAssembly.ToolNumber

        :rtype: int
        """

        return self.manufacturing_tool_assembly.ToolNumber

    def get_attribute(self, i_attribute: str) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttribute(CATBSTR iAttribute) As Parameter
                | 
                |     Returns an attribute of a tool assembly.
                |     The attribute is identified using its name, and is retrieved as a Parameter
                |     object.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             The attribute name 
                | 
                |     Returns:
                |         The retrieved attribute 
                |     Example:
                | 
                |           The following example retrieves in Diameter the attribute
                |           
                |          MfgDiameter of the tool assembly CurrentAssembly:
                |          
                | 
                |          Set Diameter = CurrentAssembly.GetAttribute(MfgDiameter)

        :param str i_attribute:
        :rtype: Parameter
        """
        return Parameter(self.manufacturing_tool_assembly.GetAttribute(i_attribute))

    def get_attribute_nls_name(self, i_attribute_name: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttributeNLSName(CATBSTR iAttributeName) As
                | CATBSTR
                | 
                |     Returns the NLS value of an attribute.
                | 
                |     Parameters:
                | 
                |         iAttributeName
                |             The attribute name 
                | 
                |     Returns:
                |         The attribute NLS value 
                |     Example:
                | 
                |           The following example gives in NLSresult the NLS value of the
                |           "MFG_COMMENT" attributes 
                |          of the tool assembly CurrentAssembly:
                |          
                | 
                |          NLSresult = CurrentAssembly.GetAttributeNLSName("MFG_COMMENT")

        :param str i_attribute_name:
        :rtype: str
        """
        return self.manufacturing_tool_assembly.GetAttributeNLSName(i_attribute_name)

    def get_list_of_attribute_units(self, io_list_of_attribute_units: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfAttributeUnits(CATSafeArrayVariant
                | ioListOfAttributeUnits)
                | 
                |     Retrieves the list of attribute units of a tool assembly.
                |     The number of items in the output array is equal to the number of
                |     attributes of the assembly. When an attribute has no unit definition, the
                |     corresponding unit item in the output array is a blank
                |     string.
                | 
                |     Parameters:
                | 
                |         ioListOfAttributeUnits
                |             The retrieved list of attributes units 
                | 
                |     Example:
                | 
                |           The following example retrieves in TabAttributeUnits the list of
                |           attribute units 
                |          of the tool assembly CurrentAssembly:
                |          
                | 
                |          call CurrentAssembly.GetListOfAttributeUnits(TabAttributeUnits)

        :param tuple io_list_of_attribute_units:
        :rtype: None
        """
        return self.manufacturing_tool_assembly.GetListOfAttributeUnits(io_list_of_attribute_units)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_attribute_units'
        # # vba_code = """
        # # Public Function get_list_of_attribute_units(manufacturing_tool_assembly)
        # #     Dim ioListOfAttributeUnits (2)
        # #     manufacturing_tool_assembly.GetListOfAttributeUnits ioListOfAttributeUnits
        # #     get_list_of_attribute_units = ioListOfAttributeUnits
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_list_of_attributes(self, io_list_of_attributes: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfAttributes(CATSafeArrayVariant
                | ioListOfAttributes)
                | 
                |     Retrieves the list of attributes of a tool assembly.
                |     Each attribute retrieved as a Parameter object.
                | 
                |     Parameters:
                | 
                |         ioListOfAttributes
                |             The retrieved list of attributes 
                | 
                |     Example:
                | 
                |           The following example retrieves in TabAttributes the list of
                |           attributes 
                |          of the tool assembly CurrentAssembly:
                |          
                | 
                |          call
                |          CurrentAssembly.GetListOfAttributes(TabAttributes)

        :param tuple io_list_of_attributes:
        :rtype: None
        """
        return self.manufacturing_tool_assembly.GetListOfAttributes(io_list_of_attributes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_attributes'
        # # vba_code = """
        # # Public Function get_list_of_attributes(manufacturing_tool_assembly)
        # #     Dim ioListOfAttributes (2)
        # #     manufacturing_tool_assembly.GetListOfAttributes ioListOfAttributes
        # #     get_list_of_attributes = ioListOfAttributes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ManufacturingToolAssembly(name="{self.name}")'
