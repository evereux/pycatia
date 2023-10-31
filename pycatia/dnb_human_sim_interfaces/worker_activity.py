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
from pycatia.dnb_human_sim_interfaces.human_task import HumanTask


class WorkerActivity(Activity):
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
                |                         WorkerActivity
                | 
                | The object that represents an Worker activity.
                | 
                | Following activity types qualify as worker activities:
                | MoveToPostureActivity
                | WalkActivity (Forward/Backward/SideStep)
                | AutoWalkActivity
                | PickActivity
                | PlaceActivity
                | HumanActivityGroup
                | HumanCallTask
                | CollisionFreeWalk (Forward and Backward)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.worker_activity = com_object

    @property
    def human_task(self) -> HumanTask:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HumanTask() As HumanTask (Read Only)
                | 
                |     Returns the parent HumanTask
                | 
                |     Returns:
                |         oHumanTask (see HumanTask for more details)

        :rtype: HumanTask
        """

        return HumanTask(self.worker_activity.HumanTask)

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
                |         oManikin (see SWKManikin for more details)

        :rtype: SWKManikin
        """

        return SWKManikin(self.worker_activity.WorkerResource)

    def __repr__(self):
        return f'WorkerActivity(name="{self.name}")'
