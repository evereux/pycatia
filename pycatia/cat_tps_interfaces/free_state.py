#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class FreeState(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FreeState
                | 
                | Interface for accessing Free State modifier on a TPS.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.free_state = com_object

    @property
    def modifier(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Modifier() As CATBSTR
                | 
                |     Retrieves Free State modifier.

        :rtype: str
        """

        return self.free_state.Modifier

    @modifier.setter
    def modifier(self, value: str):
        """
        :param str value:
        """

        self.free_state.Modifier = value

    def __repr__(self):
        return f'FreeState(name="{ self.name }")'
