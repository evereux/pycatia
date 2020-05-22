#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePlaneTangent(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Tangency plane.Role: Allows to access data of the the plane feature
                | tangent to a surface at a given point.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_tangent = com_object     

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Point
                | o Property Point(    ) As
                | 
                | Role: Get the tangency point.

        :return:
        """
        return self.hybrid_shape_plane_tangent.Point

    @property
    def surface(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Surface
                | o Property Surface(    ) As
                | 
                | Role: Get the surface to which the plane is to be tangent.

        :return:
        """
        return self.hybrid_shape_plane_tangent.Surface

    def __repr__(self):
        return f'HybridShapePlaneTangent()'
