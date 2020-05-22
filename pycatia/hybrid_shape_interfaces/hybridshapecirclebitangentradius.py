#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeCircleBitangentRadius(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape circle object defined using a radius and
                | tangent to two curves.Role: To access the data of the hybrid shape
                | circle object.This data includes:Use the CATIAHybridShapeFactory to
                | create a HybridShapeCircleBitangentRadius object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_bitangent_radius = com_object     

    @property
    def begin_of_circle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BeginOfCircle
                | o Property BeginOfCircle(    ) As
                | 
                | Return or Set the number of the beginning curve of the
                | circle. This parameter is used to stabilize the resulting
                | circle 
                |
                | Example:
                | This example set the beginning wire index of
                | the hybShpcircle hybrid shape circle
                | hybShpcircle.BeginOfCircle = 1

        :return:
        """
        return self.hybrid_shape_circle_bitangent_radius.BeginOfCircle

    @property
    def curve1(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Curve1
                | o Property Curve1(    ) As
                | 
                | Returns or sets the first curve to which the circle is or
                | will be tangent. Sub-element(s) supported (see object): or .
                | 
                |
                | Example:
                | This example retrieves in HybShpCircleFirstCurve
                | the first curve to which the HybShpCircle hybrid shape
                | circle is tangent. Dim HybShpCircleFirstCurve As Reference
                | HybShpCircleFirstCurve = HybShpCircle.Curve1

        :return:
        """
        return self.hybrid_shape_circle_bitangent_radius.Curve1

    @curve1.setter
    def curve1(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_bitangent_radius.Curve1 = value 

    @property
    def curve2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Curve2
                | o Property Curve2(    ) As
                | 
                | Returns or sets the second curve to which the circle is or
                | will be tangent. Sub-element(s) supported (see object): or .
                | 
                |
                | Example:
                | This example sets the second curve to which the
                | HybShpCircle hybrid shape circle will be tangent to Crv5.
                | HybShpCircle.Curve2 Crv5

        :return:
        """
        return self.hybrid_shape_circle_bitangent_radius.Curve2

    @curve2.setter
    def curve2(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_bitangent_radius.Curve2 = value 

    @property
    def diameter(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Diameter
                | o Property Diameter(    ) As   (Read Only)
                | 
                | Returns the circle diameter. It is expressed as a literal.
                | Succeeds only if DiameterMode is set to True.

        :return:
        """
        return self.hybrid_shape_circle_bitangent_radius.Diameter

    @property
    def diameter_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DiameterMode
                | o Property DiameterMode(    ) As
                | 
                | Returns or sets the DiameterMode. Legal values: True implies
                | diameter False implies radius (default). When DiameterMode
                | is changed, Radius/Diameter value, which is stored will not
                | be modified. 
                |
                | Example:
                | This example sets that the
                | DiameterMode of the HybShpCircle hybrid shape circle feature
                | HybShpCircle.DiameterMode = True

        :return:
        """
        return self.hybrid_shape_circle_bitangent_radius.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_bitangent_radius.DiameterMode = value 

    @property
    def discrimination_index(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DiscriminationIndex
                | o Property DiscriminationIndex(    ) As
                | 
                | Return or set the discrimination index of the current
                | circle. Several resulting solutions produced by the operator
                | can be same oriented regarding to the input wire bodies. In
                | such a case, they are sorted in order to distinguish them.
                | The Sequence FirstOrientation - SecondOrientation -
                | DiscriminationIndex allows you to identifie a unique one-
                | domain solution. 
                |
                | Example:
                | This example set the
                | discrimination index of the hybShpcircle hybrid shape circle
                | hybShpcircle.DiscriminationIndex = 2

        :return:
        """
        return self.hybrid_shape_circle_bitangent_radius.DiscriminationIndex

    @property
    def orientation1(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation1
                | o Property Orientation1(    ) As
                | 
                | Returns or sets the orientation of the first curve to which
                | the circle is tangent. Role: The orientation of the first
                | curve determines the side of this curve taken into account
                | to find the point where the circle is tangent to the curve.
                | Legal values: To be provided by Claire (1/-1??) Example:
                | This example sets the orientation of the first curve to
                | which the HybShpCircle hybrid shape circle is tangent to
                | reverse. HybShpCircle.Orientation1 -1

        :return:
        """
        return self.hybrid_shape_circle_bitangent_radius.Orientation1

    @orientation1.setter
    def orientation1(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_bitangent_radius.Orientation1 = value 

    @property
    def orientation2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation2
                | o Property Orientation2(    ) As
                | 
                | Returns or sets the orientation of the second curve to which
                | the circle is tangent. Role: The orientation of the second
                | curve determines the side of this curve taken into account
                | to find the point where the circle is tangent to the curve.
                | Legal values: To be provided by Claire (1/-1??) Example:
                | This example retrieves in HybShpCircleOrientation the
                | orientation of the second curve to which the HybShpCircle
                | hybrid shape circle is tangent. HybShpCircleOrientation =
                | HybShpCircle.Orientation2

        :return:
        """
        return self.hybrid_shape_circle_bitangent_radius.Orientation2

    @orientation2.setter
    def orientation2(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_bitangent_radius.Orientation2 = value 

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Radius
                | o Property Radius(    ) As   (Read Only)
                | 
                | Returns the circle radius. It is expressed as a literal.
                | Succeeds only if DiameterMode is set to False.

        :return:
        """
        return self.hybrid_shape_circle_bitangent_radius.Radius

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets the circle support surface. Sub-element(s)
                | supported (see object): . 
                |
                | Example:
                | This example retrieves in
                | HybShpCircleSupportSurf the support surface of the
                | HybShpCircle hybrid shape circle. Dim
                | HybShpCircleSupportSurf As Reference HybShpCircleSupportSurf
                | = HybShpCircle.Support

        :return:
        """
        return self.hybrid_shape_circle_bitangent_radius.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_bitangent_radius.Support = value 

    @property
    def tangent_orientation1(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TangentOrientation1
                | o Property TangentOrientation1(    ) As
                | 
                | Returns or sets the tangent orientation of the circle first
                | reference element. compared to the circle itself Example:
                | This example retrieves the tangent orientation of first
                | reference element of the hybShpcircle hybrid shape circle in
                | firstOrient. Dim firstOrient As long firstOrient =
                | hybShpcircle.FirstTangentOrientation

        :return:
        """
        return self.hybrid_shape_circle_bitangent_radius.TangentOrientation1

    @tangent_orientation1.setter
    def tangent_orientation1(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_bitangent_radius.TangentOrientation1 = value 

    @property
    def tangent_orientation2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TangentOrientation2
                | o Property TangentOrientation2(    ) As
                | 
                | Returns or sets the tangent orientation of the circle second
                | reference element. compared to the corner itself Example:
                | This example retrieves the tangent orientation of second
                | reference element of the hybShpcircle hybrid shape circle in
                | secondOrient. Dim secondOrient As long secondOrient =
                | hybShpcircle.SecondTangentOrientation

        :return:
        """
        return self.hybrid_shape_circle_bitangent_radius.TangentOrientation2

    @tangent_orientation2.setter
    def tangent_orientation2(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_bitangent_radius.TangentOrientation2 = value 

    @property
    def trim_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TrimMode
                | o Property TrimMode(    ) As
                | 
                | Returns or sets whether the circle reference curves are or
                | should be trimmed. Legal values: 0 if the circle reference
                | curves are not or should not be trimmed, 1 if the circle
                | reference curves are or should be trimmed, 2 if only the
                | first circle reference curve is or should be trimmed, 3 if
                | only the second circle reference curve is or should be
                | trimmed, 
                |
                | Example:
                | This example sets that the corner
                | reference curves of the hybShpCircle hybrid shape circle
                | should be trimmed. hybShpCircle.TrimMode = 1

        :return:
        """
        return self.hybrid_shape_circle_bitangent_radius.TrimMode

    @trim_mode.setter
    def trim_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle_bitangent_radius.TrimMode = value 

    def __repr__(self):
        return f'HybridShapeCircleBitangentRadius()'
