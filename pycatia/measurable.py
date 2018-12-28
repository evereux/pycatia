#! /usr/bin/python3.6

"""

    Python Class to aid access of the CATIAMeasurable measurements.

    There doesn't seem to be a solution to access some of the measurement functions other than running the VBA code
    itself and returning and capturing that output.

"""

from .general_functions import run_system_service

catia_measurable_name_list = ['CatMeasurableUnknown',
                              'CatMeasurable',
                              'CatMeasurableVolume',
                              'CatMeasurableSurface',
                              'CatMeasurableCylinder',
                              'CatMeasurableSphere',
                              'CatMeasurableCone',
                              'CatMeasurablePlane',
                              'CatMeasurableCurve',
                              'CatMeasurableCircle',
                              'CatMeasurableLine',
                              'CatMeasurablePoint',
                              'CatMeasurableAxisSystem', ]


# noinspection SpellCheckingInspection
class CATIAMeasurable:
    """
    The interface to access a CATIAMeasurable Get measurements on the object.

    ### FROM CAA V5 Visual Basic help ###
    # Two types of measurement can be done:
    #
    # itself : gives dimensions related to the object itself (ex the radius of a circle).
    # between : gives dimensions related to another object (ex the distance between two products). A restriction occurs
    # for distance between: bodies (CATBody) cannot be measured.
    #
    # Methods on VOLUME : GetVolume GetArea GetCOG
    # Methods on SURFACE : GetArea GetCOG GetPerimeter
    # Methods on PLANE : GetArea GetCOG GetPlane
    # Methods on CYLINDER : GetArea GetCOG GetAxis GetPointsOnAxis GetRadius
    # Methods on CONE : GetArea GetCOG GetAxis GetPointsOnAxis GetAngle
    # Methods on SPHERE : GetArea GetCOG GetRadius GetCenter
    # Methods on CURVE : GetLength GetCOG GetPointsOnCurve
    # Methods on LINE : GetLength GetCOG GetPointsOnCurve GetDirection
    # Methods on CIRCLE : GetLength GetCOG GetPointsOnCurve GetRadius GetCenter GetAngle GetAxis
    # Methods on POINT : GetPoint
    # Methods on AXIS SYST : GetAxisSystem

    """

    def __init__(self, measurable):
        """
        :param measurable:
        """

        self.cat_script_language = 0

        self.measurable = measurable

    @property
    def angle(self):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Property Angle( ) As double (Read Only)
        #
        # Returns the Angle of a circle or cone.
        # Example:
        # This example retrieves the Angle of NewMeasurable measure.
        #     Dim AAngle As double
        #     AAngle = NewMeasurable.Angle

        :return:
        """
        return self.measurable.Angle

    @property
    def area(self):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Property Area( ) As double (Read Only)
        #
        # Returns the area of the surface or wet area from volume.
        # Example:
        # This example retrieves the area of NewMeasurable measure. The area unit given by oArea is m²
        #     Dim AArea As double
        #     AArea = NewMeasurable.Area

        :return:
        """
        return self.measurable.Area

    @property
    def geometry_name(self):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Property GeometryName( ) As CatMeasurableName (Read Only)
        #
        # Returns the name of the geometry of the measured object.
        # Example:
        # This example retrieves the name of the geometry of the NewMeasurable measure.
        #     Dim AGeometryName As CatMeasurableName
        #     AGeometryName = NewMeasurable.GeometryName

        :return:
        """
        return catia_measurable_name_list[self.measurable.GeometryName]

    @property
    def length(self):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Property Length( ) As double (Read Only)
        #
        # Returns the Length of a curve.
        # Example:
        # This example retrieves the Length of NewMeasurable measure.
        #     Dim ALength As double
        #     ALength = NewMeasurable.Length

        :return:
        """
        return self.measurable.Length

    @property
    def perimeter(self):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Property Perimeter( ) As double (Read Only)
        #
        # Returns the perimeter of a surface.
        # Example:
        # This example retrieves the perimeter of NewMeasurable measure.
        #     Dim APerimeter As double
        #     APerimeter = NewMeasurable.Perimeter

        :return:
        """
        return self.measurable.Perimeter

    @property
    def radius(self):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Property Radius( ) As double (Read Only)
        #
        # Returns the radius of an arc, cylinder or sphere.
        # Example:
        # This example retrieves the Radius of NewMeasurable measure.
        #     Dim ARadius As double
        #     ARadius = NewMeasurable.Radius

        :return:
        """
        return self.measurable.Radius

    @property
    def volume(self):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Property Volume( ) As double (Read Only)
        #
        # Returns the volume.
        # Example:
        # This example retrieves the volume of NewMeasurable measure. The volume unit given by oVolume is m^3
        #     Dim AVolume As double
        #     AVolume = NewMeasurable.Volume

        :return:
        """
        return self.measurable.Volume

    def get_angle_between(self, reference_measurable):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Func GetAngleBetween( Reference  iMeasuredItem) As double
        #
        # Compute the angle between the CATIAMeasurable and another.
        # Example:
        # This example retrieves the angle between the reference1 and reference2.
        #
        # Dim reference1 As Reference
        # Set reference1 = part1.CreateReferenceFromObject(object1)
        #
        # Dim reference2 As Reference
        # Set reference2 = part1.CreateReferenceFromObject(object1)
        #
        # Dim TheSPAWorkbench As Workbench
        # Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
        #
        # Dim TheMeasurable As Measurable
        # Set TheMeasurable = TheSPAWorkbench.GetMeasurable(reference1)
        #
        # Dim MinimumDistance As double
        # MinimumDistance = TheMeasurable.GetAngleBetween(reference2)

        :return:
        """

        return self.measurable.GetAngleBetween(reference_measurable)

    def get_axis(self):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Sub GetAxis( CATSafeArrayVariant  oAxisVector)
        #
        # Retrieves the axis vector of the cylinder or a cone.
        # Parameters:
        # oVector
        # The axis vector of the cylinder or a cone with respect to the product coordinate system:
        # oAxisVector(0) is the X direction
        # oAxisVector(1) is the Y direction
        # oAxisVector(2) is the Z direction
        # Example:
        # This example retrieves the axis vector of the cylinder or a cone of NewMeasurable measure.
        #     Dim AxisVector (2)
        #     NewMeasurable.GetAxis AxisVector

        :return:
        """
        vba_function_name = 'get_axis'
        vba_function = 'GetAxis'
        vba_code = f'''   
        Public Function {vba_function_name}(measurable)
            Dim AxisVector (2)
            measurable.{vba_function} AxisVector
            {vba_function_name} = AxisVector
        End Function
        '''
        result = run_system_service(vba_code, vba_function_name, [self.measurable])

        return result

    def get_axis_system(self):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Sub GetAxisSystem( CATSafeArrayVariant  oComponents)
        #
        # Retrieves the information of the axis system.
        # Parameters:
        # oCoordinates
        # The information of the axis system with respect to the product coordinate system:
        # oComponents(0) is the X coordinate of the origin of the axis system
        # oComponents(1) is the Y coordinate of the origin of the axis system
        # oComponents(2) is the Z coordinate of the origin of the axis system
        # oComponents(3) is the X coordinate of the first direction of the axis system
        # oComponents(4) is the Y coordinate of the first direction of the axis system
        # oComponents(5) is the Z coordinate of the first direction of the axis system
        # oComponents(6) is the X coordinate of the second direction of the axis system
        # oComponents(7) is the Y coordinate of the second direction of the axis system
        # oComponents(8) is the Z coordinate of the second direction of the axis system
        # oComponents(9) is the X coordinate of the third direction of the axis system
        # oComponents(10) is the Y coordinate of the third direction of the axis system
        # oComponents(11) is the Z coordinate of the third direction of the axis system
        # Example:
        # This example retrieves information of the axis system of NewMeasurable measure.
        #     Dim Components (11)
        #     NewMeasurable.GetAxisSystem Components

        :return:
        """

        vba_function_name = 'get_axis_system'
        vba_function = 'GetAxisSystem'
        vba_code = f'''        
            Public Function {vba_function_name}(measurable)
                Dim Components (11)
                measurable.{vba_function} Components
                {vba_function_name} = Components
            End Function
            '''

        result = run_system_service(vba_code, vba_function_name, [self.measurable])

        return result

    def get_cog(self):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Sub GetCOG( CATSafeArrayVariant  oCoordinates)
        #
        # Retrieves the position of the center of gravity of a surface and volume .
        # Parameters:
        # oCoordinates
        # The position of the center of gravity with respect to the product coordinate system:
        # oCoordinates(0) is the X coordinate
        # oCoordinates(1) is the Y coordinate
        # oCoordinates(2) is the Z coordinate
        # Example:
        # This example retrieves the position of the center of gravity of NewMeasurable measure.
        #     Dim Coordinates (2)
        #     NewMeasurable.GetCOG Coordinates

        :return:
        """

        vba_function_name = 'create_cog'
        vba_function = 'GetCOG'
        vba_code = f'''        
        Public Function {vba_function_name}(measurable)
            Dim coord(2)
            measurable.{vba_function} coord
            {vba_function_name} = coord
        End Function
        '''
        result = run_system_service(vba_code, vba_function_name, [self.measurable])

        return result

    def get_center(self):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Sub GetCenter( CATSafeArrayVariant  oCoordinates)
        #
        # Retrieves the position of the center of a circle or sphere.
        # Parameters:
        # oCoordinates
        # The position of the center with respect to the product coordinate system:
        # oCoordinates(0) is the X coordinate
        # oCoordinates(1) is the Y coordinate
        # oCoordinates(2) is the Z coordinate
        # Example:
        # This example retrieves the position of the center of NewMeasurable measure.
        #     Dim Coordinates (2)
        #     NewMeasurable.GetCenter Coordinates << fixed typo in help

        :return:
        """

        vba_function_name = 'get_center'
        vba_function = 'GetCenter'
        vba_code = f'''        
        Public Function {vba_function_name}(measurable)
            Dim Coordinates (2)
            measurable.{vba_function} Coordinates
            {vba_function_name} = Coordinates
        End Function
        '''

        result = run_system_service(vba_code, vba_function_name, [self.measurable])

        return result

    def get_direction(self):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Sub GetDirection( CATSafeArrayVariant  oDirection)
        #
        # Retrieves the direction of the line.
        # Parameters:
        # oDirection
        # The direction of the line with respect to the product coordinate system:
        # oDirection(0) is the X direction
        # oDirection(1) is the Y direction
        # oDirection(2) is the Z direction
        # Example:
        # This example retrieves the direction of the line of NewMeasurable measure.
        #     Dim Direction (2)
        #     NewMeasurable.GetDirection Direction

        :return: 
        """

        vba_function_name = 'get_direction'
        vba_function = 'GetDirection'
        vba_code = f'''        
        Public Function {vba_function_name}(measurable)
            Dim direction (2) 
            measurable.{vba_function} direction
            {vba_function_name} = direction
        End Function
        '''

        result = run_system_service(vba_code, vba_function_name, [self.measurable])

        return result

    def get_minimum_distance(self, reference):
        # noinspection SpellCheckingInspection
        """
        ### FROM CAA V5 Visual Basic help ###
        # Func GetMinimumDistance( Reference  iMeasuredItem) As double
        #
        # Compute the minimum distance between the CATIAMeasurable and another.
        # Bodies (openbody, hybridbody..) cannot be measured between.
        # Parameters:
        # oCoordinates
        # The information of the axis system with respect to the product coordinate system:
        # oComponents(0) is the X coordinate of the origin of the axis system
        # oComponents(1) is the Y coordinate of the origin of the axis system
        # oComponents(2) is the Z coordinate of the origin of the axis system
        # oComponents(3) is the X coordinate of the first direction of the axis system
        # oComponents(4) is the Y coordinate of the first direction of the axis system
        # oComponents(5) is the Z coordinate of the first direction of the axis system
        # Example:
        #   This example retrieves the distance between the reference1 and reference2.
        #   Dim reference1 As Reference
        #   Set reference1 = part1.CreateReferenceFromObject(object1)
        #   Dim reference2 As Reference
        #   Set reference2 = part1.CreateReferenceFromObject(object1)
        #   Dim TheSPAWorkbench As Workbench
        #   Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
        #   Dim TheMeasurable As Measurable
        #   Set TheMeasurable = TheSPAWorkbench.GetMeasurable(reference1)
        #   Dim MinimumDistance As double
        #   MinimumDistance = TheMeasurable.GetMinimumDistance(reference2)

        :return:
        """

        return self.measurable.GetMinimumDistance(reference)

    def get_minimum_distance_points(self, point_reference):
        """

        ### FROM CAA V5 Visual Basic help ###
        # Sub GetMinimumDistancePoints( Reference  iMeasuredItem,
        #  CATSafeArrayVariant  oCoordinates)
        #
        # Compute the points corresponding to the minimum distance between the two references.
        # Example:
        # This example retrieves the points corresponding to the distance between the reference1 and reference2.
        #   Dim reference1 As Reference
        #   Set reference1 = part1.CreateReferenceFromObject(object1)
        #   Dim reference2 As Reference
        #   Set reference2 = part1.CreateReferenceFromObject(object1)
        #   Dim TheSPAWorkbench As Workbench
        #   Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
        #   Dim TheMeasurable As Measurable
        #   Set TheMeasurable = TheSPAWorkbench.GetMeasurable(reference1)
        #   Dim Coordinates (8)
        #   TheMeasurable.GetMinimumDistancePoints reference2, Coordinates

        :return:
        """

        vba_function_name = 'get_minimum_distance_points'
        vba_function = 'GetMinimumDistancePoints'
        vba_code = f'''        
        Public Function {vba_function_name}(measurable, point_reference)
            Dim Coordinates (8) 
            measurable.{vba_function} point_reference, Coordinates
            {vba_function_name} = Coordinates
        End Function
        '''

        return run_system_service(vba_code, vba_function_name, [self.measurable, point_reference])

    def get_plane(self):
        """

        ### FROM CAA V5 Visual Basic help ###
        # Sub GetPlane( CATSafeArrayVariant  oComponents)
        #
        # Retrieves informations of the plane.
        # Parameters:
        # oComponents
        # The informations of the plane with respect to the product coordinate system:
        # oComponents(0) is the X coordinate of the origin
        # oComponents(1) is the Y coordinate of the origin
        # oComponents(2) is the Z coordinate of the origin
        # oComponents(3) is the X coordinate of the first direction of the plane
        # oComponents(4) is the Y coordinate of the first direction of the plane
        # oComponents(5) is the Z coordinate of the first direction of the plane
        # oComponents(6) is the X coordinate of the second direction of the plane
        # oComponents(7) is the Y coordinate of the second direction of the plane
        # oComponents(8) is the Z coordinate of the second direction of the plane
        # Example:
        # This example retrieves informations of the plane of NewMeasurable measure.
        #     Dim Components (8)
        #     NewMeasurable.GetPlane Components

        :return:
        """

        vba_function_name = 'get_plane'
        vba_function = 'GetPlane'
        vba_code = f'''        
        Public Function {vba_function_name}(measurable)
            Dim Components (8)
            measurable.{vba_function} Components
            {vba_function_name} = Components
        End Function
        '''

        return run_system_service(vba_code, vba_function_name, [self.measurable])

    def get_point(self):
        """

        ### FROM CAA V5 Visual Basic help ###
        # Sub GetPoint( CATSafeArrayVariant  oCoordinates)
        #
        # Retrieves the position of the point.
        # Parameters:
        # oCoordinates
        # The coordinate of the point with respect to the product coordinate system:
        # oCoordinates(0) is the X coordinate
        # oCoordinates(1) is the Y coordinate
        # oCoordinates(2) is the Z coordinate
        # Example:
        # This example retrieves the coordinate of the point of NewMeasurable measure.
        #     Dim Coordinates (2)
        #     NewMeasurable.GetPoint Coordinates
        #

        :return:
        """

        vba_function_name = 'get_point'
        vba_function = 'GetPoint'
        vba_code = f'''        
        Public Function {vba_function_name}(measurable)
            Dim Coordinates (2)
            measurable.{vba_function} Coordinates
            {vba_function_name} = Coordinates
        End Function
        '''

        return run_system_service(vba_code, vba_function_name, [self.measurable])

    def get_points_on_axis(self):
        # noinspection SpellCheckingInspection,SpellCheckingInspection
        """

                ### FROM CAA V5 Visual Basic help ###
                # Sub GetPointsOnAxis( CATSafeArrayVariant  oCoordinates)
                #
                # Retrieves the the characteristic points of the axis with respect of the size of the revolution object.
                # Parameters:
                # oCoordinates
                # The information of the characteristic points with respect to the product coordinate system:
                # oCoordinates(0) is the X coordinate of the centerpoint of the axis
                # oCoordinates(1) is the Y coordinate of the centerpoint of the axis
                # oCoordinates(2) is the Z coordinate of the centerpoint of the axis
                # oCoordinates(3) is the X coordinate of the startpoint of the axis
                # oCoordinates(4) is the Y coordinate of the startpoint of the axis
                # oCoordinates(5) is the Z coordinate of the startpoint of the axis
                # oCoordinates(6) is the X coordinate of the endpoint of the axis
                # oCoordinates(7) is the Y coordinate of the endpoint of the axis
                # oCoordinates(8) is the Z coordinate of the endpoint of the axis
                # Example:
                # This example retrieves the characteristic points of the axis of NewMeasurable measure.
                #     Dim Coordinates (8)
                #     NewMeasurable.GetPointsOnAxis Coordinates
                #

                :return:
                """

        vba_function_name = 'get_points_on_axis'
        vba_function = 'GetPointsOnAxis'
        vba_code = f'''        
        Public Function {vba_function_name}(measurable)
            Dim Coordinates (8)
            measurable.{vba_function} Coordinates
            {vba_function_name} = Coordinates
        End Function
        '''

        return run_system_service(vba_code, vba_function_name, [self.measurable])

    def get_points_on_curve(self):
        """
        ### FROM CAA V5 Visual Basic help ###
        # Sub GetPointsOnCurve( CATSafeArrayVariant  oCoordinates)
        #
        # Retrieves the the characteristic points of the curve : the start point, the middle point and the end point.
        # Parameters:
        # oCoordinates
        # The information of the characteristic points of the curve with respect to the product coordinate system:
        # oCoordinates(0) is the X coordinate of the startpoint of the curve
        # oCoordinates(1) is the Y coordinate of the startpoint of the curve
        # oCoordinates(2) is the Z coordinate of the startpoint of the curve
        # oCoordinates(3) is the X coordinate of the midpoint of the curve
        # oCoordinates(4) is the Y coordinate of the midpoint of the curve
        # oCoordinates(5) is the Z coordinate of the midpoint of the curve
        # oCoordinates(6) is the X coordinate of the endpoint of the curve
        # oCoordinates(7) is the Y coordinate of the endpoint of the curve
        # oCoordinates(8) is the Z coordinate of the endpoint of the curve
        # Example:
        # This example retrieves the characteristic points of the curve of NewMeasurable measure.
        #     Dim Coordinates (8)
        #     NewMeasurable.GetPointsOnCurve Coordinates

        :return:
        """

        vba_function_name = 'get_points_on_curve'
        vba_function = 'GetPointsOnCurve'
        vba_code = f'''        
        Public Function {vba_function_name}(measurable)
            Dim Coordinates (8)
            measurable.{vba_function} Coordinates
            {vba_function_name} = Coordinates
        End Function
        '''

        return run_system_service(vba_code, vba_function_name, [self.measurable])
