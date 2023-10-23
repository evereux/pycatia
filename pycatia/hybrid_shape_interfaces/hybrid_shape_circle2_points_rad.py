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
from pycatia.knowledge_interfaces.length import Length


class HybridShapeCircle2PointsRad(HybridShapeCircle):
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
                |                             HybridShapeCircle2PointsRad
                | 
                | Represents the hybrid shape circle object defined using two points and a
                | radius.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes:
                | 
                |     The circle two passing points
                |     The circle radius
                |     The surface that supports the circle
                |     The circle orientation
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircle2PointsRad
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle2_points_rad = com_object

    @property
    def diameter(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Diameter() As Length (Read Only)
                | 
                |     Returns the circle diameter. It is expressed as a Length literal. Succeeds
                |     only if DiameterMode is set to True. 
                | 
                | Example:
                |     This example retrieves in HybShpCircleDiameter the diameter of the
                |     HybShpCircle hybrid shape circle feature
                | 
                |      Dim HybShpCircleDiameter As Length
                |      HybShpCircleDiameter = HybShpCircle.Diameter

        :rtype: Length
        """

        return Length(self.hybrid_shape_circle2_points_rad.Diameter)

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

        return self.hybrid_shape_circle2_points_rad.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_circle2_points_rad.DiameterMode = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation() As long
                | 
                |     Returns or sets the circle orientation.
                |     Role: The circle orientation indicates which side of the line made up using
                |     the two passing points is used to create the major part of the circle. It is
                |     determined using the cross product of the normal to the suppport and the vector
                |     made up using the two passing points (Pt1-Pt2).
                |     Legal values: 1 to state that the major part of the circle is or should be
                |     created on the side of the line shown by the vector resulting from this cross
                |     product, and -1 otherwise.
                | 
                |     Example:
                |         This example retrieves in HybShpCircleOrientation the orientation of
                |         the HybShpCircle hybrid shape circle.
                | 
                |          HybShpCircleOrientation = HybShpCircle.Orientation

        :rtype: int
        """

        return self.hybrid_shape_circle2_points_rad.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_circle2_points_rad.Orientation = value

    @property
    def pt1(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Pt1() As Reference
                | 
                |     Returns or sets the circle first passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves the first passing point of the HybShpCircle
                |         hybrid shape circle in HybShpCircleFirstPassingPoint
                |         point.
                | 
                |          Dim HybShpCircleFirstPassingPoint As Reference
                |          Set HybShpCircleFirstPassingPoint = HybShpCircle.Pt1

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_circle2_points_rad.Pt1)

    @pt1.setter
    def pt1(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_circle2_points_rad.Pt1 = reference_point.com_object

    @property
    def pt2(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Pt2() As Reference
                | 
                |     Returns or sets the circle second passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example sets the second passing point of the HybShpCircle hybrid
                |         shape circle as the Point12 point.
                | 
                |          HybShpCircle.Pt2 Point12

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_circle2_points_rad.Pt2)

    @pt2.setter
    def pt2(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_circle2_points_rad.Pt2 = reference_point.com_object

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Radius() As Length (Read Only)
                | 
                |     Returns the circle radius.
                | 
                |     Parameters:
                | 
                |         Radius
                |             The circle radius, expressed as a 
                | 
                |         Length literal. Succeeds only if DiameterMode is set to False.
                |         
                | 
                | Example:
                |     This example retrieves in HybShpCircleRadius the radius of the HybShpCircle
                |     hybrid shape circle.
                | 
                |      Dim HybShpCircleRadius As Length
                |      HybShpCircleRadius = HybShpCircle.Radius

        :rtype: Length
        """

        return Length(self.hybrid_shape_circle2_points_rad.Radius)

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

        return Reference(self.hybrid_shape_circle2_points_rad.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_circle2_points_rad.Support = reference_support

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
        return self.hybrid_shape_circle2_points_rad.IsGeodesic()

    def set_geometry_on_support(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetGeometryOnSupport()
                | 
                |     Sets GeometryOnSupport of circle.
                |     It puts the circle on the surface. S_OK if OK, E_FAIL if fail

        :rtype: None
        """
        return self.hybrid_shape_circle2_points_rad.SetGeometryOnSupport()

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
        return self.hybrid_shape_circle2_points_rad.UnsetGeometryOnSupport()

    def __repr__(self):
        return f'HybridShapeCircle2PointsRad(name="{self.name}")'
