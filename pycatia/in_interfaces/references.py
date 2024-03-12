#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.in_interfaces.reference import Reference
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class References(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     References
                | 
                | A collection of all the references aggregated in an object.
                | 
                | See also:
                |     Reference
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Reference)
        self.references = com_object

    def item(self, i_index: cat_variant) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As Reference
                | 
                |     Returns a reference using its index or its name from the References
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the reference to retrieve from the
                |             collection of references. As a numerics, this index is the rank of the
                |             reference in the collection. The index of the first reference in the collection
                |             is 1, and the index of the last reference is Count. As a string, it is the name
                |             you assigned to the reference using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved reference 
                |     Example:
                |         This example retrieves the last item in the RefList reference
                |         collection by means of the Count property.
                | 
                |          Dim LastRef As Reference
                |          Set LastRef = RefList.Item(RefList.Count)

        :param cat_variant i_index:
        :rtype: Reference
        """
        return Reference(self.references.Item(i_index))

    def __getitem__(self, n: int) -> Reference:
        if (n + 1) > self.count:
            raise StopIteration

        return Reference(self.references.Item(n + 1))

    def __iter__(self) -> Iterator[Reference]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'References(name="{self.name}")'
