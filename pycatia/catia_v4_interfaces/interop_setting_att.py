#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class InteropSettingAtt(SettingController):
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
                |                         InteropSettingAtt
                | 
                | Represents the object to handle the setting parameters of the "V4 Data Reading"
                | tab page.
                | Role: This interface is implemented by a component named
                | CATV4IInteropSettingCtrl which represents the controller of the Setting. The
                | setting parameters of the tab are the following:
                | 
                |     "Display only elements with Sensitive Attribute"
                |     "Display 3D elements labels"
                |     "Open in Light Mode: 2D Data are not taken into account"
                |     "Reading Code page"
                |     "PROJECT File Path"
                |     "DLNAME"
                |     "Prj Warn"
                |     "Characters Equivalence Table Path"
                | 
                | To access this property page:
                | 
                |     Click the Options command in the Tools menu
                |     Click + left of General to unfold the workbench list
                |     Click Compatibility
                |
                | This interface defines:
                | 
                |     A method to get each parameter
                |     A method to set the value of each parameter
                |     A method to lock/unlock each parameter
                |     A method to retrieve the informations concerning each
                |     parameter
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.interop_setting_att = com_object

    @property
    def code_page(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Code_page() As CATBSTR
                | 
                |     Retrieves or sets the value of the "Reading Code page" setting
                |     parameter.
                |     Role: The "Reading Code page" declares the language to identify the data
                |     read if this data is not labeled. It is stored in the CATIA data to be written
                |     when saving Version 5 CATPart documents as CATIA Version 4 models.

        :rtype: str
        """

        return self.interop_setting_att.Code_page

    @code_page.setter
    def code_page(self, value: str):
        """
        :param str value:
        """

        self.interop_setting_att.Code_page = value

    @property
    def conversion_table(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Conversion_Table() As CATBSTR
                | 
                |     Retrieves the location of the "Characters Equivalence Table Path" setting
                |     parameter.
                |     Role: The "Characters Equivalence Table" allows to convert characters
                |     contained in CATIA V4 documents. It is mainly used to generate V5 compliant
                |     names from V4 names by replacing special characters (", *, /, etc...) by
                |     standard characters.

        :rtype: str
        """

        return self.interop_setting_att.Conversion_Table

    @conversion_table.setter
    def conversion_table(self, value: str):
        """
        :param str value:
        """

        self.interop_setting_att.Conversion_Table = value

    @property
    def display_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DisplayMode() As boolean
                | 
                |     Retrieves or sets the state of the "Display only elements with Sensitive
                |     Attribute" setting parameter.
                |     Role: The "Display only elements with Sensitive Attribute" mode enables you
                |     to decide whether to display or not the elements which were sensitive to the
                |     shading mode in CATIA Version 4.

        :rtype: bool
        """

        return self.interop_setting_att.DisplayMode

    @display_mode.setter
    def display_mode(self, value: bool):
        """
        :param bool value:
        """

        self.interop_setting_att.DisplayMode = value

    @property
    def display_v4_text_3d(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DisplayV4Text3D() As boolean
                | 
                |     Retrieves or sets the state of the "Display 3D elements labels" setting
                |     parameter.
                |     Role: The "Display 3D elements labels" mode is activated in order to enable
                |     the reading of the 3D text associated to the V4 elements.

        :rtype: bool
        """

        return self.interop_setting_att.DisplayV4Text3D

    @display_v4_text_3d.setter
    def display_v4_text_3d(self, value: bool):
        """
        :param bool value:
        """

        self.interop_setting_att.DisplayV4Text3D = value

    @property
    def dlname(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Dlname() As CATBSTR
                | 
                |     Retrieves or sets the "DLNAME" setting parameter.
                |     Role: Retrieves the DLNAME referenced by the Model.

        :rtype: str
        """

        return self.interop_setting_att.Dlname

    @dlname.setter
    def dlname(self, value: str):
        """
        :param str value:
        """

        self.interop_setting_att.Dlname = value

    @property
    def draw(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Draw() As CATBSTR
                | 
                |     Retrieves or sets the state of the "Open in Light Mode: 2D Data are not
                |     taken into account" setting parameter.
                |     Role: This mode is activated in order to disable the reading of DRAW data
                |     in a V4 Model.

        :rtype: str
        """

        return self.interop_setting_att.Draw

    @draw.setter
    def draw(self, value: str):
        """
        :param str value:
        """

        self.interop_setting_att.Draw = value

    @property
    def project_file_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PROJECT_File_Path() As CATBSTR
                | 
                |     Retrieves or sets the value of the "PROJECT File Path" setting
                |     parameter.
                |     Role: The "PROJECT File Path" field contains the location of the external
                |     project file referenced by the V4 model.

        :rtype: str
        """

        return self.interop_setting_att.PROJECT_File_Path

    @project_file_path.setter
    def project_file_path(self, value: str):
        """
        :param str value:
        """

        self.interop_setting_att.PROJECT_File_Path = value

    def get_code_page_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCode_pageInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "Reading Code page" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.interop_setting_att.GetCode_pageInfo(admin_level, o_locked)

    def get_conversion_table_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetConversion_TableInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "Characters Equivalence Table Path" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.interop_setting_att.GetConversion_TableInfo(admin_level, o_locked)

    def get_display_mode_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDisplayModeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "Display only elements with Sensitive
                |     Attribute" setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.interop_setting_att.GetDisplayModeInfo(admin_level, o_locked)

    def get_display_v4_text_3d_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDisplayV4Text3DInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "Display 3D elements labels" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.interop_setting_att.GetDisplayV4Text3DInfo(admin_level, o_locked)

    def get_dlname_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDlnameInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "DlNAME" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.interop_setting_att.GetDlnameInfo(admin_level, o_locked)

    def get_draw_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDrawInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "Open in Light Mode: 2D Data are not taken
                |     into account" setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.interop_setting_att.GetDrawInfo(admin_level, o_locked)

    def get_project_file_path_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPROJECT_File_PathInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "PROJECT File Path" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.interop_setting_att.GetPROJECT_File_PathInfo(admin_level, o_locked)

    def set_code_page_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCode_pageLock(boolean iLock)
                | 
                |     Locks or unlocks the "Reading Code page" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.interop_setting_att.SetCode_pageLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_code_page_lock'
        # # vba_code = """
        # # Public Function set_code_page_lock(interop_setting_att)
        # #     Dim iLock (2)
        # #     interop_setting_att.SetCode_pageLock iLock
        # #     set_code_page_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_conversion_table_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetConversion_TableLock(boolean iLock)
                | 
                |     Locks or unlocks the "Characters Equivalence Table Path" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.interop_setting_att.SetConversion_TableLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_conversion_table_lock'
        # # vba_code = """
        # # Public Function set_conversion_table_lock(interop_setting_att)
        # #     Dim iLock (2)
        # #     interop_setting_att.SetConversion_TableLock iLock
        # #     set_conversion_table_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_mode_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDisplayModeLock(boolean iLock)
                | 
                |     Retrieves information about the "Display only elements with Sensitive
                |     Attribute" setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.interop_setting_att.SetDisplayModeLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_mode_lock'
        # # vba_code = """
        # # Public Function set_display_mode_lock(interop_setting_att)
        # #     Dim iLock (2)
        # #     interop_setting_att.SetDisplayModeLock iLock
        # #     set_display_mode_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_v4_text_3d_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDisplayV4Text3DLock(boolean iLock)
                | 
                |     Locks or unlocks the "Display 3D elements labels" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.interop_setting_att.SetDisplayV4Text3DLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_v4_text3_d_lock'
        # # vba_code = """
        # # Public Function set_display_v4_text3_d_lock(interop_setting_att)
        # #     Dim iLock (2)
        # #     interop_setting_att.SetDisplayV4Text3DLock iLock
        # #     set_display_v4_text3_d_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dlname_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDlnameLock(boolean iLock)
                | 
                |     Locks or unlocks the "DLNAME" setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.interop_setting_att.SetDlnameLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dlname_lock'
        # # vba_code = """
        # # Public Function set_dlname_lock(interop_setting_att)
        # #     Dim iLock (2)
        # #     interop_setting_att.SetDlnameLock iLock
        # #     set_dlname_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_draw_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDrawLock(boolean iLock)
                | 
                |     Locks or unlocks the "Open in Light Mode: 2D Data are not taken into
                |     account" setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.interop_setting_att.SetDrawLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_draw_lock'
        # # vba_code = """
        # # Public Function set_draw_lock(interop_setting_att)
        # #     Dim iLock (2)
        # #     interop_setting_att.SetDrawLock iLock
        # #     set_draw_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_project_file_path_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPROJECT_File_PathLock(boolean iLock)
                | 
                |     Locks or unlocks the "PROJECT File Path" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.interop_setting_att.SetPROJECT_File_PathLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_project_file_path_lock'
        # # vba_code = """
        # # Public Function set_project_file_path_lock(interop_setting_att)
        # #     Dim iLock (2)
        # #     interop_setting_att.SetPROJECT_File_PathLock iLock
        # #     set_project_file_path_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'InteropSettingAtt(name="{self.name}")'
