#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeReflectLine(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape reflect line feature object.Role: To
                | access the data of the hybrid shape reflect line feature object. This
                | data includes:Use the  CATIAHybridShapeFactory to create a
                | HybridShapeReflectLine object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_reflect_line = com_object     

    @property
    def angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Angle
                | o Property Angle(    ) As
                | 
                | Returns or sets the angle used to create the reflectline.
                | 
                |
                | Example:
                | This example retrieves in Ang the angle for the
                | RelectLine hybrid shape feature. Dim Ang As CATIAAngle Set
                | Ang = ReflectLine.Angle

        :return:
        """
        return self.hybrid_shape_reflect_line.Angle

    @angle.setter
    def angle(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_reflect_line.Angle = value 

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction
                | o Property Direction(    ) As
                | 
                | Returns or sets the direction used to create the cylindrical
                | reflectline. 
                |
                | Example:
                | This example retrieves in Dir the
                | direction for the cylindrical RelectLine hybrid shape
                | feature. Dim Dir As CATIAHybridShapeDirection Set Dir =
                | ReflectLine.Direction

        :return:
        """
        return self.hybrid_shape_reflect_line.Direction

    @direction.setter
    def direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_reflect_line.Direction = value 

    @property
    def orientation_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OrientationDirection
                | o Property OrientationDirection(    ) As
                | 
                | Returns or sets the direction orientation used to compute
                | the reflect line. Role: The orientation is used to define
                | the angle between the direction and the normal to the
                | support of the points on the result curve. The orientation
                | is the same than or the inverse of the result of the cross
                | product: Normal(support) ^ Tangent(FirstReferenceCurve).
                | Legal values: 1 for same orientation, and -1 for inverse

        :return:
        """
        return self.hybrid_shape_reflect_line.OrientationDirection

    @orientation_direction.setter
    def orientation_direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_reflect_line.OrientationDirection = value 

    @property
    def orientation_support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OrientationSupport
                | o Property OrientationSupport(    ) As
                | 
                | Returns or sets the support orientation used to compute the
                | reflect line. Role: The orientation is used to define the
                | angle between the direction and the normal to the support of
                | the points on the result curve. The orientation is the same
                | than or the inverse of the result of the cross product:
                | Normal(support) ^ Tangent(FirstReferenceCurve). Legal
                | values: 1 for same orientation, and -1 for inverse

        :return:
        """
        return self.hybrid_shape_reflect_line.OrientationSupport

    @orientation_support.setter
    def orientation_support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_reflect_line.OrientationSupport = value 

    @property
    def origin(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Origin
                | o Property Origin(    ) As
                | 
                | Returns or sets the origin point used to create the conical
                | reflectline. Sub-element(s) supported (see object): .
                | 
                |
                | Example:
                | This example retrieves in Point the origin point
                | for the conical ReflectLine hybrid shape feature. Dim Point
                | As Reference Set Point = ReflectLine.Origin

        :return:
        """
        return self.hybrid_shape_reflect_line.Origin

    @origin.setter
    def origin(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_reflect_line.Origin = value 

    @property
    def source_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SourceType
                | o Property SourceType(    ) As
                | 
                | Returns or sets whether the reflectline curve is or should
                | be created with infinite light source (cylindrical) or with
                | finite point light source (conical). Role: The SourceType
                | indicates whether the created reflectline curve is compute
                | with infinite light source for cylindrical type or with
                | finite point light source for conical type. Legal values: 0
                | for cylindrical and 1 for conical.

        :return:
        """
        return self.hybrid_shape_reflect_line.SourceType

    @source_type.setter
    def source_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_reflect_line.SourceType = value 

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets the support surface used to create the
                | reflectline. Sub-element(s) supported (see object): .
                | 
                |
                | Example:
                | This example retrieves in Surface the support
                | surface for the RelectLine hybrid shape feature. Dim Surface
                | As Reference Set Surface = ReflectLine.Support

        :return:
        """
        return self.hybrid_shape_reflect_line.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_reflect_line.Support = value 

    @property
    def type_solution(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TypeSolution
                | o Property TypeSolution(    ) As
                | 
                | Returns or sets whether the reflectline curve is or should
                | be created with the normal to the support or the tangent
                | plane to the support. Role: The TypeSolution indicates
                | whether the created reflectline curve is compute with the
                | angle between the normale to the support and the direction
                | or with the angle between the tangent plane to the support
                | and the direction. Legal values: 0 for the normal and 1 for
                | the tangent plane.

        :return:
        """
        return self.hybrid_shape_reflect_line.TypeSolution

    @type_solution.setter
    def type_solution(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_reflect_line.TypeSolution = value 

    def invert_orientation_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertOrientationDirection
                | o Sub InvertOrientationDirection(    )
                | 
                | Inverts the orientation of direction. This example inverts
                | the direction orientation of hybRefLine hybrid shape reflect
                | line object. hybRefLine.InvertOrientationDirection
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_reflect_line.InvertOrientationDirection()

    def invert_orientation_support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertOrientationSupport
                | o Sub InvertOrientationSupport(    )
                | 
                | Inverts the orientation of support. This example inverts the
                | support orientation of hybRefLine hybrid shape reflect line
                | object. hybRefLine.InvertOrientationSupport
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_reflect_line.InvertOrientationSupport()

    def __repr__(self):
        return f'HybridShapeReflectLine()'
