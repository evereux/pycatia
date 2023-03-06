#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.part_interfaces.boolean_shape import BooleanShape


class Intersect(BooleanShape):
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
                |                         PartInterfaces.BooleanShape
                |                             Intersect
                | 
                | Represents the intersect boolean operation.
                | It is performed between a body and the current shape.
                | 
                | Example
                | 
                | The following example shows how to create a new shape by intersecting two
                | existing pads Pad1 and Pad2, created in two different bodies Body1 and Body2
                | respectively, using the existing shape factory named
                | shapeFactory.
                | 
                |  ' Make Pad1 the current shape
                |  CATIA.ActiveDocument.Part.CurrentShape = Pad1
                |  ' 
                |  ' Create the intersection between Pad1 and Body2 
                |  Set NewShape      = shapeFactory.AddNewIntersect(Body2)

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.intersect = com_object

    def __repr__(self):
        return f'Intersect(name="{self.name}")'
