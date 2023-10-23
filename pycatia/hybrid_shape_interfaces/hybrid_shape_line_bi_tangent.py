#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.line import Line
from pycatia.in_interfaces.reference import Reference


class HybridShapeLineBiTangent(Line):
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
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLineBiTangent
                | 
                | Line tangent to a curve.
                | Role: To access data of the line feature created to be tangent to two
                | entities
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_bi_tangent = com_object

    @property
    def curve1(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Curve1() As Reference
                | 
                |     Returns or Sets the first tangency curve lying on the support
                |     surface.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in oCurve the first tangency curve for the
                |         LineBiTangent hybrid shape feature.
                | 
                |          Dim oCurve As Reference
                |          Set oCurve = LineBiTangent.Curve1

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_bi_tangent.Curve1)

    @curve1.setter
    def curve1(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_line_bi_tangent.Curve1 = reference_curve.com_object

    @property
    def element2(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Element2() As Reference
                | 
                |     Returns or Sets the second tangency element (point, curve) lying on the
                |     support surface.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge,
                |     BiDimFeatEdge or Vertex.
                | 
                |     Example:
                |         This example retrieves in oElement the second tangency Element (point,
                |         curve) for the LineBiTangent hybrid shape feature.
                | 
                |          Dim oElement As Reference
                |          Set oElement = LineBiTangent.Element2

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_bi_tangent.Element2)

    @element2.setter
    def element2(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_line_bi_tangent.Element2 = reference_element.com_object

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or Sets the supporting surface.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in oSurface the surface for the LineBiTangent
                |         hybrid shape feature.
                | 
                |          Dim oSurface As Reference 
                |          Set oSurface = LineBiTangent.Surface

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_line_bi_tangent.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_line_bi_tangent.Support = reference_support.com_object

    def get_choice_no(self, val1: int, val2: int, val3: int, val4: int, val5: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetChoiceNo(long val1,
                | long val2,
                | long val3,
                | long val4,
                | long val5)
                | 
                |     Returns a sequence which identifies a solution among all
                |     possibilities.
                | 
                |         val1 = Solution number (from 1 to n).
                | 
                |     val2 = oOriTgt1
                | 
                |     This orientation allows to compute just the results that are tangent to a
                |     specific region of the first curve.
                |     It can take 3 values:
                | 
                |         +1 : the result has the same orientation as the curve,
                |         -1 : the result has the opposite orientation of the curve,
                |         0 : no orientation is specified.
                | 
                |     val3 = oOriCvt1
                | 
                |     This orientation allows to compute just the results that are tangent to a
                |     specific side of the first curve.
                |     It can take 3 values:
                | 
                |         +1 : curvature direction of curve and cross product of support normal and result direction
                |              are in the same direction,
                |         -1 : curvature direction of curve and cross product of support normal and result direction
                |              are in opposite directions,
                |         0 : no orientation is specified.
                | 
                |     val4 = oOriTgt2
                | 
                |     In case of curve/curve bitangent line, this orientation allows to compute
                |     just the results that are tangent to a specific region of the second curve
                |     .
                |     It can take 3 values:
                | 
                |         +1 : the result has the same orientation as the curve,
                |         -1 : the result has the opposite orientation of the curve,
                |         0 : no orientation is specified.
                | 
                |     val5 = oOriCvt2
                | 
                |     In case of curve/curve bitangent line this orientation allows to compute
                |     just the results that are tangent to a specific side of the second
                |     curve.
                |     It can take 3 values:
                | 
                |         +1 : curvature direction of curve and cross product of support normal and result direction
                |              are in the same direction,
                |         -1 : curvature direction of curve and cross product of support normal and result direction
                |              are in opposite directions,
                |         0 : no orientation is specified.
                | 
                |     Example:
                |         This example retrieves in vakl1,val2,val3,val4,val5 parameters for
                |         solutions for the LineBiTangent hybrid shape feature.
                | 
                |          Dim oVal1 As long
                |          Dim oVal2 As long
                |          Dim oVal3 As long
                |          Dim oVal4 As long
                |          Dim oVal5 As long
                |          LineBiTangent.GetChoiceNo(ovla1, oVal2, oVal3, oVal4, oVal5)

        :param int val1:
        :param int val2:
        :param int val3:
        :param int val4:
        :param int val5:
        :rtype: None
        """
        return self.hybrid_shape_line_bi_tangent.GetChoiceNo(val1, val2, val3, val4, val5)

    def get_length_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLengthType() As long
                | 
                |     Gets the length type Default is 0.
                | 
                |     Parameters:
                | 
                |         oType
                |             The length type = 0 : length - the line is limited by its extremities =
                |             1 : infinite - the line is infinite = 2 : infinite start point - the line is infinite on
                |             the side of the start point = 3 : infinite end point - the line is infinite on the side
                |             of the end point

        :rtype: int
        """
        return self.hybrid_shape_line_bi_tangent.GetLengthType()

    def set_choice_no(self, val1: int, val2: int, val3: int, val4: int, val5: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetChoiceNo(long val1,
                | long val2,
                | long val3,
                | long val4,
                | long val5)
                | 
                |     Sets a sequence which identifies a solution among all
                |     possibilities.
                | 
                |         val1 = Solution number (from 1 to n).
                | 
                |     val2 = oOriTgt1
                | 
                |     This orientation allows to compute just the results that are tangent to a
                |     specific region of the first curve.
                |     It can take 3 values:
                | 
                |         +1 : the result has the same orientation as the curve,
                |         -1 : the result has the opposite orientation of the curve,
                |         0 : no orientation is specified.
                | 
                |     val3 = oOriCvt1
                | 
                |     This orientation allows to compute just the results that are tangent to a
                |     specific side of the first curve.
                |     It can take 3 values:
                | 
                |         +1 : curvature direction of curve and cross product of support normal and result direction
                |              are in the same direction,
                |         -1 : curvature direction of curve and cross product of support normal and result direction
                |              are in opposite directions,
                |         0 : no orientation is specified.
                | 
                |     val4 = oOriTgt2
                | 
                |     In case of curve/curve bitangent line, this orientation allows to compute
                |     just the results that are tangent to a specific region of the second curve
                |     .
                |     It can take 3 values:
                | 
                |         +1 : the result has the same orientation as the curve,
                |         -1 : the result has the opposite orientation of the curve,
                |         0 : no orientation is specified.
                | 
                |     val5 = oOriCvt2
                | 
                |     In case of curve/curve bitangent line this orientation allows to compute
                |     just the results that are tangent to a specific side of the second
                |     curve.
                |     It can take 3 values:
                | 
                |         +1 : curvature direction of curve and cross product of support normal and result direction
                |              are in the same direction,
                |         -1 : curvature direction of curve and cross product of support normal and result direction
                |              are in opposite directions,
                |         0 : no orientation is specified.
                | 
                |     Example:
                |         This example retrieves in vakl1,val2,val3,val4,val5 parameters for
                |         solutions for the LineBiTangent hybrid shape feature.
                | 
                |          Dim iVal1 As long
                |          Dim iVal2 As long
                |          Dim iVal3 As long
                |          Dim iVal4 As long
                |          Dim iVal5 As long
                |          ival1 = 1 
                |          ival2 = 0 
                |          ival3 = 0 
                |          ival4 = 0 
                |          ival5 = 0 
                |          LineBiTangent.SetChoiceNo(ivla1, iVal2, iVal3, iVal4, iVal5)

        :param int val1:
        :param int val2:
        :param int val3:
        :param int val4:
        :param int val5:
        :rtype: None
        """
        return self.hybrid_shape_line_bi_tangent.SetChoiceNo(val1, val2, val3, val4, val5)

    def set_length_type(self, i_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLengthType(long iType)
                | 
                |     Sets the length type Default is 0.
                | 
                |     Parameters:
                | 
                |         iType
                |             The length type = 0 : length - the line is limited by its extremities =
                |             1 : infinite - the line is infinite = 2 : infinite start point - the line is infinite
                |             on the side of the start point = 3 : infinite end point - the line is infinite on the
                |             side of the end point

        :param int i_type:
        :rtype: None
        """
        return self.hybrid_shape_line_bi_tangent.SetLengthType(i_type)

    def __repr__(self):
        return f'HybridShapeLineBiTangent(name="{self.name}")'
