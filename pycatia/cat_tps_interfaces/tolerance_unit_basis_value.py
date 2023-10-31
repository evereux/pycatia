#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ToleranceUnitBasisValue(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ToleranceUnitBasisValue
                | 
                | Interface for accessing values of the tolerance unit basis on a
                | TPS.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tolerance_unit_basis_value = com_object

    def set_values(self, i_value1: float, i_value2: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetValues(double iValue1,
                | double iValue2)
                | 
                |     Set tolerance unit basis values (in millimeters).
                | 
                |     Parameters:
                | 
                |         oValue1
                |             Positive or equal to -1 which means not valuated. 
                |         oValue2
                |             Positive or equal to -1 which means not valuated.

        :param float i_value1:
        :param float i_value2:
        :rtype: None
        """
        return self.tolerance_unit_basis_value.SetValues(i_value1, i_value2)

    def values(self, o_value1: float, o_value2: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Values(double oValue1,
                | double oValue2)
                | 
                |     Retrieves tolerance unit basis values (in millimeters).
                | 
                |     Parameters:
                | 
                |         oValue1
                |             Positive or equal to -1 which means not valuated. 
                |         oValue2
                |             Positive or equal to -1 which means not valuated.

        :param float o_value1:
        :param float o_value2:
        :rtype: None
        """
        return self.tolerance_unit_basis_value.Values(o_value1, o_value2)

    def __repr__(self):
        return f'ToleranceUnitBasisValue(name="{ self.name }")'
