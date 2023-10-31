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


class HybridShapePointOnPlane(Point):
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
                |                             HybridShapePointOnPlane
                | 
                | Point on a plane.
                | Role: Allows to access data of the point feature created on a plane with a
                | reference point or not.
                | 
                | See also:
                |     Length, Reference, HybridShapeDirection, HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_on_plane = com_object

    @property
    def first_direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstDirection() As HybridShapeDirection
                | 
                |     Returns or sets the first direction on the plane to compute the point (for
                |     stability).
                | 
                |     Example
                |     :
                |         This example retrieves in oDirection the direction of the PointOnPlane
                |         feature.
                | 
                |          Dim oDirection As CATIAHybridShapeDirection
                |          Set oDirection = PointOnPlane.FirstDirection

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_point_on_plane.FirstDirection)

    @first_direction.setter
    def first_direction(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_point_on_plane.FirstDirection = direction.com_object

    @property
    def plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Plane() As Reference
                | 
                |     Returns or sets the support plane.
                |     Sub-element(s) supported (see Boundary object):
                |     PlanarFace.
                | 
                |     Example
                |     :
                |         This example retrieves in oPlane the supporting Plane for PointOnPlane
                |         feature.
                | 
                |          Dim oPlane As CATIAReference
                |          Set oPlane  = PointOnPlane.Plane

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_point_on_plane.Plane)

    @plane.setter
    def plane(self, reference_plane: Reference):
        """
        :param Reference reference_plane:
        """

        self.hybrid_shape_point_on_plane.Plane = reference_plane.com_object

    @property
    def point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Point() As Reference
                | 
                |     Returns or sets the reference point.
                |     This data is not mandatory, if Point is
                |     null, the projection of the origin point on the plane is
                |     taken.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example
                |     :
                |         This example retrieves in oPoint the reference point for PointOnPlane
                |         feature.
                | 
                |          Dim oPoint As CATIAReference
                |          Set oPoint  = PointOnPlane.Point

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_point_on_plane.Point)

    @point.setter
    def point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_point_on_plane.Point = reference_point.com_object

    @property
    def projection_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ProjectionSurface() As Reference
                | 
                |     Returns or sets the projection surface to compute the
                |     point.
                | 
                |     Example
                |     :
                |         This example retrieves in oProjSur the projection surface of the
                |         PointOnPlane feature.
                | 
                |          Dim oProjSur As CATIAReference
                |          Set oProjSur = PointOnPlane.ProjectionSurface

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_point_on_plane.ProjectionSurface)

    @projection_surface.setter
    def projection_surface(self, reference_surface: Reference):
        """
        :param Reference reference_surface:
        """

        self.hybrid_shape_point_on_plane.ProjectionSurface = reference_surface.com_object

    @property
    def x_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property XOffset() As Length (Read Only)
                | 
                |     Returns the X cartesian coordinate in the plane.
                | 
                |     Example
                |     :
                |         This example retrieves in oX the X coordinate for PointOnPlane
                |         feature.
                | 
                |          Dim oX As  CATIALength
                |          Set oX  = PointOnPlane.XOffset

        :rtype: Length
        """

        return Length(self.hybrid_shape_point_on_plane.XOffset)

    @property
    def y_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property YOffset() As Length (Read Only)
                | 
                |     Returns the Y cartesian coordinate in the plane.
                | 
                |     Example
                |     :
                |         This example retrieves in oY the Y coordinate for PointOnPlane
                |         feature.
                | 
                |          Dim oY As  CATIALength
                |          Set oY  = PointOnPlane.YOffset

        :rtype: Length
        """

        return Length(self.hybrid_shape_point_on_plane.YOffset)

    def get_second_direction(self, o_dir_x: float, o_dir_y: float, o_dir_z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSecondDirection(double oDirX,
                | double oDirY,
                | double oDirZ)
                | 
                |     Gets the second direction on the plane to compute the point (for
                |     stability).
                |     This direction has to be kept perpendicular to the first
                |     direction
                | 
                |     Parameters:
                | 
                |         oDir
                |             second direction 
                | 
                |     See also:
                |         HybridShapeDirection

        :param float o_dir_x:
        :param float o_dir_y:
        :param float o_dir_z:
        :rtype: None
        """
        return self.hybrid_shape_point_on_plane.GetSecondDirection(o_dir_x, o_dir_y, o_dir_z)

    def set_second_direction(self, i_dir_x: float, i_dir_y: float, i_dir_z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSecondDirection(double iDirX,
                | double iDirY,
                | double iDirZ)
                | 
                |     Sets the second direction on the plane to compute the point (for
                |     stability).
                |     This direction has to be kept perpendicular to the first
                |     direction
                | 
                |     Parameters:
                | 
                |         iDir
                |             second direction 
                | 
                |     See also:
                |         HybridShapeDirection

        :param float i_dir_x:
        :param float i_dir_y:
        :param float i_dir_z:
        :rtype: None
        """
        return self.hybrid_shape_point_on_plane.SetSecondDirection(i_dir_x, i_dir_y, i_dir_z)

    def __repr__(self):
        return f'HybridShapePointOnPlane(name="{self.name}")'
