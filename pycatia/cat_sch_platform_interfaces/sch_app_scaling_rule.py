#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchAppScalingRule(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppScalingRule
                | 
                | Provide application rule of how to scale schematic objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_scaling_rule = com_object

    def app_get_scaling_priority(self, o_priority: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppGetScalingPriority(long oPriority)
                | 
                |     Get a priority number to indicate the adjustment (moving) priority of this
                |     object during scaling.
                | 
                |     Parameters:
                | 
                |         oPriority
                |             1 to 99. The lower the number, the higher the processing priority.
                |             For example, an object with priority 1 is processed first and will not move
                |             while connected objects adjust. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchAppScalingRule
                |          Dim intVar1 As Integer
                |           ...
                |          objThisIntf.AppGetScalingPriorityintVar1

        :param int o_priority:
        :rtype: None
        """
        return self.sch_app_scaling_rule.AppGetScalingPriority(o_priority)

    def __repr__(self):
        return f'SchAppScalingRule(name="{self.name}")'
