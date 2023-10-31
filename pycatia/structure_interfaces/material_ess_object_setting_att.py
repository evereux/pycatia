#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class MaterialEssObjectSettingAtt(SettingController):
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
                |                         MaterialESSObjectSettingAtt
                | 
                | The interface to access a CATIAMaterialESSObjectSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.material_ess_object_setting_att = com_object

    @property
    def member_material(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MemberMaterial() As CATBSTR
                | 
                |     Returns or sets the MemberMaterial parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.material_ess_object_setting_att.MemberMaterial

    @member_material.setter
    def member_material(self, value: str):
        """
        :param str value:
        """

        self.material_ess_object_setting_att.MemberMaterial = value

    @property
    def plate_material(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PlateMaterial() As CATBSTR
                | 
                |     Returns or sets the PlateMaterial parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.material_ess_object_setting_att.PlateMaterial

    @plate_material.setter
    def plate_material(self, value: str):
        """
        :param str value:
        """

        self.material_ess_object_setting_att.PlateMaterial = value

    def get_member_material_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMemberMaterialInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MemberMaterial
                |     parameter.
                |     Role:Retrieves the state of the MemberMaterial parameter in the current
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
        return self.material_ess_object_setting_att.GetMemberMaterialInfo(io_admin_level, io_locked)

    def get_plate_material_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPlateMaterialInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PlateMaterial
                |     parameter.
                |     Role:Retrieves the state of the PlateMaterial parameter in the current
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
        return self.material_ess_object_setting_att.GetPlateMaterialInfo(io_admin_level, io_locked)

    def set_member_material_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMemberMaterialLock(boolean iLocked)
                | 
                |     Locks or unlocks the MemberMaterial parameter.
                |     Role:Locks or unlocks the MemberMaterial parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
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
        return self.material_ess_object_setting_att.SetMemberMaterialLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_member_material_lock'
        # # vba_code = """
        # # Public Function set_member_material_lock(material_ess_object_setting_att)
        # #     Dim iLocked (2)
        # #     material_ess_object_setting_att.SetMemberMaterialLock iLocked
        # #     set_member_material_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_plate_material_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPlateMaterialLock(boolean iLocked)
                | 
                |     Locks or unlocks the PlateMaterial parameter.
                |     Role:Locks or unlocks the PlateMaterial parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
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
        return self.material_ess_object_setting_att.SetPlateMaterialLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_plate_material_lock'
        # # vba_code = """
        # # Public Function set_plate_material_lock(material_ess_object_setting_att)
        # #     Dim iLocked (2)
        # #     material_ess_object_setting_att.SetPlateMaterialLock iLocked
        # #     set_plate_material_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MaterialEssObjectSettingAtt(name="{self.name}")'
