#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeLineBiTangent(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Line tangent to a curve.Role: To access data of the line feature
                | created to  be tangent to two entities

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_bi_tangent = com_object     

    @property
    def curve1(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Curve1
                | o Property Curve1(    ) As
                | 
                | Returns or Sets the first tangency curve lying on the
                | support surface. Sub-element(s) supported (see object): or .
                | 
                |
                | Example:
                | This example retrieves in oCurve the first tangency
                | curve for the LineBiTangent hybrid shape feature. Dim oCurve
                | As Reference Set oCurve = LineBiTangent.Curve1

        :return:
        """
        return self.hybrid_shape_line_bi_tangent.Curve1

    @property
    def element2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Element2
                | o Property Element2(    ) As
                | 
                | Returns or Sets the second tangency element (point, curve)
                | lying on the support surface. Sub-element(s) supported (see
                | object): , or . 
                |
                | Example:
                | This example retrieves in oElement
                | the second tangency Element (point, curve) for the
                | LineBiTangent hybrid shape feature. Dim oElement As
                | Reference Set oElement = LineBiTangent.Element2

        :return:
        """
        return self.hybrid_shape_line_bi_tangent.Element2

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or Sets the supporting surface. Sub-element(s)
                | supported (see object): . 
                |
                | Example:
                | This example retrieves in
                | oSurface the surface for the LineBiTangent hybrid shape
                | feature. Dim oSurface As Reference Set oSurface =
                | LineBiTangent.Surface

        :return:
        """
        return self.hybrid_shape_line_bi_tangent.Support

    def get_choice_no(self, val_1, val_2, val_3, val_4, val_5):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetChoiceNo
                | o Sub GetChoiceNo(        val1,
                |                           val2,
                |                           val3,
                |                           val4,
                |                           val5)
                | 
                | Returns a sequence which identifies a solution among all
                | possibilities. val1 = Solution number (from 1 to n). val2 =
                | oOriTgt1 This orientation allows to compute just the results
                | that are tangent to a specific region of the first curve. It
                | can take 3 values: +1 : the result has the same orientation
                | as the curve, -1 : the result has the opposite orientation
                | of the curve, 0 : no orientation is specified. val3 =
                | oOriCvt1 This orientation allows to compute just the results
                | that are tangent to a specific side of the first curve. It
                | can take 3 values: +1 : curvature direction of curve and
                | cross product of support normal and result direction are in
                | the same direction, -1 : curvature direction of curve and
                | cross product of support normal and result direction are in
                | opposite directions, 0 : no orientation is specified. val4 =
                | oOriTgt2 In case of curve/curve bitangent line, this
                | orientation allows to compute just the results that are
                | tangent to a specific region of the second curve . It can
                | take 3 values: +1 : the result has the same orientation as
                | the curve, -1 : the result has the opposite orientation of
                | the curve, 0 : no orientation is specified. val5 = oOriCvt2
                | In case of curve/curve bitangent line this orientation
                | allows to compute just the results that are tangent to a
                | specific side of the second curve. It can take 3 values: +1
                | : curvature direction of curve and cross product of support
                | normal and result direction are in the same direction, -1 :
                | curvature direction of curve and cross product of support
                | normal and result direction are in opposite directions, 0 :
                | no orientation is specified. 
                |
                | Example:
                | This example retrieves
                | in vakl1,val2,val3,val4,val5 parameters for solutions for
                | the LineBiTangent hybrid shape feature. Dim oVal1 As long
                | Dim oVal2 As long Dim oVal3 As long Dim oVal4 As long Dim
                | oVal5 As long LineBiTangent.GetChoiceNo(ovla1, oVal2, oVal3,
                | oVal4, oVal5)
                |
                | Parameters:


        :param val_1:
        :param val_2:
        :param val_3:
        :param val_4:
        :param val_5:
        :return:
        """
        return self.hybrid_shape_line_bi_tangent.GetChoiceNo(val_1, val_2, val_3, val_4, val_5)

    def get_length_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLengthType
                | o Func GetLengthType(    ) As
                | 
                | Gets the length type Default is 0.
                |
                | Parameters:
                | oType
                |    The length type = 0 : length               - the line is limited by its extremities
                |                    = 1 : infinite             - the line is infinite
                |                    = 2 : infinite start point - the line is infinite on the side of the start point
                |                    = 3 : infinite end point   - the line is infinite on the side of the end point


        :return:
        """
        return self.hybrid_shape_line_bi_tangent.GetLengthType()

    def set_choice_no(self, val_1, val_2, val_3, val_4, val_5):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetChoiceNo
                | o Sub SetChoiceNo(        val1,
                |                           val2,
                |                           val3,
                |                           val4,
                |                           val5)
                | 
                | Sets a sequence which identifies a solution among all
                | possibilities. val1 = Solution number (from 1 to n). val2 =
                | oOriTgt1 This orientation allows to compute just the results
                | that are tangent to a specific region of the first curve. It
                | can take 3 values: +1 : the result has the same orientation
                | as the curve, -1 : the result has the opposite orientation
                | of the curve, 0 : no orientation is specified. val3 =
                | oOriCvt1 This orientation allows to compute just the results
                | that are tangent to a specific side of the first curve. It
                | can take 3 values: +1 : curvature direction of curve and
                | cross product of support normal and result direction are in
                | the same direction, -1 : curvature direction of curve and
                | cross product of support normal and result direction are in
                | opposite directions, 0 : no orientation is specified. val4 =
                | oOriTgt2 In case of curve/curve bitangent line, this
                | orientation allows to compute just the results that are
                | tangent to a specific region of the second curve . It can
                | take 3 values: +1 : the result has the same orientation as
                | the curve, -1 : the result has the opposite orientation of
                | the curve, 0 : no orientation is specified. val5 = oOriCvt2
                | In case of curve/curve bitangent line this orientation
                | allows to compute just the results that are tangent to a
                | specific side of the second curve. It can take 3 values: +1
                | : curvature direction of curve and cross product of support
                | normal and result direction are in the same direction, -1 :
                | curvature direction of curve and cross product of support
                | normal and result direction are in opposite directions, 0 :
                | no orientation is specified. 
                |
                | Example:
                | This example retrieves
                | in vakl1,val2,val3,val4,val5 parameters for solutions for
                | the LineBiTangent hybrid shape feature. Dim iVal1 As long
                | Dim iVal2 As long Dim iVal3 As long Dim iVal4 As long Dim
                | iVal5 As long ival1 = 1 ival2 = 0 ival3 = 0 ival4 = 0 ival5
                | = 0 LineBiTangent.SetChoiceNo(ivla1, iVal2, iVal3, iVal4,
                | iVal5)
                |
                | Parameters:


        :param val_1:
        :param val_2:
        :param val_3:
        :param val_4:
        :param val_5:
        :return:
        """
        return self.hybrid_shape_line_bi_tangent.SetChoiceNo(val_1, val_2, val_3, val_4, val_5)

    def set_length_type(self, i_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetLengthType
                | o Sub SetLengthType(        iType)
                | 
                | Sets the length type Default is 0.
                |
                | Parameters:
                | iType
                |    The length type = 0 : length               - the line is limited by its extremities
                |                    = 1 : infinite             - the line is infinite
                |                    = 2 : infinite start point - the line is infinite on the side of the start point
                |                    = 3 : infinite end point   - the line is infinite on the side of the end point


        :param i_type:
        :return:
        """
        return self.hybrid_shape_line_bi_tangent.SetLengthType(i_type)

    def __repr__(self):
        return f'HybridShapeLineBiTangent()'
