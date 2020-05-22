#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeBoundary(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape boundary feature object.Role: To access
                | the data of the hybrid shape boundary feature object. This data
                | includes:Use the  CATIAHybridShapeFactory to create a
                | HybridShapeBoundary object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_boundary = com_object

    @property
    def from_limit(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | From
                | o Property From(    ) As
                | 
                | Removes or sets the ending limit(i.e Limit2) of the boundary

        :return:
        """
        return self.hybrid_shape_boundary.From

    @property
    def from_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FromOrientation
                | o Property FromOrientation(    ) As
                | 
                | Gets or sets the Ending Limit Orientation (i.e same or
                | inverse)

        :return:
        """
        return self.hybrid_shape_boundary.FromOrientation

    @property
    def initial_element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InitialElement
                | o Property InitialElement(    ) As
                | 
                | Returns or sets the element used to initialize the boundary
                | propagation. Sub-element(s) supported (see object): .
                | 
                |
                | Example:
                | This example retrieves in InitElem the initial
                | element of the ShpBoundary hybrid shape boundary feature.
                | Dim InitElem As Reference InitElem =
                | ShpBoundary.InitialElement

        :return:
        """
        return self.hybrid_shape_boundary.InitialElement

    @initial_element.setter
    def initial_element(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_boundary.InitialElement = value

    @property
    def propagation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Propagation
                | o Property Propagation(    ) As
                | 
                | Returns or sets the boundary propagation. Legal values:
                | xxxxxxxxxx 
                |
                | Example:
                | This example retrieves in Prop the
                | boundary propagation of the ShpBoundary hybrid shape
                | boundary feature. Prop = ShpBoundary.Propagation

        :return:
        """
        return self.hybrid_shape_boundary.Propagation

    @propagation.setter
    def propagation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_boundary.Propagation = value

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets the support surface around which the
                | boundary is computed. Sub-element(s) supported (see object):
                | . 
                |
                | Example:
                | This example retrieves in SupSurf the initial
                | element of the ShpBoundary hybrid shape boundary feature.
                | Dim SupSurf As Reference SupSurf = ShpBoundary.Support

        :return:
        """
        return self.hybrid_shape_boundary.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_boundary.Support = value

    @property
    def to(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | To
                | o Property To(    ) As
                | 
                | Removes or sets the starting limit(i.e Limit1) of the
                | boundary

        :return:
        """
        return self.hybrid_shape_boundary.To

    @property
    def to_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ToOrientation
                | o Property ToOrientation(    ) As
                | 
                | Gets or sets the Starting Limit Orientation (i.e same or
                | inverse)

        :return:
        """
        return self.hybrid_shape_boundary.ToOrientation

    def __repr__(self):
        return f'HybridShapeBoundary()'
