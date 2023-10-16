#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape
from pycatia.scripts.vba import vba_nothing


class HybridShapeLoft(HybridShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeLoft
                | 
                | Represents the hybrid shape loft surface feature object.
                | Role: To access the data of the hybrid shape loft surface feature
                | object.
                | This data includes:
                | 
                |     The spine
                |     The tangent surfaces to the start and end sections
                |     Guide curves, sections, and couplings
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeLoft
                | object.
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeLoft
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_loft = com_object

    @property
    def area_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AreaLaw() As Reference
                | 
                |     Gets or sets the optional area law for multi-sections element definition.
                |     The law is a length law.

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_loft.AreaLaw)

    @area_law.setter
    def area_law(self, reference_law: Reference):
        """
        :param Reference reference_law:
        """

        self.hybrid_shape_loft.AreaLaw = reference_law.com_object

    @property
    def area_law_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AreaLawTolerance() As double
                | 
                |     Gets or sets the tolerance applied to area law. The value is in mm.

        :return: float
        :rtype: float
        """

        return self.hybrid_shape_loft.AreaLawTolerance

    @area_law_tolerance.setter
    def area_law_tolerance(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_loft.AreaLawTolerance = value

    @property
    def boolean_operation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BooleanOperation() As long
                | 
                |     Gets or sets the boolean operation for closed lofted surface. TO BE USED ONLY for Part Loft
                |     (closed loft). BooleanOperation = 1 : No boolean operation. = 2 : Union boolean operation. =
                |     3 : Removal boolean operation. This example retrieves in BoolOp the type of boolean operation
                |     for the Loft hybrid shape feature.
                | 
                |      Dim BoolOp
                |      BoolOp = Loft.BooleanOperation

        :return: int
        :rtype: int
        """

        return self.hybrid_shape_loft.BooleanOperation

    @boolean_operation.setter
    def boolean_operation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_loft.BooleanOperation = value

    @property
    def canonical_detection(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CanonicalDetection() As long
                | 
                |     Returns or sets whether canonical surfaces of the lofted surface are
                |     detected.
                |     Legal values:
                | 
                |     0
                |         No detection of canonical surface is performed
                |     1
                |         Detection of planar surfaces only is performed
                |     2
                |         Detection of canonical surfaces is performed

        :return: int
        :rtype: int
        """

        return self.hybrid_shape_loft.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_loft.CanonicalDetection = value

    @property
    def comp_end_section_tangent(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CompEndSectionTangent() As long
                | 
                |     Returns or sets whether the tangent surface to the end section of the
                |     lofted surface is computed.
                |     Legal values:
                | 
                |     1
                |         The tangent to the end section is computed
                |     2
                |         The tangent to the end section is not computed

        :return: int
        :rtype: int
        """

        return self.hybrid_shape_loft.CompEndSectionTangent

    @comp_end_section_tangent.setter
    def comp_end_section_tangent(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_loft.CompEndSectionTangent = value

    @property
    def comp_start_section_tangent(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CompStartSectionTangent() As long
                | 
                |     Returns or sets whether the tangent surface to the start section of the
                |     lofted surface is computed.
                |     Legal values:
                | 
                |     1
                |         The tangent to the start section is computed
                |     2
                |         The tangent to the start section is not computed

        :return: int
        :rtype: int
        """

        return self.hybrid_shape_loft.CompStartSectionTangent

    @comp_start_section_tangent.setter
    def comp_start_section_tangent(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_loft.CompStartSectionTangent = value

    @property
    def context(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Context() As long
                | 
                |     Returns or sets the context on Loft feature.
                |     Legal values:
                | 
                |         0 This option creates Lofted surface.
                |         1 This option creates Lofted volume.
                | 
                | 
                |     Note: Setting volume result requires GSO License.
                | 
                |     Example:
                |         This example retrieves in oContext the context for the Loft hybrid
                |         shape feature.
                | 
                |          Dim oContext
                |          Set oContext = Loft.Context

        :return: int
        :rtype: int
        """

        return self.hybrid_shape_loft.Context

    @context.setter
    def context(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_loft.Context = value

    @property
    def relimitation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Relimitation() As long
                | 
                |     Returns or sets the relimitation type between sections of the
                |     loft.
                |     NOT YET IMPLEMENTED.
                |     Legal values:
                | 
                |     1
                |         The loft will be swept along the spine, then relimited by the start
                |         section and the end section
                |     2
                |         The loft will be swept along the spine.
                | 
                |             If the spine is a user spine, then the loft is limited by the spine
                |             extremities
                |             If the spine is a computed spine, then the loft is
                |             limited:
                |                 By the start section and the end section, if there is no
                |                 guide
                |                 By the guides extremities, if there are guides
                | 
                |     3
                |         The loft will be swept along the spine, then relimited by the first
                |         section,
                | 
                |             If the spine is a user spine, then the loft is limited by the spine
                |             extremity opposite to the first section
                |             If the spine is a computed spine, then the loft is
                |             limited:
                |                 By the last section, if there is no guide
                |                 By the guides extremities opposite to the first section, if
                |                 there are guides
                | 
                |     4
                |         The loft will be swept along the spine, then relimited by the last
                |         section,
                | 
                |             If the spine is a user spine, then the loft is limited by the spine
                |             extremity opposite to the last section
                |             If the spine is a computed spine, then the loft is
                |             limited:
                |                 By the first section, if there is no guide
                |                 By the guides extremities opposite to the last section, if
                |                 there are guides

        :return: int
        :rtype: int
        """

        return self.hybrid_shape_loft.Relimitation

    @relimitation.setter
    def relimitation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_loft.Relimitation = value

    @property
    def section_coupling(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SectionCoupling() As long
                | 
                |     Returns or sets the type of coupling between sections of the
                |     loft.
                |     Legal values:
                | 
                |     1
                |         The curves will be coupled according to the curvilinear abscissa
                |         ratio
                |     2
                |         if each curve has the same number of tangency discontinuity points,
                |         then these points will be coupled, otherwise an error message is
                |         displayed
                |     3
                |         if each curve has the same number of tangency and curvature
                |         discontinuity points, then tangency discontinuity points will be coupled, and
                |         after curvature discontinuity points will be coupled, otherwise an error
                |         message is displayed
                |     4
                |         if each curve has the same number of vertices, then these points will
                |         be coupled, otherwise an error message is displayed

        :return: int
        :rtype: int
        """

        return self.hybrid_shape_loft.SectionCoupling

    @section_coupling.setter
    def section_coupling(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_loft.SectionCoupling = value

    @property
    def smooth_angle_threshold(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothAngleThreshold() As double
                | 
                |     Returns or sets the angular threshold under which discontinuities (moving
                |     frame, tangency net on reference surface) will be smoothed.

        :return: float
        :rtype: float
        """

        return self.hybrid_shape_loft.SmoothAngleThreshold

    @smooth_angle_threshold.setter
    def smooth_angle_threshold(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_loft.SmoothAngleThreshold = value

    @property
    def smooth_angle_threshold_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothAngleThresholdActivity() As boolean
                | 
                |     Returns or sets whether a angular threshold is allowed or not during
                |     lofting operation in order to smooth it.
                |     Legal values:
                | 
                |     TRUE
                |         The angular threshold value is used during the lofting
                |         operation
                |     FALSE
                |         The angular threshold value is not used during the lofting
                |         operation

        :return: bool
        :rtype: bool
        """

        return self.hybrid_shape_loft.SmoothAngleThresholdActivity

    @smooth_angle_threshold_activity.setter
    def smooth_angle_threshold_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_loft.SmoothAngleThresholdActivity = value

    @property
    def smooth_deviation(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothDeviation() As double
                | 
                |     Returns or sets the deviation value (length) allowed during lofting
                |     operation in order to smooth it.

        :return: float
        :rtype: float
        """

        return self.hybrid_shape_loft.SmoothDeviation

    @smooth_deviation.setter
    def smooth_deviation(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_loft.SmoothDeviation = value

    @property
    def smooth_deviation_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothDeviationActivity() As boolean
                | 
                |     Returns or sets whether a deviation is allowed or not during lofting
                |     operation in order to smooth it.
                |     Legal values:
                | 
                |     TRUE
                |         The deviation value is used during the lofting
                |         operation
                |     FALSE
                |         The deviation value is not used during the lofting
                |         operation

        :return: bool
        :rtype: bool
        """

        return self.hybrid_shape_loft.SmoothDeviationActivity

    @smooth_deviation_activity.setter
    def smooth_deviation_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_loft.SmoothDeviationActivity = value

    def add_guide(self, i_guide: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddGuide(Reference iGuide)
                | 
                |     Adds a guide curve to the lofted surface.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             The guide curve to be added
                | 
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): TriDimFeatEdge and BiDimFeatEdge.

        :param Reference i_guide:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.AddGuide(i_guide.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_guide'
        # # vba_code = """
        # # Public Function add_guide(hybrid_shape_loft)
        # #     Dim iGuide (2)
        # #     hybrid_shape_loft.AddGuide iGuide
        # #     add_guide = iGuide
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_guide_with_tangent(self, i_guide: Reference, i_tangent: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddGuideWithTangent(Reference iGuide,
                | Reference iTangent)
                | 
                |     Adds a guide curve and a tangent surface to the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             The guide curve to be added
                | 
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): TriDimFeatEdge and BiDimFeatEdge. 
                |     iTangent
                |         The tangent surface to be added. The guide curve must be layed on the
                |         tangent
                | 
                |         Sub-element(s) supported (see Boundary object): Face.

        :param Reference i_guide:
        :param Reference i_tangent:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.AddGuideWithTangent(i_guide.com_object, i_tangent.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_guide_with_tangent'
        # # vba_code = """
        # # Public Function add_guide_with_tangent(hybrid_shape_loft)
        # #     Dim iGuide (2)
        # #     hybrid_shape_loft.AddGuideWithTangent iGuide
        # #     add_guide_with_tangent = iGuide
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_section_to_loft(
            self,
            i_crv: Reference,
            i_ori: int,
            i_point: Reference or vba_nothing
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddSectionToLoft(Reference iCrv,
                | long iOri,
                | Reference iPoint)
                | 
                |     Retrieves a loft section.
                | 
                |     Parameters:
                | 
                |         iCrv
                |             Reference to the curve 
                |         iOri
                |             Orientation 
                |         iPoint
                |             Reference to the Closing Point

        :param Reference i_crv:
        :param int i_ori:
        :param Reference or vba_nothing i_point:
        :return: None
        :rtype: None
        """

        if i_point:
            i_point = self.application.system_service.evaluate(vba_nothing, 0, 'N', [])
        else:
            i_point = i_point.com_object

        return self.hybrid_shape_loft.AddSectionToLoft(i_crv.com_object, i_ori, i_point)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_section_to_loft'
        # # vba_code = """
        # # Public Function add_section_to_loft(hybrid_shape_loft)
        # #     Dim iCrv (2)
        # #     hybrid_shape_loft.AddSectionToLoft iCrv
        # #     add_section_to_loft = iCrv
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_area_law_tolerance_parameter(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAreaLawToleranceParameter() As Length
                | 
                |     Gets the tolerance parameter applied to area law.

        :return: Length
        :rtype: Length
        """
        return Length(self.hybrid_shape_loft.GetAreaLawToleranceParameter())

    def get_faces_for_closing(self, o_start_face: Reference, o_end_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetFacesForClosing(Reference oStartFace,
                | Reference oEndFace)
                | 
                |     Gets start and end faces if the tangent is a computed tangent surface to
                |     the start section or end section, from the lofted surface. The section must
                |     have been set as a face.
                | 
                |     Parameters:
                | 
                |         oStartFace
                |             start face used to close the loft. 
                |         oEndFace
                |             end face used to close the loft.

        :param Reference o_start_face:
        :param Reference o_end_face:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.GetFacesForClosing(o_start_face.com_object, o_end_face.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_faces_for_closing'
        # # vba_code = """
        # # Public Function get_faces_for_closing(hybrid_shape_loft)
        # #     Dim oStartFace (2)
        # #     hybrid_shape_loft.GetFacesForClosing oStartFace
        # #     get_faces_for_closing = oStartFace
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_guide(self, i_pos: int, o_guide: Reference, o_guide_tangent: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetGuide(long iPos,
                | Reference oGuide,
                | Reference oGuideTangent)
                | 
                |     Gets informations about the guide at a specified position in the list of
                |     the lofted surface.
                | 
                |     Parameters:
                | 
                |         iPos
                |             position of the guide in the list where the information is
                |             retrieved. 
                |         oGuide
                |             the guide curve. 
                |         oGuideTangent
                |             the tangent corresponding to the guide curve.

        :param int i_pos:
        :param Reference o_guide:
        :param Reference o_guide_tangent:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.GetGuide(i_pos, o_guide.com_object, o_guide_tangent.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_guide'
        # # vba_code = """
        # # Public Function get_guide(hybrid_shape_loft)
        # #     Dim iPos (2)
        # #     hybrid_shape_loft.GetGuide iPos
        # #     get_guide = iPos
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_nb_of_guides(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNbOfGuides() As long
                | 
                |     Returns the number of guides in the loft object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of guides in the loft.
                | 
                |             Example:
                |                 This example retrieves the number of guides in the hybShpLoft
                |                 hybrid shape Loft.
                | 
                |                  Dim oSize As  long
                |                  oSize = hybShpLoft.GetNbOfGuides

        :return: int
        :rtype: int
        """
        return self.hybrid_shape_loft.GetNbOfGuides()

    def get_section_from_loft(self, i_rank: int, o_crv: Reference, o_ori: int, o_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSectionFromLoft(long iRank,
                | Reference oCrv,
                | long oOri,
                | Reference oPoint)
                | 
                |     Retrieves a loft section information.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The index of the section 
                |         oCrv
                |             The reference to the curve 
                |         oOri
                |             The orientation value 
                |         oPoint
                |             The reference to the point

        :param int i_rank:
        :param Reference o_crv:
        :param int o_ori:
        :param Reference o_point:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.GetSectionFromLoft(i_rank, o_crv.com_object, o_ori, o_point.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_section_from_loft'
        # # vba_code = """
        # # Public Function get_section_from_loft(hybrid_shape_loft)
        # #     Dim iRank (2)
        # #     hybrid_shape_loft.GetSectionFromLoft iRank
        # #     get_section_from_loft = iRank
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_spine(self, o_spine_type: int, o_spine: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSpine(long oSpineType,
                | Reference oSpine)
                | 
                |     Gets the spine of the lofted surface.
                | 
                |     Parameters:
                | 
                |         oSpineType
                |             type of spine = 1 : User defined spine. = 2 : Automatically computed spine. 
                |         oSpine
                |             curve used as a spine, if the spine is user defined
                |             one.

        :param int o_spine_type:
        :param Reference o_spine:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.GetSpine(o_spine_type, o_spine.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_spine'
        # # vba_code = """
        # # Public Function get_spine(hybrid_shape_loft)
        # #     Dim oSpineType (2)
        # #     hybrid_shape_loft.GetSpine oSpineType
        # #     get_spine = oSpineType
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_start_and_end_section_tangent(self, o_start_section_tangent: Reference,
                                          o_end_section_tangent: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetStartAndEndSectionTangent(Reference
                | oStartSectionTangent,
                | Reference oEndSectionTangent)
                | 
                |     Gets the start and end section tangents of the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         oStartSectionTangent
                |             tangent surface at start section. 
                |         oEndSectionTangent
                |             tangent surface at end section.

        :param Reference o_start_section_tangent:
        :param Reference o_end_section_tangent:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.GetStartAndEndSectionTangent(o_start_section_tangent.com_object,
                                                                   o_end_section_tangent.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_start_and_end_section_tangent'
        # # vba_code = """
        # # Public Function get_start_and_end_section_tangent(hybrid_shape_loft)
        # #     Dim oStartSectionTangent (2)
        # #     hybrid_shape_loft.GetStartAndEndSectionTangent oStartSectionTangent
        # #     get_start_and_end_section_tangent = oStartSectionTangent
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def insert_coupling(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InsertCoupling(long iPosition)
                | 
                |     Inserts a coupling to the loft.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position of the coupling in the list of couplings. If 0 is
                |             specified, the coupling is inserted at the end of the
                |             list.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Vertex.

        :param int i_position:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.InsertCoupling(i_position)

    def insert_coupling_point(self, i_coupling_index: int, i_position: int, i_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InsertCouplingPoint(long iCouplingIndex,
                | long iPosition,
                | Reference iPoint)
                | 
                |     Inserts a coupling point to a coupling of the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         iCouplingIndex
                |             The index of the coupling in the list of coupling where the point
                |             wil be inserted. 
                |         iPosition
                |             The position of the coupling point in the list of coupling points.
                |             If 0 is specified, the coupling point is inserted at the end of the list.
                |             
                |         iPoint
                |             The point to be inserted. The point must be layed on the section
                |             with the same position.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): ScVertex.

        :param int i_coupling_index:
        :param int i_position:
        :param Reference i_point:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.InsertCouplingPoint(i_coupling_index, i_position, i_point.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'insert_coupling_point'
        # # vba_code = """
        # # Public Function insert_coupling_point(hybrid_shape_loft)
        # #     Dim iCouplingIndex (2)
        # #     hybrid_shape_loft.InsertCouplingPoint iCouplingIndex
        # #     insert_coupling_point = iCouplingIndex
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def insert_section_to_loft(self, i_type: bool, i_crv: Reference, i_ori: int, i_point: Reference,
                               i_section_ref: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InsertSectionToLoft(boolean iType,
                | Reference iCrv,
                | long iOri,
                | Reference iPoint,
                | Reference iSectionRef)
                | 
                |     Inserts a loft section.
                | 
                |     Parameters:
                | 
                |         iType
                |             iType if set to true section is added After and iType if set to
                |             false section is added Before iSectionRef 
                |         iCrv
                |             Reference to the curve 
                |         iOri
                |             Orientation 
                |         iPoint
                |             Reference to the Closing Point 
                |         iSectionRef
                |             iSectionRef is the section before and after which section is
                |             added.

        :param bool i_type:
        :param Reference i_crv:
        :param int i_ori:
        :param Reference i_point:
        :param Reference i_section_ref:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.InsertSectionToLoft(i_type, i_crv.com_object, i_ori, i_point.com_object,
                                                          i_section_ref.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'insert_section_to_loft'
        # # vba_code = """
        # # Public Function insert_section_to_loft(hybrid_shape_loft)
        # #     Dim iType (2)
        # #     hybrid_shape_loft.InsertSectionToLoft iType
        # #     insert_section_to_loft = iType
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def modify_guide_curve(self, i_guide: Reference, i_new_guide: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ModifyGuideCurve(Reference iGuide,
                | Reference iNewGuide)
                | 
                |     Modifies the curve of a guide from the lofted surface.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             guide curve to be replaced. 
                |         iNewGuide
                |             new guide curve, will replace iGuide.

        :param Reference i_guide:
        :param Reference i_new_guide:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.ModifyGuideCurve(i_guide.com_object, i_new_guide.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'modify_guide_curve'
        # # vba_code = """
        # # Public Function modify_guide_curve(hybrid_shape_loft)
        # #     Dim iGuide (2)
        # #     hybrid_shape_loft.ModifyGuideCurve iGuide
        # #     modify_guide_curve = iGuide
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def modify_section_curve(self, i_section: Reference, i_new_section: Reference, o_curve_section: Reference,
                             o_closing_point: Reference, o_pt_diag: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ModifySectionCurve(Reference iSection,
                | Reference iNewSection,
                | Reference oCurveSection,
                | Reference oClosingPoint,
                | long oPtDiag)
                | 
                |     Modifies the curve of section from the lofted surface.
                | 
                |     Parameters:
                | 
                |         iSection
                |             section curve to be replaced. 
                |         iNewSection
                |             section will replace iSection, can be a curve or a face
                |             
                |         oCurveSection
                |             if iSection is a face, oCurveSection is the boundary of the face.
                |             oCurveSection is used as section curve. if Part design, the face is used to
                |             close the Loft. 
                |         oClosingPoint
                |             if iSection is a closed curve, oClosingPoint is a new closing point
                |             of iSection. if iSection is a face, oClosingPoint is a new closing point the
                |             boundary of iSection. 
                |         oPtDiag
                |             Information on closing point =
                |             0 : No closing point has been created nor retrieved.
                |             1 : A closing point has been created as a vertex.
                |             2 : A closing point has been created as an extremum.
                |             3 : A closing point has been retrieved as an extremum.

        :param Reference i_section:
        :param Reference i_new_section:
        :param Reference o_curve_section:
        :param Reference o_closing_point:
        :param int o_pt_diag:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.ModifySectionCurve(i_section.com_object, i_new_section.com_object,
                                                         o_curve_section.com_object, o_closing_point.com_object,
                                                         o_pt_diag)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'modify_section_curve'
        # # vba_code = """
        # # Public Function modify_section_curve(hybrid_shape_loft)
        # #     Dim iSection (2)
        # #     hybrid_shape_loft.ModifySectionCurve iSection
        # #     modify_section_curve = iSection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def modify_section_orient(self, i_section: Reference, i_orient: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ModifySectionOrient(Reference iSection,
                | long iOrient)
                | 
                |     Modifies the orientation of the curve of a section from the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         iSection
                |             section curve to be modified. 
                |         iOrient
                |             orientation of the section curve =
                |             1 : same orientation.
                |             -1 : inverted orientation.
                |             2 : ko orientation.

        :param Reference i_section:
        :param int i_orient:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.ModifySectionOrient(i_section.com_object, i_orient)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'modify_section_orient'
        # # vba_code = """
        # # Public Function modify_section_orient(hybrid_shape_loft)
        # #     Dim iSection (2)
        # #     hybrid_shape_loft.ModifySectionOrient iSection
        # #     modify_section_orient = iSection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_face_for_closing(self, i_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveFaceForClosing(Reference iSection)
                | 
                |     Removes face used to close the lofted surface.
                | 
                |     Parameters:
                | 
                |         iSection
                |             section curve.

        :param Reference i_section:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.RemoveFaceForClosing(i_section.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_face_for_closing'
        # # vba_code = """
        # # Public Function remove_face_for_closing(hybrid_shape_loft)
        # #     Dim iSection (2)
        # #     hybrid_shape_loft.RemoveFaceForClosing iSection
        # #     remove_face_for_closing = iSection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_guide(self, i_guide: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveGuide(Reference iGuide)
                | 
                |     Removes a guide curve from the lofted surface.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             The guide curve to be removed
                | 
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): TriDimFeatEdge and BiDimFeatEdge.

        :param Reference i_guide:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.RemoveGuide(i_guide.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_guide'
        # # vba_code = """
        # # Public Function remove_guide(hybrid_shape_loft)
        # #     Dim iGuide (2)
        # #     hybrid_shape_loft.RemoveGuide iGuide
        # #     remove_guide = iGuide
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_guide_tangent(self, i_guide: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveGuideTangent(Reference iGuide)
                | 
                |     Removes a tangent surface of a guide from the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             guide curve of the guide from which the tangent will be
                |             removed.

        :param Reference i_guide:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.RemoveGuideTangent(i_guide.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_guide_tangent'
        # # vba_code = """
        # # Public Function remove_guide_tangent(hybrid_shape_loft)
        # #     Dim iGuide (2)
        # #     hybrid_shape_loft.RemoveGuideTangent iGuide
        # #     remove_guide_tangent = iGuide
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_section(self, i_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveSection(Reference iSection)
                | 
                |     Removes a loft section from the lofted surface.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The loft section to remove
                | 
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): TriDimFeatEdge and BiDimFeatEdge.

        :param Reference i_section:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.RemoveSection(i_section.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_section'
        # # vba_code = """
        # # Public Function remove_section(hybrid_shape_loft)
        # #     Dim iSection (2)
        # #     hybrid_shape_loft.RemoveSection iSection
        # #     remove_section = iSection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_section_point(self, i_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveSectionPoint(Reference iSection)
                | 
                |     Removes a closing point of a section from the lofted surface. The curve
                |     section must be closed curve.
                | 
                |     Parameters:
                | 
                |         iSection
                |             section curve of the section from which the point will be
                |             removed.

        :param Reference i_section:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.RemoveSectionPoint(i_section.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_section_point'
        # # vba_code = """
        # # Public Function remove_section_point(hybrid_shape_loft)
        # #     Dim iSection (2)
        # #     hybrid_shape_loft.RemoveSectionPoint iSection
        # #     remove_section_point = iSection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_section_tangent(self, i_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveSectionTangent(Reference iSection)
                | 
                |     Removes the tangent surface of a section from the lofted surface. The
                |     section must be the start section or the end section of the
                |     loft.
                | 
                |     Parameters:
                | 
                |         iSection
                |             section curve of the section from which the tangent will be
                |             removed.

        :param Reference i_section:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.RemoveSectionTangent(i_section.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_section_tangent'
        # # vba_code = """
        # # Public Function remove_section_tangent(hybrid_shape_loft)
        # #     Dim iSection (2)
        # #     hybrid_shape_loft.RemoveSectionTangent iSection
        # #     remove_section_tangent = iSection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_end_face_for_closing(self, i_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetEndFaceForClosing(Reference iFace)
                | 
                |     Sets a face to the end section from the lofted surface.
                | 
                |     Parameters:
                | 
                |         iFace
                |             The face to close the loft (Part design only).
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Face.

        :param Reference i_face:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.SetEndFaceForClosing(i_face.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_end_face_for_closing'
        # # vba_code = """
        # # Public Function set_end_face_for_closing(hybrid_shape_loft)
        # #     Dim iFace (2)
        # #     hybrid_shape_loft.SetEndFaceForClosing iFace
        # #     set_end_face_for_closing = iFace
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_end_section_tangent(self, i_tangent_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetEndSectionTangent(Reference iTangentSection)
                | 
                |     Sets a tangent surface to the end section from the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         iTangentSection
                |             The tangent surface to be added. The end curve section must lay on
                |             the surface.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Face.

        :param Reference i_tangent_section:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.SetEndSectionTangent(i_tangent_section.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_end_section_tangent'
        # # vba_code = """
        # # Public Function set_end_section_tangent(hybrid_shape_loft)
        # #     Dim iTangentSection (2)
        # #     hybrid_shape_loft.SetEndSectionTangent iTangentSection
        # #     set_end_section_tangent = iTangentSection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_spine(self, i_spine: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSpine(Reference iSpine)
                | 
                |     Sets the spine to the lofted surface.
                | 
                |     Parameters:
                | 
                |         iSpine
                |             The curve to be added as a spine.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): TriDimFeatEdge and BiDimFeatEdge.

        :param Reference i_spine:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.SetSpine(i_spine.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_spine'
        # # vba_code = """
        # # Public Function set_spine(hybrid_shape_loft)
        # #     Dim iSpine (2)
        # #     hybrid_shape_loft.SetSpine iSpine
        # #     set_spine = iSpine
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_start_face_for_closing(self, i_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetStartFaceForClosing(Reference iFace)
                | 
                |     Sets a face to the start section from the lofted surface.
                | 
                |     Parameters:
                | 
                |         iFace
                |             The face to close the loft (Part design only).
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Face.

        :param Reference i_face:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.SetStartFaceForClosing(i_face.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_start_face_for_closing'
        # # vba_code = """
        # # Public Function set_start_face_for_closing(hybrid_shape_loft)
        # #     Dim iFace (2)
        # #     hybrid_shape_loft.SetStartFaceForClosing iFace
        # #     set_start_face_for_closing = iFace
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_start_section_tangent(self, i_tangent_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetStartSectionTangent(Reference iTangentSection)
                | 
                |     Sets a tangent surface to the start section from the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         iTangentSection
                |             The tangent surface to be added. The start curve section must lay
                |             on the surface.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Face.

        :param Reference i_tangent_section:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_loft.SetStartSectionTangent(i_tangent_section.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_start_section_tangent'
        # # vba_code = """
        # # Public Function set_start_section_tangent(hybrid_shape_loft)
        # #     Dim iTangentSection (2)
        # #     hybrid_shape_loft.SetStartSectionTangent iTangentSection
        # #     set_start_section_tangent = iTangentSection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeLoft(name="{self.name}")'
