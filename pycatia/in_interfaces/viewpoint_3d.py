#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ViewPoint3D(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Viewpoint3D
                | 
                | Represents the 3D viewpoint.
                | The 3D viewpoint is the object that stores data which defines how your objects
                | are seen to enable their display by a 3D viewer. This data includes namely the
                | eye location, also named the origin, the distance from the eye to the target,
                | that is to the looked at point in the scene, the sight, up, and right
                | directions, defining a 3D axis system with the eye location as origin, the
                | projection type chosen among perspective (conic) and parallel (cylindric), and
                | the zoom factor. The right direction is not exposed in a property, and is
                | automatically computed from the sight and up directions.
                | 
                | See also:
                |     CatProjectionMode
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.viewpoint_3d = com_object

    @property
    def field_of_view(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FieldOfView() As double
                | 
                |     Returns or sets the field of view associated with the viewpoint. The field
                |     of view is half of the vertical angle of the viewpoint, expressed in degrees.
                |     This property exists with the perspective (conic) projection type
                |     only.
                | 
                |     Example:
                |         This example retrieves in HalfAngle the field of view associated with
                |         the NiceViewpoint viewpoint.
                | 
                |          HalfAngle = NiceViewpoint.FieldOfView

        :rtype: float
        """

        return self.viewpoint_3d.FieldOfView

    @field_of_view.setter
    def field_of_view(self, value: float):
        """
        :param float value:
        """

        self.viewpoint_3d.FieldOfView = value

    @property
    def focus_distance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FocusDistance() As double
                | 
                |     Returns or sets the focus distance of the viewpoint. The focus distance
                |     determines the target position, that is the point at which the eye located at
                |     the origin and looking towards the sight direction is looking at. It is
                |     expressed in model units.
                | 
                |     Example:
                |         This example sets the focus distance of the NiceViewpoint viewpoint to
                |         10.
                | 
                |          NiceViewpoint.FocusDistance = 10

        :rtype: float
        """

        return self.viewpoint_3d.FocusDistance

    @focus_distance.setter
    def focus_distance(self, value: float):
        """
        :param float value:
        """

        self.viewpoint_3d.FocusDistance = value

    @property
    def projection_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ProjectionMode() As CatProjectionMode
                | 
                |     Returns or sets the projection mode.
                | 
                |     Example:
                |         This example sets the projection mode for the My3DViewer 3D viewer to
                |         catProjectionConic.
                | 
                |          My3DViewer.Viewpoint3D.NavigationStyle = catProjectionConic

        :return: enum cat_projection_mode
        :rtype: int
        """

        return self.viewpoint_3d.ProjectionMode

    @projection_mode.setter
    def projection_mode(self, value: int):
        """
        :param int value: enum cat_projection_mode
        """

        self.viewpoint_3d.ProjectionMode = value

    @property
    def zoom(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Zoom() As double
                | 
                |     Returns or sets the zoom factor associated with the viewpoint. This
                |     property exists with the parallel (cylindric) projection type
                |     only.
                | 
                |     Example:
                |         This example retrieves in ZoomFactor the zoom factor associated with
                |         the NiceViewpoint viewpoint, tests if it is greater than 2, and if so, sets it
                |         to one and applies it.
                | 
                |          ZoomFactor = NiceViewpoint.Zoom
                |          If ZoomFactor > 2 Then
                |           ZoomFactor = 1
                |           NiceViewpoint.Zoom(ZoomFactor)
                |          End If

        :rtype: float
        """

        return self.viewpoint_3d.Zoom

    @zoom.setter
    def zoom(self, value: float):
        """
        :param float value:
        """

        self.viewpoint_3d.Zoom = value

    def get_origin(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetOrigin(CATSafeArrayVariant origin)
                | 
                |     Retrieves the coordinates of the origin of the viewpoint. These coordinates
                |     are returned as an array of 3 Variants (double type).
                | 
                |     Example:
                |         This example retrieves the origin of the NiceViewpoint viewpoint in the
                |         origin variable.
                | 
                |          Dim origin(2)
                |          NiceViewpoint.GetOrigin origin

        :rtype: tuple
        """
        vba_function_name = 'get_origin'
        vba_code = """
        Public Function get_origin(viewpoint_3d)
            Dim origin (2)
            viewpoint_3d.GetOrigin origin
            get_origin = origin
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_sight_direction(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSightDirection(CATSafeArrayVariant oSight)
                | 
                |     Gets the components of the sight direction of the viewpoint. The sight
                |     direction is the line passes both by the origin of the viewpoint and by the
                |     target.
                | 
                |     Example:
                |         This example gets the sight direction of the
                |         NiceViewpoint
                | 
                |          Dim sight(2)
                |          NiceViewpoint.GetSightDirection sight

        :rtype: tuple
        """
        vba_function_name = 'get_sight_direction'
        vba_code = """
        Public Function get_sight_direction(viewpoint_3d)
            Dim oSight (2)
            viewpoint_3d.GetSightDirection oSight
            get_sight_direction = oSight
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_up_direction(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetUpDirection(CATSafeArrayVariant oUp)
                | 
                |     Gets the components of the up direction of the viewpoint.
                | 
                |     Example:
                |         This example gets the up direction of the
                |         NiceViewpoint.
                | 
                |          Dim up(2)
                |          NiceViewpoint.GetUpDirection up

        :rtype: tuple
        """

        vba_function_name = 'get_up_direction'
        vba_code = """
        Public Function get_up_direction(viewpoint_3d)
            Dim oUp (2)
            viewpoint_3d.GetUpDirection oUp
            get_up_direction = oUp
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_origin(self, origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutOrigin(CATSafeArrayVariant origin)
                | 
                |     Sets the coordinates of the origin of the viewpoint. These coordinates are
                |     set as an array of 3 Variants (double type).
                | 
                |     Example:
                |         This example sets the origin of the NiceViewpoint viewpoint. to the
                |         point with coordinates (10, 25, 15).
                | 
                |          NiceViewpoint.PutOrigin Array(10, 25, 15)

        :param tuple origin:
        :rtype: None
        """
        return self.viewpoint_3d.PutOrigin(origin)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_origin'
        # # vba_code = """
        # # Public Function put_origin(viewpoint_3d)
        # #     Dim origin (2)
        # #     viewpoint_3d.PutOrigin origin
        # #     put_origin = origin
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_sight_direction(self, o_sight: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutSightDirection(CATSafeArrayVariant oSight)
                | 
                |     Sets the components of the sight direction of the viewpoint. The sight
                |     direction is the line passes both by the origin of the viewpoint and by the
                |     target.
                | 
                |     Example:
                |         This example sets the sight direction of the NiceViewpoint viewpoint to
                |         the direction with components (1.414, 1.414, 0).
                | 
                |          NiceViewpoint.PutSightDirection Array(1.414, 1.414,
                |          0)

        :param tuple o_sight:
        :rtype: None
        """
        return self.viewpoint_3d.PutSightDirection(o_sight)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_sight_direction'
        # # vba_code = """
        # # Public Function put_sight_direction(viewpoint_3d)
        # #     Dim oSight (2)
        # #     viewpoint_3d.PutSightDirection oSight
        # #     put_sight_direction = oSight
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_up_direction(self, o_up: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutUpDirection(CATSafeArrayVariant oUp)
                | 
                |     Sets the components of the up direction of the viewpoint.
                | 
                |     Example:
                |         This example sets the up direction of the NiceViewpoint viewpoint to
                |         the direction with components (0, 0, 1).
                | 
                |          NiceViewpoint.PutUpDirection Array(0, 0, 1)

        :param tuple o_up:
        :rtype: None
        """
        return self.viewpoint_3d.PutUpDirection(o_up)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_up_direction'
        # # vba_code = """
        # # Public Function put_up_direction(viewpoint_3d)
        # #     Dim oUp (2)
        # #     viewpoint_3d.PutUpDirection oUp
        # #     put_up_direction = oUp
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ViewPoint3D(name="{self.name}")'
