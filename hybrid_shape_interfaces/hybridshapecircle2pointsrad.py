#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeCircle2PointsRad(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape circle object defined using two points and
                | a radius.Role: To access the data of the hybrid shape circle
                | object.This data includes:Use the CATIAHybridShapeFactory to create a
                | HybridShapeCircle2PointsRad object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle2_points_rad = com_object     

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
        return self.hybrid_shape_circle2_points_rad.Diameter

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
                | DiameterMode of the HybShpCircle hybrid shape circle feature
                | HybShpCircle.DiameterMode = True

        :return:
        """
        return self.hybrid_shape_circle2_points_rad.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle2_points_rad.DiameterMode = value 

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(    ) As
                | 
                | Returns or sets the circle orientation. Role: The circle
                | orientation indicates which side of the line made up using
                | the two passing points is used to create the major part of
                | the circle. It is determined using the cross product of the
                | normal to the suppport and the vector made up using the two
                | passing points (Pt1-Pt2). Legal values: 1 to state that the
                | major part of the circle is or should be created on the side
                | of the line shown by the vector resulting from this cross
                | product, and -1 otherwise. 
                |
                | Example:
                | This example retrieves
                | in HybShpCircleOrientation the orientation of the
                | HybShpCircle hybrid shape circle. HybShpCircleOrientation =
                | HybShpCircle.Orientation

        :return:
        """
        return self.hybrid_shape_circle2_points_rad.Orientation

    @orientation.setter
    def orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle2_points_rad.Orientation = value 

    @property
    def pt1(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Pt1
                | o Property Pt1(    ) As
                | 
                | Returns or sets the circle first passing point. Sub-
                | element(s) supported (see object): . 
                |
                | Example:
                | This example
                | retrieves the first passing point of the HybShpCircle hybrid
                | shape circle in HybShpCircleFirstPassingPoint point. Dim
                | HybShpCircleFirstPassingPoint As Reference Set
                | HybShpCircleFirstPassingPoint = HybShpCircle.Pt1

        :return:
        """
        return self.hybrid_shape_circle2_points_rad.Pt1

    @pt1.setter
    def pt1(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle2_points_rad.Pt1 = value 

    @property
    def pt2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Pt2
                | o Property Pt2(    ) As
                | 
                | Returns or sets the circle second passing point. Sub-
                | element(s) supported (see object): . 
                |
                | Example:
                | This example
                | sets the second passing point of the HybShpCircle hybrid
                | shape circle as the Point12 point. HybShpCircle.Pt2 Point12

        :return:
        """
        return self.hybrid_shape_circle2_points_rad.Pt2

    @pt2.setter
    def pt2(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle2_points_rad.Pt2 = value 

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Radius
                | o Property Radius(    ) As   (Read Only)
                | 
                | Returns the circle radius.
                | Examples:
                | This example retrieves in HybShpCircleRadius the radius of
                | the HybShpCircle hybrid shape circle. Dim HybShpCircleRadius
                | As Length HybShpCircleRadius = HybShpCircle.Radius

        :return:
        """
        return self.hybrid_shape_circle2_points_rad.Radius

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
        return self.hybrid_shape_circle2_points_rad.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle2_points_rad.Support = value 

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
        return self.hybrid_shape_circle2_points_rad.IsGeodesic()

    def set_geometry_on_support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetGeometryOnSupport
                | o Sub SetGeometryOnSupport(    )
                | 
                | Sets GeometryOnSupport of circle. It puts the circle on the
                | surface. S_OK if OK, E_FAIL if fail
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_circle2_points_rad.SetGeometryOnSupport()

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
        return self.hybrid_shape_circle2_points_rad.UnsetGeometryOnSupport()

    def __repr__(self):
        return f'HybridShapeCircle2PointsRad()'
