#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeCircleCenterAxis(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape circle object defined using a point and
                | axis/line.Role: To access the data of the hybrid shape circle center
                | axis object.This data includes:Use the CATIAHybridShapeFactory to
                | create a HybridShapeCircleCenterAxis object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_center_axis = com_object     

    @property
    def axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Axis
                | o Property Axis(    ) As
                | 
                | Returns or sets the Axis of the circle. 
                |
                | Example:
                | This
                | example retrieves in CircleAxis the Axis of plane in which
                | circle is lying from HybShpCircle hybrid shape circle center
                | axis feature Dim CircleAxis As Reference Set CircleAxis =
                | HybShpCircle.Axis

        :return:
        """
        return self.hybrid_shape_circle_center_axis.Axis

    @axis.setter
    def axis(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_center_axis.Axis = value 

    @property
    def diameter(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Diameter
                | o Property Diameter(    ) As   (Read Only)
                | 
                | Returns the circle diameter. It is expressed as a literal.
                | Succeeds only if DiameterMode is set to True.

        :return:
        """
        return self.hybrid_shape_circle_center_axis.Diameter

    @property
    def diameter_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DiameterMode
                | o Property DiameterMode(    ) As
                | 
                | Returns or sets the DiameterMode. Legal values: True implies
                | diameter False implies radius (default). When DiameterMode
                | is changed, Radius/Diameter value, which is stored will not
                | be modified. 
                |
                | Example:
                | This example sets that the
                | DiameterMode of the HybShpCircle hybrid shape circle center
                | axis feature HybShpCircle.DiameterMode = True

        :return:
        """
        return self.hybrid_shape_circle_center_axis.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_center_axis.DiameterMode = value 

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Point
                | o Property Point(    ) As
                | 
                | Returns or sets the Point of the circle. 
                |
                | Example:
                | This
                | example retrieves in CirclePoint the point used for center
                | computation from HybShpCircle hybrid shape circle center
                | axis feature Dim CirclePoint As Reference Set CirclePoint =
                | HybShpCircle.Point

        :return:
        """
        return self.hybrid_shape_circle_center_axis.Point

    @point.setter
    def point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_center_axis.Point = value 

    @property
    def projection_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ProjectionMode
                | o Property ProjectionMode(    ) As
                | 
                | Returns or sets the ProjectionMode. Legal values: True
                | (default) implies point will be projected on to axis/line
                | False implies that point will be center of the circle.
                | 
                |
                | Example:
                | This example sets that the ProjectionMode of the
                | HybShpCircle hybrid shape circle center axis feature
                | HybShpCircle.ProjectionMode = True

        :return:
        """
        return self.hybrid_shape_circle_center_axis.ProjectionMode

    @projection_mode.setter
    def projection_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_center_axis.ProjectionMode = value 

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Radius
                | o Property Radius(    ) As   (Read Only)
                | 
                | Returns the circle radius. It is expressed as a literal.
                | Succeeds only if DiameterMode is set to False.

        :return:
        """
        return self.hybrid_shape_circle_center_axis.Radius

    def __repr__(self):
        return f'HybridShapeCircleCenterAxis()'
