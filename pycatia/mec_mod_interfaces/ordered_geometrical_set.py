#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25

from pycatia.system_interfaces.any_object import AnyObject
import pycatia.mec_mod_interfaces.bodies as bodies
from .hybrid_shapes import HybridShapes
import pycatia.mec_mod_interfaces.ordered_geometrical_sets as ordered_geom_sets
from .sketches import Sketches


class OrderedGeometricalSet(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | The object is an ordered geometrical set.The ordered geometrical set
                | manages a set of hybrid shapes, a set of bodies and a set of ordered
                | geometrical sets.It belongs to theactivateLinkAnchor('OrderedGeometric
                | alSets','','OrderedGeometricalSets')collection of aactivateLinkAnchor(
                | 'Part','','Part')oractivateLinkAnchor('OrderedGeometricalSet','','Orde
                | redGeometricalSet')object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.ordered_geometrical_set = com_object

    @property
    def bodies(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Bodies
                | o Property Bodies() As   (Read Only)
                | 
                | Returns the ordered geometrical set's Bodies collection.
                |
                | Example:
                | The following example returns in bodyColl the collection of bodies of the
                | ordered geometrical set OrderedGeometricalSet1 :
                | Set bodyColl = OrderedGeometricalSet1.Bodies

        :return: Bodies()
        """
        return bodies.Bodies(self.ordered_geometrical_set.Bodies)

    @property
    def hybrid_shapes(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HybridShapes
                | o Property HybridShapes() As   (Read Only)
                | 
                | Returns the list of hybrid shapes included in the ordered geometrical
                | set.  Returns:  oHybridShapes   The list of hybrid shapes in the
                | ordered geometrical set (@see CATIAHybridShapes   for more
                | information).
                |
                | Example:
                | The following example returns in HybridShapes1
                | the list of   hybrid shapes in the ordered geometrical
                | setOrderedGeometricalSet1:
                | Dim HybridShapes1 As HybridShapes
                | Set HybridShapes1 = OrderedGeometricalSet1.HybridShapes

        :return: HybridShapes
        """
        return HybridShapes(self.ordered_geometrical_set.HybridShapes)

    @property
    def ordered_geometrical_sets(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OrderedGeometricalSets
                | o Property OrderedGeometricalSets() As   (Read Only)
                | 
                | Returns the ordered geometrical set's OrderedGeometricalSets
                | collection.
                | Example:
                | The following example returns in
                | OrderedGeometricalSetColl the collection of  ordered geometrical set
                | of the ordered geometrical set OrderedGeometricalSet1 :
                | Set OrderedGeometricalSetColl = OrderedGeometricalSet1.OrderedGeometricalSets

        :return: OrderedGeometricalSets()
        """
        return ordered_geom_sets.OrderedGeometricalSets(self.ordered_geometrical_set.OrderedGeometricalSets)

    @property
    def ordered_sketches(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OrderedSketches
                | o Property OrderedSketches() As   (Read Only)
                | 
                | Returns the ordered geometrical set's Sketches collection. These
                | sketches are those inside the ordered geometrical set at all levels.
                |
                | Example:
                | The following example returns in sketchesCollection the
                | collection of sketches of an ordered geometrical set :
                | Set sketchesCollection = OrderedGeometricalSet1.OrderedSketches

        """
        return Sketches(self.ordered_geometrical_set.OrderedSketches)

    def insert_hybrid_shape(self, i_hybrid_shape):
        """
        .. note::
            CAA V5 Visual Basic help

                | InsertHybridShape
                | o Sub InsertHybridShape(iHybridShape)
                | 
                | Inserts a hybrid shape to the ordered geometrical set.
                |
                | Parameters:
                | iHybridShape
                |   The hybrid shape to insert.
                |
                | Examples:
                | This example inserts the hybrid shape HybridShape1
                | to the ordered geometrical set OrderedGeometricalSet1:
                | OrderedGeometricalSet1.InsertHybridShape (HybridShape1)

        """
        self.ordered_geometrical_set.InsertHybridShape(i_hybrid_shape)

    def __repr__(self):
        return f'OrderedGeometricalSet()'
