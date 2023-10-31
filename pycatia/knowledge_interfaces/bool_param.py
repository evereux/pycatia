#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.enum_param import EnumParam


class BoolParam(EnumParam):
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
                |                         KnowledgeInterfaces.EnumParam
                |                             BoolParam
                | 
                | Represents the boolean parameter.
                | The following example shows how to create it:
                | 
                |   Dim CATDocs As Documents
                |   Set CATDocs      = CATIA.Documents
                |   Dim part1 As Document
                |   Set part1        = CATDocs.Add("CATPart")
                |   Dim availability As BooleanParam
                |   Set availability = part1.Parameters.CreateBoolean("availability", True)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.bool_param = com_object

    @property
    def value(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Value() As boolean
                | 
                |     Returns or sets the value of the boolean parameter.
                | 
                |     Example:
                |         This example sets the availability boolean parameter value to True if
                |         its value is False:
                | 
                |          If (availability.Value = False)  Then
                |              availability.Value = True
                |          End If

        :rtype: bool
        """

        return self.bool_param.Value

    @value.setter
    def value(self, value: bool):
        """
        :param bool value:
        """

        self.bool_param.Value = value

    def __repr__(self):
        return f'BoolParam(name="{self.name}")'
