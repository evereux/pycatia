#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePlaneOffsetPt(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Offset plane with point reference.Role: Allows to access data of the
                | plane feature parallel to  another plane and passing through a Point.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_offset_pt = com_object     

    @property
    def plane(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Plane
                | o Property Plane(    ) As
                | 
                | Role: Get the reference plane.

        :return:
        """
        return self.hybrid_shape_plane_offset_pt.Plane

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Point
                | o Property Point(    ) As
                | 
                | Role: Get the reference point.

        :return:
        """
        return self.hybrid_shape_plane_offset_pt.Point

    def __repr__(self):
        return f'HybridShapePlaneOffsetPt()'
