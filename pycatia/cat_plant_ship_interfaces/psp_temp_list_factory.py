#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_plant_ship_interfaces.psp_list_of_bstrs import PSPListOfBSTRs
from pycatia.cat_plant_ship_interfaces.psp_list_of_doubles import PSPListOfDoubles
from pycatia.cat_plant_ship_interfaces.psp_list_of_longs import PSPListOfLongs
from pycatia.cat_plant_ship_interfaces.psp_list_of_objects import PSPListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class PSPTempListFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspTempListFactory
                | 
                | Create temporary (non-persistent) lists to be used in VB
                | environment.
                | Role: Create lists in VB environment.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_temp_list_factory = com_object

    def create_list_of_bst_rs(self) -> PSPListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateListOfBSTRs() As PspListOfBSTRs
                | 
                |     Returns a new empty list of strings.
                | 
                |     Returns:
                |         a empty list of strings.
                |
                |     Example:
                | 
                |           This example illustrates how to create a new empty list of
                |           strings.
                |
                |          Dim PspListFact As PspTempListFactory
                |          Dim NewList As PspListOfBSTRs
                |          Set NewList = PspListFact.CreateListOfBSTRs

        :rtype: PSPListOfBSTRs
        """
        return PSPListOfBSTRs(self.psp_temp_list_factory.CreateListOfBSTRs())

    def create_list_of_doubles(self) -> PSPListOfDoubles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateListOfDoubles() As PspListOfDoubles
                | 
                |     Returns a new empty list of doubles.
                | 
                |     Returns:
                |         a empty list of doubles.
                |
                |     Example:
                | 
                |           This example illustrates how to create a new empty list of
                |           doubles.
                |
                |          Dim PspListFact As PspTempListFactory
                |          Dim NewList As PspListOfDoubles
                |          Set NewList = PspListFact.CreateListOfDoubles

        :rtype: PSPListOfDoubles
        """
        return PSPListOfDoubles(self.psp_temp_list_factory.CreateListOfDoubles())

    def create_list_of_longs(self) -> PSPListOfLongs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateListOfLongs() As PspListOfLongs
                | 
                |     Returns a new empty list of long integers.
                | 
                |     Returns:
                |         a empty list of long integers.
                |
                |     Example:
                | 
                |           This example illustrates how to create a new empty list of long
                |           integers.
                |
                |          Dim PspListFact As PspTempListFactory
                |          Dim NewList As PspListOfLongs
                |          Set NewList = PspListFact.CreateListOfLongs

        :rtype: PSPListOfLongs
        """
        return PSPListOfLongs(self.psp_temp_list_factory.CreateListOfLongs())

    def create_list_of_objects(self) -> PSPListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateListOfObjects() As PspListOfObjects
                | 
                |     Returns a new empty list of objects.
                | 
                |     Returns:
                |         a empty list of objects.
                |
                |     Example:
                | 
                |           This example illustrates how to create a new empty list of
                |           objects.
                |
                |          Dim PspListFact As PspTempListFactory
                |          Dim NewList As PspListOfObjects
                |          Set NewList = PspListFact.CreateListOfObjects

        :rtype: PSPListOfObjects
        """
        return PSPListOfObjects(self.psp_temp_list_factory.CreateListOfObjects())

    def __repr__(self):
        return f'PSPTempListFactory(name="{self.name}")'
