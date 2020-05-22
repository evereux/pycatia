#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeCircleCtrRad(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape circle object defined using a center and a
                | radius.Role: To access the data of the hybrid shape circle object.This
                | data includes:Use the CATIAHybridShapeFactory to create a
                | HybridShapeCircleCtrRad object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_ctr_rad = com_object     

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
        return self.hybrid_shape_circle_ctr_rad.Center

    @center.setter
    def center(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_ctr_rad.Center = value 

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
        return self.hybrid_shape_circle_ctr_rad.Diameter

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
        return self.hybrid_shape_circle_ctr_rad.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_ctr_rad.DiameterMode = value 

    @property
    def first_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstDirection
                | o Property FirstDirection(    ) As
                | 
                | Returns or sets the first direction used to set the angles
                | reference.

        :return:
        """
        return self.hybrid_shape_circle_ctr_rad.FirstDirection

    @first_direction.setter
    def first_direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_ctr_rad.FirstDirection = value 

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
        return self.hybrid_shape_circle_ctr_rad.Radius

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
        return self.hybrid_shape_circle_ctr_rad.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_ctr_rad.Support = value 

    def get_second_direction(self, o_dir_x, o_dir_y, o_dir_z):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSecondDirection
                | o Sub GetSecondDirection(        oDirX,
                |                                  oDirY,
                |                                  oDirZ)
                | 
                | Gets the second direction on the plane to compute the point
                | (for stability). This direction has to be kept perpendicular
                | to the first direction
                |
                | Parameters:
                | oDirX,
                |  oDirY, oDirZ.      second direction
                |    
                | 
                |  See also:


        :param o_dir_x:
        :param o_dir_y:
        :param o_dir_z:
        :return:
        """
        return self.hybrid_shape_circle_ctr_rad.GetSecondDirection(o_dir_x, o_dir_y, o_dir_z)

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
        return self.hybrid_shape_circle_ctr_rad.IsGeodesic()

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
        return self.hybrid_shape_circle_ctr_rad.SetGeometryOnSupport()

    def set_second_direction(self, i_dir_x, i_dir_y, i_dir_z):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSecondDirection
                | o Sub SetSecondDirection(        iDirX,
                |                                  iDirY,
                |                                  iDirZ)
                | 
                | Sets the second direction on the plane to compute the point
                | (for stability). This direction has to be kept perpendicular
                | to the first direction
                |
                | Parameters:
                | iDirX,
                |  iDirY, iDirZ.      second direction
                |    
                | 
                |  See also:


        :param i_dir_x:
        :param i_dir_y:
        :param i_dir_z:
        :return:
        """
        return self.hybrid_shape_circle_ctr_rad.SetSecondDirection(i_dir_x, i_dir_y, i_dir_z)

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
        return self.hybrid_shape_circle_ctr_rad.UnsetGeometryOnSupport()

    def __repr__(self):
        return f'HybridShapeCircleCtrRad()'
