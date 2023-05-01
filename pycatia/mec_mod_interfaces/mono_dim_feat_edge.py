#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.edge import Edge


class MonoDimFeatEdge(Edge):
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
                |                             MecModInterfaces.Edge
                |                                 MonoDimFeatEdge
                | 
                | 1-D boundary belonging to a feature whose topological result is one
                | dimensional.
                | Role: This Boundary object may be, for example, in a part containing a Sketch
                | which is made up of a circle arc and a spline, the circle arc.
                | You will create a MonoDimFeatEdge object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | HybridShapeFactory.AddNewPointTangent ).
                | The lifetime of a MonoDimFeatEdge object is limited, see
                | Boundary.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mono_dim_feat_edge = com_object

    def __repr__(self):
        return f'MonoDimFeatEdge(name="{self.name}")'
