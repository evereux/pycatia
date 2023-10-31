#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.structure_interfaces.str_cutout_feature import StrCutoutFeature
from pycatia.structure_interfaces.str_nibbling_feature import StrNibblingFeature
from pycatia.system_interfaces.any_object import AnyObject


class StrFeatureFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrFeatureFactory
                | 
                | Represents the Factory Object for Structure Features.
                | The factory is retrieved using the StrPlate or StrMember
                | 
                | Example:
                |     The following example retrieves the Feature factory object from the
                |     Selection on ActiveDocument.
                | 
                |      Dim Plate As StrPlate
                |      Set Plate = strPlates.Item("Plate_007")
                |      Dim Sel As Selection
                |      Set Sel = CATIA.ActiveDocument.Selection
                |      ' Use the Add method to add Plate to selection
                |      Sel.Add Plate
                |      Dim Factory As StrFeatureFactory
                |      Set Factory = Sel.FindObject("CATIAStrFeatureFactory")
                |      
                | 
                |     Method Index
                |     AddCutoutWithAfterFormingMode
                |         Adds a Cutout Feature on Plate/Member using AfterForming Mode.
                |         
                |     AddCutoutWithBeforeFormingMode
                |         Adds a Cutout Feature on Plate/Member using BeforeForming Mode.
                |         
                |     AddNibbling
                |         Adds a Coping on Plate or Member. 
                | 
                |     Methods
                | 
                | o Func AddCutoutWithAfterFormingMode(	Reference 	iContour,
                | 	Reference 	iDirection) As StrCutoutFeature
                | 
                |     Adds a Cutout Feature on Plate/Member using AfterForming
                |     Mode.
                | 
                |     Parameters:
                | 
                |         iContour
                |             [in] The Sketch used to create the cutout. This must exist in the
                |             document. 
                |         iDirection
                |             [in] The direction in which the cutout should be created. Valid
                |             inputs are line created in sketch,3D Line. 
                |         oCutout[out]
                |             The CutOut Feature 
                |         @return
                |             S_OK if everything ran ok.
                | 
                |             Example
                |             :
                |                 This example creates Cutout on Plate.
                | 
                |                  ' Define the Plate on which cutout is to be
                |                  created
                |                  Dim strPlates As strPlates
                |                  Set strPlates = rootProduct.GetTechnologicalObject("StructurePlates")
                |                  Dim PlateToCut As StrPlate
                |                  Set PlateToCut = strPlates.Item("Plate_012")
                |                 ' Add the Plate to Selection
                |                  Dim Sel As Selection
                |                  Set Sel = CATIA.ActiveDocument.Selection
                |                  Sel.Add PlateToCut
                |                  'Get The factory from selection
                |                  Dim Factory As StrFeatureFactory
                |                  Set Factory = Sel.FindObject("CATIAStrFeatureFactory")
                |                  ' Select the Sketch profile exisitng in the
                |                  document
                |                  Dim sketch As Reference
                |                  Set sketch = rootProduct.CreateReferenceFromName("Product1/Grid/!Sketch.1")
                |                  ' Select the direction in which the cutout should be
                |                  created
                |                  Dim dir1 As Reference
                |                  Set dir1 = rootProduct.CreateReferenceFromName("Product1/Grid/!Sketch.2")
                |                  ' Create cutout
                |                  Dim Cutout1 As StrCutoutFeature
                |                  Set Cutout1 = Factory.AddCutoutWithAfterFormingMode(sketch, dir1)
                |                  
                | 
                | o Func AddCutoutWithBeforeFormingMode(	Reference 	iContour,
                | 	Reference 	iSurface) As StrCutoutFeature
                | 
                |     Adds a Cutout Feature on Plate/Member using BeforeForming
                |     Mode.
                | 
                |     Parameters:
                | 
                |         iContour
                |             [in] The Sketch used to create the cutout. This must exist in the
                |             document 
                |         iSurface
                |             [in] A Surface on which Plate/Member is created. 
                |         oCutout[out]
                |             The CutOut Feature 
                |         @return
                |             S_OK if everything ran ok.
                | 
                |             Example
                |             :
                |                 This example creates Cutout on Member.
                | 
                |                  'Define the Plate on which cutout is to be
                |                  created
                |                  Dim strPlates As strPlates
                |                  Set strPlates = rootProduct.GetTechnologicalObject("StructurePlates")
                |                  Dim PlateToCut As StrPlate
                |                  Set PlateToCut = strPlates.Item("Plate_012")
                |                  ' Add the Plate to Selection
                |                  Dim Sel As Selection
                |                  Set Sel = CATIA.ActiveDocument.Selection
                |                  Sel.Add PlateToCut
                |                  ' Get The factory from selection
                |                  Dim Factory As StrFeatureFactory
                |                  Set Factory = Sel.FindObject("CATIAStrFeatureFactory")
                |                  ' Select the Sketch profile exisitng in the
                |                  document
                |                  Dim sketch As Reference
                |                  Set sketch = rootProduct.CreateReferenceFromName("Product1/Grid/!Sketch.1")
                |                  ' Select the surface 
                |                  Dim Surface1 As Reference
                |                  Set Surface1 = rootProduct.CreateReferenceFromName("Product1/Grid/!Extrude.1")
                |                  ' Create cutout
                |                  Dim Cutout1 As StrCutoutFeature
                |                  Set Cutout1 = Factory.AddCutoutWithBeforeFormingMode(sketch, Surface1)
                |                  
                | 
                | o Func AddNibbling(	CATSafeArrayVariant
                | iListOfLimitingElements,
                | 	CATBSTR 	iNibblingType) As StrNibblingFeature
                | 
                |     Adds a Coping on Plate or Member.
                | 
                |     Parameters:
                | 
                |         iListOfLimitingElements
                |             [in] List of Limiting elements used for limiting the Plate/Member.
                |             Pass only one limit at a time. 
                |         iNibblingType
                |             [in] Possible Values for Plate:"Remove". Possible Values for
                |             Member:"Remove","ShortPoint","LongPoint","WeldCut". For Defining further
                |             attributes refer CATIAStrNibblingFeature. 
                |         oNibblingFeature[out]
                |             The Nibbled Plate/Member. 
                |         @return
                |             S_OK if everything ran ok.
                | 
                |             Example
                |             :
                |                 This example creates Coping on Plate.
                | 
                |                  Dim Limitplate1 As StrPlate
                |                  Set Limitplate1 = strPlates.Item("Plate_008")
                |                  Dim Listoflimits As Variant
                |                  Set Listoflimits(0) =Limitplate1
                |                  Dim NibblingFeature As StrNibblingFeature
                |                  Set NibblingFeature = Factory.AddNibbling(Listoflimits, "Remove")
                |                  
                | 
                |     Copyright © 1999-2011, Dassault Systèmes. All rights
                |     reserved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.str_feature_factory = com_object

    def add_cutout_with_after_forming_mode(self, i_contour: Reference, i_direction: Reference) -> StrCutoutFeature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddCutoutWithAfterFormingMode(Reference iContour,
                | Reference iDirection) As StrCutoutFeature
                | 
                |     Adds a Cutout Feature on Plate/Member using AfterForming
                |     Mode.
                | 
                |     Parameters:
                | 
                |         iContour
                |             [in] The Sketch used to create the cutout. This must exist in the
                |             document. 
                |         iDirection
                |             [in] The direction in which the cutout should be created. Valid
                |             inputs are line created in sketch,3D Line. 
                |         oCutout[out]
                |             The CutOut Feature 
                |         @return
                |             S_OK if everything ran ok.
                | 
                |             Example
                |             :
                |                 This example creates Cutout on Plate.
                | 
                |                  ' Define the Plate on which cutout is to be
                |                  created
                |                  Dim strPlates As strPlates
                |                  Set strPlates = rootProduct.GetTechnologicalObject("StructurePlates")
                |                  Dim PlateToCut As StrPlate
                |                  Set PlateToCut = strPlates.Item("Plate_012")
                |                 ' Add the Plate to Selection
                |                  Dim Sel As Selection
                |                  Set Sel = CATIA.ActiveDocument.Selection
                |                  Sel.Add PlateToCut
                |                  'Get The factory from selection
                |                  Dim Factory As StrFeatureFactory
                |                  Set Factory = Sel.FindObject("CATIAStrFeatureFactory")
                |                  ' Select the Sketch profile exisitng in the
                |                  document
                |                  Dim sketch As Reference
                |                  Set sketch = rootProduct.CreateReferenceFromName("Product1/Grid/!Sketch.1")
                |                  ' Select the direction in which the cutout should be
                |                  created
                |                  Dim dir1 As Reference
                |                  Set dir1 = rootProduct.CreateReferenceFromName("Product1/Grid/!Sketch.2")
                |                  ' Create cutout
                |                  Dim Cutout1 As StrCutoutFeature
                |                  Set Cutout1 = Factory.AddCutoutWithAfterFormingMode(sketch, dir1)

        :param Reference i_contour:
        :param Reference i_direction:
        :rtype: StrCutoutFeature
        """
        return StrCutoutFeature(
            self.str_feature_factory.AddCutoutWithAfterFormingMode(i_contour.com_object, i_direction.com_object))

    def add_cutout_with_before_forming_mode(self, i_contour: Reference, i_surface: Reference) -> StrCutoutFeature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddCutoutWithBeforeFormingMode(Reference iContour,
                | Reference iSurface) As StrCutoutFeature
                | 
                |     Adds a Cutout Feature on Plate/Member using BeforeForming
                |     Mode.
                | 
                |     Parameters:
                | 
                |         iContour
                |             [in] The Sketch used to create the cutout. This must exist in the
                |             document 
                |         iSurface
                |             [in] A Surface on which Plate/Member is created. 
                |         oCutout[out]
                |             The CutOut Feature 
                |         @return
                |             S_OK if everything ran ok.
                | 
                |             Example
                |             :
                |                 This example creates Cutout on Member.
                | 
                |                  'Define the Plate on which cutout is to be
                |                  created
                |                  Dim strPlates As strPlates
                |                  Set strPlates = rootProduct.GetTechnologicalObject("StructurePlates")
                |                  Dim PlateToCut As StrPlate
                |                  Set PlateToCut = strPlates.Item("Plate_012")
                |                  ' Add the Plate to Selection
                |                  Dim Sel As Selection
                |                  Set Sel = CATIA.ActiveDocument.Selection
                |                  Sel.Add PlateToCut
                |                  ' Get The factory from selection
                |                  Dim Factory As StrFeatureFactory
                |                  Set Factory = Sel.FindObject("CATIAStrFeatureFactory")
                |                  ' Select the Sketch profile exisitng in the
                |                  document
                |                  Dim sketch As Reference
                |                  Set sketch = rootProduct.CreateReferenceFromName("Product1/Grid/!Sketch.1")
                |                  ' Select the surface 
                |                  Dim Surface1 As Reference
                |                  Set Surface1 = rootProduct.CreateReferenceFromName("Product1/Grid/!Extrude.1")
                |                  ' Create cutout
                |                  Dim Cutout1 As StrCutoutFeature
                |                  Set Cutout1 = Factory.AddCutoutWithBeforeFormingMode(sketch, Surface1)

        :param Reference i_contour:
        :param Reference i_surface:
        :rtype: StrCutoutFeature
        """
        return StrCutoutFeature(
            self.str_feature_factory.AddCutoutWithBeforeFormingMode(i_contour.com_object, i_surface.com_object))

    def add_nibbling(self, i_list_of_limiting_elements: tuple, i_nibbling_type: str) -> StrNibblingFeature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddNibbling(CATSafeArrayVariant
                | iListOfLimitingElements,
                | CATBSTR iNibblingType) As StrNibblingFeature
                | 
                |     Adds a Coping on Plate or Member.
                | 
                |     Parameters:
                | 
                |         iListOfLimitingElements
                |             [in] List of Limiting elements used for limiting the Plate/Member.
                |             Pass only one limit at a time. 
                |         iNibblingType
                |             [in] Possible Values for Plate:"Remove". Possible Values for
                |             Member:"Remove","ShortPoint","LongPoint","WeldCut". For Defining further
                |             attributes refer CATIAStrNibblingFeature. 
                |         oNibblingFeature[out]
                |             The Nibbled Plate/Member. 
                |         @return
                |             S_OK if everything ran ok.
                | 
                |             Example
                |             :
                |                 This example creates Coping on Plate.
                | 
                |                  Dim Limitplate1 As StrPlate
                |                  Set Limitplate1 = strPlates.Item("Plate_008")
                |                  Dim Listoflimits As Variant
                |                  Set Listoflimits(0) =Limitplate1
                |                  Dim NibblingFeature As StrNibblingFeature
                |                  Set NibblingFeature = Factory.AddNibbling(Listoflimits, "Remove")
                |                  
                | 
                |     Copyright © 1999-2011, Dassault Systèmes. All rights
                |     reserved.

        :param tuple i_list_of_limiting_elements:
        :param str i_nibbling_type:
        :rtype: StrNibblingFeature
        """
        return StrNibblingFeature(self.str_feature_factory.AddNibbling(i_list_of_limiting_elements, i_nibbling_type))

    def __repr__(self):
        return f'StrFeatureFactory(name="{self.name}")'
