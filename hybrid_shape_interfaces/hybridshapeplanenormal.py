#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePlaneNormal(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Normal plane.Role:  Allows to access data of the plane feature normal
                | to a curve at a given point.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_normal = com_object     

    @property
    def curve(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Curve
                | o Property Curve(    ) As
                | 
                | Role: Get the curve to which the plane is to be normal.

        :return:
        """
        return self.hybrid_shape_plane_normal.Curve

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Point
                | o Property Point(    ) As
                | 
                | Role: Get the point where the plane is to be normal.

        :return:
        """
        return self.hybrid_shape_plane_normal.Point

    def __repr__(self):
        return f'HybridShapePlaneNormal()'
