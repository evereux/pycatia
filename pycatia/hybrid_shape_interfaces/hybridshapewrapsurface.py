#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeWrapSurface(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape wrap surface object.Role: To access the
                | data of the hybrid shape wrap surface object.This data includes:Use
                | the CATIAHybridShapeFactory to create a HybridShapeWrapSurface object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_wrap_surface = com_object     

    @property
    def deformation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DeformationMode
                | o Property DeformationMode(    ) As
                | 
                | Returns or sets whether the wrap surface is or should be
                | created as a"Normal" or with a "3D" deformation mode. Legal
                | values: 2 for the normal solution and 1 for 3D solution.
                | 
                |
                | Example:
                | This example sets the mode to create the wrap
                | surface hybWrapSurface with a 3D deformation mode.
                | hybWrapSurface.3D deformation mode = 1

        :return:
        """
        return self.hybrid_shape_wrap_surface.DeformationMode

    @deformation_mode.setter
    def deformation_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_wrap_surface.DeformationMode = value 

    @property
    def reference_surface(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReferenceSurface
                | o Property ReferenceSurface(    ) As
                | 
                | Returns or sets the reference surface of the WrapSurface.

        :return:
        """
        return self.hybrid_shape_wrap_surface.ReferenceSurface

    @reference_surface.setter
    def reference_surface(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_wrap_surface.ReferenceSurface = value 

    @property
    def surface(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Surface
                | o Property Surface(    ) As
                | 
                | Returns or sets the reference surface to deform of the
                | WrapSurface.

        :return:
        """
        return self.hybrid_shape_wrap_surface.Surface

    @surface.setter
    def surface(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_wrap_surface.Surface = value 

    @property
    def target_surface(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TargetSurface
                | o Property TargetSurface(    ) As
                | 
                | Returns or sets the target surface of the WrapSurface.

        :return:
        """
        return self.hybrid_shape_wrap_surface.TargetSurface

    @target_surface.setter
    def target_surface(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_wrap_surface.TargetSurface = value 

    def __repr__(self):
        return f'HybridShapeWrapSurface()'
