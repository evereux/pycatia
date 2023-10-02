#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.boundary import Boundary


class Vertex(Boundary):
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
                |                             Vertex
                | 
                | 0-D boundary.
                | Role: This Boundary object may be, for example, the corner of a Pad resulting
                | from the extrusion of a square.
                | You will create an Vertex object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | HybridShapeFactory.AddNewLinePtPt ).
                | The lifetime of a Vertex object is limited, see Boundary.
                | See also:
                | TriDimFeatVertexOrBiDimFeatVertex , NotWireBoundaryMonoDimFeatVertex ,
                | ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex .
                | 
                | Example:
                |     This example asks the end user to select successively two vertices. Then,
                |     it creates a line between these two vertices.
                | 
                |      Dim InputObjectType(0)
                |      Set Document = CATIA.ActiveDocument
                |      Set Selection = Document.Selection
                |      Set HybridBodies = Document.Part.HybridBodies
                |      Set HybridBody = HybridBodies.Item("Geometrical Set.1")
                |      'We propose to the user that he select the first vertex
                |      InputObjectType(0)="Vertex"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the first
                |      vertex",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set FirstVertex = Selection.Item(1).Value
                |      Selection.Clear
                |      'We propose to the user that he select the second vertex
                |      InputObjectType(0)="Vertex"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the second
                |      vertex",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set SecondVertex = Selection.Item(1).Value
                |      Set hybridShapeLinePtPt = HybridShapeFactory.AddNewLinePtPt(FirstVertex,SecondVertex)
                |      HybridBody.AppendHybridShape hybridShapeLinePtPt
                |      Document.Part.InWorkObject = hybridShapeLinePtPt
                |      Document.Part.Update 

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.vertex = com_object

    def __repr__(self):
        return f'Vertex(name="{self.name}")'
