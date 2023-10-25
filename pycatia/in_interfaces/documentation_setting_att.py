#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class DocumentationSettingAtt(SettingController):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         DocumentationSettingAtt
                | 
                | Setting controller for the Help property tab page.
                | Role: This interface is implemented by a component which represents the
                | controller of the documentation settings.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.documentation_setting_att = com_object

    @property
    def companion_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CompanionPath() As CATBSTR
                | 
                |     Returns the User Companion location (path) parameter.

        :rtype: str
        """

        return self.documentation_setting_att.CompanionPath

    @companion_path.setter
    def companion_path(self, value: str):
        """
        :param str value:
        """

        self.documentation_setting_att.CompanionPath = value

    @property
    def doc_language(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DocLanguage() As long
                | 
                |     Returns the technical documentation language parameter.

        :rtype: int
        """

        return self.documentation_setting_att.DocLanguage

    @doc_language.setter
    def doc_language(self, value: int):
        """
        :param int value:
        """

        self.documentation_setting_att.DocLanguage = value

    @property
    def priority(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Priority() As CATDocContextualPriority
                | 
                |     Returns the contextual priority parameter.

        :return: enum cat_doc_contextual_priority
        :rtype: int
        """

        return self.documentation_setting_att.Priority

    @priority.setter
    def priority(self, value: int):
        """
        :param int value: enum cat_doc_contextual_priority
        """

        self.documentation_setting_att.Priority = value

    @property
    def technical_documentation_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TechnicalDocumentationPath() As CATBSTR
                | 
                |     Returns the technical documentation location (path) parameter.

        :rtype: str
        """

        return self.documentation_setting_att.TechnicalDocumentationPath

    @technical_documentation_path.setter
    def technical_documentation_path(self, value: str):
        """
        :param str value:
        """

        self.documentation_setting_att.TechnicalDocumentationPath = value

    def get_companion_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetCompanionPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the User Companion location
                |     parameter.
                |     Role:Retrieves the state of the User Companion location parameter in the
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
        return self.documentation_setting_att.GetCompanionPathInfo(io_admin_level, io_locked)

    def get_doc_language_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDocLanguageInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the technical documentation language
                |     parameter.
                |     Role:Retrieves the state of the technical documentation language parameter
                |     in the current environment.
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
        return self.documentation_setting_att.GetDocLanguageInfo(io_admin_level, io_locked)

    def get_priority_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPriorityInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the contextual priority
                |     parameter.
                |     Role:Retrieves the state of the contextual priority parameter in the
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
        return self.documentation_setting_att.GetPriorityInfo(io_admin_level, io_locked)

    def get_technical_documentation_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetTechnicalDocumentationPathInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the technical documentation location
                |     parameter.
                |     Role:Retrieves the state of the technical documentation location parameter
                |     in the current environment.
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
        return self.documentation_setting_att.GetTechnicalDocumentationPathInfo(io_admin_level, io_locked)

    def set_companion_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetCompanionPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the User Companion location parameter.
                |     Role:Locks or unlocks the User Companion location parameter if it is
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
        return self.documentation_setting_att.SetCompanionPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_companion_path_lock'
        # # vba_code = """
        # # Public Function set_companion_path_lock(documentation_setting_att)
        # #     Dim iLocked (2)
        # #     documentation_setting_att.SetCompanionPathLock iLocked
        # #     set_companion_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_doc_language_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDocLanguageLock(boolean iLocked)
                | 
                |     Locks or unlocks the technical documentation language
                |     parameter.
                |     Role:Locks or unlocks the technical documentation language parameter if it
                |     is possible in the current administrative context. In user mode this method
                |     will always return E_FAIL.
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
        return self.documentation_setting_att.SetDocLanguageLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_doc_language_lock'
        # # vba_code = """
        # # Public Function set_doc_language_lock(documentation_setting_att)
        # #     Dim iLocked (2)
        # #     documentation_setting_att.SetDocLanguageLock iLocked
        # #     set_doc_language_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_priority_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPriorityLock(boolean iLocked)
                | 
                |     Locks or unlocks the contextual priority parameter.
                |     Role:Locks or unlocks the contextual priority parameter if it is possible
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
        return self.documentation_setting_att.SetPriorityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_priority_lock'
        # # vba_code = """
        # # Public Function set_priority_lock(documentation_setting_att)
        # #     Dim iLocked (2)
        # #     documentation_setting_att.SetPriorityLock iLocked
        # #     set_priority_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_technical_documentation_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTechnicalDocumentationPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the technical documentation location
                |     parameter.
                |     Role:Locks or unlocks the technical documentation location parameter if it
                |     is possible in the current administrative context. In user mode this method
                |     will always return E_FAIL.
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
        return self.documentation_setting_att.SetTechnicalDocumentationPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_technical_documentation_path_lock'
        # # vba_code = """
        # # Public Function set_technical_documentation_path_lock(documentation_setting_att)
        # #     Dim iLocked (2)
        # #     documentation_setting_att.SetTechnicalDocumentationPathLock iLocked
        # #     set_technical_documentation_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DocumentationSettingAtt(name="{self.name}")'
