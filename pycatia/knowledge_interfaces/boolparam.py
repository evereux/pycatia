#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.knowledge_interfaces.enumparam import EnumParam


class BoolParam(EnumParam):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the boolean parameter.The following example shows how to
                | create it:Dim CATDocs As Documents  Set CATDocs      = CATIA.Documents
                | Dim part1 As Document  Set part1        = CATDocs.Add("CATPart")
                | Dim availability As BooleanParam  Set availability =
                | part1.Parameters.CreateBoolean("availability", True)

    """

    def __init__(self, com_boolean_parameter):
        super().__init__(com_boolean_parameter)

    def __repr__(self):
        return f'BoolParam(name="{self.name}". value="{self.value}")'
