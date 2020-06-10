#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from .edge import Edge


class MonoDimFeatEdge(Edge):
    """
        .. note::
            CAA V5 Visual Basic help

                | 1-D boundary belonging to a feature whose topological result is one
                | dimensional.Role:
                | ThisactivateLinkAnchor('Boundary','','Boundary')object may be, for
                | example, in a part containing a Sketch which is made up of a circle
                | arc and a spline, the circle arc.  You will create a MonoDimFeatEdge
                | object using theactivateLinkAnchor('Shapes','GetBoundary','Shapes.GetB
                | oundary'),activateLinkAnchor('HybridShapes','GetBoundary','HybridShape
                | s.GetBoundary'),activateLinkAnchor('Sketches','GetBoundary','Sketches.
                | GetBoundary')oractivateLinkAnchor('Selection','SelectElement2','Select
                | ion.SelectElement2')method. Then, you pass it to the operator (such as
                | activateLinkAnchor('HybridShapeFactory','AddNewPointTangent','HybridSh
                | apeFactory.AddNewPointTangent')).  The lifetime of a MonoDimFeatEdge
                | object is limited, seeactivateLinkAnchor('Boundary','','Boundary').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mono_dim_feat_edge = com_object

    def __repr__(self):
        return f'MonoDimFeatEdge(name="{self.name}")'
