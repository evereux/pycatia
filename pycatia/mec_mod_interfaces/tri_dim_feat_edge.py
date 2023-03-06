#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.edge import Edge


class TriDimFeatEdge(Edge):
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
                |                                 TriDimFeatEdge
                | 
                | 1-D boundary belonging to a feature whose topological result is three
                | dimensional.
                | Role: This Boundary object may be, for example, the edge of a
                | Pad.
                | You will create a TriDimFeatEdge object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | ShapeFactory.AddNewEdgeFilletWithConstantRadius ).
                | The lifetime of a TriDimFeatEdge object is limited, see
                | Boundary.
                | 
                | Example:
                |     This example asks the end user to select an edge, and creates an edge
                |     fillet on this edge:
                | 
                |      Dim InputObjectType(0)
                |      Set Document = CATIA.ActiveDocument
                |      Set Selection = Document.Selection
                |      'We propose to the user that he select an edge
                |      InputObjectType(0)="TriDimFeatEdge"
                |      Status=Selection.SelectElement2(InputObjectType,"Select an
                |      edge",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set EdgeFillet = ShapeFactory.AddNewEdgeFilletWithConstantRadius(Selection.Item(1).Value,1,5.0)
                |      EdgeFillet.EdgePropagation = 1
                |      Document.Part.Update 

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tri_dim_feat_edge = com_object

    def __repr__(self):
        return f'TriDimFeatEdge(name="{self.name}")'
