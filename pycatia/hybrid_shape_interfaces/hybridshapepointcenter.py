#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePointCenter(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape PointCenter feature object.Role:  To
                | access the data of the hybrid shape PointCenter feature object. It has
                | been created by the CATIAHybridShapeFactory. This data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_center = com_object     

    @property
    def element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Element
                | o Property Element(    ) As
                | 
                | Returns or sets the circle, ellipse or sphere. Sub-
                | element(s) supported (see object): . 
                |
                | Example:
                | This example
                | retrieves in Ref_Circle the center point for the PointCenter
                | hybrid shape feature. Dim Ref_Circle As Reference Set
                | Ref_Circle = PointCenter.Element

        :return:
        """
        return self.hybrid_shape_point_center.Element

    @element.setter
    def element(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_center.Element = value 

    def __repr__(self):
        return f'HybridShapePointCenter()'
