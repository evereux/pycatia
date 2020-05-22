#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeCurvePar(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape curve parameter object.Role: To access the
                | data of the hybrid shape curve parameter object. This data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_curve_par = com_object     

    @property
    def curve_offseted(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CurveOffseted
                | o Property CurveOffseted(    ) As
                | 
                | Returns or sets the offset curve of the curve parameter
                | object. Sub-element(s) supported (see object): see or .
                | 
                |
                | Example:
                | This example retrieves the offset curve of the
                | hybShpCurvePar in offsetCrv. Dim offsetCrv As CATIAReference
                | offsetCrv = hybShpCurvePar.CurveOffseted

        :return:
        """
        return self.hybrid_shape_curve_par.CurveOffseted

    @curve_offseted.setter
    def curve_offseted(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_par.CurveOffseted = value 

    @property
    def curve_par_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CurveParLaw
                | o Property CurveParLaw(    ) As
                | 
                | Returns or sets the offset law. 
                |
                | Example:
                | This example
                | retrieves in oLaw the offset law for the hybShpCurvePar
                | hybrid shape feature. Dim oLaw As Reference Set oLaw =
                | hybShpCurvePar.CurveParLaw

        :return:
        """
        return self.hybrid_shape_curve_par.CurveParLaw

    @curve_par_law.setter
    def curve_par_law(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_par.CurveParLaw = value 

    @property
    def curve_par_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CurveParType
                | o Property CurveParType(    ) As
                | 
                | Returns or sets the corner type. Legal values: 0
                | CATGSMCurvePar_Sharp. corner with angle. 1
                | CATGSMCurvePar_Round. round corner.

        :return:
        """
        return self.hybrid_shape_curve_par.CurveParType

    @curve_par_type.setter
    def curve_par_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_par.CurveParType = value 

    @property
    def geodesic(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Geodesic
                | o Property Geodesic(    ) As
                | 
                | Returns or sets Geodesic mode. Legal values: True Geodesic
                | mode and False Euclidian mode . 
                |
                | Example:
                | This example sets
                | that the geodesic mode of the hybShpCurvePar hybrid shape
                | curve par feature to True. hybShpCurvePar.Geodesic = True

        :return:
        """
        return self.hybrid_shape_curve_par.Geodesic

    @geodesic.setter
    def geodesic(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_par.Geodesic = value 

    @property
    def invert_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertDirection
                | o Property InvertDirection(    ) As
                | 
                | Returns or sets the orientation. Legal values: True True to
                | invert this orientation and False False means that there is
                | no invertion of the curve orientation (orientation is the
                | vector product of the tangent of the curve by the normal on
                | the support). 
                |
                | Example:
                | This example sets that the
                | orientation of the hybShpCurvePar hybrid shape curve par
                | feature to True. hybShpCurvePar.InvertDirection = True

        :return:
        """
        return self.hybrid_shape_curve_par.InvertDirection

    @invert_direction.setter
    def invert_direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_par.InvertDirection = value 

    @property
    def invert_mapping_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertMappingLaw
                | o Property InvertMappingLaw(    ) As
                | 
                | Returns or sets the mapping orientation of the law (if
                | offset is specified by a law). Legal values: True Law is
                | applied from the end to the beginning of the curve (mapping
                | is inverted). False Law is applied from the beginning to the
                | end of the curve (mapping is not inverted). 
                |
                | Example:
                | This
                | example sets that the mapping orientation of the
                | hybShpCurvePar hybrid shape curve par feature to True.
                | hybShpCurvePar.InvertMappingLaw = True

        :return:
        """
        return self.hybrid_shape_curve_par.InvertMappingLaw

    @invert_mapping_law.setter
    def invert_mapping_law(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_par.InvertMappingLaw = value 

    @property
    def keep_both_sides(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | KeepBothSides
                | o Property KeepBothSides(    ) As
                | 
                | Returns or sets the both sides mode of the curve parameter
                | object. 
                |
                | Example:
                | This example retrieves the both sides mode
                | of the hybShpCurvePar Dim bothSides As Boolean bothSides =
                | hybShpCurvePar.KeepBothSides

        :return:
        """
        return self.hybrid_shape_curve_par.KeepBothSides

    @keep_both_sides.setter
    def keep_both_sides(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_par.KeepBothSides = value 

    @property
    def law_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | LawType
                | o Property LawType(    ) As
                | 
                | Returns or sets the law type. Legal values: 0
                | CATGSMBasicLawType_None. Undefined law type. 1
                | CATGSMBasicLawType_Constant. Constant law type. 2
                | CATGSMBasicLawType_Linear. Linear law type. 3
                | CATGSMBasicLawType_SType. S law type. 4
                | CATGSMBasicLawType_Advanced. Law specified by a GSD law
                | feature.

        :return:
        """
        return self.hybrid_shape_curve_par.LawType

    @law_type.setter
    def law_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_par.LawType = value 

    @property
    def maximum_deviation_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | MaximumDeviationValue
                | o Property MaximumDeviationValue(    ) As
                | 
                | Sets or Gets the maximum deviation allowed for smoothing
                | operation. Sets in distance unit, it corresponds to the
                | radius of a pipe around the input curve in which the result
                | is allowed to be. This value must be set in SI unit (m).
                | 
                |
                | Example:
                | This example retrieves in DeviationValue the
                | maximum deviation value for the CurvePar hybrid shape
                | feature. Dim DeviationValue As CATIALength Set
                | DeviationValue = CurvePar.MaximumDeviationValue

        :return:
        """
        return self.hybrid_shape_curve_par.MaximumDeviationValue

    @property
    def offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Offset
                | o Property Offset(    ) As   (Read Only)
                | 
                | Returns the offset parameter of the curve parameter object.
                | 
                |
                | Example:
                | This example retrieves the offset parameter of the
                | hybShpCurvePar in offsetParm. Dim offsetParm As CATIALength
                | offsetParm = hybShpCurvePar.Offset

        :return:
        """
        return self.hybrid_shape_curve_par.Offset

    @property
    def offset2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Offset2
                | o Property Offset2(    ) As   (Read Only)
                | 
                | Returns the second offset parameter of the curve parameter
                | object. 
                |
                | Example:
                | This example retrieves the second offset
                | parameter of the hybShpCurvePar in offsetParm. Dim
                | offsetParm As CATIALength offsetParm =
                | hybShpCurvePar.Offset2

        :return:
        """
        return self.hybrid_shape_curve_par.Offset2

    @property
    def other_side(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OtherSide
                | o Property OtherSide(    ) As   (Read Only)
                | 
                | Returns the other side of parallel curve if both sides mode
                | is on. 
                |
                | Example:
                | This example retrieves the other side of the
                | hybShpCurvePar Dim otherSide As CATIAReference Set otherSide
                | = hybShpCurvePar.OtherSide

        :return:
        """
        return self.hybrid_shape_curve_par.OtherSide

    @property
    def passing_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PassingPoint
                | o Property PassingPoint(    ) As
                | 
                | Returns or sets the passing point of the curve parameter
                | object. Sub-element(s) supported (see object): 
                |
                | Example:
                | This
                | example retrieves the offset curve of the hybShpCurvePar in
                | offsetCrv. Dim PassingPoint As CATIAReference offsetCrv =
                | hybShpCurvePar.PassingPoint

        :return:
        """
        return self.hybrid_shape_curve_par.PassingPoint

    @passing_point.setter
    def passing_point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_par.PassingPoint = value 

    @property
    def smoothing_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SmoothingType
                | o Property SmoothingType(    ) As
                | 
                | Returns or sets the smoothing Type. Smoothing type: : 0 ->
                | No Smoothing : 2 -> G1 Smoothing : Enhance current
                | continuity to tangent continuity : 3 -> G2 Smoothing :
                | Enhance current continuity to curvature continuity Example:
                | This example retrieves in SType the smoothing type for the
                | CurvePar hybrid shape feature. Dim SType As long Set SType =
                | CurvePar.SmoothingType

        :return:
        """
        return self.hybrid_shape_curve_par.SmoothingType

    @smoothing_type.setter
    def smoothing_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_par.SmoothingType = value 

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets the support of the curve.. 
                |
                | Example:
                | This
                | example retrieves in oElem the support of the curve for the
                | hybShpCurvePar hybrid shape feature. Dim oElem As Reference
                | Set oElem = hybShpCurvePar.Support

        :return:
        """
        return self.hybrid_shape_curve_par.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_par.Support = value 

    @property
    def p_3d_smoothing(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | p3DSmoothing
                | o Property p3DSmoothing(    ) As
                | 
                | Returns or sets the '3D Smoothing' option. Role: To activate
                | or not the 3D smoothing option Available only for tangent or
                | curvature smoothing type TRUE : Smoothing performed without
                | specifying support FALSE : Smoothing performed with specific
                | support 
                |
                | Example:
                | This example retrieves in 3DSmoothingOption
                | the support for the Project hybrid shape feature. Dim
                | 3DSmoothingOption As boolean Set 3DSmoothingOption =
                | Project.p3DSmoothing

        :return:
        """
        return self.hybrid_shape_curve_par.p3DSmoothing

    @p_3d_smoothing.setter
    def p_3d_smoothing(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_par.p3DSmoothing = value 

    def get_plane_normal(self, o_normal):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPlaneNormal
                | o Sub GetPlaneNormal(        oNormal)
                | 
                | Returns the Normal of the plane created when the Support of
                | the curve is not specified.
                |
                | Parameters:
                | oNormal
                |     Plane normal. It is returned as an array of three coordinates in SafeArrayVariant

                | Examples:
                | This example retrieves in oNormal the normal of the
                | hybShpCurvePar plane created. Dim oNormal(2)
                | hybShpCurvePar.GetPlaneNormal(oNormal) You can access each
                | normal coordinate as follows: x is in oNormal(0) y is in
                | oNormal(1) z is in oNormal(2)

        :param o_normal:
        :return:
        """
        return self.hybrid_shape_curve_par.GetPlaneNormal(o_normal)

    def put_plane_normal(self, i_normal):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutPlaneNormal
                | o Sub PutPlaneNormal(        iNormal)
                | 
                | Sets the Normal of the plane created when the Support of the
                | curve is not specified.
                |
                | Parameters:
                | iNormal
                |  
                |  iNormal[0]
                |    The X Coordinate of the normal vector 
                |    
                |  iNormal[1]
                |    The Y Coordinate of the normal vector
                |    
                |  iNormal[2]
                |    The Z Coordinate of the normal vector


        :param i_normal:
        :return:
        """
        return self.hybrid_shape_curve_par.PutPlaneNormal(i_normal)

    def __repr__(self):
        return f'HybridShapeCurvePar()'
