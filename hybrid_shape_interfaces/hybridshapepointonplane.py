#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePointOnPlane(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Point on a plane.Role:  Allows to access data of the point feature
                | created on a plane with a reference point or not.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_on_plane = com_object     

    @property
    def first_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstDirection
                | o Property FirstDirection(    ) As
                | 
                | Returns or sets the first direction on the plane to compute
                | the point (for stability). 
                |
                | Example:
                | This example retrieves
                | in oDirection the direction of the PointOnPlane feature. Dim
                | oDirection As CATIAHybridShapeDirection Set oDirection =
                | PointOnPlane.FirstDirection

        :return:
        """
        return self.hybrid_shape_point_on_plane.FirstDirection

    @first_direction.setter
    def first_direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_on_plane.FirstDirection = value 

    @property
    def plane(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Plane
                | o Property Plane(    ) As
                | 
                | Returns or sets the support plane. Sub-element(s) supported
                | (see object): . 
                |
                | Example:
                | This example retrieves in oPlane
                | the supporting Plane for PointOnPlane feature. Dim oPlane As
                | CATIAReference Set oPlane = PointOnPlane.Plane

        :return:
        """
        return self.hybrid_shape_point_on_plane.Plane

    @plane.setter
    def plane(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_on_plane.Plane = value 

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Point
                | o Property Point(    ) As
                | 
                | Returns or sets the reference point. This data is not
                | mandatory, if Point is null, the projection of the origin
                | point on the plane is taken. Sub-element(s) supported (see
                | object): . 
                |
                | Example:
                | This example retrieves in oPoint the
                | reference point for PointOnPlane feature. Dim oPoint As
                | CATIAReference Set oPoint = PointOnPlane.Point

        :return:
        """
        return self.hybrid_shape_point_on_plane.Point

    @point.setter
    def point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_on_plane.Point = value 

    @property
    def projection_surface(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ProjectionSurface
                | o Property ProjectionSurface(    ) As
                | 
                | Returns or sets the projection surface to compute the point.
                | 
                |
                | Example:
                | This example retrieves in oProjSur the projection
                | surface of the PointOnPlane feature. Dim oProjSur As
                | CATIAReference Set oProjSur = PointOnPlane.ProjectionSurface

        :return:
        """
        return self.hybrid_shape_point_on_plane.ProjectionSurface

    @projection_surface.setter
    def projection_surface(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_on_plane.ProjectionSurface = value 

    @property
    def x_offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | XOffset
                | o Property XOffset(    ) As   (Read Only)
                | 
                | Returns the X cartesian coordinate in the plane. Example:
                | This example retrieves in oX the X coordinate for
                | PointOnPlane feature. Dim oX As CATIALength Set oX =
                | PointOnPlane.XOffset

        :return:
        """
        return self.hybrid_shape_point_on_plane.XOffset

    @property
    def y_offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | YOffset
                | o Property YOffset(    ) As   (Read Only)
                | 
                | Returns the Y cartesian coordinate in the plane. Example:
                | This example retrieves in oY the Y coordinate for
                | PointOnPlane feature. Dim oY As CATIALength Set oY =
                | PointOnPlane.YOffset

        :return:
        """
        return self.hybrid_shape_point_on_plane.YOffset

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
                | oDir
                |       second direction
                |       
                | 
                |  See also:


        :param o_dir_x:
        :param o_dir_y:
        :param o_dir_z:
        :return:
        """
        return self.hybrid_shape_point_on_plane.GetSecondDirection(o_dir_x, o_dir_y, o_dir_z)

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
                | iDir
                |       second direction
                |       
                | 
                |  See also:


        :param i_dir_x:
        :param i_dir_y:
        :param i_dir_z:
        :return:
        """
        return self.hybrid_shape_point_on_plane.SetSecondDirection(i_dir_x, i_dir_y, i_dir_z)

    def __repr__(self):
        return f'HybridShapePointOnPlane()'
