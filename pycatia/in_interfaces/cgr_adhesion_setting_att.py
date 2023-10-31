#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class CgrAdhesionSettingAtt(SettingController):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         CGRAdhesionSettingAtt
                | 
                | Represents the base object to handle the parameters of the
                | cache.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cgr_adhesion_setting_att = com_object

    @property
    def v4_v5_fdt(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property V4V5_FDT() As boolean
                | 
                |     Retrieves the V4V5_FDT container activation state.

        :rtype: bool
        """

        return self.cgr_adhesion_setting_att.V4V5_FDT

    @v4_v5_fdt.setter
    def v4_v5_fdt(self, value: bool):
        """
        :param bool value:
        """

        self.cgr_adhesion_setting_att.V4V5_FDT = value

    @property
    def v4_model_comment_page(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property V4_Model_CommentPage() As boolean
                | 
                |     Retrieves the V4_Model_CommentPage container activation state.

        :rtype: bool
        """

        return self.cgr_adhesion_setting_att.V4_Model_CommentPage

    @v4_model_comment_page.setter
    def v4_model_comment_page(self, value: bool):
        """
        :param bool value:
        """

        self.cgr_adhesion_setting_att.V4_Model_CommentPage = value

    @property
    def v4_model_ln_f(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property V4_Model_LnF() As boolean
                | 
                |     Retrieves the V4_Model_LnF container activation state.

        :rtype: bool
        """

        return self.cgr_adhesion_setting_att.V4_Model_LnF

    @v4_model_ln_f.setter
    def v4_model_ln_f(self, value: bool):
        """
        :param bool value:
        """

        self.cgr_adhesion_setting_att.V4_Model_LnF = value

    @property
    def v5_spa(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property V5_SPA() As boolean
                | 
                |     Retrieves the V5_SPA container activation state.

        :rtype: bool
        """

        return self.cgr_adhesion_setting_att.V5_SPA

    @v5_spa.setter
    def v5_spa(self, value: bool):
        """
        :param bool value:
        """

        self.cgr_adhesion_setting_att.V5_SPA = value

    @property
    def voxels(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Voxels() As boolean
                | 
                |     Retrieves the Voxels container activation state.

        :rtype: bool
        """

        return self.cgr_adhesion_setting_att.Voxels

    @voxels.setter
    def voxels(self, value: bool):
        """
        :param bool value:
        """

        self.cgr_adhesion_setting_att.Voxels = value

    def get_v4_v5_fdt_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetV4V5_FDTInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the V4V5_FDT container activation
                |     state.
                |     Refer to CATSysSettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.cgr_adhesion_setting_att.GetV4V5_FDTInfo(admin_level, o_locked)

    def get_v4_model_comment_page_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetV4_Model_CommentPageInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Locks or unlocks the V4_Model_CommentPage container activation
                |     state.
                |     Refer to CATSysSettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.cgr_adhesion_setting_att.GetV4_Model_CommentPageInfo(admin_level, o_locked)

    def get_v4_model_ln_f_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetV4_Model_LnFInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the V4_Model_LnF container activation
                |     state.
                |     Refer to CATSysSettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.cgr_adhesion_setting_att.GetV4_Model_LnFInfo(admin_level, o_locked)

    def get_v5_spa_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetV5_SPAInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the V5_SPA container activation
                |     state.
                |     Refer to CATSysSettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.cgr_adhesion_setting_att.GetV5_SPAInfo(admin_level, o_locked)

    def get_voxels_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetVoxelsInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Voxels container activation
                |     state.
                |     Refer to CATSysSettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.cgr_adhesion_setting_att.GetVoxelsInfo(admin_level, o_locked)

    def set_v4_v5_fdt_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetV4V5_FDTLock(boolean iLocked)
                | 
                |     Locks or unlocks the V4V5_FDT container activation state.
                |     Refer to CATSysSettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.cgr_adhesion_setting_att.SetV4V5_FDTLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_v4_v5_fdt_lock'
        # # vba_code = """
        # # Public Function set_v4_v5_fdt_lock(cgr_adhesion_setting_att)
        # #     Dim iLocked (2)
        # #     cgr_adhesion_setting_att.SetV4V5_FDTLock iLocked
        # #     set_v4_v5_fdt_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_v4_model_comment_page_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetV4_Model_CommentPageLock(boolean iLocked)
                | 
                |     Retrieves information about the V4_Model_CommentPage container activation
                |     state.
                |     Refer to CATSysSettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.cgr_adhesion_setting_att.SetV4_Model_CommentPageLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_v4_model_comment_page_lock'
        # # vba_code = """
        # # Public Function set_v4_model_comment_page_lock(cgr_adhesion_setting_att)
        # #     Dim iLocked (2)
        # #     cgr_adhesion_setting_att.SetV4_Model_CommentPageLock iLocked
        # #     set_v4_model_comment_page_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_v4_model_ln_f_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetV4_Model_LnFLock(boolean iLocked)
                | 
                |     Locks or unlocks the V4_Model_LnF container activation
                |     state.
                |     Refer to CATSysSettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.cgr_adhesion_setting_att.SetV4_Model_LnFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_v4_model_ln_f_lock'
        # # vba_code = """
        # # Public Function set_v4_model_ln_f_lock(cgr_adhesion_setting_att)
        # #     Dim iLocked (2)
        # #     cgr_adhesion_setting_att.SetV4_Model_LnFLock iLocked
        # #     set_v4_model_ln_f_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_v5_spa_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetV5_SPALock(boolean iLocked)
                | 
                |     Locks or unlocks the V5_SPA container activation state.
                |     Refer to CATSysSettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.cgr_adhesion_setting_att.SetV5_SPALock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_v5_spa_lock'
        # # vba_code = """
        # # Public Function set_v5_spa_lock(cgr_adhesion_setting_att)
        # #     Dim iLocked (2)
        # #     cgr_adhesion_setting_att.SetV5_SPALock iLocked
        # #     set_v5_spa_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_voxels_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetVoxelsLock(boolean iLocked)
                | 
                |     Locks or unlocks the Voxels container activation state.
                |     Refer to CATSysSettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.cgr_adhesion_setting_att.SetVoxelsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_voxels_lock'
        # # vba_code = """
        # # Public Function set_voxels_lock(cgr_adhesion_setting_att)
        # #     Dim iLocked (2)
        # #     cgr_adhesion_setting_att.SetVoxelsLock iLocked
        # #     set_voxels_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'CgrAdhesionSettingAtt(name="{ self.name }")'
