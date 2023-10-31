#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_modeling_interfaces.swk_body_element import SWKBodyElement
from pycatia.dnb_human_modeling_interfaces.swk_center_of_gravity import SWKCenterOfGravity
from pycatia.dnb_human_modeling_interfaces.swk_segment import SWKSegment


class SWKBody(SWKBodyElement):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBHumanModelingInterfaces.SWKBodyElement
                |                         SWKBody
                | 
                | This interface represents the body of the manikin.
                | It provides access to the manikin structure.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_body = com_object

    @property
    def center_of_gravity(self) -> SWKCenterOfGravity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CenterOfGravity() As SWKCenterOfGravity (Read
                | Only)
                | 
                |     Returns the center of gravity of the current manikin.

        :rtype: SWKCenterOfGravity
        """

        return SWKCenterOfGravity(self.swk_body.CenterOfGravity)

    @property
    def center_of_gravity_displayed(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CenterOfGravityDisplayed() As boolean
                | 
                |     Returns or sets the display of the center of gravity.

        :rtype: bool
        """

        return self.swk_body.CenterOfGravityDisplayed

    @center_of_gravity_displayed.setter
    def center_of_gravity_displayed(self, value: bool):
        """
        :param bool value:
        """

        self.swk_body.CenterOfGravityDisplayed = value

    @property
    def central_cone_displayed(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CentralConeDisplayed() As boolean
                | 
                |     Returns or sets the central cone display of the active line of sight.

        :rtype: bool
        """

        return self.swk_body.CentralConeDisplayed

    @central_cone_displayed.setter
    def central_cone_displayed(self, value: bool):
        """
        :param bool value:
        """

        self.swk_body.CentralConeDisplayed = value

    @property
    def cone_type_bounded_cone(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConeTypeBoundedCone() As boolean (Read Only)
                | 
                |     Returns or sets the cone type display to bounded cone for the peripheral
                |     and central cone.

        :rtype: bool
        """

        return self.swk_body.ConeTypeBoundedCone

    @property
    def cone_type_boundings(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConeTypeBoundings() As boolean (Read Only)
                | 
                |     Returns or sets the cone type display to boundings for the peripheral and
                |     central cone.

        :rtype: bool
        """

        return self.swk_body.ConeTypeBoundings

    @property
    def cone_type_flat(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConeTypeFlat() As boolean (Read Only)
                | 
                |     Returns or sets the cone type display to flat for the peripheral and
                |     central cone.

        :rtype: bool
        """

        return self.swk_body.ConeTypeFlat

    @property
    def cone_type_spherical(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConeTypeSpherical() As boolean (Read Only)
                | 
                |     Returns or sets the cone type display to spherical for the peripheral and
                |     central cone.

        :rtype: bool
        """

        return self.swk_body.ConeTypeSpherical

    @property
    def ellipses_displayed(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EllipsesDisplayed() As boolean
                | 
                |     Returns or sets the display of the manikin ellipses.

        :rtype: bool
        """

        return self.swk_body.EllipsesDisplayed

    @ellipses_displayed.setter
    def ellipses_displayed(self, value: bool):
        """
        :param bool value:
        """

        self.swk_body.EllipsesDisplayed = value

    @property
    def line_of_sight_displayed(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LineOfSightDisplayed() As boolean
                | 
                |     Returns or sets the display of the active line of sight.

        :rtype: bool
        """

        return self.swk_body.LineOfSightDisplayed

    @line_of_sight_displayed.setter
    def line_of_sight_displayed(self, value: bool):
        """
        :param bool value:
        """

        self.swk_body.LineOfSightDisplayed = value

    @property
    def memo(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Memo() As CATBSTR
                | 
                |     Returns or records miscellaneous user-added comments about the posture.

        :rtype: str
        """

        return self.swk_body.Memo

    @memo.setter
    def memo(self, value: str):
        """
        :param str value:
        """

        self.swk_body.Memo = value

    @property
    def number_of_segments(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumberOfSegments() As long (Read Only)
                | 
                |     Returns the number of segments of the body.

        :rtype: int
        """

        return self.swk_body.NumberOfSegments

    @property
    def peripheral_cone_displayed(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PeripheralConeDisplayed() As boolean
                | 
                |     Returns or sets the peripheral cone display of the active line of sight.

        :rtype: bool
        """

        return self.swk_body.PeripheralConeDisplayed

    @peripheral_cone_displayed.setter
    def peripheral_cone_displayed(self, value: bool):
        """
        :param bool value:
        """

        self.swk_body.PeripheralConeDisplayed = value

    @property
    def referential(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Referential() As CATBSTR
                | 
                |     Returns or sets the referential of the manikin. Possible values are
                |     "HPoint", "EyePoint", "LeftFoot", "RightFoot", "LowestFoot", "BetweenFeet" and
                |     "Crotch". If this manikin is a forearm model, than the possible values are
                |     either "LeftHand" or "RightHand".
                | 
                |     Example:
                | 
                |           myManikin.Body.Referential = "LowestFoot"

        :rtype: str
        """

        return self.swk_body.Referential

    @referential.setter
    def referential(self, value: str):
        """
        :param str value:
        """

        self.swk_body.Referential = value

    @property
    def referential_displayed(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReferentialDisplayed() As boolean
                | 
                |     Returns or sets the display of the referential.

        :rtype: bool
        """

        return self.swk_body.ReferentialDisplayed

    @referential_displayed.setter
    def referential_displayed(self, value: bool):
        """
        :param bool value:
        """

        self.swk_body.ReferentialDisplayed = value

    @property
    def segments_displayed(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SegmentsDisplayed() As boolean
                | 
                |     Returns or sets the display of the segments.

        :rtype: bool
        """

        return self.swk_body.SegmentsDisplayed

    @segments_displayed.setter
    def segments_displayed(self, value: bool):
        """
        :param bool value:
        """

        self.swk_body.SegmentsDisplayed = value

    @property
    def skin_displayed(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SkinDisplayed() As boolean
                | 
                |     Returns or sets the display of the manikin surfaces (skin).

        :rtype: bool
        """

        return self.swk_body.SkinDisplayed

    @skin_displayed.setter
    def skin_displayed(self, value: bool):
        """
        :param bool value:
        """

        self.swk_body.SkinDisplayed = value

    @property
    def skin_resolution(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SkinResolution() As long
                | 
                |     Returns or sets the manikin skin resolution.
                |     The valid values range from 4 to 128.

        :rtype: int
        """

        return self.swk_body.SkinResolution

    @skin_resolution.setter
    def skin_resolution(self, value: int):
        """
        :param int value:
        """

        self.swk_body.SkinResolution = value

    def apply_position(self, pi_position_increment: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ApplyPosition(CATSafeArrayVariant piPositionIncrement)
                | 
                |     Sets a new relative manikin position.
                | 
                |     Parameters:
                | 
                |         piPositionIncrement
                |             The new position to combine with the manikin's current
                |             position.
                |             This array must contain 12 numbers, and msut be initialized using
                |             the four columns of a transformation matrix. The first nine components
                |             represent the rotation matrix.
                |             The last three components represent the translation
                |             vector.
                | 
                |     Example:
                | 
                |           This example sets the manikin to a 45-degree rotation
                |           around
                |          the x axis and at a (10, 20, 30) translation from the
                |          origin.
                |
                |          Dim myPosition(11)
                |          'Rotation (45 degrees around the x axis)
                |          myPosition(0)  = 1.000
                |          myPosition(1)  = 0
                |          myPosition(2)  = 0
                |          myPosition(3)  = 0
                |          myPosition(4)  = 0.707
                |          myPosition(5)  = 0.707
                |          myPosition(6)  = 0
                |          myPosition(7)  = -0.707
                |          myPosition(8)  = 0.707
                |          'Translation vector (10,20,30)
                |          myPosition(9)  = 10.000
                |          myPosition(10) = 20.000
                |          myPosition(11) = 30.000
                |          myManikin.Body.ApplyPosition myPosition

        :param tuple pi_position_increment:
        :rtype: None
        """
        return self.swk_body.ApplyPosition(pi_position_increment)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'apply_position'
        # # vba_code = """
        # # Public Function apply_position(swk_body)
        # #     Dim piPositionIncrement (2)
        # #     swk_body.ApplyPosition piPositionIncrement
        # #     apply_position = piPositionIncrement
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_segment(self, pi_index: int) -> SWKSegment:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSegment(long piIndex) As SWKSegment
                | 
                |     Returns a specific segment of the body, based on an index.
                | 
                |     Parameters:
                | 
                |         piIndex
                |             The index of the segment to retrieve.
                |             The first segment is at index 0.
                |             The value of this parameter should not be higher than the number of
                |             segments on the body, minus 1.

        :param int pi_index:
        :rtype: SWKSegment
        """
        return SWKSegment(self.swk_body.GetSegment(pi_index))

    def is_balanced(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsBalanced() As boolean
                | 
                |     Returns:
                |         True if the manikin is well-balaned, False otherwise.
                |         Being well balanced means that the center of gravity of the
                |         manikin
                |         falls inside its basis of support, given the manikin's current posture.

        :rtype: bool
        """
        return self.swk_body.IsBalanced()

    def lock_posture(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LockPosture(long piDOFId)
                | 
                |     Lock the body in the given dof

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_body.LockPosture(pi_dof_id)

    def reset_angular_limitations(self, pi_dof_id: int, pi_reset: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetAngularLimitations(long piDOFId,
                | long piReset)
                | 
                |     Resets the angular limitations depending on the param piReset: 0 -> 2 OR 3
                |     OR 4 depending of the first encountered. 1 -> 2 AND 3 AND 4 2 -> Unlock the
                |     value 3 -> Restore the angular limitations if it is "No Limits" 4 -> Set back
                |     the angular limitations to their default value (50.0%)

        :param int pi_dof_id:
        :param int pi_reset:
        :rtype: None
        """
        return self.swk_body.ResetAngularLimitations(pi_dof_id, pi_reset)

    def reset_attaches(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetAttaches()
                | 
                |     Reset the attaches of the body.

        :rtype: None
        """
        return self.swk_body.ResetAttaches()

    def reset_ik_offsets(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetIKOffsets()
                | 
                |     Reset the offsets of the body.

        :rtype: None
        """
        return self.swk_body.ResetIKOffsets()

    def reset_posture(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetPosture()
                | 
                |     Set the manikin to the default (standing) posture.

        :rtype: None
        """
        return self.swk_body.ResetPosture()

    def reset_pref_angles(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetPrefAngles(long piDOFId)
                | 
                |     Reset the pref angles of the body.

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_body.ResetPrefAngles(pi_dof_id)

    def set_cone_type_bounded_cone(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetConeTypeBoundedCone()

        :rtype: None
        """
        return self.swk_body.SetConeTypeBoundedCone()

    def set_cone_type_boundings(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetConeTypeBoundings()

        :rtype: None
        """
        return self.swk_body.SetConeTypeBoundings()

    def set_cone_type_flat(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetConeTypeFlat()

        :rtype: None
        """
        return self.swk_body.SetConeTypeFlat()

    def set_cone_type_spherical(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetConeTypeSpherical()

        :rtype: None
        """
        return self.swk_body.SetConeTypeSpherical()

    def set_position(self, pi_new_position: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPosition(CATSafeArrayVariant piNewPosition)
                | 
                |     Sets a new absolute manikin position.
                | 
                |     Parameters:
                | 
                |         piNewPosition
                |             The new position to place the manikin.
                |             This array must contain 12 numbers, and msut be initialized using
                |             the four columns of a transformation matrix. The first nine components
                |             represent the rotation matrix.
                |             The last three components represent the translation
                |             vector.
                | 
                |     Example:
                | 
                |           This example sets the manikin to a 45-degree rotation
                |           around
                |          the x axis and at a (10, 20, 30) translation from the
                |          origin.
                |
                |          Dim myPosition(11)
                |          'Rotation (45 degrees around the x axis)
                |          myPosition(0)  = 1.000
                |          myPosition(1)  = 0
                |          myPosition(2)  = 0
                |          myPosition(3)  = 0
                |          myPosition(4)  = 0.707
                |          myPosition(5)  = 0.707
                |          myPosition(6)  = 0
                |          myPosition(7)  = -0.707
                |          myPosition(8)  = 0.707
                |          'Translation vector (10,20,30)
                |          myPosition(9)  = 10.000
                |          myPosition(10) = 20.000
                |          myPosition(11) = 30.000
                |          myManikin.Body.SetPosition myPosition

        :param tuple pi_new_position:
        :rtype: None
        """
        return self.swk_body.SetPosition(pi_new_position)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_position'
        # # vba_code = """
        # # Public Function set_position(swk_body)
        # #     Dim piNewPosition (2)
        # #     swk_body.SetPosition piNewPosition
        # #     set_position = piNewPosition
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_posture(self, pi_posture_spec: int, pi_keep_referential: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPosture(SWKPostureSpec piPostureSpec,
                | boolean piKeepReferential)
                | 
                |     Set the manikin to a specific predefined posture.
                |     Predefined postures include "Stand", "Sit", "Reach"
                |     and "Kneel".
                | 
                |     See also:
                |         SWKPostureSpec 
                |     Parameters:
                | 
                |         piKeepReferential
                |             keeps the referential after the change of the
                |             posture

        :param int pi_posture_spec: enum swk_posture_spec
        :param bool pi_keep_referential:
        :rtype: None
        """
        return self.swk_body.SetPosture(pi_posture_spec, pi_keep_referential)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_posture'
        # # vba_code = """
        # # Public Function set_posture(swk_body)
        # #     Dim piPostureSpec (2)
        # #     swk_body.SetPosture piPostureSpec
        # #     set_posture = piPostureSpec
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_to_best_posture(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetToBestPosture()
                | 
                |     Set the manikin to the posture that will provide it its maximum score.
                |     When the manikin is in that posture, then the output of property
                |     PosturalScore will be the same as that of property MaxPosturalScore.

        :rtype: None
        """
        return self.swk_body.SetToBestPosture()

    def swap_angular_limitations(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SwapAngularLimitations(long piDOFId)
                | 
                |     Swap the angular limitations of the body.

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_body.SwapAngularLimitations(pi_dof_id)

    def swap_posture(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SwapPosture()
                | 
                |     Swap the posture with the equivalent segment, on the other side of the
                |     manikin. For instance, the right leg takes the posture of the left leg, and
                |     vice versa.

        :rtype: None
        """
        return self.swk_body.SwapPosture()

    def swap_pref_angles(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SwapPrefAngles(long piDOFId)
                | 
                |     Swap the preferred angles of the body.

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_body.SwapPrefAngles(pi_dof_id)

    def __repr__(self):
        return f'SWKBody(name="{self.name}")'
