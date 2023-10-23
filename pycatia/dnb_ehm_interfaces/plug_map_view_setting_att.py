#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class PlugMapViewSettingAtt(SettingController):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         PlugMapViewSettingAtt
                | 
                | Interface representing xxx.
                | 
                | Role: Components that implement DNBIAPlugMapViewSettingAtt are
                | ...
                | 
                | Do not use the DNBIAPlugMapViewSettingAtt interface for such and such
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.plug_map_view_setting_att = com_object

    @property
    def logical_data_attr_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LogicalDataAttrList() As CATSafeArrayVariant
                | 
                |     Returns or sets the LogicalDataAttrList parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is
                |     delegated.

        :rtype: tuple
        """

        return self.plug_map_view_setting_att.LogicalDataAttrList

    @logical_data_attr_list.setter
    def logical_data_attr_list(self, value: tuple):
        """
        :param tuple value:
        """

        self.plug_map_view_setting_att.LogicalDataAttrList = value

    @property
    def termination_attr_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TerminationAttrList() As CATSafeArrayVariant
                | 
                |     Returns or sets the ConstraintsSimul parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is
                |     delegated.

        :rtype: tuple
        """

        return self.plug_map_view_setting_att.TerminationAttrList

    @termination_attr_list.setter
    def termination_attr_list(self, value: tuple):
        """
        :param tuple value:
        """

        self.plug_map_view_setting_att.TerminationAttrList = value

    def addto_logical_data_attr_list(self, iparameter_name: str, i_refparam_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddtoLogicalDataAttrList(CATBSTR iparameterName,
                | CATBSTR iRefparamName)
                | 
                |     Method to add a parameter to the LogicalDataAttrList.

        :param str iparameter_name:
        :param str i_refparam_name:
        :rtype: None
        """
        return self.plug_map_view_setting_att.AddtoLogicalDataAttrList(iparameter_name, i_refparam_name)

    def addto_termination_attr_list(self, iparameter_name: str, i_refparam_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddtoTerminationAttrList(CATBSTR iparameterName,
                | CATBSTR iRefparamName)
                | 
                |     Method to add a parameter to the TerminationAttrList.

        :param str iparameter_name:
        :param str i_refparam_name:
        :rtype: None
        """
        return self.plug_map_view_setting_att.AddtoTerminationAttrList(iparameter_name, i_refparam_name)

    def get_logical_data_attr_list_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLogicalDataAttrListInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LogicalDataAttrList
                |     parameter.
                |     Role:Retrieves the state of the LogicalDataAttrList parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a
                |             reset.
                |         ioLocked
                |             Indicates if the parameter has been locked.
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.plug_map_view_setting_att.GetLogicalDataAttrListInfo(io_admin_level, io_locked)

    def get_termination_attr_list_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTerminationAttrListInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TerminationAttrList
                |     parameter.
                |     Role:Retrieves the state of the TerminationAttrList parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a
                |             reset.
                |         ioLocked
                |             Indicates if the parameter has been locked.
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.plug_map_view_setting_att.GetTerminationAttrListInfo(io_admin_level, io_locked)

    def remove_from_logical_data_attr_list(self, iparameter_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemovefromLogicalDataAttrList(CATBSTR iparameterName)
                | 
                |     Method to Remove a parameter fron the LogicalDataAttrList.

        :param str iparameter_name:
        :rtype: None
        """
        return self.plug_map_view_setting_att.RemovefromLogicalDataAttrList(iparameter_name)

    def remove_from_termination_attr_list(self, iparameter_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemovefromTerminationAttrList(CATBSTR iparameterName)
                | 
                |     Method to Remove a parameter fron the TerminationAttrList.

        :param str iparameter_name:
        :rtype: None
        """
        return self.plug_map_view_setting_att.RemovefromTerminationAttrList(iparameter_name)

    def set_logical_data_attr_list_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLogicalDataAttrListLock(boolean iLocked)
                | 
                |     Locks or unlocks the LogicalDataAttrList parameter.
                |     Role:Locks or unlocks the LogicalDataAttrList parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.plug_map_view_setting_att.SetLogicalDataAttrListLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_logical_data_attr_list_lock'
        # # vba_code = """
        # # Public Function set_logical_data_attr_list_lock(plug_map_view_setting_att)
        # #     Dim iLocked (2)
        # #     plug_map_view_setting_att.SetLogicalDataAttrListLock iLocked
        # #     set_logical_data_attr_list_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_termination_attr_list_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTerminationAttrListLock(boolean iLocked)
                | 
                |     Locks or unlocks the TerminationAttrList parameter.
                |     Role:Locks or unlocks the TerminationAttrList parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.plug_map_view_setting_att.SetTerminationAttrListLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_termination_attr_list_lock'
        # # vba_code = """
        # # Public Function set_termination_attr_list_lock(plug_map_view_setting_att)
        # #     Dim iLocked (2)
        # #     plug_map_view_setting_att.SetTerminationAttrListLock iLocked
        # #     set_termination_attr_list_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PlugMapViewSettingAtt(name="{self.name}")'
