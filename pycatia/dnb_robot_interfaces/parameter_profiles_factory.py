#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_robot_interfaces.parameter_profiles import ParameterProfiles
from pycatia.system_interfaces.any_object import AnyObject


class ParameterProfilesFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ParameterProfilesFactory
                | 
                | Interface to manage an user-defined applicative parameter profile(s) defined on
                | a robot controller.
                | 
                | Role: This interface allows the end-user to handle Applicative parameter
                | profiles on a robot controller. It works on both:
                | 
                |     robots created using V5 mechanisms
                |     robots imported from DENEB D5
                |
                | Applicative profiles are defined using a Feature Dictionary Editor application.
                | The application will save CATFct files that must be referenced with a file
                | Profile.xml, referenced through the environment variable CATDisciplinePath. For
                | more information, please refer to the Device Building product documentation in
                | the Advanced Tasks section on the setup.
                | 
                | To get a handle on the robot, the product must be the assembly node
                | representing the robot (the one with a robot icon).
                | 
                | The following code snippet shows how to retrieve the handle on the
                | factory.
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
                |    'loop for each profile
                |    Dim MyCurrentProfile as ParameterProfiles
                |    For Each MyCurrentProfile In MyListOfProfiles
                |       ...
                |    Next
                |
                | ParameterProfiles CATSafeArrayVariant
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.parameter_profiles_factory = com_object

    def create_profile_instance(
            self,
            i_profile_type: str,
            i_instance_name: str,
            o_app_parameter_profile: ParameterProfiles
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateProfileInstance(CATBSTR iProfileType,
                | CATBSTR iInstanceName,
                | ParameterProfiles oAppParameterProfile)
                | 
                |     Instantiates a particular profile type. The profile type is user-defined:
                |     it is the name the user has set when defining the profile in the CATFct
                |     file.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             Profile type name for which the instance has to be created (input)
                |             
                |         iInstanceName
                |             Desired instance name for the instance to be created( input)
                |             
                |         oAppParameterProfile
                |             Handle to the profile instance thus created (output)
                |
                |     Example:
                |
                |            ' declaration of 2 variable handles
                |            Dim MyNewProfile As ParameterProfiles
                |            Dim MyProfileFactory As ParameterProfilesFactory
                | 
                |            ' valuation 
                |            Set MyProfileFactory= ...
                | 
                |            ' declaration of variables for names
                |            Dim InstanceName
                |            Dim DefaultName
                |            DefaultName = "MyChoice." 'example
                | 
                |            'Create 10 instances of the profile type
                |            MyProfileType
                |            For i=1 to 10
                |                'concatenation of default name and index
                |                InstanceName = DefaultName & i
                |                ParmProfileFact.CreateProfileInstance(
                |                "MyProfileType",
                |                InstanceName,
                |                MyNewProfile)
                |            Next

        :param str i_profile_type:
        :param str i_instance_name:
        :param ParameterProfiles o_app_parameter_profile:
        :rtype: None
        """
        return self.parameter_profiles_factory.CreateProfileInstance(
            i_profile_type,
            i_instance_name,
            o_app_parameter_profile.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_profile_instance'
        # # vba_code = """
        # # Public Function create_profile_instance(parameter_profiles_factory)
        # #     Dim iProfileType (2)
        # #     parameter_profiles_factory.CreateProfileInstance iProfileType
        # #     create_profile_instance = iProfileType
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def delete_profile_instance(self, io_parameter_profile: ParameterProfiles) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub DeleteProfileInstance(ParameterProfiles
                | ioParameterProfile)
                | 
                |     Deletes a particular profile instance
                | 
                |     Parameters:
                | 
                |         ioParameterProfile
                |             Handle to the profile instance which should be deleted( input)
                |
                |     Example:
                |
                |            ' declaration of 2 variable handles
                |            Dim MyProfileToDelete As ParameterProfiles
                |            Dim MyProfileFactory As ParameterProfilesFactory
                | 
                |            ' valuation 
                |            Set MyProfileToDelete= ...
                |            Set MyProfileFactory= ...
                | 
                |            'deletion of the object
                |            MyProfileFactory.DeleteProfileInstance(MyProfileToDelete);

        :param ParameterProfiles io_parameter_profile:
        :rtype: None
        """
        return self.parameter_profiles_factory.DeleteProfileInstance(io_parameter_profile.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'delete_profile_instance'
        # # vba_code = """
        # # Public Function delete_profile_instance(parameter_profiles_factory)
        # #     Dim ioParameterProfile (2)
        # #     parameter_profiles_factory.DeleteProfileInstance ioParameterProfile
        # #     delete_profile_instance = ioParameterProfile
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_all_profile_instances(self, o_all_instances_on_product: tuple) -> ParameterProfiles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAllProfileInstances(CATSafeArrayVariant
                | oAllInstancesOnProduct)
                | 
                |     Gets the array of all the handles of the profile instances (belonging to
                |     all profile types)
                | 
                |     Parameters:
                | 
                |         oAllInstancesOnProduct
                |             The array of all the handles to all the profile instances of all
                |             the profile types(output) 
                | 
                |     Example:
                |
                |            'retrieving the handle on the profile factory
                |            Dim MyProfileFactory As ParameterProfilesFactory
                |            set MyProfileFactory = ...
                |            ...
                |            'retrieving the list of profiles as an array
                |            Dim MyListOfProfiles() As ParameterProfiles
                |            MyProfileFactory.GetAllProfileInstances(MyListOfProfiles)
                |
                |            'loop for each profile
                |            Dim MyCurrentProfile as ParameterProfiles
                |            For Each MyCurrentProfile In MyListOfProfiles
                |               ...
                |            Next

        :param tuple o_all_instances_on_product:
        :rtype: ParameterProfiles
        """
        return ParameterProfiles(self.parameter_profiles_factory.GetAllProfileInstances(o_all_instances_on_product))
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_all_profile_instances'
        # # vba_code = """
        # # Public Function get_all_profile_instances(parameter_profiles_factory)
        # #     Dim oAllInstancesOnProduct (2)
        # #     parameter_profiles_factory.GetAllProfileInstances oAllInstancesOnProduct
        # #     get_all_profile_instances = oAllInstancesOnProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_profile_instance(self, i_instance_name: str, o_profile_instance: ParameterProfiles) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetProfileInstance(CATBSTR iInstanceName,
                | ParameterProfiles oProfileInstance)
                | 
                |     Gets the handle to the profile instance against the instance
                |     name
                | 
                |     Parameters:
                | 
                |         iInstanceName
                |             The name of the profile instance(input) 
                |         oProfileInstance
                |             Handle to the profile instance which has the above name( output)
                |
                |     Example:
                |
                |            'retrieving the handle on the profile factory
                |            Dim MyProfileFactory As ParameterProfilesFactory
                |            set MyProfileFactory = ...
                |            ...
                |            'defining the type
                |            Dim MyProfileName
                |            set MyProfileName= "MyProfile.1" 'example
                |            
                |            'retrieving the profile
                |            Dim MyCurrentProfile as ParameterProfiles
                |            MyProfileFactory.GetProfileInstances(
                |               MyProfileName,
                |               MyListOfProfiles)

        :param str i_instance_name:
        :param ParameterProfiles o_profile_instance:
        :rtype: None
        """
        return self.parameter_profiles_factory.GetProfileInstance(i_instance_name, o_profile_instance.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_profile_instance'
        # # vba_code = """
        # # Public Function get_profile_instance(parameter_profiles_factory)
        # #     Dim iInstanceName (2)
        # #     parameter_profiles_factory.GetProfileInstance iInstanceName
        # #     get_profile_instance = iInstanceName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_profile_instances(self, i_profile_type: str, o_profiles: tuple) -> ParameterProfiles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetProfileInstances(CATBSTR iProfileType,
                | CATSafeArrayVariant oProfiles)
                | 
                |     Gets the array of handles of the profile instances belonging to a
                |     particular profile type
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The Profile Type (input) 
                |         oProfiles
                |             The array of handles to the profile instances of the type specified
                |             above(output) 
                | 
                |     Example:
                |
                |            'retrieving the handle on the profile factory
                |            Dim MyProfileFactory As ParameterProfilesFactory
                |            set MyProfileFactory = ...
                |            ...
                |            'defining the type
                |            Dim MyProfileType
                |            set MyProfileType = "MyProfileType" 'example
                |            
                |            'retrieving the list of profiles as an array
                |            Dim MyListOfProfiles() As ParameterProfiles
                |            MyProfileFactory.GetProfileInstances(
                |                                                   MyProfileType,
                |                                                   MyListOfProfiles)
                |
                |            'loop for each profile
                |            Dim MyCurrentProfile as ParameterProfiles
                |            For Each MyCurrentProfile In MyListOfProfiles
                |               ...
                |            Next

        :param str i_profile_type:
        :param tuple o_profiles:
        :rtype: ParameterProfiles
        """
        return ParameterProfiles(self.parameter_profiles_factory.GetProfileInstances(i_profile_type, o_profiles))
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_profile_instances'
        # # vba_code = """
        # # Public Function get_profile_instances(parameter_profiles_factory)
        # #     Dim iProfileType (2)
        # #     parameter_profiles_factory.GetProfileInstances iProfileType
        # #     get_profile_instances = iProfileType
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ParameterProfilesFactory(name="{self.name}")'
