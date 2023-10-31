#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class TPSParallelOnScreen(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TPSParallelOnScreen
                | 
                | Interface for Parallel On Screen.
                | TPS for Technological Product Specifications.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tps_parallel_on_screen = com_object

    @property
    def parallel_on_screen(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ParallelOnScreen() As boolean
                | 
                |     Retrieves the Parallel On Screen for the annotation.

        :rtype: bool
        """

        return self.tps_parallel_on_screen.ParallelOnScreen

    @parallel_on_screen.setter
    def parallel_on_screen(self, value: bool):
        """
        :param bool value:
        """

        self.tps_parallel_on_screen.ParallelOnScreen = value

    @property
    def zoomable(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Zoomable() As boolean
                | 
                |     Retrieves the Zoomable for the annotation.

        :rtype: bool
        """

        return self.tps_parallel_on_screen.Zoomable

    @zoomable.setter
    def zoomable(self, value: bool):
        """
        :param bool value:
        """

        self.tps_parallel_on_screen.Zoomable = value

    def __repr__(self):
        return f'TpsParallelOnScreen(name="{self.name}")'
