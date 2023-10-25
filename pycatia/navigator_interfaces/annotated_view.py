#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.navigator_interfaces.marker_2Ds import Marker2Ds
from pycatia.system_interfaces.any_object import AnyObject


class AnnotatedView(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnnotatedView
                | 
                | Represents an annotated view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotated_view = com_object

    @property
    def behavior_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BehaviorMode() As CatAnnotatedViewBehavior
                | 
                |     Returns or sets the behavior mode of the annotated view. This behavior mode
                |     enables the annotated view to be independant from the
                |     viewpoint.
                | 
                |     Example:
                | 
                |              This example retrieves the behavior mode of the NewAnnotatedView
                |              annotated view.
                |             
                | 
                |             Dim Mode
                |             Mode = NewAnnotatedView.BehaviorMode

        :return: enum cat_annotated_view_behavior
        :rtype: int
        """

        return self.annotated_view.BehaviorMode

    @behavior_mode.setter
    def behavior_mode(self, value: int):
        """
        :param int value: enum cat_annotated_view_behavior
        """

        self.annotated_view.BehaviorMode = value

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Comment() As CATBSTR
                | 
                |     Returns or sets the comment associated with the annotated
                |     view.
                | 
                |     Example:
                | 
                |              This example retrieves the comment of NewAnnotatedView annotated
                |              view.
                |             
                | 
                |             Dim text As String
                |             text = NewAnnotatedView.Comment

        :rtype: str
        """

        return self.annotated_view.Comment

    @comment.setter
    def comment(self, value: str):
        """
        :param str value:
        """

        self.annotated_view.Comment = value

    @property
    def field_of_view(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FieldOfView() As double (Read Only)
                | 
                |     Returns the field of view associated with the annotated view. The field of
                |     view is half of the vertical angle of the viewpoint, expressed in degrees. This
                |     property exists with the perspective (conic) projection mode
                |     only.
                | 
                |     Example:
                | 
                |              This example retrieves the field of view of the NewAnnotatedView
                |              annotated view.
                |             
                | 
                |             Dim Field As Double
                |             Field = NewAnnotatedView.FieldOfView

        :rtype: float
        """

        return self.annotated_view.FieldOfView

    @property
    def marker2_ds(self) -> Marker2Ds:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Marker2Ds() As Marker2Ds (Read Only)
                | 
                |     Returns the Marker2D Collection associated with the annotated
                |     view.
                | 
                |     Example:
                | 
                |              This example retrieves the TheMarker2Ds
                |              collection
                |             from the NewAnnotatedView annotated view.
                |             
                | 
                |             Dim TheMarker2Ds As AnnotatedView
                |             Set TheMarker2Ds = NewAnnotatedView.Marker2Ds(9)

        :rtype: Marker2Ds
        """

        return Marker2Ds(self.annotated_view.Marker2Ds)

    @property
    def projection_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ProjectionMode() As CatProjectionMode (Read Only)
                | 
                |     Returns the projection mode of the annotated view. This projection mode is
                |     the one of the associated 3D View point.
                | 
                |     Example:
                | 
                |              This example retrieves the projection mode of the NewAnnotatedView
                |              annotated view.
                |             
                | 
                |             Dim Mode
                |             Mode = NewAnnotatedView.ProjectionMode

        :return: enum cat_projection_mode
        :rtype: int
        """

        return self.annotated_view.ProjectionMode

    @property
    def sound(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Sound() As CATBSTR
                | 
                |     Returns or sets the path of the sound file associated with the annotated
                |     view.
                | 
                |     Parameters:
                | 
                |         iPath
                |             The path of the sound file. If this path is not empty, the sound
                |             replaces the old associated one (if it exists) or creates a new association (if
                |             not). If this path is empty, the sound is removed.
                |             
                | 
                |     Returns:
                |         The path of the sound file. If this path is empty, the annotated view
                |         has no associated sound. 
                |     Example:
                | 
                |              This example retrieves the path of the sound file associated with
                |              the NewAnnotatedView annotated view.
                |             
                | 
                |             Dim path As String
                |             path = NewAnnotatedView.Sound

        :rtype: str
        """

        return self.annotated_view.Sound

    @sound.setter
    def sound(self, value: str):
        """
        :param str value:
        """

        self.annotated_view.Sound = value

    @property
    def zoom(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Zoom() As double (Read Only)
                | 
                |     Returns the zoom factor associated with the annotated view. This property
                |     exists with the parallel (cylindric) projection mode only. This zoom factor is
                |     the one of the associated 3D View point.
                | 
                |     Example:
                | 
                |              This example retrieves in ZoomFactor the zoom of the
                |              NewAnnotatedView annotated view.
                |             
                | 
                |             Dim ZoomFactor As Double
                |             ZoomFactor = NewAnnotatedView.Zoom

        :rtype: float
        """

        return self.annotated_view.Zoom

    def get_origin(self, o_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetOrigin(CATSafeArrayVariant oOrigin)
                | 
                |     Retrieves the coordinates of the origin of the 3D viewpoint of the
                |     annotated view.
                | 
                |     Parameters:
                | 
                |         oOrigin
                |             The coordinates of the view point origin expressed as an array of 3
                |             variants are:
                | 
                |                 oOrigin(0) is the X coordinate of the origin
                |                 oOrigin(1) is the Y coordinate of the origin
                |                 oOrigin(2) is the Z coordinate of the origin 
                | 
                |     Example:
                | 
                |              This example retrieves the origin of the 3D viewpoint of the
                |              NewAnnotatedView annotated view.
                |             
                | 
                |             Dim origin(2)
                |             NewAnnotatedView.GetOrigin origin

        :param tuple o_origin:
        :rtype: None
        """
        return self.annotated_view.GetOrigin(o_origin)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_origin'
        # # vba_code = """
        # # Public Function get_origin(annotated_view)
        # #     Dim oOrigin (2)
        # #     annotated_view.GetOrigin oOrigin
        # #     get_origin = oOrigin
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_sight_direction(self, o_sight: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSightDirection(CATSafeArrayVariant oSight)
                | 
                |     Retrieves the components of the sight direction of the 3D viewpoint of the
                |     annotated view. The sight direction is the line that passes by the origin of
                |     the viewpoint and by the target.
                | 
                |     Parameters:
                | 
                |         oSight
                |             The components of the viewpoint sight direction expressed as an
                |             array of 3 variants are:
                | 
                |                 oSight(0) is the X component of the sight
                |                 direction
                |                 oSight(1) is the Y component of the sight
                |                 direction
                |                 oSight(2) is the Z component of the sight direction
                |                 
                | 
                |     Example:
                | 
                |              This example retrieves the sight direction of the NewAnnotatedView
                |              annotated view.
                |             
                | 
                |             Dim sight(2)
                |             NewAnnotatedView.GetSightDirection sight

        :param tuple o_sight:
        :rtype: None
        """
        return self.annotated_view.GetSightDirection(o_sight)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_sight_direction'
        # # vba_code = """
        # # Public Function get_sight_direction(annotated_view)
        # #     Dim oSight (2)
        # #     annotated_view.GetSightDirection oSight
        # #     get_sight_direction = oSight
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_up_direction(self, o_up: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetUpDirection(CATSafeArrayVariant oUp)
                | 
                |     Retrieves the components of the up direction of the 3D viewpoint of the
                |     annotated view.
                | 
                |     Parameters:
                | 
                |         oUp
                |             The components of the viewpoint up direction expressed as an array
                |             of 3 variants are:
                | 
                |                 oUp(0) is the X component of the up direction
                |                 oUp(1) is the Y component of the up direction
                |                 oUp(2) is the Z component of the up direction 
                | 
                |     Example:
                | 
                |              This example retrieves the up direction of the NewAnnotatedView
                |              annotated view.
                |             
                | 
                |             Dim up(2)
                |             NewAnnotatedView.GetUpDirection up

        :param tuple o_up:
        :rtype: None
        """
        return self.annotated_view.GetUpDirection(o_up)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_up_direction'
        # # vba_code = """
        # # Public Function get_up_direction(annotated_view)
        # #     Dim oUp (2)
        # #     annotated_view.GetUpDirection oUp
        # #     get_up_direction = oUp
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Update()
                | 
                |     Updates the annotated view: that is to take into account all modifications
                |     which occur since last update.
                | 
                |     Example:
                | 
                |              This example updates the NewAnnotatedView annotated
                |              view.
                |             
                | 
                |             NewAnnotatedView.Update

        :rtype: None
        """
        return self.annotated_view.Update()

    def __repr__(self):
        return f'AnnotatedView(name="{self.name}")'
