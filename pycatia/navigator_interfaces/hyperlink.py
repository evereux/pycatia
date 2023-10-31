#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class Hyperlink(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Hyperlink
                | 
                | Represents a hyperlink marker.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hyperlink = com_object

    def add_url(self, i_url: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddUrl(CATBSTR iUrl)
                | 
                |     Adds a url to an Hyperlink.
                | 
                |     Parameters:
                | 
                |         iUrl
                |             The URL to be added to the Hyperlink. 
                | 
                |     Example:
                | 
                |              This example links TheUrl to the NewHyperlink
                |              Hyperlink.
                |             
                | 
                |             NewHyperlink.AddUrl(TheUrl)

        :param str i_url:
        :rtype: None
        """
        return self.hyperlink.AddUrl(i_url)

    def count_object(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CountObject() As long
                | 
                |     Returns the number of Url which are linked to the
                |     Hyperlink.
                | 
                |     Example:
                | 
                |              This example reads the number of Url in the Hyperlink NewHyperlink
                |              .
                |             
                | 
                |             Dim number As Integer
                |             number = NewHyperlink.CountObject

        :rtype: int
        """
        return self.hyperlink.CountObject()

    def item_object(self, i_index: cat_variant) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func ItemObject(CATVariant iIndex) As CATBSTR
                | 
                |     Returns an Url which is linked to the Hyperlink using its
                |     index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Url in the Hyperlink. The index of the first
                |             object is 1, and the index of the last object is CountObject.
                |             
                | 
                |     Returns:
                |         The retrieved Url 
                |     Example:
                | 
                |              This example retrieves in ThisUrl the ninth
                |              object
                |             from the NewHyperlink  Hyperlink.
                |             
                | 
                |             Dim ThisUrl As String
                |             Set ThisUrl = NewHyperlink.ItemObject(9)

        :param cat_variant i_index:
        :rtype: str
        """
        return self.hyperlink.ItemObject(i_index)

    def remove_object(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveObject(CATVariant iIndex)
                | 
                |     Removes an Url which is linked to the Hyperlink using its
                |     index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the object in the Hyperlink. The index of the first
                |             object is 1, and the index of the last object is CountObject.
                |             
                | 
                |     Example:
                | 
                |              This example removes the ninth Url
                |             from the NewHyperlink  Hyperlink.
                |             
                | 
                |             NewHyperlink.RemoveObject(9)

        :param cat_variant i_index:
        :rtype: None
        """
        return self.hyperlink.RemoveObject(i_index)

    def __repr__(self):
        return f'Hyperlink(name="{self.name}")'
