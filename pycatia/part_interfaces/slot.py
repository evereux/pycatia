#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.part_interfaces.sweep import Sweep


class Slot(Sweep):
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
                |                             PartInterfaces.Sweep
                |                                 Slot
                | 
                | Represents the slot shape.
                | The slot shape is made up of a profile represented by a sketch swept along a
                | center curve represented by another sketch. This is a "negative" shape: it
                | removes material from the body it belongs to. The profile sketch is usually
                | drawn on another shape face.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.slot = com_object

    def __repr__(self):
        return f'Slot(name="{self.name}")'
