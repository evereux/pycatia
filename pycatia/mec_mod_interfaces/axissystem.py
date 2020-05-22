#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.base_object import AnyObject
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.in_interfaces.reference import Reference
from pycatia.enumeration.enumeration_types import cat_axis_system_axis_type


class AxisSystem(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | The object Axis System  A axis system has got one origin point and
                | three orthogonal axes,  crossing at the origin point.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.axis_system = com_object

    @property
    def axis_rotation_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AxisRotationAngle
                | o Property AxisRotationAngle(    ) As Angle
                | 
                | Returns the rotation angle of an axis system. Succeeds only if the
                | axis system is defined by a rotation around an axis, which means that
                | its type is catAxisSystemAxisRotation.

        """
        return Angle(self.axis_system.AxisRotationAngle)

    @property
    def axis_rotation_reference(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AxisRotationReference
                | o Property AxisRotationReference(    ) As Reference
                | 
                | Returns the reference for the axis rotation. Succeeds only if the axis
                | system is defined by a rotation around an axis, which means that its
                | type is catAxisSystemAxisRotation.

        """
        return Reference(self.axis_system.AxisRotationReference)

    @property
    def is_current(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsCurrent
                | o Property IsCurrent(    ) As boolean
                | 
                | Returns True if the axis system is the current one, else returns
                | False.  Sets the axis system as the current one or not.  Example:The
                | following example returns in isCurrent True if the axis system
                | axisSystem is the current one :   isCurrent = axisSystem.IsCurrentThe
                | following example sets the axis system axisSystem as the current one :
                | axisSystem.IsCurrent = 1The following example sets the axis system
                | axisSystem as not the current one :   axisSystem.IsCurrent = 0

        """
        return self.axis_system.IsCurrent

    @property
    def origin_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OriginPoint
                | o Property OriginPoint(    ) As Reference
                | 
                | Returns or sets the geometric point which defines the origin of the
                | axis system.   OriginPoint is and must be a reference on a geometric
                | 3D point.  Example:The following example sets the point Point.1 of the
                | Geometrical Set  Geometrical Set.1 as the origin point of the axis
                | system AxisSystem0:   Dim HybridBody4 As AnyObject Set HybridBody4 =
                | Body1.HybridBodies.Item  ( "Geometrical Set.1" )  Dim
                | HybridShapePointCoord5 As AnyObject Set HybridShapePointCoord5 =
                | HybridBody4.HybridShapes.Item  ( "Point.1" )  Dim Reference6 As
                | Reference Set Reference6 =
                | CATIA.ActiveDocument.Part.CreateReferenceFromGeometry  (
                | HybridShapePointCoord5 )  AxisSystem0.OriginPoint = Reference6

        """
        return Reference(self.axis_system.OriginPoint)

    @property
    def origin_type(self):
        """

        .. note::
            CAA V5 Visual Basic help

                | OriginType
                | o Property OriginType(    ) As CATAxisSystemOriginType
                | 
                | Returns or sets the way the origin point is defined.  The origin point
                | can be not specified, or be defined by coordinates or by a geometric
                | point. CATAxisSystemOriginType is the enumeration which describes how
                | the origin point is defined : If OriginType=0, the origin point is
                | defined by a geometric point. If no point si selected, the origin will
                | be automatically put at the intersection of the lines or planes
                | defining the axes.  If OriginType=1, the origin is defined by three
                | coordinates x,y,z. Then, the origin will always stays at the position
                | defined by the coordinates.  Example:The following example prints the
                | origin type :  Catia.SystemService.Print " OriginType = " &
                | axisSystem.OriginTypeThe following example sets the origin type to 1 :
                | axisSystem.OriginType = 1

            :return int:
        """
        return self.axis_system.OriginType

    @origin_type.setter
    def origin_type(self, value):
        types = [x for x in cat_axis_system_axis_type]
        if not isinstance(value, int) or value not in types:
            raise ValueError(
                f'Value "value" must be an int and in the range "{types}".'
            )

    @property
    def type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Type
                | o Property Type(    ) As CATAxisSystemMainType
                | 
                | Returns or sets the type of the axis system.  Sets the axis system
                | type.  Example:The following example returns in type1 the type of the
                | axis system axisSystem1:   type1 = axisSystem1.TypeThe following
                | example sets the type of the axis system axisSystem1 as standard:
                | axisSystem1.Type = 0The following example sets the type of the axis
                | system axisSystem1 as axis rotation:   axisSystem1.Type = 1The
                | following example sets the type of the axis system axisSystem1 as
                | datum (explicit):   axisSystem1.Type = 3

        """
        return self.axis_system.Type

    @type.setter
    def type(self, value):
        types = [x for x in cat_axis_system_axis_type]
        if not isinstance(value, int) or value not in types:
            raise ValueError(
                f'Value "value" must be an int and in the range "{types}".'
            )

    @property
    def x_axis_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | XAxisDirection
                | o Property XAxisDirection(    ) As Reference
                | 
                | Reads or sets the geometric point, line or plane which defines the
                | direction of the X axis. AxisDirection is and must be a reference on a
                | 3D point or 3D line or plane.  Example:The following example sets the
                | point Point.1 of the Geometrical Set  Geometrical Set.1 as the
                | direction of the X axis of the axis system AxisSystem0:  Dim
                | HybridBody4 As AnyObject Set HybridBody4 = Body1.HybridBodies.Item  (
                | "Geometrical Set.1" )  Dim HybridShapePointCoord5 As AnyObject Set
                | HybridShapePointCoord5 = HybridBody4.HybridShapes.Item  ( "Point.1" )
                | Dim Reference6 As Reference Set Reference6 =
                | CATIA.ActiveDocument.Part.CreateReferenceFromGeometry  (
                | HybridShapePointCoord5 )  AxisSystem0.XAxisDirection = Reference6

        :return: int
        """
        return self.axis_system.XAxisDirection

    @x_axis_direction.setter
    def x_axis_direction(self, value):
        types = [x for x in cat_axis_system_axis_type]
        if not isinstance(value, int) or value not in types:
            raise ValueError(
                f'Value "value" must be an int and in the range "{types}".'
            )

    @property
    def x_axis_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | XAxisType
                | o Property XAxisType(    ) As CATAxisSystemAxisType
                | 
                | Reads or sets the way the X axis is specified.  An axis X,Y, or Z of
                | the axis system can be defined  by a geometric point, line or plane,
                | or by coordinates.  AxisType = 0 : The axis is defined by a geometric
                | point, line or plane and with the same direction.         AxisType = 1
                | : The axis direction is defined by the three coordinates x,y,z, of a
                | vector, to which the axis will always stay parallel.    AxisType = 2
                | : the axis is defined by a geometric point, line or plane and with the
                | opposite direction. Notice : If the X axis is neither defined by
                | coordinates nor by a point,line or plane, the axis will be
                | automatically computed in order to build an orthogonal  axis system
                | with the other specified axes.  Example:The following example prints
                | the X axis type :  Catia.SystemService.Print " XAxisType = " &
                | axisSystem.XAxisTypeThe following example sets the X axis type to 1 :
                | axisSystem.XAxisType = 1

        :return: Reference()
        """
        return Reference(self.axis_system.XAxisType)

    @property
    def y_axis_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | YAxisDirection
                | o Property YAxisDirection(    ) As Reference
                | 
                | Reads or sets the geometric point, line or plane which defines the
                | direction of the Y axis. AxisDirection is and must be a reference on a
                | 3D point or 3D line or plane.  Example:The following example sets the
                | point Point.1 of the Geometrical Set Geometrical Set.1 as the
                | direction of the Y axis of the axis system AxisSystem0:  Dim
                | HybridBody4 As AnyObject Set HybridBody4 = Body1.HybridBodies.Item  (
                | "Geometrical Set.1" )  Dim HybridShapePointCoord5 As AnyObject Set
                | HybridShapePointCoord5 = HybridBody4.HybridShapes.Item  ( "Point.1" )
                | Dim Reference6 As Reference Set Reference6 =
                | CATIA.ActiveDocument.Part.CreateReferenceFromGeometry  (
                | HybridShapePointCoord5 )  AxisSystem0.YAxisDirection = Reference6

        :return: int
        """
        return self.axis_system.YAxisDirection

    @y_axis_direction.setter
    def y_axis_direction(self, value):
        types = [x for x in cat_axis_system_axis_type]
        if not isinstance(value, int) or value not in types:
            raise ValueError(
                f'Value "value" must be an int and in the range "{types}".'
            )

    @property
    def y_axis_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | YAxisType
                | o Property YAxisType(    ) As CATAxisSystemAxisType
                | 
                | Reads or sets the way the Y axis is specified.  An axis X,Y, or Z of
                | the axis system can be defined  by a geometric point, line or plane,
                | or by coordinates.  AxisType = 0 : The axis is defined by a geometric
                | point, line or plane and with the same direction.         AxisType = 1
                | : The axis direction is defined by the three coordinates x,y,z, of a
                | vector, to which the axis will always stay parallel.    AxisType = 2
                | : the axis is defined by a geometric point, line or plane and with the
                | opposite direction. Notice : If the Y axis is neither defined by
                | coordinates nor by a point,line or plane, the axis will be
                | automatically computed in order to build an orthogonal  axis system
                | with the other specified axes.  Example:The following example prints
                | the Y axis type :  Catia.SystemService.Print " YAxisType = " &
                | axisSystem.YAxisTypeThe following example sets the Y axis type to 1 :
                | axisSystem.YAxisType = 1

        :return: Reference()
        """
        return Reference(self.axis_system.YAxisType)

    @property
    def z_axis_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ZAxisDirection
                | o Property ZAxisDirection(    ) As Reference
                | 
                | Reads or sets the geometric point, line or plane which defines the
                | direction of the Z axis. AxisDirection is and must be a reference on a
                | 3D point or 3D line or plane.  Example:The following example sets the
                | point Point.1 of the Geometrical Set Geometrical Set.1 as the
                | direction of the Z axis of the axis system AxisSystem0:  Dim
                | HybridBody4 As AnyObject Set HybridBody4 = Body1.HybridBodies.Item  (
                | "Geometrical Set.1" )  Dim HybridShapePointCoord5 As AnyObject Set
                | HybridShapePointCoord5 = HybridBody4.HybridShapes.Item  ( "Point.1" )
                | Dim Reference6 As Reference Set Reference6 =
                | CATIA.ActiveDocument.Part.CreateReferenceFromGeometry  (
                | HybridShapePointCoord5 )  AxisSystem0.ZAxisDirection = Reference6

        :return: int
        """
        return self.axis_system.ZAxisDirection

    @y_axis_direction.setter
    def y_axis_direction(self, value):
        types = [x for x in cat_axis_system_axis_type]
        if not isinstance(value, int) or value not in types:
            raise ValueError(
                f'Value "value" must be an int and in the range "{types}".'
            )

    @property
    def z_axis_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ZAxisType
                | o Property ZAxisType(    ) As CATAxisSystemAxisType
                | 
                | Reads or sets the way the Z axis is specified.  An axis X,Y, or Z of
                | the axis system can be defined  by a geometric point, line or plane,
                | or by coordinates.  AxisType = 0 : The axis is defined by a geometric
                | point, line or plane and with the same direction.         AxisType = 1
                | : The axis direction is defined by the three coordinates x,y,z, of a
                | vector, to which the axis will always stay parallel.    AxisType = 2
                | : the axis is defined by a geometric point, line or plane and with the
                | opposite direction. Notice : If the Z axis is neither defined by
                | coordinates nor by a point,line or plane, the axis will be
                | automatically computed in order to build an orthogonal  axis system
                | with the other specified axes.  Example:The following example prints
                | the Z axis type :  Catia.SystemService.Print " ZAxisType = " &
                | axisSystem.ZAxisTypeThe following example sets the Z axis type to 1 :
                | axisSystem.ZAxisType = 1

        :return: Reference()
        """
        return Reference(self.axis_system.ZAxisType)

    def get_euler_angles(self, o_first_angle, o_second_angle, third_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetEulerAngles
                | o Sub GetEulerAngles(    Angle    oFirstAngle,
                |                          Angle    oSecondAngle,
                |                          Angle    ThirdAngle)
                | 
                | Returns the Euler Angles of an axis system. Succeeds only if the axis
                | system is defined by Euler angles, which means its type is
                | catAxisSystemEulerAngles.

        """
        return self.axis_system.GetEulerAngles(
            o_first_angle, o_second_angle, third_angle
        )

    def get_origin(self, o_origin):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOrigin
                | o Sub GetOrigin(    CATSafeArrayVariant    oOrigin)
                | 
                | Returns the coordinates X,Y,Z of the origin point of the axis system.
                |
                | Parameters:
                | oOrigin
                |    A Safe Array made up of 3 doubles: X, Y, Z, representing the 
                |    coordinates in model space of the origin point of the axis system.
                |
                | Examples:
                | 
                | The following example retrieves in originCoord the coordinates
                | of the origin point of the axisSystem axis system:
                | 
                | Dim originCoord(2)
                | axisSystem.GetOrigin originCoord

        """
        return self.axis_system.GetOrigin(o_origin)

    def get_vectors(self, o_vector_x, o_vector_y):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetVectors
                | o Sub GetVectors(    CATSafeArrayVariant    oVectorX,
                |                      CATSafeArrayVariant    oVectorY)
                | 
                | Returns the coordinates X,Y,Z of the axes X and Y of the axis system.
                |
                | Parameters:
                | oVectorX
                |    A Safe Array made up of 3 doubles: X, Y, Z, representing the 
                |    coordinates in model space of the X axis vector of the axis system.
                |  
                |  oVectorY
                |    A Safe Array made up of 3 doubles: X, Y, Z, representing the 
                |    coordinates in model space of the Y axis vector of the axis system.
                |
                | Examples:
                | 
                | The following example retrieves in vectorXCoord and vectorYCoord
                | the coordinates of the vectors of the axisSystem axis system:
                | 
                | Dim vectorXCoord(2)
                | Dim vectorYCoord(2)
                | axisSystem.GetVectors vectorXCoord, vectorYCoord


        """
        return self.axis_system.GetVectors(o_vector_x, o_vector_y)

    def get_x_axis(self, o_x_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetXAxis
                | o Sub GetXAxis(    CATSafeArrayVariant    oXAxis)
                | 
                | Returns the coordinates X,Y,Z of the X axis of the axis system.
                |
                | Parameters:
                | oXAxis
                |    A Safe Array made up of 3 doubles: X, Y, Z, representing the 
                |    coordinates in model space of the X axis of the axis system.
                |
                | Examples:
                | 
                | The following example retrieves in XAxisCoord the coordinates
                | of the X axis of the axisSystem axis system:
                | 
                | Dim XAxisCoord(2)
                | axisSystem.GetXAxis XAxisCoord


        """
        return self.axis_system.GetXAxis(o_x_axis)

    def get_y_axis(self, o_y_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetYAxis
                | o Sub GetYAxis(    CATSafeArrayVariant    oYAxis)
                | 
                | Returns the coordinates X,Y,Z of the Y axis of the axis system.
                |
                | Parameters:
                | oYAxis
                |    A Safe Array made up of 3 doubles: X, Y, Z, representing the 
                |    coordinates in model space of the Y axis of the axis system.
                |
                | Examples:
                | 
                | The following example retrieves in YAxisCoord the coordinates
                | of the Y axis of the axisSystem axis system:
                | 
                | Dim YAxisCoord(2)
                | axisSystem.GetYAxis XAxisCoord


        """
        return self.axis_system.GetYAxis(o_y_axis)

    def get_z_axis(self, o_z_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetZAxis
                | o Sub GetZAxis(    CATSafeArrayVariant    oZAxis)
                | 
                | Returns the coordinates X,Y,Z of the Z axis of the axis system.
                |
                | Parameters:
                | oZAxis
                |    A Safe Array made up of 3 doubles: X, Y, Z, representing the 
                |    coordinates in model space of the Z axis of the axis system.
                |
                | Examples:
                | 
                | The following example retrieves in ZAxisCoord the coordinates
                | of the Z axis of the axisSystem axis system:
                | 
                | Dim ZAxisCoord(2)
                | axisSystem.GetZAxis ZAxisCoord


        """
        return self.axis_system.GetZAxis(o_z_axis)

    def put_origin(self, i_origin):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutOrigin
                | o Sub PutOrigin(    CATSafeArrayVariant    iOrigin)
                | 
                | Defines the coordinates X,Y,Z of the origin point of the axis system.
                |
                | Parameters:
                | iOrigin
                |    A Safe Array made up of 3 doubles: X, Y, Z, representing the 
                |    coordinates in model space of the origin point of the axis system.
                |
                | Examples:
                | 
                | The following example puts in originCoord the new coordinates of
                | the origin point of the axisSystem axis system:
                | 
                | Dim originCoord(2)
                | originCoord ( 0 )  = 100.000000
                | originCoord ( 1 )  = 200.000000
                | originCoord ( 2 )  = 10.000000
                | axisSystem.PutOrigin originCoord


        """
        return self.axis_system.PutOrigin(i_origin)

    def put_vectors(self, i_vector_x, i_vector_y):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutVectors
                | o Sub PutVectors(    CATSafeArrayVariant    iVectorX,
                |                      CATSafeArrayVariant    iVectorY)
                | 
                | Defines the coordinates X,Y,Z of the axes X and Y of the axis system.
                |
                | Parameters:
                | iVectorX
                |    A Safe Array made up of 3 doubles: X, Y, Z, representing the 
                |    coordinates in model space of the X axis vector of the axis system.
                |  iVectorY
                |    A Safe Array made up of 3 doubles: X, Y, Z, representing the 
                |    coordinates in model space of the Y axis vector of the axis system.
                |
                | Examples:
                | 
                | The following example modifies in vectorXCoord and vectorYCoord
                | the coordinates of the vectors of the axisSystem axis system:
                | 
                | Dim vectorXCoord(2)
                | vectorYCoord ( 0 )  = 1.000000
                | vectorYCoord ( 1 )  = -1.000000
                | vectorYCoord ( 2 )  = 0.000000
                | Dim vectorYCoord(2)
                | vectorYCoord ( 0 )  = 0.000000
                | vectorYCoord ( 1 )  = 0.000000
                | vectorYCoord ( 2 )  = 1.000000
                | axisSystem.PutVectors vectorXCoord, vectorYCoord


        """
        return self.axis_system.PutVectors(i_vector_x, i_vector_y)

    def put_x_axis(self, i_x_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutXAxis
                | o Sub PutXAxis(    CATSafeArrayVariant    iXAxis)
                | 
                | Defines the coordinates X,Y,Z of the X axis of the axis system.
                |
                | Parameters:
                | iXAxis
                |    A Safe Array made up of 3 doubles: X, Y, Z, representing the 
                |    coordinates in model space of the X axis of the axis system.
                |
                | Examples:
                | 
                | The following example puts in XAxisCoord the new coordinates of
                | the X axis of the axisSystem axis system:
                | 
                | Dim XAxis(2)
                | XAxis ( 0 )  = 100.000000
                | XAxis ( 1 )  = 200.000000
                | XAxis ( 2 )  = 10.000000
                | axisSystem.PutXAxis XAxis


        """
        return self.axis_system.PutXAxis(i_x_axis)

    def put_y_axis(self, i_y_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutYAxis
                | o Sub PutYAxis(    CATSafeArrayVariant    iYAxis)
                | 
                | Defines the coordinates X,Y,Z of the Y axis of the axis system.
                |
                | Parameters:
                | iYAxis
                |    A Safe Array made up of 3 doubles: X, Y, Z, representing the 
                |    coordinates in model space of the Y axis of the axis system.
                |
                | Examples:
                | 
                | The following example puts in XAxisCoord the new coordinates of
                | the Y axis of the axisSystem axis system:
                | 
                | Dim YAxis(2)
                | YAxis ( 0 )  = 100.000000
                | YAxis ( 1 )  = 200.000000
                | YAxis ( 2 )  = 10.000000
                | axisSystem.PutYAxis YAxis


        """
        return self.axis_system.PutYAxis(i_y_axis)

    def put_z_axis(self, i_z_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutZAxis
                | o Sub PutZAxis(    CATSafeArrayVariant    iZAxis)
                | 
                | Defines the coordinates X,Y,Z of the Z axis of the axis system.
                |
                | Parameters:
                | iZAxis
                |    A Safe Array made up of 3 doubles: X, Y, Z, representing the 
                |    coordinates in model space of the Z axis of the axis system.
                |
                | Examples:
                | 
                | The following example puts in ZAxisCoord the new coordinates of
                | the Z axis of the axisSystem axis system:
                | 
                | Dim ZAxis(2)
                | ZAxis ( 0 )  = 100.000000
                | ZAxis ( 1 )  = 200.000000
                | ZAxis ( 2 )  = 10.000000
                | axisSystem.PutZAxis ZAxis


        """
        return self.axis_system.PutZAxis(i_z_axis)

    def __repr__(self):
        return f"AxisSystem()"
