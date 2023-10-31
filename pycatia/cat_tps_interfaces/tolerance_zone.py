#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ToleranceZone(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ToleranceZone
                | 
                | Interface for accessing tolerance zone informations of a TPS.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tolerance_zone = com_object

    @property
    def form(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Form() As CATBSTR
                | 
                |     Retrieves tolerance zone form.

        :rtype: str
        """

        return self.tolerance_zone.Form

    @form.setter
    def form(self, value: str):
        """
        :param str value:
        """

        self.tolerance_zone.Form = value

    @property
    def value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Value() As double
                | 
                |     Retrieves tolerance zone value (in millimeters).

        :rtype: float
        """

        return self.tolerance_zone.Value

    @value.setter
    def value(self, value: float):
        """
        :param float value:
        """

        self.tolerance_zone.Value = value

    def __repr__(self):
        return f'ToleranceZone(name="{ self.name }")'
