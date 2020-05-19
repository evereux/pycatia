#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.collection import Collection
from pycatia.sketcher_interfaces.sketch import Sketch
from .boundary import Boundary


class Sketches(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | The body's collection of sketches not yet used by any shape.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sketches = com_object

    def add(self, i_plane):
        """
        .. note::
            CAA V5 Visual Basic help

                | Add
                | o Func Add(    Reference    iPlane) As Sketch
                | 
                | Creates a new sketch and adds it to the sketch collection. The sketch
                | creation implies to specify a supporting plane. Once created, the
                | sketch exists, but is empty. You must use the
                | activateLinkAnchor('Sketch','OpenEdition','Sketch.OpenEdition')
                | method to begin to edit it.
                |
                | Parameters:
                | iPlane
                |    The sketch supporting plane
                |  The following 
                | 
                |  activateLinkAnchor('Boundary','','Boundary')  object is supported:  
                |  activateLinkAnchor('PlanarFace','','PlanarFace') . 
                |    Returns:
                |   oNewSketch   The created sketch
                |
                | Examples:
                | This example creates the newSketch sketch on the XY plane
                | of the myPart part:
                | Set XYPlane = myPart.OriginElements.PlaneXY()
                | Set newSketch = myPart.Sketches.Add(XYPlane)

        :return Sketch()
        """
        return Sketch(self.sketches.Add(i_plane))

    def get_boundary(self, i_label):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetBoundary
                | o Func GetBoundary(    CATBSTR    iLabel) As Boundary
                | 
                | Returns a boundary using its label.
                |
                | Parameters:
                | iLabel
                |    Identification of the 
                | 
                |  activateLinkAnchor('Boundary','','Boundary')  object.   See 
                |  activateLinkAnchor('Reference','DisplayName','Reference.DisplayName') . 
                |    Returns:
                |   The retrieved boundary


        """
        return Boundary(self.sketches.GetBoundary(i_label))

    def item(self, i_index):
        """

        .. warning::

            The index when not a string must be it's python index (indexes in python start from 0).
            collection. The COM interface index starts at 1.

        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(    CATVariant    iIndex) As Sketch
                | 
                | Returns a sketch using its index or its name from the Sketches
                | collection.
                |
                | Parameters:
                | iIndex
                |    The index or the name of the sketch to retrieve from
                |    the collection of sketches.
                |    As a numerics, this index is the rank of the sketch
                |    in the collection.
                |    The index of the first sketch in the collection is 1, and
                |    the index of the last sketch is Count.
                |    As a string, it is the name you assigned to the sketch using
                |    the 
                | 
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property. 
                |    Returns:
                |   The retrieved sketch
                |
                | Examples:
                | This example retrieves the last item in the collection sketches.
                | Set lastSketch = sketchList.Item(sketchList.Count)

        :return: Sketch()
        """
        if isinstance(i_index, int):
            i_index += 1

        return Sketch(self.sketches.Item(i_index))

    def __repr__(self):
        return f'Sketches()'
