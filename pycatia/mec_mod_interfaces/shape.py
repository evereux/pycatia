#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class Shape(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Shape
                | 
                | Represents the Shape object.
                | It is an abstract object which is not intended to be created as such, from
                | which all objects having a shape representation derive.
                | 
                | See also:
                |     SketchBasedShape, BooleanShape, DressUpShape, TransformationShape

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.shape = com_object

    def __repr__(self):
        return f'Shape(name="{self.name}")'
