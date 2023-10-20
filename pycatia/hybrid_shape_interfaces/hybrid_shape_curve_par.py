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


class HybridShapeCurvePar(HybridShape):
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
                |                         HybridShapeCurvePar
                | 
                | Represents the hybrid shape curve parameter object.
                | Role: To access the data of the hybrid shape curve parameter object. This data
                | includes:
                | 
                |     The face to process
                |     The offset parameter.
                | 
                | Use the HybridShapeFactory to create a HybridShapeCurvePar
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_curve_par = com_object

    @property
    def curve_offseted(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CurveOffseted() As Reference
                | 
                |     Returns or sets the offset curve of the curve parameter
                |     object.
                |     Sub-element(s) supported (see Boundary object): see TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                | 
                |           This example retrieves the offset curve of
                |          the hybShpCurvePar in offsetCrv.
                |          
                | 
                |          Dim offsetCrv As CATIAReference
                |          offsetCrv = hybShpCurvePar.CurveOffseted

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_curve_par.CurveOffseted)

    @curve_offseted.setter
    def curve_offseted(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_curve_par.CurveOffseted = reference_curve.com_object

    @property
    def curve_par_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CurveParLaw() As Reference
                | 
                |     Returns or sets the offset law.
                | 
                |     Example:
                |         This example retrieves in oLaw the offset law for the hybShpCurvePar
                |         hybrid shape feature.
                | 
                |          Dim oLaw As Reference 
                |          Set oLaw = hybShpCurvePar.CurveParLaw

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_curve_par.CurveParLaw)

    @curve_par_law.setter
    def curve_par_law(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_curve_par.CurveParLaw = value.com_object

    @property
    def curve_par_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CurveParType() As long
                | 
                |     Returns or sets the corner type.
                |     Legal values:
                | 
                |     0
                |         CATGSMCurvePar_Sharp. corner with angle. 
                |     1
                |         CATGSMCurvePar_Round. round corner.
                | 
                | Example:
                |     This example retrieves in oCurveParType the curve par type for the
                |     hybShpCurvePar hybrid shape feature.
                | 
                |      oCurveParType = hybShpCurvePar.CurveParType

        :return: int
        :rtype: int
        """

        return self.hybrid_shape_curve_par.CurveParType

    @curve_par_type.setter
    def curve_par_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_curve_par.CurveParType = value

    @property
    def geodesic(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Geodesic() As boolean
                | 
                |     Returns or sets Geodesic mode.
                |     Legal values: True Geodesic mode and False Euclidian mode
                |     .
                | 
                |     Example:
                | 
                |           This example sets that the geodesic mode of
                |          the hybShpCurvePar hybrid shape curve par feature to
                |          True.
                |          
                | 
                |          hybShpCurvePar.Geodesic = True

        :return: bool
        :rtype: bool
        """

        return self.hybrid_shape_curve_par.Geodesic

    @geodesic.setter
    def geodesic(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_curve_par.Geodesic = value

    @property
    def invert_direction(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InvertDirection() As boolean
                | 
                |     Returns or sets the orientation.
                |     Legal values: True True to invert this orientation and False False means
                |     that there is no invertion of the curve orientation (orientation is the vector
                |     product of the tangent of the curve by the normal on the
                |     support).
                | 
                |     Example:
                | 
                |           This example sets that the orientation of
                |          the hybShpCurvePar hybrid shape curve par feature to
                |          True.
                |          
                | 
                |          hybShpCurvePar.InvertDirection = True

        :return: bool
        :rtype: bool
        """

        return self.hybrid_shape_curve_par.InvertDirection

    @invert_direction.setter
    def invert_direction(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_curve_par.InvertDirection = value

    @property
    def invert_mapping_law(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InvertMappingLaw() As boolean
                | 
                |     Returns or sets the mapping orientation of the law (if offset is specified
                |     by a law).
                |     Legal values: True Law is applied from the end to the beginning of the
                |     curve (mapping is inverted). False Law is applied from the beginning to the end
                |     of the curve (mapping is not inverted).
                | 
                |     Example:
                | 
                |           This example sets that the mapping orientation of
                |          the hybShpCurvePar hybrid shape curve par feature to
                |          True.
                |          
                | 
                |          hybShpCurvePar.InvertMappingLaw = True

        :return: bool
        :rtype: bool
        """

        return self.hybrid_shape_curve_par.InvertMappingLaw

    @invert_mapping_law.setter
    def invert_mapping_law(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_curve_par.InvertMappingLaw = value

    @property
    def keep_both_sides(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property KeepBothSides() As boolean
                | 
                |     Returns or sets the both sides mode of the curve parameter
                |     object.
                | 
                |     Example:
                | 
                |           This example retrieves the both sides mode of
                |          the hybShpCurvePar
                |          
                | 
                |          Dim bothSides As Boolean
                |          bothSides = hybShpCurvePar.KeepBothSides

        :return: bool
        :rtype: bool
        """

        return self.hybrid_shape_curve_par.KeepBothSides

    @keep_both_sides.setter
    def keep_both_sides(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_curve_par.KeepBothSides = value

    @property
    def law_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LawType() As long
                | 
                |     Returns or sets the law type.
                |     Legal values:
                | 
                |     0
                |         CATGSMBasicLawType_None. Undefined law type. 
                |     1
                |         CATGSMBasicLawType_Constant. Constant law type.
                |     2
                |         CATGSMBasicLawType_Linear. Linear law type.
                |     3
                |         CATGSMBasicLawType_SType. S law type.
                |     4
                |         CATGSMBasicLawType_Advanced. Law specified by a GSD law
                |         feature.
                | 
                | Example:
                |     This example retrieves in oLawType the law type for the hybShpCurvePar
                |     hybrid shape feature.
                | 
                |      oLawType = hybShpCurvePar.LawType

        :return: int
        :rtype: int
        """

        return self.hybrid_shape_curve_par.LawType

    @law_type.setter
    def law_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_curve_par.LawType = value

    @property
    def maximum_deviation_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MaximumDeviationValue() As double
                | 
                |     Sets or Gets the maximum deviation allowed for smoothing
                |     operation.
                |     Sets in distance unit, it corresponds to the radius of a pipe around the
                |     input curve in which the result is allowed to be. This value must be set in SI
                |     unit (m).
                | 
                |     Example: This example retrieves in DeviationValue the maximum deviation
                |     value for the CurvePar hybrid shape feature.
                | 
                |      Dim DeviationValue As CATIALength
                |      Set DeviationValue = CurvePar.MaximumDeviationValue

        :return: float
        :rtype: float
        """

        return self.hybrid_shape_curve_par.MaximumDeviationValue

    @maximum_deviation_value.setter
    def maximum_deviation_value(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_curve_par.MaximumDeviationValue = value

    @property
    def offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Offset() As Length (Read Only)
                | 
                |     Returns the offset parameter of the curve parameter
                |     object.
                | 
                |     Example:
                | 
                |           This example retrieves the offset parameter of
                |          the hybShpCurvePar in offsetParm.
                |          
                | 
                |          Dim offsetParm As CATIALength
                |          offsetParm = hybShpCurvePar.Offset

        :return: Length
        :rtype: Length
        """

        return Length(self.hybrid_shape_curve_par.Offset)

    @property
    def offset2(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Offset2() As Length (Read Only)
                | 
                |     Returns the second offset parameter of the curve parameter
                |     object.
                | 
                |     Example:
                | 
                |           This example retrieves the second offset parameter
                |           of
                |          the hybShpCurvePar in offsetParm.
                |          
                | 
                |          Dim offsetParm As CATIALength
                |          offsetParm = hybShpCurvePar.Offset2

        :return: Length
        :rtype: Length
        """

        return Length(self.hybrid_shape_curve_par.Offset2)

    @property
    def other_side(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OtherSide() As Reference (Read Only)
                | 
                |     Returns the other side of parallel curve if both sides mode is
                |     on.
                | 
                |     Example:
                | 
                |           This example retrieves the other side of
                |          the hybShpCurvePar
                |          
                | 
                |          Dim otherSide As CATIAReference
                |          Set otherSide = hybShpCurvePar.OtherSide

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_curve_par.OtherSide)

    @property
    def passing_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PassingPoint() As Reference
                | 
                |     Returns or sets the passing point of the curve parameter
                |     object.
                |     Sub-element(s) supported (see Point object):
                | 
                |     Example:
                | 
                |           This example retrieves the offset curve of
                |          the hybShpCurvePar in offsetCrv.
                |          
                | 
                |          Dim PassingPoint As CATIAReference
                |          offsetCrv = hybShpCurvePar.PassingPoint

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_curve_par.PassingPoint)

    @passing_point.setter
    def passing_point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_curve_par.PassingPoint = reference_point.com_object

    @property
    def smoothing_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothingType() As long
                | 
                |     Returns or sets the smoothing Type.
                |     Smoothing type:
                | 
                |         : 0 -> No Smoothing
                |         : 2 -> G1 Smoothing : Enhance current continuity to tangent continuity
                |         : 3 -> G2 Smoothing : Enhance current continuity to curvature continuity
                | 
                |     Example: This example retrieves in SType the smoothing type for the
                |     CurvePar hybrid shape feature.
                | 
                |      Dim SType As long
                |      Set SType = CurvePar.SmoothingType

        :return: int
        :rtype: int
        """

        return self.hybrid_shape_curve_par.SmoothingType

    @smoothing_type.setter
    def smoothing_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_curve_par.SmoothingType = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or sets the support of the curve..
                | 
                |     Example:
                |         This example retrieves in oElem the support of the curve for the
                |         hybShpCurvePar hybrid shape feature.
                | 
                |          Dim oElem As Reference 
                |          Set oElem = hybShpCurvePar.Support

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_curve_par.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_curve_par.Support = reference_support.com_object

    @property
    def p_3d_smoothing(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property p3DSmoothing() As boolean
                | 
                |     Returns or sets the '3D Smoothing' option. Role: To activate or not the 3D smoothing option
                |     Available only for tangent or curvature smoothing type TRUE : Smoothing performed without
                |     specifying support FALSE : Smoothing performed with specific support
                | 
                |     Example: This example retrieves in 3DSmoothingOption the support for the
                |     Project hybrid shape feature.
                | 
                |      Dim 3DSmoothingOption As boolean
                |      Set 3DSmoothingOption = Project.p3DSmoothing

        :return: bool
        :rtype: bool
        """

        return self.hybrid_shape_curve_par.p3DSmoothing

    @p_3d_smoothing.setter
    def p_3d_smoothing(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_curve_par.p3DSmoothing = value

    def get_plane_normal(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetPlaneNormal(CATSafeArrayVariant oNormal)
                | 
                |     Returns the Normal of the plane created when the Support of the curve is
                |     not specified.
                | 
                |     Parameters:
                | 
                |         oNormal
                |             Plane normal. It is returned as an array of three coordinates in
                |             SafeArrayVariant 
                | 
                |     Example:
                |         This example retrieves in oNormal the normal of the hybShpCurvePar
                |         plane created.
                | 
                |          Dim oNormal(2)
                |          hybShpCurvePar.GetPlaneNormal(oNormal)
                |          
                | 
                |         You can access each normal coordinate as follows:
                | 
                |             x is in oNormal(0)
                |             y is in oNormal(1)
                |             z is in oNormal(2)

        :return: tuple
        :rtype: tuple
        """
        vba_function_name = 'get_plane_normal'
        vba_code = """
        Public Function get_plane_normal(hybrid_shape_curve_par)
            Dim oNormal (2)
            hybrid_shape_curve_par.GetPlaneNormal oNormal
            get_plane_normal = oNormal
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_plane_normal(self, i_normal: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutPlaneNormal(CATSafeArrayVariant iNormal)
                | 
                |     Sets the Normal of the plane created when the Support of the curve is not
                |     specified.
                | 
                |     Parameters:
                | 
                |         iNormal
                |         iNormal[0]
                |             The X Coordinate of the normal vector 
                |         iNormal[1]
                |             The Y Coordinate of the normal vector 
                |         iNormal[2]
                |             The Z Coordinate of the normal vector

        :param tuple i_normal:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_curve_par.PutPlaneNormal(i_normal)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_plane_normal'
        # # vba_code = """
        # # Public Function put_plane_normal(hybrid_shape_curve_par)
        # #     Dim iNormal (2)
        # #     hybrid_shape_curve_par.PutPlaneNormal iNormal
        # #     put_plane_normal = iNormal
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeCurvePar(name="{self.name}")'
