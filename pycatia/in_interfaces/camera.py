#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class Camera(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Camera
                | 
                | Represents the camera.
                | The camera is the object that stores a viewpoint saved from a viewer at a given
                | moment using the Viewer.NewCamera method of the Viewer object. The viewpoint
                | stored in the camera can then be applied to another viewer to display the
                | document in this viewer according to this viewpoint.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.camera = com_object

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Type() As CatCameraType (Read Only)
                | 
                |     Returns the camera's type.
                | 
                |     Example:
                |         This example retrieves in MyCameraType the type of the MyCamera 3D
                |         camera and applies the viewpoint stored in this camera to the active
                |         viewer.
                | 
                |          MyCameraType = MyCamera.Type
                |          CATIA.ActiveWindow.ActiveViewer.Viewpoint3D = MyCamera.Viewpoint3D
                |          
                | 
                |         The value returned by the Type property in MyCameraType is catCamera3D

        :return: enum cat_camera_type
        :rtype: int
        """

        return self.camera.Type

    def __repr__(self):
        return f'Camera(name="{self.name}")'
