#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.in_interfaces.move import Move
from .shape import Shape


class Solid(Shape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents an imported solid object.Role: the imported solid is a
                | solid obtained from copy/paste with link or design in context.The
                | solid object has a link to a source element obtained
                | fromactivateLinkAnchor('','SourceElement','SourceElement')and a source
                | product obtained
                | fromactivateLinkAnchor('','SourceProduct','SourceProduct').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.solid = com_object

    @property
    def move(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Move
                | o Property Move() As   (Read Only)
                | 
                | Returns the move object of the solid. Role: The move object
                | is aggregated by the solid object and itself aggregates a
                | movable object to which you can apply a move transformation
                | by means of an isometry matrix. It moves the solid according
                | to this isometry. 
                |
                | Example:
                | This example retrieves the move
                | object EngineMoveObject for the Engine product. Dim
                | EngineMoveObject As Move Set EngineMoveObject = Engine.Move
                | See also:

        :return:
        """
        return Move(self.solid.Move)

    @property
    def source_element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SourceElement
                | o Property SourceElement() As   (Read Only)
                | 
                | Returns the source element of the imported solid. Role:
                | returns the linked element in the source part. 
                |
                | Example:
                | The
                | following example returns in element the source element of
                | the imported solid importedSolid: Set element =
                | importedSolid.SourceElement

        :return: AnyObject()
        """
        return self.solid.SourceElement

    @property
    def source_product(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SourceProduct
                | o Property SourceProduct() As   (Read Only)
                | 
                | Returns the source product instance of the imported solid.
                | Role: returns the product instance which was selected when
                | the import was created. 
                |
                | Example:
                | The following example
                | returns in prod1 the source product instance of the imported
                | solid importedSolid: Set prod1 = importedSolid.SourceProduct

        :return: AnyObject
        """
        return self.solid.SourceProduct

    def __repr__(self):
        return f'Solid()'
