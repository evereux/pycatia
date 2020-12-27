#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.part_interfaces.draft_domain import DraftDomain
from pycatia.system_interfaces.collection import Collection
from pycatia.types import cat_variant


class DraftDomains(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DraftDomains
                | 
                | The collection of draft domains used by the draft shape.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.draft_domains = com_object

    def item(self, i_index: cat_variant) -> DraftDomain:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As DraftDomain
                | 
                |     Returns a draft domain using its index or its name from the DraftDomains
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the draft domain to retrieve from the
                |             collection of draft domains. As a numerics, this index is the rank of the draft
                |             domain in the collection. The index of the first draft domain in the collection
                |             is 1, and the index of the last draft domain is Count. As a string, it is the
                |             name you assigned to the draft domain using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved draft domain
                | 
                |         Example:
                |             The following example returns in domain the third draft domain of
                |             the firstDraftDomains collection:
                | 
                |              Set domain = firstDraftDomains.Item(3)

        :param cat_variant i_index:
        :return: DraftDomain
        :rtype: DraftDomain
        """
        return DraftDomain(self.draft_domains.Item(i_index))

    def __iter__(self) -> DraftDomain:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DraftDomains(name="{self.name}")'
