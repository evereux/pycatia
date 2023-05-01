#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.part_interfaces.revolution import Revolution


class Groove(Revolution):
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
                |                                 Groove
                | 
                | Represents the groove shape.
                | A groove is made up of a sketch, used as the groove profile, containing an
                | axis, used as the revolution axis, and two limiting angles around this axis.
                | This is a "negative" shape: it removes material from the body it belongs
                | to.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.groove = com_object

    def __repr__(self):
        return f'Groove(name="{self.name}")'
