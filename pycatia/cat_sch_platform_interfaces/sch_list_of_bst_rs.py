#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchListOfBSTRs(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchListOfBSTRs
                | 
                | Represents a non-persistant list of character strings to be used with Schematic
                | IDLs.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_list_of_bst_rs = com_object

    @property
    def count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Count() As long (Read Only)
                | 
                |     Returns the number of character strings in the list.
                | 
                |     Example:
                |         This example retrieves in NumberOfStrings the number of character
                |         strings currently gathered in MyList.
                | 
                |          NumberOfStrings = MyList.Count

        :rtype: int
        """

        return self.sch_list_of_bst_rs.Count

    def append(self, i_bstr: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Append(CATBSTR iBSTR)
                | 
                |     Adds a character string to the end of the list.
                | 
                |     Parameters:
                | 
                |         iBSTR
                |             The character string to be added to the list. 
                | 
                |     Example:
                | 
                |           The following example appends a string to the list.
                |
                |          Dim MyList As SchListOfBSTRs
                |          MyList.Append("MyString")

        :param str i_bstr:
        :rtype: None
        """
        return self.sch_list_of_bst_rs.Append(i_bstr)

    def item(self, i_index: int) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(long iIndex) As CATBSTR
                | 
                |     Returns a character string from its index in the list.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the first character string in the collection is 1, and
                |             the index of the last character string is Count. 
                | 
                |     Returns:
                |         the retrieved string. 
                |
                |     Example:
                | 
                |           The following example returns in the third character string in the
                |           list.
                |
                |          Dim MyStr As String
                |          Dim MyList As SchListOfBSTRs
                |          Set MyStr = SchListOfBSTRs.Item(2)

        :param int i_index:
        :rtype: str
        """
        return self.sch_list_of_bst_rs.Item(i_index)

    def remove_by_index(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveByIndex(long iIndex)
                | 
                |     Remove a character string from the list by specifying its position in the
                |     list.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The position of the character string to be removed in the list.
                |
                |     Example:
                | 
                |           The following example removes the second entry in the list. Please
                |           note that the
                |          list index starts with 1.
                |          
                | 
                |          Dim MyList As SchListOfBSTRs
                |          MyList.Remove(1)

        :param int i_index:
        :rtype: None
        """
        return self.sch_list_of_bst_rs.RemoveByIndex(i_index)

    def __repr__(self):
        return f'SchListOfBSTRs(name="{self.name}")'
