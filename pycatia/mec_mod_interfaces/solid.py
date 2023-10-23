#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.move import Move
from pycatia.mec_mod_interfaces.shape import Shape
from pycatia.system_interfaces.any_object import AnyObject


class Solid(Shape):

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
                |                         Solid
                | 
                | Represents an imported solid object.
                | Role: the imported solid is a solid obtained from copy/paste with link or
                | design in context.
                | The solid object has a link to a source element obtained from SourceElement and
                | a source product obtained from SourceProduct .
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.solid = com_object

    @property
    def move(self) -> Move:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Move() As Move (Read Only)
                | 
                |     Returns the move object of the solid.
                |     Role: The move object is aggregated by the solid object and itself
                |     aggregates a movable object to which you can apply a move transformation by
                |     means of an isometry matrix. It moves the solid according to this
                |     isometry.
                | 
                |     Example:
                | 
                |           This example retrieves the move object EngineMoveObject for
                |           the
                |          Engine product.
                |          
                | 
                |          Dim EngineMoveObject As Move
                |          Set EngineMoveObject = Engine.Move
                |          
                | 
                | 
                |          
                | 
                |     See also:
                |         Move

        :rtype: Move
        """

        return Move(self.solid.Move)

    @property
    def source_element(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SourceElement() As AnyObject (Read Only)
                | 
                |     Returns the source element of the imported solid.
                |     Role: returns the linked element in the source part.
                | 
                |     Example:
                |         The following example returns in element the source element of the
                |         imported solid importedSolid:
                | 
                |          Set element = importedSolid.SourceElement

        :rtype: AnyObject
        """

        return AnyObject(self.solid.SourceElement)

    @property
    def source_product(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SourceProduct() As AnyObject (Read Only)
                | 
                |     Returns the source product instance of the imported solid.
                |     Role: returns the product instance which was selected when the import was
                |     created.
                | 
                |     Example:
                |         The following example returns in prod1 the source product instance of
                |         the imported solid importedSolid:
                | 
                |          Set prod1 = importedSolid.SourceProduct

        :rtype: AnyObject
        """

        return AnyObject(self.solid.SourceProduct)

    def __repr__(self):
        return f'Solid(name="{ self.name }")'
