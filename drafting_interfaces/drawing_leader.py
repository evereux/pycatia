#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class DrawingLeader(AnyObject):
    """
        .. note::
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
    def all_around(self):
        """
        .. note::
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

        :return: bool
        """

        return self.drawing_leader.AllAround

    @all_around.setter
    def all_around(self, value):
        """
        :param bool value:
        """

        self.drawing_leader.AllAround = value

    @property
    def anchor_point(self):
        """
        .. note::
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

        :return: int
        """

        return self.drawing_leader.AnchorPoint

    @anchor_point.setter
    def anchor_point(self, value):
        """
        :param int value:
        """

        self.drawing_leader.AnchorPoint = value

    @property
    def head_symbol(self):
        """
        .. note::
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

        :return: enum cat_symbol_type
        """

        return self.drawing_leader.HeadSymbol

    @head_symbol.setter
    def head_symbol(self, value):
        """
        :param enum cat_symbol_type value:
        """

        self.drawing_leader.HeadSymbol = value

    @property
    def head_target(self):
        """
        .. note::
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

        :return: AnyObject
        """

        return AnyObject(self.drawing_leader.HeadTarget)

    @head_target.setter
    def head_target(self, value):
        """
        :param AnyObject value:
        """

        self.drawing_leader.HeadTarget = value

    @property
    def leaders(self):
        """
        .. note::
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

        :return: DrawingLeaders
        """
        from pycatia.drafting_interfaces.drawing_leaders import DrawingLeaders
        return DrawingLeaders(self.drawing_leader.Leaders)

    @property
    def nb_interruption(self):
        """
        .. note::
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

        :return: int
        """

        return self.drawing_leader.NbInterruption

    @property
    def nb_point(self):
        """
        .. note::
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

        :return: int
        """

        return self.drawing_leader.NbPoint

    def add_interruption(self, i_first_point_x, i_first_point_y, i_second_point_x,
                         i_second_point_y):
        """
        .. note::
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
        :return: None
        """
        return self.drawing_leader.AddInterruption(i_first_point_x, i_first_point_y, i_second_point_x, i_second_point_y)

    def add_point(self, i_num, i_x, i_y):
        """
        .. note::
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
        :return: None
        """
        return self.drawing_leader.AddPoint(i_num, i_x, i_y)

    def get_interruptions(self, o_interruptions):
        """
        .. note::
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
        :return: int
        """
        return self.drawing_leader.GetInterruptions(o_interruptions)

    def get_point(self, i_num, o_x, o_y):
        """
        .. note::
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
        :return: None
        """
        return self.drawing_leader.GetPoint(i_num, o_x, o_y)

    def get_points(self, o_points):
        """
        .. note::
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
        :return: int
        """
        return self.drawing_leader.GetPoints(o_points)

    def modify_point(self, i_num, i_x, i_y):
        """
        .. note::
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
        :return: None
        """
        return self.drawing_leader.ModifyPoint(i_num, i_x, i_y)

    def remove_interruption(self, i_num):
        """
        .. note::
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
        :return: None
        """
        return self.drawing_leader.RemoveInterruption(i_num)

    def remove_point(self, i_num):
        """
        .. note::
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
        :return: None
        """
        return self.drawing_leader.RemovePoint(i_num)

    def __repr__(self):
        return f'DrawingLeader(name="{self.name}")'
