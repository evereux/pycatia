#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.vertex import Vertex


class ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex(Vertex):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Reference
                |                         MecModInterfaces.Boundary
                |                             MecModInterfaces.Vertex
                |                                ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex
                | 
                | 0-D boundary being either an isolated point or the extremity of a feature
                | whose topological result is one dimensional.
                | Role: This Boundary object may be, for example, the extremity of a line
                | segment.
                | You will create a ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex object using
                | the Shapes.GetBoundary , HybridShapes.GetBoundary , Sketches.GetBoundary or
                | Selection.SelectElement2 method. Then, you pass it to the
                | operator.
                | The lifetime of a ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex object is
                | limited, see Boundary.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.zero_dim_feat_vertex_or_wire_boundary_mono_dim_feat_vertex = com_object

    def __repr__(self):
        return f'ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex(name="{self.name}")'
