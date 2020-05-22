#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeCircleCtrPt(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape circle object defined using a center and a
                | point on the circle.Role: To access the data of the hybrid shape
                | circle object.This data includes:Use the CATIAHybridShapeFactory to
                | create a HybridShapeCircleCtrPt object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_ctr_pt = com_object     

    @property
    def center(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Center
                | o Property Center(    ) As
                | 
                | Returns or sets the circle center. Sub-element(s) supported
                | (see object): . 
                |
                | Example:
                | This example retrieves in
                | HybShpCircleCenter the center of the HybShpCircle hybrid
                | shape circle. Dim HybShpCircleCenter As Reference
                | HybShpCircleCenter = HybShpCircle.Center

        :return:
        """
        return self.hybrid_shape_circle_ctr_pt.Center

    @center.setter
    def center(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_ctr_pt.Center = value 

    @property
    def crossing_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CrossingPoint
                | o Property CrossingPoint(    ) As
                | 
                | Returns or sets the circle passing point. Sub-element(s)
                | supported (see object): . 
                |
                | Example:
                | This example retrieves
                | the passing point of the HybShpCircle hybrid shape circle in
                | HybShpCirclePassingPoint point. Dim HybShpCirclePassingPoint
                | As Reference Set HybShpCirclePassingPoint =
                | HybShpCircle.CrossingPoint

        :return:
        """
        return self.hybrid_shape_circle_ctr_pt.CrossingPoint

    @crossing_point.setter
    def crossing_point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_ctr_pt.CrossingPoint = value 

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets the circle support surface. Sub-element(s)
                | supported (see object): . 
                |
                | Example:
                | This example retrieves in
                | HybShpCircleSupportSurf the support surface of the
                | HybShpCircle hybrid shape circle. Dim
                | HybShpCircleSupportSurf As Reference HybShpCircleSupportSurf
                | = HybShpCircle.Support

        :return:
        """
        return self.hybrid_shape_circle_ctr_pt.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_ctr_pt.Support = value 

    def is_geodesic(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsGeodesic
                | o Func IsGeodesic(    ) As
                | 
                | Queries whether the circle is geodesic or not.
                |
                | Parameters:
                | oGeod
                |        geodesic type : when TRUE, the circle is geodesic.


        :return:
        """
        return self.hybrid_shape_circle_ctr_pt.IsGeodesic()

    def set_geometry_on_support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetGeometryOnSupport
                | o Sub SetGeometryOnSupport(    )
                | 
                | Sets GeometryOnSupport of circle. It puts the circle on the
                | surface.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_circle_ctr_pt.SetGeometryOnSupport()

    def unset_geometry_on_support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UnsetGeometryOnSupport
                | o Sub UnsetGeometryOnSupport(    )
                | 
                | Inactivates GeometryOnSupport of circle. Note: The circle
                | becomes euclidean.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_circle_ctr_pt.UnsetGeometryOnSupport()

    def __repr__(self):
        return f'HybridShapeCircleCtrPt()'
