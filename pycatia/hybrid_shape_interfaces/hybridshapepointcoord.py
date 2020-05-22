#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from .point import Point


class HybridShapePointCoord(Point):
    """
        .. note::
            CAA V5 Visual Basic help

                | Point defined by coordinates.Role:  To access data of the point
                | feature created with its cartesian coordinates.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_coord = com_object

    @property
    def pt_ref(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PtRef
                | o Property PtRef(    ) As
                | 
                | Returns or Sets the reference point for PointCoord feature.
                | This data is not mandatory, if element is null, the origin
                | point is taken. When an element is given, X, Y and Z are
                | measured starting from this point. Sub-element(s) supported
                | (see object): . 
                |
                | Example:
                | This example retrieves in oPtRef
                | the reference point for PointCoord feature. Dim oPtRef As
                | CATIAReference Set oPtRef = PointCoord.PtRef

        :return:
        """
        return Reference(self.hybrid_shape_point_coord.PtRef)

    @property
    def ref_axis_system(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RefAxisSystem
                | o Property RefAxisSystem(    ) As
                | 
                | Returns or Sets the reference Axis System for PointCoord
                | feature. This data is not mandatory, if element is null, the
                | absolute axis system is taken. When an element is given, X,
                | Y and Z are considered in this Axis system. If reference
                | point is not specified, X,Y and Z are measured from origin
                | of this axis system. * 
                |
                | Example:
                | This example retrieves in
                | oRefAxis the reference Axis System for PointCoord feature.
                | Dim oRefAxis As CATIAReference Set oRefAxis =
                | PointCoord.RefAxisSystem

        :return:
        """
        return Reference(self.hybrid_shape_point_coord.RefAxisSystem)

    @property
    def x(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | X
                | o Property X(    ) As   (Read Only)
                | 
                | Returns X coordinate of the point. 
                |
                | Example:
                | This example
                | retrieves in oX the X coordinate for the PointCoord hybrid
                | shape feature. Dim oX As CATIALength Set oX = PointCoord.X

        :return:
        """
        return Length(self.hybrid_shape_point_coord.X)

    @property
    def y(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Y
                | o Property Y(    ) As   (Read Only)
                | 
                | Returns Y coordinate of the point. 
                |
                | Example:
                | This example
                | retrieves in oY the Y coordinate for the PointCoord hybrid
                | shape feature. Dim oY As CATIALength Set oY = PointCoord.Y

        :return:
        """
        return Length(self.hybrid_shape_point_coord.Y)

    @property
    def z(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Z
                | o Property Z(    ) As   (Read Only)
                | 
                | Returns Z coordinate of the point. 
                |
                | Example:
                | This example
                | retrieves in oZ the Z coordinate for the PointCoord hybrid
                | shape feature. Dim oZ As CATIALength Set oZ = PointCoord.Z

        :return:
        """
        return Length(self.hybrid_shape_point_coord.Z)

    def __repr__(self):
        return f'HybridShapePointCoord()'
