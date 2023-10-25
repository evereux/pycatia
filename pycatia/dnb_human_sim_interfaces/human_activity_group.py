#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_sim_interfaces.worker_activity import WorkerActivity


class HumanActivityGroup(WorkerActivity):
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
                |                             HumanActivityGroup
                | 
                | Interface representing xxx.
                | 
                | Role: Components that implement DNBIAHumanActivityGroup are
                | ...
                | 
                | Do not use the DNBIAHumanActivityGroup interface for such and such
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.human_activity_group = com_object

    @property
    def motion_basis(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MotionBasis() As HTSActivityGroupMotionBasis
                | 
                |     Returns or Sets Motion-Basis (see HTSActivityGroupMotionBasis for list of
                |     possible values)

        :return: enum hts_activity_group_motion_basis
        :rtype: int
        """

        return self.human_activity_group.MotionBasis

    @motion_basis.setter
    def motion_basis(self, value: int):
        """
        :param int value: enum hts_activity_group_motion_basis
        """

        self.human_activity_group.MotionBasis = value

    @property
    def reference_time(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReferenceTime() As double
                | 
                |     Returns or Sets ReferenceTime for HumanActivityGroup Activity

        :rtype: float
        """

        return self.human_activity_group.ReferenceTime

    @reference_time.setter
    def reference_time(self, value: float):
        """
        :param float value:
        """

        self.human_activity_group.ReferenceTime = value

    @property
    def user_speed(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UserSpeed() As double
                | 
                |     Returns or Sets Speed for HumanActivityGroup Activity

        :rtype: float
        """

        return self.human_activity_group.UserSpeed

    @user_speed.setter
    def user_speed(self, value: float):
        """
        :param float value:
        """

        self.human_activity_group.UserSpeed = value

    @property
    def user_time(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UserTime() As double
                | 
                |     Returns or Sets Time for HumanActivityGroup Activity

        :rtype: float
        """

        return self.human_activity_group.UserTime

    @user_time.setter
    def user_time(self, value: float):
        """
        :param float value:
        """

        self.human_activity_group.UserTime = value

    def __repr__(self):
        return f'HumanActivityGroup(name="{self.name}")'
