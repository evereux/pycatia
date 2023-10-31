#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_plant_ship_interfaces.psp_list_of_bstrs import PSPListOfBSTRs
from pycatia.cat_plant_ship_interfaces.psp_list_of_doubles import PSPListOfDoubles
from pycatia.cat_plant_ship_interfaces.psp_list_of_longs import PSPListOfLongs
from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.system_interfaces.any_object import AnyObject


class PSPAttribute(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspAttribute
                | 
                | Represents Attribute Interface to query Plant Ship objects'
                | attributes.
                | Role: To query and reset attributes.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_attribute = com_object

    def get_multi_string_attribute_values(self, i_attribute_name: str) -> PSPListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMultiStringAttributeValues(CATBSTR iAttributeName) As
                | PspListOfBSTRs
                | 
                |     Retrieves String values for the input attribute the type
                |     catPspIDLMultiString.
                | 
                |     Parameters:
                | 
                |         iAttributeName
                |             Attribute Name 
                | 
                |     Returns:
                |         List of string values 
                |     Example:
                | 
                |          Dim objThisIntf As PspAttribute
                |          Dim strVar1 As CATBSTR
                |          Dim objArg2 As PspListOfBSTRs
                |           ...
                |          Set objArg2 = objThisIntf.GetMultiStringAttributeValues (strVar1)

        :param str i_attribute_name:
        :rtype: PSPListOfBSTRs
        """
        return PSPListOfBSTRs(self.psp_attribute.GetMultiStringAttributeValues(i_attribute_name))

    def get_parameter(self, i_attribute_name: str) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetParameter(CATBSTR iAttributeName) As Parameter
                | 
                |     Retrieve parameter for the input attribute name.
                | 
                |     Parameters:
                | 
                |         iAttributeName
                |             Attribute Name 
                | 
                |     Returns:
                |         Parameter of the attribute 
                |     Example:
                |
                |          Dim objThisIntf As PspAttribute
                |          Dim strVar1 As CATBSTR
                |          Dim ObjVar2 As Parameter
                |           ...
                |          Set objArg2 = objThisIntf.GetParameter (strVar1 )

        :param str i_attribute_name:
        :rtype: Parameter
        """
        return Parameter(self.psp_attribute.GetParameter(i_attribute_name))

    def get_type(self, i_attribute_name: str) -> int:
        """
        .. note::
            :class: toggle
    
            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetType(CATBSTR iAttributeName) As
                | CatPspIDLAttrDataType
                |
                |     Retrieves type of the input attribute. If the type of the attribute is
                |     catPspIDLMultiString use GetMultiStringAttributeValues. for others, use
                |     GetParameter().
                |
                |     Parameters:
                |
                |         iAttributeName
                |             Attribute Name
                |
                |     Returns:
                |         Type of the attribute.
                |     Example:
                |
                |          Dim objThisIntf As PspAttribute
                |          Dim strVar1 As CATBSTR
                |          Dim eType As CatPspIDLAttrDataType
                |
                |           ...
                |          eType = objThisIntf.GetType (strVar1)
        
            :param str i_attribute_name:
            :rtype: enum cat_psp_idl_attr_data_type
            :return: int
            """
        return self.psp_attribute.GetType(i_attribute_name)

    def is_derived(self, i_attribute_name: str) -> bool:
        """
        .. note::
            :class: toggle
    
            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsDerived(CATBSTR iAttributeName) As boolean
                |
                |     Retrieve Derived status for the input attribute.
                |
                |     Parameters:
                |
                |         iAttributeName
                |             Attribute Name
                |
                |     Returns:
                |         TRUE if the attribute is derived
                |
                |     Example:
                |
                |          Dim objThisIntf As PspAttribute
                |          Dim strVar1 As CATBSTR
                |          Dim bIsDerived As boolean
                |           ...
                |          bIsDerived = objThisIntf.IsDerived (strVar1)
    
        :param str i_attribute_name:
        :rtype: bool
        """
        return self.psp_attribute.IsDerived(i_attribute_name)

    def is_discrete(self, i_attribute_name: str, ob_status: bool) -> int:
        """
        .. note::
            :class: toggle
    
            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsDiscrete(CATBSTR iAttributeName,
                | boolean obStatus) As short
                |
                |     Query whether the input attribute is discrete or not.
                |
                |     Parameters:
                |
                |         iAttributeName
                |             Attribute Name
                |         obStatus
                |             TRUE if attribute is discrete else FALSE
                |
                |     Returns:
                |         Discrete Type value 1-Standard 2-Encoded discrete
                |
                |     Example:
                |
                |          Dim objThisIntf As PspAttribute
                |          Dim strVar1 As CATBSTR
                |          Dim boolVar2 As Boolean
                |          Dim shortVar3  As Short
                |           ...
                |          shortVar3 = objThisIntf.IsDiscrete (strVar1,boolVar2)
    
        :param str i_attribute_name:
        :param bool ob_status:
        :rtype: int
        """
        return self.psp_attribute.IsDiscrete(i_attribute_name, ob_status)

    def list_attributes(self, i_domain_id: int) -> PSPListOfBSTRs:
        """
        .. note::
            :class: toggle
    
            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListAttributes(CatPspIDLDomainID iDomainID) As
                | PspListOfBSTRs
                |
                |     Retrieves a list of Attributes of an object in the the input domain
                |     ID.
                |
                |     Parameters:
                |
                |         iDomainID
                |             Domain ID. If set to catPspIDLNone, then it will return attributes
                |             in all the domains.
                |
                |     Returns:
                |         List of attributes ( A list of CATIAPspGroupables)
                |
                |     Example:
                |
                |          Dim objThisIntf As PspAttribute
                |          Dim objArg1 As CatPspIDLDomainID
                |          Dim objArg2 As PspListOfBSTRs
                |           ...
                |          Set objArg2 = objThisIntf.ListAttributes (objArg1)
    
        :param int i_domain_id: enum cat_psp_idl_domain_id
        :rtype: PSPListOfBSTRs
        """
        return PSPListOfBSTRs(self.psp_attribute.ListAttributes(i_domain_id))

    def list_double_discrete_values(self, i_attribute_name: str) -> PSPListOfDoubles:
        """
        .. note::
            :class: toggle
    
            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListDoubleDiscreteValues(CATBSTR iAttributeName) As
                | PspListOfDoubles
                |
                |     Retrieves double discrete values for the input attribute.
                |
                |     Parameters:
                |
                |         iAttributeName
                |             Attribute Name
                |
                |     Returns:
                |         Discrete list of double values
                |
                |     Example:
                |
                |          Dim objThisIntf As PspAttribute
                |          Dim strVar1 As CATBSTR
                |          Dim objArg2 As PspListOfDoubles
                |           ...
                |          Set objArg2 = objThisIntf.ListDoubleDiscreteValues (strVar1 )
    
        :param str i_attribute_name:
        :rtype: PSPListOfDoubles
        """
        return PSPListOfDoubles(self.psp_attribute.ListDoubleDiscreteValues(i_attribute_name))

    def list_encoded_decoded_discrete_values(
            self,
            i_attribute_name: str,
            o_l_discrete_encoded_values: PSPListOfBSTRs,
            o_l_discrete_decoded_value: PSPListOfBSTRs
    ) -> None:
        """
        .. note::
            :class: toggle
    
            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListEncodedDecodedDiscreteValues(CATBSTR
                | iAttributeName,
                | PspListOfBSTRs oLDiscreteEncodedValues,
                | PspListOfBSTRs oLDiscreteDecodedValue)
                |
                |     Retrieves Encoded-decoded discrete values for the input
                |     attribute.
                |
                |     Parameters:
                |
                |         iAttributeName
                |             Attribute Name
                |         oLDiscreteEncodedValues
                |             Discrete list of encoded string values
                |         oLDiscreteDecodedValue
                |             Discrete list of decoded string values
                |
                |     Example:
                |
                |          Dim objThisIntf As PspAttribute
                |          Dim strVar1 As CATBSTR
                |          Dim objArg2 As PspListOfBSTRs
                |          Dim objArg3 As PspListOfBSTRs
                |           ...
                |          objThisIntf.ListEncodedDecodedDiscreteValues strVar1, objArg2,
                |          objArg3
    
        :param str i_attribute_name:
        :param PSPListOfBSTRs o_l_discrete_encoded_values:
        :param PSPListOfBSTRs o_l_discrete_decoded_value:
        :rtype: None
        """
        return self.psp_attribute.ListEncodedDecodedDiscreteValues(
            i_attribute_name,
            o_l_discrete_encoded_values.com_object,
            o_l_discrete_decoded_value.com_object
        )
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_encoded_decoded_discrete_values'
        # # vba_code = """
        # # Public Function list_encoded_decoded_discrete_values(psp_attribute)
        # #     Dim iAttributeName (2)
        # #     psp_attribute.ListEncodedDecodedDiscreteValues iAttributeName
        # #     list_encoded_decoded_discrete_values = iAttributeName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def list_integer_discrete_values(self, i_attribute_name: str) -> PSPListOfLongs:
        """
        .. note::
            :class: toggle
    
            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListIntegerDiscreteValues(CATBSTR iAttributeName) As
                | PspListOfLongs
                |
                |     Retrieve integer (long) discrete values for the input
                |     attribute.
                |
                |     Parameters:
                |
                |         iAttributeName
                |             Attribute Name
                |
                |     Returns:
                |         Discrete list of integer values
                |
                |     Example:
                |
                |          Dim objThisIntf As PspAttribute
                |          Dim strVar1 As CATBSTR
                |          Dim objArg2 As PspListOfLongs
                |           ...
                |          Set objArg2 = objThisIntf.ListIntegerDiscreteValues (strVar1)
    
        :param str i_attribute_name:
        :rtype: PSPListOfLongs
        """
        return PSPListOfLongs(self.psp_attribute.ListIntegerDiscreteValues(i_attribute_name))

    def list_string_discrete_values(self, i_attribute_name: str) -> PSPListOfBSTRs:
        """
        .. note::
            :class: toggle
    
            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListStringDiscreteValues(CATBSTR iAttributeName) As
                | PspListOfBSTRs
                |
                |     RetrievesString discrete values for the input attribute.
                |
                |     Parameters:
                |
                |         iAttributeName
                |             Attribute Name
                |
                |     Returns:
                |         Discrete list of string values
                |
                |     Example:
                |
                |          Dim objThisIntf As PspAttribute
                |          Dim strVar1 As CATBSTR
                |          Dim objArg2 As PspListOfBSTRs
                |           ...
                |          Set objArg2 = objThisIntf.ListStringDiscreteValues (strVar1)
    
        :param str i_attribute_name:
        :rtype: PSPListOfBSTRs
        """
        return PSPListOfBSTRs(self.psp_attribute.ListStringDiscreteValues(i_attribute_name))

    def reset_derived_attr(self, i_attribute_name: str) -> None:
        """
        .. note::
            :class: toggle
    
            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetDerivedAttr(CATBSTR iAttributeName)
                |
                |     Reset derived status of the attribute to not-derived.
                |
                |     Parameters:
                |
                |         iAttributeName
                |             Attribute Name
                |
                |     Example:
                |
                |          Dim objThisIntf As PspAttribute
                |          Dim strVar1 As CATBSTR
                |           ...
                |          objThisIntf.ResetDerivedAttr strVar1
    
        :param str i_attribute_name:
        :rtype: None
        """
        return self.psp_attribute.ResetDerivedAttr(i_attribute_name)

    def __repr__(self):
        return f'PSPAttribute(name="{self.name}")'
