#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25

from .curve2d import Curve2D


class Spline2D(Curve2D):
    """
        .. note::
            CAA V5 Visual Basic help

                | Class defining a spline in 2D Space.A 2D spline is defined by its
                | constituting   control points.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.spline2d = com_object

    def get_control_points(self, o_ctrl_points):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetControlPoints
                | o Sub GetControlPoints(        oCtrlPoints)
                | 
                | Returns the control points making up the spline.
                |
                | Parameters:
                | oCtrlPoints
                |   The control points of the spline
                |
                | Examples:
                | 
                | The following example fetches the list of control points defining the
                | splinemySpline:
                | 
                | mySpline.GetControlPoints ControlPoints

        :return: tuple
        """
        return self.spline2d.GetControlPoints(o_ctrl_points)

    def get_number_of_control_points(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNumberOfControlPoints
                | o Func GetNumberOfControlPoints(    ) As
                | 
                | Returns the number of Control Points of the Spline
                |
                | Parameters:
                | oNumber
                |   The number of control points*

        :return: int
        """
        return self.spline2d.GetNumberOfControlPoints()

    def insert_control_point_after(self, i_ctrl_point, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | InsertControlPointAfter
                | o Sub InsertControlPointAfter(iCtrlPoint,
                |                               iPosition)
                | 
                | Inserts control points in the spline.  If a 2D point is given (and not
                | a control  point), a new control point is created and aggregated in
                | the spline.
                |
                | Parameters:
                | iCtrlPoint
                |   The new point to be inserted. (@see CATIAPoint2D and CATIAControlPoint2D
                |   for more information).
                | iPosition
                |   The position at which to insert the point.
                |   To insert a new control point as the first element, set iPosition to 0.
                |
                | Examples:
                | 
                | The following example inserts a control point myCtrlPoint as the second
                | element of the splinemySpline:
                | 
                | call mySpline.InsertControlPointAfter (myCtrlPoint, 1)

        """
        self.spline2d.InsertControlPointAfter(i_ctrl_point, i_position)

    def __repr__(self):
        return f'Spline2D(name="{self.name}")'
