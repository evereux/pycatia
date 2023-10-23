#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_circle import HybridShapeCircle
from pycatia.in_interfaces.reference import Reference


class HybridShapeCircleTritangent(HybridShapeCircle):

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
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircleTritangent
                | 
                | Represents the hybrid shape circle object tangent to three
                | curves.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes:
                | 
                |     The three curves to which the circle is tangent
                |     The surface that supports the circle
                |     The orientation of each curve
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircleTritangent
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_tritangent = com_object

    @property
    def begin_of_circle(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BeginOfCircle() As long
                | 
                |     Return or Set the number of the beginning curve of the circle. This
                |     parameter is used to stabilize the resulting circle
                | 
                |     Example:
                | 
                |           This example set the beginning wire index of
                |          the hybShpcircle hybrid shape circle 
                |          
                | 
                |          hybShpcircle.BeginOfCircle = 1

        :rtype: int
        """

        return self.hybrid_shape_circle_tritangent.BeginOfCircle

    @begin_of_circle.setter
    def begin_of_circle(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_circle_tritangent.BeginOfCircle = value

    @property
    def curve1(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Curve1() As Reference
                | 
                |     Returns or sets the first curve to which the circle is or will be
                |     tangent.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in HybShpCircleFirstCurve the first curve to
                |         which the HybShpCircle hybrid shape circle is tangent.
                | 
                |          Dim HybShpCircleFirstCurve As Reference 
                |          HybShpCircleFirstCurve = HybShpCircle.Curve1

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_circle_tritangent.Curve1)

    @curve1.setter
    def curve1(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_circle_tritangent.Curve1 = reference_curve.com_object

    @property
    def curve2(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Curve2() As Reference
                | 
                |     Returns or sets the second curve to which the circle is or will be
                |     tangent.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example sets the second curve to which the HybShpCircle hybrid
                |         shape circle will be tangent to Crv5.
                | 
                |          HybShpCircle.Curve2 Crv5

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_circle_tritangent.Curve2)

    @curve2.setter
    def curve2(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_circle_tritangent.Curve2 = reference_curve.com_object

    @property
    def curve3(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Curve3() As Reference
                | 
                |     Returns or sets the third curve to which the circle is or will be
                |     tangent.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in HybShpCircleThirsCurve the third curve to
                |         which the HybShpCircle hybrid shape circle is tangent.
                | 
                |          Dim HybShpCircleThirdCurve As Reference 
                |          HybShpCircleThirdCurve = HybShpCircle.Curve3

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_circle_tritangent.Curve3)

    @curve3.setter
    def curve3(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_circle_tritangent.Curve3 = reference_curve.com_object

    @property
    def discrimination_index(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DiscriminationIndex() As long
                | 
                |     Return or set the discrimination index of the current circle. Several
                |     resulting solutions produced by the operator can be same oriented regarding to
                |     the input wire bodies. In such a case, they are sorted in order to distinguish
                |     them. The Sequence FirstOrientation - SecondOrientation - DiscriminationIndex
                |     allows you to identify a unique one-domain solution.
                | 
                |     Example:
                | 
                |           This example set the discrimination index of
                |          the hybShpcircle hybrid shape circle 
                |          
                | 
                |          hybShpcircle.DiscriminationIndex = 2

        :rtype: int
        """

        return self.hybrid_shape_circle_tritangent.DiscriminationIndex

    @discrimination_index.setter
    def discrimination_index(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_circle_tritangent.DiscriminationIndex = value

    @property
    def orientation1(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation1() As long
                | 
                |     Returns or sets the orientation of the first curve to which the circle is
                |     tangent.
                |     Role: The orientation of the first curve determines the side of this curve
                |     taken into account to find the point where the circle is tangent to the curve.
                |     This side is determined by the cross product of the normal to the support and a
                |     tangent to the curve oriented using the curve orientation.
                |     Legal values: 1 to state that the side of the curve to be taken into
                |     account is the side shown by the vector resulting from this cross product, and
                |     -1 otherwise.
                | 
                |     Example:
                |         This example sets the orientation of the first curve to which the
                |         HybShpCircle hybrid shape circle is tangent to
                |         reverse.
                | 
                |          HybShpCircle.Orientation1 -1

        :rtype: int
        """

        return self.hybrid_shape_circle_tritangent.Orientation1

    @orientation1.setter
    def orientation1(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_circle_tritangent.Orientation1 = value

    @property
    def orientation2(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation2() As long
                | 
                |     Returns or sets the orientation of the second curve to which the circle is
                |     tangent.
                |     Role: The orientation of the second curve determines the side of this curve
                |     taken into account to find the point where the circle is tangent to the curve.
                |     This side is determined by the cross product of the normal to the support and a
                |     tangent to the curve oriented using the curve orientation.
                |     Legal values: 1 to state that the side of the curve to be taken into
                |     account is the side shown by the vector resulting from this cross product, and
                |     -1 otherwise.
                | 
                |     Example:
                |         This example retrieves in HybShpCircleOrientation the orientation of
                |         the second curve to which the HybShpCircle hybrid shape circle is
                |         tangent.
                | 
                |          HybShpCircleOrientation = HybShpCircle.Orientation2

        :rtype: int
        """

        return self.hybrid_shape_circle_tritangent.Orientation2

    @orientation2.setter
    def orientation2(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_circle_tritangent.Orientation2 = value

    @property
    def orientation3(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation3() As long
                | 
                |     Returns or sets the orientation of the third curve to which the circle is
                |     tangent.
                |     Role: The orientation of the third curve determines the side of this curve
                |     taken into account to find the point where the circle is tangent to the curve.
                |     This side is determined by the cross product of the normal to the support and a
                |     tangent to the curve oriented using the curve orientation.
                |     Legal values: 1 to state that the side of the curve to be taken into
                |     account is the side shown by the vector resulting from this cross product, and
                |     -1 otherwise.
                | 
                |     Example:
                |         This example sets the orientation of the third curve to which the
                |         HybShpCircle hybrid shape circle is tangent to
                |         reverse.
                | 
                |          HybShpCircle.Orientation3 -1

        :rtype: int
        """

        return self.hybrid_shape_circle_tritangent.Orientation3

    @orientation3.setter
    def orientation3(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_circle_tritangent.Orientation3 = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or sets the circle support surface.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in HybShpCircleSupportSurf the support surface
                |         of the HybShpCircle hybrid shape circle.
                | 
                |          Dim HybShpCircleSupportSurf As Reference 
                |          HybShpCircleSupportSurf = HybShpCircle.Support

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_circle_tritangent.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_circle_tritangent.Support = reference_support.com_object

    @property
    def tangent_orientation1(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TangentOrientation1() As long
                | 
                |     Returns or sets the tangent orientation of the circle first reference
                |     element. compared to the circle itself
                | 
                |     Example:
                | 
                |           This example retrieves the tangent orientation of first reference
                |           element of
                |          the hybShpcircle hybrid shape circle in firstOrient.
                |          
                | 
                |          Dim firstOrient As long
                |          firstOrient = hybShpcircle.FirstTangentOrientation

        :rtype: int
        """

        return self.hybrid_shape_circle_tritangent.TangentOrientation1

    @tangent_orientation1.setter
    def tangent_orientation1(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_circle_tritangent.TangentOrientation1 = value

    @property
    def tangent_orientation2(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TangentOrientation2() As long
                | 
                |     Returns or sets the tangent orientation of the circle second reference
                |     element. compared to the corner itself
                | 
                |     Example:
                | 
                |           This example retrieves the tangent orientation of second reference
                |           element of
                |          the hybShpcircle hybrid shape circle in secondOrient.
                |          
                | 
                |          Dim secondOrient As long
                |          secondOrient = hybShpcircle.SecondTangentOrientation

        :rtype: int
        """

        return self.hybrid_shape_circle_tritangent.TangentOrientation2

    @tangent_orientation2.setter
    def tangent_orientation2(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_circle_tritangent.TangentOrientation2 = value

    @property
    def tangent_orientation3(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TangentOrientation3() As long
                | 
                |     Returns or sets the tangent orientation of the circle third reference
                |     element. compared to the corner itself
                | 
                |     Example:
                | 
                |           This example retrieves the tangent orientation of third reference
                |           element of
                |          the hybShpcircle hybrid shape circle in thirdOrient.
                |          
                | 
                |          Dim thirdOrient As long
                |          thirdOrient = hybShpcircle.ThirdTangentOrientation

        :rtype: int
        """

        return self.hybrid_shape_circle_tritangent.TangentOrientation3

    @tangent_orientation3.setter
    def tangent_orientation3(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_circle_tritangent.TangentOrientation3 = value

    @property
    def trim_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TrimMode() As long
                | 
                |     Returns or sets whether the circle reference curves are or should be
                |     trimmed.
                |     Legal values: 0 if the circle reference curves are not or should not be
                |     trimmed, 1 if the circle reference curves are or should be trimmed, 2 if only
                |     the first circle reference curve is or should be trimmed, 3 if only the second
                |     circle reference curve is or should be trimmed,
                | 
                |     Example:
                | 
                |           This example sets that the reference curves of
                |          the hybShpCircle hybrid shape circle should be
                |          trimmed.
                |          
                | 
                |          hybShpCircle.TrimMode = 1

        :rtype: int
        """

        return self.hybrid_shape_circle_tritangent.TrimMode

    @trim_mode.setter
    def trim_mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_circle_tritangent.TrimMode = value

    def __repr__(self):
        return f'HybridShapeCircleTritangent(name="{ self.name }")'
