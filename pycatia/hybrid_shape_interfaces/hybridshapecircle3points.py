#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeCircle3Points(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape circle object defined using three
                | points.Role: To access the data of the hybrid shape circle object.This
                | data includes the circle three passing points.Use the
                | CATIAHybridShapeFactory to create a HybridShapeCircle2PointsRad
                | object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle3_points = com_object     

    @property
    def element1(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Element1
                | o Property Element1(    ) As
                | 
                | Returns or sets the circle first passing point. Sub-
                | element(s) supported (see object): . 
                |
                | Example:
                | This example
                | retrieves the first passing point of the HybShpCircle3Pt
                | hybrid shape circle in HybShpCircle3PtFirstPassingPoint
                | point. Dim HybShpCircle3PtFirstPassingPoint As Reference Set
                | HybShpCircle3PtFirstPassingPoint= HybShpCircle3Pt.Element1

        :return:
        """
        return self.hybrid_shape_circle3_points.Element1

    @element1.setter
    def element1(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle3_points.Element1 = value 

    @property
    def element2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Element2
                | o Property Element2(    ) As
                | 
                | Returns or sets the circle second passing point. Sub-
                | element(s) supported (see object): . 
                |
                | Example:
                | This example
                | sets the second passing point of the HybShpCircle3Pt hybrid
                | shape circle as the Point2 point. HybShpCircle3Pt.Element2
                | Point2

        :return:
        """
        return self.hybrid_shape_circle3_points.Element2

    @element2.setter
    def element2(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle3_points.Element2 = value 

    @property
    def element3(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Element3
                | o Property Element3(    ) As
                | 
                | Returns or sets the circle third passing point. Sub-
                | element(s) supported (see object): . 
                |
                | Example:
                | This example
                | retrieves the third passing point of the HybShpCircle3Pt
                | hybrid shape circle in HybShpCircle3PtThirdPassingPoint
                | point. Dim HybShpCircle3PtThirdPassingPoint As Reference Set
                | HybShpCircle3PtThirdPassingPoint= HybShpCircle3Pt.Element3

        :return:
        """
        return self.hybrid_shape_circle3_points.Element3

    @element3.setter
    def element3(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle3_points.Element3 = value 

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets the circle support surface. Sub-element(s)
                | supported (see object): . 
                |
                | Example:
                | This example retrieves in
                | HybShpCircleSupportSurf the support surface of the
                | HybShpCircle hybrid shape circle. Dim
                | HybShpCircleSupportSurf As Reference HybShpCircleSupportSurf
                | = HybShpCircle.Support

        :return:
        """
        return self.hybrid_shape_circle3_points.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle3_points.Support = value 

    def remove_support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveSupport
                | o Sub RemoveSupport(    )
                | 
                | Removes the support surface.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_circle3_points.RemoveSupport()

    def __repr__(self):
        return f'HybridShapeCircle3Points()'
