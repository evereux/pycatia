#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.any_object import AnyObject
from .hybrid_bodies import HybridBodies
from .hybrid_shapes import HybridShapes
from .ordered_geometrical_sets import OrderedGeometricalSets
from .shapes import Shapes
from .sketches import Sketches


class Body(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | The object that manages a sequence of shapes, a set of sketches, a set
                | of hybrid bodies, a set of ordered geometrical sets and a set of
                | hybrid shapes.It belongs to
                | theactivateLinkAnchor('Bodies','','Bodies')collection of aactivateLink
                | Anchor('Part','','Part')oractivateLinkAnchor('HybridBody','','HybridBo
                | dy')object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.body = com_object
        self.com_object = com_object

    @property
    def hybrid_bodies(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HybridBodies
                | o Property HybridBodies() As HybridBodies
                | 
                | Returns the body's HybridBodies collection.  Example:The following
                | example returns in hybridBodyColl the collection of hybrid bodies of
                | the main body of partDoc part document:  Dim body As Body Set body =
                | partDoc.Part.Bodies.MainBody Set hybridBodyColl = body.HybridBodies

        """
        return HybridBodies(self.body.HybridBodies)

    @property
    def hybrid_shapes(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HybridShapes
                | o Property HybridShapes() As HybridShapes
                | 
                | Returns the list of hybrid shapes included in the body.  Returns:
                | oHybridShapes   The list of hybrid shapes in the body (@see
                | CATIAHybridShapes   for more information).
                | Example:
                | The following example returns in HybridShapes1 the list of hybrid
                | shapes in the body Body1:
                | Dim HybridShapes1 As HybridShapes
                | Set HybridShapes1 = Body1.HybridShapes

        :return: HybridShapes()
        """
        return HybridShapes(self.body.HybridShapes)

    @property
    def in_boolean_operation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InBooleanOperation
                | o Property InBooleanOperation() As boolean
                | 
                | Returns True if the body is involved in a boolean operation, else
                | returns False.
                | Example:
                | The following example returns in operated True
                | if the body body1belongs to a  boolean operation.
                | operated = body1.InBooleanOperation

        :return: bool
        """
        return self.body.InBooleanOperation

    @property
    def ordered_geometrical_sets(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OrderedGeometricalSets
                | o Property OrderedGeometricalSets() As OrderedGeometricalSets
                | 
                | Returns the body's OrderedGeometricalSets collection.
                | ometricalSetColl = Body1.OrderedGeometricalSets
                |
                | Example:
                | The following example returns in OrderedGeometricalSetColl the collection
                | of ordered geometrical set of the body Body1 :
                | Set OrderedGe

        """
        return OrderedGeometricalSets(self.body.OrderedGeometricalSets)

    @property
    def shapes(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Shapes
                | o Property Shapes() As Shapes
                | 
                | Returns the body's Shapes collection. These shapes make up the
                | sequence of shapes that will produce an intermediate result for the
                | part, or the final result in the case of the main body.
                |
                | Example:
                | The following example returns in shapColl the collection of shapes managed
                | by the main body of the partDoc part document:
                | Dim body As Body
                | Set body = partDoc.Part.Bodies.MainBody
                | Set shapColl = body.Shapes


        """
        return Shapes(self.body.Shapes)

    @property
    def sketches(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Sketches
                | o Property Sketches() As Sketches
                | 
                | Returns the body's Sketches collection. These sketches are those
                | inside the body at all levels.
                |
                | Example:
                | The following example returns in skColl the collection of sketches of the main body of partDoc part
                | document:
                | Dim body As Body
                | Set body = partDoc.Part.Bodies.MainBody
                | Set skColl = body.Sketches

        """
        return Sketches(self.body.Sketches)

    def insert_hybrid_shape(self, i_hybrid_shape):
        """
        .. note::
            CAA V5 Visual Basic help

                | InsertHybridShape
                | o Sub InsertHybridShape(    HybridShape    iHybridShape)
                | 
                | Insert a hybrid shape to the body.
                |
                | Parameters:
                | iHybriShape
                |   The hybrid shape to insert.
                |
                | Examples:
                | 
                | This example inserts the hybrid shape HybridShape1
                | to the body Body1:
                | 
                | Body1.InsertHybridShape (HybridShape1)

        """
        self.body.InsertHybridShape(i_hybrid_shape)

    def __repr__(self):
        return f'Body(name="{self.name}")'
