#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import TYPE_CHECKING

from pycatia.mec_mod_interfaces.geometric_elements import GeometricElements
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape
from pycatia.mec_mod_interfaces.hybrid_shapes import HybridShapes
from pycatia.mec_mod_interfaces.sketches import Sketches
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.mec_mod_interfaces.bodies import Bodies
    from pycatia.mec_mod_interfaces.hybrid_bodies import HybridBodies


class HybridBody(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     HybridBody
                | 
                | The object is a hybrid body.
                | The hybrid body manages a set of geometric elements, a set of hybrid shapes, a
                | set of bodies and a set of hybrid bodies.
                | It belongs to the HybridBodies collection of a Part or @ref CATIABody or
                | HybridBody object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_body = com_object

    @property
    def bodies(self) -> 'Bodies':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Bodies() As Bodies (Read Only)
                | 
                |     Returns the hybrid body's Bodies collection.
                | 
                |     Example:
                |         The following example returns in bodyColl the collection of bodies of
                |         the hybrid body hybridBody :
                | 
                |          Set bodyColl = hybridBody.Bodies

        :return: Bodies
        :rtype: Bodies
        """
        from pycatia.mec_mod_interfaces.bodies import Bodies
        return Bodies(self.hybrid_body.Bodies)

    @property
    def geometric_elements(self) -> GeometricElements:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GeometricElements() As GeometricElements (Read
                | Only)
                | 
                |     Returns the list of geometrical elements included in the hybrid
                |     body.
                | 
                |     Returns:
                |         oGeometricElements The list of geometric elements in the hybrid body
                |         (@see CATIAGeometricElements
                |         for more information).
                | 
                |         Example:
                |             The following example returns in geometricElements the list
                |             of
                |             geometrical elements in the Hybrid body
                |             hybridBody:
                | 
                |              Dim geometricElements As GeometricElements
                |              Set geometricElements = hybridBody.GeometricElements

        :return: GeometricElements
        :rtype: GeometricElements
        """

        return GeometricElements(self.hybrid_body.GeometricElements)

    @property
    def hybrid_bodies(self) -> 'HybridBodies':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HybridBodies() As HybridBodies (Read Only)
                | 
                |     Returns the hybrid body's HybridBodies collection.
                | 
                |     Example:
                |         The following example returns in hybridBodyColl the collection of
                |         hybrid bodies of the hybrid body hybridBody :
                | 
                |          Set hybridBodyColl = hybridBody.HybridBodies

        :return: HybridBodies
        :rtype: HybridBodies
        """
        from pycatia.mec_mod_interfaces.hybrid_bodies import HybridBodies
        return HybridBodies(self.hybrid_body.HybridBodies)

    @property
    def hybrid_shapes(self) -> HybridShapes:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HybridShapes() As HybridShapes (Read Only)
                | 
                |     Returns the list of hybrid shapes included in the hybrid
                |     body.
                | 
                |     Returns:
                |         oHybridShapes The list of hybrid shapes in the hybrid body (@see
                |         CATIAHybridShapes
                |         for more information).
                | 
                |         Example:
                |             The following example returns in hybridShapes the list
                |             of
                |             hybrid shapes in the hybrid body hybridBody:
                | 
                |              Dim hybridShapes As HybridShapes
                |              Set hybridShapes = hybridBody.HybridShapes

        :return: HybridShapes
        :rtype: HybridShapes
        """

        return HybridShapes(self.hybrid_body.HybridShapes)

    @property
    def hybrid_sketches(self) -> Sketches:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HybridSketches() As Sketches (Read Only)
                | 
                |     Returns the hybrid body's Sketches collection. These sketches are those
                |     inside the hybrid body at all levels.
                | 
                |     Example:
                |         The following example returns in skColl the collection of sketches of a
                |         hybrid body :
                | 
                |          Set skColl = hybridBody.HybridSketches

        :return: Sketches
        :rtype: Sketches
        """

        return Sketches(self.hybrid_body.HybridSketches)

    def append_hybrid_shape(self, i_hybrid_shape: HybridShape) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AppendHybridShape(HybridShape iHybridShape)
                | 
                |     Appends a hybrid shape to the hybrid body.
                | 
                |     Parameters:
                | 
                |         iHybriShape
                |             The hybrid shape to append. 
                | 
                |     Example:
                |         This example appends the hybrid shape hybridShape to the hybrid body
                |         hybridBody:
                | 
                |          hybridBody.AppendHybridShape (hybridShape)

        :param HybridShape i_hybrid_shape:
        :return: None
        :rtype: None
        """
        return self.hybrid_body.AppendHybridShape(i_hybrid_shape.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'append_hybrid_shape'
        # # vba_code = """
        # # Public Function append_hybrid_shape(hybrid_body)
        # #     Dim iHybridShape (2)
        # #     hybrid_body.AppendHybridShape iHybridShape
        # #     append_hybrid_shape = iHybridShape
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def append_hybrid_shapes(self, shapes: list) -> None:
        """
        :param list(HybridShape) shapes:
        :return:
        """
        for shape in shapes:
            self.append_hybrid_shape(shape)

    def __repr__(self):
        return f'HybridBody(name="{self.name}")'
