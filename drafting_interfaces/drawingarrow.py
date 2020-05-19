#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:56:40.651039

from pycatia.system_interfaces.base_object import AnyObject


class DrawingArrow(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents a drawing arrow in a drawing view.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_arrow = com_object

    @property
    def head_symbol(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HeadSymbol
                | o Property HeadSymbol(    ) As
                | 
                | Returns or sets symbol type of head side. Example: This
                | example retrieves the symbol type of head side on MyArrow
                | drawing arrow. oSymbol = MyArrow.HeadSymbol
                |

        :return: int enumeration_type
        """
        return self.drawing_arrow.HeadSymbol

    @head_symbol.setter
    def head_symbol(self, value):
        """
            :param int value:
        """
        self.drawing_arrow.HeadSymbol = value

    @property
    def head_target(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HeadTarget
                | o Property HeadTarget(    ) As
                | 
                | Returns or sets target element of head side. Example: This
                | example retrieves the target element of head side on MyArrow
                | drawing arrow. oTarget = MyArrow.HeadTarget
                |

        :return:
        """
        return self.drawing_arrow.HeadTarget

    @head_target.setter
    def head_target(self, value):
        """
            :param type value:
        """
        self.drawing_arrow.HeadTarget = value

    @property
    def nb_interruption(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NbInterruption
                | o Property NbInterruption(    ) As   (Read Only)
                | 
                | Returns the number of interruptions of arrow path. Example:
                | This example retrieves the number of interruptions on
                | MyArrow drawing arrow. oNbInterruption =
                | MyArrow.NbInterruption
                |

        :return: int
        """
        return self.drawing_arrow.NbInterruption

    @property
    def nb_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NbPoint
                | o Property NbPoint(    ) As   (Read Only)
                | 
                | Returns the number of points of arrow path. Example: This
                | example retrieves the number of points on MyArrow drawing
                | arrow. oNbPoint = MyArrow.NbPoint
                |

        :return: int
        """
        return self.drawing_arrow.NbPoint

    @property
    def tail_symbol(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TailSymbol
                | o Property TailSymbol(    ) As
                | 
                | Returns or sets symbol type of tail side. Example: This
                | example retrieves the symbol type of tail side on MyArrow
                | drawing arrow. oSymbol = MyArrow.TailSymbol
                |

        :return: int enumeration_type
        """
        return self.drawing_arrow.TailSymbol

    @tail_symbol.setter
    def tail_symbol(self, value):
        """
            :param int value:
        """
        self.drawing_arrow.TailSymbol = value

    @property
    def tail_target(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TailTarget
                | o Property TailTarget(    ) As
                | 
                | Returns or sets target element of tail side. Example: This
                | example retrieves the target element of tail side on MyArrow
                | drawing arrow. oTarget = MyArrow.TailTarget
                |

        :return:
        """
        return self.drawing_arrow.TailTarget

    @tail_target.setter
    def tail_target(self, value):
        """
            :param type value:
        """
        self.drawing_arrow.TailTarget = value

    def add_interruption(self, i_first_point_x, i_first_point_y, i_second_point_x, i_second_point_y):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddInterruption
                | o Sub AddInterruption(iFirstPointX,
                |                       iFirstPointY,
                |                       iSecondPointX,
                |                       iSecondPointY)
                | 
                | Add an interruption to an arrow.
                |
                | Parameters:
                | iFirstPointX
                |   X coordinates of first point.
                | iFirstPointY
                |   Y coordinates of first point.
                | iSecondPointX
                |   X coordinates of second point.
                | iSecondPointY
                |   Y coordinates of second point.
                |
                | Examples:
                | This example adds an interruption to MyArrow. iFirstPointX =
                | 10. iFirstPointY = 20. iSecondPointX = 20. iSecondPointY =
                | 20. MyArrow.AddInterruption iFirstPointX, iFirstPointY,
                | iSecondPointX, iSecondPointY

        :param float i_first_point_x:
        :param float i_first_point_y:
        :param float i_second_point_x:
        :param float i_second_point_y:
        :return:
        """
        return self.drawing_arrow.AddInterruption(i_first_point_x, i_first_point_y, i_second_point_x, i_second_point_y)

    def add_point(self, i_num, i_x, i_y):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddPoint
                | o Sub AddPoint(iNum,
                |                iX,
                |                iY)
                | 
                | Add a point to an arrow.
                |
                | Parameters:
                | iNum
                |   Point number. Point will be inserted at iNum+1 position.
                | iX
                |   X coordinates of point to add.
                | iY
                |   Y coordinates of point to add.
                | Examples:
                | This example adds a point to MyArrow. iNum = 1 iX = 10. iY =
                | 20. MyArrow.AddPoint iNum, iX, iY

        :param int i_num:
        :param float i_x:
        :param float i_y:
        :return:
        """
        return self.drawing_arrow.AddPoint(i_num, i_x, i_y)

    def get_interruptions(self, o_interruptions):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetInterruptions
                | o Func GetInterruptions(        oInterruptions) As
                | 
                | Get arrow path.
                |
                | Parameters:
                | oInterruptions
                |   List of interruptions coordinates (X1,Y1,X2,Y2,.....Xn,Yn).
                | Returns:
                |   oNbInterruptions   Number of interruptions.
                |
                | Examples:
                | This example gets interruptions of MyArrow path.
                | oNbInterruptions = MyArrow.GetInterruptions(oInterruptions)

        :param o_interruptions:
        :return: float
        """
        return self.drawing_arrow.GetInterruptions(o_interruptions)

    def get_point(self, i_num, o_x, o_y):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPoint
                | o Sub GetPoint( iNum,
                |                 oX,
                |                 oY)
                | 
                | Get arrow point coordinates.
                |
                | Parameters:
                | iNum
                |    Point number.
                |  oX
                |    X coordinates of point.
                |  oY
                |    Y coordinates of point.
                |
                | Examples:
                | This example gets a point to MyArrow. iNum = 1
                | MyArrow.GetPoint(iNum, oX, oY)

        :param int i_num:
        :param float o_x:
        :param float o_y:
        :return:
        """
        return self.drawing_arrow.GetPoint(i_num, o_x, o_y)

    def get_points(self, o_points):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPoints
                | o Func GetPoints(        oPoints) As
                | 
                | Get arrow path.
                |
                | Parameters:
                | oPoints
                |   List of points coordinates (X1,Y1,X2,Y2,.....Xn,Yn).
                | Returns:
                |   oNbPoints   Number of points.
                |
                | Examples:
                | This example gets points of MyArrow path. oNbPoints =
                | MyArrow.GetPoints(oPoints)

        :param o_points:
        :return:
        """
        return self.drawing_arrow.GetPoints(o_points)

    def modify_point(self, i_num, i_x, i_y):
        """
        .. note::
            CAA V5 Visual Basic help

                | ModifyPoint
                | o Sub ModifyPoint(        iNum,
                |                           iX,
                |                           iY)
                | 
                | Modify a point of an Arrow.
                |
                | Parameters:
                | iNum
                |   Point number to modify.
                | iX
                |   X coordinates of new point.
                | iY
                |   Y coordinates of new point.
                |
                | Examples:
                | This example modifies a point to MyArrow. iNum = 1 iX = -10.
                | iY = -20. MyArrow.ModifyPoint iNum, iX, iY

        :param int i_num:
        :param float i_x:
        :param float i_y:
        :return:
        """
        return self.drawing_arrow.ModifyPoint(i_num, i_x, i_y)

    def remove_interruption(self, i_num):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveInterruption
                | o Sub RemoveInterruption(        iNum)
                | 
                | Remove an interruption to an arrow.
                |
                | Parameters:
                | iNum
                |    Interruption number to delete.
                |    - If iNum equals to 0, all interruptions will be removed.
                |
                | Examples:
                | This example removes an interruption from MyArrow. iNum = 2
                | MyArrow.RemoveInterruption iNum

        :param i_num:
        :return:
        """
        self.drawing_arrow.RemoveInterruption(i_num)

    def remove_point(self, i_num):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemovePoint
                | o Sub RemovePoint(        iNum)
                | 
                | Remove a point from an arrow.
                |
                | Parameters:
                | iNum
                |   Point number to delete.
                |
                | Examples:
                | This example removes a point from MyArrow. iNum = 2
                | MyArrow.RemovePoint iNum

        :param i_num:
        :return:
        """
        return self.drawing_arrow.RemovePoint(i_num)

    def __repr__(self):
        return f'DrawingArrow()'
