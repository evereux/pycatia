#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.in_interfaces.camera import Camera
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Cameras(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Cameras
                | 
                | A collection of all the Camera objects currently attached to a Document
                | object.
                | A camera can be created using the Viewer.NewCamera method of the Viewer object.
                | The first seventh cameras of the collection are Camera3D objects and cannot be
                | modified or removed. They can just be retrieved and used "as is". They store
                | the following viewpoints whose sight direction is always toward the 3D-axis
                | system origin:
                | 
                | * iso
                |     The origin is on a line with (1,1,1) as components with positive
                |     coordinates 
                | * front
                |     The origin is on the x axis with a positive x coordinate 
                | * back
                |     The origin is on the x axis with a negative x coordinate 
                | * left
                |     The origin is on the y axis with a positive y coordinate 
                | * right
                |     The origin is on the y axis with a negative y coordinate 
                | * top
                |     The origin is on the z axis with a positive z coordinate 
                | * bottom
                |     The origin is on the z axis with a negative z coordinate 
                | 
                | The cameras of the Cameras collection are available using the dialog box
                | displayed by clicking the View->Defined Views menu.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Camera)
        self.cameras = com_object

    def item(self, i_index: cat_variant) -> Camera:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As Camera
                | 
                |     Returns a camera using its index or its name from the Cameras
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the camera to retrieve from the collection
                |             of cameras. As a numerics, this index is the rank of the camera in the
                |             collection. The index of the first camera in the collection is 1, and the index
                |             of the last camera is Count. As a string, it is the name you assigned to the
                |             camera using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved camera 
                |     Example:
                |         This example retrieves in ThisCamera the ninth camera, and in
                |         ThatCamera the camera named MyCamera in the camera collection of the active
                |         document.
                | 
                |          Dim ThisCamera As Camera
                |          Set ThisCamera = CATIA.ActiveDocument.Cameras.Item(9)
                |          Dim ThatCamera As Camera
                |          Set ThatCamera = CATIA.ActiveDocument.Cameras.Item("MyCamera")

        :param cat_variant i_index:
        :rtype: Camera
        """
        return Camera(self.cameras.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a camera from the Cameras collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the camera to remove from the collection
                |             of cameras. As a numerics, this index is the rank of the camera in the
                |             collection. The index of the first camera in the collection is 1, and the index
                |             of the last camera is Count. As a string, it is the name you assigned to the
                |             camera using the 
                | 
                |         AnyObject.Name property. You cannot remove the first seventh cameras in
                |         the collection. 
                | 
                | Example:
                |     The following example removes the tenth camera and the camera named
                |     CameraToBeRemoved in the camera collection of the active
                |     document.
                | 
                |      CATIA.ActiveDocument.Cameras.Remove(10)
                |      CATIA.ActiveDocument.Cameras.Remove("CameraToBeRemoved")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.cameras.Remove(i_index)

    def __getitem__(self, n: int) -> Camera:
        if (n + 1) > self.count:
            raise StopIteration

        return Camera(self.cameras.Item(n + 1))

    def __iter__(self) -> Iterator[Camera]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Cameras(name="{self.name}")'
