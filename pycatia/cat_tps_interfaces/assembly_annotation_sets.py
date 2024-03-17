#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import Iterator

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection
from pycatia.cat_tps_interfaces.annotation_set import AnnotationSet
from pycatia.types.general import cat_variant


class AssemblyAnnotationSets(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AssemblyAnnotationSets
                | 
                | Interface for collection of Annotations' Set
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.assembly_annotation_sets = com_object

    def item(self, i_index: cat_variant) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As AnyObject
                | 
                |     Retrieve a set.

        :param cat_variant i_index:
        :rtype: AnyObject
        """
        return AnyObject(self.assembly_annotation_sets.Item(i_index))

    def load_annotation_sets_list(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LoadAnnotationSetsList()
                | 
                |     Loads the Annotation Sets list. This method is very useful when a cgr
                |     document containing Annotation Set is inserted in the product, because the
                |     Annotation Set is not automatically loaded If the Annotation Set is already
                |     loaded nothing happens.

        :rtype: None
        """
        return self.assembly_annotation_sets.LoadAnnotationSetsList()

    def __getitem__(self, n: int) -> AnnotationSet:
        if (n + 1) > self.count:
            raise StopIteration

        return AnnotationSet(self.assembly_annotation_sets.Item(n + 1))

    def __iter__(self) -> Iterator[AnnotationSet]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'AssemblyAnnotationSets(name="{self.name}")'
