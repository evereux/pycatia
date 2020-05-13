#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25


from .base_object import BaseKnowledge


class Formula(BaseKnowledge):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the formula relation.The following example shows how to
                | create a formula that computes the mass of a cuboid, given its
                | geometric dimensions and the density of the material it is made of:

    """

    def __init__(self, formula_com_object):
        super().__init__(formula_com_object)
        self.formula = formula_com_object

    def __repr__(self):
        return f'Formula(name="{self.name}")'
