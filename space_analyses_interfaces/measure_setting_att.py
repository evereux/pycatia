#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class MeasureSettingAtt(AnyObject):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Measurable
                | 
                | The interface to access a CATIAMeasurable Get measurements on the
                | object.
                | 
                | Two types of measurement can be done:
                | 
                |     itself : gives dimensions related to the object itself (ex the radius of a circle).
                |     between : gives dimensions related to another object (ex the distance between two products).
                |               A restriction occurs for distance between: bodies (CATBody) cannot be measured.
                | 
                | Methods on VOLUME : GetVolume GetArea GetCOG
                | Methods on SURFACE : GetArea GetCOG GetPerimeter
                | Methods on PLANE : GetArea GetCOG GetPlane
                | Methods on CYLINDER : GetArea GetCOG GetAxis GetPointsOnAxis GetRadius
                | Methods on CONE : GetArea GetCOG GetAxis GetPointsOnAxis GetAngle
                | Methods on SPHERE : GetArea GetCOG GetRadius GetCenter
                | Methods on CURVE : GetLength GetCOG GetPointsOnCurve
                | Methods on LINE : GetLength GetCOG GetPointsOnCurve GetDirection
                | Methods on CIRCLE : GetLength GetCOG GetPointsOnCurve GetRadius GetCenter GetAngle GetAxis
                | Methods on POINT : GetPoint Methods on AXIS SYST : GetAxisSystem
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.measure_setting_att = com_object

    @property
    def angle(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Angle() As double (Read Only)
                | 
                |     Returns the Angle of a circle or cone.
                | 
                |     Example:
                | 
                |              This example retrieves the Angle of NewMeasurable
                |              measure.
                |             
                | 
                |             Dim AAngle As double
                |             AAngle = NewMeasurable.Angle

        :return: float
        """

        return self.measure_setting_att.Angle

    @property
    def area(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Area() As double (Read Only)
                | 
                |     Returns the area of the surface or wet area from volume.
                | 
                |     Example:
                | 
                |              This example retrieves the area of NewMeasurable
                |              measure.
                |             The area unit given by oArea is m²
                |             
                | 
                |             Dim AArea As double
                |             AArea = NewMeasurable.Area

        :return: float
        """

        return self.measure_setting_att.Area

    @property
    def geometry_name(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GeometryName() As CatMeasurableName (Read Only)
                | 
                |     Returns the name of the geometry of the measured object.
                | 
                |     Example:
                | 
                |              This example retrieves the name of the geometry of the
                |              NewMeasurable measure.
                |             
                | 
                |             Dim AGeometryName As CatMeasurableName
                |             AGeometryName = NewMeasurable.GeometryName

        :return: enum cat_measurable_name
        """

        return self.measure_setting_att.GeometryName

    @property
    def length(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Length() As double (Read Only)
                | 
                |     Returns the Length of a curve.
                | 
                |     Example:
                | 
                |              This example retrieves the Length of NewMeasurable
                |              measure.
                |             
                | 
                |             Dim ALength As double
                |             ALength = NewMeasurable.Length

        :return: float
        """

        return self.measure_setting_att.Length

    @property
    def perimeter(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Perimeter() As double (Read Only)
                | 
                |     Returns the perimeter of a surface.
                | 
                |     Example:
                | 
                |              This example retrieves the perimeter of NewMeasurable
                |              measure.
                |             
                | 
                |             Dim APerimeter As double
                |             APerimeter = NewMeasurable.Perimeter

        :return: float
        """

        return self.measure_setting_att.Perimeter

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Radius() As double (Read Only)
                | 
                |     Returns the radius of an arc, cylinder or sphere.
                | 
                |     Example:
                | 
                |              This example retrieves the Radius of NewMeasurable
                |              measure.
                |             
                | 
                |             Dim ARadius As double
                |             ARadius = NewMeasurable.Radius

        :return: float
        """

        return self.measure_setting_att.Radius

    @property
    def volume(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Volume() As double (Read Only)
                | 
                |     Returns the volume.
                | 
                |     Example:
                | 
                |              This example retrieves the volume of NewMeasurable
                |              measure.
                |             The volume unit given by oVolume is m^3
                |             
                | 
                |             Dim AVolume As double
                |             AVolume = NewMeasurable.Volume

        :return: float
        """

        return self.measure_setting_att.Volume

    def get_angle_between(self, i_measured_item=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetAngleBetween(Reference iMeasuredItem) As double
                | 
                |     Compute the angle between the CATIAMeasurable and another.
                | 
                |     Example:
                | 
                |              This example retrieves the angle between the reference1 and
                |              reference2.
                |             Dim reference1 As Reference
                |             Set reference1 = part1.CreateReferenceFromObject(object1)
                |             Dim reference2 As Reference
                |             Set reference2 = part1.CreateReferenceFromObject(object1)
                |             Dim TheSPAWorkbench As Workbench
                |             Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
                |             Dim TheMeasurable As Measurable
                |             Set TheMeasurable = TheSPAWorkbench.GetMeasurable(reference1)
                |             Dim MinimumDistance As double
                |             MinimumDistance = TheMeasurable.GetAngleBetween(reference2)

        :param Reference i_measured_item:
        :return: float
        """
        return self.measure_setting_att.GetAngleBetween(i_measured_item.com_object)

    def get_axis(self, o_axis_vector=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetAxis(CATSafeArrayVariant oAxisVector)
                | 
                |     Retrieves the axis vector of the cylinder or a cone.
                | 
                |     Parameters:
                | 
                |         oVector
                |             The axis vector of the cylinder or a cone with respect to the
                |             product coordinate system:
                | 
                |                 oAxisVector(0) is the X direction
                |                 oAxisVector(1) is the Y direction
                |                 oAxisVector(2) is the Z direction 
                | 
                |     Example:
                | 
                |              This example retrieves the axis vector of the cylinder or a cone
                |              of NewMeasurable measure.
                |             
                | 
                |             Dim AxisVector (2)
                |             NewMeasurable.GetAxis AxisVector

        :param tuple o_axis_vector:
        :return: None
        """
        return self.measure_setting_att.GetAxis(o_axis_vector)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_axis'
        # # vba_code = """
        # # Public Function get_axis(measure_setting_att)
        # #     Dim oAxisVector (2)
        # #     measure_setting_att.GetAxis oAxisVector
        # #     get_axis = oAxisVector
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_axis_system(self, o_components=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetAxisSystem(CATSafeArrayVariant oComponents)
                | 
                |     Retrieves the information of the axis system.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The information of the axis system with respect to the product
                |             coordinate system:
                | 
                |                 oComponents(0) is the X coordinate of the origin of the axis
                |                 system
                |                 oComponents(1) is the Y coordinate of the origin of the axis
                |                 system
                |                 oComponents(2) is the Z coordinate of the origin of the axis
                |                 system
                |                 oComponents(3) is the X coordinate of the first direction of
                |                 the axis system
                |                 oComponents(4) is the Y coordinate of the first direction of
                |                 the axis system
                |                 oComponents(5) is the Z coordinate of the first direction of
                |                 the axis system
                |                 oComponents(6) is the X coordinate of the second direction of
                |                 the axis system
                |                 oComponents(7) is the Y coordinate of the second direction of
                |                 the axis system
                |                 oComponents(8) is the Z coordinate of the second direction of
                |                 the axis system
                |                 oComponents(9) is the X coordinate of the third direction of
                |                 the axis system
                |                 oComponents(10) is the Y coordinate of the third direction of
                |                 the axis system
                |                 oComponents(11) is the Z coordinate of the third direction of
                |                 the axis system 
                | 
                |     Example:
                | 
                |              This example retrieves information of the axis system of
                |              NewMeasurable measure.
                |             
                | 
                |             Dim Components (11)
                |             NewMeasurable.GetAxisSystem Components

        :param tuple o_components:
        :return: None
        """
        return self.measure_setting_att.GetAxisSystem(o_components)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_axis_system'
        # # vba_code = """
        # # Public Function get_axis_system(measure_setting_att)
        # #     Dim oComponents (2)
        # #     measure_setting_att.GetAxisSystem oComponents
        # #     get_axis_system = oComponents
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_cog(self, o_coordinates=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetCOG(CATSafeArrayVariant oCoordinates)
                | 
                |     Retrieves the position of the center of gravity of a surface and volume
                |     .
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The position of the center of gravity with respect to the product
                |             coordinate system:
                | 
                |                 oCoordinates(0) is the X coordinate
                |                 oCoordinates(1) is the Y coordinate
                |                 oCoordinates(2) is the Z coordinate 
                | 
                |     Example:
                | 
                |              This example retrieves the position of the center of gravity of
                |              NewMeasurable measure.
                |             
                | 
                |             Dim Coordinates (2)
                |             NewMeasurable.GetCOG Coordinates

        :param tuple o_coordinates:
        :return: None
        """
        return self.measure_setting_att.GetCOG(o_coordinates)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_cog'
        # # vba_code = """
        # # Public Function get_cog(measure_setting_att)
        # #     Dim oCoordinates (2)
        # #     measure_setting_att.GetCOG oCoordinates
        # #     get_cog = oCoordinates
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_center(self, o_coordinates=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetCenter(CATSafeArrayVariant oCoordinates)
                | 
                |     Retrieves the position of the center of a circle or
                |     sphere.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The position of the center with respect to the product coordinate
                |             system:
                | 
                |                 oCoordinates(0) is the X coordinate
                |                 oCoordinates(1) is the Y coordinate
                |                 oCoordinates(2) is the Z coordinate 
                | 
                |     Example:
                | 
                |              This example retrieves the position of the center of NewMeasurable
                |              measure.
                |             
                | 
                |             Dim Coordinates (2)
                |             NewMeasurable.GetCOGPosition Coordinates

        :param tuple o_coordinates:
        :return: None
        """
        return self.measure_setting_att.GetCenter(o_coordinates)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_center'
        # # vba_code = """
        # # Public Function get_center(measure_setting_att)
        # #     Dim oCoordinates (2)
        # #     measure_setting_att.GetCenter oCoordinates
        # #     get_center = oCoordinates
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_direction(self, o_direction=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetDirection(CATSafeArrayVariant oDirection)
                | 
                |     Retrieves the direction of the line.
                | 
                |     Parameters:
                | 
                |         oDirection
                |             The direction of the line with respect to the product coordinate
                |             system:
                | 
                |                 oDirection(0) is the X direction
                |                 oDirection(1) is the Y direction
                |                 oDirection(2) is the Z direction 
                | 
                |     Example:
                | 
                |              This example retrieves the direction of the line of NewMeasurable
                |              measure.
                |             
                | 
                |             Dim Direction (2)
                |             NewMeasurable.GetDirection Direction

        :param tuple o_direction:
        :return: None
        """
        return self.measure_setting_att.GetDirection(o_direction)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_direction'
        # # vba_code = """
        # # Public Function get_direction(measure_setting_att)
        # #     Dim oDirection (2)
        # #     measure_setting_att.GetDirection oDirection
        # #     get_direction = oDirection
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_minimum_distance(self, i_measured_item=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetMinimumDistance(Reference iMeasuredItem) As double
                | 
                |     Compute the minimum distance between the CATIAMeasurable and another.
                |     Bodies (openbody, hybridbody..) cannot be measured
                |     between.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The information of the axis system with respect to the product
                |             coordinate system:
                | 
                |                 oComponents(0) is the X coordinate of the origin of the axis
                |                 system
                |                 oComponents(1) is the Y coordinate of the origin of the axis
                |                 system
                |                 oComponents(2) is the Z coordinate of the origin of the axis
                |                 system
                |                 oComponents(3) is the X coordinate of the first direction of
                |                 the axis system
                |                 oComponents(4) is the Y coordinate of the first direction of
                |                 the axis system
                |                 oComponents(5) is the Z coordinate of the first direction of
                |                 the axis system 
                | 
                |     Example:
                | 
                |              This example retrieves the distance between the reference1 and
                |              reference2.
                |             Dim reference1 As Reference
                |             Set reference1 = part1.CreateReferenceFromObject(object1)
                |             Dim reference2 As Reference
                |             Set reference2 = part1.CreateReferenceFromObject(object1)
                |             Dim TheSPAWorkbench As Workbench
                |             Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
                |             Dim TheMeasurable As Measurable
                |             Set TheMeasurable = TheSPAWorkbench.GetMeasurable(reference1)
                |             Dim MinimumDistance As double
                |             MinimumDistance = TheMeasurable.GetMinimumDistance(reference2)

        :param Reference i_measured_item:
        :return: float
        """
        return self.measure_setting_att.GetMinimumDistance(i_measured_item.com_object)

    def get_minimum_distance_points(self, i_measured_item=None, o_coordinates=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetMinimumDistancePoints(Reference iMeasuredItem,
                | CATSafeArrayVariant oCoordinates)
                | 
                |     Compute the points corresponding to the minimum distance between the two
                |     references.
                | 
                |     Example:
                | 
                |              This example retrieves the points corresponding to the distance
                |              between the reference1 and reference2.
                |             Dim reference1 As Reference
                |             Set reference1 = part1.CreateReferenceFromObject(object1)
                |             Dim reference2 As Reference
                |             Set reference2 = part1.CreateReferenceFromObject(object1)
                |             Dim TheSPAWorkbench As Workbench
                |             Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
                |             Dim TheMeasurable As Measurable
                |             Set TheMeasurable = TheSPAWorkbench.GetMeasurable(reference1)
                |             Dim Coordinates (8)
                |             TheMeasurable.GetMinimumDistancePoints reference2,
                |             Coordinates

        :param Reference i_measured_item:
        :param tuple o_coordinates:
        :return: None
        """
        return self.measure_setting_att.GetMinimumDistancePoints(i_measured_item.com_object, o_coordinates)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_minimum_distance_points'
        # # vba_code = """
        # # Public Function get_minimum_distance_points(measure_setting_att)
        # #     Dim iMeasuredItem (2)
        # #     measure_setting_att.GetMinimumDistancePoints iMeasuredItem
        # #     get_minimum_distance_points = iMeasuredItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_plane(self, o_components=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetPlane(CATSafeArrayVariant oComponents)
                | 
                |     Retrieves informations of the plane.
                | 
                |     Parameters:
                | 
                |         oComponents
                |             The informations of the plane with respect to the product
                |             coordinate system:
                | 
                |                 oComponents(0) is the X coordinate of the
                |                 origin
                |                 oComponents(1) is the Y coordinate of the
                |                 origin
                |                 oComponents(2) is the Z coordinate of the
                |                 origin
                |                 oComponents(3) is the X coordinate of the first direction of
                |                 the plane
                |                 oComponents(4) is the Y coordinate of the first direction of
                |                 the plane
                |                 oComponents(5) is the Z coordinate of the first direction of
                |                 the plane
                |                 oComponents(6) is the X coordinate of the second direction of
                |                 the plane
                |                 oComponents(7) is the Y coordinate of the second direction of
                |                 the plane
                |                 oComponents(8) is the Z coordinate of the second direction of
                |                 the plane 
                | 
                |     Example:
                | 
                |              This example retrieves informations of the plane of NewMeasurable
                |              measure.
                |             
                | 
                |             Dim Components (2)
                |             NewMeasurable.GetPlane Components

        :param tuple o_components:
        :return: None
        """
        return self.measure_setting_att.GetPlane(o_components)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_plane'
        # # vba_code = """
        # # Public Function get_plane(measure_setting_att)
        # #     Dim oComponents (2)
        # #     measure_setting_att.GetPlane oComponents
        # #     get_plane = oComponents
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_point(self, o_coordinates=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetPoint(CATSafeArrayVariant oCoordinates)
                | 
                |     Retrieves the position of the point.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The coordinate of the point with respect to the product coordinate
                |             system:
                | 
                |                 oCoordinates(0) is the X coordinate
                |                 oCoordinates(1) is the Y coordinate
                |                 oCoordinates(2) is the Z coordinate 
                | 
                |     Example:
                | 
                |              This example retrieves the coordinate of the point of
                |              NewMeasurable measure.
                |             
                | 
                |             Dim Coordinates (2)
                |             NewMeasurable.GetPoint Coordinates

        :param tuple o_coordinates:
        :return: None
        """
        return self.measure_setting_att.GetPoint(o_coordinates)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_point'
        # # vba_code = """
        # # Public Function get_point(measure_setting_att)
        # #     Dim oCoordinates (2)
        # #     measure_setting_att.GetPoint oCoordinates
        # #     get_point = oCoordinates
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_points_on_axis(self, o_coordinates=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetPointsOnAxis(CATSafeArrayVariant oCoordinates)
                | 
                |     Retrieves the the characteristic points of the axis with respect of the
                |     size of the revolution object.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The information of the characteristic points with respect to the
                |             product coordinate system:
                | 
                |                 oCoordinates(0) is the X coordinate of the centerpoint of the
                |                 axis
                |                 oCoordinates(1) is the Y coordinate of the centerpoint of the
                |                 axis
                |                 oCoordinates(2) is the Z coordinate of the centerpoint of the
                |                 axis
                |                 oCoordinates(3) is the X coordinate of the startpoint of the
                |                 axis
                |                 oCoordinates(4) is the Y coordinate of the startpoint of the
                |                 axis
                |                 oCoordinates(5) is the Z coordinate of the startpoint of the
                |                 axis
                |                 oCoordinates(6) is the X coordinate of the endpoint of the
                |                 axis
                |                 oCoordinates(7) is the Y coordinate of the endpoint of the
                |                 axis
                |                 oCoordinates(8) is the Z coordinate of the endpoint of the axis
                |                 
                | 
                |     Example:
                | 
                |              This example retrieves the characteristic points of the axis of
                |              NewMeasurable measure.
                |             
                | 
                |             Dim Coordinates (8)
                |             NewMeasurable.GetPointsOnAxis Coordinates

        :param tuple o_coordinates:
        :return: None
        """
        return self.measure_setting_att.GetPointsOnAxis(o_coordinates)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_points_on_axis'
        # # vba_code = """
        # # Public Function get_points_on_axis(measure_setting_att)
        # #     Dim oCoordinates (2)
        # #     measure_setting_att.GetPointsOnAxis oCoordinates
        # #     get_points_on_axis = oCoordinates
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_points_on_curve(self, o_coordinates=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetPointsOnCurve(CATSafeArrayVariant oCoordinates)
                | 
                |     Retrieves the the characteristic points of the curve : the start point, the middle point and the
                |     end point.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The information of the characteristic points of the curve with
                |             respect to the product coordinate system:
                | 
                |                 oCoordinates(0) is the X coordinate of the startpoint of the
                |                 curve
                |                 oCoordinates(1) is the Y coordinate of the startpoint of the
                |                 curve
                |                 oCoordinates(2) is the Z coordinate of the startpoint of the
                |                 curve
                |                 oCoordinates(3) is the X coordinate of the midpoint of the
                |                 curve
                |                 oCoordinates(4) is the Y coordinate of the midpoint of the
                |                 curve
                |                 oCoordinates(5) is the Z coordinate of the midpoint of the
                |                 curve
                |                 oCoordinates(6) is the X coordinate of the endpoint of the
                |                 curve
                |                 oCoordinates(7) is the Y coordinate of the endpoint of the
                |                 curve
                |                 oCoordinates(8) is the Z coordinate of the endpoint of the
                |                 curve 
                | 
                |     Example:
                | 
                |              This example retrieves the characteristic points of the curve of
                |              NewMeasurable measure.
                |             
                | 
                |             Dim Coordinates (8)
                |             NewMeasurable.GetPointsOnCurve Coordinates

        :param tuple o_coordinates:
        :return: None
        """
        return self.measure_setting_att.GetPointsOnCurve(o_coordinates)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_points_on_curve'
        # # vba_code = """
        # # Public Function get_points_on_curve(measure_setting_att)
        # #     Dim oCoordinates (2)
        # #     measure_setting_att.GetPointsOnCurve oCoordinates
        # #     get_points_on_curve = oCoordinates
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MeasureSettingAtt(name="{ self.name }")'
