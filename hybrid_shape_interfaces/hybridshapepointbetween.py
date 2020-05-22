#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePointBetween(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape PointBetween feature object.Role: To
                | access the data of the hybrid shape PointBetween feature object.This
                | data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_between = com_object     

    @property
    def first_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstPoint
                | o Property FirstPoint(    ) As
                | 
                | Returns or sets the first reference point. Sub-element(s)
                | supported (see object): . 
                |
                | Example:
                | This example retrieves in
                | RefPoint1 the first reference point for the PointBetween
                | hybrid shape feature. Dim RefPoint1 As Reference Set
                | RefPoint1 = PointBetween.FirstPoint

        :return:
        """
        return self.hybrid_shape_point_between.FirstPoint

    @first_point.setter
    def first_point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_between.FirstPoint = value 

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(    ) As
                | 
                | Returns or sets the orientation. Role: Orientation = 1 means
                | that distance is measured from the second point Example:
                | This example retrieves in Orient the orientation for the
                | PointBetween hybrid shape feature. Dim Orient As long Set
                | Orient = PointBetween.Orientation

        :return:
        """
        return self.hybrid_shape_point_between.Orientation

    @orientation.setter
    def orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_between.Orientation = value 

    @property
    def ratio(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Ratio
                | o Property Ratio(    ) As   (Read Only)
                | 
                | Get the ratio. Role: if d1 is the distance between the first
                | point and the created point, and d2 is the distance between
                | the first point and the second point, then ratio = d1/d2.
                | 
                |
                | Example:
                | This example retrieves in ratio the orientation for
                | the PointBetween hybrid shape feature. Dim ratio As
                | CATIARealParam Get ratio = PointBetween.Ratio

        :return:
        """
        return self.hybrid_shape_point_between.Ratio

    @property
    def second_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondPoint
                | o Property SecondPoint(    ) As
                | 
                | Returns or sets the second reference point. Sub-element(s)
                | supported (see object): . 
                |
                | Example:
                | This example retrieves in
                | RefPoint2 the second reference point for the PointBetween
                | hybrid shape feature. Dim RefPoint2 As Reference Set
                | RefPoint2 = PointBetween.SecondPoint

        :return:
        """
        return self.hybrid_shape_point_between.SecondPoint

    @second_point.setter
    def second_point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_between.SecondPoint = value 

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or Sets the support. Note: the support can be
                | surface or curve. It is not mandatory Sub-element(s)
                | supported (see object): and and . 
                |
                | Example:
                | This example
                | retrieves in oSupport the support(if it exist) for the
                | PointBetween hybrid shape feature. Dim oSupport As Reference
                | Set oSupport = PointBetween.Support

        :return:
        """
        return self.hybrid_shape_point_between.Support

    def __repr__(self):
        return f'HybridShapePointBetween()'
