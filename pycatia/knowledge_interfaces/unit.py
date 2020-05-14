#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.base_object import AnyObject


class Unit(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents CATIAUnit object.This interface allows convertion.

    """

    def __init__(self, unit_com_object):
        super().__init__(unit_com_object)
        self.unit = unit_com_object

    @property
    def magnitude(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Magnitude
                | o Property Magnitude(    ) As CATBSTR
                | 
                | Returns the magnitude associated to the unit.

        """
        return self.unit.Magnitude

    @property
    def symbol(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Symbol
                | o Property Symbol(    ) As CATBSTR
                | 
                | Returns the symbol associated to the unit.


                | Parameters:


        """
        return self.unit.Symbol

    def convert_from_mks(self, i_value_in_mks):
        """
        .. note::
            CAA V5 Visual Basic help

                | ConvertFromMKS
                | o Func ConvertFromMKS(    double    iValueInMKS) As double
                | 
                | Convert the initial value (expressed in MKS unit) in its equivalent in
                | the current unit.


                | Parameters:
                | iValueInThisUnit
                |    The initial value in MKS unit.
                |  
                |  oValueInMKS
                |    The final value in the current unit.


        """
        return self.unit.ConvertFromMKS(i_value_in_mks)

    def convert_from_storage_unit(self, i_value_in_storage_unit):
        """
        .. note::
            CAA V5 Visual Basic help

                | ConvertFromStorageUnit
                | o Func ConvertFromStorageUnit(    double    iValueInStorageUnit) As double
                | 
                | Convert the initial value (expressed in storage unit) in its
                | equivalent in the current unit.


                | Parameters:
                | iValueInStorageUnit
                |    The initial value in storage unit.
                |  
                |  oValueInThisUnit
                |    The final value in the current unit.


        """
        return self.unit.ConvertFromStorageUnit(i_value_in_storage_unit)

    def convert_to_mks(self, i_value_in_this_unit):
        """
        .. note::
            CAA V5 Visual Basic help

                | ConvertToMKS
                | o Func ConvertToMKS(    double    iValueInThisUnit) As double
                | 
                | Convert the initial value in its equivalent in MKS unit.


                | Parameters:
                | iValueInThisUnit
                |    The initial value in the current unit.
                |  
                |  oValueInMKS
                |    The final value in the corresponding MKS unit.


        """
        return self.unit.ConvertToMKS(i_value_in_this_unit)

    def convert_to_storage_unit(self, i_value_in_this_unit):
        """
        .. note::
            CAA V5 Visual Basic help

                | ConvertToStorageUnit
                | o Func ConvertToStorageUnit(    double    iValueInThisUnit) As double
                | 
                | Convert the initial value in its equivalent in storage unit.


                | Parameters:
                | iValueInThisUnit
                |    The initial value in the current unit.
                |  
                |  oValueInStorageUnit
                |    The final value in the corresponding storage unit.


        """
        return self.unit.ConvertToStorageUnit(i_value_in_this_unit)

    def __repr__(self):
        return f'Unit()'
