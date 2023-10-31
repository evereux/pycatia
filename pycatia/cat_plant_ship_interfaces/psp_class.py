#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_plant_ship_interfaces.psp_list_of_bstrs import PSPListOfBSTRs
from pycatia.system_interfaces.any_object import AnyObject


class PSPClass(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspClass
                | 
                | Represent Interface to list the start up object classes of an
                | application.
                | Role: Application object classes.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_class = com_object

    @property
    def start_up_connectors(self) -> PSPListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StartUpConnectors() As PspListOfBSTRs (Read Only)
                | 
                |     Returns a List of start-up Connector object classes.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspClass
                |          Dim objArg1 As PspListOfBSTRs
                |           ...
                |          Set objArg1 = objThisIntf.StartUpConnectors

        :rtype: PSPListOfBSTRs
        """

        return PSPListOfBSTRs(self.psp_class.StartUpConnectors)

    @property
    def start_up_functions(self) -> PSPListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StartUpFunctions() As PspListOfBSTRs (Read Only)
                | 
                |     Returns a List of start-up Function object classes.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspClass
                |          Dim objArg1 As PspListOfBSTRs
                |           ...
                |          Set objArg1 = objThisIntf.StartupFunctions

        :rtype: PSPListOfBSTRs
        """

        return PSPListOfBSTRs(self.psp_class.StartUpFunctions)

    @property
    def start_up_physicals(self) -> PSPListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StartUpPhysicals() As PspListOfBSTRs (Read Only)
                | 
                |     Returns a List of start-up physical object classes.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspClass
                |          Dim objArg1 As PspListOfBSTRs
                |           ...
                |          Set objArg1 = objThisIntf.StartupPhysicals

        :rtype: PSPListOfBSTRs
        """

        return PSPListOfBSTRs(self.psp_class.StartUpPhysicals)

    def __repr__(self):
        return f'PSPClass(name="{self.name}")'
