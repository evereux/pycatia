#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.set_of_equation import SetOfEquation


class ConstraintSatisfaction(SetOfEquation):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.KnowledgeObject
                |                        KnowledgeInterfaces.KnowledgeActivateObject
                |                             KnowledgeInterfaces.Relation
                |                                KnowledgeInterfaces.SetOfEquation
                |                                     ConstraintSatisfaction
                | 
                | Represents the set of equation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.constraint_satisfaction = com_object

    def solve(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Solve()
                | 
                |     Solves the constraint satisfaction problem.

        :rtype: None
        """
        return self.constraint_satisfaction.Solve()

    def __repr__(self):
        return f'ConstraintSatisfaction(name="{ self.name }")'
