#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_manager import SFMManager
from pycatia.cat_str_functional_interfaces.sfm_member import SFMMember
from pycatia.cat_str_functional_interfaces.sfm_member2_points import SFMMember2Points
from pycatia.cat_str_functional_interfaces.sfm_member_curve import SFMMemberCurve
from pycatia.cat_str_functional_interfaces.sfm_member_plane2_curves import SFMMemberPlane2Curves
from pycatia.cat_str_functional_interfaces.sfm_member_point_length import SFMMemberPointLength
from pycatia.cat_str_functional_interfaces.sfm_member_point_up_to_limit import SFMMemberPointUpToLimit
from pycatia.cat_str_functional_interfaces.sfm_member_surf_surf import SFMMemberSurfSurf
from pycatia.cat_str_functional_interfaces.sfm_stiffener import SFMStiffener
from pycatia.cat_str_functional_interfaces.sfm_stiffener_on_free_edge import SFMStiffenerOnFreeEdge
from pycatia.cat_str_functional_interfaces.sfm_super_plate import SFMSuperPlate
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.factory import Factory


class SFMFactory(Factory):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Factory
                |                         SfmFactory
                | 
                | Interface to create Structure Functional Modeler Objects.
                | Role: To create the structure object such as SuperPlate, Stiffener,
                | StiffenerOnFreeEdge, Beam, Opening and Connection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_factory = com_object

    def add_adv_super_plate(self, i_category: str, i_support: Reference, i_destination: Reference) -> SFMSuperPlate:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddAdvSuperPlate(CATBSTR iCategory,
                | Reference iSupport,
                | Reference iDestination) As SfmSuperPlate
                | 
                |     Creates an advanced SuperPlate.
                |     Role: Allows creating an advanced SuperPlate, ie with the concave limit
                |     mode.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Category. 
                |         iSupport
                |             [in] Support surface. 
                |         iDestination
                |             [in] SuperPlate's destination. 
                |         oSuperPlate
                |             [out] SuperPlate. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmSuperPlate

        :param str i_category:
        :param Reference i_support:
        :param Reference i_destination:
        :rtype: SFMSuperPlate
        """
        return SFMSuperPlate(
            self.sfm_factory.AddAdvSuperPlate(
                i_category,
                i_support.com_object,
                i_destination.com_object
            )
        )

    def add_member_beams_and_plane(
            self, i_category: str,
            i_section_name: str,
            i_member1: SFMMember,
            i_member2: SFMMember,
            i_ref_plane: Reference,
            i_destination: Reference
    ) -> SFMMemberPlane2Curves:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberBeamsAndPlane(CATBSTR iCategory,
                | CATBSTR iSectionName,
                | SfmMember iMember1,
                | SfmMember iMember2,
                | Reference iRefPlane,
                | Reference iDestination) As SfmMemberPlane2Curves
                | 
                |     Creates a Member between two existing members using Plane.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Member's category. 
                |         iSectionName
                |             [in] Name of the section. 
                |         iMember1
                |             [in] First Member. 
                |         iMember1
                |             [in] Second Member. 
                |         iRefPlane
                |             [in] Plane 
                |         iDestination
                |             [in] Member's destination. 
                |         oMember
                |             [out] Member. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         CATIASfmMemberPlane2Members

        :param str i_category:
        :param str i_section_name:
        :param SFMMember i_member1:
        :param SFMMember i_member2:
        :param Reference i_ref_plane:
        :param Reference i_destination:
        :rtype: SFMMemberPlane2Curves
        """
        return SFMMemberPlane2Curves(
            self.sfm_factory.AddMemberBeamsAndPlane(
                i_category,
                i_section_name,
                i_member1.com_object,
                i_member2.com_object,
                i_ref_plane.com_object,
                i_destination.com_object
            )
        )

    def add_member_crv(
            self,
            i_category: str,
            i_section_name: str,
            i_curve: Reference,
            i_destination: Reference
    ) -> SFMMemberCurve:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberCrv(CATBSTR iCategory,
                | CATBSTR iSectionName,
                | Reference iCurve,
                | Reference iDestination) As SfmMemberCurve
                | 
                |     Creates a SuperMember on a curve.
                |     Role: Allows creating a member on a curve.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Member's category. 
                |         iSectionName
                |             [in] Name of the section. 
                |         iCurve
                |             [in] Curve.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): 
                |     iDestination
                |         [in] Member's destination. 
                |     oMember
                |         [out] Member. 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmMemberCurve

        :param str i_category:
        :param str i_section_name:
        :param Reference i_curve:
        :param Reference i_destination:
        :rtype: SFMMemberCurve
        """
        return SFMMemberCurve(
            self.sfm_factory.AddMemberCrv(
                i_category,
                i_section_name,
                i_curve.com_object,
                i_destination.com_object
            )
        )

    def add_member_crv_on_ref(
            self,
            i_category: str,
            i_section_name: str,
            i_curve: Reference,
            i_reference: Reference,
            i_destination: Reference
    ) -> SFMMemberCurve:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberCrvOnRef(CATBSTR iCategory,
                | CATBSTR iSectionName,
                | Reference iCurve,
                | Reference iReference,
                | Reference iDestination) As SfmMemberCurve
                | 
                |     Creates a SuperMember on a curve and on a reference
                |     surface.
                |     Role: Allows creating a member on a curve, perpendicular to a reference
                |     surface.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Member's category. 
                |         iSectionName
                |             [in] Name of the section. 
                |         iCurve
                |             [in] Curve.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): 
                |     iReference
                |         [in] Surface on which the curve must lay down. 
                |     iDestination
                |         [in] Member's destination. 
                |     oMember
                |         [out] Member. 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmMemberCurve

        :param str i_category:
        :param str i_section_name:
        :param Reference i_curve:
        :param Reference i_reference:
        :param Reference i_destination:
        :rtype: SFMMemberCurve
        """
        return SFMMemberCurve(
            self.sfm_factory.AddMemberCrvOnRef(
                i_category,
                i_section_name,
                i_curve.com_object,
                i_reference.com_object,
                i_destination.com_object
            )
        )

    def add_member_pt_length(
            self,
            i_category: str,
            i_section_name: str,
            i_point: Reference,
            i_direction: Reference,
            i_length: float,
            i_destination: Reference
    ) -> SFMMemberPointLength:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberPtLength(CATBSTR iCategory,
                | CATBSTR iSectionName,
                | Reference iPoint,
                | Reference iDirection,
                | double iLength,
                | Reference iDestination) As SfmMemberPointLength
                | 
                |     Creates a straight SuperMember defined by a point, a direction and a
                |     length.
                |     Role: Allows creating a member defined by a point, a direction and a
                |     length.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Member's category. 
                |         iSectionName
                |             [in] Name of the section. 
                |         iPoint
                |             [in] Point. 
                |         iDirection
                |             [in] Direction element: it can be a line or a plane.
                |             
                |         iLength
                |             [in] Length. 
                |         iDestination
                |             [in] Member's destination. 
                |         oMember
                |             [out] Member. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmMemberPointLength

        :param str i_category:
        :param str i_section_name:
        :param Reference i_point:
        :param Reference i_direction:
        :param float i_length:
        :param Reference i_destination:
        :rtype: SFMMemberPointLength
        """
        return SFMMemberPointLength(
            self.sfm_factory.AddMemberPtLength(
                i_category,
                i_section_name,
                i_point.com_object,
                i_direction.com_object,
                i_length,
                i_destination.com_object
            )
        )

    def add_member_pt_on_crv_pt(
            self,
            i_category: str,
            i_section_name: str,
            i_curve1: Reference,
            i_ratio_mode1: bool,
            i_offset1: float,
            i_point2: Reference,
            i_destination: Reference
    ) -> SFMMember2Points:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberPtOnCrvPt(CATBSTR iCategory,
                | CATBSTR iSectionName,
                | Reference iCurve1,
                | boolean iRatioMode1,
                | double iOffset1,
                | Reference iPoint2,
                | Reference iDestination) As SfmMember2Points
                | 
                |     Creates a straight SuperMember between a point on curve and a
                |     point.
                |     Role: Allows creating a member between a point on curve and a
                |     point.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Member's category. 
                |         iSectionName
                |             [in] Name of the section. 
                |         iCurve1
                |             [in] Curve. 
                |         iRatioMode1
                |             [in] If true then Ratio, if false then Length mode for the point on
                |             curve. 
                |         iOffset1
                |             [in] Offset. 
                |         iPoint2
                |             [in] Point. 
                |         iDestination
                |             [in] Member's destination. 
                |         oMember
                |             [out] Member. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmMember2Points

        :param str i_category:
        :param str i_section_name:
        :param Reference i_curve1:
        :param bool i_ratio_mode1:
        :param float i_offset1:
        :param Reference i_point2:
        :param Reference i_destination:
        :rtype: SFMMember2Points
        """
        return SFMMember2Points(
            self.sfm_factory.AddMemberPtOnCrvPt(
                i_category,
                i_section_name,
                i_curve1.com_object,
                i_ratio_mode1,
                i_offset1,
                i_point2.com_object,
                i_destination.com_object
            )
        )

    def add_member_pt_on_crv_pt_on_crv(
            self, i_category: str,
            i_section_name: str,
            i_curve1: Reference,
            i_ratio_mode1: bool,
            i_offset1: float,
            i_curve2: Reference,
            i_ratio_mode2: bool,
            i_offset2: float,
            i_destination: Reference
    ) -> SFMMember2Points:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberPtOnCrvPtOnCrv(CATBSTR iCategory,
                | CATBSTR iSectionName,
                | Reference iCurve1,
                | boolean iRatioMode1,
                | double iOffset1,
                | Reference iCurve2,
                | boolean iRatioMode2,
                | double iOffset2,
                | Reference iDestination) As SfmMember2Points
                | 
                |     Creates a straight SuperMember between two points on
                |     curve.
                |     Role: Allows creating a member between two points on
                |     curve.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Member's category. 
                |         iSectionName
                |             [in] Name of the section. 
                |         iCurve1
                |             [in] Curve. 
                |         iRatioMode1
                |             [in] If true then Ratio, if false then Length mode for the point on
                |             curve. 
                |         iOffset1
                |             [in] Offset. 
                |         iCurve2
                |             [in] Curve. 
                |         iRatioMode2
                |             [in] If true then Ratio, if false then Length mode for the point on
                |             curve. 
                |         iOffset2
                |             [in] Offset. 
                |         iDestination
                |             [in] Member's destination. 
                |         oMember
                |             [out] Member. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmMember2Points

        :param str i_category:
        :param str i_section_name:
        :param Reference i_curve1:
        :param bool i_ratio_mode1:
        :param float i_offset1:
        :param Reference i_curve2:
        :param bool i_ratio_mode2:
        :param float i_offset2:
        :param Reference i_destination:
        :rtype: SFMMember2Points
        """
        return SFMMember2Points(
            self.sfm_factory.AddMemberPtOnCrvPtOnCrv(
                i_category,
                i_section_name,
                i_curve1.com_object,
                i_ratio_mode1,
                i_offset1,
                i_curve2.com_object,
                i_ratio_mode2,
                i_offset2,
                i_destination.com_object
            )
        )

    def add_member_pt_pt(
            self,
            i_category: str,
            i_section_name: str,
            i_point1: Reference,
            i_point2: Reference,
            i_destination: Reference
    ) -> SFMMember2Points:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberPtPt(CATBSTR iCategory,
                | CATBSTR iSectionName,
                | Reference iPoint1,
                | Reference iPoint2,
                | Reference iDestination) As SfmMember2Points
                | 
                |     Creates a straight SuperMember between two points.
                |     Role: Allows creating a member between two points.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Member's category. 
                |         iSectionName
                |             [in] Name of the section. 
                |         iPoint1
                |             [in] Point. 
                |         iPoint2
                |             [in] Point. 
                |         iDestination
                |             [in] Member's destination. 
                |         oMember
                |             [out] Member. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmMember2Points

        :param str i_category:
        :param str i_section_name:
        :param Reference i_point1:
        :param Reference i_point2:
        :param Reference i_destination:
        :rtype: SFMMember2Points
        """
        return SFMMember2Points(
            self.sfm_factory.AddMemberPtPt(
                i_category,
                i_section_name,
                i_point1.com_object,
                i_point2.com_object,
                i_destination.com_object
            )
        )

    def add_member_pt_pt_on_crv(
            self,
            i_category: str,
            i_section_name: str,
            i_point1: Reference,
            i_curve2: Reference,
            i_ratio_mode2: bool,
            i_offset2: float,
            i_destination: Reference
    ) -> SFMMember2Points:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberPtPtOnCrv(CATBSTR iCategory,
                | CATBSTR iSectionName,
                | Reference iPoint1,
                | Reference iCurve2,
                | boolean iRatioMode2,
                | double iOffset2,
                | Reference iDestination) As SfmMember2Points
                | 
                |     Creates a straight SuperMember between a point and a point on
                |     curve.
                |     Role: Allows creating a member between a point and a point on
                |     curve.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Member's category. 
                |         iSectionName
                |             [in] Name of the section. 
                |         iPoint1
                |             [in] Point. 
                |         iCurve2
                |             [in] Curve. 
                |         iRatioMode2
                |             [in] If true then Ratio, if false then Length mode for the point on
                |             curve. 
                |         iOffset2
                |             [in] Offset. 
                |         iDestination
                |             [in] Member's destination. 
                |         oMember
                |             [out] Member. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmMember2Points

        :param str i_category:
        :param str i_section_name:
        :param Reference i_point1:
        :param Reference i_curve2:
        :param bool i_ratio_mode2:
        :param float i_offset2:
        :param Reference i_destination:
        :rtype: SFMMember2Points
        """
        return SFMMember2Points(
            self.sfm_factory.AddMemberPtPtOnCrv(
                i_category,
                i_section_name,
                i_point1.com_object,
                i_curve2.com_object,
                i_ratio_mode2,
                i_offset2,
                i_destination.com_object
            )
        )

    def add_member_pt_up_to_limit(
            self,
            i_category: str,
            i_section_name: str,
            i_point: Reference,
            i_direction: Reference,
            i_limit: Reference,
            i_destination: Reference
    ) -> SFMMemberPointUpToLimit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberPtUpToLimit(CATBSTR iCategory,
                | CATBSTR iSectionName,
                | Reference iPoint,
                | Reference iDirection,
                | Reference iLimit,
                | Reference iDestination) As SfmMemberPointUpToLimit
                | 
                |     Creates a straight member defined by a point, a direction and a
                |     limit.
                |     Role: Allows creating a member defined by a point, a direction and a
                |     limit.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Member's category. 
                |         iSectionName
                |             [in] Name of the section. 
                |         iPoint
                |             [in] Point. 
                |         iDirection
                |             [in] Direction element: it can be a line or a plane.
                |             
                |         iLimit
                |             [in] Limit: it can be any kind of geometric element.
                |             
                |         iDestination
                |             [in] Member's destination. 
                |         oMember
                |             [out] Member. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmMemberPointUpToLimit

        :param str i_category:
        :param str i_section_name:
        :param Reference i_point:
        :param Reference i_direction:
        :param Reference i_limit:
        :param Reference i_destination:
        :rtype: SFMMemberPointUpToLimit
        """
        return SFMMemberPointUpToLimit(
            self.sfm_factory.AddMemberPtUpToLimit(
                i_category,
                i_section_name,
                i_point.com_object,
                i_direction.com_object,
                i_limit.com_object,
                i_destination.com_object
            )
        )

    def add_member_surf_surf(
            self,
            i_category: str,
            i_section_name: str,
            i_surface1: Reference,
            i_surface2: Reference,
            i_destination: Reference
    ) -> SFMMemberSurfSurf:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddMemberSurfSurf(CATBSTR iCategory,
                | CATBSTR iSectionName,
                | Reference iSurface1,
                | Reference iSurface2,
                | Reference iDestination) As SfmMemberSurfSurf
                | 
                |     Creates a SuperMember by the intersection of two surfaces.
                |     Role: Allows creating a member by the intersection of two
                |     surfaces.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Member's category. 
                |         iSectionName
                |             [in] Name of the section. 
                |         iSurface1
                |             [in] First surface. 
                |         iSurface2
                |             [in] Second surface. 
                |         iDestination
                |             [in] Member's destination. 
                |         oMember
                |             [out] Member. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmMemberSurfSurf

        :param str i_category:
        :param str i_section_name:
        :param Reference i_surface1:
        :param Reference i_surface2:
        :param Reference i_destination:
        :rtype: SFMMemberSurfSurf
        """
        return SFMMemberSurfSurf(
            self.sfm_factory.AddMemberSurfSurf(
                i_category,
                i_section_name,
                i_surface1.com_object,
                i_surface2.com_object,
                i_destination.com_object
            )
        )

    def add_super_plate(self, i_category: str, i_support: Reference, i_destination: Reference) -> SFMSuperPlate:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddSuperPlate(CATBSTR iCategory,
                | Reference iSupport,
                | Reference iDestination) As SfmSuperPlate
                | 
                |     Creates a SuperPlate.
                |     Role: Allows creating a SuperPlate in the regular limit mode (split
                |     mode).
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Category. 
                |         iSupport
                |             [in] Support surface. 
                |         iDestination
                |             [in] SuperPlate's destination. 
                |         oSuperPlate
                |             [out] SuperPlate. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmSuperPlate

        :param str i_category:
        :param Reference i_support:
        :param Reference i_destination:
        :rtype: SFMSuperPlate
        """
        return SFMSuperPlate(self.sfm_factory.AddSuperPlate(i_category, i_support.com_object, i_destination.com_object))

    def add_super_stiffener(self, i_category: str, i_section_name: str, i_super_plate: SFMSuperPlate,
                            i_web_support: Reference) -> SFMStiffener:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddSuperStiffener(CATBSTR iCategory,
                | CATBSTR iSectionName,
                | SfmSuperPlate iSuperPlate,
                | Reference iWebSupport) As SfmStiffener
                | 
                |     Creates a SuperStiffener.
                |     Role: Allows creating a SuperStiffener in the normal to plate mode with the
                |     WebSideLeft anchor point.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Category. 
                |         iSectionName
                |             [in] Section name. 
                |         iSuperPlate
                |             [in] SuperPlate to be stiffened. 
                |         oSuperStiffener
                |             [out] SuperStiffener. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmStiffener

        :param str i_category:
        :param str i_section_name:
        :param SFMSuperPlate i_super_plate:
        :param Reference i_web_support:
        :rtype: SFMStiffener
        """
        return SFMStiffener(
            self.sfm_factory.AddSuperStiffener(
                i_category,
                i_section_name,
                i_super_plate.com_object,
                i_web_support.com_object
            )
        )

    def add_super_stiffener_on_free_edge(
            self,
            i_category: str,
            i_section_name: str,
            i_super_plate: SFMSuperPlate,
            i_free_edge: Reference
    ) -> SFMStiffenerOnFreeEdge:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddSuperStiffenerOnFreeEdge(CATBSTR iCategory,
                | CATBSTR iSectionName,
                | SfmSuperPlate iSuperPlate,
                | Reference iFreeEdge) As SfmStiffenerOnFreeEdge
                | 
                |     Creates a SuperStiffener on Free Edge.
                |     Role: Allows creating a SuperStiffener on Free Edge in the normal to plate
                |     mode with the WebSideLeft anchor point.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Category. 
                |         iSectionName
                |             [in] Section name. 
                |         iSuperPlate
                |             [in] SuperPlate to be stiffened. 
                |         iFreeEdge
                |             [in] Support to be used for creating SFE. 
                |         oSuperStiffenerOnFreeEdge
                |             [out] SuperStiffener on free edge. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmStiffenerOnFreeEdge

        :param str i_category:
        :param str i_section_name:
        :param SFMSuperPlate i_super_plate:
        :param Reference i_free_edge:
        :rtype: SFMStiffenerOnFreeEdge
        """
        return SFMStiffenerOnFreeEdge(
            self.sfm_factory.AddSuperStiffenerOnFreeEdge(
                i_category,
                i_section_name,
                i_super_plate.com_object,
                i_free_edge.com_object
            )
        )

    def get_manager(self) -> SFMManager:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetManager() As SfmManager
                | 
                |     Retrieved the services manager.
                |     Role: Allows getting the services manager.
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |     See also:
                |         SfmManager

        :rtype: SFMManager
        """
        return SFMManager(self.sfm_factory.GetManager())

    def __repr__(self):
        return f'SFMFactory(name="{self.name}")'
