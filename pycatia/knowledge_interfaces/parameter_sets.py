#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.knowledge_interfaces.parameter_set import ParameterSet
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ParameterSets(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ParameterSets
                | 
                | Represents a collection of parameter sets.
                | The ParameterSet object is a neutral object that contains parameters, like the
                | Parameters node in the specification tree.
                | 
                | The following example shows how to retrieve it on a part:
                | 
                |  Dim CATDocs As Documents
                |  Set CATDocs = CATIA.Documents
                |  Dim part1 As Document
                |  Set part1   = CATDocs.Add("CATPart")
                |  Dim parameters1 As Parameters
                |  Set parameters1 = part1.Part.Parameters
                |  Dim ParameterSet1 As ParameterSet
                |  Set ParameterSet1 = parameters1.RootParameterSet
                |  Dim parameterSets1 As ParameterSets
                |  Set parameterSets1 = parameterSet1.ParameterSets
                |  
                | 
                | This collection is not a collection of all parameter sets of a document, but a
                | collection of all parameter sets in the current parameter set.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ParameterSet)
        self.parameter_sets = com_object

    def create_set(self, i_name: str) -> ParameterSet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateSet(CATBSTR iName) As ParameterSet
                | 
                |     Creates a set of parameters and appends it to the parameter set which
                |     corresponds to this collection.

        :param str i_name:
        :rtype: ParameterSet
        """
        return ParameterSet(self.parameter_sets.CreateSet(i_name))

    def item(self, i_index: cat_variant) -> ParameterSet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As ParameterSet
                | 
                |     Returns a parameter set using its index or its name from the ParameterSets
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the parameter set to retrieve from the
                |             collection of parameter sets. As a numerics, this index is the rank of the
                |             parameter set in the collection. The index of the first parameter set in the
                |             collection is 1, and the index of the last parameter set is Count. As a string,
                |             it is the name you assigned to the parameter set using the
                |             
                | 
                |         AnyObject.Name property . 
                |     Example:
                |         This example retrieves the parameter set named "Parameters.1" in the
                |         parameterSets collection:
                | 
                |          Set theSet = parameterSets.Item("Parameters.1")

        :param cat_variant i_index:
        :rtype: ParameterSet
        """
        return ParameterSet(self.parameter_sets.Item(i_index))

    def __getitem__(self, n: int) -> ParameterSet:
        if (n + 1) > self.count:
            raise StopIteration

        return ParameterSet(self.parameter_sets.Item(n + 1))

    def __iter__(self) -> Iterator[ParameterSet]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'ParameterSets(name="{self.name}")'
