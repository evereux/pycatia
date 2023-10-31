#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.factory import Factory
from pycatia.cat_tps_interfaces.capture import Capture


class CaptureFactory(Factory):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Factory
                |                         CaptureFactory
                | 
                | Interface for the Capture Factory.
                | This factory is implemented on the Set object. All the created Captures are
                | added to the Set from which this interface is retrieved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.capture_factory = com_object

    def create_capture(self) -> Capture:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateCapture() As Capture
                | 
                |     Create a Capture.
                | 
                |     Parameters:
                | 
                |         oCapture
                |             The new created Capture.

        :rtype: Capture
        """
        return Capture(self.capture_factory.CreateCapture())

    def __repr__(self):
        return f'CaptureFactory(name="{self.name}")'
