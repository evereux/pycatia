#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .dimension import Dimension


class Angle(Dimension):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the angle parameter.The following example shows how to
                | create it:Dim CATDocs As Documents Set CATDocs = CATIA.Documents Dim
                | part1 As Document Set part1   = CATDocs.Add("CATPart") Dim angle1 As
                | Angle Set angle1  = part1.Parameters.CreateDimension("angle1",
                | "ANGLE", 40.)

    """

    def __init__(self, com_dimension_parameter):
        super().__init__(com_dimension_parameter)
        self.angle = com_dimension_parameter

    def __repr__(self):
        return f'Angle()'

