#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape
from pycatia.mec_mod_interfaces.shape import Shape


class Rotate(Shape):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         Rotate
                | 
                | Represents the shape rotate feature object.
                | This solid feature is created from an underlying HybridShapeRotate aggregated
                | by the Rotate. Role: To access the data of the hybrid shape rotate feature
                | object. This data includes:
                | 
                |     The element to be rotated
                |     The rotation axis
                |     The angle and its value
                | 
                | Use the CATIAShapeFactory to create ShapeFeature object.
                | 
                | See also:
                |     ShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rotate = com_object

    @property
    def angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Angle() As Angle (Read Only)
                | 
                |     Returns the rotation angle.

        :rtype: Angle
        """

        return Angle(self.rotate.Angle)

    @property
    def angle_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AngleValue() As double
                | 
                |     Returns or sets the rotation angle value.
                | 
                |     Example: This example retrieves in AngleValue the angle value for the
                |     Rotate hybrid shape feature.
                | 
                |      Dim AngleValue As double
                |      Set AngleValue = Rotate.AngleValue

        :rtype: float
        """

        return self.rotate.AngleValue

    @angle_value.setter
    def angle_value(self, value: float):
        """
        :param float value:
        """

        self.rotate.AngleValue = value

    @property
    def axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Axis() As Reference
                | 
                |     Returns or sets the rotation axis.
                |     To set the property, you can use one of the following Boundary objects:
                |     RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge or
                |     RectilinearMonoDimFeatEdge.
                | 
                |     Example: This example retrieves in RotationAxis the rotation axis for the
                |     Rotate hybrid shape feature.
                | 
                |      Dim RotationAxis As Reference
                |      Set RotationAxis = Rotate.Axis

        :rtype: Reference
        """

        return Reference(self.rotate.Axis)

    @axis.setter
    def axis(self, value: Reference):
        """
        :param Reference value:
        """

        self.rotate.Axis = value.com_object

    @property
    def hybrid_shape(self) -> HybridShape:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HybridShape() As HybridShape (Read Only)
                | 
                |     Gets the underlying HybridShapeRotate.
                | 
                |     Example:
                |         The following example explains how to retrieve the underlying
                |         HybridShape Rotate
                | 
                |           Dim oHybridShape as AnyObject
                |           Set oHybridShape=oRotate.HybridShape
                |           oHybridShape.SectionCoupling = 2

        :rtype: HybridShape
        """

        return HybridShape(self.rotate.HybridShape)

    def __repr__(self):
        return f'Rotate(name="{ self.name }")'
