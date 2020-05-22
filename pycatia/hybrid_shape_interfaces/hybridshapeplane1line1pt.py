#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePlane1Line1Pt(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents plane feature defined by a line and a point.Role:  Allows
                | to access data of the plane feature passing though  one line and one
                | point

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane1_line1_pt = com_object     

    @property
    def line(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Line
                | o Property Line(    ) As
                | 
                | Returns or sets the passing line.

        :return:
        """
        return self.hybrid_shape_plane1_line1_pt.Line

    @line.setter
    def line(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_plane1_line1_pt.Line = value 

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Point
                | o Property Point(    ) As
                | 
                | Return or sets the passing point.

        :return:
        """
        return self.hybrid_shape_plane1_line1_pt.Point

    def __repr__(self):
        return f'HybridShapePlane1Line1Pt()'
