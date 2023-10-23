#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_modeling_interfaces.swk_body_element import SWKBodyElement
from pycatia.dnb_human_modeling_interfaces.swkdof import SWKDOF
from pycatia.system_interfaces.any_object import AnyObject


class SWKSegment(SWKBodyElement):
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
                |                         SWKSegment
                | 
                | This interface deals with a segment of a manikin.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_segment = com_object

    @property
    def attach_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttachSize() As long (Read Only)
                | 
                |     Returns the number of objects currently attached to the
                |     segment.

        :rtype: int
        """

        return self.swk_segment.AttachSize

    @property
    def end_position_x(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndPositionX() As double (Read Only)
                | 
                |     Returns the global x coordinate of the endpoint of the
                |     segment.

        :rtype: float
        """

        return self.swk_segment.EndPositionX

    @property
    def end_position_y(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndPositionY() As double (Read Only)
                | 
                |     Returns the global y coordinate of the endpoint of the
                |     segment.

        :rtype: float
        """

        return self.swk_segment.EndPositionY

    @property
    def end_position_z(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndPositionZ() As double (Read Only)
                | 
                |     Returns the global z coordinate of the endpoint of the
                |     segment.

        :rtype: float
        """

        return self.swk_segment.EndPositionZ

    @property
    def is_dof_at0(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IsDOFAt0() As boolean (Read Only)
                | 
                |     Returns True if there is a DOF at index 0, False otherwise.

        :rtype: bool
        """

        return self.swk_segment.IsDOFAt0

    @property
    def is_dof_at1(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IsDOFAt1() As boolean (Read Only)
                | 
                |     Returns True if there is a DOF at index 1, False otherwise.

        :rtype: bool
        """

        return self.swk_segment.IsDOFAt1

    @property
    def is_dof_at2(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IsDOFAt2() As boolean (Read Only)
                | 
                |     Returns True if there is a DOF at index 2, False otherwise.

        :rtype: bool
        """

        return self.swk_segment.IsDOFAt2

    @property
    def is_on_hand(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IsOnHand() As boolean (Read Only)
                | 
                |     This property is True if this segment belongs to the manikin's hand.

        :rtype: bool
        """

        return self.swk_segment.IsOnHand

    @property
    def is_on_left_side(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IsOnLeftSide() As boolean (Read Only)
                | 
                |     This property is True if this segment is on the left side of the manikin.

        :rtype: bool
        """

        return self.swk_segment.IsOnLeftSide

    @property
    def is_on_right_side(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IsOnRightSide() As boolean (Read Only)
                | 
                |     This property is True if this segment is on the right side of the manikin.

        :rtype: bool
        """

        return self.swk_segment.IsOnRightSide

    @property
    def is_on_spine(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IsOnSpine() As boolean (Read Only)
                | 
                |     This property is True if this segment belongs to the manikin's spine.

        :rtype: bool
        """

        return self.swk_segment.IsOnSpine

    @property
    def length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Length() As double (Read Only)
                | 
                |     Returns the length of the segment, in centimeters.

        :rtype: float
        """

        return self.swk_segment.Length

    @property
    def mirror_segment(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MirrorSegment() As CATBaseDispatch (Read Only)
                | 
                |     This property returns the equivalent segment, but on the opposite side
                |     (ex.: right leg <-> left leg).

        :rtype: AnyObject
        """

        return AnyObject(self.swk_segment.MirrorSegment)

    @property
    def nb_do_fs(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NbDOFs() As long (Read Only)
                | 
                |     Returns the number of degrees of freedom on the current segment.
                |     Each segment can have up to three degrees of freedom.
                |     Therefore the value of this property will never be higher than 3.

        :rtype: int
        """

        return self.swk_segment.NbDOFs

    def apply_position(self, pi_position_increment: tuple, pi_start_segment: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ApplyPosition(CATSafeArrayVariant piPositionIncrement,
                | CATBSTR piStartSegment)
                | 
                |     Applies a new relative position for the segment.
                | 
                |     Parameters:
                | 
                |         piPositionIncrement
                |             The new position to combine with the segment's current
                |             position.
                |             This array must contain 12 numbers, and msut be initialized using
                |             the four columns of a transformation matrix. The first nine components
                |             represent the rotation matrix.
                |             The last three components represent the translation
                |             vector.
                |         piStartSegment
                |             The short name of the first segment of the kinematics chain. The
                |             short name specified has to identify a valid segment, which is an ancestor of
                |             the current one. For instance, is the segment to position is the right hand,
                |             then that start segment might be "RSArCl" (right clavicular). If the string
                |             "Default" is specified, then the start segment will be automatically chosen.
                |             
                | 
                |     Example:
                | 
                |           This example sets the segment to a 45-degree rotation
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
                |          myManikin.Body.GetItem("LSHaCPr").ApplyPosition
                |          myPosition

        :param tuple pi_position_increment:
        :param str pi_start_segment:
        :rtype: None
        """
        return self.swk_segment.ApplyPosition(pi_position_increment, pi_start_segment)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'apply_position'
        # # vba_code = """
        # # Public Function apply_position(swk_segment)
        # #     Dim piPositionIncrement (2)
        # #     swk_segment.ApplyPosition piPositionIncrement
        # #     apply_position = piPositionIncrement
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def attach(self, pi_object_to_attach: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Attach(AnyObject piObjectToAttach)
                | 
                |     Attach a geometry to the segment.
                | 
                |     Parameters:
                | 
                |         piObjectToAttach
                |             The object to attach. This object must be a movable object. Once
                |             the attach relationship is made, the object's postition will be updated every
                |             time the segment moves.

        :param AnyObject pi_object_to_attach:
        :rtype: None
        """
        return self.swk_segment.Attach(pi_object_to_attach.com_object)

    def create_reach_envelope(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateReachEnvelope()
                | 
                |     This method creates and displayed the reach envelope on the current
                |     segment. This segment must be part of the hand, otherwise an error code is
                |     returned.
                |     Property IsOnHand can be used to check whether the segment is located on
                |     the hand.

        :rtype: None
        """
        return self.swk_segment.CreateReachEnvelope()

    def destroy_reach_envelope(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub DestroyReachEnvelope()
                | 
                |     This method destroys the reach envelope previously created for this
                |     segment.

        :rtype: None
        """
        return self.swk_segment.DestroyReachEnvelope()

    def detach(self, pi_object_to_detach: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Detach(AnyObject piObjectToDetach)
                | 
                |     Detach a geometry previously attached to the segment.
                | 
                |     Parameters:
                | 
                |         piObjectToDetach
                |             The object to detach. This object's will no longer be driven by the
                |             segment's position.

        :param AnyObject pi_object_to_detach:
        :rtype: None
        """
        return self.swk_segment.Detach(pi_object_to_detach.com_object)

    def detach_all(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub DetachAll()
                | 
                |     Detach all objects attached so far to the segment.

        :rtype: None
        """
        return self.swk_segment.DetachAll()

    def get_attached_object(self, pi_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttachedObject(long piIndex) As AnyObject
                | 
                |     Retrieve one object currently attached to the segment.
                | 
                |     Parameters:
                | 
                |         piIndex
                |             The index of the object to retrieve. First attached object is at
                |             index 0.

        :param int pi_index:
        :rtype: AnyObject
        """
        return AnyObject(self.swk_segment.GetAttachedObject(pi_index))

    def get_dof(self, pi_dof_number: int) -> SWKDOF:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDOF(long piDOFNumber) As SWKDOF
                | 
                |     Returns a specific degree of freedom of the segment.
                |     A segment may have up to three degrees of freedom,
                |     and these are numbered from 0 to 2.
                |     However, the degrees of freedom do not always have
                |     consecutive indices. For instance the forearm
                |     has 2 DOFs, but these are numbered 0 and 2.
                |     That is why the set of DOFs under a segment cannot
                |     be properly accessed as if it was a collection.
                |     To loop through the degrees of freedom of a segment,
                |     one should test the value of properties IsDOFAt0, IsDOFAt1 or IsDOFAt2, and
                |     work with the
                |     DOF only if the value of one of the corresponding property
                |     is
                |     True.
                | 
                |     Parameters:
                | 
                |         piDOFNumber
                |             The index of the DOF to retrieve.
                |             This parameter must be either 0, 1 or 2.

        :param int pi_dof_number:
        :rtype: SWKDOF
        """
        return SWKDOF(self.swk_segment.GetDOF(pi_dof_number))

    def get_ik_offset(self, po_offset: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetIKOffset(CATSafeArrayVariant poOffset)
                | 
                |     Returns:
                |         The IK offset for this segment.

        :param tuple po_offset:
        :rtype: None
        """
        return self.swk_segment.GetIKOffset(po_offset)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_ik_offset'
        # # vba_code = """
        # # Public Function get_ik_offset(swk_segment)
        # #     Dim poOffset (2)
        # #     swk_segment.GetIKOffset poOffset
        # #     get_ik_offset = poOffset
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_ik_position(self, po_ik_position: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetIKPosition(CATSafeArrayVariant poIKPosition)
                | 
                |     Returns:
                |         The position used for IK on this segment.

        :param tuple po_ik_position:
        :rtype: None
        """
        return self.swk_segment.GetIKPosition(po_ik_position)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_ik_position'
        # # vba_code = """
        # # Public Function get_ik_position(swk_segment)
        # #     Dim poIKPosition (2)
        # #     swk_segment.GetIKPosition poIKPosition
        # #     get_ik_position = poIKPosition
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def is_attached(self, pi_object: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsAttached(AnyObject piObject) As boolean
                | 
                |     Returns:
                |         true if the object passed in the parameter is attached to the segment,
                |         false otherwise.

        :param AnyObject pi_object:
        :rtype: bool
        """
        return self.swk_segment.IsAttached(pi_object.com_object)

    def is_object_reachable(self, pi_object: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsObjectReachable(AnyObject piObject) As boolean
                | 
                |     Reachability check.
                | 
                |     Returns:
                |         true if the object passed is reachable by the segment, false otherwise.
                |         The position taken is that of the center of the object.

        :param AnyObject pi_object:
        :rtype: bool
        """
        return self.swk_segment.IsObjectReachable(pi_object.com_object)

    def is_reachable(self, pi_x: float, pi_y: float, pi_z: float) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsReachable(double piX,
                | double piY,
                | double piZ) As boolean
                | 
                |     Reachability check.
                | 
                |     Returns:
                |         true if the location expressed in the coordinates is reachable by the
                |         segment, false otherwise.

        :param float pi_x:
        :param float pi_y:
        :param float pi_z:
        :rtype: bool
        """
        return self.swk_segment.IsReachable(pi_x, pi_y, pi_z)

    def lock_posture(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LockPosture(long piDOFId)
                | 
                |     Lock the posture of the segment.

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_segment.LockPosture(pi_dof_id)

    def mirror_copy_angular_limitations(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub MirrorCopyAngularLimitations(long piDOFId)
                | 
                |     Mirror copy the angular limitations of the segment.

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_segment.MirrorCopyAngularLimitations(pi_dof_id)

    def mirror_copy_posture(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub MirrorCopyPosture()
                | 
                |     Copy the posture on the equivalent segment, on the other side of the
                |     manikin. For instance, it copies the posture from the right leg to the left
                |     leg.

        :rtype: None
        """
        return self.swk_segment.MirrorCopyPosture()

    def mirror_copy_pref_angles(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub MirrorCopyPrefAngles(long piDOFId)
                | 
                |     Mirror copy the preferred angles of the segment.

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_segment.MirrorCopyPrefAngles(pi_dof_id)

    def optimize(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Optimize(long piDOFId)
                | 
                |     Sets the limits to match the best PrefAngle for the DOF piDOFId

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_segment.Optimize(pi_dof_id)

    def remove_limits(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveLimits(long piDOFId)
                | 
                |     Removes the angular limitations of the segment.

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_segment.RemoveLimits(pi_dof_id)

    def reset_angular_limitations(self, pi_dof_id: int, pi_reset: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetAngularLimitations(long piDOFId,
                | long piReset)
                | 
                |     Reset the angular limitations of the segment depending on piReset: 0 -> 2
                |     OR 3 OR 4 depending of the first encountered. 1 -> 2 AND 3 AND 4 2 -> Unlock
                |     the value 3 -> Restore the angular limitations if it is "No Limits" 4 -> Set
                |     back the angular limitations to their default value (50.0%)

        :param int pi_dof_id:
        :param int pi_reset:
        :rtype: None
        """
        return self.swk_segment.ResetAngularLimitations(pi_dof_id, pi_reset)

    def reset_posture(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetPosture()
                | 
                |     Set the segment's posture back to its default position.

        :rtype: None
        """
        return self.swk_segment.ResetPosture()

    def reset_pref_angles(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetPrefAngles(long piDOFId)
                | 
                |     Reset the preferred angles of the segment.

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_segment.ResetPrefAngles(pi_dof_id)

    def set_percentage(self, pi_percentage: float, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPercentage(double piPercentage,
                | long piDOFId)
                | 
                |     Sets the angular limitations to a percentage for the DOF piDOFId

        :param float pi_percentage:
        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_segment.SetPercentage(pi_percentage, pi_dof_id)

    def set_position(self, pi_new_position: tuple, pi_start_segment: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPosition(CATSafeArrayVariant piNewPosition,
                | CATBSTR piStartSegment)
                | 
                |     Sets a new absolute position for the segment.
                | 
                |     Parameters:
                | 
                |         piNewPosition
                |             The new position to place the segment.
                |             This array must contain 12 numbers, and msut be initialized using
                |             the four columns of a transformation matrix. The first nine components
                |             represent the rotation matrix.
                |             The last three components represent the translation
                |             vector.
                |         piStartSegment
                |             The short name of the first segment of the kinematics chain. The
                |             short name specified has to identify a valid segment, which is an ancestor of
                |             the current one. For instance, is the segment to position is the right hand,
                |             then that start segment might be "RSArCl" (right clavicular). If the string
                |             "Default" is specified, then the start segment will be automatically chosen.
                |
                |     Example:
                | 
                |           This example sets the segment to a 45-degree rotation
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
                |          myManikin.Body.GetItem("LSHaCPr").SetPosition myPosition,
                |          "Default"

        :param tuple pi_new_position:
        :param str pi_start_segment:
        :rtype: None
        """
        return self.swk_segment.SetPosition(pi_new_position, pi_start_segment)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_position'
        # # vba_code = """
        # # Public Function set_position(swk_segment)
        # #     Dim piNewPosition (2)
        # #     swk_segment.SetPosition piNewPosition
        # #     set_position = piNewPosition
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def swap_angular_limitations(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SwapAngularLimitations(long piDOFId)
                | 
                |     Swap the angular limitations of the segment.

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_segment.SwapAngularLimitations(pi_dof_id)

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
        return self.swk_segment.SwapPosture()

    def swap_pref_angles(self, pi_dof_id: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SwapPrefAngles(long piDOFId)
                | 
                |     Swap the preferred angles of the segment.

        :param int pi_dof_id:
        :rtype: None
        """
        return self.swk_segment.SwapPrefAngles(pi_dof_id)

    def __repr__(self):
        return f'SWKSegment(name="{self.name}")'
