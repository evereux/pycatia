#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.exception_handling.exceptions import CATIAApplicationException
from pycatia.system_interfaces.collection import Collection
from .boundary import Boundary
from .hybrid_shape import HybridShape


class HybridShapes(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | The collection of the HybridShapes making up a body.

    """

    def __init__(self, collection_com_object):
        super().__init__(collection_com_object, child_object=HybridShape)
        self.hybrid_shapes = collection_com_object

    def get_boundary(self, i_label):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetBoundary
                | o Func GetBoundary(    CATBSTR    iLabel) As Boundary
                | 
                | Returns a boundary using its label.


                | Parameters:
                | iLabel
                |    Identification of the 
                | 
                |  activateLinkAnchor('Boundary','','Boundary')  object.   See 
                |  activateLinkAnchor('Reference','DisplayName','Reference.DisplayName') . 
                |    Returns:
                |   The retrieved boundary


        """
        return Boundary(self.hybrid_shapes.GetBoundary(i_label))

    def item(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(    CATVariant    iIndex) As HybridShape
                | 
                | Returns a HybridShape using its index or its name from the
                | HybridShapes collection.


                | Parameters:
                | iIndex
                |    The index or the name of the HybridShape to retrieve from
                |    the collection of HybridShapes.
                |    As a numeric, this index is the rank of the HybridShape
                |    in the collection.
                |    The index of the first HybridShape in the collection is 1, and
                |    the index of the last HybridShape is 
                | 
                |  activateLinkAnchor('Collection','Count','Collection.Count') .   As a
                | string, it is the name you assigned to the HybridShape using
                |    the 
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property. 
                |    Returns:
                |   The retrieved HybridShape


                | Examples:
                | 
                | 
                | This example retrieves in ThisHybridShape the third HybridShape,
                | and in ThatHybridShape the HybridShape named
                | MyHybridShape in the HybridShape collection of the active document,
                | supposed to be a part document.
                | 
                | Set ThisHybridShape = CATIA.ActiveDocument.HybridShapes.Item(3)
                | Set ThatHybridShape = CATIA.ActiveDocument.HybridShapes.Item("MyHybridShape")
                | 
                | 
                | 
        """
        try:
            return self.child_object(self.hybrid_shapes.Item(i_index))
        except CATIAApplicationException:
            raise CATIAApplicationException('Could not find item.')

    def __repr__(self):
        return f'HybridShapes(name="{self.name}")'
