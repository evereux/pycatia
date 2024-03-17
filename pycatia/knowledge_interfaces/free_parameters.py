#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from typing import TYPE_CHECKING

from pycatia.knowledge_interfaces.free_parameter import FreeParameter
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant

if TYPE_CHECKING:
    from pycatia.knowledge_interfaces.real_param import RealParam


class FreeParameters(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     FreeParameters
                | 
                | Interface to access a CATIAFreeParameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.free_parameters = com_object

    def add_free_parameter(self, parameter: 'RealParam') -> FreeParameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func AddFreeParameter(RealParam parameter) As
                | FreeParameter
                | 
                |     Adds a free parameter. This parameter must not be read only.

        :param RealParam parameter:
        :rtype: FreeParameter
        """
        return FreeParameter(self.free_parameters.AddFreeParameter(parameter.com_object))

    def item(self, i_index: cat_variant) -> FreeParameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As FreeParameter
                | 
                |     Retrieves an optimization using its index or its name from the Free
                |     Parameters collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the free parameter to retrieve from the
                |             collection of free parameters. As a numerics, this index is the rank of the
                |             free parameter in the collection. The index of the first free parameter in the
                |             collection is 1, and the index of the last free parameter is Count. As a
                |             string, it is the name you assigned to the free parameter using the
                |             
                | 
                |         AnyObject.Name property or when changing the free parameter name by the
                |         property panel. 
                |     Returns:
                |         The retrieved free parameter 
                |     Example:
                |         This example retrieves the last free parameter in the free parameters
                |         collection.
                | 
                |          Set lastFreeParameter = freeParameters.Item(freeParameters.Count)

        :param cat_variant i_index:
        :rtype: FreeParameter
        """
        return FreeParameter(self.free_parameters.Item(i_index))

    def remove_free_parameter(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveFreeParameter(CATVariant iIndex)
                | 
                |     Removes a free parameter.

        :param cat_variant i_index:
        :return: None
        """
        return self.free_parameters.RemoveFreeParameter(i_index)

    def __getitem__(self, n: int) -> FreeParameter:
        if (n + 1) > self.count:
            raise StopIteration

        return FreeParameter(self.free_parameters.Item(n + 1))

    def __iter__(self) -> Iterator[FreeParameter]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'FreeParameters(name="{self.name}")'
