#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.manufacturing_interfaces.manufacturing_tool_corrector import ManufacturingToolCorrector
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingTool(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingTool
                | 
                | A ManufacturingTool for a Manufacturing Document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_tool = com_object

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Comment() As CATBSTR (Read Only)
                | 
                |     Return the Default Comment of a Manufacturing Setup.
                | 
                |     Example:
                |         The following example return the comment ToolComment of to the
                |         manufacturing tool CurrentTool
                | 
                |          ToolComment=CurrentTool.Comment

        :rtype: str
        """

        return self.manufacturing_tool.Comment

    @property
    def corrector_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CorrectorCount() As short (Read Only)
                | 
                |     Retreive the number of correctors of a Manufacturing tool.
                | 
                |     Example:
                |         The following example retreives in CorrCount the number of tool
                |         correctors of tool CurrentTool
                | 
                |          Set NbCorr = CurrentTool.CorrectorCount

        :rtype: int
        """

        return self.manufacturing_tool.CorrectorCount

    @property
    def number_of_attributes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumberOfAttributes() As short (Read Only)
                | 
                |     Give the Number og attributes of a Manufacturing Tool.
                | 
                |     Example:
                |         The following example returns the Number of attributes of the
                |         manufacturing Tool CurrentTool
                | 
                |          Number = CurrentTool.NumberOfAttributes

        :rtype: int
        """

        return self.manufacturing_tool.NumberOfAttributes

    @property
    def picture(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Picture() As CATBSTR (Read Only)
                | 
                |     Return the path where a picture of the parametrized tool is
                |     stored.
                | 
                |     Example:
                |         The following example return the path PicturePath where can be found
                |         the picture of the tool CurrentTool
                | 
                |          PicturePath=CurrentTool.Picture

        :rtype: str
        """

        return self.manufacturing_tool.Picture

    @property
    def tool_number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ToolNumber() As long (Read Only)
                | 
                |     Give the Number linked to a Manufacturing Tool.
                | 
                |     Example:
                |         The following example returns the Number linked to the manufacturing
                |         Tool CurrentTool
                | 
                |          Number = CurrentTool.ToolNumber

        :rtype: int
        """

        return self.manufacturing_tool.ToolNumber

    @property
    def tool_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ToolType() As CATBSTR (Read Only)
                | 
                |     Return the technological type of a the tool.
                | 
                |     Example:
                |         The following example return the tool type ToolType of to the
                |         manufacturing tool CurrentTool
                | 
                |          Set ToolType=CurrentTool.ToolType

        :rtype: str
        """

        return self.manufacturing_tool.ToolType

    def add_corrector(self) -> ManufacturingToolCorrector:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddCorrector() As ManufacturingToolCorrector
                | 
                |     Adds a corrector to a Manufacturing tool.
                | 
                |     Example:
                |         The following example adds in Corr the tool corrector of Tool
                |         CurrentTool
                | 
                |          Set Corr = CurrentTool.AddCorrector

        :rtype: ManufacturingToolCorrector
        """
        return ManufacturingToolCorrector(self.manufacturing_tool.AddCorrector())

    def get_attribute(self, i_attribute: str) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttribute(CATBSTR iAttribut) As Parameter
                | 
                |     Retrieve by is name the attribute of a Manufacturing Tool.
                |     Each attribute is a CKE object.
                | 
                |     Example:
                |         The following example retreives in Diameter the attribute MfgDiameter
                |         of the Manufacturing Tool firstTool
                | 
                |          Set Diameter = firstTool.GetAttribute(MfgDiameter)

        :param str i_attribute:
        :rtype: Parameter
        """
        return Parameter(self.manufacturing_tool.GetAttribute(i_attribute))

    def get_attribute_nls_name(self, i_attribute_name: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttributeNLSName(CATBSTR iAttributName) As CATBSTR
                | 
                |     Retrieve the NLS name from the attribute name of a Manufacturing
                |     Tool.

        :param str i_attribute_name:
        :rtype: str
        """
        return self.manufacturing_tool.GetAttributeNLSName(i_attribute_name)

    def get_corrector(self, index: int) -> ManufacturingToolCorrector:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCorrector(short index) As
                | ManufacturingToolCorrector
                | 
                |     Retreive the corrector (index) of a Manufacturing tool.
                | 
                |     Example:
                |         The following example retreives in Corr the tool corrector of Tool
                |         CurrentTool
                | 
                |          Set Corr = CurrentTool.GetCorrector(index)

        :param int index:
        :rtype: ManufacturingToolCorrector
        """
        return ManufacturingToolCorrector(self.manufacturing_tool.GetCorrector(index))

    def get_list_of_apt_parameters(self, o_list_of_apt_parameters: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfAptParameters(CATSafeArrayVariant
                | oListOfAptParameters)
                | 
                |     Retrieve the list of apt definition parameters of a Manufacturing
                |     Tool.
                |     Parameters are returned in an array of real values.

        :param tuple o_list_of_apt_parameters:
        :rtype: None
        """
        return self.manufacturing_tool.GetListOfAptParameters(o_list_of_apt_parameters)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_apt_parameters'
        # # vba_code = """
        # # Public Function get_list_of_apt_parameters(manufacturing_tool)
        # #     Dim oListOfAptParameters (2)
        # #     manufacturing_tool.GetListOfAptParameters oListOfAptParameters
        # #     get_list_of_apt_parameters = oListOfAptParameters
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_list_of_attribute_units(self, o_list_of_attribute_units: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfAttributeUnits(CATSafeArrayVariant
                | oListOfAttributeUnits)
                | 
                |     Retrieve the list of attribute units of a Manufacturing
                |     Tool.
                |     The number of items in the output array is equal to the number of
                |     attributes of the tool.
                |     When an attribute has no unit definition, the corresponding unit item in
                |     the output array is a blank string.
                | 
                |     Example:
                |         The following example retrieves in TabAttributeUnits the list of
                |         attribute units of the Manufacturing Tool firstTool
                | 
                |          call
                |          firstTool.GetListOfAttributeUnits(TabAttributeUnits)

        :param tuple o_list_of_attribute_units:
        :rtype: None
        """
        return self.manufacturing_tool.GetListOfAttributeUnits(o_list_of_attribute_units)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_attribute_units'
        # # vba_code = """
        # # Public Function get_list_of_attribute_units(manufacturing_tool)
        # #     Dim oListOfAttributeUnits (2)
        # #     manufacturing_tool.GetListOfAttributeUnits oListOfAttributeUnits
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
                |     Retrieve the list of attributes of a Manufacturing Tool.
                |     Each attribute is returned as the name of a CKE object.
                | 
                |     Example:
                |         The following example retrieves in TabAttributes the list of attributes
                |         of the Manufacturing Tool firstTool
                | 
                |          call firstTool.GetListOfAttributes(TabAttributes)

        :param tuple o_list_of_attributes:
        :rtype: None
        """
        return self.manufacturing_tool.GetListOfAttributes(o_list_of_attributes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_attributes'
        # # vba_code = """
        # # Public Function get_list_of_attributes(manufacturing_tool)
        # #     Dim oListOfAttributes (2)
        # #     manufacturing_tool.GetListOfAttributes oListOfAttributes
        # #     get_list_of_attributes = oListOfAttributes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_list_of_geom_attributes(self, o_list_of_attributes: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfGeomAttributes(CATSafeArrayVariant
                | oListOfAttributes)
                | 
                |     Retrieve the list of geometry attributes of a Manufacturing
                |     Tool.
                |     Each attribute is returned as the name of a CKE object.
                | 
                |     Example:
                |         The following example retrieves in TabGeomAttributes the list of
                |         geometry attributes of the Manufacturing Tool
                |         firstTool
                | 
                |          call firstTool.GetListOfGeomAttributes(TabAttributes)

        :param tuple o_list_of_attributes:
        :rtype: None
        """
        return self.manufacturing_tool.GetListOfGeomAttributes(o_list_of_attributes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_geom_attributes'
        # # vba_code = """
        # # Public Function get_list_of_geom_attributes(manufacturing_tool)
        # #     Dim oListOfAttributes (2)
        # #     manufacturing_tool.GetListOfGeomAttributes oListOfAttributes
        # #     get_list_of_geom_attributes = oListOfAttributes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ManufacturingTool(name="{self.name}")'
