#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.edge import Edge


class BiDimFeatEdge(Edge):
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
                |                                 BiDimFeatEdge
                | 
                | 1-D boundary belonging to a feature whose topological result is two
                | dimensional.
                | Role: This Boundary object may be, for example, the edge of a surface obtained
                | through the extrusion of a spline.
                | You will create a BiDimFeatEdge object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | HybridShapeFactory.AddNewPointOnCurveFromDistance ).
                | The lifetime of a BiDimFeatEdge object is limited, see
                | Boundary.
                | 
                | Example:
                |     This example asks the end user to select an edge, and creates a point on
                |     this edge. Here, both TriDimFeatEdge and BiDimFeatEdge objects are proposed to
                |     the user.
                | 
                |      Dim InputObjectType(1)
                |      Set Document = CATIA.ActiveDocument
                |      Set Selection = Document.Selection
                |      Set HybridBodies = Document.Part.HybridBodies
                |      Set HybridBody = HybridBodies.Item("Geometrical Set.1")
                |      'We propose to the user that he select an edge
                |      InputObjectType(0)="TriDimFeatEdge"
                |      InputObjectType(1)="BiDimFeatEdge"
                |      Status=Selection.SelectElement2(InputObjectType,"Select an
                |      edge",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set Curve = Selection.Item(1).Value
                |      Set HybridShapePointOnCurve = HybridShapeFactory.AddNewPointOnCurveFromDistance(Curve,18.0,False)
                |      HybridBody.AppendHybridShape HybridShapePointOnCurve
                |      Document.Part.InWorkObject = HybridShapePointOnCurve
                |      Document.Part.Update 

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.bi_dim_feat_edge = com_object

    def __repr__(self):
        return f'BiDimFeatEdge(name="{self.name}")'
