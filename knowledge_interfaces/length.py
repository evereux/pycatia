#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from .dimension import Dimension


class Length(Dimension):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the length parameter.The following example shows how to
                | create it:Dim CATDocs As Documents Set CATDocs = CATIA.Documents Dim
                | part1 As Document Set part1   = CATDocs.Add("CATPart")  Dim Width As
                | Length Set width   = part1.Part.Parameters.CreateDimension("width",
                | "LENGTH", 20.)By default the units are the default units of the IS of
                | units.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.length = com_object

    def __repr__(self):
        return f'Length(name="{self.name}")'
