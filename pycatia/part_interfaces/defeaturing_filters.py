#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.part_interfaces.defeaturing_filter import DefeaturingFilter
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class DefeaturingFilters(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DefeaturingFilters
                | 
                | Represents the filter collection of a defeaturing object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.defeaturing_filters = com_object

    def add(self, i_filter_type_to_add: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add(CATBSTR iFilterTypeToAdd) As long
                | 
                |     Creates a new filter and adds it to the Defeaturing filters
                |     collection.
                | 
                |     Parameters:
                | 
                |         iFilterTypeToAdd
                |             The type of the new filter to add among : - "DefeaturingFilletFilter" -
                |             "DefeaturingHoleFilter" - or any user-defined filter's type
                | 
                |     Returns:
                |         oAddedFilterIndex The added filter's index - equals to 0 if
                |         FAILED
                | 
                |         Example:
                |             The following example adds a new filter of type theFilterType to
                |             defeaturing colelction firstDefeaturingFilters and returns the index theIndex
                |             of the new filter
                | 
                |              Set theIndex = firstDefeaturingFilters.Add(theFilterType)

        :param str i_filter_type_to_add:
        :rtype: int
        """
        return self.defeaturing_filters.Add(i_filter_type_to_add)

    def item(self, i_filter_id: cat_variant) -> DefeaturingFilter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iFilterId) As DefeaturingFilter
                | 
                |     Returns the filter of the Defeaturing filters collection using its index or
                |     its name.
                | 
                |     Parameters:
                | 
                |         iFilterId
                |             The index or the name of the filter to retrieve As a numerics, must
                |             be in [1;Count]) 
                | 
                |     Returns:
                |         oFilter The filter (see DefeaturingFilter for list of possible
                |         actions)
                | 
                |         Example:
                |             The following example returns in myFilter the filter number
                |             theIndex of Defeaturing collection
                |             firstDefeaturingFilters:
                | 
                |              Set myFilter = firstDefeaturingFilters.Item(theIndex)

        :param cat_variant i_filter_id:
        :rtype: DefeaturingFilter
        """
        return DefeaturingFilter(self.defeaturing_filters.Item(i_filter_id))

    def remove(self, i_filter_id: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iFilterId)
                | 
                |     Removes a filter from the Defeaturing filters collection and deletes it,
                |     using its index or its name.
                | 
                |     Parameters:
                | 
                |         iFilterId
                |             The index or the name of the filter to retrieve As a numerics, must
                |             be in [1;Count])
                | 
                |             Example:
                |                 The two following examples remove the filter number theIndex
                |                 from Defeaturing collection
                |                 firstDefeaturingFilters:
                | 
                |                  Call firstDefeaturingFilters.Remove(theIndex)
                |                  firstDefeaturingFilters.Remove theIndex

        :param cat_variant i_filter_id:
        :rtype: None
        """
        return self.defeaturing_filters.Remove(i_filter_id)

    def __getitem__(self, n: int) -> DefeaturingFilter:
        if (n + 1) > self.count:
            raise StopIteration

        return DefeaturingFilter(self.defeaturing_filters.Item(n + 1))

    def __iter__(self) -> Iterator[DefeaturingFilter]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DefeaturingFilters(name="{self.name}")'
