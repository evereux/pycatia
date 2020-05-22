#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeCircle(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape circle object.Role: To access the data of
                | the hybrid shape circle object.This data includes:All interfaces for
                | different type of circle derivates HybridShapeCircle.Use the
                | CATIAHybridShapeFactory to create a HybridShapeCircle objects.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle = com_object     

    @property
    def axis_computation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AxisComputation
                | o Property AxisComputation(    ) As
                | 
                | Returns or sets the axis computation mode. 
                |
                | Example:
                | This
                | example retrieves the axis computation mode of the
                | hybShpCircle Dim axisComp As Boolean axisComp =
                | hybShpCircle.AxisComputation

        :return:
        """
        return self.hybrid_shape_circle.AxisComputation

    @axis_computation.setter
    def axis_computation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_circle.AxisComputation = value 

    @property
    def axis_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AxisDirection
                | o Property AxisDirection(    ) As
                | 
                | Role: To get_Direction on the object.

        :return:
        """
        return self.hybrid_shape_circle.AxisDirection

    @property
    def end_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndAngle
                | o Property EndAngle(    ) As   (Read Only)
                | 
                | Returns the circle end angle. 
                |
                | Example:
                | This example
                | retrieves in ShpCircleEndAngle the end angle of the
                | ShpCircle hybrid shape circle. Dim ShpCircleEndAngle As
                | Angle ShpCircleEndAngle = ShpCircle.EndAngle

        :return:
        """
        return self.hybrid_shape_circle.EndAngle

    @property
    def start_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | StartAngle
                | o Property StartAngle(    ) As   (Read Only)
                | 
                | Returns the circle start angle. 
                |
                | Example:
                | This example
                | retrieves in ShpCircleStartAngle the end angle of the
                | ShpCircle hybrid shape circle. Dim ShpCircleStartAngle As
                | Angle ShpCircleStartAngle = ShpCircle.StartAngle

        :return:
        """
        return self.hybrid_shape_circle.StartAngle

    def get_axis(self, i_position, o_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAxis
                | o Sub GetAxis(        iPosition,
                |                       oAxis)
                | 
                | Returns the axis of the Circle.
                |
                | Parameters:
                | iType
                |      Type of axis to be retrived.
                |      3 - CATGSMAxisLineType_NormalToCircle   
                |      2 - CATGSMAxisLineType_NormalToDirection
                |      1 - CATGSMAxisLineType_AlignedWithDirection
                |    
                |  oAxis
                |      Reference to the element.

                | Examples:
                | This example retrieves the axis of the circle. HybShpCircle
                | hybrid shape circle. Dim AxisRef As Reference
                | HybShpCircle.GetAxis 1, AxisRef

        :param i_position:
        :param o_axis:
        :return:
        """
        return self.hybrid_shape_circle.GetAxis(i_position, o_axis)

    def get_center(self, o_center_x, o_center_y, o_center_z):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCenter
                | o Sub GetCenter(        oCenterX,
                |                         oCenterY,
                |                         oCenterZ)
                | 
                | Gets the mathematical center of the circle. This information
                | is available once the circle has been computed.
                |
                | Parameters:
                | oCenterX,
                |  oCenterY, oCenterZ,      circle center


        :param o_center_x:
        :param o_center_y:
        :param o_center_z:
        :return:
        """
        return self.hybrid_shape_circle.GetCenter(o_center_x, o_center_y, o_center_z)

    def get_free_center(self, io_center):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFreeCenter
                | o Sub GetFreeCenter(        ioCenter)
                | 
                | Returns the circle center.
                |
                | Parameters:
                | oCenter
                |     The circle center. It is returned as an array of three coordinates in SafeArrayVariant

                | Examples:
                | This example retrieves in HybShpCircleCenter the center of
                | the HybShpCircle hybrid shape circle. Dim HybShpCircleCenter
                | ReDim HybShpCircleCenter(2)
                | ShpCircle.GetFreeRadius(HybShpCircleCenter) You can access
                | each center coordinate as follows: x is in
                | HybShpCircleCenter(0) y is in HybShpCircleCenter(1) z is in
                | HybShpCircleCenter(2)

        :param io_center:
        :return:
        """
        return self.hybrid_shape_circle.GetFreeCenter(io_center)

    def get_free_radius(self, o_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFreeRadius
                | o Sub GetFreeRadius(        oRadius)
                | 
                | Returns the circle radius.
                |
                | Parameters:
                | oRadius
                |     The circle radius

                | Examples:
                | This example retrieves in HybShpCircleRadius the radius of
                | the HybShpCircle hybrid shape circle. double
                | HybShpCircleRadius
                | ShpCircle.GetFreeRadius(HybShpCircleRadius)

        :param o_radius:
        :return:
        """
        return self.hybrid_shape_circle.GetFreeRadius(o_radius)

    def get_limitation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLimitation
                | o Func GetLimitation(    ) As
                | 
                | Gets the limitation type for the circle.
                |
                | Parameters:
                | oLimit
                |  (Angles = 0, Whole = 1, Trimmed = 2, Complementary = 3).
                |       circle limitation


        :return:
        """
        return self.hybrid_shape_circle.GetLimitation()

    def set_limitation(self, i_limitation):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetLimitation
                | o Sub SetLimitation(        iLimitation)
                | 
                | Set the circle limitation type.
                |
                | Parameters:
                | iLimitation
                |    The circle limitation type
                |    Legal values:
                |    
                | 0 Angles
                |      1 Whole
                |      2 Trimmed
                |      3 Complementary

                | Examples:
                | This example sets the limitiation type of the ShpCircle
                | hybrid shape circle to trimmed. ShpCircle.SetLimitation 2

        :param i_limitation:
        :return:
        """
        return self.hybrid_shape_circle.SetLimitation(i_limitation)

    def __repr__(self):
        return f'HybridShapeCircle()'
