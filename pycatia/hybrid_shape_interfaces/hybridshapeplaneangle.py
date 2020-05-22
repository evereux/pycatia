#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePlaneAngle(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape plane angle feature object.Role: To access
                | the data of the hybrid shape plane angle feature object, created with
                | an angle to another plane. This data includes:Use the
                | CATIAHybridShapeFactory to create a HybridShapePlaneAngle object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_angle = com_object     

    @property
    def angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Angle
                | o Property Angle(    ) As   (Read Only)
                | 
                | Returns the rotation angle.

        :return:
        """
        return self.hybrid_shape_plane_angle.Angle

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(    ) As
                | 
                | Returns or sets the plane orientation. Role: The orientation
                | allows you to invert the plane from the reference plane.
                | Legal values: the orientation is 1 if the plane orientation
                | is not inverted, and -1 otherwise.

        :return:
        """
        return self.hybrid_shape_plane_angle.Orientation

    @orientation.setter
    def orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_plane_angle.Orientation = value 

    @property
    def plane(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Plane
                | o Property Plane(    ) As
                | 
                | Returns or sets the reference plane. Sub-element(s)
                | supported (see object): .

        :return:
        """
        return self.hybrid_shape_plane_angle.Plane

    @plane.setter
    def plane(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_plane_angle.Plane = value 

    @property
    def projection_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ProjectionMode
                | o Property ProjectionMode(    ) As
                | 
                | Gets or sets the projection mode status. ProjectionMode =
                | TRUE : Rotation axis will be projected on to reference
                | plane. = FALSE(default) : Rotation axis will be as it is.
                | This example retrieves in ProjMode the projection mode
                | status for the PlaneAngle hybrid shape feature. Dim ProjMode
                | As boolean ProjMode = PlaneAngle.ProjectionMode

        :return:
        """
        return self.hybrid_shape_plane_angle.ProjectionMode

    @property
    def revol_axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RevolAxis
                | o Property RevolAxis(    ) As
                | 
                | Returns or sets the rotation axis. Sub-element(s) supported
                | (see object): , or .

        :return:
        """
        return self.hybrid_shape_plane_angle.RevolAxis

    @revol_axis.setter
    def revol_axis(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_plane_angle.RevolAxis = value 

    def __repr__(self):
        return f'HybridShapePlaneAngle()'
