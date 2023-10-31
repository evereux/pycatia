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


class Affinity(Shape):

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
                |                         Affinity
                | 
                | Represents the hybrid shape Affinity feature object.
                | This solid feature is created from an underlying HybridShapeAffinity aggregated
                | by the Affinity. Role: To access the data of the hybrid shape Affinity feature
                | object. This data includes:
                | 
                |     The element to Affinity
                |     Origin for the Affinity
                |     Plane for the Affinity
                |     Direction for the Affinity
                |     XRatio Value for the Affinity
                |     YRatio Value for the Affinity
                |     ZRatio Value for the Affinity
                |     The translation distance and its value
                | 
                | Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.affinity = com_object

    @property
    def hybrid_shape(self) -> HybridShape:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HybridShape() As HybridShape (Read Only)
                | 
                |     Gets the underlying HybridShapeAffinity.
                | 
                |     Example:
                |         The following example explains how to retrieve the underlying
                |         HybridShape Affinity
                | 
                |           Dim oHybridShape as AnyObject
                |           Set oHybridShape=oAffinity.HybridShape
                |           oHybridShape.ElemToAffinity = reference1

        :rtype: HybridShape
        """

        return HybridShape(self.affinity.HybridShape)

    def __repr__(self):
        return f'Affinity(name="{ self.name }")'
