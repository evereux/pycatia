#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.system_interfaces.any_object import AnyObject


class AxisSystem(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AxisSystem
                |
                | The object Axis System A axis system has got one origin point and three
                | orthogonal axes, crossing at the origin point.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.axis_system = com_object

    @property
    def axis_rotation_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AxisRotationAngle() As Angle (Read Only)
                | 
                |     Returns the rotation angle of an axis system. Succeeds only if the axis
                |     system is defined by a rotation around an axis, wich means that its type is
                |     catAxisSystemAxisRotation.

        :rtype: Angle
        """

        return Angle(self.axis_system.AxisRotationAngle)

    @property
    def axis_rotation_reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AxisRotationReference() As Reference
                | 
                |     Returns the reference for the axis rotation. Succeeds only if the axis
                |     system is defined by a rotation around an axis, wich means that its type is
                |     catAxisSystemAxisRotation.

        :rtype: Reference
        """

        return Reference(self.axis_system.AxisRotationReference)

    @axis_rotation_reference.setter
    def axis_rotation_reference(self, value: Reference):
        """
        :param Reference value:
        """

        self.axis_system.AxisRotationReference = value.com_object

    @property
    def is_current(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property IsCurrent() As boolean
                | 
                |     Returns True if the axis system is the current one, else returns False.
                |     Sets the axis system as the current one or not.
                |
                |     Example:
                |         The following example returns in isCurrent True if the axis system
                |         axisSystem is the current one :
                |
                |          isCurrent = axisSystem.IsCurrent
                |
                |         The following example sets the axis system axisSystem as the current
                |         one :
                |
                |          axisSystem.IsCurrent = 1
                |
                |         The following example sets the axis system axisSystem as not the
                |         current one :
                |
                |          axisSystem.IsCurrent = 0

        :rtype: bool
        """

        return self.axis_system.IsCurrent

    @is_current.setter
    def is_current(self, value: bool):
        """
        :param bool value:
        """

        self.axis_system.IsCurrent = value

    @property
    def origin_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property OriginPoint() As Reference
                | 
                |     Returns or sets the geometric point which defines the origin of the axis
                |     system.
                |     OriginPoint is and must be a reference on a geometric 3D
                |     point.
                |
                |     Example:
                |         The following example sets the point Point.1 of the Geometrical Set
                |         Geometrical Set.1 as the origin point of the axis system
                |         AxisSystem0:
                |
                |      Dim HybridBody4 As AnyObject
                |      Set HybridBody4 = Body1.HybridBodies.Item  ( "Geometrical Set.1" )
                |      Dim HybridShapePointCoord5 As AnyObject
                |      Set HybridShapePointCoord5 = HybridBody4.HybridShapes.Item  ( "Point.1" )
                |      Dim Reference6 As Reference
                |      Set Reference6 = CATIA.ActiveDocument.Part.CreateReferenceFromGeometry(HybridShapePointCoord5)
                |      AxisSystem0.OriginPoint = Reference6

        :rtype: Reference
        """

        return Reference(self.axis_system.OriginPoint)

    @origin_point.setter
    def origin_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.axis_system.OriginPoint = value.com_object

    @property
    def origin_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property OriginType() As CATAxisSystemOriginType
                | 
                |     Returns or sets the way the origin point is defined.
                |     The origin point can be not specified, or be defined by coordinates or by a
                |     geometric point.
                |     CATAxisSystemOriginType is the enumeration which describes how the origin
                |     point is defined :
                |     If OriginType=0, the origin point is defined by a geometric point. If no
                |     point si selected, the origin will be automatically put at the intersection of
                |     the lines or planes defining the axes.
                |     If OriginType=1, the origin is defined by three coordinates x,y,z. Then,
                |     the origin will allways stays at the position defined by the
                |     coordinates.
                | 
                |     Example:
                |         The following example prints the origin type :
                | 
                |          Catia.SystemService.Print " OriginType = " & axisSystem.OriginType
                | 
                |         The following example sets the origin type to 1 :
                | 
                |          axisSystem.OriginType = 1

        :return: enum cat_axis_system_origin_type
        :rtype: int
        """

        return self.axis_system.OriginType

    @origin_type.setter
    def origin_type(self, value: int):
        """
        :param int value: enum cat_axis_system_origin_type
        """

        self.axis_system.OriginType = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Type() As CATAxisSystemMainType
                | 
                |     Returns or sets the type of the axis system. Sets the axis system
                |     type.
                | 
                |     Example:
                |         The following example returns in type1 the type of the axis system
                |         axisSystem1:
                | 
                |          type1 = axisSystem1.Type
                | 
                |         The following example sets the type of the axis system axisSystem1 as
                |         standard:
                | 
                |          axisSystem1.Type = 0
                | 
                |         The following example sets the type of the axis system axisSystem1 as
                |         axis rotation:
                | 
                |          axisSystem1.Type = 1
                | 
                |     The following example sets the type of the axis system axisSystem1 as datum
                |     (explicit):
                | 
                |      axisSystem1.Type = 3

        :return: enum cat_axis_system_main_type
        :rtype: int
        """

        return self.axis_system.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:  enum cat_axis_system_main_type
        """

        self.axis_system.Type = value

    @property
    def x_axis_direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property XAxisDirection() As Reference
                | 
                |     Reads or sets the geometric point, line or plane which defines the
                |     direction of the X axis.
                |     AxisDirection is and must be a reference on a 3D point or 3D line or
                |     plane.
                | 
                |     Example:
                |         The following example sets the point Point.1 of the Geometrical Set
                |         Geometrical Set.1 as the direction of the X axis of the axis system
                |         AxisSystem0:
                | 
                |      Dim HybridBody4 As AnyObject
                |      Set HybridBody4 = Body1.HybridBodies.Item  ( "Geometrical Set.1" )
                |      Dim HybridShapePointCoord5 As AnyObject
                |      Set HybridShapePointCoord5 = HybridBody4.HybridShapes.Item  ( "Point.1" )
                |      Dim Reference6 As Reference
                |      Set Reference6 = CATIA.ActiveDocument.Part.CreateReferenceFromGeometry( HybridShapePointCoord5 )
                |      AxisSystem0.XAxisDirection = Reference6

        :rtype: Reference
        """

        return Reference(self.axis_system.XAxisDirection)

    @x_axis_direction.setter
    def x_axis_direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.axis_system.XAxisDirection = value.com_object

    @property
    def x_axis_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property XAxisType() As CATAxisSystemAxisType
                | 
                |     Reads or sets the way the X axis is specified.
                |     An axis X,Y, or Z of the axis system can be defined by a geometric point,
                |     line or plane, or by coordinates.
                |     AxisType = 0 : The axis is defined by a geometric point, line or plane and with the same
                |                    direction.
                |     AxisType = 1 : The axis direction is defined by the three coordinates x,y,z, of a vector, to
                |                    which the axis will always stay parallel.
                |     AxisType = 2 : the axis is defined by a geometric point, line or plane and with the opposite
                |                    direction. Notice : If the X axis is neither defined by coordinates nor by a
                |                    point,line or plane, the axis will be automatically computed in order to build an
                |                    orthogonal axis system with the other specified axes.
                | 
                |     Example:
                |         The following example prints the X axis type :
                | 
                |          Catia.SystemService.Print " XAxisType = " & axisSystem.XAxisType
                | 
                |         The following example sets the X axis type to 1 :
                | 
                |          axisSystem.XAxisType = 1

        :return: enum cat_axis_system_axis_type
        :rtype: int
        """

        return self.axis_system.XAxisType

    @x_axis_type.setter
    def x_axis_type(self, value: int):
        """
        :param int value: enum cat_axis_system_axis_type
        """

        self.axis_system.XAxisType = value

    @property
    def y_axis_direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property YAxisDirection() As Reference
                | 
                |     Reads or sets the geometric point, line or plane which defines the
                |     direction of the Y axis.
                |     AxisDirection is and must be a reference on a 3D point or 3D line or
                |     plane.
                | 
                |     Example:
                |         The following example sets the point Point.1 of the Geometrical Set
                |         Geometrical Set.1 as the direction of the Y axis of the axis system
                |         AxisSystem0:
                | 
                |          Dim HybridBody4 As AnyObject
                |          Set HybridBody4 = Body1.HybridBodies.Item  ( "Geometrical Set.1" ) 
                |          Dim HybridShapePointCoord5 As AnyObject
                |          Set HybridShapePointCoord5 = HybridBody4.HybridShapes.Item  ( "Point.1" ) 
                |          Dim Reference6 As Reference
                |          Set Reference6 = CATIA.ActiveDocument.Part.
                |                               CreateReferenceFromGeometry(HybridShapePointCoord5 )
                |          AxisSystem0.YAxisDirection = Reference6

        :rtype: Reference
        """

        return Reference(self.axis_system.YAxisDirection)

    @y_axis_direction.setter
    def y_axis_direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.axis_system.YAxisDirection = value.com_object

    @property
    def y_axis_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property YAxisType() As CATAxisSystemAxisType
                | 
                |     Reads or sets the way the Y axis is specified.
                |     An axis X,Y, or Z of the axis system can be defined by a geometric point,
                |     line or plane, or by coordinates.
                |     AxisType = 0 : The axis is defined by a geometric point, line or plane and with the same
                |                    direction.
                |     AxisType = 1 : The axis direction is defined by the three coordinates x,y,z, of a vector, to
                |                    which the axis will always stay parallel.
                |     AxisType = 2 : the axis is defined by a geometric point, line or plane and with the opposite
                |                    direction. Notice : If the Y axis is neither defined by coordinates nor by a
                |                    point,line or plane, the axis will be automatically computed in order to build an
                |                    orthogonal axis system with the other specified axes.
                | 
                |     Example:
                |         The following example prints the Y axis type :
                | 
                |          Catia.SystemService.Print " YAxisType = " & axisSystem.YAxisType
                | 
                |         The following example sets the Y axis type to 1 :
                | 
                |          axisSystem.YAxisType = 1

        :return: enum cat_axis_system_axis_type
        :rtype: int
        """

        return self.axis_system.YAxisType

    @y_axis_type.setter
    def y_axis_type(self, value: int):
        """
        :param int value: enum cat_axis_system_axis_type
        """

        self.axis_system.YAxisType = value

    @property
    def z_axis_direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ZAxisDirection() As Reference
                | 
                |     Reads or sets the geometric point, line or plane which defines the
                |     direction of the Z axis.
                |     AxisDirection is and must be a reference on a 3D point or 3D line or
                |     plane.
                | 
                |     Example:
                |         The following example sets the point Point.1 of the Geometrical Set
                |         Geometrical Set.1 as the direction of the Z axis of the axis system
                |         AxisSystem0:
                | 
                |          Dim HybridBody4 As AnyObject
                |          Set HybridBody4 = Body1.HybridBodies.Item  ( "Geometrical Set.1" ) 
                |          Dim HybridShapePointCoord5 As AnyObject
                |          Set HybridShapePointCoord5 = HybridBody4.HybridShapes.Item  ( "Point.1" ) 
                |          Dim Reference6 As Reference
                |          Set Reference6 = CATIA.ActiveDocument.Part.
                |                               CreateReferenceFromGeometry(HybridShapePointCoord5)
                |          AxisSystem0.ZAxisDirection = Reference6

        :rtype: Reference
        """

        return Reference(self.axis_system.ZAxisDirection)

    @z_axis_direction.setter
    def z_axis_direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.axis_system.ZAxisDirection = value.com_object

    @property
    def z_axis_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ZAxisType() As CATAxisSystemAxisType
                | 
                |     Reads or sets the way the Z axis is specified.
                |     An axis X,Y, or Z of the axis system can be defined by a geometric point,
                |     line or plane, or by coordinates.
                |     AxisType = 0 : The axis is defined by a geometric point, line or plane and with the same
                |                    direction.
                |     AxisType = 1 : The axis direction is defined by the three coordinates x,y,z, of a vector, to
                |                    which the axis will always stay parallel.
                |     AxisType = 2 : the axis is defined by a geometric point, line or plane and with the opposite
                |                    direction. Notice : If the Z axis is neither defined by coordinates nor by a
                |                    point,line or plane, the axis will be automatically computed in order to build an
                |                    orthogonal axis system with the other specified axes.
                | 
                |     Example:
                |         The following example prints the Z axis type :
                | 
                |          Catia.SystemService.Print " ZAxisType = " & axisSystem.ZAxisType
                | 
                |         The following example sets the Z axis type to 1 :
                | 
                |          axisSystem.ZAxisType = 1

        :return: enum cat_axis_system_axis_type
        :rtype: int
        """

        return self.axis_system.ZAxisType

    @z_axis_type.setter
    def z_axis_type(self, value: int):
        """
        :param int value: enum cat_axis_system_axis_type
        """

        self.axis_system.ZAxisType = value

    def get_euler_angles(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetEulerAngles(Angle oFirstAngle,
                | Angle oSecondAngle,
                | Angle ThirdAngle)
                | 
                |     Returns the Euler Angles of an axis system. Succeeds only if the axis
                |     system is defined by Euler angles, wich means its type is
                |     catAxisSystemEulerAngles.

        :param Angle o_first_angle:
        :param Angle o_second_angle:
        :param Angle third_angle:
        :rtype: None
        """

        vba_function_name = 'get_euler_angles'
        vba_code = """
        Public Function get_euler_angles(axis_system)
            Dim oFirstAngle (2)
            axis_system.GetEulerAngles oFirstAngle
            get_euler_angles = oFirstAngle
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_origin(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetOrigin(CATSafeArrayVariant oOrigin)
                | 
                |     Returns the coordinates X,Y,Z of the origin point of the axis
                |     system.
                | 
                |     Parameters:
                | 
                |         oOrigin
                |             A Safe Array made up of 3 doubles: X, Y, Z, representing the
                |             coordinates in model space of the origin point of the axis system.
                |             
                | 
                |     Example:
                |         The following example retrieves in originCoord the coordinates of the
                |         origin point of the axisSystem axis system:
                | 
                |          Dim originCoord(2)
                |          axisSystem.GetOrigin originCoord

        :param tuple o_origin:
        :rtype: None
        """

        vba_function_name = 'get_origin'
        vba_code = """
        Public Function get_origin(axis_system)
            Dim oOrigin (2)
            axis_system.GetOrigin oOrigin
            get_origin = oOrigin
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_vectors(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetVectors(CATSafeArrayVariant oVectorX,
                | CATSafeArrayVariant oVectorY)
                | 
                |     Returns the coordinates X,Y,Z of the axes X and Y of the axis
                |     system.
                | 
                |     Parameters:
                | 
                |         oVectorX
                |             A Safe Array made up of 3 doubles: X, Y, Z, representing the
                |             coordinates in model space of the X axis vector of the axis system.
                |             
                |         oVectorY
                |             A Safe Array made up of 3 doubles: X, Y, Z, representing the
                |             coordinates in model space of the Y axis vector of the axis system.
                |             
                | 
                |     Example:
                |         The following example retrieves in vectorXCoord and vectorYCoord the
                |         coordinates of the vectors of the axisSystem axis
                |         system:
                | 
                |          Dim vectorXCoord(2)
                |          Dim vectorYCoord(2)
                |          axisSystem.GetVectors vectorXCoord, vectorYCoord

        :rtype: None
        """

        vba_function_name = "get_vectors"
        vba_code = """
        Public Function get_vectors(axis_system)
            Dim oVectorX (2)
            Dim oVectorY (2)
            axis_system.GetVectors oVectorX, oVectorY
            Dim oVectors (1)
            oVectors(0) = oVectorX
            oVectors(1) = oVectorY
            get_vectors = oVectors
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_x_axis(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetXAxis(CATSafeArrayVariant oXAxis)
                | 
                |     Returns the coordinates X,Y,Z of the X axis of the axis
                |     system.
                | 
                |     Parameters:
                | 
                |         oXAxis
                |             A Safe Array made up of 3 doubles: X, Y, Z, representing the
                |             coordinates in model space of the X axis of the axis system.
                |             
                | 
                |     Example:
                |         The following example retrieves in XAxisCoord the coordinates of the X
                |         axis of the axisSystem axis system:
                | 
                |          Dim XAxisCoord(2)
                |          axisSystem.GetXAxis XAxisCoord

        :param tuple o_x_axis:
        :rtype: None
        """

        vba_function_name = 'get_x_axis'
        vba_code = """
        Public Function get_x_axis(axis_system)
            Dim oXAxis (2)
            axis_system.GetXAxis oXAxis
            get_x_axis = oXAxis
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_y_axis(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetYAxis(CATSafeArrayVariant oYAxis)
                | 
                |     Returns the coordinates X,Y,Z of the Y axis of the axis
                |     system.
                | 
                |     Parameters:
                | 
                |         oYAxis
                |             A Safe Array made up of 3 doubles: X, Y, Z, representing the
                |             coordinates in model space of the Y axis of the axis system.
                |             
                | 
                |     Example:
                |         The following example retrieves in YAxisCoord the coordinates of the Y
                |         axis of the axisSystem axis system:
                | 
                |          Dim YAxisCoord(2)
                |          axisSystem.GetYAxis XAxisCoord

        :param tuple o_y_axis:
        :rtype: None
        """

        vba_function_name = 'get_y_axis'
        vba_code = """
        Public Function get_y_axis(axis_system)
            Dim oYAxis (2)
            axis_system.GetYAxis oYAxis
            get_y_axis = oYAxis
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_z_axis(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetZAxis(CATSafeArrayVariant oZAxis)
                | 
                |     Returns the coordinates X,Y,Z of the Z axis of the axis
                |     system.
                | 
                |     Parameters:
                | 
                |         oZAxis
                |             A Safe Array made up of 3 doubles: X, Y, Z, representing the
                |             coordinates in model space of the Z axis of the axis system.
                |             
                | 
                |     Example:
                |         The following example retrieves in ZAxisCoord the coordinates of the Z
                |         axis of the axisSystem axis system:
                | 
                |          Dim ZAxisCoord(2)
                |          axisSystem.GetZAxis ZAxisCoord

        :param tuple o_z_axis:
        :rtype: None
        """

        vba_function_name = 'get_z_axis'
        vba_code = """
        Public Function get_z_axis(axis_system)
            Dim oZAxis (2)
            axis_system.GetZAxis oZAxis
            get_z_axis = oZAxis
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_origin(self, i_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutOrigin(CATSafeArrayVariant iOrigin)
                | 
                |     Defines the coordinates X,Y,Z of the origin point of the axis
                |     system.
                | 
                |     Parameters:
                | 
                |         iOrigin
                |             A Safe Array made up of 3 doubles: X, Y, Z, representing the
                |             coordinates in model space of the origin point of the axis system.
                |             
                | 
                |     Example:
                |         The following example puts in originCoord the new coordinates of the
                |         origin point of the axisSystem axis system:
                | 
                |          Dim originCoord(2)
                |          originCoord ( 0 )  = 100.000000
                |          originCoord ( 1 )  = 200.000000
                |          originCoord ( 2 )  = 10.000000
                |          axisSystem.PutOrigin originCoord

        :param tuple i_origin:
        :rtype: None
        """
        return self.axis_system.PutOrigin(i_origin)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_origin'
        # # vba_code = """
        # # Public Function put_origin(axis_system)
        # #     Dim iOrigin (2)
        # #     axis_system.PutOrigin iOrigin
        # #     put_origin = iOrigin
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_vectors(self, i_vector_x: tuple, i_vector_y: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutVectors(CATSafeArrayVariant iVectorX,
                | CATSafeArrayVariant iVectorY)
                | 
                |     Defines the coordinates X,Y,Z of the axes X and Y of the axis
                |     system.
                | 
                |     Parameters:
                | 
                |         iVectorX
                |             A Safe Array made up of 3 doubles: X, Y, Z, representing the
                |             coordinates in model space of the X axis vector of the axis system.
                |             
                |         iVectorY
                |             A Safe Array made up of 3 doubles: X, Y, Z, representing the
                |             coordinates in model space of the Y axis vector of the axis system.
                |             
                | 
                |     Example:
                |         The following example modifies in vectorXCoord and vectorYCoord the
                |         coordinates of the vectors of the axisSystem axis
                |         system:
                | 
                |          Dim vectorXCoord(2)
                |          vectorYCoord ( 0 )  = 1.000000
                |          vectorYCoord ( 1 )  = -1.000000
                |          vectorYCoord ( 2 )  = 0.000000
                |          Dim vectorYCoord(2)
                |          vectorYCoord ( 0 )  = 0.000000
                |          vectorYCoord ( 1 )  = 0.000000
                |          vectorYCoord ( 2 )  = 1.000000
                |          axisSystem.PutVectors vectorXCoord, vectorYCoord

        :param tuple i_vector_x:
        :param tuple i_vector_y:
        :rtype: None
        """
        return self.axis_system.PutVectors(i_vector_x, i_vector_y)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_vectors'
        # # vba_code = """
        # # Public Function put_vectors(axis_system)
        # #     Dim iVectorX (2)
        # #     axis_system.PutVectors iVectorX
        # #     put_vectors = iVectorX
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_x_axis(self, i_x_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutXAxis(CATSafeArrayVariant iXAxis)
                | 
                |     Defines the coordinates X,Y,Z of the X axis of the axis
                |     system.
                | 
                |     Parameters:
                | 
                |         iXAxis
                |             A Safe Array made up of 3 doubles: X, Y, Z, representing the
                |             coordinates in model space of the X axis of the axis system.
                |             
                | 
                |     Example:
                |         The following example puts in XAxisCoord the new coordinates of the X
                |         axis of the axisSystem axis system:
                | 
                |          Dim XAxis(2)
                |          XAxis ( 0 )  = 100.000000
                |          XAxis ( 1 )  = 200.000000
                |          XAxis ( 2 )  = 10.000000
                |          axisSystem.PutXAxis XAxis

        :param tuple i_x_axis:
        :rtype: None
        """
        return self.axis_system.PutXAxis(i_x_axis)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_x_axis'
        # # vba_code = """
        # # Public Function put_x_axis(axis_system)
        # #     Dim iXAxis (2)
        # #     axis_system.PutXAxis iXAxis
        # #     put_x_axis = iXAxis
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_y_axis(self, i_y_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutYAxis(CATSafeArrayVariant iYAxis)
                | 
                |     Defines the coordinates X,Y,Z of the Y axis of the axis
                |     system.
                | 
                |     Parameters:
                | 
                |         iYAxis
                |             A Safe Array made up of 3 doubles: X, Y, Z, representing the
                |             coordinates in model space of the Y axis of the axis system.
                |             
                | 
                |     Example:
                |         The following example puts in XAxisCoord the new coordinates of the Y
                |         axis of the axisSystem axis system:
                | 
                |          Dim YAxis(2)
                |          YAxis ( 0 )  = 100.000000
                |          YAxis ( 1 )  = 200.000000
                |          YAxis ( 2 )  = 10.000000
                |          axisSystem.PutYAxis YAxis

        :param tuple i_y_axis:
        :rtype: None
        """
        return self.axis_system.PutYAxis(i_y_axis)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_y_axis'
        # # vba_code = """
        # # Public Function put_y_axis(axis_system)
        # #     Dim iYAxis (2)
        # #     axis_system.PutYAxis iYAxis
        # #     put_y_axis = iYAxis
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_z_axis(self, i_z_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutZAxis(CATSafeArrayVariant iZAxis)
                | 
                |     Defines the coordinates X,Y,Z of the Z axis of the axis
                |     system.
                | 
                |     Parameters:
                | 
                |         iZAxis
                |             A Safe Array made up of 3 doubles: X, Y, Z, representing the
                |             coordinates in model space of the Z axis of the axis system.
                |             
                | 
                |     Example:
                |         The following example puts in ZAxisCoord the new coordinates of the Z
                |         axis of the axisSystem axis system:
                | 
                |          Dim ZAxis(2)
                |          ZAxis ( 0 )  = 100.000000
                |          ZAxis ( 1 )  = 200.000000
                |          ZAxis ( 2 )  = 10.000000
                |          axisSystem.PutZAxis ZAxis

        :param tuple i_z_axis:
        :rtype: None
        """
        return self.axis_system.PutZAxis(i_z_axis)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_z_axis'
        # # vba_code = """
        # # Public Function put_z_axis(axis_system)
        # #     Dim iZAxis (2)
        # #     axis_system.PutZAxis iZAxis
        # #     put_z_axis = iZAxis
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AxisSystem(name="{self.name}")'
