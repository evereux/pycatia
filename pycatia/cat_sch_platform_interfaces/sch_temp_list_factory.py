#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_list_of_bst_rs import SchListOfBSTRs
from pycatia.cat_sch_platform_interfaces.sch_list_of_doubles import SchListOfDoubles
from pycatia.cat_sch_platform_interfaces.sch_list_of_longs import SchListOfLongs
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class SchTempListFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchTempListFactory
                | 
                | Create temporary (non-persistent) lists to be used in VB
                | environment.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_temp_list_factory = com_object

    def create_list_of_bst_rs(self) -> SchListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateListOfBSTRs() As SchListOfBSTRs
                | 
                |     This method returns a new empty list of strings.
                | 
                |     Returns:
                |         a empty list of strings. 
                |     Example:
                | 
                |           This example illustrates how to create a new empty list of
                |           strings.
                |          
                |          Dim SchListFact As SchTempListFactory
                |          Dim NewList As SchListOfBSTRs
                |          Set NewList = SchListFact.CreateListOfBSTRs

        :rtype: SchListOfBSTRs
        """
        return SchListOfBSTRs(self.sch_temp_list_factory.CreateListOfBSTRs())

    def create_list_of_doubles(self) -> SchListOfDoubles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateListOfDoubles() As SchListOfDoubles
                | 
                |     This method returns a new empty list of doubles.
                | 
                |     Returns:
                |         a empty list of doubles. 
                |
                |     Example:
                | 
                |           This example illustrates how to create a new empty list of
                |           doubles.
                |          
                |          Dim SchListFact As SchTempListFactory
                |          Dim NewList As SchListOfDoubles
                |          Set NewList = SchListFact.CreateListOfDoubles

        :rtype: SchListOfDoubles
        """
        return SchListOfDoubles(self.sch_temp_list_factory.CreateListOfDoubles())

    def create_list_of_longs(self) -> SchListOfLongs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateListOfLongs() As SchListOfLongs
                | 
                |     This method returns a new empty list of long integers.
                | 
                |     Returns:
                |         a empty list of long integers. 
                |     Example:
                | 
                |           This example illustrates how to create a new empty list of long
                |           integers.
                |
                |          Dim SchListFact As SchTempListFactory
                |          Dim NewList As SchListOfLongs
                |          Set NewList = SchListFact.CreateListOfLongs

        :rtype: SchListOfLongs
        """
        return SchListOfLongs(self.sch_temp_list_factory.CreateListOfLongs())

    def create_list_of_objects(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateListOfObjects() As SchListOfObjects
                | 
                |     This method returns a new empty list of objects.
                | 
                |     Returns:
                |         a empty list of objects. 
                |
                |     Example:
                | 
                |           This example illustrates how to create a new empty list of
                |           objects.
                |
                |          Dim SchListFact As SchTempListFactory
                |          Dim NewList As SchListOfObjects
                |          Set NewList = SchListFact.CreateListOfObjects

        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_temp_list_factory.CreateListOfObjects())

    def __repr__(self):
        return f'SchTempListFactory(name="{self.name}")'
