#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ParameterProfiles(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ParameterProfiles
                | 
                | Interface to manage an user-defined applicative parameter
                | profile.
                | 
                | Role: This interface allows the end-user to handle Applicative parameter
                | profiles attributes. To create them, please refer to
                | ParameterProfilesFactory.
                | Applicative profiles are defined using a Feature Dictionary Editor application.
                | The name of the attributes don't change after the CATFct file has been defined.
                | End-user must know what the name of the attributes are.
                | 
                | To get a handle on the robot, the product must be the assembly node
                | representing the robot (the one with a robot icon).
                | 
                | The following code can be used to retrieve a handle on a
                | profile
                | 
                |    'current document is a product
                |    'the root product is a robot
                | 
                |    'retrieving the root product
                |    Dim MyProduct As Product
                |    Set MyProduct = CATIA.ActiveDocument.Product
                | 
                |    'retrieving the handle
                |    Dim MyProfileFactory As ParameterProfilesFactory
                |    Set MyProfileFactory = MyProduct.GetTechnologicalObject("ParameterProfilesFactory")
                |    ...
                |    'retrieving the list of profiles as an array
                |    Dim MyListOfProfiles() As ParameterProfiles
                |    MyProfileFactory.GetAllProfileInstances(MyListOfProfiles)
                | 
                |    'loop for each profile to get the name
                |    Dim MyCurrentProfile as ParameterProfiles
                |    Dim MyCurrentProfileName
                |    For Each MyCurrentProfile In MyListOfProfiles
                |       MyCurrentProfileName.GetName(MyCurrentProfileName)
                |    Next
                |
                | ParameterProfilesFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.parameter_profiles = com_object

    def get_attribute_value(self, i_attribute_name: str, o_encapsulated_attribute_value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAttributeValue(CATBSTR iAttributeName,
                | CATBSTR oEncapsulatedAttributeValue)
                | 
                |     Gets the attribute value for the attribute mentioned
                | 
                |     Parameters:
                | 
                |         iAttributeName
                |             Name of the attribute for which the value has to be set (input)
                |             
                |         oEncapsulatedAttributeValue
                |             Value of the attribute encapsulated as a CATBSTR string (output)
                |
                |     Example:
                |
                |            ' declaration of handle for the profile
                |            Dim MyProfile As ParameterProfiles
                | 
                |            ' valuation 
                |            Set MyProfile= ...
                | 
                |            ' declaration of variable for name
                |            Dim AttributeName
                |            Dim AttributeValue
                | 
                |            ' valuation based on user inputs
                |            AttributeName = "MyAttributeName"  'example
                | 
                |            ' getting the attribute value 
                |            MyProfile.GetAttributeValue(AttributeName,AttributeValue)

        :param str i_attribute_name:
        :param str o_encapsulated_attribute_value:
        :rtype: None
        """
        return self.parameter_profiles.GetAttributeValue(i_attribute_name, o_encapsulated_attribute_value)

    def get_name(self, o_instance_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetName(CATBSTR oInstanceName)
                | 
                |     Gets the new name for the Profile instance
                | 
                |     Parameters:
                | 
                |         oInstanceName
                |             Name of the Profile instance (output) 
                | 
                |     Example:
                |
                |            ' declaration of handle for the profile
                |            Dim MyProfile As ParameterProfiles
                | 
                |            ' valuation 
                |            Set MyProfile= ...
                | 
                |            ' declaration of variable for name
                |            Dim InstanceName
                | 
                |            ' setting the name 
                |            MyProfile.GetName(InstanceName)

        :param str o_instance_name:
        :rtype: None
        """
        return self.parameter_profiles.GetName(o_instance_name)

    def set_attribute_value(self, i_attribute_name: str, i_encapsulated_attribute_value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttributeValue(CATBSTR iAttributeName,
                | CATBSTR iEncapsulatedAttributeValue)
                | 
                |     Sets a new attribute value for the attribute mentioned
                | 
                |     Parameters:
                | 
                |         iAttributeName
                |             Name of the attribute for which the value has to be set (input)
                |             
                |         iEncapsulatedAttributeValue
                |             Value of the attribute encapsulated as a CATBSTR string (input)
                |
                |     Example:
                |
                |            ' declaration of handle for the profile
                |            Dim MyProfile As ParameterProfiles
                | 
                |            ' valuation 
                |            Set MyProfile= ...
                | 
                |            ' declaration of variable for name
                |            Dim AttributeName
                |            Dim AttributeValue
                | 
                |            ' valuation based on user inputs
                |            AttributeName = "MyAttributeName"  'example
                |            AttributeValue= "MyAttributeValue" 'example
                | 
                |            ' setting the attribute value 
                |            MyProfile.SetAttributeValue(AttributeName,AttributeValue)

        :param str i_attribute_name:
        :param str i_encapsulated_attribute_value:
        :rtype: None
        """
        return self.parameter_profiles.SetAttributeValue(i_attribute_name, i_encapsulated_attribute_value)

    def set_name(self, i_new_instance_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetName(CATBSTR iNewInstanceName)
                | 
                |     Sets a new name for the Profile instance
                | 
                |     Parameters:
                | 
                |         iNewInstanceName
                |             New name of the Profile instance (input) 
                | 
                |     Example:
                |
                |            ' declaration of handle for the profile
                |            Dim MyProfile As ParameterProfiles
                | 
                |            ' valuation 
                |            Set MyProfile= ...
                | 
                |            ' declaration of variable for name
                |            Dim InstanceName
                |            ' valuation 
                |            InstanceName = "MyInstanceName.2" 'example
                | 
                |            ' setting the name 
                |            MyProfile.SetName(InstanceName)

        :param str i_new_instance_name:
        :rtype: None
        """
        return self.parameter_profiles.SetName(i_new_instance_name)

    def __repr__(self):
        return f'ParameterProfiles(name="{self.name}")'
