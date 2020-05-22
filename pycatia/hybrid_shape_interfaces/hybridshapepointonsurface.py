#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePointOnSurface(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the Point on Surface feature objects.Role:  Allows to
                | access data of the point feature created with a geodesic distance in a
                | direction to a reference point on a surface

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_on_surface = com_object     

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction
                | o Property Direction(    ) As
                | 
                | Returns or Sets the direction from the reference point in
                | which the point is computed. 
                |
                | Example:
                | This example retrieves
                | in oDirection the direction from the reference point for
                | PointOnSurface feature. Dim oDirection As
                | CATIAHybridShapeDirection Set oDirection =
                | PointOnSurface.Direction

        :return:
        """
        return self.hybrid_shape_point_on_surface.Direction

    @property
    def offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Offset
                | o Property Offset(    ) As   (Read Only)
                | 
                | Returns the geodesic length. 
                |
                | Example:
                | This example retrieves
                | in oGeodesicOffset the offset (Geodesic Length) from the
                | reference point for PointOnSurface feature. Dim
                | oGeodesicOffset As CATIAReference Set oGeodesicOffset =
                | PointOnSurface.GeodesicOffset

        :return:
        """
        return self.hybrid_shape_point_on_surface.Offset

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Point
                | o Property Point(    ) As
                | 
                | Returns or Sets the reference point. This data is not
                | mandatory. If no point is given, the middle point on the
                | surface is taken. Sub-element(s) supported (see object): .
                | 
                |
                | Example:
                | This example retrieves in oPointRef the reference
                | point for PointOnSurface feature. Dim oPointRef As
                | CATIAReference Set oPointRef = PointOnSurface.PointRef

        :return:
        """
        return self.hybrid_shape_point_on_surface.Point

    @property
    def surface(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Surface
                | o Property Surface(    ) As
                | 
                | Returns or Sets the surface. Sub-element(s) supported (see
                | object): . 
                |
                | Example:
                | This example retrieves in oSurface the
                | supporting surface for PointOnSurface feature. Dim oSurface
                | As CATIAReference Set oSurface = PointOnSurface.Surface

        :return:
        """
        return self.hybrid_shape_point_on_surface.Surface

    def __repr__(self):
        return f'HybridShapePointOnSurface()'
