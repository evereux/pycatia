#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.knowledge_interfaces.unit import Unit


class Dimension(RealParam):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.Parameter
                |                         KnowledgeInterfaces.RealParam
                |                             Dimension
                | 
                | Represents the dimension parameter.
                | It is an abstract object which is not intended to be created as such, but from
                | which the length and angle parameters derive.
                | 
                | See also:
                |     Length, Angle
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dimension = com_object

    @property
    def unit(self) -> Unit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Unit() As Unit (Read Only)
                | 
                |     Returns the unit used for this dimension object.

        :rtype: Unit
        """

        return Unit(self.dimension.Unit)

    def value_as_string2(self, i_nb_decimals: int, i_show_trailing_zeros: bool) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func ValueAsString2(long iNbDecimals,
                | boolean iShowTrailingZeros) As CATBSTR
                | 
                |     Gets the value of the parameter as a string, with a given
                |     precision.
                | 
                |     Parameters:
                | 
                |         iNbDecimals
                |             the maximum number of decimal places to use to generate the string
                |             (minimum 0, maximum 9) 
                |         iShowTrailingZeros
                |             this argument says if trailing zeros have to be shown
                |             
                | 
                |     Example:
                |         This example gets the value of the existing dimension parameter and
                |         shows it in a message box
                | 
                |          Dim str
                |          str = dimension.ValueAsString;
                |          MessageBox str

        :param int i_nb_decimals:
        :param bool i_show_trailing_zeros:
        :rtype: str
        """
        return self.dimension.ValueAsString2(i_nb_decimals, i_show_trailing_zeros)

    def __repr__(self):
        return f'Dimension(name="{ self.name }")'
