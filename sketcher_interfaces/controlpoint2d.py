#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .point2d import Point2D


class ControlPoint2D(Point2D):
    """
        .. note::
            CAA V5 Visual Basic help

                | Class defining a spline control point in 2D Space.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.controlpoint2d = com_object

    @property
    def curvature(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Curvature
                | o Property Curvature(    ) As double
                | 
                | Returns the curvature properties of the spline control point
                |
                | Parameters:
                | oCurvature
                |        The curvature of the tangent determined at the control point

        :return: float
        """
        return self.controlpoint2d.Curvature

    def get_tangent(self, o_tangent):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetTangent
                | o Sub GetTangent(    CATSafeArrayVariant    oTangent)
                | 
                | Returns the tangent properties of the spline control point
                |
                | Parameters:
                | oTangent[0]
                |   The X Coordinate of the tangent determined at the control point
                | oTangent[1]
                |   The Y Coordinate of the tangent determined at the control point

        :return: tuple
        """
        return self.controlpoint2d.GetTangent(o_tangent)

    def set_tangent(self, i_tangent_x, i_tangent_y):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetTangent
                | o Sub SetTangent( double iTangentX,
                |                   double iTangentY)
                | 
                | Imposes the tangent properties of the spline control point
                |
                | Parameters:
                | iTangentX
                |   The X Coordinate of the tangent determined at the control point
                | iTangentY
                |   The Y Coordinate of the tangent determined at the control point

        :param float i_tangent_x:
        :param float i_tangent_y:
        """
        self.controlpoint2d.SetTangent(i_tangent_x, i_tangent_y)

    def unset_curvature(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UnsetCurvature
                | o Sub UnsetCurvature(    )
                | 
                | Unsets the curvature properties of the spline control point

        """
        self.controlpoint2d.UnsetCurvature()

    def unset_tangent(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UnsetTangent
                | o Sub UnsetTangent(    )
                | 
                | Unsets the tangent properties of the spline control point
        """
        self.controlpoint2d.UnsetTangent()

    def __repr__(self):
        return f'ControlPoint2D(name="{self.name}")'
