#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from .edge import Edge


class TriDimFeatEdge(Edge):
    """
        .. note::
            CAA V5 Visual Basic help

                | 1-D boundary belonging to a feature whose topological result is three
                | dimensional.Role:
                | ThisactivateLinkAnchor('Boundary','','Boundary')object may be, for
                | example, the edge of a Pad.  You will create a TriDimFeatEdge object
                | using theactivateLinkAnchor('Shapes','GetBoundary','Shapes.GetBoundary
                | '),activateLinkAnchor('HybridShapes','GetBoundary','HybridShapes.GetBo
                | undary'),activateLinkAnchor('Sketches','GetBoundary','Sketches.GetBoun
                | dary')oractivateLinkAnchor('Selection','SelectElement2','Selection.Sel
                | ectElement2')method. Then, you pass it to the operator (such asactivat
                | eLinkAnchor('ShapeFactory','AddNewEdgeFilletWithConstantRadius','Shape
                | Factory.AddNewEdgeFilletWithConstantRadius')).  The lifetime of a
                | TriDimFeatEdge object is limited,
                | seeactivateLinkAnchor('Boundary','','Boundary').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tri_dim_feat_edge = com_object

    def __repr__(self):
        return f'TriDimFeatEdge(name="{self.name}")'
