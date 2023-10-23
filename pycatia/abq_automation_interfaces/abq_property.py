#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ABQProperty(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQProperty
                | 
                | Represents the base interface for all Abaqus property objects.
                | Role: The ABQProperty interface manages the common attributes of any Abaqus
                | property.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_property = com_object

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the type of the property.
                | 
                |     Returns:
                |         The type of the property.

        :rtype: str
        """

        return self.abq_property.Type

    def __repr__(self):
        return f'ABQProperty(name="{self.name}")'
