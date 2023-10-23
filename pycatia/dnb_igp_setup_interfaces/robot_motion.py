#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity
from pycatia.dnb_igp_setup_interfaces.tag import Tag
from pycatia.system_interfaces.any_object import AnyObject


class RobotMotion(Activity):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMAPSInterfaces.Activity
                |                         RobotMotion
                | 
                | Represents a Robot Motion.
                | 
                | Role: The interface is used to retrieve and set the motion attributes of a
                | Robot Motion.
                | The following code snippet can be used to obtain the Robot Motion from a
                | Operation aggreagted under a Robot Task.
                | 
                |    Dim objOpr as Operation
                |    ...
                |    Dim objRobotmotion as RobotMotion
                |    objOpr.GetRobotMotion objRobotmotion
                |  
                | 
                | 
                | The Robot Motion can also be obtained from an activity of the type
                | RobotMotion.
                | 
                |    Dim objActivity as Activity
                |    ...
                |    Dim objRobotmotion as RobotMotion
                |    Set objRobotmotion = objActivity.GetTechnologicalObject("RobotMotion" )
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.robot_motion = com_object

    def get_accuracy_profile(self, o_accuracy_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAccuracyProfile(AnyObject oAccuracyProfile)
                | 
                |     Retrieves Accuracy profile.
                | 
                |     Parameters:
                | 
                |         oAccuracyProfile
                |             The retrieved profile. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Accuracy Profile was successfully set.
                |         E_FAIL
                |             The Accuracy Profile could not be set.
                | 
                |         Example:
                |             The following example retrieves the Accuracy Profile for the robot
                |             Accuracy.
                | 
                |                Dim objRobotMotion as RobotMotion
                |                Dim AccuracyProfile As String
                |                objRobotMotion.GetAccuracyProfile
                |                AccuracyProfile

        :param AnyObject o_accuracy_profile:
        :rtype: None
        """
        return self.robot_motion.GetAccuracyProfile(o_accuracy_profile.com_object)

    def get_auxillary_axis_home(self, i_device: AnyObject, i_auxillary_axis: str, o_home_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAuxillaryAxisHome(AnyObject iDevice,
                | CATBSTR iAuxillaryAxis,
                | CATBSTR oHomeName)
                | 
                |     Retrieves the underlying Auxillary device Home.
                | 
                |     Parameters:
                | 
                |         iDevice
                |             The Auxillary Device. 
                |         iAuxillaryAxis
                |             Name of the Auxillary Device. 
                |         oHomeName
                |             Home name retrieved for the given Auxillary device.
                |
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The auxillary device target was successfully
                |             retrieved.
                |         E_FAIL
                |             The auxillary device target could not be
                |             retrieved.
                | 
                |         Example:
                |             The following example retrives the home name correspoding to the
                |             target of the auxillary device in a robot motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim Device As Product
                |                ...
                |                Dim DeviceName As String
                |                DeviceName = "Mechanism.1"
                |                Dim HomeName As String
                |                objRobotmotion.GetAuxillaryAxisHome HomeName

        :param AnyObject i_device:
        :param str i_auxillary_axis:
        :param str o_home_name:
        :rtype: None
        """
        return self.robot_motion.GetAuxillaryAxisHome(i_device.com_object, i_auxillary_axis, o_home_name)

    def get_auxillary_axis_values(
            self,
            i_device: AnyObject,
            i_auxillary_axis: str,
            o_auxillary_axis_values: tuple
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAuxillaryAxisValues(AnyObject iDevice,
                | CATBSTR iAuxillaryAxis,
                | CATSafeArrayVariant oAuxillaryAxisValues)
                | 
                |     Retrieves the underlying Auxillary device Joint values.
                | 
                |     Parameters:
                | 
                |         iDevice
                |             Auxillary device (Mechanism) 
                |         iAuxillaryAxis
                |             Name of the auxillary device. 
                |         oAuxillaryAxisValues
                |             List of Joint values retrieved for the given Auxillary device.
                |
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The auxillary device target was successfully
                |             retrieved.
                |         E_FAIL
                |             The auxillary device target could not be
                |             retrieved.
                | 
                |         Example:
                |             The following example sets the joint values correspoding to the
                |             target of the auxillary device in a robot motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim Device As Product
                |                ...
                |                Dim DeviceName As String
                |                DeviceName = "Mechanism.1"
                |                Dim JointTarget(1)
                |                objRobotmotion.GetAuxillaryAxisValues
                |                Device,DeviceName,JointTarget

        :param AnyObject i_device:
        :param str i_auxillary_axis:
        :param tuple o_auxillary_axis_values:
        :rtype: None
        """
        return self.robot_motion.GetAuxillaryAxisValues(i_device.com_object, i_auxillary_axis, o_auxillary_axis_values)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_auxillary_axis_values'
        # # vba_code = """
        # # Public Function get_auxillary_axis_values(robot_motion)
        # #     Dim iDevice (2)
        # #     robot_motion.GetAuxillaryAxisValues iDevice
        # #     get_auxillary_axis_values = iDevice
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_cartesian_target(self, o_cartesian_target: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetCartesianTarget(CATSafeArrayVariant
                | oCartesianTarget)
                | 
                |     Retrieves the Robot Cartesian target.
                | 
                |     Parameters:
                | 
                |         oCartesianTarget
                |             Cartesian Target(The Variant array containing the values in the
                |             sequence X,Y,Z,Yaw,Pitch,Roll) 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The cartesian target was successfully retrieved.
                |         E_FAIL
                |             The cartesian target could not be retrieved.
                | 
                |         Example:
                |             The following example gets the cartesian target for a robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim CartesianTarget(5)
                |                objRobotmotion.GetCartesianTarget
                |                CartesianTarget

        :param tuple o_cartesian_target:
        :rtype: None
        """
        return self.robot_motion.GetCartesianTarget(o_cartesian_target)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_cartesian_target'
        # # vba_code = """
        # # Public Function get_cartesian_target(robot_motion)
        # #     Dim oCartesianTarget (2)
        # #     robot_motion.GetCartesianTarget oCartesianTarget
        # #     get_cartesian_target = oCartesianTarget
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_config(self, o_config_number: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetConfig(short oConfigNumber)
                | 
                |     Retreives the Configuration.
                | 
                |     Parameters:
                | 
                |         oConfigNumber
                |             The Config as a Number. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Configuration was successfully retreived.
                |         E_FAIL
                |             The Configuration could not be retreived.
                | 
                |         Example:
                |             The following example retreives the Configuration for the robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim Config
                |                objRobotmotion.GetConfig Config

        :param int o_config_number:
        :rtype: None
        """
        return self.robot_motion.GetConfig(o_config_number)

    def get_joint_target(self, o_joint_target: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetJointTarget(CATSafeArrayVariant oJointTarget)
                | 
                |     Retrieves the Robot Joint target.
                | 
                |     Parameters:
                | 
                |         oJointTarget
                |             The List of Joint DOF values. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The joint target was successfully retrieved.
                |         E_FAIL
                |             The joint target could not be retrieved.
                | 
                |         Example:
                |             The following example retrieves the joint target of a robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim JointTarget(5)
                |                objRobotmotion.GetJointTarget JointTarget

        :param tuple o_joint_target:
        :rtype: None
        """
        return self.robot_motion.GetJointTarget(o_joint_target)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_joint_target'
        # # vba_code = """
        # # Public Function get_joint_target(robot_motion)
        # #     Dim oJointTarget (2)
        # #     robot_motion.GetJointTarget oJointTarget
        # #     get_joint_target = oJointTarget
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_motion_profile(self, o_motion_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetMotionProfile(AnyObject oMotionProfile)
                | 
                |     Retrieves Motion profile.
                | 
                |     Parameters:
                | 
                |         oMotionProfile
                |             The retrieved profile. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Motion Profile was successfully retrieved.
                |         E_FAIL
                |             The Motion Profile could not be retrieved.
                | 
                |         Example:
                |             The following example retrieves the Motion Profile for the robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim MotionProfile As String
                |                objRobotmotion.GetMotionProfile MotionProfile

        :param AnyObject o_motion_profile:
        :rtype: None
        """
        return self.robot_motion.GetMotionProfile(o_motion_profile.com_object)

    def get_motion_type(self, index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetMotionType(short index)
                | 
                |     Retrieves the type of Motion.
                | 
                |     Parameters:
                | 
                |         index
                |             The Motion Type
                |             JointMOVE = 0,
                |             LINEARMOVE = 1 ,
                |             PREDEFINED = 2,
                |             CIRCULAR = 3,
                |             CIRCULARVIA = 4,
                |             SLEW = 5
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The motion type was successfully obtained from the robot
                |             motion.
                |         E_FAIL
                |             The motion type could not be obtained.
                | 
                |         Example:
                |             The following example retrieves the motion type for a robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim MotionType
                |                objRobotmotion.GetMotionType MotionType

        :param int index:
        :rtype: None
        """
        return self.robot_motion.GetMotionType(index)

    def get_object_profile(self, o_obj_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetObjectProfile(AnyObject oObjProfile)
                | 
                |     Retrieves Object profile.
                | 
                |     Parameters:
                | 
                |         oObjProfile
                |             The retrieved profile. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The object Profile was successfully retrieved.
                |         E_FAIL
                |             The object Profile could not be retrieved.
                | 
                |         Example:
                |             The following example retrieves the object Profile for the robot
                |             motion.
                | 
                |                Dim objrobotmotion as robotmotion
                |                Dim objectProfile As String
                |                objrobotmotion.GetobjectProfile objectProfile

        :param AnyObject o_obj_profile:
        :rtype: None
        """
        return self.robot_motion.GetObjectProfile(o_obj_profile.com_object)

    def get_orientation_mode(self, index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOrientationMode(short index)
                | 
                |     Retrieves the TCP Orientation Mode.
                | 
                |     Parameters:
                | 
                |         index
                |             Orientation Mode (OneAxis = 0, TwoAxis = 1, ThreeAxis = 2, WristAxis = 3) 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Orientation Mode was successfully retrieved.
                |         E_FAIL
                |             The Orientation Mode could not be retrieved.
                | 
                |         Example:
                |             The following example sets the orientation mode for the robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim OrientationMode
                |                objRobotmotion.GetOrientationMode
                |                OrientationMode

        :param int index:
        :rtype: None
        """
        return self.robot_motion.GetOrientationMode(index)

    def get_tag_target(self, o_tag: Tag) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTagTarget(Tag oTag)
                | 
                |     Retrieves the underlying Tag Target.
                | 
                |     Parameters:
                | 
                |         oTag
                |             The underlying Tag. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The tag target was successfully retrieved.
                |         E_FAIL
                |             The tag target could not be retrieved.
                | 
                |         Example:
                |             The following example retrives the tag target for a robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim objTag as Tag
                |                objRobotmotion.GetTagTarget objTag

        :param Tag o_tag:
        :rtype: None
        """
        return self.robot_motion.GetTagTarget(o_tag.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_tag_target'
        # # vba_code = """
        # # Public Function get_tag_target(robot_motion)
        # #     Dim oTag (2)
        # #     robot_motion.GetTagTarget oTag
        # #     get_tag_target = oTag
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_target_type(self, index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTargetType(short index)
                | 
                |     Retrieves the Target Type.
                | 
                |     Parameters:
                | 
                |         index
                |             Type of the Target (Cartesian = 0, Joint = 1, Tag = 2, Home = 3). 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The target type was successfully obtained from the robot
                |             motion.
                |         E_FAIL
                |             The target type could not be obtained.
                | 
                |         Example:
                |             The following example retrieves the target type for a robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim TargetType
                |                objRobotmotion.GetTargetType TargetType

        :param int index:
        :rtype: None
        """
        return self.robot_motion.GetTargetType(index)

    def get_tool_profile(self, o_tool_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetToolProfile(AnyObject oToolProfile)
                | 
                |     Retrieves tool profile.
                | 
                |     Parameters:
                | 
                |         oToolProfile
                |             The retrieved tool profile. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Tool Profile was successfully retrieved.
                |         E_FAIL
                |             The Tool Profile could not be retrieved.
                | 
                |         Example:
                |             The following example retrieves the Tool Profile for the robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim ToolProfile As String
                |                objRobotmotion.GetToolProfile ToolProfile

        :param AnyObject o_tool_profile:
        :rtype: None
        """
        return self.robot_motion.GetToolProfile(o_tool_profile.com_object)

    def get_turn_numbers(self, o_turn_numbers: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTurnNumbers(CATSafeArrayVariant oTurnNumbers)
                | 
                |     Retrieves the Turn Numbers(or Turn signs) of the robot
                |     motion.
                | 
                |     Parameters:
                | 
                |         oTurnNumbers
                |             The underlying List of TurnNumbers (or turn signs).
                |             
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The turn numbers were successfully obtained.
                |         E_FAIL
                |             The turn numbers could not be obtained.
                | 
                |         Example:
                |             The following example retrives the turn numbers for a robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim TurnNumbers(4)
                |                objRobotmotion.GetTurnNumbers TurnNumbers

        :param tuple o_turn_numbers:
        :rtype: None
        """
        return self.robot_motion.GetTurnNumbers(o_turn_numbers)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_turn_numbers'
        # # vba_code = """
        # # Public Function get_turn_numbers(robot_motion)
        # #     Dim oTurnNumbers (2)
        # #     robot_motion.GetTurnNumbers oTurnNumbers
        # #     get_turn_numbers = oTurnNumbers
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_accuracy_profile(self, i_accuracy_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAccuracyProfile(AnyObject iAccuracyProfile)
                | 
                |     Sets the Accuracy profile.
                | 
                |     Parameters:
                | 
                |         iAccuracyProfile
                |             The Accuracy profile. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Accuracy Profile was successfully set.
                |         E_FAIL
                |             The Accuracy Profile could not be set.
                | 
                |         Example:
                |             The following example retrieves the Accuracy Profile for the robot
                |             Accuracy.
                | 
                |                Dim objRobotMotion as RobotMotion
                |                objRobotMotion.SetAccuracyProfile "Default"

        :param AnyObject i_accuracy_profile:
        :rtype: None
        """
        return self.robot_motion.SetAccuracyProfile(i_accuracy_profile.com_object)

    def set_auxillary_axis_home(self, i_device: AnyObject, i_auxillary_axis: str, i_home_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAuxillaryAxisHome(AnyObject iDevice,
                | CATBSTR iAuxillaryAxis,
                | CATBSTR iHomeName)
                | 
                |     Sets the underlying Auxillary device Home.
                | 
                |     Parameters:
                | 
                |         iDevice
                |             The Auxillary Device. 
                |         iAuxillaryAxis
                |             Name of the Auxillary Device. 
                |         iHomeName
                |             Home name set for the given Auxillary device. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The auxillary device target was successfully set.
                |         E_FAIL
                |             The auxillary device target could not be set.
                | 
                |         Example:
                |             The following example sets the home name correspoding to the target
                |             of the auxillary device in a robot motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim Device As Product
                |                ...
                |                Dim DeviceName As String
                |                DeviceName = "Mechanism.1"
                |                Dim HomeName As String
                |                HomeName = "Home.1"
                |                objRobotmotion.SetAuxillaryAxisHome HomeName

        :param AnyObject i_device:
        :param str i_auxillary_axis:
        :param str i_home_name:
        :rtype: None
        """
        return self.robot_motion.SetAuxillaryAxisHome(i_device.com_object, i_auxillary_axis, i_home_name)

    def set_auxillary_axis_values(
            self,
            i_device: AnyObject,
            i_auxillary_axis: str,
            i_auxillary_axis_values: tuple
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAuxillaryAxisValues(AnyObject iDevice,
                | CATBSTR iAuxillaryAxis,
                | CATSafeArrayVariant iAuxillaryAxisValues)
                | 
                |     Sets the Auxillary device Joint values.
                | 
                |     Parameters:
                | 
                |         iDevice
                |             Auxillary device (Mechanism) 
                |         iAuxillaryAxis
                |             Name of the Auxillary Device. 
                |         iAuxillaryAxisValues
                |             List of joint values of the device. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The auxillary device target was successfully set.
                |         E_FAIL
                |             The auxillary device target could not be set.
                | 
                |         Example:
                |             The following example sets the joint values correspoding to the
                |             target of the auxillary device in a robot motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim Device As Product
                |                ...
                |                Dim DeviceName As String
                |                DeviceName = "Mechanism.1"
                |                Dim JointTarget(1)
                |                JointTarget(0)=1.571
                |                JointTarget(1)=-0.785
                |                objRobotmotion.SetAuxillaryAxisValues
                |                Device,DeviceName,JointTarget

        :param AnyObject i_device:
        :param str i_auxillary_axis:
        :param tuple i_auxillary_axis_values:
        :rtype: None
        """
        return self.robot_motion.SetAuxillaryAxisValues(i_device.com_object, i_auxillary_axis, i_auxillary_axis_values)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auxillary_axis_values'
        # # vba_code = """
        # # Public Function set_auxillary_axis_values(robot_motion)
        # #     Dim iDevice (2)
        # #     robot_motion.SetAuxillaryAxisValues iDevice
        # #     set_auxillary_axis_values = iDevice
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_cartesian_target(self, i_cartesian_target: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCartesianTarget(CATSafeArrayVariant
                | iCartesianTarget)
                | 
                |     Sets the Robot Cartesian target.
                | 
                |     Parameters:
                | 
                |         iCartesianTarget
                |             Cartesian Target(The Variant array should contain the values in the
                |             sequence X,Y,Z,Yaw,Pitch,Roll) 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The cartesian target was successfully set.
                |         E_FAIL
                |             The cartesian target could not be set.
                | 
                |         Example:
                |             The following example Sets the cartesian target for a robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim CartesianTarget(5)
                |                CartesianTarget(0)=150
                |                CartesianTarget(1)=200
                |                CartesianTarget(2)=350
                |                CartesianTarget(3)=1.571
                |                CartesianTarget(4)=3.142
                |                CartesianTarget(5)=-0.785
                |                objRobotmotion.SetCartesianTarget
                |                CartesianTarget

        :param tuple i_cartesian_target:
        :rtype: None
        """
        return self.robot_motion.SetCartesianTarget(i_cartesian_target)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_cartesian_target'
        # # vba_code = """
        # # Public Function set_cartesian_target(robot_motion)
        # #     Dim iCartesianTarget (2)
        # #     robot_motion.SetCartesianTarget iCartesianTarget
        # #     set_cartesian_target = iCartesianTarget
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_config(self, i_config_number: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetConfig(short iConfigNumber)
                | 
                |     Sets the Configuration for the robot motion.
                | 
                |     Parameters:
                | 
                |         iConfigNumber
                |             The Config as a Number. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Configuration was successfully set.
                |         E_FAIL
                |             The Configuration could not be set.
                | 
                |         Example:
                |             The following example sets the configuration for the robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                objRobotmotion.SetConfig 1

        :param int i_config_number:
        :rtype: None
        """
        return self.robot_motion.SetConfig(i_config_number)

    def set_joint_target(self, i_joint_target: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetJointTarget(CATSafeArrayVariant iJointTarget)
                | 
                |     Sets the Robot Joint target.
                | 
                |     Parameters:
                | 
                |         iJointTarget
                |             The List of Joint DOF values. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The joint target was successfully set.
                |         E_FAIL
                |             The joint target could not be set.
                | 
                |         Example:
                |             The following example sets the joint target for a robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim JointTarget(5)
                |                JointTarget(0)=1.571
                |                JointTarget(1)=-0.785
                |                JointTarget(2)=3.142
                |                JointTarget(3)=0.38
                |                JointTarget(4)=1.57
                |                JointTarget(5)=0.6
                |                objRobotmotion.SetJointTarget JointTarget

        :param tuple i_joint_target:
        :rtype: None
        """
        return self.robot_motion.SetJointTarget(i_joint_target)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_joint_target'
        # # vba_code = """
        # # Public Function set_joint_target(robot_motion)
        # #     Dim iJointTarget (2)
        # #     robot_motion.SetJointTarget iJointTarget
        # #     set_joint_target = iJointTarget
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_motion_profile(self, i_motion_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMotionProfile(AnyObject iMotionProfile)
                | 
                |     Sets the Motion profile.
                | 
                |     Parameters:
                | 
                |         iMotionProfile
                |             The Motion profile. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Motion Profile was successfully set.
                |         E_FAIL
                |             The Motion Profile could not be set.
                | 
                |         Example:
                |             The following example retrieves the Motion Profile for the robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                objRobotmotion.SetMotionProfile "Default"

        :param AnyObject i_motion_profile:
        :rtype: None
        """
        return self.robot_motion.SetMotionProfile(i_motion_profile.com_object)

    def set_motion_type(self, index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMotionType(short index)
                | 
                |     Sets the type of Motion.
                | 
                |     Parameters:
                | 
                |         index
                |             The Motion Type
                |             JointMOVE = 0,
                |             LINEARMOVE = 1 ,
                |             PREDEFINED = 2,
                |             CIRCULAR = 3,
                |             CIRCULARVIA = 4, SLEW = 5
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The motion type was successfully set to the robot
                |             motion.
                |         E_FAIL
                |             The motion type could not be set.
                | 
                |         Example:
                |             The following example Sets the motion type for a robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                objRobotmotion.SetMotionType 1

        :param int index:
        :rtype: None
        """
        return self.robot_motion.SetMotionType(index)

    def set_object_profile(self, i_obj_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetObjectProfile(AnyObject iObjProfile)
                | 
                |     Sets the Object profile.
                | 
                |     Parameters:
                | 
                |         iObjProfile
                |             The Object profile. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Object Profile was successfully set.
                |         E_FAIL
                |             The Object Profile could not be set.
                | 
                |         Example:
                |             The following example retrieves the Object Profile for the robot
                |             Object.
                | 
                |                Dim objRobotMotion as RobotMotion
                |                Dim ObjectProfile As String
                |                objRobotMotion.SetObjectProfile "Default"

        :param AnyObject i_obj_profile:
        :rtype: None
        """
        return self.robot_motion.SetObjectProfile(i_obj_profile.com_object)

    def set_orientation_mode(self, index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOrientationMode(short index)
                | 
                |     Sets the TCP Orientation Mode.
                | 
                |     Parameters:
                | 
                |         index
                |             Orientation Mode (OneAxis = 0, TwoAxis = 1, ThreeAxis = 2, WristAxis = 3) 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Orientation Mode was successfully set.
                |         E_FAIL
                |             The Orientation Mode could not be set.
                | 
                |         Example:
                |             The following example sets the orientation mode for the robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                objRobotmotion.SetOrientationMode 1

        :param int index:
        :rtype: None
        """
        return self.robot_motion.SetOrientationMode(index)

    def set_tag_target(self, i_tag: Tag) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTagTarget(Tag iTag)
                | 
                |     Sets the Robot Tag target.
                | 
                |     Parameters:
                | 
                |         iTag
                |             The Tag to Set as the target. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The tag target was successfully set.
                |         E_FAIL
                |             The tag target could not be set.
                | 
                |         Example:
                |             The following example sets the tag target for a robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim objTag as Tag
                |                ...
                |                objRobotmotion.SetTagTarget objTag

        :param Tag i_tag:
        :rtype: None
        """
        return self.robot_motion.SetTagTarget(i_tag.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_tag_target'
        # # vba_code = """
        # # Public Function set_tag_target(robot_motion)
        # #     Dim iTag (2)
        # #     robot_motion.SetTagTarget iTag
        # #     set_tag_target = iTag
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tool_profile(self, i_tool_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetToolProfile(AnyObject iToolProfile)
                | 
                |     Sets the Tool profile.
                | 
                |     Parameters:
                | 
                |         iToolProfile
                |             The Tool profile. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Tool Profile was successfully set.
                |         E_FAIL
                |             The Tool Profile could not be set.
                | 
                |         Example:
                |             The following example retrieves the Tool Profile for the robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                objRobotmotion.SetToolProfile "Default"

        :param AnyObject i_tool_profile:
        :rtype: None
        """
        return self.robot_motion.SetToolProfile(i_tool_profile.com_object)

    def set_turn_numbers(self, i_turn_numbers: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTurnNumbers(CATSafeArrayVariant iTurnNumbers)
                | 
                |     Sets Turn Numbers or Turn signs for the robot motion.
                | 
                |     Parameters:
                | 
                |         iTurnNumbers
                |             The List of Turn numbers (or turn signs) to be set.
                |             
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The turn numbers were successfully set.
                |         E_FAIL
                |             The turn numbers could not be set.
                | 
                |         Example:
                |             The following example sets the turn numbers for a robot
                |             motion.
                | 
                |                Dim objRobotmotion as RobotMotion
                |                Dim TurnNumbers(4)
                |                TurnNumbers(0)=1
                |                TurnNumbers(1)=-1
                |                TurnNumbers(2)=0
                |                TurnNumbers(3)=2
                |                objRobotmotion.SetTurnNumbers TurnNumbers

        :param tuple i_turn_numbers:
        :rtype: None
        """
        return self.robot_motion.SetTurnNumbers(i_turn_numbers)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_turn_numbers'
        # # vba_code = """
        # # Public Function set_turn_numbers(robot_motion)
        # #     Dim iTurnNumbers (2)
        # #     robot_motion.SetTurnNumbers iTurnNumbers
        # #     set_turn_numbers = iTurnNumbers
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'RobotMotion(name="{self.name}")'
