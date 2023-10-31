#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class E5Property(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     E5Property
                | 
                | Interface to access object properties.
                | Role: This interface allow user to access and edit properties for those V5
                | objects who were loaded from E5. Note
                | 
                | While getting or setting the value for any attribute the implementation
                | attempts to access attribute value from V5 object first & then from
                | Manufacturing Hub. If attribute happens to be one of the mapped attribute or if
                | attribute with same name (user attribute, CATIA attribute ...) exists on V5
                | object, then value will be returned from V5 object. If V5 object doesn't have
                | that attribute, then value will be directly returned from Manufacturing Hub
                | database. When we try to get attribute from V5 object, if required object will
                | be loaded in memory and this may result in populating of cache (CGR, Selective
                | loading...)
                | 
                | This interface expect caller to use attribute name define in PPPR server for
                | example caller should use "note" to access Description .
                | 
                | Set calls will succeed only if user has editing privileges for that
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.e5_property = com_object

    def get_boolean_attribute(self, i_attr_name: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetBooleanAttribute(CATBSTR iAttrName) As boolean
                | 
                |     This gets an CATBoolean Attribute value of an input Object
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The name of the Attribute whose value we need 
                |         oAttrValue
                |             CATBoolean value of the Attribute

        :param str i_attr_name:
        :rtype: bool
        """
        return self.e5_property.GetBooleanAttribute(i_attr_name)

    def get_double_attribute(self, i_attr_name: str) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDoubleAttribute(CATBSTR iAttrName) As double
                | 
                |     This gets a Double Attribute value of an input Object
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The name of the Attribute whose value we need 
                |         oAttrValue
                |             Double value of the Attribute

        :param str i_attr_name:
        :rtype: float
        """
        return self.e5_property.GetDoubleAttribute(i_attr_name)

    def get_long_attribute(self, i_attr_name: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLongAttribute(CATBSTR iAttrName) As long
                | 
                |     This gets a Long Attribute value of an input Object
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The name of the Attribute whose value we need 
                |         oAttrValue
                |             Long value of the Attribute

        :param str i_attr_name:
        :rtype: int
        """
        return self.e5_property.GetLongAttribute(i_attr_name)

    def get_string_attribute(self, i_attr_name: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStringAttribute(CATBSTR iAttrName) As CATBSTR
                | 
                |     This gets a String Attribute value of an input Object
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The name of the Attribute whose value we need 
                | 
                |     Returns:
                |         CATUnicodeString value of the Attribute

        :param str i_attr_name:
        :rtype: str
        """
        return self.e5_property.GetStringAttribute(i_attr_name)

    def set_boolean_attribute(self, i_attr_name: str, i_attr_value: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetBooleanAttribute(CATBSTR iAttrName,
                | boolean iAttrValue)
                | 
                |     This sets an CATBoolean Attribute value to an input Object
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The Attribute Name whose value we need to set 
                |         iAttrValue
                |             CATBoolean value of the Attribute 
                | 
                |     Returns:
                |         Value of iAttrName

        :param str i_attr_name:
        :param bool i_attr_value:
        :rtype: None
        """
        return self.e5_property.SetBooleanAttribute(i_attr_name, i_attr_value)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_boolean_attribute'
        # # vba_code = """
        # # Public Function set_boolean_attribute(e5_property)
        # #     Dim iAttrName (2)
        # #     e5_property.SetBooleanAttribute iAttrName
        # #     set_boolean_attribute = iAttrName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_double_attribute(self, i_attr_name: str, i_attr_value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDoubleAttribute(CATBSTR iAttrName,
                | double iAttrValue)
                | 
                |     This sets a Double Attribute value to an input Object
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The Attribute Name whose value we need to set 
                |         iAttrValue
                |             Double value of the Attribute 
                | 
                |     Returns:
                |         Value of iAttrName

        :param str i_attr_name:
        :param float i_attr_value:
        :rtype: None
        """
        return self.e5_property.SetDoubleAttribute(i_attr_name, i_attr_value)

    def set_long_attribute(self, i_attr_name: str, i_attr_value: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLongAttribute(CATBSTR iAttrName,
                | long iAttrValue)
                | 
                |     This sets a Long Attribute value to an input Object
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The Attribute Name whose value we need to set 
                | 
                |     Returns:
                |         Value of iAttrName

        :param str i_attr_name:
        :param int i_attr_value:
        :rtype: None
        """
        return self.e5_property.SetLongAttribute(i_attr_name, i_attr_value)

    def set_string_attribute(self, i_attr_name: str, i_attr_value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStringAttribute(CATBSTR iAttrName,
                | CATBSTR iAttrValue)
                | 
                |     This sets a String Attribute value to an input Object
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The Attribute Name whose value we need to set 
                |         iAttrValue
                |             CATUnicodeString value of the Attribute

        :param str i_attr_name:
        :param str i_attr_value:
        :rtype: None
        """
        return self.e5_property.SetStringAttribute(i_attr_name, i_attr_value)

    def __repr__(self):
        return f'E5Property(name="{ self.name }")'
