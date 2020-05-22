#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeSphere(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape sphere feature object.Role: To access the
                | data of the hybrid shape sphere  explicit feature object.The Sphere
                | feature : a Sphere is made up of 4 angles parameters.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sphere = com_object     

    @property
    def axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Axis
                | o Property Axis(    ) As
                | 
                | Returns or sets axis on the object.

        :return:
        """
        return self.hybrid_shape_sphere.Axis

    @axis.setter
    def axis(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sphere.Axis = value 

    @property
    def begin_meridian_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BeginMeridianAngle
                | o Property BeginMeridianAngle(    ) As   (Read Only)
                | 
                | Returns BeginMeridianAngle on the object.

        :return:
        """
        return self.hybrid_shape_sphere.BeginMeridianAngle

    @property
    def begin_parallel_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BeginParallelAngle
                | o Property BeginParallelAngle(    ) As   (Read Only)
                | 
                | Returns BeginParallelAngle on the object.

        :return:
        """
        return self.hybrid_shape_sphere.BeginParallelAngle

    @property
    def center(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Center
                | o Property Center(    ) As
                | 
                | Returns or sets the sphere center. Sub-element(s) supported
                | (see object): . 
                |
                | Example:
                | This example retrieves in
                | HybShpSphereCenter the center of the HybShpSphere hybrid
                | shape sphere. Dim HybShpSphereCenter As Reference
                | HybShpSphereCenter = HybShpSphere.Center

        :return:
        """
        return self.hybrid_shape_sphere.Center

    @center.setter
    def center(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sphere.Center = value 

    @property
    def end_meridian_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndMeridianAngle
                | o Property EndMeridianAngle(    ) As   (Read Only)
                | 
                | Returns EndMeridianAngle on the object.

        :return:
        """
        return self.hybrid_shape_sphere.EndMeridianAngle

    @property
    def end_parallel_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndParallelAngle
                | o Property EndParallelAngle(    ) As   (Read Only)
                | 
                | Returns EndParallelAngle on the object.

        :return:
        """
        return self.hybrid_shape_sphere.EndParallelAngle

    @property
    def limitation(self, i_limitation_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | Limitation
                | o Property Limitation(        iLimitationType)
                | 
                | Returns whether the sphere is created as a whole sphere or
                | not. Legal values: 0 for a sphere with angles and 1 for a
                | whole sphere. Example:

        :param i_limitation_type:
        :return:
        """
        return self.hybrid_shape_sphere.Limitation

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Radius
                | o Property Radius(    ) As   (Read Only)
                | 
                | Role: Get sphere radius.

        :return:
        """
        return self.hybrid_shape_sphere.Radius

    def set_begin_meridian_angle(self, i_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetBeginMeridianAngle
                | o Sub SetBeginMeridianAngle(        iAngle)
                | 
                | Sets BeginMeridianAngle on the object.
                |
                | Parameters:
                | iAngle
                |  
                | 
                |  See also:
                |  
                |  See also:


        :param i_angle:
        :return:
        """
        return self.hybrid_shape_sphere.SetBeginMeridianAngle(i_angle)

    def set_begin_parallel_angle(self, i_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetBeginParallelAngle
                | o Sub SetBeginParallelAngle(        iAngle)
                | 
                | Sets BeginParallelAngle on the object.
                |
                | Parameters:
                | iAngle
                |  
                | 
                |  See also:
                |  
                |  See also:


        :param i_angle:
        :return:
        """
        return self.hybrid_shape_sphere.SetBeginParallelAngle(i_angle)

    def set_end_meridian_angle(self, i_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetEndMeridianAngle
                | o Sub SetEndMeridianAngle(        iAngle)
                | 
                | Sets EndMeridianAngle on the object.
                |
                | Parameters:
                | iAngle
                |  
                | 
                |  See also:
                |  
                |  See also:


        :param i_angle:
        :return:
        """
        return self.hybrid_shape_sphere.SetEndMeridianAngle(i_angle)

    def set_end_parallel_angle(self, i_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetEndParallelAngle
                | o Sub SetEndParallelAngle(        iAngle)
                | 
                | Sets EndParallelAngle on the object.
                |
                | Parameters:
                | iAngle
                |  
                | 
                |  See also:
                |  
                |  See also:


        :param i_angle:
        :return:
        """
        return self.hybrid_shape_sphere.SetEndParallelAngle(i_angle)

    def set_radius(self, i_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetRadius
                | o Sub SetRadius(        iRadius)
                | 
                | Sets Radius on the object.
                |
                | Parameters:
                | iAngle
                |  
                | 
                |  See also:
                |  
                |  See also:


        :param i_radius:
        :return:
        """
        return self.hybrid_shape_sphere.SetRadius(i_radius)

    def __repr__(self):
        return f'HybridShapeSphere()'
