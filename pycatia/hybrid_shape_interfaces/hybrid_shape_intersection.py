#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeIntersection(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeIntersection
                | 
                | Represents the hybrid shape intersection feature object.
                | Role: To access the data of the hybrid shape intersection object. This data
                | includes:
                | 
                |     The first element to intersect
                |     The second element to intersect
                | 
                | Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_intersection = com_object

    @property
    def element1(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Element1() As Reference
                | 
                |     Returns or sets the first element to intersect.
                |     Sub-element(s) supported (see Boundary object): Face, TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in FirstElem the first element to intersect for
                |         the Intersection hybrid shape feature.
                | 
                |          Dim FirstElem As Reference
                |          Set FirstElem = Intersection.Element1

        :return: Reference
        """

        return Reference(self.hybrid_shape_intersection.Element1)

    @element1.setter
    def element1(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_intersection.Element1 = value

    @property
    def element2(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Element2() As Reference
                | 
                |     Returns or sets the second element to intersect.
                |     Sub-element(s) supported (see Boundary object): Face, TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in SecondElem the second element to intersect
                |         for the Intersection hybrid shape feature.
                | 
                |          Dim SecondElem As Reference
                |          Set SecondElem = Intersection.Element2

        :return: Reference
        """

        return Reference(self.hybrid_shape_intersection.Element2)

    @element2.setter
    def element2(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_intersection.Element2 = value

    @property
    def extend_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ExtendMode() As long
                | 
                |     Returns or sets the ExtendMode flag for intersect.
                | 
                |     Example:
                |         This example retrieves in ExtendMode the ExtendMode to intersect for
                |         the Intersection hybrid shape feature.
                | 
                |          Dim ExtendMode As Reference
                |          Set ExtendMode = Intersection.ExtendMode
                |          ExtendMode is 0 when both "Extend Linear Supposr for intersection" are
                |          unchecked
                |          ExtendMode is 1 when "Extend Linear Supposr for intersection" for
                |          First Element is checked and for Second Element is
                |          unchecked
                |          ExtendMode is 2 when "Extend Linear Supposr for intersection" for
                |          First Element is unchecked and for Second Element is
                |          checked
                |          ExtendMode is 3 when both "Extend Linear Supposr for intersection" are
                |          checked

        :return: int
        """

        return self.hybrid_shape_intersection.ExtendMode

    @extend_mode.setter
    def extend_mode(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_intersection.ExtendMode = value

    @property
    def extrapolate_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ExtrapolateMode() As boolean
                | 
                |     Returns or sets the ExtrapolateMode flag for intersect.
                | 
                |     Example:
                |         This example retrieves in ExtrapolateMode the ExtrapolateMode to
                |         intersect for the Intersection hybrid shape feature.
                | 
                |          Dim ExtrapolateMode As Reference
                |          Set ExtrapolateMode = Intersection.ExtrapolateMode

        :return: bool
        """

        return self.hybrid_shape_intersection.ExtrapolateMode

    @extrapolate_mode.setter
    def extrapolate_mode(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_intersection.ExtrapolateMode = value

    @property
    def intersect_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property IntersectMode() As boolean
                | 
                |     Returns or sets the IntersectMode flag for intersect.
                | 
                |     Example:
                |         This example retrieves in IntersectMode the IntersectMode to intersect
                |         for the Intersection hybrid shape feature.
                | 
                |          Dim IntersectMode As Reference
                |          Set IntersectMode = Intersection.IntersectMode

        :return: bool
        """

        return self.hybrid_shape_intersection.IntersectMode

    @intersect_mode.setter
    def intersect_mode(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_intersection.IntersectMode = value

    @property
    def point_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property PointType() As long
                | 
                |     Returns or sets the PointType flag for intersect.
                | 
                |     Example:
                |         This example retrieves in PointType the PointType to intersect for the
                |         Intersection hybrid shape feature.
                | 
                |          Dim PointType As Reference
                |          Set PointType = Intersection.PointType

        :return: int
        """

        return self.hybrid_shape_intersection.PointType

    @point_type.setter
    def point_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_intersection.PointType = value

    @property
    def solid_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property SolidMode() As boolean
                | 
                |     Returns or sets the SolidMode flag for intersect.
                | 
                |     Example:
                |         This example retrieves in SolidMode the SolidMode to intersect for the
                |         Intersection hybrid shape feature.
                | 
                |          Dim SolidMode As Reference
                |          Set SolidMode = Intersection.SolidMode

        :return: bool
        """

        return self.hybrid_shape_intersection.SolidMode

    @solid_mode.setter
    def solid_mode(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_intersection.SolidMode = value

    def __repr__(self):
        return f'HybridShapeIntersection(name="{ self.name }")'
