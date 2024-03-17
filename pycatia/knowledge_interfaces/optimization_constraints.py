#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.knowledge_interfaces.optimization_constraint import OptimizationConstraint
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class OptimizationConstraints(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OptimizationConstraints
                | 
                | Represents a collection of Optimization Constraint.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.optimization_constraints = com_object

    def add_constraint(self, constraint_expression: str) -> OptimizationConstraint:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func AddConstraint(CATBSTR constraintExpression) As
                | OptimizationConstraint
                | 
                |     Adds a optimization constraint. This parameter must not be read only.

        :param str constraint_expression:
        :rtype: OptimizationConstraint
        """
        return OptimizationConstraint(self.optimization_constraints.AddConstraint(constraint_expression))

    def item(self, i_index: cat_variant) -> OptimizationConstraint:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As OptimizationConstraint
                | 
                |     Returns an optimization constraint using its index or its name from the
                |     optimization constraints collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the optimization constraint to retrieve
                |             from the collection of optimization constraints. As a numerics, this index is
                |             the rank of the optimization constraint in the collection. The index of the
                |             first optimization constraint in the collection is 1, and the index of the last
                |             optimization constraint is Count. As a string, it is the name you assigned to
                |             the optimization constraint using the 
                | 
                |         AnyObject.Name property or when changing the optimization constraint
                |         name by the property panel. 
                |     Returns:
                |         The retrieved optimization constraint 
                |     Example:
                |         This example retrieves the last optimization constraint in the
                |         optimization constraints collection.
                | 
                |          Set lastConstraint = constraints.Item(constraints.Count)

        :param cat_variant i_index:
        :rtype: OptimizationConstraint
        """
        return OptimizationConstraint(self.optimization_constraints.Item(i_index))

    def remove_constraint(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveConstraint(CATVariant iIndex)
                | 
                |     Removes a given optimization constraint using its index or its name from
                |     the optimization constraints collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             the name of the constraint if argument is a string or the index of
                |             the constraint if argument is an integer.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.optimization_constraints.RemoveConstraint(i_index)

    def __getitem__(self, n: int) -> OptimizationConstraint:
        if (n + 1) > self.count:
            raise StopIteration

        return OptimizationConstraint(self.optimization_constraints.Item(n + 1))

    def __iter__(self) -> Iterator[OptimizationConstraint]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'OptimizationConstraints(name="{self.name}")'
