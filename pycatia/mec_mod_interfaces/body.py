#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.hybrid_bodies import HybridBodies
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape
from pycatia.mec_mod_interfaces.hybrid_shapes import HybridShapes
from pycatia.mec_mod_interfaces.ordered_geometrical_sets import OrderedGeometricalSets
from pycatia.mec_mod_interfaces.shapes import Shapes
from pycatia.mec_mod_interfaces.sketches import Sketches
from pycatia.system_interfaces.any_object import AnyObject


class Body(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Body
                | 
                | The object that manages a sequence of shapes, a set of sketches, a set of
                | hybrid bodies, a set of ordered geometrical sets and a set of hybrid
                | shapes.
                | 
                | It belongs to the Bodies collection of a Part or HybridBody
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.body = com_object

    @property
    def hybrid_bodies(self) -> HybridBodies:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HybridBodies() As HybridBodies (Read Only)
                | 
                |     Returns the body's HybridBodies collection.
                | 
                |     Example:
                |         The following example returns in hybridBodyColl the collection of
                |         hybrid bodies of the main body of partDoc part
                |         document:
                | 
                |          Dim body As Body
                |          Set body = partDoc.Part.Bodies.MainBody
                |          Set hybridBodyColl = body.HybridBodies

        :rtype: HybridBodies
        """

        return HybridBodies(self.body.HybridBodies)

    @property
    def hybrid_shapes(self) -> HybridShapes:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HybridShapes() As HybridShapes (Read Only)
                | 
                |     Returns the list of hybrid shapes included in the body.
                | 
                |     Returns:
                |         oHybridShapes The list of hybrid shapes in the body (@see
                |         CATIAHybridShapes
                |         for more information).
                | 
                |         Example:
                |             The following example returns in HybridShapes1 the list
                |             of
                |             hybrid shapes in the body Body1:
                | 
                |              Dim HybridShapes1 As HybridShapes
                |              Set HybridShapes1 = Body1.HybridShapes

        :rtype: HybridShapes
        """

        return HybridShapes(self.body.HybridShapes)

    @property
    def in_boolean_operation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InBooleanOperation() As boolean (Read Only)
                | 
                |     Returns True if the body is involved in a boolean operation, else returns
                |     False.
                | 
                |     Example:
                |         The following example returns in operated True if the body body1belongs
                |         to a boolean operation.
                | 
                |          operated = body1.InBooleanOperation

        :rtype: bool
        """

        return self.body.InBooleanOperation

    @property
    def ordered_geometrical_sets(self) -> OrderedGeometricalSets:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OrderedGeometricalSets() As OrderedGeometricalSets (Read
                | Only)
                | 
                |     Returns the body's OrderedGeometricalSets collection.
                | 
                |     ometricalSetColl = Body1.OrderedGeometricalSets Example:
                |         The following example returns in OrderedGeometricalSetColl the
                |         collection of ordered geometrical set of the body Body1
                |         :
                | 
                |          Set OrderedGe

        :rtype: OrderedGeometricalSets
        """

        return OrderedGeometricalSets(self.body.OrderedGeometricalSets)

    @property
    def shapes(self) -> Shapes:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Shapes() As Shapes (Read Only)
                | 
                |     Returns the body's Shapes collection. These shapes make up the sequence of
                |     shapes that will produce an intermediate result for the part, or the final
                |     result in the case of the main body.
                | 
                |     Example:
                |         The following example returns in shapColl the collection of shapes
                |         managed by the main body of the partDoc part document:
                | 
                |          Dim body As Body
                |          Set body = partDoc.Part.Bodies.MainBody
                |          Set shapColl = body.Shapes

        :rtype: Shapes
        """

        return Shapes(self.body.Shapes)

    @property
    def sketches(self) -> Sketches:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Sketches() As Sketches (Read Only)
                | 
                |     Returns the body's Sketches collection. These sketches are those inside the
                |     body at all levels.
                | 
                |     Example:
                |         The following example returns in skColl the collection of sketches of
                |         the main body of partDoc part document:
                | 
                |          Dim body As Body
                |          Set body = partDoc.Part.Bodies.MainBody
                |          Set skColl = body.Sketches

        :rtype: Sketches
        """

        return Sketches(self.body.Sketches)

    def insert_hybrid_shape(self, i_hybrid_shape: HybridShape) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InsertHybridShape(HybridShape iHybridShape)
                | 
                |     Insert a hybrid shape to the body.
                | 
                |     Parameters:
                | 
                |         iHybriShape
                |             The hybrid shape to insert. 
                | 
                |     Example:
                |         This example inserts the hybrid shape HybridShape1 to the body
                |         Body1:
                | 
                |          Body1.InsertHybridShape (HybridShape1)

        :param HybridShape i_hybrid_shape:
        :rtype: None
        """
        return self.body.InsertHybridShape(i_hybrid_shape.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'insert_hybrid_shape'
        # # vba_code = """
        # # Public Function insert_hybrid_shape(body)
        # #     Dim iHybridShape (2)
        # #     body.InsertHybridShape iHybridShape
        # #     insert_hybrid_shape = iHybridShape
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Body(name="{self.name}")'
