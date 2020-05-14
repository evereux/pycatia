#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .realparam import RealParam
from .unit import Unit


class Dimension(RealParam):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the dimension parameter.It is an abstract object which is
                | not intended to be created as such, but from which the length and
                | angle parameters derive.

    """

    def __init__(self, com_dimension_parameter):
        super().__init__(com_dimension_parameter)
        self.dimension = com_dimension_parameter

    @property
    def unit(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Unit
                | o Property Unit(    ) As Unit
                | 
                | Returns the unit used for this dimension object.


                | Parameters:


        """
        return Unit(self.dimension.Unit)

    def value_as_string2(self, i_nb_decimals, i_show_trailing_zeros):
        """
        .. note::
            CAA V5 Visual Basic help

                | ValueAsString2
                | o Func ValueAsString2(    long    iNbDecimals,
                |                           boolean    iShowTrailingZeros) As CATBSTR
                | 
                | Gets the value of the parameter as a string, with a given precision.


                | Parameters:
                | iNbDecimals
                |  the maximum number of decimal places to use to generate the string (minimum 0, maximum 9)
                |  
                |  iShowTrailingZeros
                |  this argument says if trailing zeros have to be shown


                | Examples:
                | 
                | 
                | This example gets the value of the existing dimension parameter
                | and shows it in a message box
                | 
                | Dim str
                | str = dimension.ValueAsString;
                | MessageBox str
                | 
                | 
                | 
        """
        return self.dimension.ValueAsString2(i_nb_decimals, i_show_trailing_zeros)

    def __repr__(self):
        return f'Dimension(name:{self.name})'
