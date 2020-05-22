#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from .vertex import Vertex


class TriDimFeatVertexOrBiDimFeatVertex(Vertex):
    """
        .. note::
            CAA V5 Visual Basic help

                | 0-D boundary belonging to a feature whose topological result is three
                | dimensional or two dimentional.Role:
                | ThisactivateLinkAnchor('Boundary','','Boundary')object may be, for
                | example, the corner of a Pad resulting from the extrusion of a
                | square. You will create a TriDimFeatVertexOrBiDimFeatVertex object
                | using theactivateLinkAnchor('Shapes','GetBoundary','Shapes.GetBoundary
                | '),activateLinkAnchor('HybridShapes','GetBoundary','HybridShapes.GetBo
                | undary'),activateLinkAnchor('Sketches','GetBoundary','Sketches.GetBoun
                | dary')oractivateLinkAnchor('Selection','SelectElement2','Selection.Sel
                | ectElement2')method. Then, you pass it to the operator.  The lifetime
                | of a TriDimFeatVertexOrBiDimFeatVertex object is limited,
                | seeactivateLinkAnchor('Boundary','','Boundary').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tri_dim_feat_vertex_or_bi_dim_feat_vertex = com_object

    def __repr__(self):
        return f'TriDimFeatVertexOrBiDimFeatVertex()'
