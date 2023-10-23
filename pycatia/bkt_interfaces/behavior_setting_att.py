#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class BehaviorSettingAtt(SettingController):
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
                |                         BehaviorSettingAtt
                | 
                | Enables attribute access to BKT options.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.behavior_setting_att = com_object

    @property
    def bkt_access_rights(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BKTAccessRights() As long
                | 
                |     Returns or sets the BKTAccessRights parameter.
                | 
                |     Parameters:
                | 
                |         iBKTAccessRights
                |             oBKTAccessRights Legal values:
                |             0 : User mode
                |             1: Administrator mode
                |             2: Expert mode 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: int
        """

        return self.behavior_setting_att.BKTAccessRights

    @bkt_access_rights.setter
    def bkt_access_rights(self, value: int):
        """
        :param int value:
        """

        self.behavior_setting_att.BKTAccessRights = value

    @property
    def bkt_behavior_operation_message(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BKTBehaviorOperationMessage() As long
                | 
                |     Returns or sets the BKTBehaviorOperationMessage parameter.
                | 
                |     Parameters:
                | 
                |         iBKTBehaviorOperationMessage
                |             oBKTBehaviorOperationMessage Legal values:
                |             0 : No operation messages
                |             1: with operation messages 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: int
        """

        return self.behavior_setting_att.BKTBehaviorOperationMessage

    @bkt_behavior_operation_message.setter
    def bkt_behavior_operation_message(self, value: int):
        """
        :param int value:
        """

        self.behavior_setting_att.BKTBehaviorOperationMessage = value

    @property
    def bkt_specification_tree(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BKTSpecificationTree() As long
                | 
                |     Returns or sets the BKTSpecificationTree parameter.
                | 
                |     Parameters:
                | 
                |         iBKTSpecificationTree
                |             oBKTSpecificationTree Legal values:
                |             0 : hides behaviors variables
                |             1: displays behaviors variables 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: int
        """

        return self.behavior_setting_att.BKTSpecificationTree

    @bkt_specification_tree.setter
    def bkt_specification_tree(self, value: int):
        """
        :param int value:
        """

        self.behavior_setting_att.BKTSpecificationTree = value

    def get_bkt_access_rights_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetBKTAccessRightsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the BKTAccessRights
                |     parameter.
                |     Role:Retrieves the state of the BKTAccessRights parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
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
        return self.behavior_setting_att.GetBKTAccessRightsInfo(io_admin_level, io_locked)

    def get_bkt_behavior_operation_message_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetBKTBehaviorOperationMessageInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the BKTBehaviorOperationMessage
                |     parameter.
                |     Role:Retrieves the state of the BKTBehaviorOperationMessage parameter in
                |     the current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
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
        return self.behavior_setting_att.GetBKTBehaviorOperationMessageInfo(io_admin_level, io_locked)

    def get_bkt_specification_tree_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetBKTSpecificationTreeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the BKTSpecificationTree
                |     parameter.
                |     Role:Retrieves the state of the BKTSpecificationTree parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
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
        return self.behavior_setting_att.GetBKTSpecificationTreeInfo(io_admin_level, io_locked)

    def set_bkt_access_rights_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetBKTAccessRightsLock(boolean iLocked)
                | 
                |     Locks or unlocks the BKTAccessRights parameter.
                |     Role:Locks or unlocks the BKTAccessRights parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
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
        return self.behavior_setting_att.SetBKTAccessRightsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_bkt_access_rights_lock'
        # # vba_code = """
        # # Public Function set_bkt_access_rights_lock(behavior_setting_att)
        # #     Dim iLocked (2)
        # #     behavior_setting_att.SetBKTAccessRightsLock iLocked
        # #     set_bkt_access_rights_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_bkt_behavior_operation_message_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetBKTBehaviorOperationMessageLock(boolean iLocked)
                | 
                |     Locks or unlocks the BKTBehaviorOperationMessage
                |     parameter.
                |     Role:Locks or unlocks the BKTBehaviorOperationMessage parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.behavior_setting_att.SetBKTBehaviorOperationMessageLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_bkt_behavior_operation_message_lock'
        # # vba_code = """
        # # Public Function set_bkt_behavior_operation_message_lock(behavior_setting_att)
        # #     Dim iLocked (2)
        # #     behavior_setting_att.SetBKTBehaviorOperationMessageLock iLocked
        # #     set_bkt_behavior_operation_message_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_bkt_specification_tree_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetBKTSpecificationTreeLock(boolean iLocked)
                | 
                |     Locks or unlocks the BKTSpecificationTree parameter.
                |     Role:Locks or unlocks the BKTSpecificationTree parameter if it is possible
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
        return self.behavior_setting_att.SetBKTSpecificationTreeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_bkt_specification_tree_lock'
        # # vba_code = """
        # # Public Function set_bkt_specification_tree_lock(behavior_setting_att)
        # #     Dim iLocked (2)
        # #     behavior_setting_att.SetBKTSpecificationTreeLock iLocked
        # #     set_bkt_specification_tree_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'BehaviorSettingAtt(name="{self.name}")'
