#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .relation import Relation


class Rule(Relation):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the program relation.The following example shows how to
                | create a program that selects a  depth with respect to a mass value.
                | The depth and mass parameters should exist before the creation of the
                | program (also called Rule) object.

    """

    def __init__(self, rule_com_object):
        super().__init__(rule_com_object)
        self.rule = rule_com_object

    def __repr__(self):
        return 'Rule()'
