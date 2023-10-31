#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_activities import ManufacturingActivities
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingProcess(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingProcess
                | 
                | A ManufacturingProcess for a Manufacturing Document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_process = com_object

    @property
    def setups(self) -> ManufacturingActivities:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Setups() As MfgActivities (Read Only)
                | 
                |     Give the List of Setups linked to a Manufacturing Process.
                | 
                |     Example:
                |         The following example returns the list of Setups SetupsList linked to
                |         the manufacturing Process CurrentProcess
                | 
                |          Set SetupsList = CurrentProcess.Setups

        :rtype: MfgActivities
        """

        return ManufacturingActivities(self.manufacturing_process.Setups)

    def __repr__(self):
        return f'ManufacturingProcess(name="{self.name}")'
