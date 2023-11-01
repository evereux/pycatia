#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import TYPE_CHECKING

from pycatia.in_interfaces.camera import Camera
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.in_interfaces.viewer_2d import Viewer2D
    from pycatia.in_interfaces.viewer_3d import Viewer3D


class Viewer(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Viewer
                | 
                | Represents the viewer.
                | The viewer is the object that makes your objects display on the
                | screen.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.viewer = com_object

    @property
    def full_screen(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FullScreen() As boolean
                | 
                |     Returns or sets the state of a viewer to occupy the whole
                |     screen.
                |     True if the viewer occupies the whole screen.
                | 
                |     Example:
                |         This example retrieves in IsFullScreen whether the MyViewer viewer
                |         occupies the whole screen.
                | 
                |          IsFullScreen = MyViewer.FullScreen

        :rtype: bool
        """

        return self.viewer.FullScreen

    @full_screen.setter
    def full_screen(self, value: bool):
        """
        :param bool value:
        """

        self.viewer.FullScreen = value

    @property
    def height(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Height() As long (Read Only)
                | 
                |     Returns the viewer's height, in pixels.
                | 
                |     Example:
                |         This example retrieves the height of the MyViewer
                |         viewer.
                | 
                |          h = MyViewer.Height

        :rtype: int
        """

        return self.viewer.Height

    @property
    def width(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Width() As long (Read Only)
                | 
                |     Returns the viewer's width, in pixels.
                | 
                |     Example:
                |         This example retrieves the width of the MyViewer
                |         viewer.
                | 
                |          w = MyViewer.Width

        :rtype: int
        """

        return self.viewer.Width

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Activate()
                | 
                |     Activates the viewer in the window.
                | 
                |     Example:
                |         This example activates Viewers(1) in the window
                |         MyWindow.
                | 
                |          MyWindow.Viewers(1).Activate()

        :rtype: None
        """
        return self.viewer.Activate()

    def capture_to_file(self, i_format: int, i_file: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub CaptureToFile(CatCaptureFormat iFormat,
                | CATBSTR iFile)
                | 
                |     Captures the actually displayed scene by the viewer as an image, and stores
                |     the image in a file. Clipped parts of the scene are also clipped in the
                |     captured image. Images can be captured as CGM, EMF, TIFF, TIFF Greyscale, BMP,
                |     and JPEG images.
                | 
                |     Parameters:
                | 
                |         iFormat
                |             The format in which the image will be created 
                |         iFile
                |             The full pathname of the file into which you want to store the
                |             captured image 
                |         Example:
                |             This example captures the displayed part of the MyViewer viewer as
                |             a BMP image, and stores it in the e:\\MyImage.bmp
                |             file.
                | 
                |              MyViewer.CaptureToFile catCaptureFormatBMP, "e:\\MyImage.bmp"

        :param int i_format: enum cat_capture_format
        :param str i_file:
        :rtype: None
        """
        return self.viewer.CaptureToFile(i_format, i_file)

    def get_background_color(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetBackgroundColor(CATSafeArrayVariant color)
                | 
                |     Gets the viewer's background color. The color is expressed in the RGB color
                |     mode, as a triplet of coordinates ranging from 0 to 1 for the red, green, and
                |     blue colors respectively.
                | 
                |     Example:
                |         This example gets the background color of the MyViewer
                |         viewer.
                | 
                |          Dim color(2)
                |          MyViewer.GetBackgroundColor color

        :rtype: tuple
        """
        vba_function_name = 'get_background_color'
        vba_code = """
        Public Function get_background_color(viewer)
            Dim color (2)
            viewer.GetBackgroundColor color
            get_background_color = color
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_viewer_2d(self) -> 'Viewer2D':
        from pycatia.in_interfaces.viewer_2d import Viewer2D

        return Viewer2D(self.viewer)

    def create_viewer_3d(self) -> 'Viewer3D':
        from pycatia.in_interfaces.viewer_3d import Viewer3D

        return Viewer3D(self.viewer)

    def new_camera(self) -> Camera:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func NewCamera() As Camera
                | 
                |     Creates a new camera from the viewpoint of the viewer.
                | 
                |     Example:
                |         This example creates the MyCamera new camera by using the current
                |         viewpoint of the MyViewer viewer.
                | 
                |          Dim MyCamera As Camera
                |          Set MyCamera = MyViewer.NewCamera()

        :rtype: Camera
        """
        return Camera(self.viewer.NewCamera())

    def put_background_color(self, color: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutBackgroundColor(CATSafeArrayVariant color)
                | 
                |     Sets the viewer's background color. The color is expressed in the RGB color
                |     mode, as a triplet of coordinates ranging from 0 to 1 for the red, green, and
                |     blue colors respectively.
                | 
                |     Example:
                |         This example sets the background color of the MyViewer viewer to blue,
                |         that is the color with (0.,0.,1.) coordinates
                | 
                |          MyViewer.PutBackgroundColor Array(0, 0, 1)

        :param tuple color:
        :rtype: None
        """
        return self.viewer.PutBackgroundColor(color)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_background_color'
        # # vba_code = """
        # # Public Function put_background_color(viewer)
        # #     Dim color (2)
        # #     viewer.PutBackgroundColor color
        # #     put_background_color = color
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def reframe(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Reframe()
                | 
                |     Reframes the viewer's contents (Fits all in). Reframing means that the
                |     viewer's contents is zoomed in or out to enable every object of the scene to be
                |     displayed in such a way that most of the space available in the viewer is used,
                |     just leaving a thin empty strip around the scene.
                | 
                |     Example:
                |         This example reframes the contents of the MyViewer
                |         viewer.
                | 
                |          MyViewer.Reframe()

        :rtype: None
        """
        return self.viewer.Reframe()

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Update()
                | 
                |     Updates the viewer's contents. Since the viewer is not automatically
                |     updated after a viewpoint modification (for performance reasons), it must be
                |     explicitely redrawn when needed.
                | 
                |     Example:
                |         This example updates the contents of the MyViewer
                |         viewer.
                | 
                |          MyViewer.Update()

        :rtype: None
        """
        return self.viewer.Update()

    def zoom_in(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ZoomIn()
                | 
                |     Zooms in the viewer's contents.
                | 
                |     Example:
                |         This example zooms in the contents of the MyViewer
                |         viewer.
                | 
                |          MyViewer.ZoomIn()

        :rtype: None
        """
        return self.viewer.ZoomIn()

    def zoom_out(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ZoomOut()
                | 
                |     Zooms out the viewer's contents.
                | 
                |     Example:
                |         This example zooms out the contents of the MyViewer
                |         viewer.
                | 
                |          MyViewer.ZoomOut()

        :rtype: None
        """
        return self.viewer.ZoomOut()

    def __repr__(self):
        return f'Viewer(name="{self.name}")'
