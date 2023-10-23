#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class DmuTolSettingAtt(SettingController):
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
                |                         DMUTolSettingAtt
                | 
                | Represents the DMU Tolerancing setting controller object.
                | Role: The DMU Tolerancing setting controller object deals with the setting
                | parameters displayed in:
                | 
                |     The DMU Tolerancing property page for the Related Surface Color and the
                |     Design Mode setting parameters.
                |     To access this property page:
                |         Click the Options command in the Tools menu
                |         Click + left of Digital Mockup to unfold the workbench
                |         list
                |         Click DMU Tolerancing Review
                |     The Cgr Management property page for the Save in CGR setting
                |     parameter.
                |     To access this property page:
                |         Click the Options command in the Tools menu
                |         Click + left of Infrastructure to unfold the workbench
                |         list
                |         Click Product Structure
                |         Click the Cgr Management property page
                | 
                |     The Save in CGR setting parameter represents the state of the check button
                |     named: Save FTA 3D Annotation representation in CGR.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dmu_tol_setting_att = com_object

    @property
    def design_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DesignMode() As boolean
                | 
                |     Returns or sets the Design Mode setting parameter value.
                |     True if the Design Mode setting parameter is checked and thus set to
                |     Automatic.
                |     Role: When set to True, models are loaded in Design Mode to access
                |     technological data. Otherwise, when set to False, models are loaded in
                |     Visualization Mode, and only visualization data is loaded.

        :rtype: bool
        """

        return self.dmu_tol_setting_att.DesignMode

    @design_mode.setter
    def design_mode(self, value: bool):
        """
        :param bool value:
        """

        self.dmu_tol_setting_att.DesignMode = value

    @property
    def prev_area(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PrevArea() As boolean
                | 
                |     Returns or sets the Preview Area setting parameter value.
                |     True if the Preview Area setting parameter is checked.

        :rtype: bool
        """

        return self.dmu_tol_setting_att.PrevArea

    @prev_area.setter
    def prev_area(self, value: bool):
        """
        :param bool value:
        """

        self.dmu_tol_setting_att.PrevArea = value

    @property
    def save_cgr(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SaveCGR() As boolean
                | 
                |     Returns or sets the Save in CGR setting parameter value.
                |     True if the Save in CGR setting parameter is checked.
                |     Role: When set to True, the FTA 3D Annotation representations are saved in
                |     CGR. Otherwise, they are not saved.

        :rtype: bool
        """

        return self.dmu_tol_setting_att.SaveCGR

    @save_cgr.setter
    def save_cgr(self, value: bool):
        """
        :param bool value:
        """

        self.dmu_tol_setting_att.SaveCGR = value

    @property
    def sect_pattern(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectPattern() As boolean
                | 
                |     Returns or sets the Pattern of Visu setting parameter
                |     value.
                |     True if the Pattern of Visu setting parameter is checked.
                |     Role: When set to True, the FTA 3D Annotation representations are saved in
                |     CGR. Otherwise, they are not saved.

        :rtype: bool
        """

        return self.dmu_tol_setting_att.SectPattern

    @sect_pattern.setter
    def sect_pattern(self, value: bool):
        """
        :param bool value:
        """

        self.dmu_tol_setting_att.SectPattern = value

    def get_design_mode_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDesignModeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Design Mode setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.dmu_tol_setting_att.GetDesignModeInfo(admin_level, o_locked)

    def get_prev_area_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPrevAreaInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Preview Area setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.dmu_tol_setting_att.GetPrevAreaInfo(admin_level, o_locked)

    def get_related_colours(self, o_related_r: int, o_related_g: int, o_related_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetRelatedColors(long oRelatedR,
                | long oRelatedG,
                | long oRelatedB)
                | 
                |     Retrieves the Related Surface Color setting parameter
                |     value.
                |     Role: The Related Surface Color setting parameter defines the color of the
                |     annotation related surfaces, that is, of all the surfaces referenced or
                |     toleranced using the CATIA V4 FD&T function.
                |     Legal values:The three color indexes range from 0 to 255.
                | 
                |     Parameters:
                | 
                |         oRelatedR
                |             [out] The Related Surface Color red index 
                |         oRelatedG
                |             [out] The Related Surface Color green index 
                |         oRelatedB
                |             [out] The Related Surface Color blue index

        :param int o_related_r:
        :param int o_related_g:
        :param int o_related_b:
        :rtype: None
        """
        return self.dmu_tol_setting_att.GetRelatedColors(o_related_r, o_related_g, o_related_b)

    def get_related_colours_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRelatedColorsInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Related Surface Color setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.dmu_tol_setting_att.GetRelatedColorsInfo(admin_level, o_locked)

    def get_save_cgr_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSaveCGRInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Save in CGR setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.dmu_tol_setting_att.GetSaveCGRInfo(admin_level, o_locked)

    def get_sect_pattern_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSectPatternInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Pattern of Visu setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.dmu_tol_setting_att.GetSectPatternInfo(admin_level, o_locked)

    def set_design_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDesignModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Design Mode setting parameter value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.dmu_tol_setting_att.SetDesignModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_design_mode_lock'
        # # vba_code = """
        # # Public Function set_design_mode_lock(dmu_tol_setting_att)
        # #     Dim iLocked (2)
        # #     dmu_tol_setting_att.SetDesignModeLock iLocked
        # #     set_design_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_prev_area_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPrevAreaLock(boolean iLocked)
                | 
                |     Locks or unlocks the Preview Area setting parameter value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.dmu_tol_setting_att.SetPrevAreaLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_prev_area_lock'
        # # vba_code = """
        # # Public Function set_prev_area_lock(dmu_tol_setting_att)
        # #     Dim iLocked (2)
        # #     dmu_tol_setting_att.SetPrevAreaLock iLocked
        # #     set_prev_area_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_related_colours(self, i_related_r: int, i_related_g: int, i_related_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRelatedColors(long iRelatedR,
                | long iRelatedG,
                | long iRelatedB)
                | 
                |     Sets the Related Surface Color setting parameter value.
                |     Role: The Related Surface Color setting parameter defines the color of the
                |     annotation related surfaces, that is, of all the surfaces referenced or
                |     toleranced using the CATIA V4 FD&T function.
                |     Legal values:The three color indexes range from 0 to 255.
                | 
                |     Parameters:
                | 
                |         iRelatedR
                |             [in] The Related Surface Color red index 
                |         iRelatedG
                |             [in] The Related Surface Color green index 
                |         iRelatedB
                |             [in] The Related Surface Color blue index

        :param int i_related_r:
        :param int i_related_g:
        :param int i_related_b:
        :rtype: None
        """
        return self.dmu_tol_setting_att.SetRelatedColors(i_related_r, i_related_g, i_related_b)

    def set_related_colours_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRelatedColorsLock(boolean iLocked)
                | 
                |     Locks or unlocks the Related Surface Color setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.dmu_tol_setting_att.SetRelatedColorsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_related_colors_lock'
        # # vba_code = """
        # # Public Function set_related_colors_lock(dmu_tol_setting_att)
        # #     Dim iLocked (2)
        # #     dmu_tol_setting_att.SetRelatedColorsLock iLocked
        # #     set_related_colors_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_save_cgr_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSaveCGRLock(boolean iLocked)
                | 
                |     Locks or unlocks the Save in CGR setting parameter value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.dmu_tol_setting_att.SetSaveCGRLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_save_cgr_lock'
        # # vba_code = """
        # # Public Function set_save_cgr_lock(dmu_tol_setting_att)
        # #     Dim iLocked (2)
        # #     dmu_tol_setting_att.SetSaveCGRLock iLocked
        # #     set_save_cgr_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_sect_pattern_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSectPatternLock(boolean iLocked)
                | 
                |     Locks or unlocks the Pattern of Visu setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.dmu_tol_setting_att.SetSectPatternLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_sect_pattern_lock'
        # # vba_code = """
        # # Public Function set_sect_pattern_lock(dmu_tol_setting_att)
        # #     Dim iLocked (2)
        # #     dmu_tol_setting_att.SetSectPatternLock iLocked
        # #     set_sect_pattern_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DmuTolSettingAtt(name="{self.name}")'
