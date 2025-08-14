#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.mec_mod_interfaces.boundary import Boundary
from pycatia.mec_mod_interfaces.shape import Shape
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Shapes(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Shapes
                | 
                | The collection of the shapes making up a body.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Shape)
        self.shapes = com_object

    def get_boundary(self, i_label: str) -> Boundary:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBoundary(CATBSTR iLabel) As Boundary
                | 
                |     Returns a boundary using its label.
                | 
                |     Parameters:
                | 
                |         iLabel
                |             Identification of the 
                | 
                |         Boundary object. See Reference.DisplayName. 
                |     Returns:
                |         The retrieved boundary

        :param str i_label:
        :rtype: Boundary
        """
        return Boundary(self.shapes.GetBoundary(i_label))

    def item(self, i_index: cat_variant) -> Shape:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As Shape
                | 
                |     Returns a shape using its index or its name from the Shapes
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the shape to retrieve from the collection
                |             of shapes. As a numerics, this index is the rank of the shape in the
                |             collection. The index of the first shape in the collection is 1, and the index
                |             of the last shape is 
                | 
                |         Collection.Count. As a string, it is the name you assigned to the shape
                |         using the AnyObject.Name property. 
                |     Returns:
                |         The retrieved shape 
                |     Example:
                |         This example retrieves in ThisShape the third shape, and in ThatShape
                |         the shape named MyShape in the shape collection of the active document,
                |         supposed to be a part document.
                | 
                |          Set ThisShape = CATIA.ActiveDocument.Shapes.Item(3)
                |          Set ThatShape = CATIA.ActiveDocument.Shapes.Item("MyShape")

        :param cat_variant i_index:
        :rtype: Shape
        """
        return Shape(self.shapes.Item(i_index))

    def __getitem__(self, n: int) -> Shape:
        if (n + 1) > self.count:
            raise StopIteration

        return Shape(self.shapes.Item(n + 1))

    def __iter__(self) -> Iterator[Shape]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Shapes(name="{self.name}")'
