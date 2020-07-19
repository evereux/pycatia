#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.hybrid_shape_interfaces.point import Point
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length


class HybridShapePointOnSurface(Point):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointOnSurface
                | 
                | Represents the Point on Surface feature objects.
                | Role: Allows to access data of the point feature created with a geodesic
                | distance in a direction to a reference point on a surface
                | 
                | See also:
                |     Length 
                | See also:
                |     Reference 
                | See also:
                |     HybridShapeDirection 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_on_surface = com_object

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Direction() As HybridShapeDirection
                | 
                |     Returns or Sets the direction from the reference point in which the point
                |     is computed.
                | 
                |     Example
                |     :
                |         This example retrieves in oDirection the direction from the reference
                |         point for PointOnSurface feature.
                | 
                |          Dim oDirection As CATIAHybridShapeDirection
                |          Set oDirection  = PointOnSurface.Direction

        :return: HybridShapeDirection
        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_point_on_surface.Direction)

    @direction.setter
    def direction(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.hybrid_shape_point_on_surface.Direction = value

    @property
    def offset(self) -> Length:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Offset() As Length (Read Only)
                | 
                |     Returns the geodesic length.
                | 
                |     Example
                |     :
                |         This example retrieves in oGeodesicOffset the offset (Geodesic Length)
                |         from the reference point for PointOnSurface feature.
                | 
                |          Dim oGeodesicOffset As CATIAReference
                |          Set oGeodesicOffset  = PointOnSurface.GeodesicOffset

        :return: Length
        :rtype: Length
        """

        return Length(self.hybrid_shape_point_on_surface.Offset)

    @property
    def point(self) -> Reference:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Point() As Reference
                | 
                |     Returns or Sets the reference point.
                |     This data is not mandatory.
                |     If no point is given, the middle point on the surface is
                |     taken.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example
                |     :
                |         This example retrieves in oPointRef the reference point for
                |         PointOnSurface feature.
                | 
                |          Dim oPointRef As CATIAReference
                |          Set oPointRef  = PointOnSurface.PointRef

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_point_on_surface.Point)

    @point.setter
    def point(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_point_on_surface.Point = value

    @property
    def surface(self) -> Reference:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Surface() As Reference
                | 
                |     Returns or Sets the surface.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example
                |     :
                |         This example retrieves in oSurface the supporting surface for
                |         PointOnSurface feature.
                | 
                |          Dim oSurface As CATIAReference
                |          Set oSurface  = PointOnSurface.Surface

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_point_on_surface.Surface)

    @surface.setter
    def surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_point_on_surface.Surface = value

    def __repr__(self):
        return f'HybridShapePointOnSurface(name="{ self.name }")'
