#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_sim_interfaces.worker_activity import WorkerActivity


class WalkActivity(WorkerActivity):
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
                |                             WalkActivity

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.walk_activity = com_object

    @property
    def body_pose(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BodyPose() As HTSBodyPoseOptions
                | 
                |     Returns or Sets Body Posture option (see HTSBodyPoseOptions for list of
                |     possible values)

        :return: enum hts_body_pose_options
        :rtype: int
        """

        return self.walk_activity.BodyPose

    @body_pose.setter
    def body_pose(self, value: int):
        """
        :param int value: enum hts_body_pose_options
        """

        self.walk_activity.BodyPose = value

    @property
    def motion_basis(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MotionBasis() As HTSWalkMotionBasis
                | 
                |     Returns or Sets Motion-Basis (see HTSWalkMotionBasis for list of possible
                |     values)

        :return: enum hts_walk_motion_basis
        :rtype: int
        """

        return self.walk_activity.MotionBasis

    @motion_basis.setter
    def motion_basis(self, value: int):
        """
        :param int value: enum hts_walk_motion_basis
        """

        self.walk_activity.MotionBasis = value

    @property
    def stride(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Stride() As HTSStrideOptions
                | 
                |     Returns or Sets Stride option (see HTSStrideOptions for list of possible
                |     values)

        :return: enum hts_stride_options
        :rtype: int
        """

        return self.walk_activity.Stride

    @stride.setter
    def stride(self, value: int):
        """
        :param int value: enum hts_stride_options
        """

        self.walk_activity.Stride = value

    @property
    def swing(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Swing() As HTSSwingOptions
                | 
                |     Returns or Sets Swing option (see HTSSwingOptions for list of possible
                |     values)

        :return: enum hts_swing_options
        :rtype: int
        """

        return self.walk_activity.Swing

    @swing.setter
    def swing(self, value: int):
        """
        :param int value: enum hts_swing_options
        """

        self.walk_activity.Swing = value

    @property
    def user_speed(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UserSpeed() As double
                | 
                |     Returns or Sets Speed for Walk Activity

        :rtype: float
        """

        return self.walk_activity.UserSpeed

    @user_speed.setter
    def user_speed(self, value: float):
        """
        :param float value:
        """

        self.walk_activity.UserSpeed = value

    @property
    def user_time(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UserTime() As double
                | 
                |     Returns or Sets Time for Walk Activity

        :rtype: float
        """

        return self.walk_activity.UserTime

    @user_time.setter
    def user_time(self, value: float):
        """
        :param float value:
        """

        self.walk_activity.UserTime = value

    @property
    def walk_length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WalkLength() As double (Read Only)
                | 
                |     Returns WalkLength for Walk Activity

        :rtype: float
        """

        return self.walk_activity.WalkLength

    def get_walk_curve_def_points(self, i_num_points: int, ad_points: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetWalkCurveDefPoints(long iNumPoints,
                | CATSafeArrayVariant adPoints)
                | 
                |     This gets the Walk Path definition Point
                | 
                |     Parameters:
                | 
                |         iNumPoints
                |             Number of Coplanar-Points defining the Walk Path in Plane
                |             
                |         adPoints
                |             Point values x1,y1,z1 , x2,y2,z2, .... Area of Plane coordinates
                |             User needs to pass in sufficiently large-sized
                |             array

        :param int i_num_points:
        :param tuple ad_points:
        :rtype: None
        """
        return self.walk_activity.GetWalkCurveDefPoints(i_num_points, ad_points)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_walk_curve_def_points'
        # # vba_code = """
        # # Public Function get_walk_curve_def_points(walk_activity)
        # #     Dim iNumPoints (2)
        # #     walk_activity.GetWalkCurveDefPoints iNumPoints
        # #     get_walk_curve_def_points = iNumPoints
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
                |     Returns if there is any PartRelation
                | 
                |     Returns:
                |         bFlag TRUE, if there exist any Part-Relation

        :rtype: bool
        """
        return self.walk_activity.HasPartRelation()

    def set_walk_curve_def_points(self, i_num_points: int, ad_points: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetWalkCurveDefPoints(long iNumPoints,
                | CATSafeArrayVariant adPoints)
                | 
                |     This sets the Walk Path definition Point
                | 
                |     Parameters:
                | 
                |         iNumPoints
                |             Number of Coplanar-Points defining the Walk Path in Plane
                |             
                |         adPoints
                |             Point values x1,y1,z1 , x2,y2,z2, .... Area of Plane
                |             coordinates

        :param int i_num_points:
        :param tuple ad_points:
        :rtype: None
        """
        return self.walk_activity.SetWalkCurveDefPoints(i_num_points, ad_points)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_walk_curve_def_points'
        # # vba_code = """
        # # Public Function set_walk_curve_def_points(walk_activity)
        # #     Dim iNumPoints (2)
        # #     walk_activity.SetWalkCurveDefPoints iNumPoints
        # #     set_walk_curve_def_points = iNumPoints
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Update()
                | 
                |     This method is the key-method to create children-MoveToPostures for a
                |     created Walk.
                |     This is must be called after setting appropriate values for Walk Activity.

        :rtype: None
        """
        return self.walk_activity.Update()

    def __repr__(self):
        return f'WalkActivity(name="{self.name}")'
