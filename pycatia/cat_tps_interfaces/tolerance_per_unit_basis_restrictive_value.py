#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class TolerancePerUnitBasisRestrictiveValue(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TolerancePerUnitBasisRestrictiveValue
                | 
                | Interface for accessing tolerance per unit basis restrictive value on a
                | TPS.
                | (ASME norm only)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tolerance_per_unit_basis_restrictive_value = com_object

    @property
    def value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Value() As double
                | 
                |     Retrieves value (in millimeters).
                | 
                |     Parameters:
                | 
                |         oValue
                |             Positive or equal to -1 which means not valuated.

        :rtype: float
        """

        return self.tolerance_per_unit_basis_restrictive_value.Value

    @value.setter
    def value(self, value: float):
        """
        :param float value:
        """

        self.tolerance_per_unit_basis_restrictive_value.Value = value

    def __repr__(self):
        return f'TolerancePerUnitBasisRestrictiveValue(name="{ self.name }")'
