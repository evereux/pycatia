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


class HybridShapeCircle3Points(HybridShapeCircle):
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
                |                             HybridShapeCircle3Points
                | 
                | Represents the hybrid shape circle object defined using three
                | points.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes the circle three passing points.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircle2PointsRad
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle3_points = com_object

    @property
    def element1(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Element1() As Reference
                | 
                |     Returns or sets the circle first passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves the first passing point of the HybShpCircle3Pt
                |         hybrid shape circle in HybShpCircle3PtFirstPassingPoint
                |         point.
                | 
                |          Dim HybShpCircle3PtFirstPassingPoint As Reference
                |          Set HybShpCircle3PtFirstPassingPoint=
                |          HybShpCircle3Pt.Element1

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_circle3_points.Element1)

    @element1.setter
    def element1(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_circle3_points.Element1 = reference_element.com_object

    @property
    def element2(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Element2() As Reference
                | 
                |     Returns or sets the circle second passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example sets the second passing point of the HybShpCircle3Pt
                |         hybrid shape circle as the Point2 point.
                | 
                |          HybShpCircle3Pt.Element2 Point2

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_circle3_points.Element2)

    @element2.setter
    def element2(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_circle3_points.Element2 = reference_element.com_object

    @property
    def element3(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Element3() As Reference
                | 
                |     Returns or sets the circle third passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves the third passing point of the HybShpCircle3Pt
                |         hybrid shape circle in HybShpCircle3PtThirdPassingPoint
                |         point.
                | 
                |          Dim HybShpCircle3PtThirdPassingPoint As Reference
                |          Set HybShpCircle3PtThirdPassingPoint=
                |          HybShpCircle3Pt.Element3

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_circle3_points.Element3)

    @element3.setter
    def element3(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_circle3_points.Element3 = reference_element.com_object

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

        return Reference(self.hybrid_shape_circle3_points.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_circle3_points.Support = reference_support.com_object

    def remove_support(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveSupport()
                | 
                |     Removes the support surface.

        :rtype: None
        """
        return self.hybrid_shape_circle3_points.RemoveSupport()

    def __repr__(self):
        return f'HybridShapeCircle3Points(name="{self.name}")'
