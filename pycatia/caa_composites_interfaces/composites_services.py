#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class CompositesServices(AnyObject):
    """

    Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CompositesServices
                |
                | Represents CATIACompositesServices that allow to query composites
                | entity.
                | Role: On any object recovers is it his a composites object or not and provides
                | its type if yes.
                |
                | Example:
                |     This VBScript example illustrates how to GetCompositesType if any , on
                |     objects in CATIA Part.
                |
                |
                |      VBScript example to identify composites object type
                |
                |      Sub CATMain()
                |         Const UNKNOWN       = 0
                |         Const STACKING      = 1
                |         Const PLYGROUP      = 2
                |         Const SEQUENCE      = 3
                |         Const CUTPIECEGROUP = 4
                |         Const PLY           = 5
                |         Const CORE          = 6
                |         Const CUTPIECE      = 7
                |         ' Part
                |         Set myPart = CATIA.ActiveDocument.Part
                |
                |         ' Get Service Object by querying on part - extension of CATIA Base
                |
                |         Set myCompServObj = myPart.GetItem("CATCompositesServices")
                |
                |         ' Hybrid Bodies
                |         Set myHBodies = myPart.HybridBodies
                |
                |         ' Get Part Hybrid Bodies Count
                |         HBCount = myHBodies.Count
                |
                |         StckCnt = 0
                |         For N = 1 To PartHBCount
                |            ' Iterate through all Hybrid Bodies in Part one by one and retrieve
                |            its type
                |              Set myObject = myHBodies.Item(N)
                |              myCompServObj.GetCompositesType myObject, myType
                |              If myType = STACKING Then
                |         		     ' ==> Stacking Composites feature type is recovered  among
                |         hybridshapes under part
                |         		    ObjCompositesStacking =  myObject
                |         		    ' ....
                |         		Exit For
                |         	End if
                |         Next
                |         Mggbox "Stacking="& ObjCompositesStacking.Name
                |      End Sub

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.composites_services = com_object

    def get_composites_type(self, i_object: cat_variant, i_composites_type: int) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub GetCompositesType(CATVariant iObject,CATCompositesTypeEnum
                | oCompositesType)
                |     Retrieves "Composites Type" of an 3D object.
                |
                |     Parameters:
                |
                |         iObject
                |             Object whose type is to be retrieved.
                |         oCompositesType
                |             Composites Type of input object.
                |
                |     See also:
                |         CATCompositesTypeEnum

        :param cat_variant i_object:
        :param int i_composites_type: see enumeration type cat_composites_type
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.composites_services.GetCompositesType(i_object.com_object, i_composites_type)

    def __repr__(self):
        return f'CompositesServices(name="{self.name}")'
