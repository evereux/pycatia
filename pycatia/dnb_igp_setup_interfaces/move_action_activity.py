#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity


class MoveActionActivity(Activity):
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
                |                         MoveActionActivity
                | 
                | Interface representing a Move Activity inside a generic Action (Close Gun/Open
                | Gun etc).
                | 
                | Role: This interface is used to retieve/assign the value of motion
                | targets/attributes for the Move Activity.
                | The following code snippet can be used to obtain a MoveActionActivity from a
                | selected Activity
                | 
                |    Dim oSelectAct As Activity
                |    set oSelectAct = CATIA.ActiveDocument.Selection.FindObject("CATIAActivity")
                |    Dim objMoveAct As MoveActionActivity
                |    set objMoveAct = oSelectAct.GetTechnologicalObject("MoveActionActivity")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.move_action_activity = com_object

    @property
    def home_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HomeName() As CATBSTR
                | 
                |     Sets and Retreives Home Name corresponding to the activity
                |     target
                | 
                |     Returns:
                |         oHomeName Home Name stored as the target. 
                |     Parameters:
                | 
                |         iHomeName
                |             The specified Home Name as the activity target 
                | 
                |     Example:
                |
                |            Dim objMoveAct As MoveActionActivity
                |                   ......
                |            Dim  HomeName as string
                |            set HomeName=objMoveAct.HomeName
                |            HomeName  = "Home.2"
                |            objMoveAct.HomeName=HomeName

        :rtype: str
        """

        return self.move_action_activity.HomeName

    @home_name.setter
    def home_name(self, value: str):
        """
        :param str value:
        """

        self.move_action_activity.HomeName = value

    @property
    def joint_values(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property JointValues() As CATSafeArrayVariant
                | 
                |     This property returns and sets the joint values for the Move
                |     activity.
                | 
                |     Returns:
                |         oJointVal The joint values for the Move activity. 
                |     Parameters:
                | 
                |         iJointVal
                |             The specified joint values for the move activity. 
                | 
                |     Example:
                |
                |            Dim objMoveAct As MoveActionActivity
                |                   ......
                |            Dim  ListOfJointValues() 
                |            set ListOfJointValues=objMoveAct.JointValues
                |            ..
                |            For i = 0 to ubound (ListOfJointValues)
                |               ...
                |            Next
                |            objMoveAct.JointValues=ListOfJointValues

        :rtype: tuple
        """

        return self.move_action_activity.JointValues

    @joint_values.setter
    def joint_values(self, value: tuple):
        """
        :param tuple value:
        """

        self.move_action_activity.JointValues = value

    @property
    def target_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TargetType() As CATBSTR (Read Only)
                | 
                |     Retreives Target Type depending on the defined target("HOME" /
                |     "JOINT")
                | 
                |     Returns:
                |         oTargetType The Target Type for the Move. 
                |     Example:
                |
                |            Dim objMoveAct As MoveActionActivity
                |                   ......
                |            Dim  TgtType As String
                |            TgtType=objMoveAct.TargetType

        :rtype: str
        """

        return self.move_action_activity.TargetType

    def __repr__(self):
        return f'MoveActionActivity(name="{self.name}")'
