#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeSpline(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape spline feature object.Role: To access the
                | data of the hybrid shape spline feature object. This data includes:Use
                | the  CATIAHybridShapeFactory to create a HybridShapeAffinity object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_spline = com_object     

    def add_point(self, ip_ia_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddPoint
                | o Sub AddPoint(        ipIAPoint)
                | 
                | Add a new point .
                |
                | Parameters:
                | iPoint
                |     Point element.


        :param ip_ia_point:
        :return:
        """
        return self.hybrid_shape_spline.AddPoint(ip_ia_point)

    def add_point_with_constraint_explicit(self, ip_ia_point, ip_ia_dir_tangency, i_tangency_norm, i_inverse_tangency, ip_ia_dir_curvature, i_curvature_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddPointWithConstraintExplicit
                | o Sub AddPointWithConstraintExplicit(        ipIAPoint,
                |                                              ipIADirTangency,
                |                                              iTangencyNorm,
                |                                              iInverseTangency,
                |                                              ipIADirCurvature,
                |                                              iCurvatureRadius)
                | 
                | Add a new point with explicit tangency and curvature.
                |
                | Parameters:
                | ipIAPoint
                |     Point element.
                |  
                |  ipIADirTangency
                |     Tangent direction.
                |  
                |  iTangencyNorm
                |     Tension.
                |  
                |  iInverseTangency
                |     Flag to reverse tangent direction (value can be 1 or -1).
                |  
                |  ipIADirCurvature
                |     Curvature direction.
                |  
                |  iCurvatureRadius
                |     Curvature radius value.


        :param ip_ia_point:
        :param ip_ia_dir_tangency:
        :param i_tangency_norm:
        :param i_inverse_tangency:
        :param ip_ia_dir_curvature:
        :param i_curvature_radius:
        :return:
        """
        return self.hybrid_shape_spline.AddPointWithConstraintExplicit(ip_ia_point, ip_ia_dir_tangency, i_tangency_norm, i_inverse_tangency, ip_ia_dir_curvature, i_curvature_radius)

    def add_point_with_constraint_from_curve(self, ip_ia_point, ip_ia_curve_cst, i_tangency_norm, i_invert_value, i_crv_cst_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddPointWithConstraintFromCurve
                | o Sub AddPointWithConstraintFromCurve(        ipIAPoint,
                |                                               ipIACurveCst,
                |                                               iTangencyNorm,
                |                                               iInvertValue,
                |                                               iCrvCstType)
                | 
                | Add a new point with tangency/curvature from a curve.
                |
                | Parameters:
                | ipIAPoint
                |     Point element.
                |  
                |  ipIACurveCst
                |    Curvature direction.
                |  
                |  iTangencyNorm
                |      tension factor for tangency.
                |  
                |  iInvertValue
                |    Orientation for tangent 
                |  
                |  iCrvCstType
                |     Continuity type for Curve Constraint (1=Tangency , 2-= Curvature).


        :param ip_ia_point:
        :param ip_ia_curve_cst:
        :param i_tangency_norm:
        :param i_invert_value:
        :param i_crv_cst_type:
        :return:
        """
        return self.hybrid_shape_spline.AddPointWithConstraintFromCurve(ip_ia_point, ip_ia_curve_cst, i_tangency_norm, i_invert_value, i_crv_cst_type)

    def get_closure(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetClosure
                | o Func GetClosure(    ) As
                | 
                | Gets whether the curve is closed.
                |
                | Parameters:
                | oClosed
                |        Closing flag
                | 1 for a closed curve
                | 0 for an open curve


        :return:
        """
        return self.hybrid_shape_spline.GetClosure()

    def get_constraint_type(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetConstraintType
                | o Func GetConstraintType(        iPos) As
                | 
                | Returns the ControlPoint type at the given position.
                |
                | Parameters:
                | iPos
                |     The poistion of the point to retrieve
                |  
                |  oCstType
                |    Type of Control point (CstType=0 : not defined / CstType=1 : Explicit / CstType=2 : FromCurve)


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_spline.GetConstraintType(i_pos)

    def get_curvature_radius(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCurvatureRadius
                | o Func GetCurvatureRadius(        iPos) As
                | 
                | Returns the curvature radius value for each point of the
                | spline.
                |
                | Parameters:
                | iPos
                |     The position of the point in the spline.
                |    Legal values: first position is 1.
                |     The position cannot be 0. 
                |  
                |  oRadius
                |    The curvature radius value at this point


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_spline.GetCurvatureRadius(i_pos)

    def get_direction_inversion(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDirectionInversion
                | o Func GetDirectionInversion(        iPos) As
                | 
                | Gets the orientation of the tangent direction .
                |
                | Parameters:
                | oInvertFlag
                |       invert flag
                |     = 1  No Inversion
                |     = -1 Invert
                |    
                |  iPos
                |       Position of point in spline
                |                    First Position is 1
                |                    Position 0 return E_FAIL


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_spline.GetDirectionInversion(i_pos)

    def get_nb_control_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbControlPoint
                | o Func GetNbControlPoint(    ) As
                | 
                | Returns the number of control points.
                |
                | Parameters:
                | oNbCtrPt
                |    The number of control points.


        :return:
        """
        return self.hybrid_shape_spline.GetNbControlPoint()

    def get_point(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPoint
                | o Func GetPoint(        iPos) As
                | 
                | Returns the Point at the given position.
                |
                | Parameters:
                | iPos
                |     The poistion of the point to retrieve
                |  
                |  opIAPoint
                |    Type of Control point (TypeCtrPoint =1 : Explicit / TypeCtrPoint =2 : FromCurve)


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_spline.GetPoint(i_pos)

    def get_point_constraint_explicit(self, i_pos, op_ia_dir_tangency, o_tangency_norm, o_inverse_tangency, op_ia_dir_curvature, o_curvature_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPointConstraintExplicit
                | o Sub GetPointConstraintExplicit(        iPos,
                |                                          opIADirTangency,
                |                                          oTangencyNorm,
                |                                          oInverseTangency,
                |                                          opIADirCurvature,
                |                                          oCurvatureRadius)
                | 
                | Returns the Constraint of the point at iPos. Available for
                | Explicit Point Constraint type (CstType =1 from
                | GetContraintType)
                |
                | Parameters:
                | iPos
                |     The position of the point to retrieve
                |  
                |  opIADirTangency
                |     Tangent direction.
                |  
                |  oTangencyNorm
                |     Tension.
                |  
                |  oInverseTangency
                |     Flag to reverse tangent direction (value can be 1 or -1).
                |  
                |  opIADirCurvature
                |     Curvature direction.
                |  
                |  oCurvatureRadius
                |     Curvature radius value.


        :param i_pos:
        :param op_ia_dir_tangency:
        :param o_tangency_norm:
        :param o_inverse_tangency:
        :param op_ia_dir_curvature:
        :param o_curvature_radius:
        :return:
        """
        return self.hybrid_shape_spline.GetPointConstraintExplicit(i_pos, op_ia_dir_tangency, o_tangency_norm, o_inverse_tangency, op_ia_dir_curvature, o_curvature_radius)

    def get_point_constraint_from_curve(self, i_pos, op_ia_curve_cst, o_tangency_norm, o_invert_value, o_crv_cst_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPointConstraintFromCurve
                | o Sub GetPointConstraintFromCurve(        iPos,
                |                                           opIACurveCst,
                |                                           oTangencyNorm,
                |                                           oInvertValue,
                |                                           oCrvCstType)
                | 
                | Returns the Constraint of the point at iPos. Available for
                | FromCurve Point Constraint type (CstType =2 from
                | GetContraintType)
                |
                | Parameters:
                | iPos
                |     The position of the point to retrieve
                |  
                |  opIACurveCst
                |    Curvature direction.
                |  
                |  oTangencyNorm
                |      tension factor for tangency.
                |  
                |  oInvertValue
                |    Orientation for tangent 
                |  
                |  oCrvCstType
                |     Continuity type for Curve Constraint (1=Tangency , 2-= Curvature).


        :param i_pos:
        :param op_ia_curve_cst:
        :param o_tangency_norm:
        :param o_invert_value:
        :param o_crv_cst_type:
        :return:
        """
        return self.hybrid_shape_spline.GetPointConstraintFromCurve(i_pos, op_ia_curve_cst, o_tangency_norm, o_invert_value, o_crv_cst_type)

    def get_point_position(self, ip_ia_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPointPosition
                | o Func GetPointPosition(        ipIAPoint) As
                | 
                | Returns the position of a given point.
                |
                | Parameters:
                | ipIAPoint
                |    Point 
                |  
                |  oPos
                |     The position of the point (=0 Point Not in Spline)


        :param ip_ia_point:
        :return:
        """
        return self.hybrid_shape_spline.GetPointPosition(ip_ia_point)

    def get_spline_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSplineType
                | o Func GetSplineType(    ) As
                | 
                | Gets the spline type.
                |
                | Parameters:
                | oType
                |  = 0 : Cubic Type Spline.                = 1 : WilsonFowler Type Spline.


        :return:
        """
        return self.hybrid_shape_spline.GetSplineType()

    def get_support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSupport
                | o Func GetSupport(    ) As
                | 
                | Gets the support surface.
                |
                | Parameters:
                | oSupport
                |       Supporting surface for spline (if exist)


        :return:
        """
        return self.hybrid_shape_spline.GetSupport()

    def get_tangent_norm(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetTangentNorm
                | o Func GetTangentNorm(        iPos) As
                | 
                | Returns the tension for each point of the spline. The
                | tension is the tangent norm at the given point.
                |
                | Parameters:
                | iPos
                |     The position of the point in the spline.
                |    Legal values: first position is 1.
                |     The position cannot be 0. 
                |  
                |  oTension
                |     The tension at this point


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_spline.GetTangentNorm(i_pos)

    def invert_direction(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertDirection
                | o Sub InvertDirection(        iPos)
                | 
                | Inverts the orientation of the tangent direction .
                |
                | Parameters:
                | iPos
                |       Position of point in spline
                |                    First Position is 1
                |                    Position 0 return E_FAIL


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_spline.InvertDirection(i_pos)

    def remove_all(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAll
                | o Sub RemoveAll(    )
                | 
                | Removes all elements in the list of points.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_spline.RemoveAll()

    def remove_control_point(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveControlPoint
                | o Sub RemoveControlPoint(        iPos)
                | 
                | Removes a point at the given position.
                |
                | Parameters:
                | iPos
                |     The position of the point to remove


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_spline.RemoveControlPoint(i_pos)

    def remove_curvature_radius_direction(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveCurvatureRadiusDirection
                | o Sub RemoveCurvatureRadiusDirection(        iPos)
                | 
                | Removes Curvature Radius Direction for the given point of
                | the spline.
                |
                | Parameters:
                | iPos
                |       Position of point in spline
                |                    First Position is 1
                |                    Position 0 return E_FAIL


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_spline.RemoveCurvatureRadiusDirection(i_pos)

    def remove_curvature_radius_value(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveCurvatureRadiusValue
                | o Sub RemoveCurvatureRadiusValue(        iPos)
                | 
                | Removes Curvature Radius Value for the given point of the
                | spline.
                |
                | Parameters:
                | iPos
                |       Position of point in spline
                |                    First Position is 1
                |                    Position 0 return E_FAIL


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_spline.RemoveCurvatureRadiusValue(i_pos)

    def remove_support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveSupport
                | o Sub RemoveSupport(    )
                | 
                | Removes the support surface.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_spline.RemoveSupport()

    def remove_tangent_direction(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveTangentDirection
                | o Sub RemoveTangentDirection(        iPos)
                | 
                | Removes tangent Direction for the given point of the spline.
                |
                | Parameters:
                | iPos
                |       Position of point in spline
                |                    First Position is 1
                |                    Position 0 return E_FAIL


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_spline.RemoveTangentDirection(i_pos)

    def remove_tension(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveTension
                | o Sub RemoveTension(        iPos)
                | 
                | Removes the Tension for the given point of the spline.
                |
                | Parameters:
                | iPos
                |       Position of point in spline
                |                    First Position is 1
                |                    Position 0 return E_FAIL


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_spline.RemoveTension(i_pos)

    def replace_point_at_position(self, i_pos, i_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReplacePointAtPosition
                | o Sub ReplacePointAtPosition(        iPos,
                |                                      iPoint)
                | 
                | Replaces a point in the list at the given position.
                |
                | Parameters:
                | oPoint
                |       Point
                |    
                |  iPos
                |       Replace position


        :param i_pos:
        :param i_point:
        :return:
        """
        return self.hybrid_shape_spline.ReplacePointAtPosition(i_pos, i_point)

    def set_closing(self, i_closing_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetClosing
                | o Sub SetClosing(        iClosingType)
                | 
                | Activates the closing option of the spline.
                |
                | Parameters:
                | iClosingType
                |     The spline closing option


        :param i_closing_type:
        :return:
        """
        return self.hybrid_shape_spline.SetClosing(i_closing_type)

    def set_point_after(self, i_pos, ip_ia_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPointAfter
                | o Sub SetPointAfter(        iPos,
                |                             ipIAPoint)
                | 
                | Sets the Point After a given position.
                |
                | Parameters:
                | iPos
                |     The position reference (0 < position < Nbpt)
                |  
                |  ipIAPoint
                |    Point


        :param i_pos:
        :param ip_ia_point:
        :return:
        """
        return self.hybrid_shape_spline.SetPointAfter(i_pos, ip_ia_point)

    def set_point_before(self, i_pos, ip_ia_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPointBefore
                | o Sub SetPointBefore(        iPos,
                |                              ipIAPoint)
                | 
                | Sets the Point Before a given position.
                |
                | Parameters:
                | iPos
                |     The position reference (1 < position < Nbpt+1) 
                |  
                |  ipIAPoint
                |    Point


        :param i_pos:
        :param ip_ia_point:
        :return:
        """
        return self.hybrid_shape_spline.SetPointBefore(i_pos, ip_ia_point)

    def set_point_constraint_explicit(self, i_pos, ip_ia_dir_tangency, i_tangency_norm, i_inverse_tangency, ip_ia_dir_curvature, i_curvature_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPointConstraintExplicit
                | o Sub SetPointConstraintExplicit(        iPos,
                |                                          ipIADirTangency,
                |                                          iTangencyNorm,
                |                                          iInverseTangency,
                |                                          ipIADirCurvature,
                |                                          iCurvatureRadius)
                | 
                | Sets the Constraint of the point at iPos. Available for
                | Explicit Point Constraint type (CstType =1 from
                | GetContraintType)
                |
                | Parameters:
                | iPos
                |     The position of the point to retrieve
                |  
                |  ipIADirTangency
                |     Tangent direction.
                |  
                |  iTangencyNorm
                |     Tension.
                |  
                |  iInverseTangency
                |     Flag to reverse tangent direction (value can be 1 or -1).
                |  
                |  ipIADirCurvature
                |     Curvature direction.
                |  
                |  iCurvatureRadius
                |     Curvature radius value.


        :param i_pos:
        :param ip_ia_dir_tangency:
        :param i_tangency_norm:
        :param i_inverse_tangency:
        :param ip_ia_dir_curvature:
        :param i_curvature_radius:
        :return:
        """
        return self.hybrid_shape_spline.SetPointConstraintExplicit(i_pos, ip_ia_dir_tangency, i_tangency_norm, i_inverse_tangency, ip_ia_dir_curvature, i_curvature_radius)

    def set_point_constraint_from_curve(self, i_pos, ip_ia_curve_cst, i_tangency_norm, i_invert_value, i_crv_cst_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPointConstraintFromCurve
                | o Sub SetPointConstraintFromCurve(        iPos,
                |                                           ipIACurveCst,
                |                                           iTangencyNorm,
                |                                           iInvertValue,
                |                                           iCrvCstType)
                | 
                | Sets the Constraint of the point at iPos. Available for From
                | Curve Point Constraint type (CstType =2 from
                | GetContraintType)
                |
                | Parameters:
                | iPos
                |     The position of the point to retrieve
                |  
                |  ipIACurveCst
                |    Curvature direction.
                |  
                |  iTangencyNorm
                |      tension factor for tangency.
                |  
                |  iInvertValue
                |    Orientation for tangent 
                |  
                |  iCrvCstType
                |     Continuity type for Curve Constraint (1=Tangency , 2-= Curvature).


        :param i_pos:
        :param ip_ia_curve_cst:
        :param i_tangency_norm:
        :param i_invert_value:
        :param i_crv_cst_type:
        :return:
        """
        return self.hybrid_shape_spline.SetPointConstraintFromCurve(i_pos, ip_ia_curve_cst, i_tangency_norm, i_invert_value, i_crv_cst_type)

    def set_spline_type(self, i_spline_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSplineType
                | o Sub SetSplineType(        iSplineType)
                | 
                | Sets the spline type.
                |
                | Parameters:
                | iSplineType
                |     The spline type
                |    Legal values: Cubic spline (0) or WilsonFowler (1)


        :param i_spline_type:
        :return:
        """
        return self.hybrid_shape_spline.SetSplineType(i_spline_type)

    def set_support(self, i_support):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSupport
                | o Sub SetSupport(        iSupport)
                | 
                | Sets the spline support surface. Have your "tangent
                | direction" tangent to this support is recommended.
                |
                | Parameters:
                | iSupport
                |     The spline support surface.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | .


        :param i_support:
        :return:
        """
        return self.hybrid_shape_spline.SetSupport(i_support)

    def __repr__(self):
        return f'HybridShapeSpline()'
