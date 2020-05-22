#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePlane1Curve(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | plane through a curve.Role:  Allows to access data of the plane
                | feature passing though  a planar curve.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane1_curve = com_object     

    @property
    def curve(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Curve
                | o Property Curve(    ) As
                | 
                | Role: Get the planar curve.

        :return:
        """
        return self.hybrid_shape_plane1_curve.Curve

    def __repr__(self):
        return f'HybridShapePlane1Curve()'
