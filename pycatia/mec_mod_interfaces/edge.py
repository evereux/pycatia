#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from pycatia.mec_mod_interfaces.boundary import Boundary


class Edge(Boundary):
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
                |                             Edge
                |
                | 1-D boundary.
                | Role: This Boundary object may be, for example, the edge of a
                | cylinder.
                | You will create an Edge object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | HybridShapeFactory.AddNewPointTangent ).
                | The lifetime of an Edge object is limited, see Boundary.
                | See also:
                | TriDimFeatEdge , RectilinearTriDimFeatEdge , BiDimFeatEdge ,
                | RectilinearBiDimFeatEdge , MonoDimFeatEdge , RectilinearMonoDimFeatEdge
                | .
                |
                | Example:
                |     This example asks the end user to select a planar curve, whose plane is
                |     parallel to the XY plane. Then, it creates a point on the tangent to the curve
                |     in the X direction:
                |
                |      Dim InputObjectType(0)
                |      Set Document = CATIA.ActiveDocument
                |      Set Selection = Document.Selection
                |      Set HybridBodies = Document.Part.HybridBodies
                |      Set HybridBody = HybridBodies.Item("Geometrical Set.1")
                |      'We propose to the user that he select a planar curve whose plane is
                |      parallel to the XY plane
                |      InputObjectType(0)="Edge"
                |      Status=Selection.SelectElement2(InputObjectType,"Select a planar curve
                |      whose plane is parallel to the XY plane",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set PlanarCurve = Selection.Item(1).Value
                |      Set HybridShapeDirection = HybridShapeFactory.AddNewDirectionByCoord(1.0,0.0,0.0)
                |      Set HybridShapePointTangent = HybridShapeFactory.
                |                                        AddNewPointTangent(PlanarCurve,HybridShapeDirection)
                |      HybridBody.AppendHybridShape HybridShapePointTangent
                |      Document.Part.InWorkObject = HybridShapePointTangent
                |      Document.Part.Update

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.edge = com_object

    def __repr__(self):
        return f'Edge(name="{self.name}")'
