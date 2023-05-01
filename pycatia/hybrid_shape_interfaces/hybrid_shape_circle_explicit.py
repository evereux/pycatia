#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_circle import HybridShapeCircle


class HybridShapeCircleExplicit(HybridShapeCircle):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircleExplicit
                | 
                | Represents the hybrid shape circle object explicitely defined.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes:
                | 
                |     ??????????????
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircleExplicit
                | object.
                | 
                | See also:
                |     HybridShapeFactory 

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_explicit = com_object

    def __repr__(self):
        return f'HybridShapeCircleExplicit(name="{self.name}")'
