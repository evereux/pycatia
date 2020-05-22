#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from .boundary import Boundary


class Vertex(Boundary):
    """
        .. note::
            CAA V5 Visual Basic help

                | 0-D boundary.Role:
                | ThisactivateLinkAnchor('Boundary','','Boundary')object may be, for
                | example, the corner of a Pad resulting from the extrusion of a
                | square. You will create an Vertex object using theactivateLinkAnchor('
                | Shapes','GetBoundary','Shapes.GetBoundary'),activateLinkAnchor('Hybrid
                | Shapes','GetBoundary','HybridShapes.GetBoundary'),activateLinkAnchor('
                | Sketches','GetBoundary','Sketches.GetBoundary')oractivateLinkAnchor('S
                | election','SelectElement2','Selection.SelectElement2')method. Then,
                | you pass it to the operator (such asactivateLinkAnchor('HybridShapeFac
                | tory','AddNewLinePtPt','HybridShapeFactory.AddNewLinePtPt')).  The
                | lifetime of a Vertex object is limited,
                | seeactivateLinkAnchor('Boundary','','Boundary').See also:activateLinkA
                | nchor('TriDimFeatVertexOrBiDimFeatVertex','','TriDimFeatVertexOrBiDimF
                | eatVertex'),activateLinkAnchor('NotWireBoundaryMonoDimFeatVertex','','
                | NotWireBoundaryMonoDimFeatVertex'),activateLinkAnchor('ZeroDimFeatVert
                | exOrWireBoundaryMonoDimFeatVertex','','ZeroDimFeatVertexOrWireBoundary
                | MonoDimFeatVertex').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.vertex = com_object

    def __repr__(self):
        return f'Vertex(name="{self.name}")'
