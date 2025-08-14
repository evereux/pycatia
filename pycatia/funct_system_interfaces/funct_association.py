#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class FunctAssociation(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FunctAssociation
                | 
                | The interface to access a Functional Association.
                | 
                | It is managed on a Functional Element, thru the MultiRep Facet Manager
                | (MRM).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.funct_association = com_object

    @property
    def linked_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LinkedCount() As long (Read Only)
                | 
                |     Get count of linked objects.

        :rtype: int
        """

        return self.funct_association.LinkedCount

    def detach_from(self, i_linked: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub DetachFrom(AnyObject iLinked)
                | 
                |     Delete a link to a linked object.

        :param AnyObject i_linked:
        :rtype: None
        """
        return self.funct_association.DetachFrom(i_linked.com_object)

    def link_to(self, i_linked: AnyObject, i_kind: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LinkTo(AnyObject iLinked,
                | CATBSTR iKind)
                | 
                |     Create a link to another object.

        :param AnyObject i_linked:
        :param str i_kind:
        :rtype: None
        """
        return self.funct_association.LinkTo(i_linked.com_object, i_kind)

    def retrieve_kind_of_linked(self, i_index: cat_variant) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func RetrieveKindOfLinked(CATVariant iIndex) As CATBSTR
                | 
                |     Retrieve the kind of linked object.

        :param cat_variant i_index:
        :rtype: str
        """
        return self.funct_association.RetrieveKindOfLinked(i_index)

    def retrieve_linked(self, i_index: cat_variant) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func RetrieveLinked(CATVariant iIndex) As AnyObject
                | 
                |     Retrieve a linked object.

        :param cat_variant i_index:
        :rtype: AnyObject
        """
        return AnyObject(self.funct_association.RetrieveLinked(i_index))

    def __repr__(self):
        return f'FunctAssociation(name="{self.name}")'
