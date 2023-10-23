#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity


class DelayAct(Activity):
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
                |                         DelayAct
                | 
                | Interface representing a DelayAct.
                | 
                | Role: This interface is used to retrieve/assign the value of motion
                | targets/attrs for the move home activity.
                | The following code snippet can be used to obtain a MoveHomeAct from a selected
                | Activity
                | 
                |    Dim oSelectAct As Activity
                |    Set oSelectAct = CATIA.ActiveDocument.Selection.FindObject("CATIAActivity")
                |    Dim objMoveAct As DelayAct
                |    Set objMoveAct = oSelectAct.GetTechnologicalObject("DelayAct")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.delay_act = com_object

    @property
    def delay(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Delay() As double
                | 
                |     This property returns and sets the delay value of the
                |     activity.
                | 
                |     Example:
                |
                |            Dim objDelayAct As DelayAct
                |            .......
                |            Dim  delay as Double
                |            delay=objDelayAct.Delay
                |            delay  = 30
                |            objDelayAct.Delay=delay

        :rtype: float
        """

        return self.delay_act.Delay

    @delay.setter
    def delay(self, value: float):
        """
        :param float value:
        """

        self.delay_act.Delay = value

    def __repr__(self):
        return f'DelayAct(name="{self.name}")'
