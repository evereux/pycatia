#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from .vertex import Vertex


class ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex(Vertex):
    """
        .. note::
            CAA V5 Visual Basic help

                | 0-D boundary beeing either an isolated point or the extremity of a
                | feature whose topological result is one dimensional.Role:
                | ThisactivateLinkAnchor('Boundary','','Boundary')object may be, for
                | example, the extremity of a line segment.  You will create a
                | ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex object using theactiv
                | ateLinkAnchor('Shapes','GetBoundary','Shapes.GetBoundary'),activateLin
                | kAnchor('HybridShapes','GetBoundary','HybridShapes.GetBoundary'),activ
                | ateLinkAnchor('Sketches','GetBoundary','Sketches.GetBoundary')oractiva
                | teLinkAnchor('Selection','SelectElement2','Selection.SelectElement2')m
                | ethod.  Then, you pass it to the operator.  The lifetime of a
                | ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex object is limited,
                | seeactivateLinkAnchor('Boundary','','Boundary').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.zero_dim_feat_vertex_or_wire_boundary_mono_dim_feat_vertex = com_object

    def __repr__(self):
        return f'ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex()'
