#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ControlledRadius(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ControledRadius
                | 
                | Interface for accessing Controled Radius modifier on a linear TPS (ASME norm
                | only).
                | This interface is exposed only by radius linear TPS.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.controlled_radius = com_object

    @property
    def modifier(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Modifier() As CATBSTR (Read Only)
                | 
                |     Retrieves Controled Radius modifier.

        :rtype: str
        """

        return self.controlled_radius.Modifier

    def __repr__(self):
        return f'ControlledRadius(name="{self.name}")'
