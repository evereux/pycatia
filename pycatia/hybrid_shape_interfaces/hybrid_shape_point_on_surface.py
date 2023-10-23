#! usr/bin/python3.9
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
            :class: toggle

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
            :class: toggle

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

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_point_on_surface.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_point_on_surface.Direction = direction.com_object

    @property
    def offset(self) -> Length:
        """
        .. note::
            :class: toggle

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

        :rtype: Length
        """

        return Length(self.hybrid_shape_point_on_surface.Offset)

    @property
    def point(self) -> Reference:
        """
        .. note::
            :class: toggle

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

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_point_on_surface.Point)

    @point.setter
    def point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_point_on_surface.Point = reference_point.com_object

    @property
    def surface(self) -> Reference:
        """
        .. note::
            :class: toggle

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

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_point_on_surface.Surface)

    @surface.setter
    def surface(self, reference_surface: Reference):
        """
        :param Reference reference_surface:
        """

        self.hybrid_shape_point_on_surface.Surface = reference_surface.com_object

    def __repr__(self):
        return f'HybridShapePointOnSurface(name="{self.name}")'
