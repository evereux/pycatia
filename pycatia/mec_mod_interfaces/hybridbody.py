#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.base_object import AnyObject
import pycatia.mec_mod_interfaces.bodies as bodies
from .geometricelements import GeometricElements
import pycatia.mec_mod_interfaces.hybridbodies as hybridbodies
from .hybridshapes import HybridShapes
from .sketches import Sketches


class HybridBody(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | The object is a hybrid body.The hybrid body manages a set of geometric
                | elements, a set of hybrid shapes, a set of bodies and a set of hybrid
                | bodies.It belongs to
                | theactivateLinkAnchor('HybridBodies','','HybridBodies')collection of
                | aactivateLinkAnchor('Part','','Part')or @ref CATIABody
                | oractivateLinkAnchor('HybridBody','','HybridBody')object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybridbody = com_object

    @property
    def bodies(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Bodies
                | o Property Bodies(    ) As Bodies
                | 
                | Returns the hybrid body's Bodies collection.  Example:The following
                | example returns in bodyColl the collection of bodies of the hybrid
                | body hybridBody :  Set bodyColl = hybridBody.Bodies

        :return: Body()
        """
        return bodies.Bodies(self.hybridbody.Bodies)

    @property
    def geometric_elements(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GeometricElements
                | o Property GeometricElements(    ) As GeometricElements
                | 
                | Returns the list of geometrical elements included in the hybrid body.
                | Returns:  oGeometricElements   The list of geometric elements in the
                | hybrid body (@see CATIAGeometricElements   for more information).
                |
                | Example:
                | The following example returns in geometricElements the list of
                | geometrical elements in the Hybrid body hybridBody:
                | Dim geometricElements As GeometricElements
                | Set geometricElements = hybridBody.GeometricElements

        :return: GeometricElements()
        """
        return GeometricElements(self.hybridbody.GeometricElements)

    @property
    def hybrid_bodies(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HybridBodies
                | o Property HybridBodies(    ) As HybridBodies
                | 
                | Returns the hybrid body's HybridBodies collection.
                |
                | Example:
                | The following example returns in hybridBodyColl the collection of hybrid
                | bodies of the hybrid body hybridBody :
                | Set hybridBodyColl = hybridBody.HybridBodies

        :return: HybridBodies()
        """
        return hybridbodies.HybridBodies(self.hybridbody.HybridBodies)

    @property
    def hybrid_shapes(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HybridShapes
                | o Property HybridShapes(    ) As HybridShapes
                | 
                | Returns the list of hybrid shapes included in the hybrid body.
                | Returns:  oHybridShapes   The list of hybrid shapes in the hybrid body
                | (@see CATIAHybridShapes   for more information).
                |
                | Example:
                | The following example returns in hybridShapes the list of hybrid shapes in the
                | hybrid body hybridBody:
                | Dim hybridShapes As HybridShapes
                | Set hybridShapes = hybridBody.HybridShapes

        :return: HybridShapes()
        """
        return HybridShapes(self.hybridbody.HybridShapes)

    @property
    def hybrid_sketches(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HybridSketches
                | o Property HybridSketches(    ) As Sketches
                | 
                | Returns the hybrid body's Sketches collection. These sketches are
                | those inside the hybrid body at all levels.  Example:The following
                | example returns in skColl the collection of sketches of a hybrid body
                | :  Set skColl = hybridBody.HybridSketches

        :return: Sketches()
        """
        return Sketches(self.hybridbody.HybridSketches)

    def append_hybrid_shape(self, i_hybrid_shape):
        """
        .. note::
            CAA V5 Visual Basic help

                | AppendHybridShape
                | o Sub AppendHybridShape(    HybridShape    iHybridShape)
                | 
                | Appends a hybrid shape to the hybrid body.
                |
                | Parameters:
                | iHybriShape
                |   The hybrid shape to append.
                |
                | Examples:
                |
                | This example appends the hybrid shape hybridShape
                | to the hybrid body hybridBody:
                | 
                | hybridBody.AppendHybridShape (hybridShape)
        """
        self.hybridbody.AppendHybridShape(i_hybrid_shape)

    def __repr__(self):
        return f'HybridBody(name="{self.name}")'
