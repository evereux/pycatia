#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeCircle(HybridShape):
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
                |                         HybridShapeCircle
                | 
                | Represents the hybrid shape circle object.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes:
                | 
                |     The circle radius
                |     Two circle center
                |     The circle arc limitation mode
                |     The circle start and end angles
                | 
                | All interfaces for different type of circle derivates
                | HybridShapeCircle.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircle
                | objects.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle = com_object

    @property
    def axis_computation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AxisComputation() As boolean
                | 
                |     Returns or sets the axis computation mode.
                | 
                |     Example:
                | 
                |           This example retrieves the axis computation mode of
                |          the hybShpCircle
                |          
                | 
                |          Dim axisComp As Boolean
                |          axisComp = hybShpCircle.AxisComputation

        :return: bool
        :rtype: bool
        """

        return self.hybrid_shape_circle.AxisComputation

    @axis_computation.setter
    def axis_computation(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_circle.AxisComputation = value

    @property
    def axis_direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AxisDirection() As HybridShapeDirection
                | 
                |     Role: To get_Direction on the object.
                | 
                |     Parameters:
                | 
                |         oDir
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         HybridShapeDirection 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: HybridShapeDirection
        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_circle.AxisDirection)

    @axis_direction.setter
    def axis_direction(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_circle.AxisDirection = direction.com_object

    @property
    def end_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EndAngle() As Angle (Read Only)
                | 
                |     Returns the circle end angle.
                | 
                |     Example:
                |         This example retrieves in ShpCircleEndAngle the end angle of the
                |         ShpCircle hybrid shape circle.
                | 
                |          Dim ShpCircleEndAngle As Angle
                |          ShpCircleEndAngle = ShpCircle.EndAngle

        :return: Angle
        :rtype: Angle
        """

        return Angle(self.hybrid_shape_circle.EndAngle)

    @property
    def start_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property StartAngle() As Angle (Read Only)
                | 
                |     Returns the circle start angle.
                | 
                |     Example:
                |         This example retrieves in ShpCircleStartAngle the end angle of the
                |         ShpCircle hybrid shape circle.
                | 
                |          Dim ShpCircleStartAngle As Angle
                |          ShpCircleStartAngle = ShpCircle.StartAngle

        :return: Angle
        :rtype: Angle
        """

        return Angle(self.hybrid_shape_circle.StartAngle)

    def get_axis(self, i_position: int, o_axis: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetAxis(long iPosition,
                | Reference oAxis)
                | 
                |     Returns the axis of the Circle.
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of axis to be retrived. 3 - CATGSMAxisLineType_NormalToCircle
                |             2 - CATGSMAxisLineType_NormalToDirection 1 -
                |             CATGSMAxisLineType_AlignedWithDirection 
                |         oAxis
                |             Reference to the element.
                | 
                |             Example:
                |                 This example retrieves the axis of the circle. HybShpCircle
                |                 hybrid shape circle.
                | 
                |                  Dim AxisRef As Reference
                |                  HybShpCircle.GetAxis 1, AxisRef

        :param int i_position:
        :param Reference o_axis:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_circle.GetAxis(i_position, o_axis.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_axis'
        # # vba_code = """
        # # Public Function get_axis(hybrid_shape_circle)
        # #     Dim iPosition (2)
        # #     hybrid_shape_circle.GetAxis iPosition
        # #     get_axis = iPosition
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_center(self, o_center_x: float, o_center_y: float, o_center_z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetCenter(double oCenterX,
                | double oCenterY,
                | double oCenterZ)
                | 
                |     Gets the mathematical center of the circle. This information is available
                |     once the circle has been computed.
                | 
                |     Parameters:
                | 
                |         oCenterX,
                |             oCenterY, oCenterZ, circle center

        :param float o_center_x:
        :param float o_center_y:
        :param float o_center_z:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_circle.GetCenter(o_center_x, o_center_y, o_center_z)

    def get_free_center(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetFreeCenter(CATSafeArrayVariant ioCenter)
                | 
                |     Returns the circle center.
                | 
                |     Parameters:
                | 
                |         oCenter
                |             The circle center. It is returned as an array of three coordinates
                |             in SafeArrayVariant 
                | 
                |     Example:
                |         This example retrieves in HybShpCircleCenter the center of the
                |         HybShpCircle hybrid shape circle.
                | 
                |          Dim HybShpCircleCenter
                |          ReDim HybShpCircleCenter(2)
                |          ShpCircle.GetFreeRadius(HybShpCircleCenter)
                |          
                | 
                |         You can access each center coordinate as follows:
                | 
                |             x is in HybShpCircleCenter(0)
                |             y is in HybShpCircleCenter(1)
                |             z is in HybShpCircleCenter(2)

        :return: tuple
        :rtype: tuple
        """
        vba_function_name = 'get_free_center'
        vba_code = """
        Public Function get_free_center(hybrid_shape_circle)
            Dim ioCenter (2)
            hybrid_shape_circle.GetFreeCenter ioCenter
            get_free_center = ioCenter
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_free_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetFreeRadius(double oRadius)
                | 
                |     Returns the circle radius.
                | 
                |     Parameters:
                | 
                |         oRadius
                |             The circle radius 
                | 
                |     Example:
                |         This example retrieves in HybShpCircleRadius the radius of the
                |         HybShpCircle hybrid shape circle.
                | 
                |          double HybShpCircleRadius
                |          ShpCircle.GetFreeRadius(HybShpCircleRadius)

        :return: float
        :rtype: float
        """
        return self.hybrid_shape_circle.GetFreeRadius()

    def get_limitation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLimitation() As long
                | 
                |     Gets the limitation type for the circle.
                | 
                |     Parameters:
                | 
                |         oLimit
                |             (Angles = 0, Whole = 1, Trimmed = 2, Complementary = 3). circle limitation

        :return: int
        :rtype: int
        """
        return self.hybrid_shape_circle.GetLimitation()

    def set_limitation(self, i_limitation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLimitation(long iLimitation)
                | 
                |     Set the circle limitation type.
                | 
                |     Parameters:
                | 
                |         iLimitation
                |             The circle limitation type
                |             Legal values:
                | 
                |             0
                |                 Angles 
                |             1
                |                 Whole 
                |             2
                |                 Trimmed 
                |             3
                |                 Complementary 
                | 
                |     Example:
                |         This example sets the limitiation type of the ShpCircle hybrid shape
                |         circle to trimmed.
                | 
                |          ShpCircle.SetLimitation 2

        :param int i_limitation:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_circle.SetLimitation(i_limitation)

    def __repr__(self):
        return f'HybridShapeCircle(name="{self.name}")'
