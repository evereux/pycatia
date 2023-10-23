#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class IpdTemplateProperty(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     IPDTemplateProperty
                | 
                | Interface to access template object (being pointed by the given V5 object)
                | properties.
                | Role: This interface given a V5 object, will get the handle to the template
                | object using the pointer attribute referring in it and allows to access the
                | properties of the template object.
                | 
                | This interface expect caller to use attribute name define in PPPR server for
                | example caller should use "note" to access Description .
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.ipd_template_property = com_object

    def get_template_boolean_attribute(self, i_attr_name: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTemplateBooleanAttribute(CATBSTR iAttrName) As
                | boolean
                | 
                |     This gets a String Attribute value of an input Object
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The name of the Attribute whose value we need 
                |         oAttrValue
                |             The value of the attribute 
                | 
                |     Returns:
                |         S_OK

        :param str i_attr_name:
        :rtype: bool
        """
        return self.ipd_template_property.GetTemplateBooleanAttribute(i_attr_name)

    def get_template_double_attribute(self, i_attr_name: str) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTemplateDoubleAttribute(CATBSTR iAttrName) As
                | double
                | 
                |     This gets a String Attribute value of an input Object
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The name of the Attribute whose value we need 
                |         oAttrValue
                |             The value of the attribute 
                | 
                |     Returns:
                |         S_OK

        :param str i_attr_name:
        :rtype: float
        """
        return self.ipd_template_property.GetTemplateDoubleAttribute(i_attr_name)

    def get_template_long_attribute(self, i_attr_name: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTemplateLongAttribute(CATBSTR iAttrName) As long
                | 
                |     This gets a String Attribute value of an input Object
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The name of the Attribute whose value we need 
                |         oAttrValue
                |             The value of the attribute 
                | 
                |     Returns:
                |         S_OK

        :param str i_attr_name:
        :rtype: int
        """
        return self.ipd_template_property.GetTemplateLongAttribute(i_attr_name)

    def get_template_string_attribute(self, i_attr_name: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTemplateStringAttribute(CATBSTR iAttrName) As
                | CATBSTR
                | 
                |     This gets a String Attribute value of an input Object
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             The name of the Attribute whose value we need 
                |         oAttrValue
                |             The value of the attribute 
                | 
                |     Returns:
                |         S_OK

        :param str i_attr_name:
        :rtype: str
        """
        return self.ipd_template_property.GetTemplateStringAttribute(i_attr_name)

    def __repr__(self):
        return f'IpdTemplateProperty(name="{ self.name }")'
