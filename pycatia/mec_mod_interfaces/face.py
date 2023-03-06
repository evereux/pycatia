#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from pycatia.mec_mod_interfaces.boundary import Boundary


class Face(Boundary):
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
                |                             Face
                |
                | 2-D boundary.
                | Role: This Boundary object may be, for example, the lateral face of
                | cylinder.
                | You will create a Face object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | ShapeFactory.AddNewFaceFillet ).
                | The lifetime of a Face object is limited, see Boundary.
                | See also:
                | PlanarFace , CylindricalFace .
                |
                | Example:
                |     This example asks the end user to select two faces, and creates a face-face
                |     fillet on these faces:
                |
                |      Dim InputObjectType(0)
                |      Set Document = CATIA.ActiveDocument
                |      Set Selection = Document.Selection
                |      'We propose to the user that he select the first face
                |      InputObjectType(0)="Face"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the first
                |      face",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set FirstFace = Selection.Item(1).Value
                |      Selection.Clear
                |      'We propose to the user that he select the second face
                |      InputObjectType(0)="Face"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the second
                |      face",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set SecondFace = Selection.Item(1).Value
                |      Set FaceFillet = ShapeFactory.AddNewFaceFillet(FirstFace,SecondFace,5.0)
                |      Document.Part.Update

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.face = com_object

    def __repr__(self):
        return f'Face(name="{self.name}")'
