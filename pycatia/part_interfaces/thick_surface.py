#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.length import Length
from pycatia.part_interfaces.surface_based_shape import SurfaceBasedShape


class ThickSurface(SurfaceBasedShape):

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
                |                         PartInterfaces.SurfaceBasedShape
                |                             ThickSurface
                | 
                | Represents the ThickSurface feature.
                | It thicks surface using an offset element (such as a surface or a skin) and two
                | offset values TopOffset and Botoffset. TopOffset is the offset between the
                | offset element and the top skin of the feature. BotOffset is the offset between
                | the offset element and the bottom skin of the feature.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.thick_surface = com_object

    @property
    def bot_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BotOffset() As Length (Read Only)
                | 
                |     Returns the value of the bottom offset.
                | 
                |     Example:
                |         The following example returns in botoffset the bottom offset of the
                |         thicksurface firstThickSurface:
                | 
                |          Set botoffset = firstThickSurface.BotOffset

        :rtype: Length
        """

        return Length(self.thick_surface.BotOffset)

    @property
    def offset_side(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OffsetSide() As long (Read Only)
                | 
                |     Returns the offset direction (defines in regards of the normal direction)
                |     .
                | 
                |     Example:
                |         The following example returns in offsetside the side of the
                |         ThickSurface firstThickSurface:
                | 
                |          Set offsetside = firstThickSurface.OffsetSide

        :rtype: int
        """

        return self.thick_surface.OffsetSide

    @property
    def top_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TopOffset() As Length (Read Only)
                | 
                |     Returns the value of the top offset.
                | 
                |     Example:
                |         The following example returns in topoffset the top offset of the
                |         ThickSurface firstThickSurface:
                | 
                |          Set topoffset = firstThickSurface.TopOffset

        :rtype: Length
        """

        return Length(self.thick_surface.TopOffset)

    def swap_offset_side(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub swap_OffsetSide()
                | 
                |     Swap the side of the offset. 
                | 
                | Example:
                |     The following example changes the side of the ThickSurface
                |     firstThickSurface:
                | 
                |      call firstThickSurface.swap_OffsetSide()
                |      
                | 
                |     Copyright © 1999-2011, Dassault Systèmes. All rights
                |     reserved.

        :rtype: None
        """
        return self.thick_surface.swap_OffsetSide()

    def __repr__(self):
        return f'ThickSurface(name="{ self.name }")'
