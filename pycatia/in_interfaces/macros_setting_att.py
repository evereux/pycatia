#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class MacrosSettingAtt(SettingController):
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
                |                         MacrosSettingAtt
                | 
                | Setting controller for the Macros tab page.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.macros_setting_att = com_object

    def get_default_macro_libraries(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDefaultMacroLibraries() As CATSafeArrayVariant
                | 
                |     Returns the list of default macro libraries.

        :rtype: tuple
        """
        return self.macros_setting_att.GetDefaultMacroLibraries()

    def get_default_macro_libraries_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDefaultMacroLibrariesInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the default macro libraries
                |     setting.
                |     Role:Retrieves the state of the parameter default macro libraries setting
                |     in the current environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.macros_setting_att.GetDefaultMacroLibrariesInfo(admin_level, o_locked)

    def get_external_references(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetExternalReferences() As CATSafeArrayVariant
                | 
                |     Returns the list of external references.

        :rtype: tuple
        """
        return self.macros_setting_att.GetExternalReferences()

    def get_external_references_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetExternalReferencesInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the external references
                |     setting.
                |     Role:Retrieves the state of the parameter external references setting in
                |     the current environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.macros_setting_att.GetExternalReferencesInfo(admin_level, o_locked)

    def get_language_editor(self, i_language: int) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLanguageEditor(CATScriptLanguage iLanguage) As
                | CATBSTR
                | 
                |     Returns the editor path for the specified language.

        :param int i_language: enum cat_script_language
        :rtype: str
        """
        return self.macros_setting_att.GetLanguageEditor(i_language)

    def get_language_editor_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLanguageEditorInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the language editors
                |     setting.
                |     Role:Retrieves the state of the parameter language editors setting in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.macros_setting_att.GetLanguageEditorInfo(admin_level, o_locked)

    def set_default_macro_libraries(self, i_libraries: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDefaultMacroLibraries(CATSafeArrayVariant
                | iLibraries)
                | 
                |     Sets the list of default macro libraries.

        :param tuple i_libraries:
        :rtype: None
        """
        return self.macros_setting_att.SetDefaultMacroLibraries(i_libraries)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_macro_libraries'
        # # vba_code = """
        # # Public Function set_default_macro_libraries(macros_setting_att)
        # #     Dim iLibraries (2)
        # #     macros_setting_att.SetDefaultMacroLibraries iLibraries
        # #     set_default_macro_libraries = iLibraries
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_default_macro_libraries_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDefaultMacroLibrariesLock(boolean iLocked)
                | 
                |     Locks or unlocks the default macro libraries setting.
                |     Role:Locks or unlocks the default macro libraries setting if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             True : to lock the parameter.
                |             False: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.macros_setting_att.SetDefaultMacroLibrariesLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_macro_libraries_lock'
        # # vba_code = """
        # # Public Function set_default_macro_libraries_lock(macros_setting_att)
        # #     Dim iLocked (2)
        # #     macros_setting_att.SetDefaultMacroLibrariesLock iLocked
        # #     set_default_macro_libraries_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_external_references(self, i_references: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExternalReferences(CATSafeArrayVariant iReferences)
                | 
                |     Sets the list of external references.

        :param tuple i_references:
        :rtype: None
        """
        return self.macros_setting_att.SetExternalReferences(i_references)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_external_references'
        # # vba_code = """
        # # Public Function set_external_references(macros_setting_att)
        # #     Dim iReferences (2)
        # #     macros_setting_att.SetExternalReferences iReferences
        # #     set_external_references = iReferences
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_external_references_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExternalReferencesLock(boolean iLocked)
                | 
                |     Locks or unlocks the external references setting.
                |     Role:Locks or unlocks the external references setting if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             True : to lock the parameter.
                |             False: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.macros_setting_att.SetExternalReferencesLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_external_references_lock'
        # # vba_code = """
        # # Public Function set_external_references_lock(macros_setting_att)
        # #     Dim iLocked (2)
        # #     macros_setting_att.SetExternalReferencesLock iLocked
        # #     set_external_references_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_language_editor(self, i_language: int, i_editor_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLanguageEditor(CATScriptLanguage iLanguage,
                | CATBSTR iEditorPath)
                | 
                |     Sets the editor path for the specified language.

        :param int i_language: enum cat_script_language
        :param str i_editor_path:
        :rtype: None
        """
        return self.macros_setting_att.SetLanguageEditor(i_language, i_editor_path)

    def set_language_editor_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLanguageEditorLock(boolean iLocked)
                | 
                |     Locks or unlocks the language editors setting.
                |     Role:Locks or unlocks the language editors setting if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             True : to lock the parameter.
                |             False: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.macros_setting_att.SetLanguageEditorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_language_editor_lock'
        # # vba_code = """
        # # Public Function set_language_editor_lock(macros_setting_att)
        # #     Dim iLocked (2)
        # #     macros_setting_att.SetLanguageEditorLock iLocked
        # #     set_language_editor_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MacrosSettingAtt(name="{self.name}")'
