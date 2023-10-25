#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class Fastener(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Fastener

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.fastener = com_object

    def all_parts_loaded(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AllPartsLoaded() As boolean
                | 
                |     Gets the loading status of the joining parts of the fastener If all the joining parts are
                |     loaded in the V5 session then it returns TRUE If no parts or some parts are loaded in the
                |     V5 session then it returns FALSE Return type : 1,0
                | 
                | Example:
                |     Dim AllPartsLoaded AllPartsLoaded = MyFastener.AllPartsLoaded

        :rtype: bool
        """
        return self.fastener.AllPartsLoaded()

    def get_double_user_attribute(self, i_attribute_label: str) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDoubleUserAttribute(CATBSTR iAttributeLabel) As
                | double
                | 
                |     Returns the value of user attribute whoes name matches the
                |     input
                |     string. Valid for attributes of type double. User attributes
                |     are
                |     created from Process Engineer user attributes only.
                | 
                |     Parameters:
                | 
                |         iAttributeLabel
                |             The label of user attribute of double type 
                | 
                |     Example:
                |         This example gets value of double user attribute "PLATE SIZE" on
                |         Process Engineer fastener
                | 
                |          DblAttrVal = MyFastener.GetDoubleUserAttribute ("PLATE SIZE")

        :param str i_attribute_label:
        :rtype: float
        """
        return self.fastener.GetDoubleUserAttribute(i_attribute_label)

    def get_int_user_attribute(self, i_attribute_label: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetIntUserAttribute(CATBSTR iAttributeLabel) As long

        :param str i_attribute_label:
        :rtype: int
        """
        return self.fastener.GetIntUserAttribute(i_attribute_label)

    def get_part(self, index: int) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPart(short index) As Product
                | 
                |     Returns the product at the specified index from list of parts joined by
                |     fastener.
                | 
                |     Parameters:
                | 
                |         index
                |             Index should be greater than equal to 1. 
                | 
                |     Example:
                |         This example gets the part at index 1
                | 
                |          Dim MyProduct As Product
                |          Set MyProduct = MyFastener.GetPart(1)

        :param int index:
        :rtype: Product
        """
        return Product(self.fastener.GetPart(index))

    def get_parts(self, o_list_of_parts: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetParts(CATSafeArrayVariant oListOfParts)
                | 
                |     Returns the list of parts joined by fastener.
                | 
                |     Parameters:
                | 
                |         oListOfParts
                |             The list of parts 
                | 
                |     Example:
                |         This example gets list of parts joined by fastener
                | 
                |          Dim NumberOfParts
                |          Dim JoiningParts()
                |          NumberOfParts = MyFastener.NumberOfJoiningParts
                |          ReDim JoiningParts(NumParts-1)
                |          MyFastener.GetParts(JoiningParts)

        :param tuple o_list_of_parts:
        :rtype: None
        """
        return self.fastener.GetParts(o_list_of_parts)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_parts'
        # # vba_code = """
        # # Public Function get_parts(fastener)
        # #     Dim oListOfParts (2)
        # #     fastener.GetParts oListOfParts
        # #     get_parts = oListOfParts
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_process(self, index: int) -> Activity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProcess(short index) As Activity
                | 
                |     Returns the activity, at the specified index, on which the fastener is
                |     assigned
                | 
                |     Parameters:
                | 
                |         index
                |             Index should be greater than equal to 1. 
                | 
                |     Example:
                |         This example gets the activity at index 1
                | 
                |          Dim MyActivity As Activity
                |          Set MyActivity = MyFastener.GetProcess(1)

        :param int index:
        :rtype: Activity
        """
        return Activity(self.fastener.GetProcess(index))

    def get_string_user_attribute(self, i_attribute_label: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStringUserAttribute(CATBSTR iAttributeLabel) As
                | CATBSTR
                | 
                |     Returns the value of user attribute whoes name matches the
                |     input
                |     string. Valid for attributes of type string. User attributes
                |     are
                |     created from Process Engineer user attributes only.
                | 
                |     Parameters:
                | 
                |         iAttributeLabel
                |             The label of user attribute of string type 
                | 
                |     Example:
                |         This example gets value of string user attribute "PLATE NAME" on
                |         Process Engineer fastener
                | 
                |          Dim StrAttrVal As String
                |          StrAttrVal = MyFastener.GetStringUserAttribute ("PLATE NAME")

        :param str i_attribute_label:
        :rtype: str
        """
        return self.fastener.GetStringUserAttribute(i_attribute_label)

    def number_of_assigned_processes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func NumberOfAssignedProcesses() As long
                | 
                |     Returns Number of processes assigned with the fastener 
                | 
                | Example:
                |     Dim Num Num = MyFastener.NumberOfAssignedProcesses

        :rtype: int
        """
        return self.fastener.NumberOfAssignedProcesses()

    def number_of_joining_parts(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func NumberOfJoiningParts() As long
                | 
                |     Returns the number of parts joined by fastener.
                | 
                |     Parameters:
                | 
                |         oNumOfParts
                |             The number of parts 
                | 
                |     Example:
                |         This example gets number of parts joined by fastener
                | 
                |          Dim NumberOfParts
                |          NumberOfParts = MyFastener.NumberOfJoiningParts

        :rtype: int
        """
        return self.fastener.NumberOfJoiningParts()

    def remove_from_ppr(self, i_force_remove_if_assigned: bool, e_status: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveFromPPR(boolean iForceRemoveIfAssigned,
                | DNBPPRRemoveStatus eStatus)
                | 
                |     Removes the fastener from the current session without deleting it in the
                |     Manufacturing HUB project.
                | 
                |     Parameters:
                | 
                |         in
                |             iForceRemoveIfAssigned Valid Param : 1 : for removing fastener from session even in
                |             case it is assigned to a process or resource. The product/resource to fastener relation
                |             remains un-affected in PPRHUB. 0 : for NOT removing the fastener from session in case it
                |             is assigned to a process or resource.
                |         out
                |             eStatus Status of remove call. See DNBPPRRemoveStatus definition
                |             above. * 
                | 
                |     Example:
                |         Dim RemoveStatus As EnumParam MyFastenerPPRServices.RemoveFromPPR 1,
                |         RemoveStatus MsgBox RemoveStatus

        :param bool i_force_remove_if_assigned:
        :param int e_status: enum dnbppr_remove_status
        :rtype: None
        """
        return self.fastener.RemoveFromPPR(i_force_remove_if_assigned, e_status)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_from_ppr'
        # # vba_code = """
        # # Public Function remove_from_ppr(fastener)
        # #     Dim iForceRemoveIfAssigned (2)
        # #     fastener.RemoveFromPPR iForceRemoveIfAssigned
        # #     remove_from_ppr = iForceRemoveIfAssigned
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_double_user_attribute(self, i_attribute_label: str, i_double_value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDoubleUserAttribute(CATBSTR iAttributeLabel,
                | double iDoubleValue)
                | 
                |     Set the value of user attribute whoes name matches the
                |     input
                |     string. Valid for attributes of type double. User attributes
                |     are
                |     created from Process Engineer user attributes only.
                | 
                |     Parameters:
                | 
                |         iAttributeLabel
                |             The label of user attribute of double type 
                | 
                |     Example:
                |         This example gets value of double user attribute "PLATE SIZE" on
                |         Process Engineer fastener
                | 
                |          MyFastener.GetDoubleUserAttribute ("PLATE SIZE",DblAttrVal)

        :param str i_attribute_label:
        :param float i_double_value:
        :rtype: None
        """
        return self.fastener.SetDoubleUserAttribute(i_attribute_label, i_double_value)

    def set_int_user_attribute(self, i_attribute_label: str, i_int_value: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetIntUserAttribute(CATBSTR iAttributeLabel,
                | long iIntValue)

        :param str i_attribute_label:
        :param int i_int_value:
        :rtype: None
        """
        return self.fastener.SetIntUserAttribute(i_attribute_label, i_int_value)

    def set_string_user_attribute(self, i_attribute_label: str, i_string_value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStringUserAttribute(CATBSTR iAttributeLabel,
                | CATBSTR iStringValue)
                | 
                |     Set the value of user attribute whoes name matches the
                |     input
                |     string. Valid for attributes of type string. User attributes
                |     are
                |     created from Process Engineer user attributes only.
                | 
                |     Parameters:
                | 
                |         iAttributeLabel
                |             The label of user attribute of string type 
                | 
                |     Example:
                |         This example gets value of string user attribute "PLATE NAME" on
                |         Process Engineer fastener
                | 
                |          Dim StrAttrVal As String
                |          StrAttrVal = "Name"
                |          MyFastener.SetStringUserAttribute ("PLATE NAME",StrAttrVal)

        :param str i_attribute_label:
        :param str i_string_value:
        :rtype: None
        """
        return self.fastener.SetStringUserAttribute(i_attribute_label, i_string_value)

    def set_text_id_visibility(self, i_status: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTextIDVisibility(boolean iStatus)
                | 
                |     Sets the Hide/Show status of the text ID of the fastener in the 3D window Valid Param : 1,0 
                | 
                | Example:
                |     //to make the fastener id visible in 3D MyFastener.SetIDVisibility(1) //to
                |     make the fastener id hidden in 3D
                |     MyFastener.SetIDVisibility(0)
                | 
                |     Copyright © 1999-2011, Dassault Systèmes. All rights
                |     reserved.

        :param bool i_status:
        :rtype: None
        """
        return self.fastener.SetTextIDVisibility(i_status)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_text_id_visibility'
        # # vba_code = """
        # # Public Function set_text_id_visibility(fastener)
        # #     Dim iStatus (2)
        # #     fastener.SetTextIDVisibility iStatus
        # #     set_text_id_visibility = iStatus
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Fastener(name="{self.name}")'
