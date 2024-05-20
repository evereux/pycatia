#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeAxisLine(HybridShape):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeAxisLine
                | 
                | Represents the hybrid shape axis line feature object.
                | Role: To access the data of the hybrid shape axis line feature object. This
                | data includes:
                | 
                |     The element used to compute the axis
                |     The direction used in orientation of axis
                |     AxisLineType to change the axis type
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeAxisLine
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_axis_line = com_object

    @property
    def axis_line_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AxisLineType() As long
                | 
                |     Returns or sets the axis line type.
                |     Legal values:
                | 
                |     1
                |         This option creates Axis along major axis if element is ellipse or
                |         oblong, Axis is aligned with direction specified if input is circle and
                |         coincides with revolution axis if element is revolution
                |         surface
                |     2
                |         This option creates Axis along minor axis if element is ellipse or
                |         oblong, Axis is normal to direction specified if input is
                |         circle
                |     3
                |         This option creates Axis normal to the element if it is circle, ellipse
                |         or oblong
                | 
                | Example:
                |     This example retrieves in oType the axis line type for the AxisLine hybrid
                |     shape feature.
                | 
                |      Dim oType
                |      Set oType = AxisLine.AxisLineType

        :rtype: int
        """

        return self.hybrid_shape_axis_line.AxisLineType

    @axis_line_type.setter
    def axis_line_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_axis_line.AxisLineType = value

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Direction() As HybridShapeDirection
                | 
                |     Gets the reference direction used in computation of axis.
                |     This is useful only if the element selected is circle, arc or sphere. If
                |     the element is circle or arc Axis may be normal to reference direction or
                |     aligned with reference direction
                | 
                |     Example:
                |         This example retrieves in oDir the direction for the AxisLine hybrid
                |         shape feature.
                | 
                |          Dim oDir As CATIAHybridShapeDirection
                |          Set oDir = AxisLine.Direction

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_axis_line.Direction)

    @direction.setter
    def direction(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.hybrid_shape_axis_line.Direction = value

    @property
    def element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Element() As Reference
                | 
                |     Returns or sets the element from which axis is computed.
                | 
                |     Example:
                |         This example retrieves in Element the element from which axis is
                |         computed for the AxisLine hybrid shape feature.
                | 
                |          Dim Element As Reference 
                |          Set Element = AxisLine.Element

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_axis_line.Element)

    @element.setter
    def element(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_axis_line.Element = value.com_object

    def __repr__(self):
        return f'HybridShapeAxisLine(name="{ self.name }")'
