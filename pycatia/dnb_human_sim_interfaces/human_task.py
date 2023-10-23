#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity
from pycatia.dnb_human_modeling_interfaces.swk_manikin import SWKManikin


class HumanTask(Activity):
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
                |                         HumanTask

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.human_task = com_object

    @property
    def specified_cycle_time(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SpecifiedCycleTime() As double (Read Only)
                | 
                |     returns the time set by the user by set_SpecifiedCycleTime

        :rtype: float
        """

        return self.human_task.SpecifiedCycleTime

    @property
    def specified_joint_speed(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SpecifiedJointSpeed() As double (Read Only)
                | 
                |     returns the speed set by the user by set_SpecifiedJointSpeed

        :rtype: float
        """

        return self.human_task.SpecifiedJointSpeed

    @property
    def worker_resource(self) -> SWKManikin:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WorkerResource() As SWKManikin (Read Only)
                | 
                |     Returns the Worker-Resource associated with this
                |     worker-activity.
                | 
                |     Returns:
                |         oManikin

        :rtype: SWKManikin
        """

        return SWKManikin(self.human_task.WorkerResource)

    def set_specified_cycle_time(self, time: float, i_override_child_act_simulation_time: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_SpecifiedCycleTime(double time,
                | long iOverrideChildActSimulationTime)
                | 
                |     sets the time on the specified task iOverrideChildActSimulationTime: this
                |     should be set equal to zero when no child act overriding is required

        :param float time:
        :param int i_override_child_act_simulation_time:
        :rtype: None
        """
        return self.human_task.set_SpecifiedCycleTime(time, i_override_child_act_simulation_time)

    def set_specified_joint_speed(self, speed: float, i_override_child_joint_speed: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_SpecifiedJointSpeed(double speed,
                | long iOverrideChildJointSpeed)
                | 
                |     sets the joint speed on the specified task(speed should be between 0.0 to
                |     1.0) iOverrideChildJointSpeed: this should be set equal to zero when no child
                |     act overriding is required

        :param float speed:
        :param int i_override_child_joint_speed:
        :rtype: None
        """
        return self.human_task.set_SpecifiedJointSpeed(speed, i_override_child_joint_speed)

    def __repr__(self):
        return f'HumanTask(name="{self.name}")'
