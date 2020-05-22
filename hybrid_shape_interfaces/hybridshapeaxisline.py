#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeAxisLine(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape axis line feature object.Role: To access
                | the data of the hybrid shape axis line feature object. This data
                | includes:Use the  CATIAHybridShapeFactory to create a
                | HybridShapeAxisLine object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_axis_line = com_object

    @property
    def axis_line_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AxisLineType
                | o Property AxisLineType(    ) As
                | 
                | Returns or sets the axis line type. Legal values: 1 This
                | option creates Axis along major axis if element is ellipse
                | or oblong, Axis is aligned with direction specified if input
                | is circle and coincides with revolution axis if element is
                | revolution surface 2 This option creates Axis along minor
                | axis if element is ellipse or oblong, Axis is normal to
                | direction specified if input is circle 3 This option creates
                | Axis normal to the element if it is circle, ellipse or
                | oblong

        :return:
        """
        return self.hybrid_shape_axis_line.AxisLineType

    @axis_line_type.setter
    def axis_line_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_axis_line.AxisLineType = value

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction
                | o Property Direction(    ) As
                | 
                | Gets the reference direction used in computation of axis.
                | This is useful only if the element selected is circle, arc
                | or sphere. If the element is circle or arc Axis may be
                | normal to reference direction or aligned with reference
                | direction 
                |
                | Example:
                | This example retrieves in oDir the
                | direction for the AxisLine hybrid shape feature. Dim oDir As
                | CATIAHybridShapeDirection Set oDir = AxisLine.Direction

        :return:
        """
        return self.hybrid_shape_axis_line.Direction

    @property
    def element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Element
                | o Property Element(    ) As
                | 
                | Returns or sets the element from which axis is computed.
                | 
                |
                | Example:
                | This example retrieves in Element the element from
                | which axis is computed for the AxisLine hybrid shape
                | feature. Dim Element As Reference Set Element =
                | AxisLine.Element

        :return:
        """
        return self.hybrid_shape_axis_line.Element

    @element.setter
    def element(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_axis_line.Element = value

    def __repr__(self):
        return f'HybridShapeAxisLine()'
