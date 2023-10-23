#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class LanguageSheetSettingAtt(SettingController):

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
                |                         LanguageSheetSettingAtt
                | 
                | The interface to access a CATIALanguageSheetSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.language_sheet_setting_att = com_object

    @property
    def knowledge_build_path_directory(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property KnowledgeBuildPathDirectory() As CATBSTR
                | 
                |     Returns or sets the CATKnowledgeBuildPath setting
                |     parameter.
                |     Role:Return or Set the CATKnowledgeBuildPath parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oKnowledgeBuildPathDirectory
                |             The knowledge build path directory: the path where all the
                |             resources are located.

        :rtype: str
        """

        return self.language_sheet_setting_att.KnowledgeBuildPathDirectory

    @knowledge_build_path_directory.setter
    def knowledge_build_path_directory(self, value: str):
        """
        :param str value:
        """

        self.language_sheet_setting_att.KnowledgeBuildPathDirectory = value

    @property
    def list_of_packages_to_load(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ListOfPackagesToLoad() As CATBSTR
                | 
                |     Returns or sets the ListOfPackagesToLoad parameter.
                |     Role:Return or Set the ListOfPackagesToLoad parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oListOfPackagesToLoad
                |             The list of packages to load.

        :rtype: str
        """

        return self.language_sheet_setting_att.ListOfPackagesToLoad

    @list_of_packages_to_load.setter
    def list_of_packages_to_load(self, value: str):
        """
        :param str value:
        """

        self.language_sheet_setting_att.ListOfPackagesToLoad = value

    @property
    def load_all_packages(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LoadAllPackages() As short
                | 
                |     Returns or sets the LoadAllPackages parameter.
                |     Role:Return or Set the LoadAllPackages parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oLoadAllPackages
                |             Legal values:
                |             0 : to not load all packages
                |             1 : to load all packages.

        :rtype: int
        """

        return self.language_sheet_setting_att.LoadAllPackages

    @load_all_packages.setter
    def load_all_packages(self, value: int):
        """
        :param int value:
        """

        self.language_sheet_setting_att.LoadAllPackages = value

    @property
    def load_extended_language_lib(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LoadExtendedLanguageLib() As short
                | 
                |     Returns or sets the LoadExtendedLanguageLib parameter.
                |     Role:Return or Set the LoadExtendedLanguageLib parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         oLoadExtendedLanguageLib
                |             Legal values:
                |             0 : to not use extended libraries
                |             1 : to use extended libraries.

        :rtype: int
        """

        return self.language_sheet_setting_att.LoadExtendedLanguageLib

    @load_extended_language_lib.setter
    def load_extended_language_lib(self, value: int):
        """
        :param int value:
        """

        self.language_sheet_setting_att.LoadExtendedLanguageLib = value

    @property
    def reference_directory_for_types(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ReferenceDirectoryForTypes() As CATBSTR
                | 
                |     Returns or sets the ReferenceDirectoryForTypes parameter.
                |     Role:Return or Set the ReferenceDirectoryForTypes parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         oReferenceDirectoryForTypes
                |             The reference directory for types.

        :rtype: str
        """

        return self.language_sheet_setting_att.ReferenceDirectoryForTypes

    @reference_directory_for_types.setter
    def reference_directory_for_types(self, value: str):
        """
        :param str value:
        """

        self.language_sheet_setting_att.ReferenceDirectoryForTypes = value

    def get_knowledge_build_path_directory_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetKnowledgeBuildPathDirectoryInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the CATKnowledgeBuildPath setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.language_sheet_setting_att.GetKnowledgeBuildPathDirectoryInfo(io_admin_level, io_locked)

    def get_list_of_packages_to_load_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetListOfPackagesToLoadInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ListOfPackagesToLoad setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.language_sheet_setting_att.GetListOfPackagesToLoadInfo(io_admin_level, io_locked)

    def get_load_all_packages_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLoadAllPackagesInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the LoadAllPackages setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.language_sheet_setting_att.GetLoadAllPackagesInfo(io_admin_level, io_locked)

    def get_load_extended_language_lib_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLoadExtendedLanguageLibInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the LoadExtendedLanguageLib setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.language_sheet_setting_att.GetLoadExtendedLanguageLibInfo(io_admin_level, io_locked)

    def get_reference_directory_for_types_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetReferenceDirectoryForTypesInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ReferenceDirectoryForTypes setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.language_sheet_setting_att.GetReferenceDirectoryForTypesInfo(io_admin_level, io_locked)

    def set_knowledge_build_path_directory_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetKnowledgeBuildPathDirectoryLock(boolean iLocked)
                | 
                |     Locks or unlocks the CATKnowledgeBuildPath setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.language_sheet_setting_att.SetKnowledgeBuildPathDirectoryLock(i_locked)

    def set_list_of_packages_to_load_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetListOfPackagesToLoadLock(boolean iLocked)
                | 
                |     Locks or unlocks the ListOfPackagesToLoad setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.language_sheet_setting_att.SetListOfPackagesToLoadLock(i_locked)

    def set_load_all_packages_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLoadAllPackagesLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadAllPackages setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.language_sheet_setting_att.SetLoadAllPackagesLock(i_locked)

    def set_load_extended_language_lib_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLoadExtendedLanguageLibLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadExtendedLanguageLib setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.language_sheet_setting_att.SetLoadExtendedLanguageLibLock(i_locked)

    def set_reference_directory_for_types_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetReferenceDirectoryForTypesLock(boolean iLocked)
                | 
                |     Locks or unlocks the ReferenceDirectoryForTypes setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.language_sheet_setting_att.SetReferenceDirectoryForTypesLock(i_locked)

    def __repr__(self):
        return f'LanguageSheetSettingAtt(name="{self.name}")'
