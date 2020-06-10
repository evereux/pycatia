#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:56:40.651039


from .edge import Edge


class BiDimFeatEdge(Edge):
    """
        .. note::
            CAA V5 Visual Basic help

                | 1-D boundary belonging to a feature whose topological result is two
                | dimensional.Role:
                | ThisactivateLinkAnchor('Boundary','','Boundary')object may be, for
                | example, the edge of a surface obtained through the extrusion of a
                | spline.  You will create a BiDimFeatEdge object using theactivateLinkA
                | nchor('Shapes','GetBoundary','Shapes.GetBoundary'),activateLinkAnchor(
                | 'HybridShapes','GetBoundary','HybridShapes.GetBoundary'),activateLinkA
                | nchor('Sketches','GetBoundary','Sketches.GetBoundary')oractivateLinkAn
                | chor('Selection','SelectElement2','Selection.SelectElement2')method.
                | Then, you pass it to the operator (such asactivateLinkAnchor('HybridSh
                | apeFactory','AddNewPointOnCurveFromDistance','HybridShapeFactory.AddNe
                | wPointOnCurveFromDistance')).  The lifetime of a BiDimFeatEdge object
                | is limited, seeactivateLinkAnchor('Boundary','','Boundary').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.bi_dim_feat_edge = com_object

    def __repr__(self):
        return f'BiDimFeatEdge(name="{self.name}")'
