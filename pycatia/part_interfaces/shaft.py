#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.part_interfaces.revolution import Revolution


class Shaft(Revolution):
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
                |                             PartInterfaces.Revolution
                |                                 Shaft
                | 
                | Represents the shaft shape.
                | A shaft is made up of a sketch, used as the shaft profile, and containing an
                | axis, used as the revolution axis, and two limiting angles around this axis.
                | This is a "positive" shape: it adds material to the body it belongs
                | to.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.shaft = com_object

    def __repr__(self):
        return f'Shaft(name="{self.name}")'
