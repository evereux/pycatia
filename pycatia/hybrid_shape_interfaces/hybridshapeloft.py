#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeLoft(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape loft surface feature object.Role: To
                | access the data of the hybrid shape loft surface feature object.This
                | data includes:Use the  CATIAHybridShapeFactory to create a
                | HybridShapeLoft object.Use the  CATIAHybridShapeFactory to create a
                | HybridShapeLoft object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_loft = com_object     

    @property
    def area_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AreaLaw
                | o Property AreaLaw(    ) As
                | 
                | Gets or sets the optional area law for multi-sections
                | element definition. The law is a length law.

        :return:
        """
        return self.hybrid_shape_loft.AreaLaw

    @property
    def area_law_tolerance(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AreaLawTolerance
                | o Property AreaLawTolerance(    ) As
                | 
                | Gets or sets the tolerance applied to area law. The value is
                | in mm.

        :return:
        """
        return self.hybrid_shape_loft.AreaLawTolerance

    @property
    def boolean_operation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BooleanOperation
                | o Property BooleanOperation(    ) As
                | 
                | Gets or sets the boolean operation for closed lofted
                | surface. TO BE USED ONLY for Part Loft (closed loft).
                | BooleanOperation = 1 : No boolean operation. = 2 : Union
                | boolean operation. = 3 : Removal boolean operation. This
                | example retrieves in BoolOp the type of boolean operation
                | for the Loft hybrid shape feature. Dim BoolOp BoolOp =
                | Loft.BooleanOperation

        :return:
        """
        return self.hybrid_shape_loft.BooleanOperation

    @property
    def canonical_detection(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CanonicalDetection
                | o Property CanonicalDetection(    ) As
                | 
                | Returns or sets whether canonical surfaces of the lofted
                | surface are detected. Legal values: 0 No detection of
                | canonical surface is performed 1 Detection of planar
                | surfaces only is performed 2 Detection of canonical surfaces
                | is performed

        :return:
        """
        return self.hybrid_shape_loft.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_loft.CanonicalDetection = value 

    @property
    def comp_end_section_tangent(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CompEndSectionTangent
                | o Property CompEndSectionTangent(    ) As
                | 
                | Returns or sets whether the tangent surface to the end
                | section of the lofted surface is computed. Legal values: 1
                | The tangent to the end section is computed 2 The tangent to
                | the end section is not computed

        :return:
        """
        return self.hybrid_shape_loft.CompEndSectionTangent

    @comp_end_section_tangent.setter
    def comp_end_section_tangent(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_loft.CompEndSectionTangent = value 

    @property
    def comp_start_section_tangent(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CompStartSectionTangent
                | o Property CompStartSectionTangent(    ) As
                | 
                | Returns or sets whether the tangent surface to the start
                | section of the lofted surface is computed. Legal values: 1
                | The tangent to the start section is computed 2 The tangent
                | to the start section is not computed

        :return:
        """
        return self.hybrid_shape_loft.CompStartSectionTangent

    @comp_start_section_tangent.setter
    def comp_start_section_tangent(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_loft.CompStartSectionTangent = value 

    @property
    def context(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Context
                | o Property Context(    ) As
                | 
                | Returns or sets the context on Loft feature. Legal values: 0
                | This option creates Lofted surface. 1 This option creates
                | Lofted volume. Note: Setting volume result requires GSO
                | License. 
                |
                | Example:
                | This example retrieves in oContext the
                | context for the Loft hybrid shape feature. Dim oContext Set
                | oContext = Loft.Context

        :return:
        """
        return self.hybrid_shape_loft.Context

    @context.setter
    def context(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_loft.Context = value 

    @property
    def relimitation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Relimitation
                | o Property Relimitation(    ) As
                | 
                | Returns or sets the relimitation type between sections of
                | the loft. NOT YET IMPLEMENTED. Legal values: 1 The loft will
                | be swept along the spine, then relimited by the start
                | section and the end section 2 The loft will be swept along
                | the spine. If the spine is a user spine, then the loft is
                | limited by the spine extremities If the spine is a computed
                | spine, then the loft is limited: By the start section and
                | the end section, if there is no guide By the guides
                | extremities, if there are guides 3 The loft will be swept
                | along the spine, then relimited by the first section, If the
                | spine is a user spine, then the loft is limited by the spine
                | extremity opposite to the first section If the spine is a
                | computed spine, then the loft is limited: By the last
                | section, if there is no guide By the guides extremities
                | opposite to the first section, if there are guides 4 The
                | loft will be swept along the spine, then relimited by the
                | last section, If the spine is a user spine, then the loft is
                | limited by the spine extremity opposite to the last section
                | If the spine is a computed spine, then the loft is limited:
                | By the first section, if there is no guide By the guides
                | extremities opposite to the last section, if there are
                | guides

        :return:
        """
        return self.hybrid_shape_loft.Relimitation

    @relimitation.setter
    def relimitation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_loft.Relimitation = value 

    @property
    def section_coupling(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SectionCoupling
                | o Property SectionCoupling(    ) As
                | 
                | Returns or sets the type of coupling between sections of the
                | loft. Legal values: 1 The curves will be coupled according
                | to the curvilinear abscissa ratio 2 if each curve has the
                | same number of tangency discontinuity points, then these
                | points will be coupled, otherwise an error message is
                | displayed 3 if each curve has the same number of tangency
                | and curvature discontinuity points, then tangency
                | discontinuity points will be coupled, and after curvature
                | discontinuity points will be coupled, otherwise an error
                | message is displayed 4 if each curve has the same number of
                | vertices, then these points will be coupled, otherwise an
                | error message is displayed

        :return:
        """
        return self.hybrid_shape_loft.SectionCoupling

    @section_coupling.setter
    def section_coupling(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_loft.SectionCoupling = value 

    @property
    def smooth_angle_threshold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SmoothAngleThreshold
                | o Property SmoothAngleThreshold(    ) As
                | 
                | Returns or sets the angular threshold under which
                | discontinuities (moving frame, tangency net on reference
                | surface) will be smoothed.

        :return:
        """
        return self.hybrid_shape_loft.SmoothAngleThreshold

    @smooth_angle_threshold.setter
    def smooth_angle_threshold(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_loft.SmoothAngleThreshold = value 

    @property
    def smooth_angle_threshold_activity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SmoothAngleThresholdActivity
                | o Property SmoothAngleThresholdActivity(    ) As
                | 
                | Returns or sets whether a angular threshold is allowed or
                | not during lofting operation in order to smooth it. Legal
                | values: TRUE The angular threshold value is used during the
                | lofting operation FALSE The angular threshold value is not
                | used during the lofting operation

        :return:
        """
        return self.hybrid_shape_loft.SmoothAngleThresholdActivity

    @smooth_angle_threshold_activity.setter
    def smooth_angle_threshold_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_loft.SmoothAngleThresholdActivity = value 

    @property
    def smooth_deviation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SmoothDeviation
                | o Property SmoothDeviation(    ) As
                | 
                | Returns or sets the deviation value (length) allowed during
                | lofting operation in order to smooth it.

        :return:
        """
        return self.hybrid_shape_loft.SmoothDeviation

    @smooth_deviation.setter
    def smooth_deviation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_loft.SmoothDeviation = value 

    @property
    def smooth_deviation_activity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SmoothDeviationActivity
                | o Property SmoothDeviationActivity(    ) As
                | 
                | Returns or sets whether a deviation is allowed or not during
                | lofting operation in order to smooth it. Legal values: TRUE
                | The deviation value is used during the lofting operation
                | FALSE The deviation value is not used during the lofting
                | operation

        :return:
        """
        return self.hybrid_shape_loft.SmoothDeviationActivity

    @smooth_deviation_activity.setter
    def smooth_deviation_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_loft.SmoothDeviationActivity = value 

    def add_guide(self, i_guide):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddGuide
                | o Sub AddGuide(        iGuide)
                | 
                | Adds a guide curve to the lofted surface.
                |
                | Parameters:
                | iGuide
                |      The guide curve to be added
                | Sub-element(s) supported (see 
                | 
                |  object):  
                |  and 
                | .


        :param i_guide:
        :return:
        """
        return self.hybrid_shape_loft.AddGuide(i_guide)

    def add_guide_with_tangent(self, i_guide, i_tangent):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddGuideWithTangent
                | o Sub AddGuideWithTangent(        iGuide,
                |                                   iTangent)
                | 
                | Adds a guide curve and a tangent surface to the lofted
                | surface.
                |
                | Parameters:
                | iGuide
                |      The guide curve to be added
                | Sub-element(s) supported (see 
                | 
                |  object):  
                |  and 
                | .   
                |      iTangent
                |      The tangent surface to be added.
                |      The guide curve must be layed on the tangent
                | Sub-element(s) supported (see 
                |  object):  
                | .


        :param i_guide:
        :param i_tangent:
        :return:
        """
        return self.hybrid_shape_loft.AddGuideWithTangent(i_guide, i_tangent)

    def add_section_to_loft(self, i_crv, i_ori, i_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddSectionToLoft
                | o Sub AddSectionToLoft(        iCrv,
                |                                iOri,
                |                                iPoint)
                | 
                | Retrieves a loft section.
                |
                | Parameters:
                | iCrv
                |    Reference to the curve
                |  
                |  iOri
                |    Orientation
                |  
                |  iPoint
                |     Reference to the Closing Point


        :param i_crv:
        :param i_ori:
        :param i_point:
        :return:
        """
        return self.hybrid_shape_loft.AddSectionToLoft(i_crv, i_ori, i_point)

    def get_area_law_tolerance_parameter(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAreaLawToleranceParameter
                | o Func GetAreaLawToleranceParameter(    ) As
                | 
                | Gets the tolerance parameter applied to area law.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_loft.GetAreaLawToleranceParameter()

    def get_faces_for_closing(self, o_start_face, o_end_face):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFacesForClosing
                | o Sub GetFacesForClosing(        oStartFace,
                |                                  oEndFace)
                | 
                | Gets start and end faces if the tangent is a computed
                | tangent surface to the start section or end section, from
                | the lofted surface. The section must have been set as a
                | face.
                |
                | Parameters:
                | oStartFace
                |       start face used to close the loft.  
                |    
                |  oEndFace
                |       end face used to close the loft.


        :param o_start_face:
        :param o_end_face:
        :return:
        """
        return self.hybrid_shape_loft.GetFacesForClosing(o_start_face, o_end_face)

    def get_guide(self, i_pos, o_guide, o_guide_tangent):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetGuide
                | o Sub GetGuide(        iPos,
                |                        oGuide,
                |                        oGuideTangent)
                | 
                | Gets informations about the guide at a specified position in
                | the list of the lofted surface.
                |
                | Parameters:
                | iPos
                |       position of the guide in the list where the information is retrieved.
                |    
                |  oGuide
                |       the guide curve.
                |    
                |  oGuideTangent
                |       the tangent corresponding to the guide curve.


        :param i_pos:
        :param o_guide:
        :param o_guide_tangent:
        :return:
        """
        return self.hybrid_shape_loft.GetGuide(i_pos, o_guide, o_guide_tangent)

    def get_nb_of_guides(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbOfGuides
                | o Func GetNbOfGuides(    ) As
                | 
                | Returns the number of guides in the loft object.
                |
                | Parameters:
                | oSize
                |      Number of guides in the loft.

                | Examples:
                | This example retrieves the number of guides in the
                | hybShpLoft hybrid shape Loft. Dim oSize As long oSize =
                | hybShpLoft.GetNbOfGuides

        :return:
        """
        return self.hybrid_shape_loft.GetNbOfGuides()

    def get_section_from_loft(self, i_rank, o_crv, o_ori, o_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSectionFromLoft
                | o Sub GetSectionFromLoft(        iRank,
                |                                  oCrv,
                |                                  oOri,
                |                                  oPoint)
                | 
                | Retrieves a loft section information.
                |
                | Parameters:
                | iRank
                |    The index of the section
                |  
                |  oCrv
                |    The reference to the curve
                |  
                |  oOri
                |    The orientation value
                |  
                |  oPoint
                |    The reference to the point


        :param i_rank:
        :param o_crv:
        :param o_ori:
        :param o_point:
        :return:
        """
        return self.hybrid_shape_loft.GetSectionFromLoft(i_rank, o_crv, o_ori, o_point)

    def get_spine(self, o_spine_type, o_spine):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSpine
                | o Sub GetSpine(        oSpineType,
                |                        oSpine)
                | 
                | Gets the spine of the lofted surface.
                |
                | Parameters:
                | oSpineType
                |       type of spine = 1 : User defined spine.
                |                     = 2 : Automatically computed spine.
                |    
                |  oSpine
                |       curve used as a spine, if the spine is user defined one.


        :param o_spine_type:
        :param o_spine:
        :return:
        """
        return self.hybrid_shape_loft.GetSpine(o_spine_type, o_spine)

    def get_start_and_end_section_tangent(self, o_start_section_tangent, o_end_section_tangent):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetStartAndEndSectionTangent
                | o Sub GetStartAndEndSectionTangent(        oStartSectionTangent,
                |                                            oEndSectionTangent)
                | 
                | Gets the start and end section tangents of the lofted
                | surface.
                |
                | Parameters:
                | oStartSectionTangent
                |       tangent surface at start section.
                |    
                |  oEndSectionTangent
                |       tangent surface at end section.


        :param o_start_section_tangent:
        :param o_end_section_tangent:
        :return:
        """
        return self.hybrid_shape_loft.GetStartAndEndSectionTangent(o_start_section_tangent, o_end_section_tangent)

    def insert_coupling(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | InsertCoupling
                | o Sub InsertCoupling(        iPosition)
                | 
                | Inserts a coupling to the loft.
                |
                | Parameters:
                | iPosition
                |     The position of the coupling in the list of couplings.
                |    If 0 is specified, the coupling is inserted at the end of the list.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | .


        :param i_position:
        :return:
        """
        return self.hybrid_shape_loft.InsertCoupling(i_position)

    def insert_coupling_point(self, i_coupling_index, i_position, i_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | InsertCouplingPoint
                | o Sub InsertCouplingPoint(        iCouplingIndex,
                |                                   iPosition,
                |                                   iPoint)
                | 
                | Inserts a coupling point to a coupling of the lofted
                | surface.
                |
                | Parameters:
                | iCouplingIndex
                |     The index of the coupling in the list of coupling where the point wil be inserted.
                |  
                |  iPosition
                |     The position of the coupling point in the list of coupling points.
                |    If 0 is specified, the coupling point is inserted at the end of the list.
                |  
                |  iPoint
                |    The point to be inserted. The point must be layed on the section with the same position.
                |  Sub-element(s) supported (see 
                | 
                |  object):  ScVertex.


        :param i_coupling_index:
        :param i_position:
        :param i_point:
        :return:
        """
        return self.hybrid_shape_loft.InsertCouplingPoint(i_coupling_index, i_position, i_point)

    def insert_section_to_loft(self, i_type, i_crv, i_ori, i_point, i_section_ref):
        """
        .. note::
            CAA V5 Visual Basic help

                | InsertSectionToLoft
                | o Sub InsertSectionToLoft(        iType,
                |                                   iCrv,
                |                                   iOri,
                |                                   iPoint,
                |                                   iSectionRef)
                | 
                | Inserts a loft section.
                |
                | Parameters:
                | iType
                | 	 iType if set to true section is added After and iType if set to false section is added Before iSectionRef
                |  
                |  iCrv
                |    Reference to the curve
                |  
                |  iOri
                |    Orientation
                |  
                |  iPoint
                |     Reference to the Closing Point 
                |  
                |  iSectionRef
                | 	iSectionRef is the section before and after which section is added.


        :param i_type:
        :param i_crv:
        :param i_ori:
        :param i_point:
        :param i_section_ref:
        :return:
        """
        return self.hybrid_shape_loft.InsertSectionToLoft(i_type, i_crv, i_ori, i_point, i_section_ref)

    def modify_guide_curve(self, i_guide, i_new_guide):
        """
        .. note::
            CAA V5 Visual Basic help

                | ModifyGuideCurve
                | o Sub ModifyGuideCurve(        iGuide,
                |                                iNewGuide)
                | 
                | Modifies the curve of a guide from the lofted surface.
                |
                | Parameters:
                | iGuide
                |       guide curve to be replaced.
                |    
                |  iNewGuide
                |       new guide curve, will replace iGuide.


        :param i_guide:
        :param i_new_guide:
        :return:
        """
        return self.hybrid_shape_loft.ModifyGuideCurve(i_guide, i_new_guide)

    def modify_section_curve(self, i_section, i_new_section, o_curve_section, o_closing_point, o_pt_diag):
        """
        .. note::
            CAA V5 Visual Basic help

                | ModifySectionCurve
                | o Sub ModifySectionCurve(        iSection,
                |                                  iNewSection,
                |                                  oCurveSection,
                |                                  oClosingPoint,
                |                                  oPtDiag)
                | 
                | Modifies the curve of section from the lofted surface.
                |
                | Parameters:
                | iSection
                |       section curve to be replaced.
                |    
                |  iNewSection
                |       section will replace iSection, can be a curve or a face
                |    
                |  oCurveSection
                |       if iSection is a face, oCurveSection is the boundary of the face.
                |       oCurveSection is used as section curve.
                |       if Part design, the face is used to close the Loft.
                |    
                |  oClosingPoint
                |       if iSection is a closed curve, oClosingPoint is a new closing point
                |       of iSection.
                |       if iSection is a face, oClosingPoint is a new closing point the boundary
                |       of iSection.
                |    
                |  oPtDiag
                |       Information on closing point = 0 : No closing point has been created nor retrieved. 
                |                                    = 1 : A closing point has been created as a vertex.
                |                                    = 2 : A closing point has been created as an extremum.
                |                                    = 3 : A closing point has been retrieved as an extremum.


        :param i_section:
        :param i_new_section:
        :param o_curve_section:
        :param o_closing_point:
        :param o_pt_diag:
        :return:
        """
        return self.hybrid_shape_loft.ModifySectionCurve(i_section, i_new_section, o_curve_section, o_closing_point, o_pt_diag)

    def modify_section_orient(self, i_section, i_orient):
        """
        .. note::
            CAA V5 Visual Basic help

                | ModifySectionOrient
                | o Sub ModifySectionOrient(        iSection,
                |                                   iOrient)
                | 
                | Modifies the orientation of the curve of a section from the
                | lofted surface.
                |
                | Parameters:
                | iSection
                |       section curve to be modified.
                |    
                |  iOrient
                |       orientation of the section curve =  1 : same orientation.
                |                                        = -1 : inverted orientation.
                |                                        =  2 : ko orientation.


        :param i_section:
        :param i_orient:
        :return:
        """
        return self.hybrid_shape_loft.ModifySectionOrient(i_section, i_orient)

    def remove_face_for_closing(self, i_section):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveFaceForClosing
                | o Sub RemoveFaceForClosing(        iSection)
                | 
                | Removes face used to close the lofted surface.
                |
                | Parameters:
                | iSection
                |         section curve.


        :param i_section:
        :return:
        """
        return self.hybrid_shape_loft.RemoveFaceForClosing(i_section)

    def remove_guide(self, i_guide):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveGuide
                | o Sub RemoveGuide(        iGuide)
                | 
                | Removes a guide curve from the lofted surface.
                |
                | Parameters:
                | iGuide
                |      The guide curve to be removed
                | Sub-element(s) supported (see 
                | 
                |  object):  
                |  and 
                | .


        :param i_guide:
        :return:
        """
        return self.hybrid_shape_loft.RemoveGuide(i_guide)

    def remove_guide_tangent(self, i_guide):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveGuideTangent
                | o Sub RemoveGuideTangent(        iGuide)
                | 
                | Removes a tangent surface of a guide from the lofted
                | surface.
                |
                | Parameters:
                | iGuide
                |       guide curve of the guide from which the tangent will be removed.


        :param i_guide:
        :return:
        """
        return self.hybrid_shape_loft.RemoveGuideTangent(i_guide)

    def remove_section(self, i_section):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveSection
                | o Sub RemoveSection(        iSection)
                | 
                | Removes a loft section from the lofted surface.
                |
                | Parameters:
                | iSection
                |     The loft section to remove
                | Sub-element(s) supported (see 
                | 
                |  object):  
                |  and 
                | .


        :param i_section:
        :return:
        """
        return self.hybrid_shape_loft.RemoveSection(i_section)

    def remove_section_point(self, i_section):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveSectionPoint
                | o Sub RemoveSectionPoint(        iSection)
                | 
                | Removes a closing point of a section from the lofted
                | surface. The curve section must be closed curve.
                |
                | Parameters:
                | iSection
                |       section curve of the section from which the point will be removed.


        :param i_section:
        :return:
        """
        return self.hybrid_shape_loft.RemoveSectionPoint(i_section)

    def remove_section_tangent(self, i_section):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveSectionTangent
                | o Sub RemoveSectionTangent(        iSection)
                | 
                | Removes the tangent surface of a section from the lofted
                | surface. The section must be the start section or the end
                | section of the loft.
                |
                | Parameters:
                | iSection
                |       section curve of the section from which the tangent will be removed.


        :param i_section:
        :return:
        """
        return self.hybrid_shape_loft.RemoveSectionTangent(i_section)

    def set_end_face_for_closing(self, i_face):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetEndFaceForClosing
                | o Sub SetEndFaceForClosing(        iFace)
                | 
                | Sets a face to the end section from the lofted surface.
                |
                | Parameters:
                | iFace
                |       The face to close the loft (Part design only).
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | .


        :param i_face:
        :return:
        """
        return self.hybrid_shape_loft.SetEndFaceForClosing(i_face)

    def set_end_section_tangent(self, i_tangent_section):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetEndSectionTangent
                | o Sub SetEndSectionTangent(        iTangentSection)
                | 
                | Sets a tangent surface to the end section from the lofted
                | surface.
                |
                | Parameters:
                | iTangentSection
                |      The tangent surface to be added. The end curve section must lay on the surface.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | .


        :param i_tangent_section:
        :return:
        """
        return self.hybrid_shape_loft.SetEndSectionTangent(i_tangent_section)

    def set_spine(self, i_spine):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSpine
                | o Sub SetSpine(        iSpine)
                | 
                | Sets the spine to the lofted surface.
                |
                | Parameters:
                | iSpine
                |      The curve to be added as a spine.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                |  and 
                | .


        :param i_spine:
        :return:
        """
        return self.hybrid_shape_loft.SetSpine(i_spine)

    def set_start_face_for_closing(self, i_face):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetStartFaceForClosing
                | o Sub SetStartFaceForClosing(        iFace)
                | 
                | Sets a face to the start section from the lofted surface.
                |
                | Parameters:
                | iFace
                |       The face to close the loft (Part design only).
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | .


        :param i_face:
        :return:
        """
        return self.hybrid_shape_loft.SetStartFaceForClosing(i_face)

    def set_start_section_tangent(self, i_tangent_section):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetStartSectionTangent
                | o Sub SetStartSectionTangent(        iTangentSection)
                | 
                | Sets a tangent surface to the start section from the lofted
                | surface.
                |
                | Parameters:
                | iTangentSection
                |       The tangent surface to be added. The start curve section must lay on the surface.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | .


        :param i_tangent_section:
        :return:
        """
        return self.hybrid_shape_loft.SetStartSectionTangent(i_tangent_section)

    def __repr__(self):
        return f'HybridShapeLoft()'
