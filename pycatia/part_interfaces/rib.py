#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.part_interfaces.sweep import Sweep


class Rib(Sweep):
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
                |                                 Rib
                | 
                | Represents the rib shape.
                | The rib shape is made up of a profile represented by a sketch swept along a
                | center curve represented by another sketch. This is a "positive" shape: it adds
                | material to the body it belongs to.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rib = com_object

    def __repr__(self):
        return f'Rib(name="{self.name}")'
