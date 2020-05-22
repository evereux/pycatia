#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeTransfer(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape Transfer feature object.Role: To access
                | the data of the hybrid shape Transfer feature object. This data
                | includes:Use the  CATIAHybridShapeFactory to create a
                | HybridShapeTransfer object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_transfer = com_object     

    @property
    def element_to_transfer(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ElementToTransfer
                | o Property ElementToTransfer(    ) As
                | 
                | Returns or sets the element to transfer.

        :return:
        """
        return self.hybrid_shape_transfer.ElementToTransfer

    @element_to_transfer.setter
    def element_to_transfer(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_transfer.ElementToTransfer = value 

    @property
    def surface_to_unfold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SurfaceToUnfold
                | o Property SurfaceToUnfold(    ) As
                | 
                | Returns or sets the surface to unfold.

        :return:
        """
        return self.hybrid_shape_transfer.SurfaceToUnfold

    @surface_to_unfold.setter
    def surface_to_unfold(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_transfer.SurfaceToUnfold = value 

    @property
    def type_of_transfer(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TypeOfTransfer
                | o Property TypeOfTransfer(    ) As
                | 
                | Returns or sets the type of transfer. 0= The type of surface
                | is not defined 1= The type of transfer is folded to unfolded
                | 2= The type of surface is unfolded to folded

        :return:
        """
        return self.hybrid_shape_transfer.TypeOfTransfer

    @type_of_transfer.setter
    def type_of_transfer(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_transfer.TypeOfTransfer = value 

    @property
    def unfold_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UnfoldType
                | o Property UnfoldType(    ) As
                | 
                | Returns or sets the type of unfold to take into account
                | during transfer. 0= The type is undefined 1= The surface to
                | unfold is ruled, 2= the surface to unfold is all

        :return:
        """
        return self.hybrid_shape_transfer.UnfoldType

    @unfold_type.setter
    def unfold_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_transfer.UnfoldType = value 

    @property
    def unfolded_surface(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UnfoldedSurface
                | o Property UnfoldedSurface(    ) As
                | 
                | Returns or sets the unfolded surface.

        :return:
        """
        return self.hybrid_shape_transfer.UnfoldedSurface

    @unfolded_surface.setter
    def unfolded_surface(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_transfer.UnfoldedSurface = value 

    def __repr__(self):
        return f'HybridShapeTransfer()'
