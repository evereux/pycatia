#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.boundary import Boundary
from pycatia.sketcher_interfaces.sketch import Sketch
from pycatia.system_interfaces.collection import Collection


class Sketches(Collection):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Sketches
                | 
                | The body's collection of sketches not yet used by any shape.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sketches = com_object

    def add(self, i_plane: Reference) -> Sketch:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add(Reference iPlane) As Sketch
                | 
                |     Creates a new sketch and adds it to the sketch collection. The sketch
                |     creation implies to specify a supporting plane. Once created, the sketch
                |     exists, but is empty. You must use the Sketch.OpenEdition method to begin to
                |     edit it.
                | 
                |     Parameters:
                | 
                |         iPlane
                |             The sketch supporting plane
                |             The following 
                | 
                |         Boundary object is supported: PlanarFace. 
                |     Returns:
                |         oNewSketch The created sketch 
                |     Example:
                |         This example creates the newSketch sketch on the XY plane of the myPart
                |         part:
                | 
                |          Set XYPlane = myPart.OriginElements.PlaneXY()
                |          Set newSketch = myPart.Sketches.Add(XYPlane)

        :param Reference i_plane:
        :return: Sketch
        :rtype: Sketch
        """
        return Sketch(self.sketches.Add(i_plane.com_object))

    def get_boundary(self, i_label: str) -> Boundary:
        """
        .. note::
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
        :return: Boundary
        :rtype: Boundary
        """
        return Boundary(self.sketches.GetBoundary(i_label))

    def item(self, i_index: CATVariant) -> Sketch:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As Sketch
                | 
                |     Returns a sketch using its index or its name from the Sketches
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the sketch to retrieve from the collection
                |             of sketches. As a numerics, this index is the rank of the sketch in the
                |             collection. The index of the first sketch in the collection is 1, and the index
                |             of the last sketch is Count. As a string, it is the name you assigned to the
                |             sketch using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved sketch 
                |     Example:
                |         This example retrieves the last item in the collection
                |         sketches.
                | 
                |          Set lastSketch = sketchList.Item(sketchList.Count)

        :param CATVariant i_index:
        :return: Sketch
        :rtype: Sketch
        """
        return Sketch(self.sketches.Item(i_index.com_object))

    def __repr__(self):
        return f'Sketches(name="{self.name}")'
