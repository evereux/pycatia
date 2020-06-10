#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class DrawingArrow(AnyObject):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingArrow
                | 
                | Represents a drawing arrow in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_arrow = com_object

    @property
    def head_symbol(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property HeadSymbol() As CatSymbolType
                | 
                |     Returns or sets symbol type of head side.
                | 
                |     Example:
                |         This example retrieves the symbol type of head side on MyArrow drawing
                |         arrow.
                | 
                |          oSymbol = MyArrow.HeadSymbol

        :return: enum cat_symbol_type
        """

        return self.drawing_arrow.HeadSymbol

    @head_symbol.setter
    def head_symbol(self, value):
        """
        :param enum cat_symbol_type value:
        """

        self.drawing_arrow.HeadSymbol = value

    @property
    def head_target(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property HeadTarget() As CATBaseDispatch
                | 
                |     Returns or sets target element of head side.
                | 
                |     Example:
                |         This example retrieves the target element of head side on MyArrow
                |         drawing arrow.
                | 
                |          oTarget = MyArrow.HeadTarget

        :return: AnyObject
        """

        return AnyObject(self.drawing_arrow.HeadTarget)

    @head_target.setter
    def head_target(self, value):
        """
        :param AnyObject value:
        """

        self.drawing_arrow.HeadTarget = value

    @property
    def nb_interruption(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property NbInterruption() As long (Read Only)
                | 
                |     Returns the number of interruptions of arrow path.
                | 
                |     Example:
                |         This example retrieves the number of interruptions on MyArrow drawing
                |         arrow.
                | 
                |          oNbInterruption = MyArrow.NbInterruption

        :return: int
        """

        return self.drawing_arrow.NbInterruption

    @property
    def nb_point(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property NbPoint() As long (Read Only)
                | 
                |     Returns the number of points of arrow path.
                | 
                |     Example:
                |         This example retrieves the number of points on MyArrow drawing
                |         arrow.
                | 
                |          oNbPoint = MyArrow.NbPoint

        :return: int
        """

        return self.drawing_arrow.NbPoint

    @property
    def tail_symbol(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property TailSymbol() As CatSymbolType
                | 
                |     Returns or sets symbol type of tail side.
                | 
                |     Example:
                |         This example retrieves the symbol type of tail side on MyArrow drawing
                |         arrow.
                | 
                |          oSymbol = MyArrow.TailSymbol

        :return: enum cat_symbol_type
        """

        return self.drawing_arrow.TailSymbol

    @tail_symbol.setter
    def tail_symbol(self, value):
        """
        :param enum cat_symbol_type value:
        """

        self.drawing_arrow.TailSymbol = value

    @property
    def tail_target(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property TailTarget() As CATBaseDispatch
                | 
                |     Returns or sets target element of tail side.
                | 
                |     Example:
                |         This example retrieves the target element of tail side on MyArrow
                |         drawing arrow.
                | 
                |          oTarget = MyArrow.TailTarget

        :return: AnyObject
        """

        return AnyObject(self.drawing_arrow.TailTarget)

    @tail_target.setter
    def tail_target(self, value):
        """
        :param AnyObject value:
        """

        self.drawing_arrow.TailTarget = value

    def add_interruption(self, i_first_point_x=None, i_first_point_y=None, i_second_point_x=None, i_second_point_y=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub AddInterruption(double iFirstPointX,
                | double iFirstPointY,
                | double iSecondPointX,
                | double iSecondPointY)
                | 
                |     Add an interruption to an arrow.
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
                |             This example adds an interruption to MyArrow.
                | 
                |              iFirstPointX = 10.
                |              iFirstPointY = 20.
                |              iSecondPointX = 20.
                |              iSecondPointY = 20.
                |              MyArrow.AddInterruption iFirstPointX, iFirstPointY, iSecondPointX,
                |              iSecondPointY

        :param float i_first_point_x:
        :param float i_first_point_y:
        :param float i_second_point_x:
        :param float i_second_point_y:
        :return: None
        """
        return self.drawing_arrow.AddInterruption(i_first_point_x, i_first_point_y, i_second_point_x, i_second_point_y)

    def add_point(self, i_num=None, i_x=None, i_y=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub AddPoint(long iNum,
                | double iX,
                | double iY)
                | 
                |     Add a point to an arrow.
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
                |             This example adds a point to MyArrow.
                | 
                |              iNum = 1
                |              iX = 10.
                |              iY = 20.
                |              MyArrow.AddPoint iNum, iX, iY

        :param int i_num:
        :param float i_x:
        :param float i_y:
        :return: None
        """
        return self.drawing_arrow.AddPoint(i_num, i_x, i_y)

    def get_interruptions(self, o_interruptions=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetInterruptions(CATSafeArrayVariant oInterruptions) As
                | long
                | 
                |     Get arrow path.
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
                |         This example gets interruptions of MyArrow path.
                | 
                |          oNbInterruptions = MyArrow.GetInterruptions(oInterruptions)

        :param tuple o_interruptions:
        :return: int
        """
        return int(self.drawing_arrow.GetInterruptions(o_interruptions))

    def get_point(self, i_num=None, o_x=None, o_y=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetPoint(long iNum,
                | double oX,
                | double oY)
                | 
                |     Get arrow point coordinates.
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
                |             This example gets a point to MyArrow.
                | 
                |              iNum = 1
                |              MyArrow.GetPoint(iNum, oX, oY)

        :param int i_num:
        :param float o_x:
        :param float o_y:
        :return: None
        """
        return self.drawing_arrow.GetPoint(i_num, o_x, o_y)

    def get_points(self, o_points=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetPoints(CATSafeArrayVariant oPoints) As long
                | 
                |     Get arrow path.
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
                |         This example gets points of MyArrow path.
                | 
                |          oNbPoints = MyArrow.GetPoints(oPoints)

        :param tuple o_points:
        :return: int
        """
        return int(self.drawing_arrow.GetPoints(o_points))

    def modify_point(self, i_num=None, i_x=None, i_y=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub ModifyPoint(long iNum,
                | double iX,
                | double iY)
                | 
                |     Modify a point of an Arrow.
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
                |             This example modifys a point to MyArrow.
                | 
                |              iNum = 1
                |              iX = -10.
                |              iY = -20.
                |              MyArrow.ModifyPoint iNum, iX, iY

        :param int i_num:
        :param float i_x:
        :param float i_y:
        :return: None
        """
        return self.drawing_arrow.ModifyPoint(i_num, i_x, i_y)

    def remove_interruption(self, i_num=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RemoveInterruption(long iNum)
                | 
                |     Remove an interruption to an arrow.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Interruption number to delete. 
                |             - If iNum equals to 0, all interruptions will be removed.
                |             
                |         Example:
                |             This example removes an interruption from MyArrow.
                | 
                |              iNum = 2
                |              MyArrow.RemoveInterruption iNum

        :param int i_num:
        :return: None
        """
        return self.drawing_arrow.RemoveInterruption(i_num)

    def remove_point(self, i_num=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RemovePoint(long iNum)
                | 
                |     Remove a point from an arrow.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Point number to delete. 
                |         Example:
                |             This example removes a point from MyArrow.
                | 
                |              iNum = 2
                |              MyArrow.RemovePoint iNum

        :param int i_num:
        :return: None
        """
        return self.drawing_arrow.RemovePoint(i_num)

    def __repr__(self):
        return f'DrawingArrow(name="{ self.name }")'
