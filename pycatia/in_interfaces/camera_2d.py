#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.camera import Camera
from pycatia.in_interfaces.viewpoint_2d import Viewpoint2D


class Camera2D(Camera):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Camera
                |                         Camera2D
                | 
                | Represents a 2D camera.
                | The 2D camera stores a 2D viewpoint, that is a Viewpoint2D
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.camera_2d = com_object

    @property
    def viewpoint2_d(self) -> Viewpoint2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Viewpoint2D() As Viewpoint2D
                | 
                |     Returns or sets the 2D viewpoint of a 2D camera.
                | 
                |     Example:
                |         Assume the active window is a SpecsAndGeomWindow object. This example
                |         retrieves the Viewpoint2D of the SpecsViewer and creates from it a Camera2D you
                |         handle using the MyCamera variable. Then the camera zoom is set to 2, and the
                |         camera's viewpoint is assigned to the SpecsViewer.
                | 
                |          Dim MyCamera As Camera
                |          Set MyCamera = CATIA.ActiveWindow.SpecsViewer.NewCamera()
                |          MyCamera.Viewpoint2D.Zoom = 2
                |          CATIA.ActiveWindow.SpecsViewer.Viewpoint2D = MyCamera.Viewpoint2D

        :rtype: Viewpoint2D
        """

        return Viewpoint2D(self.camera_2d.Viewpoint2D)

    @viewpoint2_d.setter
    def viewpoint2_d(self, value: Viewpoint2D):
        """
        :param Viewpoint2D value:
        """

        self.camera_2d.Viewpoint2D = value

    def __repr__(self):
        return f'Camera2D(name="{self.name}")'
