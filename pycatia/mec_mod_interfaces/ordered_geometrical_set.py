#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import TYPE_CHECKING

from pycatia.mec_mod_interfaces.hybrid_shapes import HybridShapes
from pycatia.mec_mod_interfaces.sketches import Sketches
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.mec_mod_interfaces.bodies import Bodies
    from pycatia.mec_mod_interfaces.ordered_geometrical_sets import OrderedGeometricalSets
    from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class OrderedGeometricalSet(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OrderedGeometricalSet
                | 
                | The object is an ordered geometrical set.
                | The ordered geometrical set manages a set of hybrid shapes, a set of bodies and
                | a set of ordered geometrical sets.
                | It belongs to the OrderedGeometricalSets collection of a Part or
                | OrderedGeometricalSet object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.ordered_geometrical_set = com_object

    @property
    def bodies(self) -> 'Bodies':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Bodies() As Bodies (Read Only)
                | 
                |     Returns the ordered geometrical set's Bodies collection.
                | 
                |     Example:
                |         The following example returns in bodyColl the collection of bodies of
                |         the ordered geometrical set OrderedGeometricalSet1 :
                | 
                |          Set bodyColl = OrderedGeometricalSet1.Bodies

        :rtype: Bodies
        """
        from pycatia.mec_mod_interfaces.bodies import Bodies
        return Bodies(self.ordered_geometrical_set.Bodies)

    @property
    def hybrid_shapes(self) -> HybridShapes:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property HybridShapes() As HybridShapes (Read Only)
                | 
                |     Returns the list of hybrid shapes included in the ordered geometrical
                |     set.
                | 
                |     Returns:
                |         oHybridShapes The list of hybrid shapes in the ordered geometrical set
                |         (@see CATIAHybridShapes
                |         for more information).
                | 
                |         Example:
                |             The following example returns in HybridShapes1 the list
                |             of
                |             hybrid shapes in the ordered geometrical
                |             setOrderedGeometricalSet1:
                | 
                |              Dim HybridShapes1 As HybridShapes
                |              Set HybridShapes1 = OrderedGeometricalSet1.HybridShapes

        :rtype: HybridShapes
        """

        return HybridShapes(self.ordered_geometrical_set.HybridShapes)

    @property
    def ordered_geometrical_sets(self) -> 'OrderedGeometricalSets':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OrderedGeometricalSets() As OrderedGeometricalSets (Read
                | Only)
                | 
                |     Returns the ordered geometrical set's OrderedGeometricalSets
                |     collection.
                | 
                |     Example:
                |         The following example returns in OrderedGeometricalSetColl the
                |         collection of ordered geometrical set of the ordered geometrical set
                |         OrderedGeometricalSet1 :
                | 
                |          Set OrderedGeometricalSetColl = OrderedGeometricalSet1.OrderedGeometricalSets

        :rtype: OrderedGeometricalSets
        """
        from pycatia.mec_mod_interfaces.ordered_geometrical_sets import OrderedGeometricalSets
        return OrderedGeometricalSets(self.ordered_geometrical_set.OrderedGeometricalSets)

    @property
    def ordered_sketches(self) -> Sketches:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property OrderedSketches() As Sketches (Read Only)
                | 
                |     Returns the ordered geometrical set's Sketches collection. These sketches
                |     are those inside the ordered geometrical set at all
                |     levels.
                | 
                |     Example:
                |         The following example returns in sketchesCollection the collection of
                |         sketches of an ordered geometrical set :
                | 
                |          Set sketchesCollection = OrderedGeometricalSet1.OrderedSketches

        :rtype: Sketches
        """

        return Sketches(self.ordered_geometrical_set.OrderedSketches)

    def insert_hybrid_shape(self, i_hybrid_shape: 'HybridShape') -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InsertHybridShape(HybridShape iHybridShape)
                | 
                |     Inserts a hybrid shape to the ordered geometrical set.
                | 
                |     Parameters:
                | 
                |         iHybridShape
                |             The hybrid shape to insert. 
                | 
                |     Example:
                |         This example inserts the hybrid shape HybridShape1 to the ordered
                |         geometrical set OrderedGeometricalSet1:
                | 
                |          OrderedGeometricalSet1.InsertHybridShape
                |          (HybridShape1)

        :param HybridShape i_hybrid_shape:
        :rtype: None
        """
        return self.ordered_geometrical_set.InsertHybridShape(i_hybrid_shape.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'insert_hybrid_shape'
        # # vba_code = """
        # # Public Function insert_hybrid_shape(ordered_geometrical_set)
        # #     Dim iHybridShape (2)
        # #     ordered_geometrical_set.InsertHybridShape iHybridShape
        # #     insert_hybrid_shape = iHybridShape
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'OrderedGeometricalSet(name="{self.name}")'
