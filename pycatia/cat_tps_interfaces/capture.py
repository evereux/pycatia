#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect
from typing import TYPE_CHECKING

from pycatia.in_interfaces.camera_3d import Camera3D
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.cat_tps_interfaces.tps_view import TPSView
from pycatia.cat_tps_interfaces.tps_views import TPSViews
from pycatia.cat_tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen

if TYPE_CHECKING:
    from pycatia.cat_tps_interfaces.annotations import Annotations
    from pycatia.cat_tps_interfaces.annotation_set import AnnotationSet


class Capture(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Capture
                | 
                | The interface to access a CATIACapture
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.capture = com_object

    @property
    def active_view(self) -> TPSView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActiveView() As TPSView
                | 
                |     Retrieves the active view for the capture.

        :rtype: TPSView
        """

        return TPSView(self.capture.ActiveView)

    @active_view.setter
    def active_view(self, value: TPSView):
        """
        :param TPSView value:
        """

        self.capture.ActiveView = value

    @property
    def active_view_state(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActiveViewState() As boolean
                | 
                |     Retrieves the Active View state, saved or Not. The Active View state
                |     describes what happens when Capture is displayed, if TRUE, the active view of
                |     the tolerancing set is replaced by the active view of the capture.

        :rtype: bool
        """

        return self.capture.ActiveViewState

    @active_view_state.setter
    def active_view_state(self, value: bool):
        """
        :param bool value:
        """

        self.capture.ActiveViewState = value

    @property
    def annotations(self) -> 'Annotations':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Annotations() As Annotations
                | 
                |     Retrieves the TPSs that are visualy managed by this Capture.

        :rtype: Annotations
        """
        from pycatia.cat_tps_interfaces.annotations import Annotations
        return Annotations(self.capture.Annotations)

    @annotations.setter
    def annotations(self, value: 'Annotations'):
        """
        :param Annotations value:
        """

        self.capture.Annotations = value

    @property
    def camera(self) -> Camera3D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Camera() As Camera3D
                | 
                |     Retrieves or sets a camera.

        :rtype: Camera3D
        """

        return Camera3D(self.capture.Camera)

    @camera.setter
    def camera(self, value: Camera3D):
        """
        :param Camera3D value:
        """

        self.capture.Camera = value

    @property
    def clipping_plane(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ClippingPlane() As boolean
                | 
                |     Retrieves the clipping plane state, activated or Not. The Clipping plane
                |     state describes what happens when Capture is displayed, if TRUE, the active
                |     view is used to define a clipping plane. If FALSE, there is no clipping plane
                |     applied.
                | 
                |     Parameters:
                | 
                |         oClipPlane
                |             The clipping plane state.

        :rtype: bool
        """

        return self.capture.ClippingPlane

    @clipping_plane.setter
    def clipping_plane(self, value: bool):
        """
        :param bool value:
        """

        self.capture.ClippingPlane = value

    @property
    def current(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Current() As boolean
                | 
                |     Retrieves the Capture state, current or Not.
                | 
                |     Parameters:
                | 
                |         oCurrentState
                |             Capture state. if TRUE the capture is current.that means that after
                |             the creation of the capture, the future TPSs that would be added to the
                |             document will belong to the capture.

        :rtype: bool
        """

        return self.capture.Current

    @current.setter
    def current(self, value: bool):
        """
        :param bool value:
        """

        self.capture.Current = value

    @property
    def manage_hide_show_body(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ManageHideShowBody() As boolean
                | 
                |     Manages the visibility of Part instances, bodies and geometrical sets
                |     across the Capture.
                | 
                |     Parameters:
                | 
                |         obManageHideShowBody
                |             TRUE: If Hide/Show of these elements will be managed FALSE: If
                |             Hide/Show of these elements will not be managed

        :rtype: bool
        """

        return self.capture.ManageHideShowBody

    @manage_hide_show_body.setter
    def manage_hide_show_body(self, value: bool):
        """
        :param bool value:
        """

        self.capture.ManageHideShowBody = value

    @property
    def set(self) -> 'AnnotationSet':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Set() As AnnotationSet (Read Only)
                | 
                |     Retrieves tolerancing set the Capture belongs too.

        :rtype: AnnotationSet
        """
        from pycatia.cat_tps_interfaces.annotation_set import AnnotationSet
        return AnnotationSet(self.capture.Set)

    @property
    def tps_views(self) -> TPSViews:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TPSViews() As TPSViews
                | 
                |     Retrieves the TPS Views that are visualy managed by this Capture.

        :rtype: TPSViews
        """

        return TPSViews(self.capture.TPSViews)

    @tps_views.setter
    def tps_views(self, value: TPSViews):
        """
        :param TPSViews value:
        """

        self.capture.TPSViews = value

    @property
    def view_point(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ViewPoint() As boolean
                | 
                |     Retrieves the ViewPoint state, saved or Not. The ViewPoint state describes
                |     what happens when Capture is displayed, if TRUE, the 3D Camera of the Capture
                |     is used to change the 3D ViewPoint.

        :rtype: bool
        """

        return self.capture.ViewPoint

    @view_point.setter
    def view_point(self, value: bool):
        """
        :param bool value:
        """

        self.capture.ViewPoint = value

    def display_capture(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub DisplayCapture()
                | 
                |     Displays the Capture.

        :rtype: None
        """
        return self.capture.DisplayCapture()

    def display_capture_2(self, ib_apply_mirror: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub DisplayCapture2(boolean ibApplyMirror)
                | 
                |     Displays the Capture with mirroring annotations
                |     management.
                | 
                |     Parameters:
                | 
                |         out
                |             boolean ibApplyMirror [out] Annotations mirroring management: TRUE:
                |             The annotations mirroring is activated. FALSE: The annotations mirroring is
                |             desactivated.

        :param bool ib_apply_mirror:
        :rtype: None
        """
        return self.capture.DisplayCapture2(ib_apply_mirror)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise, completely remove all this.
        # # vba_function_name = 'display_capture2'
        # # vba_code = """
        # # Public Function display_capture2(capture)
        # #     Dim ibApplyMirror (2)
        # #     capture.DisplayCapture2 ibApplyMirror
        # #     display_capture2 = ibApplyMirror
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func TPSParallelOnScreen() As TPSParallelOnScreen
                | 
                |     Gets the annotation on TPSParallelOnScreen interface.

        :rtype: TPSParallelOnScreen
        """
        return TPSParallelOnScreen(self.capture.TPSParallelOnScreen())

    def get_nbr_of_part_inst_and_body(self) -> int:
        """

        Introduced in V5-6R2022.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2026-02-21 15:26:49.309967)
                | Func GetNbrOfPartInstAndBody() As long
                |     Reads the number of Body and Part Instances assigned to this Capture. This
                |     call is to be called just before @GetPartInstAndBody to allocate the array with
                |     the accurate size. This call is working properly only if ManageHideShowBody is
                |     set to True.
                |
                |     Parameters:
                |
                |         oEntityCount
                |             The number of Part Instance(s) and/or Body(ies) associated with the
                |             Capture.

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.capture.GetNbrOfPartInstAndBody()

    def get_part_inst_and_body(self, o_list_of_elements: tuple) -> None:
        """

        Introduced in V5-6R2022.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2026-02-21 15:26:49.309967)
                | Sub GetPartInstAndBody(CATSafeArrayVariant oListOfElements)
                |     Returns the list of Body and Part Instances. This call is working properly
                |     only if ManageHideShowBody is set to True.
                |
                |     Parameters:
                |
                |         oListOfElements
                |             The list of Part Instance(s) and Body(s) bound to this Capture. It
                |             is returned as an array of SafeArrayVariant whose size is given by
                |             GetNbrOfPartInstAndBody.
                |
                |             Note: You can access each constraint as follows:
                |
                |                 1 is in oListOfElements(0)
                |                 2 is in oListOfElements(1)
                |                 oEntityCount is in oListOfElements(oEntityCount-1)

        :param tuple o_list_of_elements:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.capture.GetPartInstAndBody(o_list_of_elements)

    def set_part_inst_and_body(self, i_list_of_elements: tuple, i_entity_count: int) -> None:
        """

        Introduced in V5-6R2022.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2026-02-21 15:26:49.309967)
                | Sub SetPartInstAndBody(CATSafeArrayVariant iListOfElements,long
                | iEntityCount)
                |     Sets the list of Body and Part Instances. This call is working properly
                |     only if ManageHideShowBody is set to True.
                |
                |     Parameters:
                |
                |         iListOfElements
                |             The list of Part Instance(s) and Body(s) to assign to this Capture.
                |             iEntityCount of elements are taken for the SafeArrayVariant.
                |
                |         iEntityCount
                |             The number of items in the given stack.

        :param tuple i_list_of_elements:
        :param int i_entity_count:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.capture.SetPartInstAndBody(i_list_of_elements, i_entity_count)

    def __repr__(self):
        return f'Capture(name="{self.name}")'
