#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ABQInteraction(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQInteraction
                | 
                | Represents the base interface for Abaqus interaction objects.
                | Role: The ABQInteraction interface manages the common properties of any
                | interaction.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_interaction = com_object

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the type of the Interaction.
                | 
                |     Returns:
                |         The type of the Interaction.

        :rtype: str
        """

        return self.abq_interaction.Type

    def __repr__(self):
        return f'ABQInteraction(name="{self.name}")'
