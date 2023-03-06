#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.shape import Shape


class DressUpShape(Shape):
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
                |                         DressUpShape
                | 
                | Represents the shapes built with other shape sub-elements such as faces or
                | edges.
                | It is the base object for chamfers, drafts, fillets, scalings, shells, and
                | thickness objects.
                | 
                | See also:
                |     Chamfer, Draft, Fillet, Scaling, Shell, Thickness 

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dress_up_shape = com_object

    def __repr__(self):
        return f'DressUpShape(name="{self.name}")'
