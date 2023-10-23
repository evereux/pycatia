#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_device_interfaces.basic_device import BasicDevice


class D5Device(BasicDevice):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBDeviceInterfaces.BasicDevice
                |                         D5Device
                | 
                | Interface representing a D5 Device.
                | 
                | Role: This interface is used to interact with devices that are available in the
                | Device Building workbench. This interfaces is derived from BasicDevice to
                | support specific properties for D5 devices.
                | The following code snippet can be used to obtain a device in a CATProduct
                | document.
                | 
                |    Dim objDevice As BasicDevice
                |    set objDevice = CATIA.ActiveDocument.Product.GetTechnologicalObject("BasicDevice")
                |    Dim objD5Device as D5Device
                |    Set objD5Device = objDevice
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.d5_device = com_object

    def get_linked_device_file(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLinkedDeviceFile() As CATBSTR
                | 
                |     Get the Linked D5 Device File.
                | 
                |     Parameters:
                | 
                |         oFileName
                |             This will contain the full path to the file (file name and path) to
                |             the D5 device file.

        :rtype: str
        """
        return self.d5_device.GetLinkedDeviceFile()

    def __repr__(self):
        return f'D5Device(name="{self.name}")'
