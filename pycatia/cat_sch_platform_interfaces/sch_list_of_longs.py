#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchListOfLongs(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchListOfLongs
                | 
                | Represent a non-persistant list of LONGs to be used with schematic
                | IDLs.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_list_of_longs = com_object

    @property
    def count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Count() As long (Read Only)
                | 
                |     Returns the number of long integers in the list.
                | 
                |     Example:
                |         This example retrieves in NumberOfLongs the number of long integers
                |         currently gathered in MyList.
                | 
                |          NumberOfLongs = MyList.Count

        :rtype: int
        """

        return self.sch_list_of_longs.Count

    def append(self, i_long: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Append(long iLong)
                | 
                |     Adds an long integer to the end of the list.
                | 
                |     Parameters:
                | 
                |         iLong
                |             The long integer to be added to the list. 
                | 
                |     Example:
                | 
                |           The following example appends a long integer to the
                |           list.
                |          
                | 
                |          Dim MInteger As Long
                |          MInteger = 4
                |          Dim MyList As SchListOfLongs
                |          MyList.Append(MInteger)

        :param int i_long:
        :rtype: None
        """
        return self.sch_list_of_longs.Append(i_long)

    def item(self, i_index: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(long iIndex) As long
                | 
                |     Returns a long integer from its index in the list.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the first long integer in the collection is 1, and the
                |             index of the last long integer is Count. 
                | 
                |     Returns:
                |         the retrieved long integer. 
                |     Example:
                | 
                |           The following example returns in the third long integer in the
                |           list.
                |          
                | 
                |          Dim MyLong As Integer
                |          Dim MyList As SchListOfLongs
                |          Set MyLong = SchListOfLongs.Item(2)

        :param int i_index:
        :rtype: int
        """
        return self.sch_list_of_longs.Item(i_index)

    def remove_by_index(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveByIndex(long iIndex)
                | 
                |     Remove a long integer from the list by specifying its position in the
                |     list.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The position of the long integer to be removed in the list.
                |             
                | 
                |     Example:
                | 
                |           The following example removes the second entry in the list. Please
                |           note that the
                |          list index starts with 1.
                |
                |          Dim MyList As SchListOfLongs
                |          MyList.Remove(1)

        :param int i_index:
        :rtype: None
        """
        return self.sch_list_of_longs.RemoveByIndex(i_index)

    def __repr__(self):
        return f'SchListOfLongs(name="{self.name}")'
