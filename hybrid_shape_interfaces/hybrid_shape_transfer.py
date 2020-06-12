#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeTransfer(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeTransfer
                | 
                | Represents the hybrid shape Transfer feature object.
                | Role: To access the data of the hybrid shape Transfer feature object. This data
                | includes:
                | 
                |     The element to transfer
                |     The surface to unfold
                |     The unfolded surface
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeTransfer
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_transfer = com_object

    @property
    def element_to_transfer(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ElementToTransfer() As Reference
                | 
                |     Returns or sets the element to transfer.

        :return: Reference
        """

        return Reference(self.hybrid_shape_transfer.ElementToTransfer)

    @element_to_transfer.setter
    def element_to_transfer(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_transfer.ElementToTransfer = value

    @property
    def surface_to_unfold(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SurfaceToUnfold() As Reference
                | 
                |     Returns or sets the surface to unfold.

        :return: Reference
        """

        return Reference(self.hybrid_shape_transfer.SurfaceToUnfold)

    @surface_to_unfold.setter
    def surface_to_unfold(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_transfer.SurfaceToUnfold = value

    @property
    def type_of_transfer(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property TypeOfTransfer() As long
                | 
                |     Returns or sets the type of transfer.
                | 
                |         0= The type of surface is not defined
                |         1= The type of transfer is folded to unfolded
                |         2= The type of surface is unfolded to folded

        :return: int
        """

        return self.hybrid_shape_transfer.TypeOfTransfer

    @type_of_transfer.setter
    def type_of_transfer(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_transfer.TypeOfTransfer = value

    @property
    def unfold_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property UnfoldType() As long
                | 
                |     Returns or sets the type of unfold to take into account during
                |     transfer.
                | 
                |         0= The type is undefined
                |         1= The surface to unfold is ruled,
                |         2= the surface to unfold is all

        :return: int
        """

        return self.hybrid_shape_transfer.UnfoldType

    @unfold_type.setter
    def unfold_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_transfer.UnfoldType = value

    @property
    def unfolded_surface(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property UnfoldedSurface() As Reference
                | 
                |     Returns or sets the unfolded surface.

        :return: Reference
        """

        return Reference(self.hybrid_shape_transfer.UnfoldedSurface)

    @unfolded_surface.setter
    def unfolded_surface(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_transfer.UnfoldedSurface = value

    def __repr__(self):
        return f'HybridShapeTransfer(name="{ self.name }")'
