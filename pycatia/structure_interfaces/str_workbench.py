#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.workbench import Workbench
from pycatia.structure_interfaces.str_compute_services import StrComputeServices


class StrWorkbench(Workbench):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Workbench
                |                         StrWorkbench
                | 
                | Represents the structure workbench object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.str_workbench = com_object

    @property
    def str_compute_services(self) -> StrComputeServices:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StrComputeServices() As StrComputeServices (Read
                | Only)
                | 
                |     Returns the compute services object. It allows you to calculate some
                |     properties on the structure objects.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim services As StrComputeServices
                |          Set services = workbench_1.StrComputeServices

        :rtype: StrComputeServices
        """

        return StrComputeServices(self.str_workbench.StrComputeServices)

    def __repr__(self):
        return f'StrWorkbench(name="{self.name}")'
