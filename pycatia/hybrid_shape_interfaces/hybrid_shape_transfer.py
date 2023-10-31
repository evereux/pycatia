#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

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
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

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
    def element_to_transfer(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ElementToTransfer() As Reference
                | 
                |     Returns or sets the element to transfer.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_transfer.ElementToTransfer)

    @element_to_transfer.setter
    def element_to_transfer(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_transfer.ElementToTransfer = reference_element.com_object

    @property
    def surface_to_unfold(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SurfaceToUnfold() As Reference
                | 
                |     Returns or sets the surface to unfold.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_transfer.SurfaceToUnfold)

    @surface_to_unfold.setter
    def surface_to_unfold(self, reference_surface: Reference):
        """
        :param Reference reference_surface:
        """

        self.hybrid_shape_transfer.SurfaceToUnfold = reference_surface.com_object

    @property
    def type_of_transfer(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TypeOfTransfer() As long
                | 
                |     Returns or sets the type of transfer.
                | 
                |         0= The type of surface is not defined
                |         1= The type of transfer is folded to unfolded
                |         2= The type of surface is unfolded to folded

        :rtype: int
        """

        return self.hybrid_shape_transfer.TypeOfTransfer

    @type_of_transfer.setter
    def type_of_transfer(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_transfer.TypeOfTransfer = value

    @property
    def unfold_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property UnfoldType() As long
                | 
                |     Returns or sets the type of unfold to take into account during
                |     transfer.
                | 
                |         0= The type is undefined
                |         1= The surface to unfold is ruled,
                |         2= the surface to unfold is all

        :rtype: int
        """

        return self.hybrid_shape_transfer.UnfoldType

    @unfold_type.setter
    def unfold_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_transfer.UnfoldType = value

    @property
    def unfolded_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property UnfoldedSurface() As Reference
                | 
                |     Returns or sets the unfolded surface.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_transfer.UnfoldedSurface)

    @unfolded_surface.setter
    def unfolded_surface(self, reference_surface: Reference):
        """
        :param Reference reference_surface:
        """

        self.hybrid_shape_transfer.UnfoldedSurface = reference_surface.com_object

    def __repr__(self):
        return f'HybridShapeTransfer(name="{self.name}")'
