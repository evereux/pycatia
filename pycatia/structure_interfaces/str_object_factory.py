#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.document import Document
from pycatia.in_interfaces.reference import Reference
from pycatia.structure_interfaces.str_foundation import StrFoundation
from pycatia.structure_interfaces.str_member import StrMember
from pycatia.structure_interfaces.str_plate import StrPlate
from pycatia.structure_interfaces.str_section import StrSection
from pycatia.system_interfaces.any_object import AnyObject


class StrObjectFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrObjectFactory
                | 
                | Represents the factory object for all the structure objects.
                | The factory is retrieved using the Product.GetTechnologicalObject method of the
                | product.
                | 
                | Example:
                |     The following example retrieves the structure factory object from the
                |     oProduct Product.
                | 
                |      Dim oFactory as AnyObject
                |      Set oFactory = oProduct.GetTechnologicalObject("StructureObjectFactory")
                |      
                | 
                |     Method Index
                |     AddDefExtFromCoordinates
                |         Creates a member extremity definition object from coordinates and an
                |         offset value. 
                |     AddDefExtFromReference
                |         Creates a member extremity definition object from an existing object in
                |         the model and an offset value. 
                |     AddDefExtOnMember
                |         Creates a member extremity definition object from another member
                |         object, its side, a distance on it and an offset. 
                |     AddDimMember
                |         Creates a dimension member object from a point and a mathematical
                |         definition of a direction. 
                |     AddDimMemberOnPlane
                |         Creates a dimension member object on a plane following a mathematical
                |         definition of a plane. 
                |     AddDimMemberPtPt
                |         Creates a dimension member object from two given points.
                |         
                |     AddDimMemberWithSupport
                |         Creates a dimension member object using a support object.
                |         
                |     AddMember
                |         Creates a member object. 
                |     AddMemberFromDir
                |         Creates a member object using a direction object as a line or a plane.
                |         
                |     AddMemberFromMathDir
                |         Creates a member object using a mathematical definition of the
                |         direction. 
                |     AddMemberFromMathPlane
                |         Creates a member object from a mathematical definition of a plane.
                |         
                |     AddMemberOnSupport
                |         Creates a member object on a given support. 
                |     AddMemberOnSupportWithRef
                |         Creates a member object on a given support object and a surface used to
                |         define the orientation of the section. 
                |     AddPlate
                |         Creates a plate from a contour defined by coordinates.
                |         
                |     AddPlateOnSurface
                |         Creates a plate from a surface. 
                |     AddRectangularEndPlate
                |         Creates a rectangular end plate on an extremity of a given member.
                |         
                |     AddSection
                |         Creates a section object from part document. 
                |     AddSectionFromCatalog
                |         Creates a section object from part document. 
                |     ExtendProductAsFoundation
                |         Extend an assembly as a structure foundation assembly.
                |         
                | 
                |     Methods
                | 
                | o Func AddDefExtFromCoordinates(	CATSafeArrayVariant 	iCoord,
                | 	double 	iOffset) As AnyObject
                | 
                |     Creates a member extremity definition object from coordinates and an offset
                |     value.
                | 
                |     Parameters:
                | 
                |         iCoord
                |             The coordinates of the extremity 
                |         iOffset
                |             The offset on this extremity
                | 
                | o Func AddDefExtFromReference(	Reference 	iReference,
                | 	double 	iOffset) As AnyObject
                | 
                |     Creates a member extremity definition object from an existing object in the
                |     model and an offset value.
                | 
                |     Parameters:
                | 
                |         iReference
                |             The reference object defining the extremity 
                |         iOffset
                |             The offset on this extremity
                | 
                | o Func AddDefExtOnMember(	StrMember 	iMember,
                | 	CatStrMemberExtremity 	iSide,
                | 	double 	iDistance,
                | 	double 	iOffset) As AnyObject
                | 
                |     Creates a member extremity definition object from another member object,
                |     its side, a distance on it and an offset.
                | 
                |     Parameters:
                | 
                |         iMember
                |             The member used to define the extremity 
                |         iSide
                |             The side of the previous member used to define the distance along
                |             the member 
                |         iDistance
                |             The distance along the selected member 
                |         iOffset
                |             The offset on the extremity 
                | 
                | o Func AddDimMember(	StrSection 	iSection,
                | 	CATBSTR 	iAnchorName,
                | 	double 	iAngle,
                | 	AnyObject 	iDefExtr1,
                | 	CATSafeArrayVariant 	iMathDirection,
                | 	double 	iLength,
                | 	CATBSTR 	iType) As StrMember
                | 
                |     Creates a dimension member object from a point and a mathematical
                |     definition of a direction.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iMathDirection
                |             The mathematical definition of the direction 
                |         iLength
                |             The length of the member 
                |         iType
                |             The type of the member. This type is user defined.
                | 
                | o Func AddDimMemberOnPlane(	StrSection 	iSection,
                | 	CATBSTR 	iAnchorName,
                | 	double 	iAngle,
                | 	AnyObject 	iDefExtr1,
                | 	AnyObject 	iDefExtr2,
                | 	CATSafeArrayVariant 	iDirection,
                | 	CatStrPlaneMode 	iMode,
                | 	double 	iLength,
                | 	CATBSTR 	iType) As StrMember
                | 
                |     Creates a dimension member object on a plane following a mathematical
                |     definition of a plane.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member
                |             
                |         iDirection
                |             The direction object. It can be a line or a plane 
                |         iMode
                |             The way the member is created with respect to the direction plane.
                |             Useless if if the direction is not a plane. 
                |         iOrientation
                |             The orientation of the member 
                |         iLength
                |             The length of the member 
                |         iType
                |             The type of the member. This type is user defined.
                | 
                | o Func AddDimMemberPtPt(	StrSection 	iSection,
                | 	CATBSTR 	iAnchorName,
                | 	double 	iAngle,
                | 	AnyObject 	iDefExtr1,
                | 	AnyObject 	iDefExtr2,
                | 	double 	iLength,
                | 	CATBSTR 	iType) As StrMember
                | 
                |     Creates a dimension member object from two given points.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member
                |             
                |         iLength
                |             The length of the member 
                |         iType
                |             The type of the member. This type is user defined.
                | 
                | o Func AddDimMemberWithSupport(	StrSection 	iSection,
                | 	CATBSTR 	iAnchorName,
                | 	double 	iAngle,
                | 	AnyObject 	iDefExtr1,
                | 	AnyObject 	iDefExtr2,
                | 	Reference 	iDirection,
                | 	CatStrPlaneMode 	iMode,
                | 	CatStrMaterialOrientation 	iOrientation,
                | 	double 	iLength,
                | 	CATBSTR 	iType) As StrMember
                | 
                |     Creates a dimension member object using a support object.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member. In case
                |             of line for a support, this parameter is not taking into account.
                |             
                |         iDirection
                |             The direction object. It can be a line or a plane 
                |         iMode
                |             The way the member is created with respect to the direction plane.
                |             Useless if if the direction is not a plane. 
                |         iOrientation
                |             The orientation of the member 
                |         iLength
                |             The length of the member 
                |         iType
                |             The type of the member
                | 
                | o Func AddMember(	StrSection 	iSection,
                | 	CATBSTR 	iAnchorName,
                | 	double 	iAngle,
                | 	AnyObject 	iDefExtr1,
                | 	AnyObject 	iDefExtr2,
                | 	CATBSTR 	iType) As StrMember
                | 
                |     Creates a member object.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member
                |             
                |         iType
                |             The type of the member. This type is user defined.
                | 
                | o Func AddMemberFromDir(	StrSection 	iSection,
                | 	CATBSTR 	iAnchorName,
                | 	double 	iAngle,
                | 	AnyObject 	iDefExtr1,
                | 	AnyObject 	iDefExtr2,
                | 	Reference 	iDirection,
                | 	CatStrPlaneMode 	iMode,
                | 	CATBSTR 	iType) As StrMember
                | 
                |     Creates a member object using a direction object as a line or a
                |     plane.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member
                |             
                |         iDirection
                |             The direction object used to orientate the support. The direction
                |             object can be a plane or a line. 
                |         iMode
                |             The way the member is created with respect to the direction plane.
                |             Useless if if the direction is not a plane. 
                |         iType
                |             The type of the member. This type is user defined.
                | 
                | o Func AddMemberFromMathDir(	StrSection 	iSection,
                | 	CATBSTR 	iAnchorName,
                | 	double 	iAngle,
                | 	AnyObject 	iDefExtr1,
                | 	AnyObject 	iDefExtr2,
                | 	CATSafeArrayVariant 	iDirection,
                | 	CATBSTR 	iType) As StrMember
                | 
                |     Creates a member object using a mathematical definition of the
                |     direction.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member
                |             
                |         iDirection
                |             The mathematical definition of the direction 
                |         iType
                |             The type of the member. This type is user defined.
                |             
                | 
                | o Func AddMemberFromMathPlane(	StrSection 	iSection,
                | 	CATBSTR 	iAnchorName,
                | 	double 	iAngle,
                | 	AnyObject 	iDefExtr1,
                | 	AnyObject 	iDefExtr2,
                | 	CATSafeArrayVariant 	iPlane,
                | 	CatStrPlaneMode 	iPlaneMode,
                | 	CATBSTR 	iType) As StrMember
                | 
                |     Creates a member object from a mathematical definition of a
                |     plane.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member
                |             
                |         iDirection
                |             The mathematical definition of a plane 
                |         iPlaneMode
                |             The way the member is created with respect to the direction plane.
                |             Useless if if the direction is not a plane. 
                |         iType
                |             The type of the member. This type is user defined.
                | 
                | o Func AddMemberOnSupport(	StrSection 	iSection,
                | 	CATBSTR 	iAnchorName,
                | 	double 	iAngle,
                | 	Reference 	iSupport,
                | 	AnyObject 	iDefExtr1,
                | 	AnyObject 	iDefExtr2,
                | 	CATBSTR 	iType) As StrMember
                | 
                |     Creates a member object on a given support.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iSupport
                |             The support for the member. The support can be a line or a curve
                |             
                |         iDefExtr1
                |             The extremity object defining the start limit of the member. It can
                |             be NULL. 
                |         iDefExtr2
                |             The extremity object defining the end limit of the member. It can
                |             be NULL. 
                |         iType
                |             The type of the member. This type is user defined.
                |             
                | 
                | o Func AddMemberOnSupportWithRef(	StrSection 	iSection,
                | 	CATBSTR 	iAnchorName,
                | 	Reference 	iSurfRef,
                | 	double 	iAngle,
                | 	Reference 	iSupport,
                | 	AnyObject 	iDefExtr1,
                | 	AnyObject 	iDefExtr2,
                | 	CATBSTR 	iType) As StrMember
                | 
                |     Creates a member object on a given support object and a surface used to
                |     define the orientation of the section. The surface reference defines the
                |     relative orientation on which you add an angle.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iReference
                |             The reference to define the zero orientation of the section. The
                |             section follows this guide line along the support of the member.
                |             
                |         iAngle
                |             The orientation of the section on its support 
                |         iSupport
                |             The support for the member. The support can be a line or a curve
                |             
                |         iDefExtr1
                |             The extremity object defining the start limit of the member. It can
                |             be NULL. 
                |         iDefExtr2
                |             The extremity object defining the end limit of the member. It can
                |             be NULL. 
                |         iType
                |             The type of the member. This type is user defined.
                | 
                | o Func AddPlate(	Reference 	iSupport,
                | 	double 	iThickness,
                | 	CatStrMaterialOrientation 	iOrientation,
                | 	CATSafeArrayVariant 	iContour,
                | 	double 	iOffset,
                | 	CATBSTR 	iType) As StrPlate
                | 
                |     Creates a plate from a contour defined by coordinates.
                | 
                |     Parameters:
                | 
                |         iSupport
                |             The plane defining the support of the plate 
                |         iThickness
                |             The standard thickness of the plate. The thickness follows the
                |             standard orientation of the support 
                |         iOrientation
                |             The material orientation of the plate 
                |         iContour
                |             The array containing all objects defining the contour of the plate
                |             
                |         iOffset
                |             The offset applies to the support of the plate 
                |         iType
                |             The type of the plate. This information is user defined. It is
                |             added as an attribute on the plate.
                | 
                | o Func AddPlateOnSurface(	double 	iThickness,
                | 	CatStrMaterialOrientation 	iOrientation,
                | 	Reference 	iSurface,
                | 	double 	iOffset,
                | 	CATBSTR 	iType) As StrPlate
                | 
                |     Creates a plate from a surface.
                | 
                |     Parameters:
                | 
                |         iThickness
                |             The standard thickness of the plate. The thickness follows the
                |             standard orientation of the support 
                |         iOrientation
                |             The material orientation of the plate 
                |         iSurface
                |             The surface on which plate is to be created. If Surface path is
                |             NULL then method will return E_INVALID_ARG 
                |         iOffset
                |             The offset applies to the support of the plate 
                |         iType
                |             The type of the plate. This information is user defined. It is
                |             added as an attribute on the plate.
                | 
                | o Func AddRectangularEndPlate(	StrMember 	iMember,
                | 	CatStrMemberExtremity 	iSide,
                | 	double 	iThickness,
                | 	double 	iHeight,
                | 	double 	iWidth,
                | 	CatStrMaterialOrientation 	iOrientation,
                | 	CATBSTR 	iType) As StrPlate
                | 
                |     Creates a rectangular end plate on an extremity of a given
                |     member.
                | 
                |     Parameters:
                | 
                |         iMember
                |             The member on which the end-plate will be created 
                |         iSide
                |             The side of the selected member 
                |         iThickness
                |             The standard thickness of the plate. The thickness follows the
                |             standard orientation of the support 
                |         iHeight
                |             The height of the plate 
                |         iWidth
                |             The width of the plate 
                |         iOrientation
                |             The material orientation of the plate 
                |         iType
                |             The type of the plate. This information is user defined. It is
                |             added as an attribute on the plate.
                | 
                | o Func AddSection(	Document 	iPart) As StrSection
                | 
                |     Creates a section object from part document. This part must aggregate a
                |     sketch object defining the contour of the section. The contour of the section
                |     have to be closed and may contain several domains.
                | 
                |     Parameters:
                | 
                |         iPart
                |             The part document where the sketch of the section is
                |             defined
                | 
                | o Func AddSectionFromCatalog(	Document 	iPart,
                | 	CATBSTR 	iCatalogName,
                | 	CATBSTR 	iFamilyName,
                | 	CATBSTR 	iSectionName) As StrSection
                | 
                |     Creates a section object from part document. This part must aggregate a
                |     sketch object defining the contour of the section. This service gives you to
                |     define where the resolved part comes from to allow a replace mechanism. The
                |     contour of the section have to be closed and may contain several
                |     domains.
                | 
                |     Parameters:
                | 
                |         iCatalogName
                |             The catalog name where the document comes from 
                |         iFamilyName
                |             The family name where the document comes from 
                |         iSectionName
                |             The section name where the document comes from 
                |         iPart
                |             The part document where the sketch of the section is
                |             defined
                | 
                | o Func ExtendProductAsFoundation(	CATBSTR 	iClass) As
                | StrFoundation
                | 
                |     Extend an assembly as a structure foundation assembly.
                | 
                |     Parameters:
                | 
                |         iClass
                |             the name of the user class
                | 
                | Copyright © 1999-2011, Dassault Systèmes. All rights reserved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.str_object_factory = com_object

    def add_def_ext_from_coordinates(self, i_coord: tuple, i_offset: float) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddDefExtFromCoordinates(CATSafeArrayVariant iCoord,
                | double iOffset) As AnyObject
                | 
                |     Creates a member extremity definition object from coordinates and an offset
                |     value.
                | 
                |     Parameters:
                | 
                |         iCoord
                |             The coordinates of the extremity 
                |         iOffset
                |             The offset on this extremity

        :param tuple i_coord:
        :param float i_offset:
        :rtype: AnyObject
        """
        return AnyObject(self.str_object_factory.AddDefExtFromCoordinates(i_coord, i_offset))

    def add_def_ext_from_reference(self, i_reference: Reference, i_offset: float) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddDefExtFromReference(Reference iReference,
                | double iOffset) As AnyObject
                | 
                |     Creates a member extremity definition object from an existing object in the
                |     model and an offset value.
                | 
                |     Parameters:
                | 
                |         iReference
                |             The reference object defining the extremity 
                |         iOffset
                |             The offset on this extremity

        :param Reference i_reference:
        :param float i_offset:
        :rtype: AnyObject
        """
        return AnyObject(self.str_object_factory.AddDefExtFromReference(i_reference.com_object, i_offset))

    def add_def_ext_on_member(self, i_member: StrMember, i_side: int, i_distance: float, i_offset: float) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddDefExtOnMember(StrMember iMember,
                | CatStrMemberExtremity iSide,
                | double iDistance,
                | double iOffset) As AnyObject
                | 
                |     Creates a member extremity definition object from another member object,
                |     its side, a distance on it and an offset.
                | 
                |     Parameters:
                | 
                |         iMember
                |             The member used to define the extremity 
                |         iSide
                |             The side of the previous member used to define the distance along
                |             the member 
                |         iDistance
                |             The distance along the selected member 
                |         iOffset
                |             The offset on the extremity

        :param StrMember i_member:
        :param int i_side: enum cat_str_member_extremity
        :param float i_distance:
        :param float i_offset:
        :rtype: AnyObject
        """
        return AnyObject(self.str_object_factory.AddDefExtOnMember(i_member.com_object, i_side, i_distance, i_offset))

    def add_dim_member(self,
                       i_section: StrSection,
                       i_anchor_name: str,
                       i_angle: float,
                       i_def_extr1: AnyObject,
                       i_math_direction: tuple,
                       i_length: float,
                       i_type: str) -> StrMember:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddDimMember(StrSection iSection,
                | CATBSTR iAnchorName,
                | double iAngle,
                | AnyObject iDefExtr1,
                | CATSafeArrayVariant iMathDirection,
                | double iLength,
                | CATBSTR iType) As StrMember
                | 
                |     Creates a dimension member object from a point and a mathematical
                |     definition of a direction.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iMathDirection
                |             The mathematical definition of the direction 
                |         iLength
                |             The length of the member 
                |         iType
                |             The type of the member. This type is user defined.

        :param StrSection i_section:
        :param str i_anchor_name:
        :param float i_angle:
        :param AnyObject i_def_extr1:
        :param tuple i_math_direction:
        :param float i_length:
        :param str i_type:
        :rtype: StrMember
        """
        return StrMember(
            self.str_object_factory.AddDimMember(
                i_section.com_object,
                i_anchor_name,
                i_angle,
                i_def_extr1.com_object,
                i_math_direction,
                i_length,
                i_type
            )
        )

    def add_dim_member_on_plane(self,
                                i_section: StrSection,
                                i_anchor_name: str,
                                i_angle: float,
                                i_def_extr1: AnyObject,
                                i_def_extr2: AnyObject,
                                i_direction: tuple,
                                i_mode: int,
                                i_length: float,
                                i_type: str) -> StrMember:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddDimMemberOnPlane(StrSection iSection,
                | CATBSTR iAnchorName,
                | double iAngle,
                | AnyObject iDefExtr1,
                | AnyObject iDefExtr2,
                | CATSafeArrayVariant iDirection,
                | CatStrPlaneMode iMode,
                | double iLength,
                | CATBSTR iType) As StrMember
                | 
                |     Creates a dimension member object on a plane following a mathematical
                |     definition of a plane.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member
                |             
                |         iDirection
                |             The direction object. It can be a line or a plane 
                |         iMode
                |             The way the member is created with respect to the direction plane.
                |             Useless if if the direction is not a plane. 
                |         iOrientation
                |             The orientation of the member 
                |         iLength
                |             The length of the member 
                |         iType
                |             The type of the member. This type is user defined.

        :param StrSection i_section:
        :param str i_anchor_name:
        :param float i_angle:
        :param AnyObject i_def_extr1:
        :param AnyObject i_def_extr2:
        :param tuple i_direction:
        :param int i_mode: enum cat_str_plane_mode
        :param float i_length:
        :param str i_type:
        :rtype: StrMember
        """
        return StrMember(
            self.str_object_factory.AddDimMemberOnPlane(
                i_section.com_object,
                i_anchor_name,
                i_angle,
                i_def_extr1.com_object,
                i_def_extr2.com_object,
                i_direction,
                i_mode,
                i_length,
                i_type
            )
        )

    def add_dim_member_pt_pt(
            self,
            i_section: StrSection,
            i_anchor_name: str,
            i_angle: float,
            i_def_extr1: AnyObject,
            i_def_extr2: AnyObject,
            i_length: float,
            i_type: str) -> StrMember:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddDimMemberPtPt(StrSection iSection,
                | CATBSTR iAnchorName,
                | double iAngle,
                | AnyObject iDefExtr1,
                | AnyObject iDefExtr2,
                | double iLength,
                | CATBSTR iType) As StrMember
                | 
                |     Creates a dimension member object from two given points.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member
                |             
                |         iLength
                |             The length of the member 
                |         iType
                |             The type of the member. This type is user defined.

        :param StrSection i_section:
        :param str i_anchor_name:
        :param float i_angle:
        :param AnyObject i_def_extr1:
        :param AnyObject i_def_extr2:
        :param float i_length:
        :param str i_type:
        :rtype: StrMember
        """
        return StrMember(
            self.str_object_factory.AddDimMemberPtPt(
                i_section.com_object,
                i_anchor_name,
                i_angle,
                i_def_extr1.com_object,
                i_def_extr2.com_object,
                i_length,
                i_type
            )
        )

    def add_dim_member_with_support(
            self,
            i_section: StrSection,
            i_anchor_name: str,
            i_angle: float,
            i_def_extr1: AnyObject,
            i_def_extr2: AnyObject,
            i_direction: Reference,
            i_mode: int,
            i_orientation: int,
            i_length: float,
            i_type: str) -> StrMember:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddDimMemberWithSupport(StrSection iSection,
                | CATBSTR iAnchorName,
                | double iAngle,
                | AnyObject iDefExtr1,
                | AnyObject iDefExtr2,
                | Reference iDirection,
                | CatStrPlaneMode iMode,
                | CatStrMaterialOrientation iOrientation,
                | double iLength,
                | CATBSTR iType) As StrMember
                | 
                |     Creates a dimension member object using a support object.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member. In case
                |             of line for a support, this parameter is not taking into account.
                |             
                |         iDirection
                |             The direction object. It can be a line or a plane 
                |         iMode
                |             The way the member is created with respect to the direction plane.
                |             Useless if if the direction is not a plane. 
                |         iOrientation
                |             The orientation of the member 
                |         iLength
                |             The length of the member 
                |         iType
                |             The type of the member

        :param StrSection i_section:
        :param str i_anchor_name:
        :param float i_angle:
        :param AnyObject i_def_extr1:
        :param AnyObject i_def_extr2:
        :param Reference i_direction:
        :param int i_mode: enum cat_str_plane_mode
        :param int i_orientation: enum cat_str_material_orientation
        :param float i_length:
        :param str i_type:
        :rtype: StrMember
        """
        return StrMember(
            self.str_object_factory.AddDimMemberWithSupport(
                i_section.com_object,
                i_anchor_name,
                i_angle,
                i_def_extr1.com_object,
                i_def_extr2.com_object,
                i_direction.com_object,
                i_mode,
                i_orientation,
                i_length,
                i_type
            )
        )

    def add_member(
            self,
            i_section: StrSection,
            i_anchor_name: str,
            i_angle: float,
            i_def_extr1: AnyObject,
            i_def_extr2: AnyObject,
            i_type: str) -> StrMember:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMember(StrSection iSection,
                | CATBSTR iAnchorName,
                | double iAngle,
                | AnyObject iDefExtr1,
                | AnyObject iDefExtr2,
                | CATBSTR iType) As StrMember
                | 
                |     Creates a member object.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member
                |             
                |         iType
                |             The type of the member. This type is user defined.

        :param StrSection i_section:
        :param str i_anchor_name:
        :param float i_angle:
        :param AnyObject i_def_extr1:
        :param AnyObject i_def_extr2:
        :param str i_type:
        :rtype: StrMember
        """
        return StrMember(
            self.str_object_factory.AddMember(
                i_section.com_object,
                i_anchor_name,
                i_angle,
                i_def_extr1.com_object,
                i_def_extr2.com_object,
                i_type
            )
        )

    def add_member_from_dir(
            self,
            i_section: StrSection,
            i_anchor_name: str,
            i_angle: float,
            i_def_extr1: AnyObject,
            i_def_extr2: AnyObject,
            i_direction: Reference,
            i_mode: int,
            i_type: str) -> StrMember:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberFromDir(StrSection iSection,
                | CATBSTR iAnchorName,
                | double iAngle,
                | AnyObject iDefExtr1,
                | AnyObject iDefExtr2,
                | Reference iDirection,
                | CatStrPlaneMode iMode,
                | CATBSTR iType) As StrMember
                | 
                |     Creates a member object using a direction object as a line or a
                |     plane.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member
                |             
                |         iDirection
                |             The direction object used to orientate the support. The direction
                |             object can be a plane or a line. 
                |         iMode
                |             The way the member is created with respect to the direction plane.
                |             Useless if if the direction is not a plane. 
                |         iType
                |             The type of the member. This type is user defined.

        :param StrSection i_section:
        :param str i_anchor_name:
        :param float i_angle:
        :param AnyObject i_def_extr1:
        :param AnyObject i_def_extr2:
        :param Reference i_direction:
        :param int i_mode: enum cat_str_plane_mode
        :param str i_type:
        :rtype: StrMember
        """
        return StrMember(
            self.str_object_factory.AddMemberFromDir(
                i_section.com_object,
                i_anchor_name,
                i_angle,
                i_def_extr1.com_object,
                i_def_extr2.com_object,
                i_direction.com_object,
                i_mode,
                i_type
            )
        )

    def add_member_from_math_dir(
            self,
            i_section: StrSection,
            i_anchor_name: str,
            i_angle: float,
            i_def_extr1: AnyObject,
            i_def_extr2: AnyObject,
            i_direction: tuple,
            i_type: str) -> StrMember:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberFromMathDir(StrSection iSection,
                | CATBSTR iAnchorName,
                | double iAngle,
                | AnyObject iDefExtr1,
                | AnyObject iDefExtr2,
                | CATSafeArrayVariant iDirection,
                | CATBSTR iType) As StrMember
                | 
                |     Creates a member object using a mathematical definition of the
                |     direction.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member
                |             
                |         iDirection
                |             The mathematical definition of the direction 
                |         iType
                |             The type of the member. This type is user defined.

        :param StrSection i_section:
        :param str i_anchor_name:
        :param float i_angle:
        :param AnyObject i_def_extr1:
        :param AnyObject i_def_extr2:
        :param tuple i_direction:
        :param str i_type:
        :rtype: StrMember
        """
        return StrMember(
            self.str_object_factory.AddMemberFromMathDir(
                i_section.com_object,
                i_anchor_name,
                i_angle,
                i_def_extr1.com_object,
                i_def_extr2.com_object,
                i_direction,
                i_type)
        )

    def add_member_from_math_plane(
            self,
            i_section: StrSection,
            i_anchor_name: str,
            i_angle: float,
            i_def_extr1: AnyObject,
            i_def_extr2: AnyObject,
            i_plane: tuple,
            i_plane_mode: int,
            i_type: str) -> StrMember:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberFromMathPlane(StrSection iSection,
                | CATBSTR iAnchorName,
                | double iAngle,
                | AnyObject iDefExtr1,
                | AnyObject iDefExtr2,
                | CATSafeArrayVariant iPlane,
                | CatStrPlaneMode iPlaneMode,
                | CATBSTR iType) As StrMember
                | 
                |     Creates a member object from a mathematical definition of a
                |     plane.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iDefExtr1
                |             The extremity object defining the start limit of the member
                |             
                |         iDefExtr2
                |             The extremity object defining the end limit of the member
                |             
                |         iDirection
                |             The mathematical definition of a plane 
                |         iPlaneMode
                |             The way the member is created with respect to the direction plane.
                |             Useless if if the direction is not a plane. 
                |         iType
                |             The type of the member. This type is user defined.

        :param StrSection i_section:
        :param str i_anchor_name:
        :param float i_angle:
        :param AnyObject i_def_extr1:
        :param AnyObject i_def_extr2:
        :param tuple i_plane:
        :param int i_plane_mode: enum cat_str_plane_mode
        :param str i_type:
        :rtype: StrMember
        """
        return StrMember(
            self.str_object_factory.AddMemberFromMathPlane(
                i_section.com_object,
                i_anchor_name,
                i_angle,
                i_def_extr1.com_object,
                i_def_extr2.com_object,
                i_plane,
                i_plane_mode,
                i_type
            )
        )

    def add_member_on_support(
            self,
            i_section: StrSection,
            i_anchor_name: str,
            i_angle: float,
            i_support: Reference,
            i_def_extr1: AnyObject,
            i_def_extr2: AnyObject,
            i_type: str) -> StrMember:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberOnSupport(StrSection iSection,
                | CATBSTR iAnchorName,
                | double iAngle,
                | Reference iSupport,
                | AnyObject iDefExtr1,
                | AnyObject iDefExtr2,
                | CATBSTR iType) As StrMember
                | 
                |     Creates a member object on a given support.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iAngle
                |             The orientation of the section on its support 
                |         iSupport
                |             The support for the member. The support can be a line or a curve
                |             
                |         iDefExtr1
                |             The extremity object defining the start limit of the member. It can
                |             be NULL. 
                |         iDefExtr2
                |             The extremity object defining the end limit of the member. It can
                |             be NULL. 
                |         iType
                |             The type of the member. This type is user defined.

        :param StrSection i_section:
        :param str i_anchor_name:
        :param float i_angle:
        :param Reference i_support:
        :param AnyObject i_def_extr1:
        :param AnyObject i_def_extr2:
        :param str i_type:
        :rtype: StrMember
        """
        return StrMember(
            self.str_object_factory.AddMemberOnSupport(
                i_section.com_object,
                i_anchor_name,
                i_angle,
                i_support.com_object,
                i_def_extr1.com_object,
                i_def_extr2.com_object,
                i_type
            )
        )

    def add_member_on_support_with_ref(
            self,
            i_section: StrSection,
            i_anchor_name: str,
            i_surf_ref: Reference,
            i_angle: float,
            i_support: Reference,
            i_def_extr1: AnyObject,
            i_def_extr2: AnyObject,
            i_type: str) -> StrMember:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberOnSupportWithRef(StrSection iSection,
                | CATBSTR iAnchorName,
                | Reference iSurfRef,
                | double iAngle,
                | Reference iSupport,
                | AnyObject iDefExtr1,
                | AnyObject iDefExtr2,
                | CATBSTR iType) As StrMember
                | 
                |     Creates a member object on a given support object and a surface used to
                |     define the orientation of the section. The surface reference defines the
                |     relative orientation on which you add an angle.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section object defining the profile for the member
                |             
                |         iAnchorName
                |             The name of the anchor point 
                |         iReference
                |             The reference to define the zero orientation of the section. The
                |             section follows this guide line along the support of the member.
                |             
                |         iAngle
                |             The orientation of the section on its support 
                |         iSupport
                |             The support for the member. The support can be a line or a curve
                |             
                |         iDefExtr1
                |             The extremity object defining the start limit of the member. It can
                |             be NULL. 
                |         iDefExtr2
                |             The extremity object defining the end limit of the member. It can
                |             be NULL. 
                |         iType
                |             The type of the member. This type is user defined.

        :param StrSection i_section:
        :param str i_anchor_name:
        :param Reference i_surf_ref:
        :param float i_angle:
        :param Reference i_support:
        :param AnyObject i_def_extr1:
        :param AnyObject i_def_extr2:
        :param str i_type:
        :rtype: StrMember
        """
        return StrMember(
            self.str_object_factory.AddMemberOnSupportWithRef(
                i_section.com_object,
                i_anchor_name,
                i_surf_ref.com_object,
                i_angle,
                i_support.com_object,
                i_def_extr1.com_object,
                i_def_extr2.com_object,
                i_type
            )
        )

    def add_plate(
            self,
            i_support: Reference,
            i_thickness: float,
            i_orientation: int,
            i_contour: tuple,
            i_offset: float,
            i_type: str) -> StrPlate:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddPlate(Reference iSupport,
                | double iThickness,
                | CatStrMaterialOrientation iOrientation,
                | CATSafeArrayVariant iContour,
                | double iOffset,
                | CATBSTR iType) As StrPlate
                | 
                |     Creates a plate from a contour defined by coordinates.
                | 
                |     Parameters:
                | 
                |         iSupport
                |             The plane defining the support of the plate 
                |         iThickness
                |             The standard thickness of the plate. The thickness follows the
                |             standard orientation of the support 
                |         iOrientation
                |             The material orientation of the plate 
                |         iContour
                |             The array containing all objects defining the contour of the plate
                |             
                |         iOffset
                |             The offset applies to the support of the plate 
                |         iType
                |             The type of the plate. This information is user defined. It is
                |             added as an attribute on the plate.

        :param Reference i_support:
        :param float i_thickness:
        :param int i_orientation: enum cat_str_material_orientation
        :param tuple i_contour:
        :param float i_offset:
        :param str i_type:
        :rtype: StrPlate
        """
        return StrPlate(
            self.str_object_factory.AddPlate(
                i_support.com_object,
                i_thickness,
                i_orientation,
                i_contour,
                i_offset,
                i_type
            )
        )

    def add_plate_on_surface(
            self,
            i_thickness: float,
            i_orientation: int,
            i_surface: Reference,
            i_offset: float,
            i_type: str) -> StrPlate:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddPlateOnSurface(double iThickness,
                | CatStrMaterialOrientation iOrientation,
                | Reference iSurface,
                | double iOffset,
                | CATBSTR iType) As StrPlate
                | 
                |     Creates a plate from a surface.
                | 
                |     Parameters:
                | 
                |         iThickness
                |             The standard thickness of the plate. The thickness follows the
                |             standard orientation of the support 
                |         iOrientation
                |             The material orientation of the plate 
                |         iSurface
                |             The surface on which plate is to be created. If Surface path is
                |             NULL then method will return E_INVALID_ARG 
                |         iOffset
                |             The offset applies to the support of the plate 
                |         iType
                |             The type of the plate. This information is user defined. It is
                |             added as an attribute on the plate.

        :param float i_thickness:
        :param int i_orientation: enum cat_str_material_orientation
        :param Reference i_surface:
        :param float i_offset:
        :param str i_type:
        :rtype: StrPlate
        """
        return StrPlate(
            self.str_object_factory.AddPlateOnSurface(
                i_thickness,
                i_orientation,
                i_surface.com_object,
                i_offset,
                i_type
            )
        )

    def add_rectangular_end_plate(
            self,
            i_member: StrMember,
            i_side: int,
            i_thickness: float,
            i_height: float,
            i_width: float,
            i_orientation: int,
            i_type: str) -> StrPlate:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddRectangularEndPlate(StrMember iMember,
                | CatStrMemberExtremity iSide,
                | double iThickness,
                | double iHeight,
                | double iWidth,
                | CatStrMaterialOrientation iOrientation,
                | CATBSTR iType) As StrPlate
                | 
                |     Creates a rectangular end plate on an extremity of a given
                |     member.
                | 
                |     Parameters:
                | 
                |         iMember
                |             The member on which the end-plate will be created 
                |         iSide
                |             The side of the selected member 
                |         iThickness
                |             The standard thickness of the plate. The thickness follows the
                |             standard orientation of the support 
                |         iHeight
                |             The height of the plate 
                |         iWidth
                |             The width of the plate 
                |         iOrientation
                |             The material orientation of the plate 
                |         iType
                |             The type of the plate. This information is user defined. It is
                |             added as an attribute on the plate.

        :param StrMember i_member:
        :param int i_side: enum cat_str_member_extremity
        :param float i_thickness:
        :param float i_height:
        :param float i_width:
        :param int i_orientation: enum cat_str_material_orientation
        :param str i_type:
        :rtype: StrPlate
        """
        return StrPlate(
            self.str_object_factory.AddRectangularEndPlate(
                i_member.com_object,
                i_side,
                i_thickness,
                i_height,
                i_width,
                i_orientation,
                i_type
            )
        )

    def add_section(self, i_part: Document) -> StrSection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddSection(Document iPart) As StrSection
                | 
                |     Creates a section object from part document. This part must aggregate a
                |     sketch object defining the contour of the section. The contour of the section
                |     have to be closed and may contain several domains.
                | 
                |     Parameters:
                | 
                |         iPart
                |             The part document where the sketch of the section is
                |             defined

        :param Document i_part:
        :rtype: StrSection
        """
        return StrSection(self.str_object_factory.AddSection(i_part.com_object))

    def add_section_from_catalog(
            self,
            i_part: Document,
            i_catalog_name: str,
            i_family_name: str,
            i_section_name: str) -> StrSection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddSectionFromCatalog(Document iPart,
                | CATBSTR iCatalogName,
                | CATBSTR iFamilyName,
                | CATBSTR iSectionName) As StrSection
                | 
                |     Creates a section object from part document. This part must aggregate a
                |     sketch object defining the contour of the section. This service gives you to
                |     define where the resolved part comes from to allow a replace mechanism. The
                |     contour of the section have to be closed and may contain several
                |     domains.
                | 
                |     Parameters:
                | 
                |         iCatalogName
                |             The catalog name where the document comes from 
                |         iFamilyName
                |             The family name where the document comes from 
                |         iSectionName
                |             The section name where the document comes from 
                |         iPart
                |             The part document where the sketch of the section is
                |             defined

        :param Document i_part:
        :param str i_catalog_name:
        :param str i_family_name:
        :param str i_section_name:
        :rtype: StrSection
        """
        return StrSection(
            self.str_object_factory.AddSectionFromCatalog(
                i_part.com_object,
                i_catalog_name,
                i_family_name,
                i_section_name
            )
        )

    def extend_product_as_foundation(self, i_class: str) -> StrFoundation:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ExtendProductAsFoundation(CATBSTR iClass) As
                | StrFoundation
                | 
                |     Extend an assembly as a structure foundation assembly.
                | 
                |     Parameters:
                | 
                |         iClass
                |             the name of the user class

        :param str i_class:
        :rtype: StrFoundation
        """
        return StrFoundation(self.str_object_factory.ExtendProductAsFoundation(i_class))

    def __repr__(self):
        return f'StrObjectFactory(name="{self.name}")'
