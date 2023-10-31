#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.point import Point
from pycatia.in_interfaces.reference import Reference


class HybridShapePointCenter(Point):
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
                |                             HybridShapePointCenter
                | 
                | Represents the hybrid shape PointCenter feature object.
                | Role: To access the data of the hybrid shape PointCenter feature object. It has
                | been created by the CATIAHybridShapeFactory. This data
                | includes:
                | 
                |     The circle, ellipsa element 
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_center = com_object

    @property
    def element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Element() As Reference
                | 
                |     Returns or sets the circle, ellipse or sphere.
                |     Sub-element(s) supported (see Boundary object): Edge.
                | 
                |     Example
                |     :
                |         This example retrieves in Ref_Circle the center point for the
                |         PointCenter hybrid shape feature.
                | 
                |          Dim Ref_Circle As Reference
                |          Set Ref_Circle = PointCenter.Element

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_point_center.Element)

    @element.setter
    def element(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_point_center.Element = reference_element.com_object

    def __repr__(self):
        return f'HybridShapePointCenter(name="{self.name}")'
