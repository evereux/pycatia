#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeWrapSurface(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeWrapSurface
                | 
                | Represents the hybrid shape wrap surface object.
                | Role: To access the data of the hybrid shape wrap surface
                | object.
                | 
                | This data includes:
                | 
                |     Two definition surfaces (refrence and target), who define the
                |     deformation
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeWrapSurface
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_wrap_surface = com_object

    @property
    def deformation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property DeformationMode() As long
                | 
                |     Returns or sets whether the wrap surface is or should be created as
                |     a"Normal" or with a "3D" deformation mode.
                |     Legal values: 2 for the normal solution and 1 for 3D
                |     solution.
                | 
                |     Example:
                | 
                |           This example sets the mode to create the wrap
                |           surface
                |          hybWrapSurface with a 3D deformation mode.
                |          
                | 
                |          hybWrapSurface.3D deformation mode = 1

        :return: int
        """

        return self.hybrid_shape_wrap_surface.DeformationMode

    @deformation_mode.setter
    def deformation_mode(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_wrap_surface.DeformationMode = value

    @property
    def reference_surface(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ReferenceSurface() As Reference
                | 
                |     Returns or sets the reference surface of the WrapSurface. 
                | 
                | Example:
                |     This example retrieves in ReferenceSurface the surface to deform of the
                |     ShpWrapSurface hybrid shape WrapSurface feature.
                | 
                |      ReferenceSurface = ShpWrapSurface.Surface

        :return: Reference
        """

        return Reference(self.hybrid_shape_wrap_surface.ReferenceSurface)

    @reference_surface.setter
    def reference_surface(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_wrap_surface.ReferenceSurface = value

    @property
    def surface(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Surface() As Reference
                | 
                |     Returns or sets the reference surface to deform of the WrapSurface.
                |     
                | 
                | Example:
                |     This example retrieves in SurfaceToDeform the surface to deform of the
                |     ShpWrapSurface hybrid shape WrapSurface feature.
                | 
                |      SurfaceToDeform = ShpWrapSurface.Surface

        :return: Reference
        """

        return Reference(self.hybrid_shape_wrap_surface.Surface)

    @surface.setter
    def surface(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_wrap_surface.Surface = value

    @property
    def target_surface(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property TargetSurface() As Reference
                | 
                |     Returns or sets the target surface of the WrapSurface. 
                | 
                | Example:
                |     This example retrieves in TargetSurface the surface to deform of the
                |     ShpWrapSurface hybrid shape WrapSurface feature.
                | 
                |      TargetSurface = ShpWrapSurface.Surface

        :return: Reference
        """

        return Reference(self.hybrid_shape_wrap_surface.TargetSurface)

    @target_surface.setter
    def target_surface(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_wrap_surface.TargetSurface = value

    def __repr__(self):
        return f'HybridShapeWrapSurface(name="{ self.name }")'
