#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_sim_interfaces.human_task import HumanTask
from pycatia.dnb_human_sim_interfaces.human_task_list import HumanTaskList
from pycatia.system_interfaces.any_object import AnyObject


class HumanProgram(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     HumanProgram
                | 
                | The object that represents program-node of Worker.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.human_program = com_object

    @property
    def task_list(self) -> HumanTaskList:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TaskList() As HumanTaskList (Read Only)
                | 
                |     Returns the HumanTaskList from HumanProgram
                | 
                |     Returns:
                |         oTaskList

        :rtype: HumanTaskList
        """

        return HumanTaskList(self.human_program.TaskList)

    def create_human_task(self) -> HumanTask:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateHumanTask() As HumanTask
                | 
                |     Returns newly created HumanTask.
                | 
                |     Returns:
                |         oManikin

        :rtype: HumanTask
        """
        return HumanTask(self.human_program.CreateHumanTask())

    def __repr__(self):
        return f'HumanProgram(name="{self.name}")'
