#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.cat_tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen


class Roughness(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Roughness
                | 
                | Interface to manage Roughness TPS.
                | TPS for Technological Product Specifications.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.roughness = com_object

    @property
    def applicability(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Applicability() As short
                | 
                |     Retrieves or sets roughness applicability.

        :rtype: int
        """

        return self.roughness.Applicability

    @applicability.setter
    @applicability.setter
    def applicability(self, value: int):
        """
        :param int value:
        """

        self.roughness.Applicability = value

    @property
    def obtention(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Obtention() As short
                | 
                |     Retrieves or sets roughness obtention mode.

        :rtype: int
        """

        return self.roughness.Obtention

    @obtention.setter
    def obtention(self, value: int):
        """
        :param int value:
        """

        self.roughness.Obtention = value

    def field(self, i_index: int) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Field(short iIndex) As CATBSTR
                | 
                |     Retrieves roughness field.
                | 
                |                                           Field 4
                |                           Field 1     ------------------
                |                                      /         (Field 9)
                |                           Field 2   /
                |                                    / (Field 8)  Field 5
                |                               \\   /
                |                     Field 3    \\ /    Field 7   Field 6
                |      
                |       Pour le champs 7 les lettres autorisees sont :
                |       M, C, R, P, X, = ,L (symbole perpendicularite de la DSES)
                |      
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Field index, from 1 to 9 from V5R13 (Fields 8 and 9 added). from 1
                |             to 7 before V5R13 
                |         oField
                |             The contain of the iIndex field.

        :param int i_index:
        :rtype: str
        """
        return self.roughness.Field(i_index)

    def set_field(self, i_index: int, i_field: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetField(short iIndex,
                | CATBSTR iField)
                | 
                |     Set roughness field.
                | 
                |                                           Field 4
                |                           Field 1     ------------------
                |                                      /         (Field 9)
                |                           Field 2   /
                |                                    / (Field 8)  Field 5
                |                               \\   /
                |                     Field 3    \\ /    Field 7   Field 6
                |      
                |       Pour le champs 7 les lettres autorisees sont :
                |       M, C, R, P, X, = ,L (symbole perpendicularite de la DSES)
                |      
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Field index, from 1 to 9 from V5R13 (Fields 8 and 9 added). from 1
                |             to 7 before V5R13 
                |         iField
                |             The contain of the iIndex field.

        :param int i_index:
        :param str i_field:
        :rtype: None
        """
        return self.roughness.SetField(i_index, i_field)

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func TPSParallelOnScreen() As TPSParallelOnScreen
                | 
                |     Gets the annotation on TPSParallelOnScreen interface.

        :rtype: TPSParallelOnScreen
        """
        return TPSParallelOnScreen(self.roughness.TPSParallelOnScreen())

    def __repr__(self):
        return f'Roughness(name="{self.name}")'
