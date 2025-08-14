#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_display_group import ABQDisplayGroup
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ABQDisplayGroups(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ABQDisplayGroups
                | 
                | The collection of display groups under the abaqus analysis
                | case
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ABQDisplayGroup)
        self.abq_display_groups = com_object

    def item(self, i_index: cat_variant) -> ABQDisplayGroup:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ABQDisplayGroup
                | 
                |     Returns an display group using its index or its name from the
                |     ABQDisplayGroups collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the display group to retrieve from the
                |             collection of display groups. If the index is a number, it specifies the rank
                |             of the display group in the collection. The index of the first display group in
                |             the collection is 1, and the index of the last display group is Count. If the
                |             index is a string, it specifies the name you assigned to the display group
                |             using the CATIACollection::Name property. 
                | 
                |     Returns:
                |         The specified ABQDisplayGroup.

        :param cat_variant i_index:
        :rtype: ABQDisplayGroup
        """
        return ABQDisplayGroup(self.abq_display_groups.Item(i_index))

    def __repr__(self):
        return f'ABQDisplayGroups(name="{self.name}")'
