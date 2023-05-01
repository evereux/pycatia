#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PageSetup(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PageSetup
                | 
                | Represents the page setup.
                | The page setup is the object that stores data which defines how your documents
                | and images are actually printed on paper. This data includes namely the paper
                | size, the orientation, the bottom, top, right, and left margins, the zoom
                | factor, the banner, and the printing quality.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.page_setup = com_object

    def __repr__(self):
        return f'PageSetup(name="{ self.name }")'
