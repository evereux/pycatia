#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.collection import Collection


class GeometricElements(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | A collection of all geometric elements contained in a part or a
                | sketch.Geometric elements are created with the 2D factory for the
                | sketch and with the 3D factory for the part. Geometric elements thus
                | created are then aggregated either in the sketch or as part of the
                | geometric element collection.

    """

    def __init__(self, collection_com_object):
        super().__init__(collection_com_object)
        self.geometric_elements = collection_com_object

    def item(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(    CATVariant    iIndex) As GeometricElement
                | 
                | Returns a geometric element using its index or its name from the
                | GeometricElements collection.


                | Parameters:
                | iIndex
                |    The index or the name of the geometric element to retrieve from
                |    the collection of geometric elements.
                |    As a numeric, this index is the rank of the geometric element
                |    in the collection.
                |    The index of the first geometric element in the collection is 1, and
                |    the index of the last geometric element is Count.
                |    As a string, it is the name you assigned to the geometric element using
                |    the 
                | 
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property. 
                |    Returns:
                |   The retrieved geometric element


                | Examples:
                | 
                | 
                | This example retrieves the last item in the geometric element collection.
                | 
                | Set lastCst = cstList.Item(cstList.Count)

            see sketcher_interfaces.enumeration_types.geometric_type
            :return: int
        """
        return self.geometric_elements.Item(i_index)

    def __repr__(self):
        return f'GeometricElements()'
