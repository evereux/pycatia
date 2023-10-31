#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter


class EnumParam(Parameter):

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
                |                         EnumParam
                | 
                | Represents the enum parameter.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.enum_param = com_object

    @property
    def value_enum(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ValueEnum() As CATBSTR
                | 
                |     Returns or sets the value of the EnumParameter object. Units are expressed
                |     in the IS unit system, except for lengths expressed in millimeters, and angles
                |     expressed in decimal degrees.
                | 
                |     Example:
                |         This example sets the param1 value to 1 if its value is greater than
                |         2.5:
                | 
                |          If (density.Value > 2.5)  Then
                |              density.Value = 1
                |          End If

        :rtype: str
        """

        return self.enum_param.ValueEnum

    @value_enum.setter
    def value_enum(self, value: str):
        """
        :param str value:
        """

        self.enum_param.ValueEnum = value

    def __repr__(self):
        return f'EnumParam(name="{ self.name }")'
