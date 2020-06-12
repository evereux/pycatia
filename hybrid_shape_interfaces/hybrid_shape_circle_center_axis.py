#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_circle import HybridShapeCircle
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length


class HybridShapeCircleCenterAxis(HybridShapeCircle):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircleCenterAxis
                | 
                | Represents the hybrid shape circle object defined using a point and
                | axis/line.
                | Role: To access the data of the hybrid shape circle center axis
                | object.
                | 
                | This data includes:
                | 
                |     Point
                |     Axis/Line
                |     Value of radius/diameter
                |     Diameter Mode
                |     Projection Mode
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircleCenterAxis
                | object.
                | 
                | See also:
                |     HybridShapeFactory.AddNewCircleCenterAxis
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_center_axis = com_object

    @property
    def axis(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Axis() As Reference
                | 
                |     Returns or sets the Axis of the circle.
                | 
                |     Example:
                |         This example retrieves in CircleAxis the Axis of plane in which circle
                |         is lying from HybShpCircle hybrid shape circle center axis
                |         feature
                | 
                |          Dim CircleAxis As Reference 
                |          Set CircleAxis = HybShpCircle.Axis

        :return: Reference
        """

        return Reference(self.hybrid_shape_circle_center_axis.Axis)

    @axis.setter
    def axis(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_circle_center_axis.Axis = value

    @property
    def diameter(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Diameter() As Length (Read Only)
                | 
                |     Returns the circle diameter. It is expressed as a Length literal. Succeeds
                |     only if DiameterMode is set to True. 
                | 
                | Example:
                |     This example retrieves in HybShpCircleDiameter the diameter of the
                |     HybShpCircle hybrid shape circle center axis feature
                | 
                |      Dim HybShpCircleDiameter As Length
                |      HybShpCircleDiameter = HybShpCircle.Diameter

        :return: Length
        """

        return Length(self.hybrid_shape_circle_center_axis.Diameter)

    @property
    def diameter_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
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
                |           the HybShpCircle hybrid shape circle center axis
                |           feature
                |           
                | 
                |           HybShpCircle.DiameterMode = True

        :return: bool
        """

        return self.hybrid_shape_circle_center_axis.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_circle_center_axis.DiameterMode = value

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Point() As Reference
                | 
                |     Returns or sets the Point of the circle.
                | 
                |     Example:
                |         This example retrieves in CirclePoint the point used for center
                |         computation from HybShpCircle hybrid shape circle center axis
                |         feature
                | 
                |          Dim CirclePoint As Reference 
                |          Set CirclePoint = HybShpCircle.Point

        :return: Reference
        """

        return Reference(self.hybrid_shape_circle_center_axis.Point)

    @point.setter
    def point(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_circle_center_axis.Point = value

    @property
    def projection_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ProjectionMode() As boolean
                | 
                |     Returns or sets the ProjectionMode.
                |     Legal values: True (default) implies point will be projected on to
                |     axis/line False implies that point will be center of the
                |     circle.
                | 
                |     Example:
                | 
                |            This example sets that the ProjectionMode of
                |           the HybShpCircle hybrid shape circle center axis
                |           feature
                |           
                | 
                |           HybShpCircle.ProjectionMode = True

        :return: bool
        """

        return self.hybrid_shape_circle_center_axis.ProjectionMode

    @projection_mode.setter
    def projection_mode(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_circle_center_axis.ProjectionMode = value

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Radius() As Length (Read Only)
                | 
                |     Returns the circle radius. It is expressed as a Length literal. Succeeds
                |     only if DiameterMode is set to False. 
                | 
                | Example:
                |     This example retrieves in HybShpCircleRadius the radius of the HybShpCircle
                |     hybrid shape circle center axis feature
                | 
                |      Dim HybShpCircleRadius As Length
                |      HybShpCircleRadius = HybShpCircle.Radius
                |      
                | 
                |     Copyright © 1999-2011, Dassault Systèmes. All rights
                |     reserved.

        :return: Length
        """

        return Length(self.hybrid_shape_circle_center_axis.Radius)

    def __repr__(self):
        return f'HybridShapeCircleCenterAxis(name="{ self.name }")'
