#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection


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

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As AnyObject
                | 
                |     Retrieve a set.

        :param CATVariant i_index:
        :return: AnyObject
        :rtype: AnyObject
        """
        return AnyObject(self.assembly_annotation_sets.Item(i_index.com_object))

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

        :return: None
        :rtype: None
        """
        return self.assembly_annotation_sets.LoadAnnotationSetsList()

    def __repr__(self):
        return f'AssemblyAnnotationSets(name="{ self.name }")'
