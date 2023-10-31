#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PSPListOfDoubles(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspListOfDoubles
                | 
                | Represents a collection of double values.
                | Role: Collection of double.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_list_of_doubles = com_object

    @property
    def count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Count() As long (Read Only)
                | 
                |     Returns the number of doubles in the list.
                | 
                |     Example:
                |         This example retrieves in NumberOfdoubles the number of doubles
                |         currently gathered in MyList.
                | 
                |          NumberOfdoubles = MyList.Count

        :rtype: int
        """

        return self.psp_list_of_doubles.Count

    def append(self, i_double: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Append(double iDouble)
                | 
                |     Adds a double to the end of the list.
                | 
                |     Parameters:
                | 
                |         iDouble
                |             The double to be added to the list. 
                | 
                |     Example:
                | 
                |           The following example appends an object to the list.
                |
                |          Dim MyDouble As Double
                |          MyDouble = 0.6789
                |          Dim MyList As PspListOfDoubles
                |          MyList.Append(MyDouble)

        :param float i_double:
        :rtype: None
        """
        return self.psp_list_of_doubles.Append(i_double)

    def item(self, i_index: int) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(long iIndex) As double
                | 
                |     Returns a double from its index in the list.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the first double in the collection is 1, and the index
                |             of the last double is Count. 
                | 
                |     Returns:
                |         the retrieved double.
                |
                |     Example:
                | 
                |           The following example returns in the third double in the
                |           list.
                |
                |          Dim MyDouble As double
                |          Dim MyList As PspListOfDoubles
                |          MyDouble = PspListOfDoubles.Item(3)

        :param int i_index:
        :rtype: float
        """
        return self.psp_list_of_doubles.Item(i_index)

    def remove_by_index(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveByIndex(long iIndex)
                | 
                |     Removes a double from the list by specifying its position in the
                |     list.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The position of the double to be removed in the list.
                |
                |     Example:
                | 
                |           The following example removes the second entry in the list. Please
                |           note that the
                |          list index starts with 1.
                |
                |          Dim MyList As PspListOfDoubles
                |          MyList.RemoveByIndex(2)

        :param int i_index:
        :rtype: None
        """
        return self.psp_list_of_doubles.RemoveByIndex(i_index)

    def __repr__(self):
        return f'PSPListOfDoubles(name="{self.name}")'
