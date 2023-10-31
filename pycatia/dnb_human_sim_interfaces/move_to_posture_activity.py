#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_modeling_interfaces.swkik_constraint import SWKIKConstraint
from pycatia.dnb_human_sim_interfaces.worker_activity import WorkerActivity
from pycatia.product_structure_interfaces.product import Product


class MoveToPostureActivity(WorkerActivity):
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
                |                         DNBHumanSimInterfaces.WorkerActivity
                |                             MoveToPostureActivity
                | 
                | The object that represents an MoveToPosture(MTP) Activity.
                | MTP allows to store a target posture for a specific manikin at a specific time
                | in the process. When a MTP is created, the current posture of the manikin along
                | with any constraints (if any).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.move_to_posture_activity = com_object

    @property
    def acceleration_percent(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AccelerationPercent() As double
                | 
                |     Returns or Sets Acceleration Percentage

        :rtype: float
        """

        return self.move_to_posture_activity.AccelerationPercent

    @acceleration_percent.setter
    def acceleration_percent(self, value: float):
        """
        :param float value:
        """

        self.move_to_posture_activity.AccelerationPercent = value

    @property
    def corner_rounding(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CornerRounding() As double
                | 
                |     Returns or Sets Corner Rounding

        :rtype: float
        """

        return self.move_to_posture_activity.CornerRounding

    @corner_rounding.setter
    def corner_rounding(self, value: float):
        """
        :param float value:
        """

        self.move_to_posture_activity.CornerRounding = value

    @property
    def motion_basis(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MotionBasis() As HTSMotionBasis
                | 
                |     Returns or Sets Motion-Basis (see HTSMotionBasis for list of possible
                |     values)

        :return: enum hts_motion_basis
        :rtype: int
        """

        return self.move_to_posture_activity.MotionBasis

    @motion_basis.setter
    def motion_basis(self, value: int):
        """
        :param int value: enum hts_motion_basis
        """

        self.move_to_posture_activity.MotionBasis = value

    @property
    def referential(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Referential() As HTSManikinReferential
                | 
                |     Returns or Sets Manikin Referential (see HTSManikinReferential for list of
                |     possible values)

        :return: enum hts_manikin_referential
        :rtype: int
        """

        return self.move_to_posture_activity.Referential

    @referential.setter
    def referential(self, value: int):
        """
        :param int value: enum hts_manikin_referential
        """

        self.move_to_posture_activity.Referential = value

    @property
    def speed_percent(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SpeedPercent() As double
                | 
                |     Returns or Sets Speed Percentage

        :rtype: float
        """

        return self.move_to_posture_activity.SpeedPercent

    @speed_percent.setter
    def speed_percent(self, value: float):
        """
        :param float value:
        """

        self.move_to_posture_activity.SpeedPercent = value

    def add_constraint(self, pi_constraint: SWKIKConstraint) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddConstraint(SWKIKConstraint piConstraint)
                | 
                |     Adds the given constraint to MoveToPosture activity
                | 
                |     Parameters:
                | 
                |         piConstraint
                |             Constraint to be added. (see 
                | 
                |         SWKIKConstraint for list of possible values)

        :param SWKIKConstraint pi_constraint:
        :rtype: None
        """
        return self.move_to_posture_activity.AddConstraint(pi_constraint.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_constraint'
        # # vba_code = """
        # # Public Function add_constraint(move_to_posture_activity)
        # #     Dim piConstraint (2)
        # #     move_to_posture_activity.AddConstraint piConstraint
        # #     add_constraint = piConstraint
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def apply_posture_to_manikin(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ApplyPostureToManikin()
                | 
                |     Set the MoveToPosture(MTP) Activity's DegreeOfFreedom(DOF) values onto
                |     Manikin (which owns this MTP activity).

        :rtype: None
        """
        return self.move_to_posture_activity.ApplyPostureToManikin()

    def get_constraint(self, i_index: int) -> SWKIKConstraint:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetConstraint(long iIndex) As SWKIKConstraint
                | 
                |     Returns the constraint at given index
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index in the constraint-list to be retrieved 
                | 
                |     Returns:
                |         pioConstraint Constraint at given index (see SWKIKConstraint for list
                |         of possible values)

        :param int i_index:
        :rtype: SWKIKConstraint
        """
        return SWKIKConstraint(self.move_to_posture_activity.GetConstraint(i_index))

    def get_joint_values(self, o_joint_vals: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetJointValues(CATSafeArrayVariant oJointVals)
                | 
                |     Gets the Manikin's Position and Posture values in 137 doubles. (Array
                |     includeds Position information - first 6 values represent X,Y,Z and R,P,Y value
                |     of Manikin w.r.to its Father.)
                | 
                |     Parameters:
                | 
                |         oJointVals
                |             Joint Values

        :param tuple o_joint_vals:
        :rtype: None
        """
        return self.move_to_posture_activity.GetJointValues(o_joint_vals)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_joint_values'
        # # vba_code = """
        # # Public Function get_joint_values(move_to_posture_activity)
        # #     Dim oJointVals (2)
        # #     move_to_posture_activity.GetJointValues oJointVals
        # #     get_joint_values = oJointVals
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_number_of_constraints(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetNumberOfConstraints() As long
                | 
                |     Returns the number of constraints on the MoveToPosture
                |     activity
                | 
                |     Returns:
                |         iNumber Number of Constraints

        :rtype: int
        """
        return self.move_to_posture_activity.GetNumberOfConstraints()

    def get_part_relation(self, e_ee: int, o_product: Product, o_offset_trans: tuple) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPartRelation(HTSEndEffector eEE,
                | Product oProduct,
                | CATSafeArrayVariant oOffsetTrans) As boolean
                | 
                |     DEPRECATED. DO NOT USE

        :param int e_ee: enum hts_end_effector
        :param Product o_product:
        :param tuple o_offset_trans:
        :rtype: bool
        """
        return self.move_to_posture_activity.GetPartRelation(e_ee, o_product.com_object, o_offset_trans)

    def get_position(self, o_trans_matrix: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetPosition(CATSafeArrayVariant oTransMatrix)
                | 
                |     This gets the position value in 12 doubles
                | 
                |     Parameters:
                | 
                |         oTransMatrix
                |             The first nine represent succcessively the components of the
                |             x-axis, y-axis, and z-axis. The last three represent the coordinates of the
                |             origin point.

        :param tuple o_trans_matrix:
        :rtype: None
        """
        return self.move_to_posture_activity.GetPosition(o_trans_matrix)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_position'
        # # vba_code = """
        # # Public Function get_position(move_to_posture_activity)
        # #     Dim oTransMatrix (2)
        # #     move_to_posture_activity.GetPosition oTransMatrix
        # #     get_position = oTransMatrix
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_posture_values(self, o_pos_vals: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetPostureValues(CATSafeArrayVariant oPosVals)
                | 
                |     Gets the Manikin's Posture values in 131 doubles. (This array excludes
                |     Position information)
                | 
                |     Parameters:
                | 
                |         oPosVals
                |             Posture values

        :param tuple o_pos_vals:
        :rtype: None
        """
        return self.move_to_posture_activity.GetPostureValues(o_pos_vals)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_posture_values'
        # # vba_code = """
        # # Public Function get_posture_values(move_to_posture_activity)
        # #     Dim oPosVals (2)
        # #     move_to_posture_activity.GetPostureValues oPosVals
        # #     get_posture_values = oPosVals
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_segment_values(self, in_seg_name: str, o_dof_vals: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetSegmentValues(CATBSTR inSegName,
                | CATSafeArrayVariant oDofVals)
                | 
                |     Gets the DOF values of the given segment from MoveToPosture
                |     activity
                | 
                |     Parameters:
                | 
                |         inSegName
                |             Name of the Segment 
                |         oDofVals
                |             Dof values of constraint, array of size 3

        :param str in_seg_name:
        :param tuple o_dof_vals:
        :rtype: None
        """
        return self.move_to_posture_activity.GetSegmentValues(in_seg_name, o_dof_vals)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_segment_values'
        # # vba_code = """
        # # Public Function get_segment_values(move_to_posture_activity)
        # #     Dim inSegName (2)
        # #     move_to_posture_activity.GetSegmentValues inSegName
        # #     get_segment_values = inSegName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def has_part_relation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasPartRelation() As boolean
                | 
                |     DEPRECATED. DO NOT USE

        :rtype: bool
        """
        return self.move_to_posture_activity.HasPartRelation()

    def remove_constraint(self, pi_constraint: SWKIKConstraint) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveConstraint(SWKIKConstraint piConstraint)
                | 
                |     Removes the given constraint from MoveToPosture activity
                | 
                |     Parameters:
                | 
                |         piConstraint
                |             Constraint to be removed. (see 
                | 
                |         SWKIKConstraint for list of possible values)

        :param SWKIKConstraint pi_constraint:
        :rtype: None
        """
        return self.move_to_posture_activity.RemoveConstraint(pi_constraint.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_constraint'
        # # vba_code = """
        # # Public Function remove_constraint(move_to_posture_activity)
        # #     Dim piConstraint (2)
        # #     move_to_posture_activity.RemoveConstraint piConstraint
        # #     remove_constraint = piConstraint
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_current_constraint_set(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCurrentConstraintSet()
                | 
                |     Set the current Constraints existing on Manikin onto MoveToPosture activity

        :rtype: None
        """
        return self.move_to_posture_activity.SetCurrentConstraintSet()

    def set_joint_values(self, o_joint_vals: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetJointValues(CATSafeArrayVariant oJointVals)
                | 
                |     Sets the Manikin's Position and Posture values with 137 doubles. (Array
                |     should includes Position information - first 6 values represent X,Y,Z and R,P,Y
                |     value of Manikin w.r.to its Father.)
                | 
                |     Parameters:
                | 
                |         oJointVals
                |             Joint Values

        :param tuple o_joint_vals:
        :rtype: None
        """
        return self.move_to_posture_activity.SetJointValues(o_joint_vals)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_joint_values'
        # # vba_code = """
        # # Public Function set_joint_values(move_to_posture_activity)
        # #     Dim oJointVals (2)
        # #     move_to_posture_activity.SetJointValues oJointVals
        # #     set_joint_values = oJointVals
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_part_relation(self, e_ee: int, o_product: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPartRelation(HTSEndEffector eEE,
                | Product oProduct)
                | 
                |     DEPRECATED. DO NOT USE

        :param int e_ee: enum hts_end_effector
        :param Product o_product:
        :rtype: None
        """
        return self.move_to_posture_activity.SetPartRelation(e_ee, o_product.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_part_relation'
        # # vba_code = """
        # # Public Function set_part_relation(move_to_posture_activity)
        # #     Dim eEE (2)
        # #     move_to_posture_activity.SetPartRelation eEE
        # #     set_part_relation = eEE
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_part_relation_with_offset(self, e_ee: int, o_product: Product, o_offset_trans: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPartRelationWithOffset(HTSEndEffector eEE,
                | Product oProduct,
                | CATSafeArrayVariant oOffsetTrans)
                | 
                |     DEPRECATED. DO NOT USE

        :param int e_ee: enum hts_end_effector
        :param Product o_product:
        :param tuple o_offset_trans:
        :rtype: None
        """
        return self.move_to_posture_activity.SetPartRelationWithOffset(e_ee, o_product.com_object, o_offset_trans)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_part_relation_with_offset'
        # # vba_code = """
        # # Public Function set_part_relation_with_offset(move_to_posture_activity)
        # #     Dim eEE (2)
        # #     move_to_posture_activity.SetPartRelationWithOffset eEE
        # #     set_part_relation_with_offset = eEE
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_position(self, o_trans_matrix: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPosition(CATSafeArrayVariant oTransMatrix)
                | 
                |     Sets the Manikin's position value in the MoveToPosture Activity. ( Pos.
                |     vals are w.r.to Manikin's Father )
                | 
                |     Parameters:
                | 
                |         oTransMatrix
                |             The array initialized with the components to set to the Manikin's
                |             position. The first nine represent succcessively the components of the x-axis,
                |             y-axis, and z-axis. The last three represent the coordinates of the origin
                |             point. 
                | 
                |     Example:
                | 
                |           This example sets the Position of Manikin
                |          oTransMatrix for MoveToPosture oMTP
                |
                |          Dim oTransMatrix( 11 )
                |          'Rotation( 45 degrees around the Z axis) components
                |          ' x axis components
                |          oTransMatrix( 0 ) = 0.707
                |          oTransMatrix( 1 ) = 0.707
                |          oTransMatrix( 2 ) = 0.0
                |          ' y axis components
                |          oTransMatrix( 3 ) = -0.707
                |          oTransMatrix( 4 ) = 0.707
                |          oTransMatrix( 5 ) = 0
                |          ' z axis components
                |          oTransMatrix( 6 ) = 0
                |          oTransMatrix( 7 ) = 0
                |          oTransMatrix( 8 ) = 1
                |          ' origin point coordinates
                |          oTransMatrix( 9 ) = 0
                |          oTransMatrix( 10 ) = 0
                |          oTransMatrix( 11 ) = 947.0
                | 
                |          oMTP.SetPosition(oTransMatrix)

        :param tuple o_trans_matrix:
        :rtype: None
        """
        return self.move_to_posture_activity.SetPosition(o_trans_matrix)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_position'
        # # vba_code = """
        # # Public Function set_position(move_to_posture_activity)
        # #     Dim oTransMatrix (2)
        # #     move_to_posture_activity.SetPosition oTransMatrix
        # #     set_position = oTransMatrix
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_posture_values(self, o_pos_vals: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPostureValues(CATSafeArrayVariant oPosVals)
                | 
                |     Sets the Manikin's Posture values with 131 values
                | 
                |     Parameters:
                | 
                |         oPosVals
                |             Posture values

        :param tuple o_pos_vals:
        :rtype: None
        """
        return self.move_to_posture_activity.SetPostureValues(o_pos_vals)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_posture_values'
        # # vba_code = """
        # # Public Function set_posture_values(move_to_posture_activity)
        # #     Dim oPosVals (2)
        # #     move_to_posture_activity.SetPostureValues oPosVals
        # #     set_posture_values = oPosVals
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_segment_values(self, in_seg_name: str, o_dof_vals: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSegmentValues(CATBSTR inSegName,
                | CATSafeArrayVariant oDofVals)
                | 
                |     Sets the given DOF values for Segments from MoveToPosture
                |     activity
                | 
                |     Parameters:
                | 
                |         inSegName
                |             Name of the Segment 
                |         oDofVals
                |             Dof values of constraint, array of size 3

        :param str in_seg_name:
        :param tuple o_dof_vals:
        :rtype: None
        """
        return self.move_to_posture_activity.SetSegmentValues(in_seg_name, o_dof_vals)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_segment_values'
        # # vba_code = """
        # # Public Function set_segment_values(move_to_posture_activity)
        # #     Dim inSegName (2)
        # #     move_to_posture_activity.SetSegmentValues inSegName
        # #     set_segment_values = inSegName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MoveToPostureActivity(name="{self.name}")'
