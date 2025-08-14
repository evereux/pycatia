#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.sketcher_interfaces.geometric_element import GeometricElement
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class GeometricElements(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     GeometricElements
                | 
                | A collection of all geometric elements contained in a part or a
                | sketch.
                | Geometric elements are created with the 2D factory for the sketch and with the
                | 3D factory for the part. Geometric elements thus created are then aggregated
                | either in the sketch or as part of the geometric element
                | collection.
                | 
                | See also:
                |     Factory2D, HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=GeometricElement)
        self.geometric_elements = com_object

    def item(self, i_index: cat_variant) -> GeometricElement:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As GeometricElement
                | 
                |     Returns a geometric element using its index or its name from the
                |     GeometricElements collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the geometric element to retrieve from the
                |             collection of geometric elements. As a numerics, this index is the rank of the
                |             geometric element in the collection. The index of the first geometric element
                |             in the collection is 1, and the index of the last geometric element is Count.
                |             As a string, it is the name you assigned to the geometric element using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved geometric element 
                |     Example:
                |         This example retrieves the last item in the geometric element
                |         collection.
                | 
                |          Set lastCst = cstList.Item(cstList.Count)

        :param cat_variant i_index:
        :rtype: GeometricElement
        """
        return GeometricElement(self.geometric_elements.Item(i_index))

    def __getitem__(self, n: int) -> GeometricElement:
        if (n + 1) > self.count:
            raise StopIteration

        return GeometricElement(self.geometric_elements.Item(n + 1))

    def __iter__(self) -> Iterator[GeometricElement]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'GeometricElements(name="{self.name}")'
