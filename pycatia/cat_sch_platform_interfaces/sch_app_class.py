#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_list_of_bst_rs import SchListOfBSTRs
from pycatia.system_interfaces.any_object import AnyObject


class SchAppClass(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppClass
                | 
                | Manage the class hierarchy of an application model.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_class = com_object

    def app_get_component_base_class(self) -> SchListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppGetComponentBaseClass() As SchListOfBSTRs
                | 
                |     Provide the application class names for the base component
                |     classes.
                | 
                |     Parameters:
                | 
                |         oLBaseCompClasses
                |             Class names of application base component classes.
                |             
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppClass
                |          Dim objArg1 As SchListOfBSTRs
                |           ...
                |          Set objArg1 = objThisIntf.AppGetComponentBaseClass

        :rtype: SchListOfBSTRs
        """
        return SchListOfBSTRs(self.sch_app_class.AppGetComponentBaseClass())

    def app_get_group_base_class(self, o_group_class_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppGetGroupBaseClass(CATBSTR oGroupClassName)
                | 
                |     Provide the application class name for Schematic Group
                |     class.
                | 
                |     Parameters:
                | 
                |         oGroupClassName
                |             Class name of application class. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppClass
                |          Dim strVar1 As String
                |           ...
                |          objThisIntf.AppGetGroupBaseClassstrVar1

        :param str o_group_class_name:
        :rtype: None
        """
        return self.sch_app_class.AppGetGroupBaseClass(o_group_class_name)

    def app_get_route_base_class(self, o_route_class_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppGetRouteBaseClass(CATBSTR oRouteClassName)
                | 
                |     Provide the application class name for Schematic Route
                |     class.
                | 
                |     Parameters:
                | 
                |         oRouteClassName
                |             Class name of application class. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppClass
                |          Dim strVar1 As String
                |           ...
                |          objThisIntf.AppGetRouteBaseClassstrVar1

        :param str o_route_class_name:
        :rtype: None
        """
        return self.sch_app_class.AppGetRouteBaseClass(o_route_class_name)

    def app_get_zone_base_class(self, o_zone_class_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppGetZoneBaseClass(CATBSTR oZoneClassName)
                | 
                |     Provide the application class name for Schematic Zone
                |     class.
                | 
                |     Parameters:
                | 
                |         oZoneClassName
                |             Class name of application class. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppClass
                |          Dim strVar1 As String
                |           ...
                |          objThisIntf.AppGetZoneBaseClassstrVar1

        :param str o_zone_class_name:
        :rtype: None
        """
        return self.sch_app_class.AppGetZoneBaseClass(o_zone_class_name)

    def app_list_valid_route_types(self) -> SchListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppListValidRouteTypes() As SchListOfBSTRs
                | 
                |     List the valid application route types allowed to be
                |     created.
                | 
                |     Parameters:
                | 
                |         oLValidRouteTypes
                |             A list of route class types allowed. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppClass
                |          Dim objArg1 As SchListOfBSTRs
                |           ...
                |          Set objArg1 = objThisIntf.AppListValidRouteTypes

        :rtype: SchListOfBSTRs
        """
        return SchListOfBSTRs(self.sch_app_class.AppListValidRouteTypes())

    def __repr__(self):
        return f'SchAppClass(name="{self.name}")'
