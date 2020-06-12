#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.any_object import AnyObject


class HybridShape(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybridshape = com_object

    @property
    def thickness(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Thickness
                | o Property Thickness() As HybridShape
                | 
                | Returns the thickness of the hybrid shape.   The thickness is a
                | CATIAHybridShapeThickness.  Example:The following example returns the
                | thickness ExtrudeThickness of the extrude Extrude.1 as the origin
                | point of the axis system AxisSystem0:  Dim Extrude1 As AnyObject Set
                | Extrude1 = HybridBody1.HybridShapes.Item  ( "Extrude.1" )  Dim
                | Thickness1 As HybridShapeThickness Set Thickness1 = Extrude1.Thickness

        """
        return HybridShape(self.hybridshape.Thickness)

    def append_hybrid_shape(self, i_hybrid_shape):
        """
        .. note::
            CAA V5 Visual Basic help

                | AppendHybridShape
                | o Sub AppendHybridShape(    HybridShape    iHybridShape)
                | 
                | Appends a hybrid shape to another hybrid shape.
                |
                | Parameters:
                | iHybridShape
                |    The hybrid shape to append.
                |
                | Examples:
                |
                | This example appends the hybrid shape newHybridShape
                | to the hybrid shape oldHybridShape:
                | 
                | oldHybridShape.AppendHybridShape (newHybridShape)

        """
        return self.hybridshape.AppendHybridShape(i_hybrid_shape.com_object)

    def compute(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Compute
                | o Sub Compute()
                | 
                | Computes the result of the hybrid shape.


                | Parameters:


        """
        return self.hybridshape.Compute()

    def __repr__(self):
        return f'HybridShape(name="{self.name}")'
