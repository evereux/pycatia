#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeFilletBiTangent(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Fillet Bi-Tangent feature.Role: Manipulation of Fillet Bi-Tangent
                | feature Allows to access data of the Fillet Bi-Tangent feature created
                | by using two support surfaces, their orientation, a radius, and
                | options (supports trimming and fillet extremities type)

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_fillet_bi_tangent = com_object     

    @property
    def conical_section_parameter(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ConicalSectionParameter
                | o Property ConicalSectionParameter(    ) As
                | 
                | Returns or Sets parameter for conical section.

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.ConicalSectionParameter

    @property
    def first_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstElem
                | o Property FirstElem(    ) As
                | 
                | Returns or Sets the first support surface feature.

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.FirstElem

    @property
    def first_law_relimiter(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstLawRelimiter
                | o Property FirstLawRelimiter(    ) As
                | 
                | Gets or sets Law first relimiter for variable shape fillet
                | with law management. Relimiters must be point on spine. The
                | input law will be mapped between first and second
                | relimiters. This example retrieves in HybLaw the first law
                | relimiter for the Fillet hybrid shape feature. Dim HybLaw As
                | Reference HybLaw = Fillet.FirstLawRelimiter

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.FirstLawRelimiter

    @property
    def first_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstOrientation
                | o Property FirstOrientation(    ) As
                | 
                | Returns or Setsthe first orientation used to specify fillet
                | center position. Orientation is same or inverse than the
                | normal to the first surface support

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.FirstOrientation

    @property
    def hold_curve(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HoldCurve
                | o Property HoldCurve(    ) As
                | 
                | Returns or Sets the Hold Curve feature.

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.HoldCurve

    @property
    def integrated_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IntegratedLaw
                | o Property IntegratedLaw(    ) As
                | 
                | Gets or sets Integrated Law to manage Variable Shape Fillet
                | with law.

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.IntegratedLaw

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Radius
                | o Property Radius(    ) As   (Read Only)
                | 
                | Returns fillet radius in a CATIALength.

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.Radius

    @property
    def radius_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RadiusType
                | o Property RadiusType(    ) As
                | 
                | Returns or Sets fillet radius type. Fillet radius type : -
                | CATGSMRadiusDefault (0) - CATGSMRadiusChordLength(1)

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.RadiusType

    @property
    def radius_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RadiusValue
                | o Property RadiusValue(    ) As
                | 
                | Returns or Sets fillet radius value.

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.RadiusValue

    @property
    def ribbon_relimitation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RibbonRelimitationMode
                | o Property RibbonRelimitationMode(    ) As
                | 
                | Returns or Sets fillet ribbon relimitation mode (or fillet
                | extremities mode). Fillet extremities mode : - CATGSMSmooth
                | (0) - CATGSMStraight(1) - CATGSMMaximum (2) - CATGSMMinimum
                | (3)

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.RibbonRelimitationMode

    @property
    def second_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondElem
                | o Property SecondElem(    ) As
                | 
                | Returns or sets the Second support surface feature.

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.SecondElem

    @second_elem.setter
    def second_elem(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fillet_bi_tangent.SecondElem = value 

    @property
    def second_law_relimiter(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondLawRelimiter
                | o Property SecondLawRelimiter(    ) As
                | 
                | Gets or sets Law second relimiter for variable shape fillet
                | with law management. Relimiters must be point on spine. The
                | input law will be mapped between first and second
                | relimiters. This example retrieves in HybLaw the second law
                | relimiter for the Fillet hybrid shape feature. Dim HybLaw As
                | Reference HybLaw = Fillet.SecondLawRelimiter

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.SecondLawRelimiter

    @property
    def second_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondOrientation
                | o Property SecondOrientation(    ) As
                | 
                | Returns or Sets the Second orientation used to specify
                | fillet center position. Orientation is same or inverse than
                | the normal to the Second surface support

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.SecondOrientation

    @property
    def section_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SectionType
                | o Property SectionType(    ) As
                | 
                | Returns or Sets fillet section type. Fillet radius type : -
                | CATGSMCircularSection(0) - CATGSMConicalSection (1)

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.SectionType

    @property
    def spine(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Spine
                | o Property Spine(    ) As
                | 
                | Returns or Sets the spine feature.

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.Spine

    @property
    def supports_trim_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SupportsTrimMode
                | o Property SupportsTrimMode(    ) As
                | 
                | Returns or Sets whether support surfaces are trimmed or not.
                | Possible values of SupportsTrimMode = 0 : No trim of fillet
                | supports. = 1 : Trim of both fillet supports. = 2 : Trim of
                | fillet support 1. = 3 : Trim of fillet support 2.

        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.SupportsTrimMode

    def append_new_face_to_keep(self, i_face):
        """
        .. note::
            CAA V5 Visual Basic help

                | AppendNewFaceToKeep
                | o Sub AppendNewFaceToKeep(        iFace)
                | 
                | Append a new face to keep.
                |
                | Parameters:
                | iFace


        :param i_face:
        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.AppendNewFaceToKeep(i_face)

    def get_face_to_keep(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFaceToKeep
                | o Func GetFaceToKeep(        iPos) As
                | 
                | Gets the face to keep for fillet operation.
                |
                | Parameters:
                | oFace
                |       The face to keep for fillet operation.
                |    
                |  iPos
                |       Position of the face to be retrieved.


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.GetFaceToKeep(i_pos)

    def invert_first_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertFirstOrientation
                | o Sub InvertFirstOrientation(    )
                | 
                | Inverts first orientation used to specify fillet center
                | position.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.InvertFirstOrientation()

    def invert_second_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertSecondOrientation
                | o Sub InvertSecondOrientation(    )
                | 
                | Inverts second orientation used to specify fillet center
                | position.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.InvertSecondOrientation()

    def remove_all_faces_to_keep(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAllFacesToKeep
                | o Sub RemoveAllFacesToKeep(    )
                | 
                | Remove all the faces to keep.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.RemoveAllFacesToKeep()

    def remove_face_to_keep(self, i_face):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveFaceToKeep
                | o Sub RemoveFaceToKeep(        iFace)
                | 
                | Remove a face to keep.
                |
                | Parameters:
                | iFace


        :param i_face:
        :return:
        """
        return self.hybrid_shape_fillet_bi_tangent.RemoveFaceToKeep(i_face)

    def __repr__(self):
        return f'HybridShapeFilletBiTangent()'
