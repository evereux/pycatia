#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_3d_curve_offset import HybridShape3DCurveOffset
from pycatia.hybrid_shape_interfaces.hybrid_shape_affinity import HybridShapeAffinity
from pycatia.hybrid_shape_interfaces.hybrid_shape_assemble import HybridShapeAssemble
from pycatia.hybrid_shape_interfaces.hybrid_shape_axis_line import HybridShapeAxisLine
from pycatia.hybrid_shape_interfaces.hybrid_shape_axis_to_axis import HybridShapeAxisToAxis
from pycatia.hybrid_shape_interfaces.hybrid_shape_blend import HybridShapeBlend
from pycatia.hybrid_shape_interfaces.hybrid_shape_boundary import HybridShapeBoundary
from pycatia.hybrid_shape_interfaces.hybrid_shape_bump import HybridShapeBump
from pycatia.hybrid_shape_interfaces.hybrid_shape_circle2_points_rad import HybridShapeCircle2PointsRad
from pycatia.hybrid_shape_interfaces.hybrid_shape_circle3_points import HybridShapeCircle3Points
from pycatia.hybrid_shape_interfaces.hybrid_shape_circle_bitangent_point import HybridShapeCircleBitangentPoint
from pycatia.hybrid_shape_interfaces.hybrid_shape_circle_bitangent_radius import HybridShapeCircleBitangentRadius
from pycatia.hybrid_shape_interfaces.hybrid_shape_circle_center_axis import HybridShapeCircleCenterAxis
from pycatia.hybrid_shape_interfaces.hybrid_shape_circle_center_tangent import HybridShapeCircleCenterTangent
from pycatia.hybrid_shape_interfaces.hybrid_shape_circle_ctr_pt import HybridShapeCircleCtrPt
from pycatia.hybrid_shape_interfaces.hybrid_shape_circle_ctr_rad import HybridShapeCircleCtrRad
from pycatia.hybrid_shape_interfaces.hybrid_shape_circle_explicit import HybridShapeCircleExplicit
from pycatia.hybrid_shape_interfaces.hybrid_shape_circle_tritangent import HybridShapeCircleTritangent
from pycatia.hybrid_shape_interfaces.hybrid_shape_combine import HybridShapeCombine
from pycatia.hybrid_shape_interfaces.hybrid_shape_conic import HybridShapeConic
from pycatia.hybrid_shape_interfaces.hybrid_shape_connect import HybridShapeConnect
from pycatia.hybrid_shape_interfaces.hybrid_shape_corner import HybridShapeCorner
from pycatia.hybrid_shape_interfaces.hybrid_shape_curve_explicit import HybridShapeCurveExplicit
from pycatia.hybrid_shape_interfaces.hybrid_shape_curve_par import HybridShapeCurvePar
from pycatia.hybrid_shape_interfaces.hybrid_shape_curve_smooth import HybridShapeCurveSmooth
from pycatia.hybrid_shape_interfaces.hybrid_shape_cylinder import HybridShapeCylinder
from pycatia.hybrid_shape_interfaces.hybrid_shape_develop import HybridShapeDevelop
from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.hybrid_shape_interfaces.hybrid_shape_extract import HybridShapeExtract
from pycatia.hybrid_shape_interfaces.hybrid_shape_extract_multi import HybridShapeExtractMulti
from pycatia.hybrid_shape_interfaces.hybrid_shape_extrapol import HybridShapeExtrapol
from pycatia.hybrid_shape_interfaces.hybrid_shape_extremum import HybridShapeExtremum
from pycatia.hybrid_shape_interfaces.hybrid_shape_extremum_polar import HybridShapeExtremumPolar
from pycatia.hybrid_shape_interfaces.hybrid_shape_extrude import HybridShapeExtrude
from pycatia.hybrid_shape_interfaces.hybrid_shape_fill import HybridShapeFill
from pycatia.hybrid_shape_interfaces.hybrid_shape_fillet_bi_tangent import HybridShapeFilletBiTangent
from pycatia.hybrid_shape_interfaces.hybrid_shape_fillet_tri_tangent import HybridShapeFilletTriTangent
from pycatia.hybrid_shape_interfaces.hybrid_shape_healing import HybridShapeHealing
from pycatia.hybrid_shape_interfaces.hybrid_shape_helix import HybridShapeHelix
from pycatia.hybrid_shape_interfaces.hybrid_shape_integrated_law import HybridShapeIntegratedLaw
from pycatia.hybrid_shape_interfaces.hybrid_shape_intersection import HybridShapeIntersection
from pycatia.hybrid_shape_interfaces.hybrid_shape_inverse import HybridShapeInverse
from pycatia.hybrid_shape_interfaces.hybrid_shape_law_dist_proj import HybridShapeLawDistProj
from pycatia.hybrid_shape_interfaces.hybrid_shape_line_angle import HybridShapeLineAngle
from pycatia.hybrid_shape_interfaces.hybrid_shape_line_bi_tangent import HybridShapeLineBiTangent
from pycatia.hybrid_shape_interfaces.hybrid_shape_line_bisecting import HybridShapeLineBisecting
from pycatia.hybrid_shape_interfaces.hybrid_shape_line_explicit import HybridShapeLineExplicit
from pycatia.hybrid_shape_interfaces.hybrid_shape_line_normal import HybridShapeLineNormal
from pycatia.hybrid_shape_interfaces.hybrid_shape_line_pt_dir import HybridShapeLinePtDir
from pycatia.hybrid_shape_interfaces.hybrid_shape_line_pt_pt import HybridShapeLinePtPt
from pycatia.hybrid_shape_interfaces.hybrid_shape_line_tangency import HybridShapeLineTangency
from pycatia.hybrid_shape_interfaces.hybrid_shape_loft import HybridShapeLoft
from pycatia.hybrid_shape_interfaces.hybrid_shape_mid_surface import HybridShapeMidSurface
from pycatia.hybrid_shape_interfaces.hybrid_shape_near import HybridShapeNear
from pycatia.hybrid_shape_interfaces.hybrid_shape_offset import HybridShapeOffset
from pycatia.hybrid_shape_interfaces.hybrid_shape_plane1_curve import HybridShapePlane1Curve
from pycatia.hybrid_shape_interfaces.hybrid_shape_plane1_line1_pt import HybridShapePlane1Line1Pt
from pycatia.hybrid_shape_interfaces.hybrid_shape_plane2_lines import HybridShapePlane2Lines
from pycatia.hybrid_shape_interfaces.hybrid_shape_plane3_points import HybridShapePlane3Points
from pycatia.hybrid_shape_interfaces.hybrid_shape_plane_angle import HybridShapePlaneAngle
from pycatia.hybrid_shape_interfaces.hybrid_shape_plane_equation import HybridShapePlaneEquation
from pycatia.hybrid_shape_interfaces.hybrid_shape_plane_explicit import HybridShapePlaneExplicit
from pycatia.hybrid_shape_interfaces.hybrid_shape_plane_mean import HybridShapePlaneMean
from pycatia.hybrid_shape_interfaces.hybrid_shape_plane_normal import HybridShapePlaneNormal
from pycatia.hybrid_shape_interfaces.hybrid_shape_plane_offset import HybridShapePlaneOffset
from pycatia.hybrid_shape_interfaces.hybrid_shape_plane_offset_pt import HybridShapePlaneOffsetPt
from pycatia.hybrid_shape_interfaces.hybrid_shape_plane_tangent import HybridShapePlaneTangent
from pycatia.hybrid_shape_interfaces.hybrid_shape_point_between import HybridShapePointBetween
from pycatia.hybrid_shape_interfaces.hybrid_shape_point_center import HybridShapePointCenter
from pycatia.hybrid_shape_interfaces.hybrid_shape_point_coord import HybridShapePointCoord
from pycatia.hybrid_shape_interfaces.hybrid_shape_point_explicit import HybridShapePointExplicit
from pycatia.hybrid_shape_interfaces.hybrid_shape_point_on_curve import HybridShapePointOnCurve
from pycatia.hybrid_shape_interfaces.hybrid_shape_point_on_plane import HybridShapePointOnPlane
from pycatia.hybrid_shape_interfaces.hybrid_shape_point_on_surface import HybridShapePointOnSurface
from pycatia.hybrid_shape_interfaces.hybrid_shape_point_tangent import HybridShapePointTangent
from pycatia.hybrid_shape_interfaces.hybrid_shape_polyline import HybridShapePolyline
from pycatia.hybrid_shape_interfaces.hybrid_shape_position_transfo import HybridShapePositionTransfo
from pycatia.hybrid_shape_interfaces.hybrid_shape_project import HybridShapeProject
from pycatia.hybrid_shape_interfaces.hybrid_shape_reflect_line import HybridShapeReflectLine
from pycatia.hybrid_shape_interfaces.hybrid_shape_revol import HybridShapeRevol
from pycatia.hybrid_shape_interfaces.hybrid_shape_rotate import HybridShapeRotate
from pycatia.hybrid_shape_interfaces.hybrid_shape_scaling import HybridShapeScaling
from pycatia.hybrid_shape_interfaces.hybrid_shape_section import HybridShapeSection
from pycatia.hybrid_shape_interfaces.hybrid_shape_sphere import HybridShapeSphere
from pycatia.hybrid_shape_interfaces.hybrid_shape_spine import HybridShapeSpine
from pycatia.hybrid_shape_interfaces.hybrid_shape_spiral import HybridShapeSpiral
from pycatia.hybrid_shape_interfaces.hybrid_shape_spline import HybridShapeSpline
from pycatia.hybrid_shape_interfaces.hybrid_shape_split import HybridShapeSplit
from pycatia.hybrid_shape_interfaces.hybrid_shape_surface_explicit import HybridShapeSurfaceExplicit
from pycatia.hybrid_shape_interfaces.hybrid_shape_sweep_circle import HybridShapeSweepCircle
from pycatia.hybrid_shape_interfaces.hybrid_shape_sweep_conic import HybridShapeSweepConic
from pycatia.hybrid_shape_interfaces.hybrid_shape_sweep_explicit import HybridShapeSweepExplicit
from pycatia.hybrid_shape_interfaces.hybrid_shape_sweep_line import HybridShapeSweepLine
from pycatia.hybrid_shape_interfaces.hybrid_shape_symmetry import HybridShapeSymmetry
from pycatia.hybrid_shape_interfaces.hybrid_shape_transfer import HybridShapeTransfer
from pycatia.hybrid_shape_interfaces.hybrid_shape_translate import HybridShapeTranslate
from pycatia.hybrid_shape_interfaces.hybrid_shape_trim import HybridShapeTrim
from pycatia.hybrid_shape_interfaces.hybrid_shape_unfold import HybridShapeUnfold
from pycatia.hybrid_shape_interfaces.hybrid_shape_volume_explicit import HybridShapeVolumeExplicit
from pycatia.hybrid_shape_interfaces.hybrid_shape_wrap_curve import HybridShapeWrapCurve
from pycatia.hybrid_shape_interfaces.hybrid_shape_wrap_surface import HybridShapeWrapSurface
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.factory import Factory
from pycatia.scripts.vba import vba_nothing


class HybridShapeFactory(Factory):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Factory
                |                         HybridShapeFactory
                |
                | Interface to create all kinds of HybridShape objects that may be needed in
                | wireframe and surface design.
                |
                | Note:
                | This interface concern GSD/GSO/DL1 feature creation via VB
                | Use of the creation methods requires to have granted license configuration for
                | feature creation
                | i.e:
                | - Bump, Develop,WrapCurve,WrapSurface require GSO license.
                | - Unfold, Develop require DL1 license.
                | - Other require GSD license.
                | Note2:
                | For all methods creating datums AddNew*Datum,
                | the object passed as parameter to create the datum has to be in the current
                | container.
                | Otherwise, an error occurs.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_factory = com_object

    def add_new3_d_corner(self, i_element1: Reference, i_element2: Reference, i_direction: HybridShapeDirection,
                          i_radius: float, i_orientation1: int, i_orientation2: int, i_trim: bool) -> HybridShapeCorner:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNew3DCorner(Reference iElement1,
                | Reference iElement2,
                | HybridShapeDirection iDirection,
                | double iRadius,
                | long iOrientation1,
                | long iOrientation2,
                | boolean iTrim) As HybridShapeCorner
                |
                |     Creates a new 3D Corner within the current body.
                |     Create a 3D corner curve between a point and a curve or 2 curves along a
                |     direction.
                |
                |     Parameters:
                |
                |         iElement1
                |             First reference curve.
                |         iElement2
                |             Second reference curve.
                |         iDirection
                |             Direction.
                |         iRadius
                |             Radius of the corner.
                |         iOrientation1
                |             Manage the corner center position. Value can be 1 or -1
                |
                |         iOrientation2
                |             Manage the corner center position. Value can be 1 or -1
                |
                |         iTrim
                |             Value can be FALSE or TRUE
                |             if TRUE the 2 curves are trimed and asembled with the corner.
                |
                |         oCorner
                |             Created corner.

        :param Reference i_element1:
        :param Reference i_element2:
        :param HybridShapeDirection i_direction:
        :param float i_radius:
        :param int i_orientation1:
        :param int i_orientation2:
        :param bool i_trim:
        :return: HybridShapeCorner
        :rtype: HybridShapeCorner
        """
        return HybridShapeCorner(self.hybrid_shape_factory.AddNew3DCorner(i_element1.com_object, i_element2.com_object,
                                                                          i_direction.com_object, i_radius,
                                                                          i_orientation1, i_orientation2, i_trim))

    def add_new_3d_curve_offset(self, i_curve_to_offset: Reference, i_direction: HybridShapeDirection, i_offset: float,
                                i_corner_radius: float, i_corner_tension: float) -> HybridShape3DCurveOffset:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNew3DCurveOffset(Reference iCurveToOffset,
                | HybridShapeDirection iDirection,
                | double iOffset,
                | double iCornerRadius,
                | double iCornerTension) As HybridShape3DCurveOffset
                |
                |     Creates a 3D Curve Offset.
                |
                |     Parameters:
                |
                |         iCurve
                |             The curve to offset
                |         iDirection
                |             Offset pulling direction.
                |         iOffsetValue
                |             Offset Value.
                |         iCornerRadius
                |             Radius of the 3D corners.
                |         iCornerTension
                |             Tension of the 3D corners.
                |
                |     Returns:
                |         CATIGSM3DCurveOffset_var created 3DCurveOffset.

        :param Reference i_curve_to_offset:
        :param HybridShapeDirection i_direction:
        :param float i_offset:
        :param float i_corner_radius:
        :param float i_corner_tension:
        :return: HybridShape3DCurveOffset
        :rtype: HybridShape3DCurveOffset
        """
        return HybridShape3DCurveOffset(
            self.hybrid_shape_factory.AddNew3DCurveOffset(i_curve_to_offset.com_object, i_direction.com_object,
                                                          i_offset, i_corner_radius, i_corner_tension))

    def add_new_affinity(self, i_element: Reference, i_x_ratio: float, i_y_ratio: float,
                         i_z_ratio: float) -> HybridShapeAffinity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewAffinity(Reference iElement,
                | double iXRatio,
                | double iYRatio,
                | double iZRatio) As HybridShapeAffinity
                |
                |     Creates a new Affinity within the current body.
                |
                |     Parameters:
                |
                |         iElement
                |             point, curve, surface or solid.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face, TriDimFeatEdge, BiDimFeatEdge and Vertex.
                |
                |     iXRatio
                |         Ratio of affinity in iX direction.
                |     iYRatio
                |         Ratio of affinity in iY direction.
                |     iZRatio
                |         Ratio of affinity in iZ direction.
                |     oAffinity
                |         Created affinity

        :param Reference i_element:
        :param float i_x_ratio:
        :param float i_y_ratio:
        :param float i_z_ratio:
        :return: HybridShapeAffinity
        :rtype: HybridShapeAffinity
        """
        return HybridShapeAffinity(
            self.hybrid_shape_factory.AddNewAffinity(i_element.com_object, i_x_ratio, i_y_ratio, i_z_ratio))

    def add_new_axis_line(self, i_element: Reference) -> HybridShapeAxisLine:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewAxisLine(Reference iElement) As
                | HybridShapeAxisLine
                |
                |     Creates a new AxisLine within the current body.
                |
                |     Parameters:
                |
                |         iElement
                |             Circle, Ellipse, Oblong, Sphere, Revolution surface. Axis is
                |             computed for this element
                |         oAxisLine
                |             Created axis line

        :param Reference i_element:
        :return: HybridShapeAxisLine
        :rtype: HybridShapeAxisLine
        """
        return HybridShapeAxisLine(self.hybrid_shape_factory.AddNewAxisLine(i_element.com_object))

    def add_new_axis_to_axis(self, i_object: Reference, i_reference_axis: Reference,
                             i_target_axis: Reference) -> HybridShapeAxisToAxis:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewAxisToAxis(Reference iObject,
                | Reference iReferenceAxis,
                | Reference iTargetAxis) As HybridShapeAxisToAxis
                |
                |     Creates a new axis to axis transformation within the current
                |     body.
                |
                |     Parameters:
                |
                |         iObject
                |             Point, curve, surface or solid to transform.
                |         iReferenceAxis
                |             reference axis system
                |         iTargetAxis
                |             target axis system
                |         oAxisToAxis
                |             Created axis to axis transformation.

        :param Reference i_object:
        :param Reference i_reference_axis:
        :param Reference i_target_axis:
        :return: HybridShapeAxisToAxis
        :rtype: HybridShapeAxisToAxis
        """
        return HybridShapeAxisToAxis(
            self.hybrid_shape_factory.AddNewAxisToAxis(i_object.com_object, i_reference_axis.com_object,
                                                       i_target_axis.com_object))

    def add_new_blend(self) -> HybridShapeBlend:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewBlend() As HybridShapeBlend
                |
                |     Creates a new blend surface within the current body.
                |
                |     Parameters:
                |
                |         oBlend
                |             The Blend object if succeded

        :return: HybridShapeBlend
        :rtype: HybridShapeBlend
        """
        return HybridShapeBlend(self.hybrid_shape_factory.AddNewBlend())

    def add_new_boundary(self, i_initial_element: Reference, i_support: Reference,
                         i_typede_propagation: int) -> HybridShapeBoundary:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewBoundary(Reference iInitialElement,
                | Reference iSupport,
                | long iTypedePropagation) As HybridShapeBoundary
                |
                |     Creates a new Boundary within the current body.
                |
                |     Parameters:
                |
                |         iInitialElement
                |             the element used to initialise the propagation around the
                |             surface
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see BiDimFeatEdge.
                |     iSupport
                |         the surface used to compute the boundary around it
                |
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iTypedePropagation
                |         Propagation type the values are: 0 for Boundary for all edges 1 for
                |         Boundary propagation for edges on connexe point 2 for Boundary propagation for
                |         edges tangent at point breaks 3 for Boundary not propagation from the current
                |         edge
                |     oBoundary
                |         The computed element

        :param Reference i_initial_element:
        :param Reference i_support:
        :param int i_typede_propagation:
        :return: HybridShapeBoundary
        :rtype: HybridShapeBoundary
        """
        return HybridShapeBoundary(
            self.hybrid_shape_factory.AddNewBoundary(i_initial_element.com_object, i_support.com_object,
                                                     i_typede_propagation))

    def add_new_boundary_of_surface(self, surface: Reference) -> HybridShapeBoundary:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewBoundaryOfSurface(Reference Surface) As
                | HybridShapeBoundary
                |
                |     Creates a Boundary within the current body.
                |
                |     Parameters:
                |
                |         iSurface
                |             the feature on which all the boundaries will be computed
                |
                |         oBoundary
                |             the whole boundary of the Surface given in first
                |             parameter

        :param Reference surface:
        :return: HybridShapeBoundary
        :rtype: HybridShapeBoundary
        """
        return HybridShapeBoundary(self.hybrid_shape_factory.AddNewBoundaryOfSurface(surface.com_object))

    def add_new_bump(self, i_body_to_bump: Reference) -> HybridShapeBump:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewBump(Reference iBodyToBump) As HybridShapeBump
                |
                |     Creates a new Bump within the current body.
                |     Note: require GSO license.
                |
                |     Parameters:
                |
                |         :
                |             iBodyToBump Body to deform witn a Bump
                |         :
                |             oBump Bump result

        :param Reference i_body_to_bump:
        :return: HybridShapeBump
        :rtype: HybridShapeBump
        """
        return HybridShapeBump(self.hybrid_shape_factory.AddNewBump(i_body_to_bump.com_object))

    def add_new_circle2_points_rad(self, i_point1: Reference, i_point2: Reference, i_support: Reference,
                                   i_geodesic: bool, i_radius: float, i_ori: int) -> HybridShapeCircle2PointsRad:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircle2PointsRad(Reference iPoint1,
                | Reference iPoint2,
                | Reference iSupport,
                | boolean iGeodesic,
                | double iRadius,
                | long iOri) As HybridShapeCircle2PointsRad
                |
                |     Creates a new Circle passing through 2 points with a radius within the
                |     current body.
                |
                |     Parameters:
                |
                |         iPoint1
                |             first passing point.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iPoint2
                |         second passing point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iSupport
                |         support surface.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iGeodesic
                |         Puts the circle on the surface.
                |     iRadius
                |         Value specified is considered as radius. To use this value as diameter,
                |         set DiameterMode using SetDiameterMode method
                |     iOri
                |         circle orientation. Defines the side where circle is computed using the
                |         normal direction of line between the 2 passing points.
                |
                |     oCircle
                |         The Circle object if succeeded

        :param Reference i_point1:
        :param Reference i_point2:
        :param Reference i_support:
        :param bool i_geodesic:
        :param float i_radius:
        :param int i_ori:
        :return: HybridShapeCircle2PointsRad
        :rtype: HybridShapeCircle2PointsRad
        """
        return HybridShapeCircle2PointsRad(
            self.hybrid_shape_factory.AddNewCircle2PointsRad(i_point1.com_object, i_point2.com_object,
                                                             i_support.com_object, i_geodesic, i_radius, i_ori))

    def add_new_circle3_points(self, i_point1: Reference, i_point2: Reference,
                               i_point3: Reference) -> HybridShapeCircle3Points:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircle3Points(Reference iPoint1,
                | Reference iPoint2,
                | Reference iPoint3) As HybridShapeCircle3Points
                |
                |     Creates a new circle passing through 3 points within the current
                |     body.
                |
                |     Parameters:
                |
                |         iPoint1
                |             first passing point.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iPoint2
                |         second passing point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iPoint3
                |         third passing point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     oCircle
                |         Created circle

        :param Reference i_point1:
        :param Reference i_point2:
        :param Reference i_point3:
        :return: HybridShapeCircle3Points
        :rtype: HybridShapeCircle3Points
        """
        return HybridShapeCircle3Points(
            self.hybrid_shape_factory.AddNewCircle3Points(i_point1.com_object, i_point2.com_object,
                                                          i_point3.com_object))

    def add_new_circle_bitangent_point(self, i_curve1: Reference, i_curve2: Reference, i_point: Reference,
                                       i_support: Reference, i_ori1: int,
                                       i_ori2: int) -> HybridShapeCircleBitangentPoint:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircleBitangentPoint(Reference iCurve1,
                | Reference iCurve2,
                | Reference iPoint,
                | Reference iSupport,
                | long iOri1,
                | long iOri2) As HybridShapeCircleBitangentPoint
                |
                |     Creates a new circle tangent to 2 curves and passing through one point
                |     within the current body.
                |
                |     Parameters:
                |
                |         iCurve1
                |             first curve to which the circle will be tangent.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iCurve2
                |         second curve to which the circle will be tangent.
                |         Sub-element(s) supported (see Boundary object): see TriDimFeatEdge and
                |         BiDimFeatEdge.
                |     iPoint
                |         passing point. This point must lie on second curve.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iSupport
                |         support surface.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iOri1
                |         first curve orientation for circle computation.
                |     iOri2
                |         second curve orientation for circle computation.
                |     oCircle
                |         Created circle

        :param Reference i_curve1:
        :param Reference i_curve2:
        :param Reference i_point:
        :param Reference i_support:
        :param int i_ori1:
        :param int i_ori2:
        :return: HybridShapeCircleBitangentPoint
        :rtype: HybridShapeCircleBitangentPoint
        """
        return HybridShapeCircleBitangentPoint(
            self.hybrid_shape_factory.AddNewCircleBitangentPoint(i_curve1.com_object, i_curve2.com_object,
                                                                 i_point.com_object, i_support.com_object, i_ori1,
                                                                 i_ori2))

    def add_new_circle_bitangent_radius(self, i_curve1: Reference, i_curve2: Reference, i_support: Reference,
                                        i_radius: float, i_ori1: int, i_ori2: int) -> HybridShapeCircleBitangentRadius:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircleBitangentRadius(Reference iCurve1,
                | Reference iCurve2,
                | Reference iSupport,
                | double iRadius,
                | long iOri1,
                | long iOri2) As HybridShapeCircleBitangentRadius
                |
                |     Creates a new circle tangent to 2 curves and with a radius within the
                |     current body.
                |
                |     Parameters:
                |
                |         iCurve1
                |             first curve to which the circle will be tangent.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iCurve2
                |         second curve to which the circle will be tangent.
                |         Sub-element(s) supported (see Boundary object): see TriDimFeatEdge and
                |         BiDimFeatEdge.
                |     iSupport
                |         support surface.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iRadius
                |         Value specified is considered as radius. To use this value as diameter,
                |         set DiameterMode using SetDiameterMode method
                |     iOri1
                |         first curve orientation for circle computation.
                |     iOri2
                |         second curve orientation for circle computation.
                |     oCircle
                |         Created circle

        :param Reference i_curve1:
        :param Reference i_curve2:
        :param Reference i_support:
        :param float i_radius:
        :param int i_ori1:
        :param int i_ori2:
        :return: HybridShapeCircleBitangentRadius
        :rtype: HybridShapeCircleBitangentRadius
        """
        return HybridShapeCircleBitangentRadius(
            self.hybrid_shape_factory.AddNewCircleBitangentRadius(i_curve1.com_object, i_curve2.com_object,
                                                                  i_support.com_object, i_radius, i_ori1, i_ori2))

    def add_new_circle_center_axis(self, i_axis: Reference, i_point: Reference, i_value: float,
                                   i_projection: bool) -> HybridShapeCircleCenterAxis:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircleCenterAxis(Reference iAxis,
                | Reference iPoint,
                | double iValue,
                | boolean iProjection) As HybridShapeCircleCenterAxis
                |
                |     Creates a circle from point and axis.
                |
                |     Parameters:
                |
                |         iAxis
                |             Axis of plane in which circle is lying
                |         iPoint
                |             Point used for center computation. It will be the center if ProjectionMode is False.
                |             If ProjectionMode = True, this point will be projected on to axis/line
                |         iValue
                |             Value specified is considered as radius. To use this value as
                |             diameter, set DiameterMode property
                |         iProjection
                |             Sets Projection Mode. ProjectionMode = TRUE implies point will be projected on to
                |             axis/line, ProjectionMode = FALSE implies that point will be center of the circle.
                |         oCircle
                |             Created circle

        :param Reference i_axis:
        :param Reference i_point:
        :param float i_value:
        :param bool i_projection:
        :return: HybridShapeCircleCenterAxis
        :rtype: HybridShapeCircleCenterAxis
        """
        return HybridShapeCircleCenterAxis(
            self.hybrid_shape_factory.AddNewCircleCenterAxis(i_axis.com_object, i_point.com_object, i_value,
                                                             i_projection))

    def add_new_circle_center_axis_with_angles(self, i_axis: Reference, i_point: Reference, i_value: float,
                                               i_projection: bool, i_start_angle: float,
                                               i_end_angle: float) -> HybridShapeCircleCenterAxis:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircleCenterAxisWithAngles(Reference iAxis,
                | Reference iPoint,
                | double iValue,
                | boolean iProjection,
                | double iStartAngle,
                | double iEndAngle) As HybridShapeCircleCenterAxis
                |
                |     Creates a circle from point and axis.
                |
                |     Parameters:
                |
                |         iAxis
                |             Axis of plane in which circle is lying
                |             Sub-element(s) supported (see
                |
                |         Boundary object):
                |     iPoint
                |         Point used for center computation. It will be the center if ProjectionMode is False.
                |         If ProjectionMode = True, this point will be projected on to axis/line
                |         Sub-element(s) supported (see Boundary object):
                |     iValue
                |         Value specified is considered as radius. To use this value as diameter,
                |         set DiameterMode property
                |     iProjection
                |         Sets Projection Mode. ProjectionMode = TRUE implies point will be projected on to axis/line,
                |         ProjectionMode = FALSE implies that point will be center of the circle.
                |     iStartAngle
                |         start angle
                |     iEndAngle
                |         end angle
                |     oCircle
                |         Created circle

        :param Reference i_axis:
        :param Reference i_point:
        :param float i_value:
        :param bool i_projection:
        :param float i_start_angle:
        :param float i_end_angle:
        :return: HybridShapeCircleCenterAxis
        :rtype: HybridShapeCircleCenterAxis
        """
        return HybridShapeCircleCenterAxis(
            self.hybrid_shape_factory.AddNewCircleCenterAxisWithAngles(i_axis.com_object, i_point.com_object, i_value,
                                                                       i_projection, i_start_angle, i_end_angle))

    def add_new_circle_center_tangent(self, i_center_elem: Reference, i_tangent_curve: Reference, i_support: Reference,
                                      i_radius: float) -> HybridShapeCircleCenterTangent:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircleCenterTangent(Reference iCenterElem,
                | Reference iTangentCurve,
                | Reference iSupport,
                | double iRadius) As HybridShapeCircleCenterTangent
                |
                |     Creates a new circle with given center element and tangent
                |     curve.
                |
                |     Parameters:
                |
                |         iCenterElem
                |             Can be either curve or point.
                |         iTangentCurve
                |             Curve to which the circle will be tangent.
                |         iSupport
                |             support surface or plane.
                |         iRadius
                |             circle radius, valid only if center element is curve. Value
                |             specified is considered as radius. To use this value as diameter, set
                |             DiameterMode using SetDiameterMode method
                |         oCircle
                |             Created circle

        :param Reference i_center_elem:
        :param Reference i_tangent_curve:
        :param Reference i_support:
        :param float i_radius:
        :return: HybridShapeCircleCenterTangent
        :rtype: HybridShapeCircleCenterTangent
        """
        return HybridShapeCircleCenterTangent(
            self.hybrid_shape_factory.AddNewCircleCenterTangent(i_center_elem.com_object, i_tangent_curve.com_object,
                                                                i_support.com_object, i_radius))

    def add_new_circle_ctr_pt(self, i_center: Reference, i_crossing_point: Reference, i_support: Reference,
                              i_geodesic: bool) -> HybridShapeCircleCtrPt:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircleCtrPt(Reference iCenter,
                | Reference iCrossingPoint,
                | Reference iSupport,
                | boolean iGeodesic) As HybridShapeCircleCtrPt
                |
                |     Creates a new whole circle defined by its center, a passing point within
                |     the current body.
                |
                |     Parameters:
                |
                |         iCenter
                |             circle center.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iCrossingPoint
                |         passing point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iSupport
                |         support surface.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iGeodesic
                |         Puts the circle on the surface.
                |     oCircle
                |         CreatedCircle

        :param Reference i_center:
        :param Reference i_crossing_point:
        :param Reference i_support:
        :param bool i_geodesic:
        :return: HybridShapeCircleCtrPt
        :rtype: HybridShapeCircleCtrPt
        """
        return HybridShapeCircleCtrPt(
            self.hybrid_shape_factory.AddNewCircleCtrPt(i_center.com_object, i_crossing_point.com_object,
                                                        i_support.com_object, i_geodesic))

    def add_new_circle_ctr_pt_with_angles(self, i_center: Reference, i_crossing_point: Reference, i_support: Reference,
                                          i_geodesic: bool, i_start_angle: float,
                                          i_end_angle: float) -> HybridShapeCircleCtrPt:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircleCtrPtWithAngles(Reference iCenter,
                | Reference iCrossingPoint,
                | Reference iSupport,
                | boolean iGeodesic,
                | double iStartAngle,
                | double iEndAngle) As HybridShapeCircleCtrPt
                |
                |     Creates a new circle defined by its center, a passing point and angles
                |     within the current body.
                |
                |     Parameters:
                |
                |         iCenter
                |             circle center.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iCrossingPoint
                |         passing point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iSupport
                |         support surface.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iGeodesic
                |         Puts the circle on the surface.
                |     iStartAngle
                |         start angle
                |     iEndAngle
                |         end angle
                |     oCircle
                |         Created circle

        :param Reference i_center:
        :param Reference i_crossing_point:
        :param Reference i_support:
        :param bool i_geodesic:
        :param float i_start_angle:
        :param float i_end_angle:
        :return: HybridShapeCircleCtrPt
        :rtype: HybridShapeCircleCtrPt
        """
        return HybridShapeCircleCtrPt(
            self.hybrid_shape_factory.AddNewCircleCtrPtWithAngles(i_center.com_object, i_crossing_point.com_object,
                                                                  i_support.com_object, i_geodesic, i_start_angle,
                                                                  i_end_angle))

    def add_new_circle_ctr_rad(self, i_center: Reference, i_support: Reference, i_geodesic: bool,
                               i_radius: float) -> HybridShapeCircleCtrRad:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircleCtrRad(Reference iCenter,
                | Reference iSupport,
                | boolean iGeodesic,
                | double iRadius) As HybridShapeCircleCtrRad
                |
                |     Creates a new whole circle defined by its center and a radius within the
                |     current body.
                |
                |     Parameters:
                |
                |         iCenter
                |             circle center.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iSupport
                |         support surface.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iGeodesic
                |         Puts the circle on the surface.
                |     iRadius
                |         Value specified is considered as radius. To use this value as diameter,
                |         set DiameterMode using SetDiameterMode method
                |     oCircle
                |         Created circle

        :param Reference i_center:
        :param Reference i_support:
        :param bool i_geodesic:
        :param float i_radius:
        :return: HybridShapeCircleCtrRad
        :rtype: HybridShapeCircleCtrRad
        """
        return HybridShapeCircleCtrRad(
            self.hybrid_shape_factory.AddNewCircleCtrRad(i_center.com_object, i_support.com_object, i_geodesic,
                                                         i_radius))

    def add_new_circle_ctr_rad_with_angles(self, i_center: Reference, i_support: Reference, i_geodesic: bool,
                                           i_radius: float, i_start_angle: float,
                                           i_end_angle: float) -> HybridShapeCircleCtrRad:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircleCtrRadWithAngles(Reference iCenter,
                | Reference iSupport,
                | boolean iGeodesic,
                | double iRadius,
                | double iStartAngle,
                | double iEndAngle) As HybridShapeCircleCtrRad
                |
                |     Creates a new circle defined by its center, a radius and angles within the
                |     current body.
                |
                |     Parameters:
                |
                |         iCenter
                |             circle center.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iSupport
                |         support surface.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iGeodesic
                |         Puts the circle on the surface.
                |     iRadius
                |         Value specified is considered as radius. To use this value as diameter,
                |         set DiameterMode using SetDiameterMode method
                |     iStartAngle
                |         start angle
                |     iEndAngle
                |         end angle
                |     oCircle
                |         Created circle

        :param Reference i_center:
        :param Reference i_support:
        :param bool i_geodesic:
        :param float i_radius:
        :param float i_start_angle:
        :param float i_end_angle:
        :return: HybridShapeCircleCtrRad
        :rtype: HybridShapeCircleCtrRad
        """
        return HybridShapeCircleCtrRad(
            self.hybrid_shape_factory.AddNewCircleCtrRadWithAngles(i_center.com_object, i_support.com_object,
                                                                   i_geodesic, i_radius, i_start_angle, i_end_angle))

    def add_new_circle_datum(self, i_object: Reference) -> HybridShapeCircleExplicit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircleDatum(Reference iObject) As
                | HybridShapeCircleExplicit
                |
                |     Creates a new datum of circle within the current body.
                |
                |     Parameters:
                |
                |         iObject
                |             The object whose topological body will be duplicated and put into
                |             created datum
                |         oCircle
                |             Created datum Note2: the object passed as parameter to create the
                |             datum has to be in the current container. Otherwise, an error
                |             occurs.

        :param Reference i_object:
        :return: HybridShapeCircleExplicit
        :rtype: HybridShapeCircleExplicit
        """
        return HybridShapeCircleExplicit(self.hybrid_shape_factory.AddNewCircleDatum(i_object.com_object))

    def add_new_circle_tritangent(self, i_curve1: Reference, i_curve2: Reference, i_curve3: Reference,
                                  i_support: Reference, i_ori1: int, i_ori2: int,
                                  i_ori3: int) -> HybridShapeCircleTritangent:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircleTritangent(Reference iCurve1,
                | Reference iCurve2,
                | Reference iCurve3,
                | Reference iSupport,
                | long iOri1,
                | long iOri2,
                | long iOri3) As HybridShapeCircleTritangent
                |
                |     Creates a new tritangent circle within the current body.
                |
                |     Parameters:
                |
                |         iCurve1
                |             first curve to which the circle will be tangent.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iCurve2
                |         second curve to which the circle will be tangent.
                |         Sub-element(s) supported (see Boundary object): see TriDimFeatEdge and
                |         BiDimFeatEdge.
                |     iCurve3
                |         third curve to which the circle will be tangent.
                |         Sub-element(s) supported (see Boundary object): see TriDimFeatEdge and
                |         BiDimFeatEdge.
                |     iSupport
                |         support surface.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iOri1
                |         first curve orientation for circle computation.
                |     iOri2
                |         second curve orientation for circle computation.
                |     iOri3
                |         third curve orientation for circle computation.
                |     oCircle
                |         Created circle

        :param Reference i_curve1:
        :param Reference i_curve2:
        :param Reference i_curve3:
        :param Reference i_support:
        :param int i_ori1:
        :param int i_ori2:
        :param int i_ori3:
        :return: HybridShapeCircleTritangent
        :rtype: HybridShapeCircleTritangent
        """
        return HybridShapeCircleTritangent(
            self.hybrid_shape_factory.AddNewCircleTritangent(i_curve1.com_object, i_curve2.com_object,
                                                             i_curve3.com_object, i_support.com_object, i_ori1, i_ori2,
                                                             i_ori3))

    def add_new_combine(self, i_first_curve: Reference, i_second_curve: Reference,
                        i_nearest_solutions: int) -> HybridShapeCombine:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCombine(Reference iFirstCurve,
                | Reference iSecondCurve,
                | long iNearestSolutions) As HybridShapeCombine
                |
                |     Creates a new Combine within the current body. By default, the combine
                |     direction is the normal of each curve. If you want to change see
                |     CATIAHybridShapeCombine interfaces.
                |
                |     Parameters:
                |
                |         iFirstCurve
                |             First curve to combine
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iSecondCurve
                |         Second curve to combine
                |
                |         Sub-element(s) supported (see Boundary object): see TriDimFeatEdge and
                |         BiDimFeatEdge.
                |     iNearestSolution
                |         If more than one solution, to choose the nearest solution of the first
                |         curve
                |     oCombine
                |         The combine object if succeded

        :param Reference i_first_curve:
        :param Reference i_second_curve:
        :param int i_nearest_solutions:
        :return: HybridShapeCombine
        :rtype: HybridShapeCombine
        """
        return HybridShapeCombine(
            self.hybrid_shape_factory.AddNewCombine(i_first_curve.com_object, i_second_curve.com_object,
                                                    i_nearest_solutions))

    def add_new_conic(self, i_support: Reference, i_starting_point: Reference,
                      i_end_point: Reference) -> HybridShapeConic:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewConic(Reference iSupport,
                | Reference iStartingPoint,
                | Reference iEndPoint) As HybridShapeConic
                |
                |     Creates a new conic within the current body.
                |
                |     Parameters:
                |
                |         iSupport
                |             The conic support (always a plane).
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see PlanarFace.
                |     iStartingPoint
                |         Starting Point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iEndPoint
                |         End Point
                |
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     oConic
                |         The Conic object if succeded

        :param Reference i_support:
        :param Reference i_starting_point:
        :param Reference i_end_point:
        :return: HybridShapeConic
        :rtype: HybridShapeConic
        """
        return HybridShapeConic(self.hybrid_shape_factory.AddNewConic(i_support.com_object, i_starting_point.com_object,
                                                                      i_end_point.com_object))

    def add_new_conical_reflect_line_with_type(self, i_support: Reference, i_origin: Reference, i_angle: float,
                                               i_orientation_support: int, i_type: int) -> HybridShapeReflectLine:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewConicalReflectLineWithType(Reference iSupport,
                | Reference iOrigin,
                | double iAngle,
                | long iOrientationSupport,
                | long iType) As HybridShapeReflectLine
                |
                |     Creates a new conical ReflectLine within the current body.
                |     Create a conical reflectline curve on a support surface from an origin
                |     point with an angle.
                |
                |     Parameters:
                |
                |         iSupport
                |             Support surface.
                |         iOrigin
                |             Origin point.
                |         iAngle
                |             Angle of the reflectline.
                |         iOrientationSupport
                |             Manage the angle used to compute the reflectline. Value can be 1 or
                |             -1
                |         iType
                |             Manage the type used to compute the reflectline. Value can be 0 or
                |             1 Returns or sets whether the reflectline curve is or should be created with
                |             the normal to the support or the tangent plane to the
                |             support.
                |             Role: The TypeSolution indicates whether the created reflectline
                |             curve is compute with the angle between the normale to the support and the
                |             direction or with the angle between the tangent plane to the support and the
                |             direction..
                |             Legal values: 0 for the normal and 1 for the tangent plane.
                |
                |         oReflectLine
                |             Created conical reflectline.

        :param Reference i_support:
        :param Reference i_origin:
        :param float i_angle:
        :param int i_orientation_support:
        :param int i_type:
        :return: HybridShapeReflectLine
        :rtype: HybridShapeReflectLine
        """
        return HybridShapeReflectLine(
            self.hybrid_shape_factory.AddNewConicalReflectLineWithType(i_support.com_object, i_origin.com_object,
                                                                       i_angle, i_orientation_support, i_type))

    def add_new_connect(self, i_curve1: Reference, i_point1: Reference, i_orient1: int, i_continuity1: int,
                        i_tension1: float, i_curve2: Reference, i_point2: Reference, i_orient2: int, i_continuity2: int,
                        i_tension2: float, trim: bool) -> HybridShapeConnect:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewConnect(Reference iCurve1,
                | Reference iPoint1,
                | long iOrient1,
                | long iContinuity1,
                | double iTension1,
                | Reference iCurve2,
                | Reference iPoint2,
                | long iOrient2,
                | long iContinuity2,
                | double iTension2,
                | boolean Trim) As HybridShapeConnect
                |
                |     Creates a new Connect within the current body.
                |
                |     Parameters:
                |
                |         iCurve1
                |             First curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iPoint1
                |         First point (lying on the first curve)
                |
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iOrient1
                |         Orientation on the first curve
                |     iContinuity1
                |         Continuity on first curve
                |     iTension1
                |         Tension on first curve
                |     iCurve2
                |         Second curve.
                |         Sub-element(s) supported (see Boundary object): see TriDimFeatEdge and
                |         BiDimFeatEdge.
                |     iPoint2
                |         Second point (lying on the second curve)
                |
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iOrient2
                |         Orientation on the second curve
                |     iContinuity2
                |         Continuity on second curve
                |     iTension2
                |         Tension on second curve
                |     iTrim
                |         Trim the two curves with the connect
                |     oConnect
                |         The connect object

        :param Reference i_curve1:
        :param Reference i_point1:
        :param int i_orient1:
        :param int i_continuity1:
        :param float i_tension1:
        :param Reference i_curve2:
        :param Reference i_point2:
        :param int i_orient2:
        :param int i_continuity2:
        :param float i_tension2:
        :param bool trim:
        :return: HybridShapeConnect
        :rtype: HybridShapeConnect
        """
        return HybridShapeConnect(
            self.hybrid_shape_factory.AddNewConnect(i_curve1.com_object, i_point1.com_object, i_orient1, i_continuity1,
                                                    i_tension1, i_curve2.com_object, i_point2.com_object, i_orient2,
                                                    i_continuity2, i_tension2, trim))

    def add_new_corner(self, i_element1: Reference, i_element2: Reference, i_support: Reference, i_radius: float,
                       i_orientation1: int, i_orientation2: int, i_trim: bool) -> HybridShapeCorner:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCorner(Reference iElement1,
                | Reference iElement2,
                | Reference iSupport,
                | double iRadius,
                | long iOrientation1,
                | long iOrientation2,
                | boolean iTrim) As HybridShapeCorner
                |
                |     Creates a new Corner within the current body.
                |     Create a corner curve between a point and a curve or 2 curves on a support
                |     surface.
                |
                |     Parameters:
                |
                |         iElement1
                |             First reference curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge, BiDimFeatEdge and Vertex.
                |
                |     iElement2
                |         Second reference curve.
                |         Sub-element(s) supported (see Boundary object): see TriDimFeatEdge,
                |         BiDimFeatEdge and Vertex.
                |     iSupport
                |         Support surface.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iRadius
                |         Radius of the corner.
                |     iOrientation1
                |         Manage the corner center position. Value can be 1 or -1
                |
                |     iOrientation2
                |         Manage the corner center position. Value can be 1 or -1
                |
                |     iTrim
                |         Value can be FALSE or TRUE
                |         if TRUE the 2 curves are trimed and asembled with the corner.
                |
                |     oCorner
                |         Created corner.

        :param Reference i_element1:
        :param Reference i_element2:
        :param Reference i_support:
        :param float i_radius:
        :param int i_orientation1:
        :param int i_orientation2:
        :param bool i_trim:
        :return: HybridShapeCorner
        :rtype: HybridShapeCorner
        """
        return HybridShapeCorner(
            self.hybrid_shape_factory.AddNewCorner(i_element1.com_object, i_element2.com_object, i_support.com_object,
                                                   i_radius, i_orientation1, i_orientation2, i_trim))

    def add_new_curve_datum(self, i_object: Reference) -> HybridShapeCurveExplicit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCurveDatum(Reference iObject) As
                | HybridShapeCurveExplicit
                |
                |     Creates a new datum of curve within the current body.
                |
                |     Parameters:
                |
                |         iObject
                |             The object whose topological body will be duplicated and put into
                |             created datum
                |         oCurve
                |             Created curve Note2: the object passed as parameter to create the
                |             datum has to be in the current container. Otherwise, an error
                |             occurs.

        :param Reference i_object:
        :return: HybridShapeCurveExplicit
        :rtype: HybridShapeCurveExplicit
        """
        return HybridShapeCurveExplicit(self.hybrid_shape_factory.AddNewCurveDatum(i_object.com_object))

    def add_new_curve_par(self, curve: Reference, support: Reference, distance: float, invert_direction: bool,
                          geodesic: bool) -> HybridShapeCurvePar:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCurvePar(Reference Curve,
                | Reference Support,
                | double Distance,
                | boolean InvertDirection,
                | boolean Geodesic) As HybridShapeCurvePar
                |
                |     Creates a new CurvePar within the current body.
                |
                |     Parameters:
                |
                |         iCurve
                |             Reference curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iSupport
                |         Support on which the curve is lying on
                |
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iDistance
                |         Distance value
                |     iInvertDirection
                |         Orientation
                |     iGeodesic
                |         Geodesic mode
                |     oCurvePar
                |         Parallel curve

        :param Reference curve:
        :param Reference support:
        :param float distance:
        :param bool invert_direction:
        :param bool geodesic:
        :return: HybridShapeCurvePar
        :rtype: HybridShapeCurvePar
        """
        return HybridShapeCurvePar(
            self.hybrid_shape_factory.AddNewCurvePar(curve.com_object, support.com_object, distance, invert_direction,
                                                     geodesic))

    def add_new_curve_smooth(self, ip_ia_curve: Reference) -> HybridShapeCurveSmooth:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCurveSmooth(Reference ipIACurve) As
                | HybridShapeCurveSmooth
                |
                |     Creates a new CurveSmooth within the current body.
                |
                |     Parameters:
                |
                |         iCurve
                |             Reference curve to be smoothened
                |         oCurveSmooth
                |             Smoothened curve

        :param Reference ip_ia_curve:
        :return: HybridShapeCurveSmooth
        :rtype: HybridShapeCurveSmooth
        """
        return HybridShapeCurveSmooth(self.hybrid_shape_factory.AddNewCurveSmooth(ip_ia_curve.com_object))

    def add_new_cylinder(self, i_center: Reference, i_radius: float, i_first_length: float, i_second_length: float,
                         i_direction: HybridShapeDirection) -> HybridShapeCylinder:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCylinder(Reference iCenter,
                | double iRadius,
                | double iFirstLength,
                | double iSecondLength,
                | HybridShapeDirection iDirection) As HybridShapeCylinder
                |
                |     Creates a new Cylinder within the current body.
                |
                |     Parameters:
                |
                |         iCenter
                |             Center of the Cylinder - Can be Point or Vertex.
                |             Sub-element(s) supported (see
                |
                |         Vertex object):
                |     iRadius
                |         Radius of Cylinder.
                |     iFirstLength
                |         Length of Cylinder in the given direction.
                |     iSecondLength
                |         Length of Cylinder in the opposite direction.
                |     iDirection
                |         Direction of extrusion for Cylinder.
                |     oCylinderObject
                |         Created CylinderObjct.

        :param Reference i_center:
        :param float i_radius:
        :param float i_first_length:
        :param float i_second_length:
        :param HybridShapeDirection i_direction:
        :return: HybridShapeCylinder
        :rtype: HybridShapeCylinder
        """
        return HybridShapeCylinder(
            self.hybrid_shape_factory.AddNewCylinder(i_center.com_object, i_radius, i_first_length, i_second_length,
                                                     i_direction.com_object))

    def add_new_datums(self, i_elem: Reference) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewDatums(Reference iElem) As CATSafeArrayVariant
                |
                |     Creates datums from a multi-domain result feature, one datum is created by
                |     object domain.
                |     Note; Available only for a shape design feature as input ( not for datum
                |     feature ).
                |
                |     Parameters:
                |
                |         iElem
                |             Reference element
                |         oArrayOfDatum
                |             List of datum objects , one datum is created per
                |             omain
                |             Level of availability = V5R14
                |
                |             Example:
                |                 This example converts a hybrid shape object in as much as
                |                 datums that the original hybrid shape features contains of
                |                 domain
                |
                |                   Dim HShape
                |                   Set reference   = part.CreateReferenceFromObject(hybridShapeObject)
                |                   ' Convert to Datums
                |                   HShape = hybridShapeFactory.AddNewDatums reference
                |                   Num =UBound(HShape)
                |                   For i = 0 to Num
                |                         hybridBody1.AppendHybridShape HShape (i)
                |
                |                   Next
                |                   part.InWorkObject = HShape(num)
                |                   part.Update
                |                   ' Delete original feature
                |                   hybridShapeFactory.DeleteObjectForDatum
                |                   reference

        :param Reference i_elem:
        :return: tuple
        :rtype: tuple
        """
        # return self.hybrid_shape_factory.AddNewDatums(i_elem.com_object)
        from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape

        com_object_shapes = self.hybrid_shape_factory.AddNewDatums(i_elem.com_object)

        hybrid_shapes = []

        for com_object in com_object_shapes:
            hybrid_shapes.append(HybridShape(com_object))

        return tuple(hybrid_shapes)

    def add_new_develop(self, i_mode: int, i_to_develop: Reference, i_support: Reference) -> HybridShapeDevelop:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewDevelop(long iMode,
                | Reference iToDevelop,
                | Reference iSupport) As HybridShapeDevelop
                |
                |     Creates a new Develop within the current body.
                |     Note: require either DL1 or GSO license.
                |
                |     Parameters:
                |
                |         iMode
                |             Develop method.
                |         iToDevelop
                |             Wire to be developed.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iSupport
                |         Revolution support surface.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     oExt
                |         Created developed wire.

        :param int i_mode:
        :param Reference i_to_develop:
        :param Reference i_support:
        :return: HybridShapeDevelop
        :rtype: HybridShapeDevelop
        """
        return HybridShapeDevelop(
            self.hybrid_shape_factory.AddNewDevelop(i_mode, i_to_develop.com_object, i_support.com_object))

    def add_new_direction(self, i_element: Reference) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewDirection(Reference iElement) As
                | HybridShapeDirection
                |
                |     Creates a new direction specified by an element within the current
                |     body.
                |
                |     Parameters:
                |
                |         iElement
                |             Line or plane specifying the direction. In case of plane, the plane
                |             normal vector is the direction
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see RectilinearTriDimFeatEdge,
                |         RectilinearBiDimFeatEdge and RectilinearMonoDimFeatEdge.
                |
                |     oDirection
                |         Created direction.

        :param Reference i_element:
        :return: HybridShapeDirection
        :rtype: HybridShapeDirection
        """
        return HybridShapeDirection(self.hybrid_shape_factory.AddNewDirection(i_element.com_object))

    def add_new_direction_by_coord(self, i_x: float, i_y: float, i_z: float) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewDirectionByCoord(double iX,
                | double iY,
                | double iZ) As HybridShapeDirection
                |
                |     Creates a new Direction specifed by coordinates within the current
                |     body.
                |
                |     Parameters:
                |
                |         iX
                |             X component
                |         iY
                |             Y component
                |         iZ
                |             Z component
                |         oDirection
                |             Created direction

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :return: HybridShapeDirection
        :rtype: HybridShapeDirection
        """
        return HybridShapeDirection(self.hybrid_shape_factory.AddNewDirectionByCoord(i_x, i_y, i_z))

    def add_new_empty_rotate(self) -> HybridShapeRotate:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewEmptyRotate() As HybridShapeRotate
                |
                |     Creates a new empty Rotate within the current body.

        :return: HybridShapeRotate
        :rtype: HybridShapeRotate
        """
        return HybridShapeRotate(self.hybrid_shape_factory.AddNewEmptyRotate())

    def add_new_empty_translate(self) -> HybridShapeTranslate:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewEmptyTranslate() As HybridShapeTranslate
                |
                |     Creates a new empty Translate within the current body.

        :return: HybridShapeTranslate
        :rtype: HybridShapeTranslate
        """
        return HybridShapeTranslate(self.hybrid_shape_factory.AddNewEmptyTranslate())

    def add_new_extract(self, element: Reference) -> HybridShapeExtract:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewExtract(Reference Element) As
                | HybridShapeExtract
                |
                |     Creates a new Extract within the current body.
                |
                |     Parameters:
                |
                |         iElement
                |             Initial element used to start the extraction
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Boundary.
                |     oExt
                |         The extracted object

        :param Reference element:
        :return: HybridShapeExtract
        :rtype: HybridShapeExtract
        """
        return HybridShapeExtract(self.hybrid_shape_factory.AddNewExtract(element.com_object))

    def add_new_extract_multi(self, element: Reference) -> HybridShapeExtractMulti:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewExtractMulti(Reference Element) As
                | HybridShapeExtractMulti
                |
                |     Creates a new Multiple Extract within the current body.
                |
                |     Parameters:
                |
                |         iElement
                |             Initial element used to start the extraction
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Boundary.
                |     oExt
                |         The extracted object

        :param Reference element:
        :return: HybridShapeExtractMulti
        :rtype: HybridShapeExtractMulti
        """
        return HybridShapeExtractMulti(self.hybrid_shape_factory.AddNewExtractMulti(element.com_object))

    def add_new_extrapol_length(self, i_boundary: Reference, i_to_extrapol: Reference,
                                i_length: float) -> HybridShapeExtrapol:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewExtrapolLength(Reference iBoundary,
                | Reference iToExtrapol,
                | double iLength) As HybridShapeExtrapol
                |
                |     Creates a new Extrapol (specified by length) within the current
                |     body.
                |
                |     Parameters:
                |
                |         iBoundary
                |             Boundary point of curve to extrapolate or boundary curve of surface
                |             to extrapolate.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iToExtrapol
                |         Curve or surface to extrapolate.
                |         Sub-element(s) supported (see Boundary object): see Face,
                |         TriDimFeatEdge and BiDimFeatEdge.
                |     iLength
                |         Extrapolation length.
                |     oExtrapol
                |         Created Extrapolation.

        :param Reference i_boundary:
        :param Reference i_to_extrapol:
        :param float i_length:
        :return: HybridShapeExtrapol
        :rtype: HybridShapeExtrapol
        """
        return HybridShapeExtrapol(
            self.hybrid_shape_factory.AddNewExtrapolLength(i_boundary.com_object, i_to_extrapol.com_object, i_length))

    def add_new_extrapol_until(self, i_boundary: Reference, i_to_extrapol: Reference,
                               i_until: Reference) -> HybridShapeExtrapol:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewExtrapolUntil(Reference iBoundary,
                | Reference iToExtrapol,
                | Reference iUntil) As HybridShapeExtrapol
                |
                |     Creates a new Extrapol (until an element) within the current
                |     body.
                |
                |     Parameters:
                |
                |         iBoundary
                |             Boundary point of curve to extrapolate or boundary curve of surface
                |             to extrapolate.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iToExtrapol
                |         Curve or surface to extrapolate.
                |         Sub-element(s) supported (see Boundary object): see Face,
                |         TriDimFeatEdge and BiDimFeatEdge.
                |     iUntil
                |         Extrapolation limit surface.
                |     oExtrapol
                |         Created Extrapolation.

        :param Reference i_boundary:
        :param Reference i_to_extrapol:
        :param Reference i_until:
        :return: HybridShapeExtrapol
        :rtype: HybridShapeExtrapol
        """
        return HybridShapeExtrapol(
            self.hybrid_shape_factory.AddNewExtrapolUntil(i_boundary.com_object, i_to_extrapol.com_object,
                                                          i_until.com_object))

    def add_new_extremum(self, i_objet: Reference, i_dir: HybridShapeDirection, i_min_max: int) -> HybridShapeExtremum:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewExtremum(Reference iObjet,
                | HybridShapeDirection iDir,
                | long iMinMax) As HybridShapeExtremum
                |
                |     Creates a new Extremum within the current body.
                |
                |     Parameters:
                |
                |         iObjet
                |             Element onto extremum is computed
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge, BiDimFeatEdge and Face.
                |
                |     iDir
                |         Extremum direction
                |     iMinMax
                |         Maximum (GSMMax) or Minimum (GSMMin)
                |     oExt
                |         The extremum object if succeded

        :param Reference i_objet:
        :param HybridShapeDirection i_dir:
        :param int i_min_max:
        :return: HybridShapeExtremum
        :rtype: HybridShapeExtremum
        """
        return HybridShapeExtremum(
            self.hybrid_shape_factory.AddNewExtremum(i_objet.com_object, i_dir.com_object, i_min_max))

    def add_new_extremum_polar(self, i_type: int, ip_ia_contour: Reference) -> HybridShapeExtremumPolar:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewExtremumPolar(short iType,
                | Reference ipIAContour) As HybridShapeExtremumPolar
                |
                |     Creates a new Extremum Polar within the current body.
                |
                |     Parameters:
                |
                |         iType
                |             Type of extremum polar 0-Min Radius 1-Max Radius 2- Min Angle 3-
                |             Maximum Angle
                |         ipIAContour
                |             Extremum Polar Contour. It should be non convex
                |         opIAExtPolar
                |             The extremum polar object if succeded

        :param int i_type:
        :param Reference ip_ia_contour:
        :return: HybridShapeExtremumPolar
        :rtype: HybridShapeExtremumPolar
        """
        return HybridShapeExtremumPolar(self.hybrid_shape_factory.AddNewExtremumPolar(i_type, ip_ia_contour.com_object))

    def add_new_extrude(self, i_object_to_extrude: Reference, i_offset_debut: float, i_offset_fin: float,
                        i_direction: HybridShapeDirection) -> HybridShapeExtrude:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewExtrude(Reference iObjectToExtrude,
                | double iOffsetDebut,
                | double iOffsetFin,
                | HybridShapeDirection iDirection) As HybridShapeExtrude
                |
                |     Creates a new extrude within the current body.
                |
                |     Parameters:
                |
                |         iObjectToExtrude
                |             Object to be extruded (point, line ,curve,or face)
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Boundary.
                |     iOffsetDebut
                |         Length value
                |     iOffsetFin
                |         Length value ( iOffsetFin has to be larger than iOffsetDebut)
                |
                |     iDirection
                |         Extrusion direction
                |     oExtrudeObject
                |         Extruded result

        :param Reference i_object_to_extrude:
        :param float i_offset_debut:
        :param float i_offset_fin:
        :param HybridShapeDirection i_direction:
        :return: HybridShapeExtrude
        :rtype: HybridShapeExtrude
        """
        return HybridShapeExtrude(
            self.hybrid_shape_factory.AddNewExtrude(i_object_to_extrude.com_object, i_offset_debut, i_offset_fin,
                                                    i_direction.com_object))

    def add_new_fill(self) -> HybridShapeFill:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewFill() As HybridShapeFill
                |
                |     Creates a new Fill within the current body.
                |
                |     Parameters:
                |
                |         oFill
                |             Fill object

        :return: HybridShapeFill
        :rtype: HybridShapeFill
        """
        return HybridShapeFill(self.hybrid_shape_factory.AddNewFill())

    def add_new_fillet_bi_tangent(self, i_element1: Reference, i_element2: Reference, i_radius: float,
                                  i_orientation1: int, i_orientation2: int, i_supports_trim_mode: int,
                                  i_ribbon_relimitation_mode: int) -> HybridShapeFilletBiTangent:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewFilletBiTangent(Reference iElement1,
                | Reference iElement2,
                | double iRadius,
                | long iOrientation1,
                | long iOrientation2,
                | long iSupportsTrimMode,
                | long iRibbonRelimitationMode) As HybridShapeFilletBiTangent
                |
                |     Creates a new a sphere bitangent fillet between two skins.
                |
                |     Parameters:
                |
                |         iElement1
                |             First support of fillet.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face.
                |     iElement2
                |         Second support of fillet.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iRadius
                |         Radius of the fillet.
                |     iOrientation1
                |         Manage the fillet center position.
                |     iOrientation2
                |         Manage the fillet center position.
                |     iSupportsTrimMode
                |         The 2 supports can be trimmed and assembled with the fillet. Value can
                |         be 0 (No trim ) or 1 (Trim)
                |     iRibbonRelimitationMode
                |         Manage the relimition of fillet extremities.
                |         Value can be : 0 (Smooth), 1 (Straight), 2 (Maximum) or 3 (Minimum)
                |     oFillet
                |         Created fillet.

        :param Reference i_element1:
        :param Reference i_element2:
        :param float i_radius:
        :param int i_orientation1:
        :param int i_orientation2:
        :param int i_supports_trim_mode:
        :param int i_ribbon_relimitation_mode:
        :return: HybridShapeFilletBiTangent
        :rtype: HybridShapeFilletBiTangent
        """
        return HybridShapeFilletBiTangent(
            self.hybrid_shape_factory.AddNewFilletBiTangent(i_element1.com_object, i_element2.com_object, i_radius,
                                                            i_orientation1, i_orientation2, i_supports_trim_mode,
                                                            i_ribbon_relimitation_mode))

    def add_new_fillet_tri_tangent(self, i_element1: Reference, i_element2: Reference, i_remove_elem: Reference,
                                   i_orientation1: int, i_orientation2: int, i_remove_orientation: int,
                                   i_supports_trim_mode: int,
                                   i_ribbon_relimitation_mode: int) -> HybridShapeFilletTriTangent:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewFilletTriTangent(Reference iElement1,
                | Reference iElement2,
                | Reference iRemoveElem,
                | long iOrientation1,
                | long iOrientation2,
                | long iRemoveOrientation,
                | long iSupportsTrimMode,
                | long iRibbonRelimitationMode) As HybridShapeFilletTriTangent
                |
                |     Creates a new a tritangent fillet between three skins.
                |
                |     Parameters:
                |
                |         iElement1
                |             First support of fillet.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face.
                |     iElement2
                |         Second support of fillet.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iRemoveElem
                |         Support to remove of fillet.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iOrientation1
                |         Manage the fillet center position.
                |     iOrientation2
                |         Manage the fillet center position.
                |     iRemoveOrientation
                |         Manage the fillet center position.
                |     iSupportsTrimMode
                |         The 2 supports can be trimmed and assembled with the fillet. Value can
                |         be 0 (No trim ) or 1 (Trim)
                |     iRibbonRelimitationMode
                |         Manage the relimition of fillet extremities.
                |         Value can be : 0 (Smooth), 1 (Straight), 2 (Maximum) or 3 (Minimum)
                |     oFillet
                |         Created fillet.

        :param Reference i_element1:
        :param Reference i_element2:
        :param Reference i_remove_elem:
        :param int i_orientation1:
        :param int i_orientation2:
        :param int i_remove_orientation:
        :param int i_supports_trim_mode:
        :param int i_ribbon_relimitation_mode:
        :return: HybridShapeFilletTriTangent
        :rtype: HybridShapeFilletTriTangent
        """
        return HybridShapeFilletTriTangent(
            self.hybrid_shape_factory.AddNewFilletTriTangent(i_element1.com_object, i_element2.com_object,
                                                             i_remove_elem.com_object, i_orientation1, i_orientation2,
                                                             i_remove_orientation, i_supports_trim_mode,
                                                             i_ribbon_relimitation_mode))

    def add_new_healing(self, i_body_toheal: Reference) -> HybridShapeHealing:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewHealing(Reference iBodyToheal) As
                | HybridShapeHealing
                |
                |     Creates a new healing within the current body.
                |
                |     Parameters:
                |
                |         iBodyToHeal
                |             The body to heal
                |         oHealing
                |             The created healing

        :param Reference i_body_toheal:
        :return: HybridShapeHealing
        :rtype: HybridShapeHealing
        """
        return HybridShapeHealing(self.hybrid_shape_factory.AddNewHealing(i_body_toheal.com_object))

    def add_new_helix(self, i_axis: Reference, i_invert_axis: bool, i_starting_point: Reference, i_pitch: float,
                      i_height: float, i_clockwise_revolution: bool, i_starting_angle: float, i_taper_angle: float,
                      i_taper_outward: bool) -> HybridShapeHelix:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewHelix(Reference iAxis,
                | boolean iInvertAxis,
                | Reference iStartingPoint,
                | double iPitch,
                | double iHeight,
                | boolean iClockwiseRevolution,
                | double iStartingAngle,
                | double iTaperAngle,
                | boolean iTaperOutward) As HybridShapeHelix
                |
                |     Creates a new Helix within the current body.
                |
                |     Parameters:
                |
                |         iAxis
                |             The helix axis (always a line).
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see RectilinearTriDimFeatEdge and
                |         RectilinearBiDimFeatEdge.
                |     iInvertAxis
                |     iStartingPoint
                |         Starting Point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iPitch
                |         Pitch.
                |     iHeight
                |         Helix height.
                |     iClockwiseRevolution
                |         Revolutions are clockwise if TRUE, counterclockwise if FALSE.
                |
                |     iStartingAngle
                |         Starting angle from starting point measured on the helix itself. If no
                |         starting angle is wanted, set it to 0.0.
                |     iTaperAngle
                |         0 <= Taper Angle < Pi/2 If no taper angle is wanted, set it to 0.0
                |         (constant helix radius).
                |     iTaperOutward
                |         Helix radius increases if TRUE, decreases if FALSE.
                |     oHelix
                |         The Helix object if succeded

        :param Reference i_axis:
        :param bool i_invert_axis:
        :param Reference i_starting_point:
        :param float i_pitch:
        :param float i_height:
        :param bool i_clockwise_revolution:
        :param float i_starting_angle:
        :param float i_taper_angle:
        :param bool i_taper_outward:
        :return: HybridShapeHelix
        :rtype: HybridShapeHelix
        """
        return HybridShapeHelix(
            self.hybrid_shape_factory.AddNewHelix(i_axis.com_object, i_invert_axis, i_starting_point.com_object,
                                                  i_pitch, i_height, i_clockwise_revolution, i_starting_angle,
                                                  i_taper_angle, i_taper_outward))

    def add_new_hybrid_scaling(self, i_elem_to_scale: Reference, i_center: Reference,
                               i_ratio: float) -> HybridShapeScaling:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewHybridScaling(Reference iElemToScale,
                | Reference iCenter,
                | double iRatio) As HybridShapeScaling
                |
                |     Creates a new scaling within the current body.
                |
                |     Parameters:
                |
                |         iElemToScale
                |             Point, curve, surface or solid to transform.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face, TriDimFeatEdge, BiDimFeatEdge and Vertex.
                |
                |     iCenter
                |         Reference point or reference plane.
                |         Sub-element(s) supported (see Boundary object): see PlanarFace and
                |         Vertex.
                |     iRatio
                |         Scaling ratio.
                |     oScaling
                |         Created scaling.

        :param Reference i_elem_to_scale:
        :param Reference i_center:
        :param float i_ratio:
        :return: HybridShapeScaling
        :rtype: HybridShapeScaling
        """
        return HybridShapeScaling(
            self.hybrid_shape_factory.AddNewHybridScaling(i_elem_to_scale.com_object, i_center.com_object, i_ratio))

    def add_new_hybrid_split(self, i_element1: Reference, i_element2: Reference,
                             i_orientation: int) -> HybridShapeSplit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewHybridSplit(Reference iElement1,
                | Reference iElement2,
                | long iOrientation) As HybridShapeSplit
                |
                |     Creates a new Split within the current body.
                |
                |     Parameters:
                |
                |         iElement1
                |             The feature to cut (curve or surface).
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face, TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iElement2
                |         The cutting feature (point, curve, surface).
                |         Sub-element(s) supported (see Boundary object): see Face,
                |         TriDimFeatEdge, BiDimFeatEdge and Vertex.
                |     iOrientation
                |         Manage the kept side of the feature to cut (value can be 1 or -1)
                |
                |     oSplit
                |         Created split

        :param Reference i_element1:
        :param Reference i_element2:
        :param int i_orientation:
        :return: HybridShapeSplit
        :rtype: HybridShapeSplit
        """
        return HybridShapeSplit(
            self.hybrid_shape_factory.AddNewHybridSplit(i_element1.com_object, i_element2.com_object, i_orientation))

    def add_new_hybrid_trim(self, i_element1: Reference, i_orientation1: int, i_element2: Reference,
                            i_orientation2: int) -> HybridShapeTrim:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewHybridTrim(Reference iElement1,
                | long iOrientation1,
                | Reference iElement2,
                | long iOrientation2) As HybridShapeTrim
                |
                |     Creates a new Trim within the current body by cutting and joining two
                |     elements.
                |     You can trim a surface by a surface or a curve by a curve.
                |
                |     Parameters:
                |
                |         iElement1
                |             The feature to trim (curve or surface).
                |         iOrientation1
                |             Manage the kept side of iElement1 (value can be 1 or -1).
                |
                |         iElement2
                |             The second feature to trim (curve or surface).
                |         iOrientation2
                |             Manage the kept side of iElement2 (value can be 1 or -1).
                |
                |         oTrim
                |             Created trim.

        :param Reference i_element1:
        :param int i_orientation1:
        :param Reference i_element2:
        :param int i_orientation2:
        :return: HybridShapeTrim
        :rtype: HybridShapeTrim
        """
        return HybridShapeTrim(
            self.hybrid_shape_factory.AddNewHybridTrim(i_element1.com_object, i_orientation1, i_element2.com_object,
                                                       i_orientation2))

    def add_new_integrated_law(self, i_type: int) -> HybridShapeIntegratedLaw:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewIntegratedLaw(long iType) As
                | HybridShapeIntegratedLaw
                |
                |     Creates Integrated Law.
                |
                |     Parameters:
                |
                |         iType
                |             Type of law =
                |             0 : None | 1 : Constant | 2 : Linear | 3 : SType | 4 : Advanced | 5 : Implicit

        :param int i_type:
        :return: HybridShapeIntegratedLaw
        :rtype: HybridShapeIntegratedLaw
        """
        return HybridShapeIntegratedLaw(self.hybrid_shape_factory.AddNewIntegratedLaw(i_type))

    def add_new_intersection(self, i_object1: Reference, i_object2: Reference) -> HybridShapeIntersection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewIntersection(Reference iObject1,
                | Reference iObject2) As HybridShapeIntersection
                |
                |     Creates a new Intersection within the current body.
                |
                |     Parameters:
                |
                |         iObject1
                |             First element ( line, curve, plane, surface.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face, RectilinearTriDimFeatEdge and
                |         RectilinearBiDimFeatEdge.
                |     iObject2
                |         Second element ( line , curve, plane, surface.
                |         Sub-element(s) supported (see Boundary object): see Face,
                |         RectilinearTriDimFeatEdge and
                |         RectilinearBiDimFeatEdge.
                |     oIntersection
                |         Intersection

        :param Reference i_object1:
        :param Reference i_object2:
        :return: HybridShapeIntersection
        :rtype: HybridShapeIntersection
        """
        return HybridShapeIntersection(
            self.hybrid_shape_factory.AddNewIntersection(i_object1.com_object, i_object2.com_object))

    def add_new_inverse(self, element: Reference, inverse: int) -> HybridShapeInverse:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewInverse(Reference Element,
                | long Inverse) As HybridShapeInverse
                |
                |     Creates a new Inverse within the current body.
                |
                |     Parameters:
                |
                |         iElement
                |             The objet to inverse
                |         iInverse
                |             the type of inversion (see CATGSMOrientation.h) 1 for no inversion
                |             -1 for inversion
                |         oInv
                |             The inverted object

        :param Reference element:
        :param int inverse:
        :return: HybridShapeInverse
        :rtype: HybridShapeInverse
        """
        return HybridShapeInverse(self.hybrid_shape_factory.AddNewInverse(element.com_object, inverse))

    def add_new_join(self, element1: Reference, element2: Reference) -> HybridShapeAssemble:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewJoin(Reference Element1,
                | Reference Element2) As HybridShapeAssemble
                |
                |     Creates a new Join within the current body.
                |
                |     Parameters:
                |
                |         iElement1
                |             First element to join ( curve or surface.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face, TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iElement2
                |         Second element to join ( same type of the first
                |         element)
                |
                |         Sub-element(s) supported (see Boundary object): see Face,
                |         TriDimFeatEdge and BiDimFeatEdge.
                |     oExt
                |         Join result The default value used to join element is
                |         0.001mm

        :param Reference element1:
        :param Reference element2:
        :return: HybridShapeAssemble
        :rtype: HybridShapeAssemble
        """
        return HybridShapeAssemble(self.hybrid_shape_factory.AddNewJoin(element1.com_object, element2.com_object))

    def add_new_law_dist_proj(self, i_reference: Reference, i_definition: Reference) -> HybridShapeLawDistProj:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLawDistProj(Reference iReference,
                | Reference iDefinition) As HybridShapeLawDistProj
                |
                |     Creates a new law within the current body.
                |
                |     Parameters:
                |
                |         iReference
                |             Reference line of the law.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see RectilinearTriDimFeatEdge and
                |         RectilinearBiDimFeatEdge.
                |     iDefinition
                |         Definition curve of the law.
                |         Sub-element(s) supported (see Boundary object): see TriDimFeatEdge and
                |         BiDimFeatEdge.
                |     oLaw
                |         The Law object if succeded

        :param Reference i_reference:
        :param Reference i_definition:
        :return: HybridShapeLawDistProj
        :rtype: HybridShapeLawDistProj
        """
        return HybridShapeLawDistProj(
            self.hybrid_shape_factory.AddNewLawDistProj(i_reference.com_object, i_definition.com_object))

    def add_new_line_angle(self, i_curve: Reference, i_surface: Reference, i_point: Reference, i_geodesic: bool,
                           i_begin_offset: float, i_end_offset: float, i_angle: float,
                           i_orientation: bool) -> HybridShapeLineAngle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLineAngle(Reference iCurve,
                | Reference iSurface,
                | Reference iPoint,
                | boolean iGeodesic,
                | double iBeginOffset,
                | double iEndOffset,
                | double iAngle,
                | boolean iOrientation) As HybridShapeLineAngle
                |
                |     Creates a new angle line within the current body.
                |
                |     Parameters:
                |
                |         iCurve
                |             Reference curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iSurface
                |         Reference surface.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iPoint
                |         reference point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iGeodesic
                |         Puts the line on the surface
                |     iBeginOffset
                |         start offset
                |     iEndOffset
                |         end offset
                |     iAngle
                |         angle to reference curve
                |     iOrientation
                |         Orientation allows to reverse the line direction from the reference
                |         point. For a line of L length, it is the same as creating this line with -L
                |         length.
                |     oLine
                |         Created line

        :param Reference i_curve:
        :param Reference i_surface:
        :param Reference i_point:
        :param bool i_geodesic:
        :param float i_begin_offset:
        :param float i_end_offset:
        :param float i_angle:
        :param bool i_orientation:
        :return: HybridShapeLineAngle
        :rtype: HybridShapeLineAngle
        """
        return HybridShapeLineAngle(
            self.hybrid_shape_factory.AddNewLineAngle(i_curve.com_object, i_surface.com_object, i_point.com_object,
                                                      i_geodesic, i_begin_offset, i_end_offset, i_angle, i_orientation))

    def add_new_line_bi_tangent(self, i_curve1: Reference, i_element2: Reference,
                                i_support: Reference) -> HybridShapeLineBiTangent:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLineBiTangent(Reference iCurve1,
                | Reference iElement2,
                | Reference iSupport) As HybridShapeLineBiTangent
                |
                |     Creates a new bitangent line within the current body.
                |
                |     Parameters:
                |
                |         iCurve1
                |             First tangency curve lying on the support surface.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iCurve2
                |         Second tangency element (point, curve) lying on the support
                |         surface.
                |         Sub-element(s) supported (see Boundary object): see TriDimFeatEdge,
                |         BiDimFeatEdge and Vertex.
                |     iSupport
                |         The support surface of the two elements.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     oLine
                |         Created line

        :param Reference i_curve1:
        :param Reference i_element2:
        :param Reference i_support:
        :return: HybridShapeLineBiTangent
        :rtype: HybridShapeLineBiTangent
        """
        return HybridShapeLineBiTangent(
            self.hybrid_shape_factory.AddNewLineBiTangent(i_curve1.com_object, i_element2.com_object,
                                                          i_support.com_object))

    def add_new_line_bisecting(self, i_line1: Reference, i_line2: Reference, i_begin_offset: float, i_end_offset: float,
                               i_orientation: bool, solution_nb: int) -> HybridShapeLineBisecting:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLineBisecting(Reference iLine1,
                | Reference iLine2,
                | double iBeginOffset,
                | double iEndOffset,
                | boolean iOrientation,
                | long SolutionNb) As HybridShapeLineBisecting
                |
                |     Creates a new bisecting line within the current body.
                |
                |     Parameters:
                |
                |         iLine1
                |             First line.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see RectilinearTriDimFeatEdge and
                |         RectilinearBiDimFeatEdge.
                |     iLine2
                |         Second line.
                |         Sub-element(s) supported (see Boundary object): see
                |         RectilinearTriDimFeatEdge and
                |         RectilinearBiDimFeatEdge.
                |     iBeginOffset
                |         start offset
                |     iEndOffset
                |         end offset
                |     iOrientation
                |         Orientation allows to reverse the line direction from the reference
                |         point. For a line of L length, it is the same as creating this line with -L
                |         length.
                |     oLine
                |         Created line

        :param Reference i_line1:
        :param Reference i_line2:
        :param float i_begin_offset:
        :param float i_end_offset:
        :param bool i_orientation:
        :param int solution_nb:
        :return: HybridShapeLineBisecting
        :rtype: HybridShapeLineBisecting
        """
        return HybridShapeLineBisecting(
            self.hybrid_shape_factory.AddNewLineBisecting(i_line1.com_object, i_line2.com_object, i_begin_offset,
                                                          i_end_offset, i_orientation, solution_nb))

    def add_new_line_bisecting_on_support(self, i_line1: Reference, i_line2: Reference, i_surface: Reference,
                                          i_begin_offset: float, i_end_offset: float, i_orientation: bool,
                                          solution_nb: int) -> HybridShapeLineBisecting:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLineBisectingOnSupport(Reference iLine1,
                | Reference iLine2,
                | Reference iSurface,
                | double iBeginOffset,
                | double iEndOffset,
                | boolean iOrientation,
                | long SolutionNb) As HybridShapeLineBisecting
                |
                |     Creates a new bisecting line on a support within the current
                |     body.
                |
                |     Parameters:
                |
                |         iLine1
                |             First line.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see RectilinearTriDimFeatEdge and
                |         RectilinearBiDimFeatEdge.
                |     iLine2
                |         Second line.
                |         Sub-element(s) supported (see Boundary object): see
                |         RectilinearTriDimFeatEdge and
                |         RectilinearBiDimFeatEdge.
                |     iSurface
                |         Reference surface.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iBeginOffset
                |         start offset
                |     iEndOffset
                |         end offset
                |     iOrientation
                |         Orientation allows to reverse the line direction from the reference
                |         point. For a line of L length, it is the same as creating this line with -L
                |         length.
                |     oLine
                |         Created line

        :param Reference i_line1:
        :param Reference i_line2:
        :param Reference i_surface:
        :param float i_begin_offset:
        :param float i_end_offset:
        :param bool i_orientation:
        :param int solution_nb:
        :return: HybridShapeLineBisecting
        :rtype: HybridShapeLineBisecting
        """
        return HybridShapeLineBisecting(
            self.hybrid_shape_factory.AddNewLineBisectingOnSupport(i_line1.com_object, i_line2.com_object,
                                                                   i_surface.com_object, i_begin_offset, i_end_offset,
                                                                   i_orientation, solution_nb))

    def add_new_line_bisecting_on_support_with_point(self, i_line1: Reference, i_line2: Reference,
                                                     i_ref_point: Reference, i_surface: Reference,
                                                     i_begin_offset: float, i_end_offset: float, i_orientation: bool,
                                                     solution_nb: int) -> HybridShapeLineBisecting:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLineBisectingOnSupportWithPoint(Reference
                | iLine1,
                | Reference iLine2,
                | Reference iRefPoint,
                | Reference iSurface,
                | double iBeginOffset,
                | double iEndOffset,
                | boolean iOrientation,
                | long SolutionNb) As HybridShapeLineBisecting
                |
                |     Creates a new bisecting line on a support with a atarting point within the
                |     current body.
                |
                |     Parameters:
                |
                |         iLine1
                |             First line.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see RectilinearTriDimFeatEdge and
                |         RectilinearBiDimFeatEdge.
                |     iLine2
                |         Second line.
                |         Sub-element(s) supported (see Boundary object): see
                |         RectilinearTriDimFeatEdge and
                |         RectilinearBiDimFeatEdge.
                |     iRefPoint
                |         Starting point of the bisecting line.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iSurface
                |         Reference surface.
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iBeginOffset
                |         start offset
                |     iEndOffset
                |         end offset
                |     iOrientation
                |         Orientation allows to reverse the line direction from the reference
                |         point. For a line of L length, it is the same as creating this line with -L
                |         length.
                |     oLine
                |         Created line

        :param Reference i_line1:
        :param Reference i_line2:
        :param Reference i_ref_point:
        :param Reference i_surface:
        :param float i_begin_offset:
        :param float i_end_offset:
        :param bool i_orientation:
        :param int solution_nb:
        :return: HybridShapeLineBisecting
        :rtype: HybridShapeLineBisecting
        """
        return HybridShapeLineBisecting(
            self.hybrid_shape_factory.AddNewLineBisectingOnSupportWithPoint(i_line1.com_object, i_line2.com_object,
                                                                            i_ref_point.com_object,
                                                                            i_surface.com_object, i_begin_offset,
                                                                            i_end_offset, i_orientation, solution_nb))

    def add_new_line_bisecting_with_point(self, i_line1: Reference, i_line2: Reference, i_ref_point: Reference,
                                          i_begin_offset: float, i_end_offset: float, i_orientation: bool,
                                          solution_nb: int) -> HybridShapeLineBisecting:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLineBisectingWithPoint(Reference iLine1,
                | Reference iLine2,
                | Reference iRefPoint,
                | double iBeginOffset,
                | double iEndOffset,
                | boolean iOrientation,
                | long SolutionNb) As HybridShapeLineBisecting
                |
                |     Creates a new bisecting line with a starting point within the current
                |     body.
                |
                |     Parameters:
                |
                |         iLine1
                |             First line.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see RectilinearTriDimFeatEdge and
                |         RectilinearBiDimFeatEdge.
                |     iLine2
                |         Second line.
                |         Sub-element(s) supported (see Boundary object): see
                |         RectilinearTriDimFeatEdge and
                |         RectilinearBiDimFeatEdge.
                |     iRefPoint
                |         Starting point of the bisecting line.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iBeginOffset
                |         start offset
                |     iEndOffset
                |         end offset
                |     iOrientation
                |         Orientation allows to reverse the line direction from the reference
                |         point. For a line of L length, it is the same as creating this line with -L
                |         length.
                |     oLine
                |         Created line

        :param Reference i_line1:
        :param Reference i_line2:
        :param Reference i_ref_point:
        :param float i_begin_offset:
        :param float i_end_offset:
        :param bool i_orientation:
        :param int solution_nb:
        :return: HybridShapeLineBisecting
        :rtype: HybridShapeLineBisecting
        """
        return HybridShapeLineBisecting(
            self.hybrid_shape_factory.AddNewLineBisectingWithPoint(i_line1.com_object, i_line2.com_object,
                                                                   i_ref_point.com_object, i_begin_offset, i_end_offset,
                                                                   i_orientation, solution_nb))

    def add_new_line_datum(self, i_object: Reference) -> HybridShapeLineExplicit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLineDatum(Reference iObject) As
                | HybridShapeLineExplicit
                |
                |     Creates a new datum of line within the current body.
                |
                |     Parameters:
                |
                |         iObject
                |             The object whose topological body will be duplicated and put into
                |             created datum
                |         oLine
                |             Created datum Note2: the object passed as parameter to create the
                |             datum has to be in the current container. Otherwise, an error
                |             occurs.

        :param Reference i_object:
        :return: HybridShapeLineExplicit
        :rtype: HybridShapeLineExplicit
        """
        return HybridShapeLineExplicit(self.hybrid_shape_factory.AddNewLineDatum(i_object.com_object))

    def add_new_line_normal(self, i_surface: Reference, i_point: Reference, i_begin_offset: float, i_end_offset: float,
                            i_orientation: bool) -> HybridShapeLineNormal:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLineNormal(Reference iSurface,
                | Reference iPoint,
                | double iBeginOffset,
                | double iEndOffset,
                | boolean iOrientation) As HybridShapeLineNormal
                |
                |     Creates a new normal line within the current body.
                |
                |     Parameters:
                |
                |         iSurface
                |             Reference surface.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face.
                |     iPoint
                |         Reference point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iBeginOffset
                |         start offset
                |     iEndOffset
                |         end offset
                |     iOrientation
                |         Orientation allows to reverse the line direction from the reference
                |         point. For a line of L length, it is the same as creating this line with -L
                |         length.
                |     oLine
                |         Created line

        :param Reference i_surface:
        :param Reference i_point:
        :param float i_begin_offset:
        :param float i_end_offset:
        :param bool i_orientation:
        :return: HybridShapeLineNormal
        :rtype: HybridShapeLineNormal
        """
        return HybridShapeLineNormal(
            self.hybrid_shape_factory.AddNewLineNormal(i_surface.com_object, i_point.com_object, i_begin_offset,
                                                       i_end_offset, i_orientation))

    def add_new_line_pt_dir(self, i_pt: Reference, i_direction: HybridShapeDirection, i_begin_offset: float,
                            i_end_offset: float, i_orientation: bool) -> HybridShapeLinePtDir:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLinePtDir(Reference iPt,
                | HybridShapeDirection iDirection,
                | double iBeginOffset,
                | double iEndOffset,
                | boolean iOrientation) As HybridShapeLinePtDir
                |
                |     Creates a new point-direction line within the current
                |     body.
                |
                |     Parameters:
                |
                |         iPt
                |             reference point.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iDirection
                |         Direction
                |     iBeginOffset
                |         start offset
                |     iEndOffset
                |         end offset
                |     iOrientation
                |         Orientation allows to reverse the line direction from the reference
                |         point. For a line of L length, it is the same as creating this line with -L
                |         length.
                |     oLine
                |         Created line

        :param Reference i_pt:
        :param HybridShapeDirection i_direction:
        :param float i_begin_offset:
        :param float i_end_offset:
        :param bool i_orientation:
        :return: HybridShapeLinePtDir
        :rtype: HybridShapeLinePtDir
        """
        return HybridShapeLinePtDir(
            self.hybrid_shape_factory.AddNewLinePtDir(i_pt.com_object, i_direction.com_object, i_begin_offset,
                                                      i_end_offset, i_orientation))

    def add_new_line_pt_dir_on_support(self, i_pt: Reference, i_direction: HybridShapeDirection, i_support: Reference,
                                       i_begin_offset: float, i_end_offset: float,
                                       i_orientation: bool) -> HybridShapeLinePtDir:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLinePtDirOnSupport(Reference iPt,
                | HybridShapeDirection iDirection,
                | Reference iSupport,
                | double iBeginOffset,
                | double iEndOffset,
                | boolean iOrientation) As HybridShapeLinePtDir
                |
                |     Creates a new point-direction line within the current
                |     body.
                |
                |     Parameters:
                |
                |         iPt
                |             reference point.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iDirection
                |         Direction
                |     iSupport
                |         Support element (surface or plane)
                |
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iBeginOffset
                |         start offset
                |     iEndOffset
                |         end offset
                |     iOrientation
                |         Orientation allows to reverse the line direction from the reference
                |         point. For a line of L length, it is the same as creating this line with -L
                |         length.
                |     oLine
                |         Created line

        :param Reference i_pt:
        :param HybridShapeDirection i_direction:
        :param Reference i_support:
        :param float i_begin_offset:
        :param float i_end_offset:
        :param bool i_orientation:
        :return: HybridShapeLinePtDir
        :rtype: HybridShapeLinePtDir
        """
        return HybridShapeLinePtDir(
            self.hybrid_shape_factory.AddNewLinePtDirOnSupport(i_pt.com_object, i_direction.com_object,
                                                               i_support.com_object, i_begin_offset, i_end_offset,
                                                               i_orientation))

    def add_new_line_pt_pt(self, i_pt_origine: Reference, i_pt_extremite: Reference) -> HybridShapeLinePtPt:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLinePtPt(Reference iPtOrigine,
                | Reference iPtExtremite) As HybridShapeLinePtPt
                |
                |     Creates a new point-point line within the current body.
                |
                |     Parameters:
                |
                |         iPtOrigine
                |             Origin point.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iPtExtremite
                |         Extremity point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     oLine
                |         Created line

        :param Reference i_pt_origine:
        :param Reference i_pt_extremite:
        :return: HybridShapeLinePtPt
        :rtype: HybridShapeLinePtPt
        """
        return HybridShapeLinePtPt(
            self.hybrid_shape_factory.AddNewLinePtPt(i_pt_origine.com_object, i_pt_extremite.com_object))

    def add_new_line_pt_pt_extended(self, i_pt_origine: Reference, i_pt_extremite: Reference, i_begin_offset: float,
                                    i_end_offset: float) -> HybridShapeLinePtPt:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLinePtPtExtended(Reference iPtOrigine,
                | Reference iPtExtremite,
                | double iBeginOffset,
                | double iEndOffset) As HybridShapeLinePtPt
                |
                |     Creates a new point-point line with extensions within the current
                |     body.
                |
                |     Parameters:
                |
                |         iPtOrigine
                |             Origin point.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iPtExtremite
                |         Extremity point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iBeginOffset
                |         start offset
                |     iEndOffset
                |         end offset
                |     oLine
                |         Created line

        :param Reference i_pt_origine:
        :param Reference i_pt_extremite:
        :param float i_begin_offset:
        :param float i_end_offset:
        :return: HybridShapeLinePtPt
        :rtype: HybridShapeLinePtPt
        """
        return HybridShapeLinePtPt(
            self.hybrid_shape_factory.AddNewLinePtPtExtended(i_pt_origine.com_object, i_pt_extremite.com_object,
                                                             i_begin_offset, i_end_offset))

    def add_new_line_pt_pt_on_support(self, i_pt_origine: Reference, i_pt_extremite: Reference,
                                      i_support: Reference) -> HybridShapeLinePtPt:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLinePtPtOnSupport(Reference iPtOrigine,
                | Reference iPtExtremite,
                | Reference iSupport) As HybridShapeLinePtPt
                |
                |     Creates a new point-point line with support within the current
                |     body.
                |
                |     Parameters:
                |
                |         iPtOrigine
                |             Origin point.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iPtExtremite
                |         Extremity point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iSupport
                |         Support element (surface or plane)
                |
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     oLine
                |         Created line

        :param Reference i_pt_origine:
        :param Reference i_pt_extremite:
        :param Reference i_support:
        :return: HybridShapeLinePtPt
        :rtype: HybridShapeLinePtPt
        """
        return HybridShapeLinePtPt(
            self.hybrid_shape_factory.AddNewLinePtPtOnSupport(i_pt_origine.com_object, i_pt_extremite.com_object,
                                                              i_support.com_object))

    def add_new_line_pt_pt_on_support_extended(self, i_pt_origine: Reference, i_pt_extremite: Reference,
                                               i_support: Reference, i_begin_offset: float,
                                               i_end_offset: float) -> HybridShapeLinePtPt:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLinePtPtOnSupportExtended(Reference iPtOrigine,
                | Reference iPtExtremite,
                | Reference iSupport,
                | double iBeginOffset,
                | double iEndOffset) As HybridShapeLinePtPt
                |
                |     Creates a new point-point line with extensions and with support within the
                |     current body.
                |
                |     Parameters:
                |
                |         iPtOrigine
                |             Origin point.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iPtExtremite
                |         Extremity point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iSupport
                |         Support element (surface or plane)
                |
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iBeginOffset
                |         start offset
                |     iEndOffset
                |         end offset
                |     oLine
                |         Created line

        :param Reference i_pt_origine:
        :param Reference i_pt_extremite:
        :param Reference i_support:
        :param float i_begin_offset:
        :param float i_end_offset:
        :return: HybridShapeLinePtPt
        :rtype: HybridShapeLinePtPt
        """
        return HybridShapeLinePtPt(self.hybrid_shape_factory.AddNewLinePtPtOnSupportExtended(i_pt_origine.com_object,
                                                                                             i_pt_extremite.com_object,
                                                                                             i_support.com_object,
                                                                                             i_begin_offset,
                                                                                             i_end_offset))

    def add_new_line_tangency(self, i_curve: Reference, i_point: Reference, i_begin_offset: float, i_end_offset: float,
                              i_orientation: bool) -> HybridShapeLineTangency:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLineTangency(Reference iCurve,
                | Reference iPoint,
                | double iBeginOffset,
                | double iEndOffset,
                | boolean iOrientation) As HybridShapeLineTangency
                |
                |     Creates a new tangent line within the current body.
                |
                |     Parameters:
                |
                |         iCurve
                |             Reference curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iPoint
                |         Reference point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iBeginOffset
                |         start offset
                |     iEndOffset
                |         end offset
                |     iOrientation
                |         Orientation allows to reverse the line direction from the reference
                |         point. For a line of L length, it is the same as creating this line with -L
                |         length.
                |     oLine
                |         Created line

        :param Reference i_curve:
        :param Reference i_point:
        :param float i_begin_offset:
        :param float i_end_offset:
        :param bool i_orientation:
        :return: HybridShapeLineTangency
        :rtype: HybridShapeLineTangency
        """
        return HybridShapeLineTangency(
            self.hybrid_shape_factory.AddNewLineTangency(i_curve.com_object, i_point.com_object, i_begin_offset,
                                                         i_end_offset, i_orientation))

    def add_new_line_tangency_on_support(self, i_curve: Reference, i_point: Reference, i_support: Reference,
                                         i_begin_offset: float, i_end_offset: float,
                                         i_orientation: bool) -> HybridShapeLineTangency:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLineTangencyOnSupport(Reference iCurve,
                | Reference iPoint,
                | Reference iSupport,
                | double iBeginOffset,
                | double iEndOffset,
                | boolean iOrientation) As HybridShapeLineTangency
                |
                |     Creates a new tangent line within the current body.
                |
                |     Parameters:
                |
                |         iCurve
                |             Reference curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iPoint
                |         Reference point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iSupport
                |         Support element (surface or plane)
                |
                |         Sub-element(s) supported (see Boundary object): see
                |         Face.
                |     iBeginOffset
                |         start offset
                |     iEndOffset
                |         end offset
                |     iOrientation
                |         Orientation allows to reverse the line direction from the reference
                |         point. For a line of L length, it is the same as creating this line with -L
                |         length.
                |     oLine
                |         Created line

        :param Reference i_curve:
        :param Reference i_point:
        :param Reference i_support:
        :param float i_begin_offset:
        :param float i_end_offset:
        :param bool i_orientation:
        :return: HybridShapeLineTangency
        :rtype: HybridShapeLineTangency
        """
        return HybridShapeLineTangency(
            self.hybrid_shape_factory.AddNewLineTangencyOnSupport(i_curve.com_object, i_point.com_object,
                                                                  i_support.com_object, i_begin_offset, i_end_offset,
                                                                  i_orientation))

    def add_new_loft(self) -> HybridShapeLoft:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLoft() As HybridShapeLoft
                |
                |     Creates a new Loft within the current body.
                |
                |     Parameters:
                |
                |         oExt
                |             CATIAHybridShapeLoft created

        :return: HybridShapeLoft
        :rtype: HybridShapeLoft
        """
        return HybridShapeLoft(self.hybrid_shape_factory.AddNewLoft())

    def add_new_mid_surface(self, i_support: Reference, i_creation_mode: int,
                            i_threshold: float) -> HybridShapeMidSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewMidSurface(Reference iSupport,
                | long iCreationMode,
                | double iThreshold) As HybridShapeMidSurface
                |
                |     Creates a new MidSurface in Automatic Creation Mode Only.
                |
                |     Parameters:
                |
                |         iSupport
                |             support Body
                |         iCreationMode
                |             Creation Mode (Only Automatic Accepted)
                |         iThreshold
                |             Threshold Thickness
                |
                |     Returns:
                |         oMidSurface Created MidSurface

        :param Reference i_support:
        :param int i_creation_mode:
        :param float i_threshold:
        :return: HybridShapeMidSurface
        :rtype: HybridShapeMidSurface
        """
        return HybridShapeMidSurface(
            self.hybrid_shape_factory.AddNewMidSurface(i_support.com_object, i_creation_mode, i_threshold))

    def add_new_mid_surface_with_auto_threshold(self, i_support: Reference, i_creation_mode: int, i_threshold: float,
                                                i_auto_thickness_threshold: int) -> HybridShapeMidSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewMidSurfaceWithAutoThreshold(Reference iSupport,
                | long iCreationMode,
                | double iThreshold,
                | long iAutoThicknessThreshold) As HybridShapeMidSurface
                |
                |     Creates a new MidSurface in Automatic Creation Mode Only.
                |
                |     Parameters:
                |
                |         iSupport
                |             support Body
                |         iCreationMode
                |             Creation Mode (Only Automatic Accepted)
                |         iThreshold
                |             Threshold Thickness
                |         iAutoThicknessThreshold
                |             Automatic Thickness Threshold
                |
                |     Returns:
                |         oMidSurface Created MidSurface

        :param Reference i_support:
        :param int i_creation_mode:
        :param float i_threshold:
        :param int i_auto_thickness_threshold:
        :return: HybridShapeMidSurface
        :rtype: HybridShapeMidSurface
        """
        return HybridShapeMidSurface(
            self.hybrid_shape_factory.AddNewMidSurfaceWithAutoThreshold(i_support.com_object, i_creation_mode,
                                                                        i_threshold, i_auto_thickness_threshold))

    def add_new_near(self, multi_element: Reference, reference_element: Reference) -> HybridShapeNear:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewNear(Reference MultiElement,
                | Reference ReferenceElement) As HybridShapeNear
                |
                |     Creates a new Near within the current body.
                |
                |     Parameters:
                |
                |         iMultiElement
                |             Non connex element (point,curve,surface.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face, TriDimFeatEdge, BiDimFeatEdge and Vertex.
                |
                |     iReferenceElement
                |         Reference element
                |
                |         Sub-element(s) supported (see Boundary object): see Face,
                |         TriDimFeatEdge, BiDimFeatEdge and Vertex.
                |     oNear
                |         The result is the connex component that is the nearest from the
                |         reference element

        :param Reference multi_element:
        :param Reference reference_element:
        :return: HybridShapeNear
        :rtype: HybridShapeNear
        """
        return HybridShapeNear(
            self.hybrid_shape_factory.AddNewNear(multi_element.com_object, reference_element.com_object))

    def add_new_offset(self, i_object_to_offset: Reference, i_offset: float, i_orientation: bool,
                       i_precision: float) -> HybridShapeOffset:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewOffset(Reference iObjectToOffset,
                | double iOffset,
                | boolean iOrientation,
                | double iPrecision) As HybridShapeOffset
                |
                |     Creates a new offset within the current body.
                |
                |     Parameters:
                |
                |         iObjectToOffset
                |             Surface to offset.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face.
                |     iOffset
                |         Offset value
                |     iOrientation
                |         Offset orientation
                |     iPrecision
                |         This variable is no longer in use and any change in it's value does not
                |         impact the output.
                |     oOffsetObject
                |         Offset Surface

        :param Reference i_object_to_offset:
        :param float i_offset:
        :param bool i_orientation:
        :param float i_precision:
        :return: HybridShapeOffset
        :rtype: HybridShapeOffset
        """
        return HybridShapeOffset(
            self.hybrid_shape_factory.AddNewOffset(i_object_to_offset.com_object, i_offset, i_orientation, i_precision))

    def add_new_plane1_curve(self, i_planar_curve: Reference) -> HybridShapePlane1Curve:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPlane1Curve(Reference iPlanarCurve) As
                | HybridShapePlane1Curve
                |
                |     Creates a new plane passing through one planar curve within the current
                |     body.
                |
                |     Parameters:
                |
                |         iPlanarCurve
                |             passing curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     oPlane
                |         Created plane

        :param Reference i_planar_curve:
        :return: HybridShapePlane1Curve
        :rtype: HybridShapePlane1Curve
        """
        return HybridShapePlane1Curve(self.hybrid_shape_factory.AddNewPlane1Curve(i_planar_curve.com_object))

    def add_new_plane1_line1_pt(self, i_ln: Reference, i_pt: Reference) -> HybridShapePlane1Line1Pt:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPlane1Line1Pt(Reference iLn,
                | Reference iPt) As HybridShapePlane1Line1Pt
                |
                |     Creates a new plane passing through 1 line and 1 point within the current
                |     body.
                |
                |     Parameters:
                |
                |         iLn
                |             passing line.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see RectilinearTriDimFeatEdge,
                |         RectilinearBiDimFeatEdge and RectilinearMonoDimFeatEdge.
                |
                |     iPt
                |         passing point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     oPlane
                |         Created plane

        :param Reference i_ln:
        :param Reference i_pt:
        :return: HybridShapePlane1Line1Pt
        :rtype: HybridShapePlane1Line1Pt
        """
        return HybridShapePlane1Line1Pt(self.hybrid_shape_factory.AddNewPlane1Line1Pt(i_ln.com_object, i_pt.com_object))

    def add_new_plane2_lines(self, i_ln1: Reference, i_ln2: Reference) -> HybridShapePlane2Lines:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPlane2Lines(Reference iLn1,
                | Reference iLn2) As HybridShapePlane2Lines
                |
                |     Creates a new plane passing through 2 lines within the current
                |     body.
                |
                |     Parameters:
                |
                |         iLn1
                |             first passing line.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see RectilinearTriDimFeatEdge,
                |         RectilinearBiDimFeatEdge and RectilinearMonoDimFeatEdge.
                |
                |     iLn2
                |         second passing line.
                |         Sub-element(s) supported (see Boundary object): see
                |         RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge and
                |         RectilinearMonoDimFeatEdge.
                |     oPlane
                |         Created line

        :param Reference i_ln1:
        :param Reference i_ln2:
        :return: HybridShapePlane2Lines
        :rtype: HybridShapePlane2Lines
        """
        return HybridShapePlane2Lines(self.hybrid_shape_factory.AddNewPlane2Lines(i_ln1.com_object, i_ln2.com_object))

    def add_new_plane3_points(self, i_pt1: Reference, i_pt2: Reference, i_pt3: Reference) -> HybridShapePlane3Points:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPlane3Points(Reference iPt1,
                | Reference iPt2,
                | Reference iPt3) As HybridShapePlane3Points
                |
                |     Creates a new plane passing through 3 points within the current
                |     body.
                |
                |     Parameters:
                |
                |         iPt1
                |             first passing point.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iPt2
                |         second passing point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iPt3
                |         third passing point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     oPlane
                |         Created plane

        :param Reference i_pt1:
        :param Reference i_pt2:
        :param Reference i_pt3:
        :return: HybridShapePlane3Points
        :rtype: HybridShapePlane3Points
        """
        return HybridShapePlane3Points(
            self.hybrid_shape_factory.AddNewPlane3Points(i_pt1.com_object, i_pt2.com_object, i_pt3.com_object))

    def add_new_plane_angle(self, i_plane: Reference, i_revol_axis: Reference, i_angle: float,
                            i_orientation: bool) -> HybridShapePlaneAngle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPlaneAngle(Reference iPlane,
                | Reference iRevolAxis,
                | double iAngle,
                | boolean iOrientation) As HybridShapePlaneAngle
                |
                |     Creates a new angle plane within the current body.
                |
                |     Parameters:
                |
                |         iPlane
                |             reference plane
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see PlanarFace.
                |     iRevolAxis
                |         rotation axis
                |
                |         Sub-element(s) supported (see Boundary object): see
                |         RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge and
                |         RectilinearMonoDimFeatEdge.
                |     iAngle
                |         angle
                |     iOrientation
                |         Orientation to reverse the plane from the reference plane.
                |
                |     oPlane
                |         Created plane

        :param Reference i_plane:
        :param Reference i_revol_axis:
        :param float i_angle:
        :param bool i_orientation:
        :return: HybridShapePlaneAngle
        :rtype: HybridShapePlaneAngle
        """
        return HybridShapePlaneAngle(
            self.hybrid_shape_factory.AddNewPlaneAngle(i_plane.com_object, i_revol_axis.com_object, i_angle,
                                                       i_orientation))

    def add_new_plane_datum(self, i_object: Reference) -> HybridShapePlaneExplicit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPlaneDatum(Reference iObject) As
                | HybridShapePlaneExplicit
                |
                |     Creates a new datum of plane within the current body.
                |
                |     Parameters:
                |
                |         iObject
                |             The object whose topological body will be duplicated and put into
                |             created datum
                |         oPlane
                |             Created datum Note2: the object passed as parameter to create the
                |             datum has to be in the current container. Otherwise, an error
                |             occurs.

        :param Reference i_object:
        :return: HybridShapePlaneExplicit
        :rtype: HybridShapePlaneExplicit
        """
        return HybridShapePlaneExplicit(self.hybrid_shape_factory.AddNewPlaneDatum(i_object.com_object))

    def add_new_plane_equation(self, i_a_coeff: float, i_b_coeff: float, i_c_coeff: float,
                               i_d_coeff: float) -> HybridShapePlaneEquation:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPlaneEquation(double iA_Coeff,
                | double iB_Coeff,
                | double iC_Coeff,
                | double iD_Coeff) As HybridShapePlaneEquation
                |
                |     Creates a new equation plane within the current body. Plane equation is Ax+By+Cz = D.
                |
                |     Parameters:
                |
                |         iA_Coeff
                |             A coefficient
                |         iB_Coeff
                |             B coefficient
                |         iC_Coeff
                |             C coefficient
                |         iD_Coeff
                |             D coefficient
                |         oPlane
                |             Created plane

        :param float i_a_coeff:
        :param float i_b_coeff:
        :param float i_c_coeff:
        :param float i_d_coeff:
        :return: HybridShapePlaneEquation
        :rtype: HybridShapePlaneEquation
        """
        return HybridShapePlaneEquation(
            self.hybrid_shape_factory.AddNewPlaneEquation(i_a_coeff, i_b_coeff, i_c_coeff, i_d_coeff))

    def add_new_plane_mean(self, i_list_of_points: tuple, nb_point: int) -> HybridShapePlaneMean:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPlaneMean(CATSafeArrayVariant iListOfPoints,
                | long NbPoint) As HybridShapePlaneMean
                |
                |     Creates a new mean through points plane within the current
                |     body.
                |
                |     Parameters:
                |
                |         oIListOfPoints
                |             list of passing points Warning : Input and Output parameter for CATScript applications,
                |             procedural type
                |         iNbPoint
                |             Number of points
                |         oPlane
                |             Created plane

        :param tuple i_list_of_points:
        :param int nb_point:
        :return: HybridShapePlaneMean
        :rtype: HybridShapePlaneMean
        """
        return HybridShapePlaneMean(self.hybrid_shape_factory.AddNewPlaneMean(i_list_of_points, nb_point))

    def add_new_plane_normal(self, i_curve: Reference, i_pt: Reference) -> HybridShapePlaneNormal:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPlaneNormal(Reference iCurve,
                | Reference iPt) As HybridShapePlaneNormal
                |
                |     Creates a new normal plane within the current body.
                |
                |     Parameters:
                |
                |         iCurve
                |             Reference curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iPt
                |         Reference point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     oPlane
                |         Created plane

        :param Reference i_curve:
        :param Reference i_pt:
        :return: HybridShapePlaneNormal
        :rtype: HybridShapePlaneNormal
        """
        return HybridShapePlaneNormal(self.hybrid_shape_factory.AddNewPlaneNormal(i_curve.com_object, i_pt.com_object))

    def add_new_plane_offset(self, i_plane: Reference, i_offset: float, i_orientation: bool) -> HybridShapePlaneOffset:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPlaneOffset(Reference iPlane,
                | double iOffset,
                | boolean iOrientation) As HybridShapePlaneOffset
                |
                |     Creates a new offset plane within the current body.
                |
                |     Parameters:
                |
                |         iPlane
                |             reference plane
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see PlanarFace.
                |     iOffset
                |         offset value
                |     iOrientation
                |         Orientation to reverse the plane from the reference plane.
                |
                |     oPlane
                |         Created plane

        :param Reference i_plane:
        :param float i_offset:
        :param bool i_orientation:
        :return: HybridShapePlaneOffset
        :rtype: HybridShapePlaneOffset
        """
        return HybridShapePlaneOffset(
            self.hybrid_shape_factory.AddNewPlaneOffset(i_plane.com_object, i_offset, i_orientation))

    def add_new_plane_offset_pt(self, i_plane: Reference, i_pt: Reference) -> HybridShapePlaneOffsetPt:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPlaneOffsetPt(Reference iPlane,
                | Reference iPt) As HybridShapePlaneOffsetPt
                |
                |     Creates a new offset trough point plane within the current
                |     body.
                |
                |     Parameters:
                |
                |         iPlane
                |             reference plane
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see PlanarFace.
                |     iPt
                |         Reference point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     oPlane
                |         Created plane

        :param Reference i_plane:
        :param Reference i_pt:
        :return: HybridShapePlaneOffsetPt
        :rtype: HybridShapePlaneOffsetPt
        """
        return HybridShapePlaneOffsetPt(
            self.hybrid_shape_factory.AddNewPlaneOffsetPt(i_plane.com_object, i_pt.com_object))

    def add_new_plane_tangent(self, i_surface: Reference, i_pt: Reference) -> HybridShapePlaneTangent:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPlaneTangent(Reference iSurface,
                | Reference iPt) As HybridShapePlaneTangent
                |
                |     Creates a new tangent plane within the current body.
                |
                |     Parameters:
                |
                |         iSurface
                |             reference surface.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face.
                |     iPt
                |         reference point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     oPlane
                |         Created plane

        :param Reference i_surface:
        :param Reference i_pt:
        :return: HybridShapePlaneTangent
        :rtype: HybridShapePlaneTangent
        """
        return HybridShapePlaneTangent(
            self.hybrid_shape_factory.AddNewPlaneTangent(i_surface.com_object, i_pt.com_object))

    def add_new_point_between(self, i_point1: Reference, i_point2: Reference, i_ratio: float,
                              i_orientation: int) -> HybridShapePointBetween:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointBetween(Reference iPoint1,
                | Reference iPoint2,
                | double iRatio,
                | long iOrientation) As HybridShapePointBetween
                |
                |     Creates a new PointBetween within the current body.
                |
                |     Parameters:
                |
                |         iPoint1
                |             Reference point to compute the barycenter.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iPoint2
                |         Second point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iRatio
                |         barycenter parameter
                |     iOrientation
                |         To compute the barycenter of the segment [Pt1 - Pt2]
                |     oPoint
                |         PointBetween if succeded

        :param Reference i_point1:
        :param Reference i_point2:
        :param float i_ratio:
        :param int i_orientation:
        :return: HybridShapePointBetween
        :rtype: HybridShapePointBetween
        """
        return HybridShapePointBetween(
            self.hybrid_shape_factory.AddNewPointBetween(i_point1.com_object, i_point2.com_object, i_ratio,
                                                         i_orientation))

    def add_new_point_center(self, i_curve: Reference) -> HybridShapePointCenter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointCenter(Reference iCurve) As
                | HybridShapePointCenter
                |
                |     Creates a new circle center point within the current body.
                |
                |     Parameters:
                |
                |         iCurve
                |             Reference circle
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Edge.
                |     oPoint
                |         Created point

        :param Reference i_curve:
        :return: HybridShapePointCenter
        :rtype: HybridShapePointCenter
        """
        return HybridShapePointCenter(self.hybrid_shape_factory.AddNewPointCenter(i_curve.com_object))

    def add_new_point_coord(self, i_x: float, i_y: float, i_z: float) -> HybridShapePointCoord:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointCoord(double iX,
                | double iY,
                | double iZ) As HybridShapePointCoord
                |
                |     Creates a new point defined by its cartesian coordinates within the current
                |     body.
                |
                |     Parameters:
                |
                |         iX
                |             X coordinate for the point
                |         iY
                |             Y coordinate for the point
                |         iZ
                |             Z coordinate for the point
                |         oPoint
                |             Created point

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :return: HybridShapePointCoord
        :rtype: HybridShapePointCoord
        """
        return HybridShapePointCoord(self.hybrid_shape_factory.AddNewPointCoord(i_x, i_y, i_z))

    def add_new_point_coords(self, coord_list):
        """
        coord_list must be a list of iterables of length 3.
        Example: coord_list = [[0, 0, 1], [0, 1, 0]]
        :param list() coord_list:
        :returns: list[HybridShapePointCoord]
        """

        r = []

        for coord in coord_list:
            r.append(self.add_new_point_coord(coord[0], coord[1], coord[2]))

        return r

    def add_new_point_coord_with_reference(self, i_x: float, i_y: float, i_z: float,
                                           i_pt: Reference) -> HybridShapePointCoord:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointCoordWithReference(double iX,
                | double iY,
                | double iZ,
                | Reference iPt) As HybridShapePointCoord
                |
                |     Creates a new point defined its the cartesian coordinates regarding a
                |     reference point.
                |
                |     Parameters:
                |
                |         iX
                |             X coordinate for the point
                |         iY
                |             Y coordinate for the point
                |         iZ
                |             Z coordinate for the point
                |         iPt
                |             Reference point.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     oPoint
                |         Created point

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :param Reference i_pt:
        :return: HybridShapePointCoord
        :rtype: HybridShapePointCoord
        """
        return HybridShapePointCoord(
            self.hybrid_shape_factory.AddNewPointCoordWithReference(i_x, i_y, i_z, i_pt.com_object))

    def add_new_point_datum(self, i_object: Reference) -> HybridShapePointExplicit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointDatum(Reference iObject) As
                | HybridShapePointExplicit
                |
                |     Creates a new datum of point within the current body.
                |
                |     Parameters:
                |
                |         iObject
                |             The object whose topological body will be duplicated and put into
                |             created datum
                |         oPoint
                |             Created datum Note2: the object passed as parameter to create the
                |             datum has to be in the current container. Otherwise, an error
                |             occurs.

        :param Reference i_object:
        :return: HybridShapePointExplicit
        :rtype: HybridShapePointExplicit
        """
        return HybridShapePointExplicit(self.hybrid_shape_factory.AddNewPointDatum(i_object.com_object))

    def add_new_point_on_curve_along_direction(self, i_crv: Reference, i_long: float, i_orientation: bool,
                                               i_direction: HybridShapeDirection) -> HybridShapePointOnCurve:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointOnCurveAlongDirection(Reference iCrv,
                | double iLong,
                | boolean iOrientation,
                | HybridShapeDirection iDirection) As HybridShapePointOnCurve
                |
                |     Creates a new point on a curve with a deafult origin point and from a
                |     distance along direction.
                |
                |     Parameters:
                |
                |         iCrv
                |             support curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iLong
                |         distance to default origin point.(origin of acurrent axis system)
                |
                |     iOrientation
                |         Orientation = TRUE means that distance is measured in the other orientation of the curve.
                |     iDirection
                |         Direction = The distance at which point is created is measured in this direction.
                |     oPoint
                |         Created point

        :param Reference i_crv:
        :param float i_long:
        :param bool i_orientation:
        :param HybridShapeDirection i_direction:
        :return: HybridShapePointOnCurve
        :rtype: HybridShapePointOnCurve
        """
        return HybridShapePointOnCurve(
            self.hybrid_shape_factory.AddNewPointOnCurveAlongDirection(i_crv.com_object, i_long, i_orientation,
                                                                       i_direction.com_object))

    def add_new_point_on_curve_from_distance(self, i_crv: Reference, i_long: float,
                                             i_orientation: bool) -> HybridShapePointOnCurve:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointOnCurveFromDistance(Reference iCrv,
                | double iLong,
                | boolean iOrientation) As HybridShapePointOnCurve
                |
                |     Creates a new point on a curve from a distance to an extremity within the
                |     current body.
                |
                |     Parameters:
                |
                |         iCrv
                |             support curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iLong
                |         distance to extremity
                |     iOrientation
                |         Orientation = TRUE means that distance is measured in the other orientation of the curve and
                |         from the other extremity.
                |     oPoint
                |         Created point

        :param Reference i_crv:
        :param float i_long:
        :param bool i_orientation:
        :return: HybridShapePointOnCurve
        :rtype: HybridShapePointOnCurve
        """
        return HybridShapePointOnCurve(
            self.hybrid_shape_factory.AddNewPointOnCurveFromDistance(i_crv.com_object, i_long, i_orientation))

    def add_new_point_on_curve_from_percent(self, i_crv: Reference, i_long: float,
                                            i_orientation: bool) -> HybridShapePointOnCurve:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointOnCurveFromPercent(Reference iCrv,
                | double iLong,
                | boolean iOrientation) As HybridShapePointOnCurve
                |
                |     Creates a new point on a curve from a ratio of distance to an extremity
                |     within the current body.
                |
                |     Parameters:
                |
                |         iCrv
                |             support curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iLong
                |         Ratio of curve length
                |     iOrientation
                |         Orientation = TRUE means that ratio is measured in the other orientation of the curve and
                |         from the other extremity.
                |     oPoint
                |         Created point

        :param Reference i_crv:
        :param float i_long:
        :param bool i_orientation:
        :return: HybridShapePointOnCurve
        :rtype: HybridShapePointOnCurve
        """
        return HybridShapePointOnCurve(
            self.hybrid_shape_factory.AddNewPointOnCurveFromPercent(i_crv.com_object, i_long, i_orientation))

    def add_new_point_on_curve_with_reference_along_direction(
            self, i_crv: Reference, i_pt: Reference, i_long: float,
            i_orientation: bool,
            i_direction: HybridShapeDirection
    ) -> HybridShapePointOnCurve:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointOnCurveWithReferenceAlongDirection(Reference
                | iCrv,
                | Reference iPt,
                | double iLong,
                | boolean iOrientation,
                | HybridShapeDirection iDirection) As HybridShapePointOnCurve
                |
                |     Creates a new point on a curve with a reference point and from a distance
                |     along direction.
                |
                |     Parameters:
                |
                |         iCrv
                |             support curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iPt
                |         reference point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iLong
                |         distance (length) to reference point
                |     iOrientation
                |         Orientation = TRUE means that distance is measured in the other orientation of the curve
                |     iDirection
                |         Direction = The distance at which point is created is measured in this direction.
                |     oPoint
                |         Created point

        :param Reference i_crv:
        :param Reference i_pt:
        :param float i_long:
        :param bool i_orientation:
        :param HybridShapeDirection i_direction:
        :return: HybridShapePointOnCurve
        :rtype: HybridShapePointOnCurve
        """
        return HybridShapePointOnCurve(
            self.hybrid_shape_factory.AddNewPointOnCurveWithReferenceAlongDirection(i_crv.com_object, i_pt.com_object,
                                                                                    i_long, i_orientation,
                                                                                    i_direction.com_object))

    def add_new_point_on_curve_with_reference_from_distance(self, i_crv: Reference, i_pt: Reference, i_long: float,
                                                            i_orientation: bool) -> HybridShapePointOnCurve:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointOnCurveWithReferenceFromDistance(Reference
                | iCrv,
                | Reference iPt,
                | double iLong,
                | boolean iOrientation) As HybridShapePointOnCurve
                |
                |     Creates a new point on a curve with a reference point and from a distance
                |     within the current body.
                |
                |     Parameters:
                |
                |         iCrv
                |             support curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iPt
                |         reference point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iLong
                |         distance (length) to reference point
                |     iOrientation
                |         Orientation = TRUE means that distance is measured in the other orientation of the curve
                |     oPoint
                |         Created point

        :param Reference i_crv:
        :param Reference i_pt:
        :param float i_long:
        :param bool i_orientation:
        :return: HybridShapePointOnCurve
        :rtype: HybridShapePointOnCurve
        """
        return HybridShapePointOnCurve(
            self.hybrid_shape_factory.AddNewPointOnCurveWithReferenceFromDistance(i_crv.com_object, i_pt.com_object,
                                                                                  i_long, i_orientation))

    def add_new_point_on_curve_with_reference_from_percent(self, i_crv: Reference, i_pt: Reference, i_long: float,
                                                           i_orientation: bool) -> HybridShapePointOnCurve:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointOnCurveWithReferenceFromPercent(Reference
                | iCrv,
                | Reference iPt,
                | double iLong,
                | boolean iOrientation) As HybridShapePointOnCurve
                |
                |     Creates a new point on a curve with a reference point and from a ratio of
                |     distance within the current body.
                |
                |     Parameters:
                |
                |         iCrv
                |             Support curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iPt
                |         reference point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iLong
                |         Ratio of curve length
                |     iOrientation
                |         Orientation = TRUE means that ratio is measured in the other orientation of the curve
                |     oPoint
                |         Created point

        :param Reference i_crv:
        :param Reference i_pt:
        :param float i_long:
        :param bool i_orientation:
        :return: HybridShapePointOnCurve
        :rtype: HybridShapePointOnCurve
        """
        return HybridShapePointOnCurve(
            self.hybrid_shape_factory.AddNewPointOnCurveWithReferenceFromPercent(i_crv.com_object, i_pt.com_object,
                                                                                 i_long, i_orientation))

    def add_new_point_on_plane(self, i_plane: Reference, i_x: float, i_y: float) -> HybridShapePointOnPlane:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointOnPlane(Reference iPlane,
                | double iX,
                | double iY) As HybridShapePointOnPlane
                |
                |     Creates a new point on a plane within the current body.
                |
                |     Parameters:
                |
                |         iPlane
                |             Support plane
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see PlanarFace.
                |     iX
                |         X cartesian coordinates in the plane.
                |     iY
                |         Y cartesian coordinates in the plane.
                |     oPoint
                |         Created point

        :param Reference i_plane:
        :param float i_x:
        :param float i_y:
        :return: HybridShapePointOnPlane
        :rtype: HybridShapePointOnPlane
        """
        return HybridShapePointOnPlane(self.hybrid_shape_factory.AddNewPointOnPlane(i_plane.com_object, i_x, i_y))

    def add_new_point_on_plane_with_reference(self, i_plane: Reference, i_pt: Reference, i_x: float,
                                              i_y: float) -> HybridShapePointOnPlane:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointOnPlaneWithReference(Reference iPlane,
                | Reference iPt,
                | double iX,
                | double iY) As HybridShapePointOnPlane
                |
                |     Creates a new point on a plane with a reference point within the current
                |     body.
                |
                |     Parameters:
                |
                |         iPlane
                |             Support plane
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see PlanarFace.
                |     iPt
                |         Reference plane
                |
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iX
                |         X cartesian coordinates in the plane.
                |     iY
                |         Y cartesian coordinates in the plane.
                |     oPoint
                |         Created point

        :param Reference i_plane:
        :param Reference i_pt:
        :param float i_x:
        :param float i_y:
        :return: HybridShapePointOnPlane
        :rtype: HybridShapePointOnPlane
        """
        return HybridShapePointOnPlane(
            self.hybrid_shape_factory.AddNewPointOnPlaneWithReference(i_plane.com_object, i_pt.com_object, i_x, i_y))

    def add_new_point_on_surface(self, i_surface: Reference, i_direction: HybridShapeDirection,
                                 i_x: float) -> HybridShapePointOnSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointOnSurface(Reference iSurface,
                | HybridShapeDirection iDirection,
                | double iX) As HybridShapePointOnSurface
                |
                |     Creates a new point on a surface within the current body.
                |
                |     Parameters:
                |
                |         iSurface
                |             Support surface.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face.
                |     iDirection
                |         Direction from the reference point in which the point is computed.
                |
                |     iX
                |         geodesic length to reference point
                |     oPoint
                |         Created point

        :param Reference i_surface:
        :param HybridShapeDirection i_direction:
        :param float i_x:
        :return: HybridShapePointOnSurface
        :rtype: HybridShapePointOnSurface
        """
        return HybridShapePointOnSurface(
            self.hybrid_shape_factory.AddNewPointOnSurface(i_surface.com_object, i_direction.com_object, i_x))

    def add_new_point_on_surface_with_reference(self, i_surface: Reference, i_pt: Reference,
                                                i_direction: HybridShapeDirection,
                                                i_x: float) -> HybridShapePointOnSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointOnSurfaceWithReference(Reference iSurface,
                | Reference iPt,
                | HybridShapeDirection iDirection,
                | double iX) As HybridShapePointOnSurface
                |
                |     Creates a new point on a surface with a reference point within the current
                |     body.
                |
                |     Parameters:
                |
                |         iSurface
                |             Support surface.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face.
                |     iPt
                |         reference point.
                |         Sub-element(s) supported (see Boundary object): see
                |         Vertex.
                |     iDirection
                |         Direction from the reference point in which the point is computed.
                |
                |     iX
                |         geodesic length to reference point
                |     oPoint
                |         Created point

        :param Reference i_surface:
        :param Reference i_pt:
        :param HybridShapeDirection i_direction:
        :param float i_x:
        :return: HybridShapePointOnSurface
        :rtype: HybridShapePointOnSurface
        """
        return HybridShapePointOnSurface(
            self.hybrid_shape_factory.AddNewPointOnSurfaceWithReference(i_surface.com_object, i_pt.com_object,
                                                                        i_direction.com_object, i_x))

    def add_new_point_tangent(self, i_curve: Reference, i_direction: HybridShapeDirection) -> HybridShapePointTangent:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPointTangent(Reference iCurve,
                | HybridShapeDirection iDirection) As HybridShapePointTangent
                |
                |     Creates a new tangent to curve point within the current
                |     body.
                |
                |     Parameters:
                |
                |         iCurve
                |             Reference curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Edge.
                |     iDirection
                |         Direction in which tangent points are computed
                |     oPoint
                |         Created point

        :param Reference i_curve:
        :param HybridShapeDirection i_direction:
        :return: HybridShapePointTangent
        :rtype: HybridShapePointTangent
        """
        return HybridShapePointTangent(
            self.hybrid_shape_factory.AddNewPointTangent(i_curve.com_object, i_direction.com_object))

    def add_new_polyline(self) -> HybridShapePolyline:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPolyline() As HybridShapePolyline
                |
                |     Creates a new Polyline within the current body.
                |
                |     Parameters:
                |
                |         oPolyline
                |             The Polyline object if succeded

        :return: HybridShapePolyline
        :rtype: HybridShapePolyline
        """
        return HybridShapePolyline(self.hybrid_shape_factory.AddNewPolyline())

    def add_new_position_transfo(self, i_mode: int) -> HybridShapePositionTransfo:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPositionTransfo(long iMode) As
                | HybridShapePositionTransfo
                |
                |     Creates a new PositionTransfo within the current body.
                |
                |     Parameters:
                |
                |         iMode
                |             Positioning mode.
                |         oExt
                |             Created positioning transformation (i.e. positioned wire /
                |             profile).

        :param int i_mode:
        :return: HybridShapePositionTransfo
        :rtype: HybridShapePositionTransfo
        """
        return HybridShapePositionTransfo(self.hybrid_shape_factory.AddNewPositionTransfo(i_mode))

    def add_new_project(self, i_element: Reference, i_support: Reference) -> HybridShapeProject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewProject(Reference iElement,
                | Reference iSupport) As HybridShapeProject
                |
                |     Creates a new Project within the current body.
                |
                |     Parameters:
                |
                |         iElement
                |             Element to project (point, curve).
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge, BiDimFeatEdge and Vertex.
                |
                |     iSupport
                |         Curve or surface support for projection.
                |         Sub-element(s) supported (see Boundary object): see Face,
                |         TriDimFeatEdge and BiDimFeatEdge.
                |     oProjection
                |         Created projection

        :param Reference i_element:
        :param Reference i_support:
        :return: HybridShapeProject
        :rtype: HybridShapeProject
        """
        return HybridShapeProject(self.hybrid_shape_factory.AddNewProject(i_element.com_object, i_support.com_object))

    def add_new_reflect_line(self, i_support: Reference, i_dir: HybridShapeDirection, i_angle: float,
                             i_orientation_support: int, i_orientation_direction: int) -> HybridShapeReflectLine:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewReflectLine(Reference iSupport,
                | HybridShapeDirection iDir,
                | double iAngle,
                | long iOrientationSupport,
                | long iOrientationDirection) As HybridShapeReflectLine
                |
                |     Deprecated:
                |         V5R17 CATIAHybridShapeFactory#AddNewReflectLineWithType Creates a new
                |         ReflectLine within the current body.
                |         Create a reflectline curve on a support surface along a direction with
                |         an angle.
                |     Parameters:
                |
                |         iSupport
                |             Support surface.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face.
                |     iAngle
                |         Angle of the reflectline.
                |     iOrientationSupport
                |         Manage the angle used to compute the reflectline. Value can be 1 or -1
                |
                |     iOrientationDirection
                |         Manage the angle used to compute the reflectline. Value can be 1 or -1
                |
                |     oReflectLine
                |         Created reflectline.

        :param Reference i_support:
        :param HybridShapeDirection i_dir:
        :param float i_angle:
        :param int i_orientation_support:
        :param int i_orientation_direction:
        :return: HybridShapeReflectLine
        :rtype: HybridShapeReflectLine
        """
        return HybridShapeReflectLine(
            self.hybrid_shape_factory.AddNewReflectLine(i_support.com_object, i_dir.com_object, i_angle,
                                                        i_orientation_support, i_orientation_direction))

    def add_new_reflect_line_with_type(self, i_support: Reference, i_dir: HybridShapeDirection, i_angle: float,
                                       i_orientation_support: int, i_orientation_direction: int,
                                       i_type: int) -> HybridShapeReflectLine:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewReflectLineWithType(Reference iSupport,
                | HybridShapeDirection iDir,
                | double iAngle,
                | long iOrientationSupport,
                | long iOrientationDirection,
                | long iType) As HybridShapeReflectLine
                |
                |     Creates a new ReflectLine within the current body.
                |     Create a reflectline curve on a support surface along a direction with an
                |     angle.
                |
                |     Parameters:
                |
                |         iSupport
                |             Support surface.
                |         iAngle
                |             Angle of the reflectline.
                |         iOrientationSupport
                |             Manage the angle used to compute the reflectline. Value can be 1 or
                |             -1
                |         iOrientationDirection
                |             Manage the angle used to compute the reflectline. Value can be 1 or
                |             -1
                |         iType
                |             Manage the type used to compute the reflectline. Value can be 0 or
                |             1 Returns or sets whether the reflectline curve is or should be created with
                |             the normal to the support or the tangent plane to the
                |             support.
                |             Role: The TypeSolution indicates whether the created reflectline
                |             curve is compute with the angle between the normale to the support and the
                |             direction or with the angle between the tangent plane to the support and the
                |             direction..
                |             Legal values: 0 for the normal and 1 for the tangent plane.
                |
                |         oReflectLine
                |             Created reflectline.

        :param Reference i_support:
        :param HybridShapeDirection i_dir:
        :param float i_angle:
        :param int i_orientation_support:
        :param int i_orientation_direction:
        :param int i_type:
        :return: HybridShapeReflectLine
        :rtype: HybridShapeReflectLine
        """
        return HybridShapeReflectLine(
            self.hybrid_shape_factory.AddNewReflectLineWithType(i_support.com_object, i_dir.com_object, i_angle,
                                                                i_orientation_support, i_orientation_direction, i_type))

    def add_new_revol(self, i_object_to_extrude: Reference, i_offset_debut: float, i_offset_fin: float,
                      i_axis: Reference) -> HybridShapeRevol:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewRevol(Reference iObjectToExtrude,
                | double iOffsetDebut,
                | double iOffsetFin,
                | Reference iAxis) As HybridShapeRevol
                |
                |     Creates a new revolution within the current body.
                |
                |     Parameters:
                |
                |         iObjectToExtrude
                |             Profile to be revolved
                |
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face, TriDimFeatEdge, BiDimFeatEdge and Vertex.
                |
                |     iOffsetDebut
                |         Angle value
                |     iOffsetFin
                |         Angle value
                |     iAxis
                |         Revolution axis ( line that has to be in the profil
                |         plane
                |
                |         Sub-element(s) supported (see Boundary object): see
                |         RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge and
                |         RectilinearMonoDimFeatEdge.
                |     oRevolObject
                |         Revolved result

        :param Reference i_object_to_extrude:
        :param float i_offset_debut:
        :param float i_offset_fin:
        :param Reference i_axis:
        :return: HybridShapeRevol
        :rtype: HybridShapeRevol
        """
        return HybridShapeRevol(
            self.hybrid_shape_factory.AddNewRevol(i_object_to_extrude.com_object, i_offset_debut, i_offset_fin,
                                                  i_axis.com_object))

    def add_new_rotate(self, i_to_rotate: Reference, i_axis: Reference, i_angle: float) -> HybridShapeRotate:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewRotate(Reference iToRotate,
                | Reference iAxis,
                | double iAngle) As HybridShapeRotate
                |
                |     Creates a new Rotate within the current body.
                |
                |     Parameters:
                |
                |         iToRotate
                |             point, curve, surface or solid to transform.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face, TriDimFeatEdge, BiDimFeatEdge and Vertex.
                |
                |     iAxis
                |         Rotation axis.
                |         Sub-element(s) supported (see Boundary object): see
                |         Edge.
                |     iAngle
                |         Rotation angle.
                |     oRotate
                |         Created rotation.

        :param Reference i_to_rotate:
        :param Reference i_axis:
        :param float i_angle:
        :return: HybridShapeRotate
        :rtype: HybridShapeRotate
        """
        return HybridShapeRotate(
            self.hybrid_shape_factory.AddNewRotate(i_to_rotate.com_object, i_axis.com_object, i_angle))

    def add_new_section(self) -> HybridShapeSection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSection() As HybridShapeSection
                |
                |     Creates a new section.
                |
                |     Parameters:
                |
                |         oSection
                |             Created Section

        :return: HybridShapeSection
        :rtype: HybridShapeSection
        """
        return HybridShapeSection(self.hybrid_shape_factory.AddNewSection())

    def add_new_sphere(
            self,
            i_center: Reference,
            i_axis: Reference,
            i_radius: float,
            i_begin_parallel_angle: float,
            i_end_parallel_angle: float,
            i_begin_meridian_angle: float,
            i_end_meridian_angle: float
    ) -> HybridShapeSphere:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSphere(Reference iCenter,
                | Reference iAxis,
                | double iRadius,
                | double iBeginParallelAngle,
                | double iEndParallelAngle,
                | double iBeginMeridianAngle,
                | double iEndMeridianAngle) As HybridShapeSphere
                |
                |     Creates a new Sphere within the current body.
                |
                |     Parameters:
                |
                |         iCenter
                |             Sphere center.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Vertex.
                |     iAxis
                |         Sphere axis
                |     iRadius
                |         Radius
                |     iBeginParallelAngle
                |         Angle value
                |     iEndParallelAngle
                |         Angle value
                |     iBeginMeridianAngle
                |         Angle value
                |     iEndMeridianAngle
                |         Angle value
                |     oSphereObject
                |         Sphere result

        :param Reference i_center:
        :param Reference i_axis:
        :param float i_radius:
        :param float i_begin_parallel_angle:
        :param float i_end_parallel_angle:
        :param float i_begin_meridian_angle:
        :param float i_end_meridian_angle:
        :return: HybridShapeSphere
        :rtype: HybridShapeSphere
        """

        if type(i_axis) is str:
            i_axis = self.application.system_service.evaluate(vba_nothing, 0, 'N', [])
        else:
            i_axis = i_axis.com_object

        return HybridShapeSphere(
            self.hybrid_shape_factory.AddNewSphere(
                i_center.com_object,
                i_axis,
                i_radius,
                i_begin_parallel_angle,
                i_end_parallel_angle,
                i_begin_meridian_angle,
                i_end_meridian_angle
            )
        )

    def add_new_spine(self) -> HybridShapeSpine:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSpine() As HybridShapeSpine
                |
                |     Creates a new spine within the current body.
                |
                |     Parameters:
                |
                |         oExt
                |             CATIAHybridShapeSpine created

        :return: HybridShapeSpine
        :rtype: HybridShapeSpine
        """
        return HybridShapeSpine(self.hybrid_shape_factory.AddNewSpine())

    def add_new_spiral(self, i_type: int, i_support: Reference, i_center_point: Reference, i_axis: HybridShapeDirection,
                       i_starting_radius: float, i_clockwise_revolution: bool) -> HybridShapeSpiral:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSpiral(long iType,
                | Reference iSupport,
                | Reference iCenterPoint,
                | HybridShapeDirection iAxis,
                | double iStartingRadius,
                | boolean iClockwiseRevolution) As HybridShapeSpiral
                |
                |     Creates a new Spiral within the current body.
                |
                |     Parameters:
                |
                |         iType
                |             Spiral is defined by AngleRadius, AnglePitch or PitchRadius.
                |
                |         iSupport
                |             Spiral planar support.
                |         iCenterPoint
                |             Center point.
                |         iAxis
                |             Axis.
                |         iStartingRadius
                |             Defines the starting point: distance from the center point on the
                |             axis.
                |         iClockwiseRevolution
                |             Revolutions are clockwise if TRUE, counterclockwise if FALSE.
                |
                |         oSpiral
                |             The Spiral object if succeded

        :param int i_type:
        :param Reference i_support:
        :param Reference i_center_point:
        :param HybridShapeDirection i_axis:
        :param float i_starting_radius:
        :param bool i_clockwise_revolution:
        :return: HybridShapeSpiral
        :rtype: HybridShapeSpiral
        """
        return HybridShapeSpiral(
            self.hybrid_shape_factory.AddNewSpiral(i_type, i_support.com_object, i_center_point.com_object,
                                                   i_axis.com_object, i_starting_radius, i_clockwise_revolution))

    def add_new_spline(self) -> HybridShapeSpline:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSpline() As HybridShapeSpline
                |
                |     Creates a new Spline within the current body.
                |
                |     Parameters:
                |
                |         oSpline
                |             Created spline.

        :return: HybridShapeSpline
        :rtype: HybridShapeSpline
        """
        return HybridShapeSpline(self.hybrid_shape_factory.AddNewSpline())

    def add_new_surface_datum(self, i_object: Reference) -> HybridShapeSurfaceExplicit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSurfaceDatum(Reference iObject) As
                | HybridShapeSurfaceExplicit
                |
                |     Creates a new datum of surface within the current body.
                |
                |     Parameters:
                |
                |         iObject
                |             The object whose topological body will be duplicated and put into
                |             created datum
                |         oSurface
                |             Created surface Note2: the object passed as parameter to create the
                |             datum has to be in the current container. Otherwise, an error
                |             occurs.

        :param Reference i_object:
        :return: HybridShapeSurfaceExplicit
        :rtype: HybridShapeSurfaceExplicit
        """
        return HybridShapeSurfaceExplicit(self.hybrid_shape_factory.AddNewSurfaceDatum(i_object.com_object))

    def add_new_sweep_circle(self, i_guide1: Reference) -> HybridShapeSweepCircle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSweepCircle(Reference iGuide1) As
                | HybridShapeSweepCircle
                |
                |     Creates a new SweepCircle within the current body.
                |
                |     Parameters:
                |
                |         iGuide1
                |             First guide or center curve.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     oExt
                |         Created swept surface.

        :param Reference i_guide1:
        :return: HybridShapeSweepCircle
        :rtype: HybridShapeSweepCircle
        """
        return HybridShapeSweepCircle(self.hybrid_shape_factory.AddNewSweepCircle(i_guide1.com_object))

    def add_new_sweep_conic(self, ip_ia_guide1: Reference) -> HybridShapeSweepConic:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSweepConic(Reference ipIAGuide1) As
                | HybridShapeSweepConic
                |
                |     Creates a new SweepConic within the current body.
                |
                |     Parameters:
                |
                |         iGuide1
                |             First guide curve.
                |         opIASweepConic
                |             Created swept surface.

        :param Reference ip_ia_guide1:
        :return: HybridShapeSweepConic
        :rtype: HybridShapeSweepConic
        """
        return HybridShapeSweepConic(self.hybrid_shape_factory.AddNewSweepConic(ip_ia_guide1.com_object))

    def add_new_sweep_explicit(self, i_profile: Reference, i_guide: Reference) -> HybridShapeSweepExplicit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSweepExplicit(Reference iProfile,
                | Reference iGuide) As HybridShapeSweepExplicit
                |
                |     Creates a new SweepExplicit within the current body.
                |
                |     Parameters:
                |
                |         iProfile
                |             Profile.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see TriDimFeatEdge and BiDimFeatEdge.
                |
                |     iGuide
                |         First guide curve.
                |         Sub-element(s) supported (see Boundary object): see TriDimFeatEdge and
                |         BiDimFeatEdge.
                |     oExt
                |         Created swept surface.

        :param Reference i_profile:
        :param Reference i_guide:
        :return: HybridShapeSweepExplicit
        :rtype: HybridShapeSweepExplicit
        """
        return HybridShapeSweepExplicit(
            self.hybrid_shape_factory.AddNewSweepExplicit(i_profile.com_object, i_guide.com_object))

    def add_new_sweep_line(self, i_guide1: Reference) -> HybridShapeSweepLine:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSweepLine(Reference iGuide1) As
                | HybridShapeSweepLine
                |
                |     Creates a new SweepLine within the current body.
                |
                |     Parameters:
                |
                |         iGuide1
                |             First guide curve.
                |         oExt
                |             Created swept surface.

        :param Reference i_guide1:
        :return: HybridShapeSweepLine
        :rtype: HybridShapeSweepLine
        """
        return HybridShapeSweepLine(self.hybrid_shape_factory.AddNewSweepLine(i_guide1.com_object))

    def add_new_symmetry(self, i_object: Reference, i_reference: Reference) -> HybridShapeSymmetry:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSymmetry(Reference iObject,
                | Reference iReference) As HybridShapeSymmetry
                |
                |     Creates a new Symmetry within the current body.
                |
                |     Parameters:
                |
                |         iObject
                |             Point, curve, surface or solid to transform.
                |             Sub-element(s) supported (see
                |
                |         Boundary object): see Face, TriDimFeatEdge, BiDimFeatEdge and Vertex.
                |
                |     iReference
                |         Point, line or reference plane.
                |         Sub-element(s) supported (see Boundary object): see PlanarFace, Edge
                |         and Vertex.
                |     oSymmetry
                |         Created symmetry.

        :param Reference i_object:
        :param Reference i_reference:
        :return: HybridShapeSymmetry
        :rtype: HybridShapeSymmetry
        """
        return HybridShapeSymmetry(
            self.hybrid_shape_factory.AddNewSymmetry(i_object.com_object, i_reference.com_object))

    def add_new_transfer(self, i_element_to_transfer: Reference, i_type_of_transfer: int) -> HybridShapeTransfer:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewTransfer(Reference iElementToTransfer,
                | long iTypeOfTransfer) As HybridShapeTransfer
                |
                |     Creates a new Transfer within the current body.
                |     Note: require DL1 license.
                |
                |     Parameters:
                |
                |         iElementToTransfer
                |             The element to transfer
                |         iTypeOfTransfer
                |             The type of transfer
                |         oExt
                |             Created Transfer operation.

        :param Reference i_element_to_transfer:
        :param int i_type_of_transfer:
        :return: HybridShapeTransfer
        :rtype: HybridShapeTransfer
        """
        return HybridShapeTransfer(
            self.hybrid_shape_factory.AddNewTransfer(i_element_to_transfer.com_object, i_type_of_transfer))

    def add_new_translate(self, i_element: Reference, i_direction: HybridShapeDirection,
                          i_distance: float) -> HybridShapeTranslate:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewTranslate(Reference iElement,
                | HybridShapeDirection iDirection,
                | double iDistance) As HybridShapeTranslate
                |
                |     Creates a new Translate within the current body.
                |
                |     Parameters:
                |
                |         iElement
                |             Point, curve, surface or solid to translate.
                |         iDirection
                |             Translation direction.
                |         iDistance
                |             Translation Distance.
                |         oTranslate
                |             Created translation
                |         oTranslate
                |             Created Translate (Empty feature)
                |             Note: Then translate mode and inputs has to be initialized
                |
                |
                |     See also:
                |         HybridShapeTranslate

        :param Reference i_element:
        :param HybridShapeDirection i_direction:
        :param float i_distance:
        :return: HybridShapeTranslate
        :rtype: HybridShapeTranslate
        """
        return HybridShapeTranslate(
            self.hybrid_shape_factory.AddNewTranslate(i_element.com_object, i_direction.com_object, i_distance))

    def add_new_unfold(self) -> HybridShapeUnfold:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewUnfold() As HybridShapeUnfold
                |
                |     Creates a new Unfold within the current body.
                |     Note: require DL1 license.
                |
                |     Parameters:
                |
                |         oExt
                |             Created unfold operation.

        :return: HybridShapeUnfold
        :rtype: HybridShapeUnfold
        """
        return HybridShapeUnfold(self.hybrid_shape_factory.AddNewUnfold())

    def add_new_volume_datum(self, i_object: Reference) -> HybridShapeVolumeExplicit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewVolumeDatum(Reference iObject) As
                | HybridShapeVolumeExplicit
                |
                |     Creates a new datum of volume within the current body.
                |     Note: requires GSO License
                |
                |     Parameters:
                |
                |         iObject
                |             The object whose topological body will be duplicated and put into
                |             created datum
                |         oVolume
                |             Created Volume Note2: the object passed as parameter to create the
                |             datum has to be in the current container. Otherwise, an error
                |             occurs.

        :param Reference i_object:
        :return: HybridShapeVolumeExplicit
        :rtype: HybridShapeVolumeExplicit
        """
        return HybridShapeVolumeExplicit(self.hybrid_shape_factory.AddNewVolumeDatum(i_object.com_object))

    def add_new_wrap_curve(self) -> HybridShapeWrapCurve:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewWrapCurve() As HybridShapeWrapCurve
                |
                |     Creates a new Wrap Curve Surface within the current body.
                |     Note: require GSO license.
                |
                |     Parameters:
                |
                |         oWrapCurve
                |             The Wrap Curve object if succeded

        :return: HybridShapeWrapCurve
        :rtype: HybridShapeWrapCurve
        """
        return HybridShapeWrapCurve(self.hybrid_shape_factory.AddNewWrapCurve())

    def add_new_wrap_surface(self, i_body_to_deform: Reference) -> HybridShapeWrapSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewWrapSurface(Reference iBodyToDeform) As
                | HybridShapeWrapSurface
                |
                |     Creates a new Wrap Surface within the current body.
                |     Note: require GSO license.
                |
                |     Parameters:
                |
                |         :
                |             iBodyToDeform Body to deform with a Wrap Surface
                |         oWrapSurface
                |             The Wrap Surface object if succeded

        :param Reference i_body_to_deform:
        :return: HybridShapeWrapSurface
        :rtype: HybridShapeWrapSurface
        """
        return HybridShapeWrapSurface(self.hybrid_shape_factory.AddNewWrapSurface(i_body_to_deform.com_object))

    def change_feature_name(self, i_elem: Reference, name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ChangeFeatureName(Reference iElem,
                | CATBSTR Name)
                |
                |     Set display name for Shape Design Features.
                |
                |     Parameters:
                |
                |         iElem
                |             Element to rename
                |         Name
                |             User name

        :param Reference i_elem:
        :param str name:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_factory.ChangeFeatureName(i_elem.com_object, name)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'change_feature_name'
        # # vba_code = """
        # # Public Function change_feature_name(hybrid_shape_factory)
        # #     Dim iElem (2)
        # #     hybrid_shape_factory.ChangeFeatureName iElem
        # #     change_feature_name = iElem
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def delete_object_for_datum(self, i_object: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub DeleteObjectForDatum(Reference iObject)
                |
                |     Deletes an object within the current body.
                |
                |     Parameters:
                |
                |         iObject
                |             Object to delete

        :param Reference i_object:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_factory.DeleteObjectForDatum(i_object.com_object)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'delete_object_for_datum'
        # # vba_code = """
        # # Public Function delete_object_for_datum(hybrid_shape_factory)
        # #     Dim iObject (2)
        # #     hybrid_shape_factory.DeleteObjectForDatum iObject
        # #     delete_object_for_datum = iObject
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def gsm_visibility(self, i_elem: Reference, show: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GSMVisibility(Reference iElem,
                | long Show)
                |
                |     Set Visibility attribut for Shape Design Features.
                |
                |     Parameters:
                |
                |         iElem
                |             Element to show/NoShow
                |         Show
                |             = 0 NoShow , 1= Show

        :param Reference i_elem:
        :param int show:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_factory.GSMVisibility(i_elem.com_object, show)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'gsm_visibility'
        # # vba_code = """
        # # Public Function gsm_visibility(hybrid_shape_factory)
        # #     Dim iElem (2)
        # #     hybrid_shape_factory.GSMVisibility iElem
        # #     gsm_visibility = iElem
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_geometrical_feature_type(self, i_elem: Reference) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetGeometricalFeatureType(Reference iElem) As short
                |
                |     Returns type of "geometrical" shape Design feature .
                |
                |     Parameters:
                |
                |         iElem
                |             Reference element
                |         oType
                |             Type of feature
                |             0 = Unknown, 1 = Point,  2 = Curve, 3 = Line, 4 = Circle,
                |             5 = Surface, 6 = Plane, 7 = Solid / Volume
                |             Level of availability = V5R14


        See enumeration.enumeration_types.geometrical_feature_type() for enums.

        :param Reference i_elem:
        :return: 0 = Unknown, 1 = Point, 2 = Curve, 3 = Line, 4 = Circle, 5 = Surface, 6 = Plane, 7 = Solid, Volume
        :rtype: int
        """
        return self.hybrid_shape_factory.GetGeometricalFeatureType(i_elem.com_object)

    def __repr__(self):
        return f'HybridShapeFactory(name="{self.name}")'
