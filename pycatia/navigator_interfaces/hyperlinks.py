#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.navigator_interfaces.hyperlink import Hyperlink
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Hyperlinks(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Hyperlinks

    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Hyperlink)
        self.hyperlinks = com_object

    def add(self, i_object: AnyObject) -> Hyperlink:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add(AnyObject iObject) As Hyperlink
                | 
                |     Adds a Hyperlink to the Hyperlinks collection. Be careful: only one
                |     Hyperlink instance is allowed per object which supports the hyperlink. If one
                |     adds a Hyperlink on an object which already has a Hyperlink, the call fails.
                |     The Hyperlink name is internally generated. If one wants to manage Hyperlink
                |     using its name, he has to set it manually.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object which supports the hyperlink. 
                | 
                |     Example:
                | 
                |              The following example adds a Hyperlink
                |             
                | 
                |             Dim NewHyperlink As Hyperlink
                |             Set NewHyperlink = TheHyperlinks.Add(iObject)

        :param AnyObject i_object:
        :rtype: Hyperlink
        """
        return Hyperlink(self.hyperlinks.Add(i_object.com_object))

    def get_hyperlink(self, i_object: AnyObject) -> Hyperlink:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetHyperlink(AnyObject iObject) As Hyperlink
                | 
                |     Retrieve an Hyperlink associated to an object
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object which supports the hyperlink. The call fails otherwise.
                |             
                | 
                |     Returns:
                |         The retrieved Hyperlink if it exists 
                |     Example:
                | 
                |              This example retrieves an existing one in the TheHyperlinks
                |              collection.
                |             
                | 
                |             Dim NewHyperlink As Hyperlink
                |             Set NewHyperlink = TheHyperlinks.GetHyperlink(iObject)

        :param AnyObject i_object:
        :rtype: Hyperlink
        """
        return Hyperlink(self.hyperlinks.GetHyperlink(i_object.com_object))

    def item(self, i_index: cat_variant) -> Hyperlink:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As Hyperlink
                | 
                |     Returns an Hyperlink using its index from the Hyperlinks
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the hyperlink to retrieve from the
                |             collection of Hyperlinks. As a numerics, this index is the rank of the
                |             Hyperlink in the collection. The index of the first Hyperlink in the collection
                |             is 1, and the index of the last Hyperlink is Count. As a string, it is the name
                |             you assigned to the Hyperlink. 
                | 
                |     Returns:
                |         The retrieved Hyperlink 
                |     Example:
                | 
                |              This example retrieves in ThisHyperlink the ninth Hyperlink
                |              ,
                |             and in ThatHyperlink the Hyperlink named
                |              Hyperlink3 from the TheHyperlinks collection. 
                |             
                | 
                |             Dim ThisHyperlink As Hyperlink
                |             Set ThisHyperlink = TheHyperlinks.Item(9)
                |             Dim ThatHyperlink As Hyperlink
                |             Set ThatHyperlink = TheHyperlinks.Item("Hyperlink3")

        :param cat_variant i_index:
        :rtype: Hyperlink
        """
        return Hyperlink(self.hyperlinks.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a Hyperlink from the Hyperlinks collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Hyperlink to retrieve from the
                |             collection of Hyperlinks. As a numerics, this index is the rank of the
                |             Hyperlink in the collection. The index of the first Hyperlink in the collection
                |             is 1, and the index of the last Hyperlink is Count. As a string, it is the name
                |             you assigned to the Hyperlink. 
                | 
                |     Example:
                | 
                |              The following example removes the tenth Hyperlink and the
                |              Hyperlink named
                |              Hyperlink 2 from the TheHyperlinks collection.
                |             
                | 
                |             TheHyperlinks.Remove(10)
                |             TheHyperlinks.Remove("Hyperlink2")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.hyperlinks.Remove(i_index)

    def __getitem__(self, n: int) -> Hyperlink:
        if (n + 1) > self.count:
            raise StopIteration

        return Hyperlink(self.hyperlinks.Item(n + 1))

    def __iter__(self) -> Iterator[Hyperlink]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Hyperlinks(name="{self.name}")'
