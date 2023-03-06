#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from pycatia.in_interfaces.reference import Reference


class Boundary(Reference):
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
                |                         Boundary
                |
                | Topological cell, such as a face, an edge or a vertex.
                | Role: The Boundary objects are basic topological objects, such as the edge of a
                | Pad. Some of them posess a geometrical feature (planar face, rectilinear
                | edge).
                | You will create a Boundary object (such as the TriDimFeatEdge object, which is
                | derived, indirectly, from the Boundary object) using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | ShapeFactory.AddNewEdgeFilletWithConstantRadius ). Note that, regarding V4
                | sub-elements, once the data of a CATIA Version 4 Model has been copied to a
                | .CATPart, the sub-elements of the resulting .CATPart are supported by the
                | Boundary object.
                | The lifetime of a Boundary object is limited. In particular, after having call
                | Part.Update , the Boundary objects are usually no more valid.
                | See also:
                |
                |     Face , PlanarFace , CylindricalFace
                |     Edge , TriDimFeatEdge , RectilinearTriDimFeatEdge , BiDimFeatEdge ,
                |     RectilinearBiDimFeatEdge , MonoDimFeatEdge ,
                |     RectilinearMonoDimFeatEdge
                |     Vertex , TriDimFeatVertexOrBiDimFeatVertex ,
                |     NotWireBoundaryMonoDimFeatVertex,
                |     ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex
                |
                | Note: Boundary objects cannot be selected into the specification
                | tree.
                |
                | Note:For a Boundary object, the object returned by the AnyObject.Parent
                | property is the master shape. For example, if we have:
                |
                |                          Pad.2
                |                           !
                |                           !
                |  +                        V
                |  !                      +---+
                |  !                    /   / !
                |  +-- Pad.1          /   /   !
                |  !                /   / one +------+
                |  !               +---+    /       /! <--- Pad.1
                |  !               !   !  /       /  +
                |  +-- Pad.2       !   !/       /   /
                |                  !   +------+   /
                |                  !          ! /
                |                  +----------+
                |
                |
                | then, for the PlanarFace number "one", the AnyObject.Parent property returns
                | the Pad.2 automation object (see Pad ).
                |
                | Example:
                |     This example asks the end user to select an edge (using the TriDimFeatEdge
                |     object), and creates an edge fillet on this edge:
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
        self.boundary = com_object

    def __repr__(self):
        return f'Boundary(name="{self.name}")'
