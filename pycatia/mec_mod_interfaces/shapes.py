#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25

from pycatia.system_interfaces.collection import Collection
from .boundary import Boundary
from .shape import Shape


class Shapes(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | The collection of the shapes making up a body.

    """

    def __init__(self, collection_com_object):
        super().__init__(collection_com_object, child_object=Shape)
        self.shapes = collection_com_object

    def get_boundary(self, i_label):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetBoundary
                | o Func GetBoundary(iLabel) As Boundary
                | 
                | Returns a boundary using its label.
                |
                | Parameters:
                | iLabel
                |    Identification of the Boundary object. See Reference.DisplayName.
                | . 
                |    Returns:
                |   The retrieved boundary

        :return: Boundary()
        """
        return Boundary(self.shapes.GetBoundary(i_label))

    def item(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(iIndex) As
                | 
                | Returns a shape using its index or its name from the Shapes
                | collection.


                | Parameters:
                | iIndex
                |    The index or the name of the shape to retrieve from
                |    the collection of shapes.
                |    As a numeric, this index is the rank of the shape
                |    in the collection.
                |    The index of the first shape in the collection is 1, and
                |    the index of the last shape is 
                | 
                | .   As a string, it is the name you assigned to the shape using
                |    the 
                |  property. 
                |    Returns:
                |   The retrieved shape
                |
                | Examples:
                | 
                | This example retrieves in ThisShape the third shape,
                | and in ThatShape the shape named
                | MyShape in the shape collection of the active document,
                | supposed to be a part document.
                | 
                | Set ThisShape = CATIA.ActiveDocument.Shapes.Item(3)
                | Set ThatShape = CATIA.ActiveDocument.Shapes.Item("MyShape")

        :return: Shape()
        """
        return self.child_object(self.shapes.Item(i_index))

    def __repr__(self):
        return f'Shapes(name="{self.name}")'
