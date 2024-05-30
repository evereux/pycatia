#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.mec_mod_interfaces.shape import Shape


class Scaling2(Shape):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         Scaling2
                | 
                | Represents the Scaling2 feature object.
                | This solid feature is created from an underlying HybridShapeScaling aggregated
                | by the Scaling. Role: To access the data of the feature object. This data
                | includes:
                | 
                |     The element to be transformed using the Scaling2
                |     The reference element for the Scaling2 which is a point or a
                |     plane
                |     The ratio and its value
                | 
                | Use the CATIAShapeFactory to create Part object.
                | 
                | See also:
                |     ShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.scaling2 = com_object

    @property
    def center(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Center() As Reference
                | 
                |     Returns or sets the reference element.This element can be a point or a
                |     plane.
                |     To set the property, you can use one of the following Boundary objects:
                |     PlanarFace or Vertex.
                | 
                |     Example:
                |         This example retrieves in RefElem the reference element for the
                |         Scaling2 hybrid shape feature.
                | 
                |          Dim RefElem As Reference
                |          Set RefElem = Scaling2.Center

        :rtype: Reference
        """

        return Reference(self.scaling2.Center)

    @center.setter
    def center(self, value: Reference):
        """
        :param Reference value:
        """

        self.scaling2.Center = value.com_object

    @property
    def ratio(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Ratio() As RealParam (Read Only)
                | 
                |     Returns the scaling ratio.

        :rtype: RealParam
        """

        return RealParam(self.scaling2.Ratio)

    @property
    def ratio_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RatioValue() As double
                | 
                |     Returns or sets the scaling ratio value.
                | 
                |     Example:
                |         This example retrieves in Value the ratio value for the Scaling hybrid
                |         shape feature.
                | 
                |          Dim Value As double
                |          Set Value = Scaling2.RatioValue

        :rtype: float
        """

        return self.scaling2.RatioValue

    @ratio_value.setter
    def ratio_value(self, value: float):
        """
        :param float value:
        """

        self.scaling2.RatioValue = value

    def __repr__(self):
        return f'Scaling2(name="{ self.name }")'
