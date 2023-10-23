#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity


class MoveJointsAct(Activity):
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
                |                         MoveJointsAct
                | 
                | Interface representing a MoveJointsAct.
                | 
                | Role: This interface is used to retrieve/assign the value of motion
                | targets/attrs for the MoveJointsAct.
                | The following code snippet can be used to obtain a MoveJointsAct from a
                | selected Activity
                | 
                |    Dim oSelectAct As Activity
                |    Set oSelectAct = CATIA.ActiveDocument.Selection.FindObject("CATIAActivity")
                |    Dim objMoveAct As MoveJointsAct
                |    Set objMoveAct = oSelectAct.GetTechnologicalObject("MoveJointsAct")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.move_joints_act = com_object

    @property
    def acceleration(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Acceleration() As double
                | 
                |     This property returns and sets the Acceleration percentage for the
                |     activity. • For straight line motion, the percentage of the maximum TCP linear
                |     acceleration • For joint-interpolated motion, the percentage of the maximum
                |     joint acceleration
                | 
                |     Returns:
                |         oAccel The Speed Percent for the activity. 
                |     Parameters:
                | 
                |         iAccel
                |             The specified Speed Percent for the activity. 
                | 
                |     Example:
                |
                |            Dim objMoveAct As MoveJointsAct
                |                   ......
                |            Dim  Accl as Double
                |            Accl=objMoveAct.Acceleration
                |            Accl  = 30
                |            objMoveAct.Acceleration=Accl

        :rtype: float
        """

        return self.move_joints_act.Acceleration

    @acceleration.setter
    def acceleration(self, value: float):
        """
        :param float value:
        """

        self.move_joints_act.Acceleration = value

    @property
    def corner_rounding(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CornerRounding() As double
                | 
                |     This property returns and sets the Corner Rounding for the activity. Corner
                |     Rounding::The percentage represents the extent to which the device decelerates
                |     as it rounds the corner.
                | 
                |     Returns:
                |         oCornerRounding The Corner Rounding for the activity. 
                |     Parameters:
                | 
                |         iCornerRounding
                |             The specified Corner Rounding for the activity. 
                | 
                |     Example:
                |
                |            Dim objMoveAct As MoveJointsAct
                |                   ......
                |            Dim  Rounding as Double
                |            Rounding=objMoveAct.CornerRounding
                |            Rounding = 30
                |            objMoveAct.CornerRounding=Rounding

        :rtype: float
        """

        return self.move_joints_act.CornerRounding

    @corner_rounding.setter
    def corner_rounding(self, value: float):
        """
        :param float value:
        """

        self.move_joints_act.CornerRounding = value

    @property
    def joint_values(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property JointValues() As CATSafeArrayVariant
                | 
                |     This property returns and sets the joint values for the
                |     activity.
                | 
                |     Returns:
                |         oJointVal The joint values for the activity. 
                |     Parameters:
                | 
                |         iJointVal
                |             The specified joint values for the activity. 
                | 
                |     Example:
                |
                |            Dim objMoveAct As MoveJointsAct
                |                   ......
                |            Dim  ListOfJointValues() 
                |            ListOfJointValues=objMoveAct.JointValues
                |            ..
                |            For i = 0 to ubound (ListOfJointValues)
                |               ...
                |            Next
                |            objMoveAct.JointValues=ListOfJointValues

        :rtype: tuple
        """

        return self.move_joints_act.JointValues

    @joint_values.setter
    def joint_values(self, value: tuple):
        """
        :param tuple value:
        """

        self.move_joints_act.JointValues = value

    @property
    def mechanism_index(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MechanismIndex() As short
                | 
                |     Sets and Retrieves mechanism index for the activity. The index of mechanism
                |     in the list of mechanisms of the owning resource.
                | 
                |     Returns:
                |         oMechanismIndex The mechanism index for the activity. 
                |     Parameters:
                | 
                |         iMechanismIndex
                |             The specified mechanism index for the activity. 
                | 
                |     Example:
                |
                |            Dim objMoveAct As MoveJointsAct
                |                   ......
                |            Dim  MechIndex as Integer
                |            MechIndex=objMoveAct.MechanismIndex
                |            MechIndex = 1
                |            objMoveAct.MechanismIndex=MechIndex

        :rtype: int
        """

        return self.move_joints_act.MechanismIndex

    @mechanism_index.setter
    def mechanism_index(self, value: int):
        """
        :param int value:
        """

        self.move_joints_act.MechanismIndex = value

    @property
    def motion_basis(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MotionBasis() As CATBSTR
                | 
                |     Sets and Retrieves Motion Basis defined for the activity ("TIME" /
                |     "SPEED")
                | 
                |     Returns:
                |         oMotionBasis The Motion Basis for the activity. 
                |     Parameters:
                | 
                |         iMotionBasis
                |             The specified Motion Basis for the activity. 
                | 
                |     Example:
                |
                |            Dim objMoveAct As MoveJointsAct
                |                   ......
                |            Dim  MotionBas as string
                |            MotionBas=objMoveAct.MotionBasis
                |            MotionBas  = "SPEED"
                |            objMoveAct.MotionBasis=MotionBas

        :rtype: str
        """

        return self.move_joints_act.MotionBasis

    @motion_basis.setter
    def motion_basis(self, value: str):
        """
        :param str value:
        """

        self.move_joints_act.MotionBasis = value

    @property
    def speed_percent(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SpeedPercent() As double
                | 
                |     This property returns and sets the speed value percentage for the activity.
                |     • For straight line motion, the percentage of the maximum TCP linear speed. •
                |     For joint-interpolated motion, the percentage of the maximum joint
                |     speed.
                | 
                |     Returns:
                |         oSpeedPercent The Speed Percent for the activity. 
                |     Parameters:
                | 
                |         iSpeedPercent
                |             The specified Speed Percent for the activity. 
                | 
                |     Example:
                |
                |            Dim objMoveAct As MoveJointsAct
                |                   ......
                |            Dim  SpeedValPr as Double
                |            SpeedValPr=objMoveAct.SpeedPercent
                |            SpeedValPr = 80
                |            objMoveAct.SpeedPercent=SpeedValPr

        :rtype: float
        """

        return self.move_joints_act.SpeedPercent

    @speed_percent.setter
    def speed_percent(self, value: float):
        """
        :param float value:
        """

        self.move_joints_act.SpeedPercent = value

    def __repr__(self):
        return f'MoveJointsAct(name="{self.name}")'
