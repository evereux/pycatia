#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.part_interfaces.prism import Prism


class Pocket(Prism):
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
                |                         PartInterfaces.SketchBasedShape
                |                             PartInterfaces.Prism
                |                                 Pocket
                | 
                | Represents the pocket shape.
                | A pocket is created by extruding a profile represented by a sketch in one or
                | two opposite directions. It is a "negative" shape: it removes material from the
                | body it belongs to. The sketch is usually drawn on another shape
                | face.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.pocket = com_object

    def __repr__(self):
        return f'Pocket(name="{self.name}")'
