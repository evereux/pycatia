#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_circle import HybridShapeCircle
from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length


class HybridShapeCircleCtrRad(HybridShapeCircle):

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
                |                             HybridShapeCircleCtrRad
                | 
                | Represents the hybrid shape circle object defined using a center and a
                | radius.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes:
                | 
                |     The circle center
                |     The circle radius
                |     The surface that supports the circle
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircleCtrRad
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_ctr_rad = com_object

    @property
    def center(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Center() As Reference
                | 
                |     Returns or sets the circle center.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in HybShpCircleCenter the center of the
                |         HybShpCircle hybrid shape circle.
                | 
                |          Dim HybShpCircleCenter As Reference
                |          HybShpCircleCenter = HybShpCircle.Center

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_circle_ctr_rad.Center)

    @center.setter
    def center(self, reference_center: Reference):
        """
        :param Reference reference_center:
        """

        self.hybrid_shape_circle_ctr_rad.Center = reference_center.com_object

    @property
    def diameter(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Diameter() As Length (Read Only)
                | 
                |     Returns the circle diameter.
                |     It is expressed as a Length literal. Succeeds only if DiameterMode is set
                |     to True. 
                | 
                | Example:
                |     This example retrieves in HybShpCircleDiameter the diameter of the
                |     HybShpCircle hybrid shape circle feature
                | 
                |      Dim HybShpCircleDiameter As Length
                |      HybShpCircleDiameter = HybShpCircle.Diameter

        :rtype: Length
        """

        return Length(self.hybrid_shape_circle_ctr_rad.Diameter)

    @property
    def diameter_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DiameterMode() As boolean
                | 
                |     Returns or sets the DiameterMode.
                |     Legal values: True implies diameter False implies radius (default). When
                |     DiameterMode is changed, Radius/Diameter value, which is stored will not be
                |     modified.
                | 
                |     Example:
                | 
                |            This example sets that the DiameterMode of
                |           the HybShpCircle hybrid shape circle feature
                |           
                | 
                |           HybShpCircle.DiameterMode = True

        :rtype: bool
        """

        return self.hybrid_shape_circle_ctr_rad.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_circle_ctr_rad.DiameterMode = value

    @property
    def first_direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstDirection() As HybridShapeDirection
                | 
                |     Returns or sets the first direction used to set the angles reference.
                |     
                | 
                | Example:
                |     This example retrieves in myHybridShapeDirection the first direction of the
                |     HybShpCircle hybrid shape circle feature
                | 
                |      Dim myHybridShapeDirection As CATIAHybridShapeDirection 
                |      myHybridShapeDirection = HybShpCircle.FirstDirection
                |      
                | 
                |     See also:
                |         HybridShapeDirection

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_circle_ctr_rad.FirstDirection)

    @first_direction.setter
    def first_direction(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_circle_ctr_rad.FirstDirection = direction.com_object

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Radius() As Length (Read Only)
                | 
                |     Returns the circle radius. It is expressed as a Length literal. Succeeds
                |     only if DiameterMode is set to False. 
                | 
                | Example:
                |     This example retrieves in HybShpCircleRadius the radius of the HybShpCircle
                |     hybrid shape circle.
                | 
                |      Dim HybShpCircleRadius As Length
                |      HybShpCircleRadius = HybShpCircle.Radius

        :rtype: Length
        """

        return Length(self.hybrid_shape_circle_ctr_rad.Radius)

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

        return Reference(self.hybrid_shape_circle_ctr_rad.Support)

    @support.setter
    def support(self, support_reference: Reference):
        """
        :param Reference support_reference:
        """

        self.hybrid_shape_circle_ctr_rad.Support = support_reference.com_object

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
                |         oDirX,
                |             oDirY, oDirZ. second direction 
                | 
                |     See also:
                |         HybridShapeDirection

        :param float o_dir_x:
        :param float o_dir_y:
        :param float o_dir_z:
        :rtype: None
        """
        return self.hybrid_shape_circle_ctr_rad.GetSecondDirection(o_dir_x, o_dir_y, o_dir_z)

    def is_geodesic(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func IsGeodesic() As boolean
                | 
                |     Queries whether the circle is geodesic or not.
                | 
                |     Parameters:
                | 
                |         oGeod
                |             geodesic type : when TRUE, the circle is geodesic.

        :rtype: bool
        """
        return self.hybrid_shape_circle_ctr_rad.IsGeodesic()

    def set_geometry_on_support(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetGeometryOnSupport()
                | 
                |     Sets GeometryOnSupport of circle.
                |     It puts the circle on the surface.

        :rtype: None
        """
        return self.hybrid_shape_circle_ctr_rad.SetGeometryOnSupport()

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
                |         iDirX,
                |             iDirY, iDirZ. second direction 
                | 
                |     See also:
                |         HybridShapeDirection

        :param float i_dir_x:
        :param float i_dir_y:
        :param float i_dir_z:
        :rtype: None
        """
        return self.hybrid_shape_circle_ctr_rad.SetSecondDirection(i_dir_x, i_dir_y, i_dir_z)

    def unset_geometry_on_support(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub UnsetGeometryOnSupport()
                | 
                |     Inactivates GeometryOnSupport of circle.
                |     Note: The circle becomes euclidean.

        :rtype: None
        """
        return self.hybrid_shape_circle_ctr_rad.UnsetGeometryOnSupport()

    def __repr__(self):
        return f'HybridShapeCircleCtrRad(name="{ self.name }")'
