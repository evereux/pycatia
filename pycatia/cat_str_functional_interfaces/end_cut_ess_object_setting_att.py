#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class EndCutESSObjectSettingAtt(SettingController):
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
                |                         EndCutESSObjectSettingAtt
                | 
                | The interface to access a CATIAEndCutESSObjectSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.end_cut_ess_object_setting_att = com_object

    @property
    def member_end_cut(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MemberEndCut() As CATBSTR
                | 
                |     Returns or sets the MemberEndCut parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.end_cut_ess_object_setting_att.MemberEndCut

    @member_end_cut.setter
    def member_end_cut(self, value: str):
        """
        :param str value:
        """

        self.end_cut_ess_object_setting_att.MemberEndCut = value

    @property
    def sfe_end_cut(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SFEEndCut() As CATBSTR

        :rtype: str
        """

        return self.end_cut_ess_object_setting_att.SFEEndCut

    @sfe_end_cut.setter
    def sfe_end_cut(self, value: str):
        """
        :param str value:
        """

        self.end_cut_ess_object_setting_att.SFEEndCut = value

    @property
    def stiffener_end_cut(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StiffenerEndCut() As CATBSTR

        :rtype: str
        """

        return self.end_cut_ess_object_setting_att.StiffenerEndCut

    @stiffener_end_cut.setter
    def stiffener_end_cut(self, value: str):
        """
        :param str value:
        """

        self.end_cut_ess_object_setting_att.StiffenerEndCut = value

    def get_member_end_cut_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMemberEndCutInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MemberEndCut
                |     parameter.
                |     Role:Retrieves the state of the MemberEndCut parameter in the current
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
        return self.end_cut_ess_object_setting_att.GetMemberEndCutInfo(io_admin_level, io_locked)

    def get_sfe_end_cut_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSFEEndCutInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SFEEndCut
                |     parameter.
                |     Role:Retrieves the state of the SFEEndCut parameter in the current
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
        return self.end_cut_ess_object_setting_att.GetSFEEndCutInfo(io_admin_level, io_locked)

    def get_stiffener_end_cut_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStiffenerEndCutInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the StiffenerEndCut
                |     parameter.
                |     Role:Retrieves the state of the StiffenerEndCut parameter in the current
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
        return self.end_cut_ess_object_setting_att.GetStiffenerEndCutInfo(io_admin_level, io_locked)

    def set_member_end_cut_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMemberEndCutLock(boolean iLocked)

        :param bool i_locked:
        :rtype: None
        """
        return self.end_cut_ess_object_setting_att.SetMemberEndCutLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_member_end_cut_lock'
        # # vba_code = """
        # # Public Function set_member_end_cut_lock(end_cut_ess_object_setting_att)
        # #     Dim iLocked (2)
        # #     end_cut_ess_object_setting_att.SetMemberEndCutLock iLocked
        # #     set_member_end_cut_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_sfe_end_cut_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSFEEndCutLock(boolean iLocked)

        :param bool i_locked:
        :rtype: None
        """
        return self.end_cut_ess_object_setting_att.SetSFEEndCutLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_sfe_end_cut_lock'
        # # vba_code = """
        # # Public Function set_sfe_end_cut_lock(end_cut_ess_object_setting_att)
        # #     Dim iLocked (2)
        # #     end_cut_ess_object_setting_att.SetSFEEndCutLock iLocked
        # #     set_sfe_end_cut_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_stiffener_end_cut_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStiffenerEndCutLock(boolean iLocked)

        :param bool i_locked:
        :rtype: None
        """
        return self.end_cut_ess_object_setting_att.SetStiffenerEndCutLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_stiffener_end_cut_lock'
        # # vba_code = """
        # # Public Function set_stiffener_end_cut_lock(end_cut_ess_object_setting_att)
        # #     Dim iLocked (2)
        # #     end_cut_ess_object_setting_att.SetStiffenerEndCutLock iLocked
        # #     set_stiffener_end_cut_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'EndCutESSObjectSettingAtt(name="{self.name}")'
