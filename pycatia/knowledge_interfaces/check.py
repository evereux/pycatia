#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .relation import Relation


class Check(Relation):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the check relation.The following example shows how to
                | create a check which checks if a given mass is less than 10kg. The
                | mass should be defined previously:

    """

    def __init__(self, relation_com_object):
        super().__init__(relation_com_object)
        self.check = relation_com_object

    @property
    def diagnosis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Diagnosis
                | o Property Diagnosis(    ) As boolean
                | 
                | Returns the check diagnosis. True if the condition of the check is
                | verified. False otherwise.


                | Parameters:


        """
        return self.check.Diagnosis

    @property
    def severity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Severity
                | o Property Severity(    ) As long
                | 
                | Returns or sets the check severity. The severity is the way the check
                | will manifest itself:             Silent (1)Information (2)Warning (3)


                | Parameters:


        """
        return self.check.Severity
