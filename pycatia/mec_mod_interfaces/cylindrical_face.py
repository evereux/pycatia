#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from pycatia.mec_mod_interfaces.face import Face


class CylindricalFace(Face):
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
                |                             MecModInterfaces.Face
                |                                 CylindricalFace
                |
                | 2-D boundary with a cylindrical geometry.
                | Role: This Boundary object may be, for example, the lateral face of a
                | cylinder.
                | You will create a CylindricalFace object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | ShapeFactory.AddNewCircPattern ).
                | The lifetime of a CylindricalFace object is limited, see
                | Boundary.
                |
                | Example:
                |     This example asks the end user to select a shape to pattern and a
                |     cylindrical face, and creates a circular pattern of the shape. The cylindrical
                |     face specifies the rotation axis.
                |
                |      Dim InputObjectType(0)
                |      Set Document = CATIA.ActiveDocument
                |      Set Selection = Document.Selection
                |      'We propose to the user that he select the shape to
                |      pattern
                |      InputObjectType(0)="SketchBasedShape"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the shape to
                |      pattern",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set Shape = Selection.Item(1).Value
                |      Selection.Clear
                |      'We propose to the user that he select the cylindrical
                |      face
                |      InputObjectType(0)="CylindricalFace"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the cylindrical
                |      face",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set CylindricalFace = Selection.Item(1).Value
                |      Set RotationCenter = Document.Part.CreateReferenceFromName("")
                |      Set CircPattern = ShapeFactory.AddNewCircPattern(Shape,1,4,20.0,45.0,1,4,RotationCenter,
                |                            CylindricalFace,True,0.0,True)
                |      Document.Part.Update

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cylindrical_face = com_object

    def get_direction(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetDirection(CATSafeArrayVariant oDirection)
                | 
                |     Returns the direction of the cylindrical face axis
                |
                |     Parameters:
                |
                |         oDirection[0]
                |             The X Coordinate of the axis direction
                |         oDirection[1]
                |             The Y Coordinate of the axis direction
                |         oDirection[2]
                |             The Z Coordinate of the axis direction

        :param tuple o_direction:
        :return: None
        """

        vba_function_name = 'get_direction'
        vba_code = """
        Public Function get_direction(cylindrical_face)
            Dim oDirection (2)
            cylindrical_face.GetDirection oDirection
            get_direction = oDirection
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_origin(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetOrigin(CATSafeArrayVariant oOrigin)
                | 
                |     Returns the origin of the cylindrical face axis.
                |
                |     Parameters:
                |
                |         oOrigin[0]
                |             The X Coordinate of the axis origin
                |         oOrigin[1]
                |             The Y Coordinate of the axis origin
                |         oOrigin[2]
                |             The Z Coordinate of the axis origin

        :param tuple o_origin:
        :rtype: None
        """

        vba_function_name = 'get_origin'
        vba_code = """
        Public Function get_origin(cylindrical_face)
            Dim oOrigin (2)
            cylindrical_face.GetOrigin oOrigin
            get_origin = oOrigin
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'CylindricalFace(name="{self.name}")'
