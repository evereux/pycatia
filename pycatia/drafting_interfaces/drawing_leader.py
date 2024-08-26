#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect
from typing import TYPE_CHECKING

from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.drafting_interfaces.drawing_leaders import DrawingLeaders


class DrawingLeader(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingLeader
                | 
                | Represents a drawing leader in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_leader = com_object

    @property
    def all_around(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AllAround() As boolean
                | 
                |     Returns or sets the status of all around.
                | 
                |     Example:
                |         This example retrieves the status of all around on MyLeader drawing
                |         leader.
                | 
                |          oSymbol = MyLeader.AllAround

        :rtype: bool
        """

        return self.drawing_leader.AllAround

    @all_around.setter
    def all_around(self, value: bool):
        """
        :param bool value:
        """

        self.drawing_leader.AllAround = value

    @property
    def anchor_point(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AnchorPoint() As long
                | 
                |     Returns or sets anchor point.
                | 
                |     Example:
                |         This example retrieves the anchor point on MyLeader drawing
                |         leader.
                | 
                |          oAnchorPoint = MyLeader.AnchorPoint

        :rtype: int
        """

        return self.drawing_leader.AnchorPoint

    @anchor_point.setter
    def anchor_point(self, value: int):
        """
        :param int value:
        """

        self.drawing_leader.AnchorPoint = value

    @property
    def anchor_symbol(self) -> int:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property AnchorSymbol() As long
                |     Returns or sets the anchor symbol of the drawing leader. AnchorSymbol 0 : No anchor symbol 1 : All-Around style (circle) - For GDT, Text, Table 2 : All-Over (2 concentric circles) - For GDT, Text, Table 3 : AllAboutWithHorLine (square with an horizontal line) - For GDT, Text, Table 4 : AllAboutWithVerLine (square with a vertical line) - For GDT, Text, Table 5 : AllAroundPartial (half circle) - For GDT, Text, Table 6 : AllOverPartial (2 half concentric circles) - For GDT, Text, Table 7 : AllAboutWithHorLinePartial (half square with an horizontal line) - For GDT, Text, Table 8 : AllAboutWithVerLinePartial (half square with an vertical line) - For GDT, Text, Table 9 : Flag (Flag) - For welding annotation only 10 : FlagAndAllAround (Flag And AllAround) - For welding annotation only

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_leader.AnchorSymbol

    @anchor_symbol.setter
    def anchor_symbol(self, value: int):
        """
        :param int value:
        """

        self.drawing_leader.AnchorSymbol = value

    @property
    def head_symbol(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property HeadSymbol() As CatSymbolType
                | 
                |     Returns or sets symbol type of head side.
                | 
                |     Example:
                |         This example retrieves the symbol type of head side on MyLeader drawing
                |         leader.
                | 
                |          oSymbol = MyLeader.HeadSymbol

        :rtype: int
        """

        return self.drawing_leader.HeadSymbol

    @head_symbol.setter
    def head_symbol(self, value: int):
        """
        :param int value:
        """

        self.drawing_leader.HeadSymbol = value

    @property
    def head_target(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property HeadTarget() As CATBaseDispatch
                | 
                |     Returns or sets target element of head side.
                | 
                |     Example:
                |         This example retrieves the target element of head side on MyLeader
                |         drawing leader.
                | 
                |          oTarget = MyLeader.HeadTarget

        :rtype: AnyObject
        """

        return AnyObject(self.drawing_leader.HeadTarget)

    @head_target.setter
    def head_target(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.drawing_leader.HeadTarget = value

    @property
    def leaders(self) -> 'DrawingLeaders':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Leaders() As DrawingLeaders (Read Only)
                | 
                |     Returns the secondary drawing leader collection of the drawing
                |     leader.
                | 
                |     Example:
                |         This example retrieves in LeaderCollection the collection of leaders of
                |         the Myleader drawing leader.
                | 
                |          Dim LeaderCollection As DrawingLeaders
                |          Set LeaderCollection = MyLeader.Leaders

        :rtype: DrawingLeaders
        """
        from pycatia.drafting_interfaces.drawing_leaders import DrawingLeaders
        return DrawingLeaders(self.drawing_leader.Leaders)

    @property
    def nb_interruption(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property NbInterruption() As long (Read Only)
                | 
                |     Returns the number of interruptions of leader path.
                | 
                |     Example:
                |         This example retrieves the number of interruptions on MyLeader drawing
                |         leader.
                | 
                |          oNbInterruption = MyLeader.NbInterruption

        :rtype: int
        """

        return self.drawing_leader.NbInterruption

    @property
    def nb_point(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property NbPoint() As long (Read Only)
                | 
                |     Returns the number of points of leader path.
                | 
                |     Example:
                |         This example retrieves the number of points on MyLeader drawing
                |         leader.
                | 
                |          oNbPoint = MyLeader.NbPoint

        :rtype: int
        """

        return self.drawing_leader.NbPoint

    def add_interruption(self, i_first_point_x: float, i_first_point_y: float, i_second_point_x: float,
                         i_second_point_y: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddInterruption(double iFirstPointX,
                | double iFirstPointY,
                | double iSecondPointX,
                | double iSecondPointY)
                | 
                |     Add an interruption to an leader.
                | 
                |     Parameters:
                | 
                |         iFirstPointX
                |             X coordinates of first point. 
                |         iFirstPointY
                |             Y coordinates of first point. 
                |         iSecondPointX
                |             X coordinates of second point. 
                |         iSecondPointY
                |             Y coordinates of second point. 
                |         Example:
                |             This example adds an interruption to MyLeader.
                | 
                |              iFirstPointX = 10.
                |              iFirstPointY = 20.
                |              iSecondPointX = 20.
                |              iSecondPointY = 20.
                |              MyLeader.AddInterruption iFirstPointX, iFirstPointY,
                |              iSecondPointX, iSecondPointY

        :param float i_first_point_x:
        :param float i_first_point_y:
        :param float i_second_point_x:
        :param float i_second_point_y:
        :rtype: None
        """
        return self.drawing_leader.AddInterruption(i_first_point_x, i_first_point_y, i_second_point_x, i_second_point_y)

    def add_point(self, i_num: int, i_x: float, i_y: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddPoint(long iNum,
                | double iX,
                | double iY)
                | 
                |     Add a point to an leader.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Point number. Point will be inserted at iNum+1 position.
                |             
                |         iX
                |             X coordinates of point to add. 
                |         iY
                |             Y coordinates of point to add. 
                |         Example:
                |             This example adds a point to MyLeader.
                | 
                |              iNum = 1
                |              iX = 10.
                |              iY = 20.
                |              MyLeader.AddPoint iNum, iX, iY

        :param int i_num:
        :param float i_x:
        :param float i_y:
        :rtype: None
        """
        return self.drawing_leader.AddPoint(i_num, i_x, i_y)

    def get_interruptions(self, o_interruptions: tuple) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetInterruptions(CATSafeArrayVariant oInterruptions) As
                | long
                | 
                |     Get leader path.
                | 
                |     Parameters:
                | 
                |         oInterruptions
                |             List of interruptions coordinates (X1,Y1,X2,Y2,.....Xn,Yn).
                |             
                | 
                |     Returns:
                |         oNbInterruptions Number of interruptions. 
                |     Example:
                |         This example gets interruptions of MyLeader path.
                | 
                |          oNbInterruptions = MyLeader.GetInterruptions(oInterruptions)

        :param tuple o_interruptions:
        :rtype: int
        """
        return self.drawing_leader.GetInterruptions(o_interruptions)

    def get_point(self, i_num: int, o_x: float, o_y: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetPoint(long iNum,
                | double oX,
                | double oY)
                | 
                |     Get leader point coordinates.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Point number. 
                |         oX
                |             X coordinates of point. 
                |         oY
                |             Y coordinates of point. 
                |         Example:
                |             This example gets a point to MyLeader.
                | 
                |              iNum = 1
                |              MyLeader.GetPoint(iNum, oX, oY)

        :param int i_num:
        :param float o_x:
        :param float o_y:
        :rtype: None
        """
        return self.drawing_leader.GetPoint(i_num, o_x, o_y)

    def get_points(self, o_points: tuple) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPoints(CATSafeArrayVariant oPoints) As long
                | 
                |     Get leader path.
                | 
                |     Parameters:
                | 
                |         oPoints
                |             List of points coordinates (X1,Y1,X2,Y2,.....Xn,Yn).
                |             
                | 
                |     Returns:
                |         oNbPoints Number of points. 
                |     Example:
                |         This example gets points of MyLeader path.
                | 
                |          oNbPoints = MyLeader.GetPoints(oPoints)

        :param tuple o_points:
        :rtype: int
        """
        return self.drawing_leader.GetPoints(o_points)

    def modify_point(self, i_num: int, i_x: float, i_y: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ModifyPoint(long iNum,
                | double iX,
                | double iY)
                | 
                |     Modify a point of an leader.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Point number to modify. 
                |         iX
                |             X coordinates of new point. 
                |         iY
                |             Y coordinates of new point. 
                |         Example:
                |             This example modifies a point to MyLeader.
                | 
                |              iNum = 1
                |              iX = -10.
                |              iY = -20.
                |              MyLeader.ModifyPoint iNum, iX, iY

        :param int i_num:
        :param float i_x:
        :param float i_y:
        :rtype: None
        """
        return self.drawing_leader.ModifyPoint(i_num, i_x, i_y)

    def remove_interruption(self, i_num: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveInterruption(long iNum)
                | 
                |     Remove an interruption to an leader.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Interruption number to delete. 
                |             - If iNum equals to 0, all interruptions will be removed.
                |             
                |         Example:
                |             This example removes an interruption from
                |             MyLeader.
                | 
                |              iNum = 2
                |              MyLeader.RemoveInterruption iNum

        :param int i_num:
        :rtype: None
        """
        return self.drawing_leader.RemoveInterruption(i_num)

    def remove_point(self, i_num: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemovePoint(long iNum)
                | 
                |     Remove a point from an leader.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Point number to delete. 
                |         Example:
                |             This example removes a point from MyLeader.
                | 
                |              iNum = 2
                |              MyLeader.RemovePoint iNum

        :param int i_num:
        :rtype: None
        """
        return self.drawing_leader.RemovePoint(i_num)

    def __repr__(self):
        return f'DrawingLeader(name="{self.name}")'
