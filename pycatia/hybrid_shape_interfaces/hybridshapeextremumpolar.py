#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeExtremumPolar(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape extremum polar  feature.Role: To access
                | the data of the extremum polar  feature . This data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extremum_polar = com_object     

    @property
    def angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Angle
                | o Property Angle(    ) As   (Read Only)
                | 
                | returns the resulting angle of extremum.

        :return:
        """
        return self.hybrid_shape_extremum_polar.Angle

    @property
    def contour(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Contour
                | o Property Contour(    ) As
                | 
                | returns or sets the input contour.

        :return:
        """
        return self.hybrid_shape_extremum_polar.Contour

    @property
    def dir(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Dir
                | o Property Dir(    ) As
                | 
                | returns or sets the direction of computation.

        :return:
        """
        return self.hybrid_shape_extremum_polar.Dir

    @property
    def extremum_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ExtremumType
                | o Property ExtremumType(    ) As
                | 
                | returns or sets the type of extremum.

        :return:
        """
        return self.hybrid_shape_extremum_polar.ExtremumType

    @property
    def origin(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Origin
                | o Property Origin(    ) As
                | 
                | returns or sets the origin of the polar axis.

        :return:
        """
        return self.hybrid_shape_extremum_polar.Origin

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Radius
                | o Property Radius(    ) As   (Read Only)
                | 
                | returns the resulting radius of extremum.

        :return:
        """
        return self.hybrid_shape_extremum_polar.Radius

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | returns or sets the support (if exist).

        :return:
        """
        return self.hybrid_shape_extremum_polar.Support

    def __repr__(self):
        return f'HybridShapeExtremumPolar()'
