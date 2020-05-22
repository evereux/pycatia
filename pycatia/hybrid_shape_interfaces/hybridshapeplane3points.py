#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePlane3Points(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape plane through three points feature
                | object.Role: Allows to access data of the plane feature passing though
                | three points. This data includes:Use the CATIAHybridShapeFactory to
                | create HybridShapeFeature object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane3_points = com_object     

    @property
    def first(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | First
                | o Property First(    ) As
                | 
                | Returns or sets the first point. Sub-element(s) supported
                | (see object): . 
                |
                | Example:
                | This example retrieves in
                | FirstPoint the first point for the Plane passing through
                | three points hybrid shape feature. Dim FirstPoint As
                | Reference Set FirstPoint = Plane3Points.First

        :return:
        """
        return self.hybrid_shape_plane3_points.First

    @first.setter
    def first(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_plane3_points.First = value 

    @property
    def second(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Second
                | o Property Second(    ) As
                | 
                | Returns or sets the second point. Sub-element(s) supported
                | (see object): . 
                |
                | Example:
                | This example retrieves in
                | SecondPoint the second point for the Plane passing through
                | three points hybrid shape feature. Dim SecondPoint As
                | Reference Set SecondPoint = Plane3Points.Second

        :return:
        """
        return self.hybrid_shape_plane3_points.Second

    @second.setter
    def second(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_plane3_points.Second = value 

    @property
    def third(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Third
                | o Property Third(    ) As
                | 
                | Returns or sets the third point. Sub-element(s) supported
                | (see object): . 
                |
                | Example:
                | This example retrieves in
                | ThirdPoint the third point for the Plane passing through
                | three points hybrid shape feature. Dim ThridPoint As
                | Reference Set ThirdPoint = Plane3Points.Third

        :return:
        """
        return self.hybrid_shape_plane3_points.Third

    @third.setter
    def third(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_plane3_points.Third = value 

    def __repr__(self):
        return f'HybridShapePlane3Points()'
