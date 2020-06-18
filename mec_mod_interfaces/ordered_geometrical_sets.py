#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.ordered_geometrical_set import OrderedGeometricalSet
from pycatia.system_interfaces.collection import Collection


class OrderedGeometricalSets(Collection):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OrderedGeometricalSets
                | 
                | A collection of the OrderedGeometricalSet objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.ordered_geometrical_sets = com_object

    def add(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add() As OrderedGeometricalSet
                | 
                |     Creates a new ordered geometrical set and adds it to the
                |     OrderedGeometricalSets collection. Thisordered geometrical set becomes the
                |     current one
                | 
                |     Returns:
                |         The created ordered geometrical set 
                |     Example:
                |         The following example creates a ordered geometrical set named
                |         newOrderedGeometricalSet in the ordered geometrical set collection of the
                |         rootPart part in the partDoc part document. NewPartBody becomes the in work
                |         object of partDoc.
                | 
                |          Set NewPartBody = rootPart.OrderedGeometricalSets.Add()

        :return: OrderedGeometricalSet
        """
        return OrderedGeometricalSet(self.ordered_geometrical_sets.Add())

    def item(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As OrderedGeometricalSet
                | 
                |     Returns a ordered geometrical set using its index or its name from the
                |     ordered geometrical set collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ordered geometrical set to retrieve
                |             from the collection of ordered geometrical sets. As a numerics, this index is
                |             the rank of the ordered geometrical set in the collection. The index of the
                |             first ordered geometrical set in the collection is 1, and the index of the last
                |             ordered geometrical set is Count. As a string, it is the name you assigned to
                |             the ordered geometrical set using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved ordered geometrical set 
                |     Example:
                |         This example retrieves in ThisOrderedGeometricalSet the fifth ordered
                |         geometrical set in the collection and in ThatOrderedGeometricalSet the ordered
                |         geometrical set named MyOrderedGeometricalSet in the ordered geometrical set
                |         collection of the partDoc part document.
                | 
                |          Set orderedGeometricalSetColl = partDoc.Part.OrderedGeometricalSets
                |          Set ThisOrderedGeometricalSet = orderedGeometricalSetColl.Item(5)
                |          Set ThatOrderedGeometricalSet = orderedGeometricalSetColl.Item("MyOrderedGeometricalSet")

        :param CATVariant i_index:
        :return: OrderedGeometricalSet
        """
        return OrderedGeometricalSet(self.ordered_geometrical_sets.Item(i_index))

    def __repr__(self):
        return f'OrderedGeometricalSets(name="{self.name}")'
