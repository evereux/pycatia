#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.shape import Shape


class SurfaceBasedShape(Shape):

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
                |                         SurfaceBasedShape
                | 
                | Represents the shapes based on Surface.
                | It is the base object for Split , SewSurface , CloseSurface and ThickSurface
                | shapes.
                | 
                | See also:
                |     Split, SewSurface, CloseSurface, ThickSurface
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.surface_based_shape = com_object

    @property
    def surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Surface() As Reference
                | 
                |     Returns or sets the surface.

        :rtype: Reference
        """

        return Reference(self.surface_based_shape.Surface)

    @surface.setter
    def surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.surface_based_shape.Surface = value.com_object

    def __repr__(self):
        return f'SurfaceBasedShape(name="{ self.name }")'
