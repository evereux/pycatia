#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape
from pycatia.mec_mod_interfaces.shape import Shape


class Symmetry(Shape):

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
                |                         Symmetry
                | 
                | Represents the shape symmetry feature object.
                | This solid feature is created from an underlying HybridShapeSymmetry aggregated
                | by the Symmetry. Role: To access the data of the symmetry shape feature object.
                | The data includes:
                | 
                |     The element to be transformed
                |     The reference element which can be a point, a line or a
                |     plane
                | 
                | Use the CATIAShapeFactory to create ShapeFeature object.
                | 
                | See also:
                |     ShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.symmetry = com_object

    @property
    def hybrid_shape(self) -> HybridShape:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HybridShape() As HybridShape (Read Only)
                | 
                |     Gets the underlying HybridShapeSymmetry.
                | 
                |     Example:
                |         The following example explains how to retrieve the underlying
                |         HybridShape Symmetry
                | 
                |           Dim oHybridShape as AnyObject
                |           Set oHybridShape=oSymmetry.HybridShape
                |           oHybridShape.SectionCoupling = 2

        :rtype: HybridShape
        """

        return HybridShape(self.symmetry.HybridShape)

    def __repr__(self):
        return f'Symmetry(name="{ self.name }")'
