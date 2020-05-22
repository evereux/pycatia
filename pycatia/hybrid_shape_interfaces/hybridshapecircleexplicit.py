#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeCircleExplicit(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape circle object explicitely defined.Role: To
                | access the data of the hybrid shape circle object.This data
                | includes:Use the CATIAHybridShapeFactory to create a
                | HybridShapeCircleExplicit object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_explicit = com_object     

    def __repr__(self):
        return f'HybridShapeCircleExplicit()'
