#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_circle import HybridShapeCircle
from pycatia.in_interfaces.reference import Reference


class HybridShapeCircleCtrPt(HybridShapeCircle):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircleCtrPt
                | 
                | Represents the hybrid shape circle object defined using a center and a point on
                | the circle.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes:
                | 
                |     The circle center
                |     The point on the circle
                |     The surface that supports the circle
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircleCtrPt
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_ctr_pt = com_object

    @property
    def center(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Reference
        """

        return Reference(self.hybrid_shape_circle_ctr_pt.Center)

    @center.setter
    def center(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_circle_ctr_pt.Center = value

    @property
    def crossing_point(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CrossingPoint() As Reference
                | 
                |     Returns or sets the circle passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves the passing point of the HybShpCircle hybrid
                |         shape circle in HybShpCirclePassingPoint point.
                | 
                |          Dim HybShpCirclePassingPoint As Reference
                |          Set HybShpCirclePassingPoint = HybShpCircle.CrossingPoint

        :return: Reference
        """

        return Reference(self.hybrid_shape_circle_ctr_pt.CrossingPoint)

    @crossing_point.setter
    def crossing_point(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_circle_ctr_pt.CrossingPoint = value

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Reference
        """

        return Reference(self.hybrid_shape_circle_ctr_pt.Support)

    @support.setter
    def support(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_circle_ctr_pt.Support = value

    def is_geodesic(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func IsGeodesic() As boolean
                | 
                |     Queries whether the circle is geodesic or not.
                | 
                |     Parameters:
                | 
                |         oGeod
                |             geodesic type : when TRUE, the circle is geodesic.

        :return: bool
        """
        return bool(self.hybrid_shape_circle_ctr_pt.IsGeodesic())

    def set_geometry_on_support(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetGeometryOnSupport()
                | 
                |     Sets GeometryOnSupport of circle.
                |     It puts the circle on the surface.

        :return: None
        """
        return self.hybrid_shape_circle_ctr_pt.SetGeometryOnSupport()

    def unset_geometry_on_support(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub UnsetGeometryOnSupport()
                | 
                |     Inactivates GeometryOnSupport of circle.
                |     Note: The circle becomes euclidean.

        :return: None
        """
        return self.hybrid_shape_circle_ctr_pt.UnsetGeometryOnSupport()

    def __repr__(self):
        return f'HybridShapeCircleCtrPt(name="{ self.name }")'
