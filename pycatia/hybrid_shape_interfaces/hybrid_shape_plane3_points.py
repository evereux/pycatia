#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.plane import Plane
from pycatia.in_interfaces.reference import Reference


class HybridShapePlane3Points(Plane):
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
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlane3Points
                | 
                | Represents the hybrid shape plane through three points feature
                | object.
                | Role: Allows to access data of the plane feature passing though three points.
                | This data includes:
                | 
                |     The first point
                |     The second point
                |     The third point
                | 
                | Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane3_points = com_object

    @property
    def first(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property First() As Reference
                | 
                |     Returns or sets the first point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example: This example retrieves in FirstPoint the first point for the Plane
                |     passing through three points hybrid shape feature.
                | 
                |      Dim FirstPoint As Reference
                |      Set FirstPoint = Plane3Points.First

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_plane3_points.First)

    @first.setter
    def first(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_plane3_points.First = reference_point.com_object

    @property
    def second(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Second() As Reference
                | 
                |     Returns or sets the second point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example: This example retrieves in SecondPoint the second point for the
                |     Plane passing through three points hybrid shape feature.
                | 
                |      Dim SecondPoint As Reference
                |      Set SecondPoint = Plane3Points.Second

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_plane3_points.Second)

    @second.setter
    def second(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_plane3_points.Second = reference_point.com_object

    @property
    def third(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Third() As Reference
                | 
                |     Returns or sets the third point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example: This example retrieves in ThirdPoint the third point for the Plane
                |     passing through three points hybrid shape feature.
                | 
                |      Dim ThridPoint As Reference
                |      Set ThirdPoint = Plane3Points.Third

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_plane3_points.Third)

    @third.setter
    def third(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_plane3_points.Third = reference_point

    def __repr__(self):
        return f'HybridShapePlane3Points(name="{self.name}")'
