#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_robot_interfaces.rob_generic_controller import RobGenericController
from pycatia.system_interfaces.any_object import AnyObject


class GenericMotionProfile(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     GenericMotionProfile
                | 
                | Interface to manage Generic Motion Profile of Robot
                | controller.
                | 
                | Role: This interface provides methods to get/set data related to Accuracy
                | Profile.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.generic_motion_profile = com_object

    def get_acceleration_value(self, value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAccelerationValue(double value)
                | 
                |     Retrieves acceleration value of the Profile.
                | 
                |     Parameters:
                | 
                |         value
                |             This out parameter contains motion acceleration of the Profile.
                |             
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float value:
        :rtype: None
        """
        return self.generic_motion_profile.GetAccelerationValue(value)

    def get_angular_acceleration_value(self, value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAngularAccelerationValue(double value)
                | 
                |     Get Angular acceleration value of the Profile.
                | 
                |     Parameters:
                | 
                |         value
                |             Percentage of max angular acceleration of robot. The value is used
                |             when robot TCP rotate against a axis. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float value:
        :rtype: None
        """
        return self.generic_motion_profile.GetAngularAccelerationValue(value)

    def get_angular_speed_value(self, value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAngularSpeedValue(double value)
                | 
                |     Retrieves Angular Speed value of the Profile.
                | 
                |     Parameters:
                | 
                |         value
                |             This out parameter contains Angular Speed of the Profile.
                |             
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float value:
        :rtype: None
        """
        return self.generic_motion_profile.GetAngularSpeedValue(value)

    def get_controller(self, o_controller: RobGenericController) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetController(RobGenericController oController)
                | 
                |     Retrieves controller owning the profile.
                | 
                |     Parameters:
                | 
                |         oController
                |             This parameter contains pointer to controller. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param RobGenericController o_controller:
        :rtype: None
        """
        return self.generic_motion_profile.GetController(o_controller.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_controller'
        # # vba_code = """
        # # Public Function get_controller(generic_motion_profile)
        # #     Dim oController (2)
        # #     generic_motion_profile.GetController oController
        # #     get_controller = oController
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_motion_basis(self, basis: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetMotionBasis(MotionBasis basis)
                | 
                |     Retrieves motion basis of the Profile.
                | 
                |     Parameters:
                | 
                |         basis
                |             motion basis, one of following: MOTION_ABSOLUTE, MOTION_PERCENT,
                |             MOTION_TIME 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param int basis: enum motion_basis
        :rtype: None
        """
        return self.generic_motion_profile.GetMotionBasis(basis)

    def get_name(self, o_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetName(CATBSTR oName)
                | 
                |     Gets name of the Motion Profile.
                | 
                |     Parameters:
                | 
                |         oName
                |             Name of the required Motion Profile. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param str o_name:
        :rtype: None
        """
        return self.generic_motion_profile.GetName(o_name)

    def get_speed_value(self, value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetSpeedValue(double value)
                | 
                |     Retrieves speed value of the Profile.
                | 
                |     Parameters:
                | 
                |         value
                |             This out parameter contains motion speed of the Profile.
                |
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float value:
        :rtype: None
        """
        return self.generic_motion_profile.GetSpeedValue(value)

    def set_acceleration_value(self, value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAccelerationValue(double value)
                | 
                |     Set acceleration value of the Profile.
                | 
                |     Parameters:
                | 
                |         value
                |             meaning of the value is based on the motion basis:
                |             MOTION_ABSOLUTE : absolute acceleration value. MOTION_PERCENT : 0-1, percent of
                |             max acceleration of the device MOTION_TIME : percent of total move time used on
                |             acceleration/deceleration
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float value:
        :rtype: None
        """
        return self.generic_motion_profile.SetAccelerationValue(value)

    def set_angular_acceleration_value(self, value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAngularAccelerationValue(double value)
                | 
                |     Set Angular acceleration value of the Profile.
                | 
                |     Parameters:
                | 
                |         value
                |             Percentage of max angular acceleration of robot. The value is used
                |             when robot TCP rotate against a axis. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float value:
        :rtype: None
        """
        return self.generic_motion_profile.SetAngularAccelerationValue(value)

    def set_angular_speed_value(self, value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAngularSpeedValue(double value)
                | 
                |     Set Angular Speed value of the Profile.
                | 
                |     Parameters:
                | 
                |         value
                |             Percentage of max angular speed of robot. The value is used when
                |             robot TCP rotate against a axis. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float value:
        :rtype: None
        """
        return self.generic_motion_profile.SetAngularSpeedValue(value)

    def set_motion_basis(self, basis: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMotionBasis(MotionBasis basis)
                | 
                |     Set motion basis of the Profile.
                | 
                |     Parameters:
                | 
                |         basis
                |             motion basis, one of following: MOTION_ABSOLUTE, MOTION_PERCENT,
                |             MOTION_TIME 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param int basis: enum motion_basis
        :rtype: None
        """
        return self.generic_motion_profile.SetMotionBasis(basis)

    def set_name(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetName(CATBSTR iName)
                | 
                |     Set name of the Motion Profile.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the Motion Profile to be set. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param str i_name:
        :rtype: None
        """
        return self.generic_motion_profile.SetName(i_name)

    def set_speed_value(self, value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSpeedValue(double value)
                | 
                |     Set speed value of the Profile.
                | 
                |     Parameters:
                | 
                |         value
                |             meaning of the value is based on the motion basis: MOTION_ABSOLUTE : absolute
                |             speed value. MOTION_PERCENT : 0-1, percent of max speed of the device
                |             MOTION_TIME : in seconds
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float value:
        :rtype: None
        """
        return self.generic_motion_profile.SetSpeedValue(value)

    def __repr__(self):
        return f'GenericMotionProfile(name="{self.name}")'
