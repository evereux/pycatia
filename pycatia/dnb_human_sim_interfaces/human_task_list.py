#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_sim_interfaces.human_task import HumanTask
from pycatia.system_interfaces.collection import Collection


class HumanTaskList(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     HumanTaskList

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.human_task_list = com_object

    def item(self, i_index: int) -> HumanTask:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(long iIndex) As HumanTask
                | 
                |     Returns the HumanTask of the specified index from
                |     HumanTaskList
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The task index

        :param int i_index:
        :rtype: HumanTask
        """
        return HumanTask(self.human_task_list.Item(i_index))

    def remove(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(long iIndex)
                | 
                |     This method removes the specified HumanTask on the current
                |     TaskList
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The task index

        :param int i_index:
        :rtype: None
        """
        return self.human_task_list.Remove(i_index)

    def __repr__(self):
        return f'HumanTaskList(name="{self.name}")'
