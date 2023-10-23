#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchListOfObjects(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchListOfObjects
                | 
                | Represent a non-persistant list of schematic objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_list_of_objects = com_object

    @property
    def count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Count() As long (Read Only)
                | 
                |     Returns the number of objects in the list.
                | 
                |     Example:
                |         This example retrieves in NumberOfObjects the number of objects
                |         currently gathered in MyList.
                | 
                |          NumberOfObjects = MyList.Count

        :rtype: int
        """

        return self.sch_list_of_objects.Count

    def append(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Append(AnyObject iObject)
                | 
                |     Adds an object to the end of the list.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to be added to the list. 
                | 
                |     Example:
                | 
                |           The following example appends an object to the list.
                |          
                |          Dim MyObject As AnyObject
                |          Dim MyList As SchListOfObjects
                |          MyList.Append(MyObject)

        :param AnyObject i_object:
        :rtype: None
        """
        return self.sch_list_of_objects.Append(i_object.com_object)

    def item(self, i_index: int, i_interface_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(long iIndex,
                | CATBSTR iInterfaceName) As AnyObject
                | 
                |     Returns an object from its index in the list.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the first object in the collection is 1, and the index
                |             of the last object is Count. 
                |         iInterfaceName
                |             The interface name of oObj. 
                | 
                |     Returns:
                |         the retrieved object. 
                |     Example:
                | 
                |           The following example returns in the third object in the
                |           list.
                |
                |          Dim MyObject As AnyObject
                |          Dim MyList As SchListOfObjects
                |          Set MyObject = SchListOfObjects.Item(2,"CATIASchComponent")

        :param int i_index:
        :param str i_interface_name:
        :rtype: AnyObject
        """
        return AnyObject(self.sch_list_of_objects.Item(i_index, i_interface_name))

    def remove_by_index(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveByIndex(long iIndex)
                | 
                |     Remove an object from the list by specifying its position in the
                |     list.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The position of the object to be removed in the list.
                |
                |     Example:
                | 
                |           The following example removes the second entry in the list. Please
                |           note that the
                |          list index starts with 1.
                |
                |          Dim MyList As SchListOfObjects
                |          MyList.Remove(1)

        :param int i_index:
        :rtype: None
        """
        return self.sch_list_of_objects.RemoveByIndex(i_index)

    def __repr__(self):
        return f'SchListOfObjects(name="{self.name}")'
