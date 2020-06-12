#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.knowledge_interfaces.optimization import Optimization
from pycatia.knowledge_interfaces.set_of_equation import SetOfEquation
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection


class Optimizations(Collection):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Optimizations
                | 
                | Represents a collection of optimization features.
                | 
                | See also:
                |     Optimization
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Optimization)
        self.optimizations = com_object

    def create_constraints_satisfaction(self, i_name, i_comment, i_formula_body):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateConstraintsSatisfaction(CATBSTR iName,
                | CATBSTR iComment,
                | CATBSTR iFormulaBody) As SetOfEquation
                | 
                |     Returns a set of equations.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the set of equations. 
                |         iComment
                |             The comment of the set of equations. 
                |         iFormulaBody
                |             The body of the set of equations " a==b+4; c ≤
                |             90".

        :param str i_name:
        :param str i_comment:
        :param str i_formula_body:
        :return: SetOfEquation
        """
        return SetOfEquation(self.optimizations.CreateConstraintsSatisfaction(i_name, i_comment, i_formula_body))

    def create_optimization(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateOptimization() As Optimization
                | 
                |     Creates an empty optimization.
                |     This optimization cannot be used while its properties have not been set.

        :return: Optimization
        """
        return Optimization(self.optimizations.CreateOptimization())

    def item(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As AnyObject
                | 
                |     Retrieves an optimization using its index or its name from the
                |     Optimizations collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the item (optimization or
                |             constraintSatisfaction) to retrieve from the collection of optimizations. As a
                |             numerics, this index is the rank of the item in the collection. The index of
                |             the first item in the collection is 1, and the index of the last item is Count.
                |             As a string, it is the name you assigned to the item using the
                |             
                | 
                |         AnyObject.Name property or when changing the item name by the property
                |         panel. 
                |     Returns:
                |         either the retrieved optimization or the retreived
                |         constraintSatisfaction 
                |     Example:
                |         This example retrieves the last item (optimization or
                |         constraintSatisfaction) in the optimizations
                |         collection.
                | 
                |          Set lastItem = optimizations.Item(optimizations.Count)

        :param CATVariant i_index:
        :return: AnyObject
        """
        return AnyObject(self.optimizations.Item(i_index))

    def __repr__(self):
        return f'Optimizations(name="{self.name}")'
