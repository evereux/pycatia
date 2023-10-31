#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class Unit(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Unit
                | 
                | Represents CATIAUnit object.
                | This interface allows convertion.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.unit = com_object

    @property
    def magnitude(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Magnitude() As CATBSTR (Read Only)
                | 
                |     Returns the magnitude associated to the unit.

        :rtype: str
        """

        return self.unit.Magnitude

    @property
    def symbol(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Symbol() As CATBSTR (Read Only)
                | 
                |     Returns the symbol associated to the unit.

        :rtype: str
        """

        return self.unit.Symbol

    def convert_from_mks(self, i_value_in_mks: float) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func ConvertFromMKS(double iValueInMKS) As double
                | 
                |     Convert the initial value (expressed in MKS unit) in its equivalent in the
                |     current unit.
                | 
                |     Parameters:
                | 
                |         iValueInThisUnit
                |             The initial value in MKS unit. 
                |         oValueInMKS
                |             The final value in the current unit.

        :param float i_value_in_mks:
        :rtype: float
        """
        return self.unit.ConvertFromMKS(i_value_in_mks)

    def convert_from_storage_unit(self, i_value_in_storage_unit: float) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func ConvertFromStorageUnit(double iValueInStorageUnit) As
                | double
                | 
                |     Convert the initial value (expressed in storage unit) in its equivalent in
                |     the current unit.
                | 
                |     Parameters:
                | 
                |         iValueInStorageUnit
                |             The initial value in storage unit. 
                |         oValueInThisUnit
                |             The final value in the current unit.

        :param float i_value_in_storage_unit:
        :rtype: float
        """
        return self.unit.ConvertFromStorageUnit(i_value_in_storage_unit)

    def convert_to_mks(self, i_value_in_this_unit: float) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func ConvertToMKS(double iValueInThisUnit) As double
                | 
                |     Convert the initial value in its equivalent in MKS unit.
                | 
                |     Parameters:
                | 
                |         iValueInThisUnit
                |             The initial value in the current unit. 
                |         oValueInMKS
                |             The final value in the corresponding MKS unit.

        :param float i_value_in_this_unit:
        :rtype: float
        """
        return self.unit.ConvertToMKS(i_value_in_this_unit)

    def convert_to_storage_unit(self, i_value_in_this_unit: float) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func ConvertToStorageUnit(double iValueInThisUnit) As
                | double
                | 
                |     Convert the initial value in its equivalent in storage
                |     unit.
                | 
                |     Parameters:
                | 
                |         iValueInThisUnit
                |             The initial value in the current unit. 
                |         oValueInStorageUnit
                |             The final value in the corresponding storage unit.

        :param float i_value_in_this_unit:
        :rtype: float
        """
        return self.unit.ConvertToStorageUnit(i_value_in_this_unit)

    def __repr__(self):
        return f'Unit(name="{ self.name }")'
