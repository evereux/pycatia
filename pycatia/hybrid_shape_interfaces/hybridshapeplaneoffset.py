#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePlaneOffset(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Offset plane.Role: Allows to access data of the plane feature created
                | with an offset to another plane.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_offset = com_object     

    @property
    def offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Offset
                | o Property Offset(    ) As   (Read Only)
                | 
                | Returns the offset value.

        :return:
        """
        return self.hybrid_shape_plane_offset.Offset

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
        return self.hybrid_shape_plane_offset.Orientation

    @orientation.setter
    def orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_plane_offset.Orientation = value 

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
        return self.hybrid_shape_plane_offset.Plane

    @plane.setter
    def plane(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_plane_offset.Plane = value 

    def __repr__(self):
        return f'HybridShapePlaneOffset()'
