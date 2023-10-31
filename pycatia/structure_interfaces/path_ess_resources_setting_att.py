#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class PathEssResourcesSettingAtt(SettingController):
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
                |                         PathESSRessourcesSettingAtt
                | 
                | The interface to access a CATIAPathESSRessourcesSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.path_ess_resources_setting_att = com_object

    @property
    def resolved_sections_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ResolvedSectionsPath() As CATBSTR
                | 
                |     Returns or sets the ResolvedSectionsPath parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.path_ess_resources_setting_att.ResolvedSectionsPath

    @resolved_sections_path.setter
    def resolved_sections_path(self, value: str):
        """
        :param str value:
        """

        self.path_ess_resources_setting_att.ResolvedSectionsPath = value

    @property
    def sections_catalog_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectionsCatalogPath() As CATBSTR
                | 
                |     Returns or sets the SectionsCatalogPath parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.path_ess_resources_setting_att.SectionsCatalogPath

    @sections_catalog_path.setter
    def sections_catalog_path(self, value: str):
        """
        :param str value:
        """

        self.path_ess_resources_setting_att.SectionsCatalogPath = value

    @property
    def thickness_list_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ThicknessListPath() As CATBSTR
                | 
                |     Returns or sets the ThicknessListPath parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.path_ess_resources_setting_att.ThicknessListPath

    @thickness_list_path.setter
    def thickness_list_path(self, value: str):
        """
        :param str value:
        """

        self.path_ess_resources_setting_att.ThicknessListPath = value

    def get_resolved_sections_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetResolvedSectionsPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ResolvedSectionsPath
                |     parameter.
                |     Role:Retrieves the state of the ResolvedSectionsPath parameter in the
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
        return self.path_ess_resources_setting_att.GetResolvedSectionsPathInfo(io_admin_level, io_locked)

    def get_sections_catalog_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSectionsCatalogPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SectionsCatalogPath
                |     parameter.
                |     Role:Retrieves the state of the SectionsCatalogPath parameter in the
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
        return self.path_ess_resources_setting_att.GetSectionsCatalogPathInfo(io_admin_level, io_locked)

    def get_thickness_list_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetThicknessListPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ThicknessListPath
                |     parameter.
                |     Role:Retrieves the state of the ThicknessListPath parameter in the current
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
        return self.path_ess_resources_setting_att.GetThicknessListPathInfo(io_admin_level, io_locked)

    def set_resolved_sections_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetResolvedSectionsPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the ResolvedSectionsPath parameter.
                |     Role:Locks or unlocks the ResolvedSectionsPath parameter if it is possible
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
        return self.path_ess_resources_setting_att.SetResolvedSectionsPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_resolved_sections_path_lock'
        # # vba_code = """
        # # Public Function set_resolved_sections_path_lock(path_ess_ressources_setting_att)
        # #     Dim iLocked (2)
        # #     path_ess_ressources_setting_att.SetResolvedSectionsPathLock iLocked
        # #     set_resolved_sections_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_sections_catalog_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSectionsCatalogPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the SectionsCatalogPath parameter.
                |     Role:Locks or unlocks the SectionsCatalogPath parameter if it is possible
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
        return self.path_ess_resources_setting_att.SetSectionsCatalogPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_sections_catalog_path_lock'
        # # vba_code = """
        # # Public Function set_sections_catalog_path_lock(path_ess_ressources_setting_att)
        # #     Dim iLocked (2)
        # #     path_ess_ressources_setting_att.SetSectionsCatalogPathLock iLocked
        # #     set_sections_catalog_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_thickness_list_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetThicknessListPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the ThicknessListPath parameter.
                |     Role:Locks or unlocks the ThicknessListPath parameter if it is possible in
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
        return self.path_ess_resources_setting_att.SetThicknessListPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_thickness_list_path_lock'
        # # vba_code = """
        # # Public Function set_thickness_list_path_lock(path_ess_ressources_setting_att)
        # #     Dim iLocked (2)
        # #     path_ess_ressources_setting_att.SetThicknessListPathLock iLocked
        # #     set_thickness_list_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PathEssResourcesSettingAtt(name="{self.name}")'
