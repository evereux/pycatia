#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSurfaceExplicit(HybridShape):
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
                |                         HybridShapeSurfaceExplicit
                | 
                | Represents the hybrid shape Surface explicit feature object.
                | Role: Declare hybrid shape Surface explicit feature object.
                | 
                | See also:
                |     HybridShapeFactory.AddNewSurfaceDatum 

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_surface_explicit = com_object

    def __repr__(self):
        return f'HybridShapeSurfaceExplicit(name="{self.name}")'
