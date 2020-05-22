#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePointTangent(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Point Tangent.Role: Allows to access data of the point feature created
                | as follow :The tangent to the curve at this point is colinear to a
                | given direction.Note: The resulting feature can contain several
                | points.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_tangent = com_object     

    @property
    def curve(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Curve
                | o Property Curve(    ) As
                | 
                | Returns or Gets the supporting curve. Sub-element(s)
                | supported (see object): . 
                |
                | Example:
                | This example retrieves in
                | oCurve the supporting Curve for the PointTangent feature.
                | Dim oCurve As CATIAReference Set oCurve = PointTangent.Curve

        :return:
        """
        return self.hybrid_shape_point_tangent.Curve

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction
                | o Property Direction(    ) As
                | 
                | Returns or Sets the direction. 
                |
                | Example:
                | This example
                | retrieves in oDirection the tangent direction use to compute
                | on supporting curve the PointTangent feature. Dim oDirection
                | As CATIAHybridShapeDirection Set oDirection =
                | PointTangent.Direction

        :return:
        """
        return self.hybrid_shape_point_tangent.Direction

    def __repr__(self):
        return f'HybridShapePointTangent()'
