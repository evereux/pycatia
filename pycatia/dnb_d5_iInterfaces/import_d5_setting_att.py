#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class ImportD5SettingAtt(SettingController):
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
                |                         ImportD5SettingAtt
                | 
                | Interface to handle parameters of General-Compatibility-DELMIA D5 Tools Options
                | Tab page.
                | Role: This interface is implemented by a component which represents the
                | controller of DELMIA D5 Tools Options parameter settings.
                | 
                |     Methods to set value of each parameter xxx
                |     Methods to get value of each parameter xxx
                |     Methods to get information on each parameter xxx
                |     Methods to lock/unlock value of each parameter xxx
                | 
                | Here are the list of parameters to use and their meanings:
                | 
                |     ImportLibrary: define the D5 root libraries. For several libraries, they
                |     are separated by the character ;.
                |         D:/Syslib;D:/Robotlib; for Windows
                |         /usr/deneb/Syslib;/usr/deneb/Robotlib; for UNIX 
                |     ImportConfigFile: defines the configuration file to
                |     append.
                |     ImportConfigFile: defines the configuration file to
                |     append.
                |     ImportPDBCache : defines the D5 pdb cache directory for UG files.
                |     ImportRecording : defines the option for importing D5 recording file into V5 replays.
                |     ImportUserViews : defines the option for importing D5 user views into V5 cameras.
                |         For workcells only.
                |     ImportAnnotation: defines the option for importing D5 annotations into V5
                |     3D annotations. For workcells only.
                |     ImportWclMessage: defines the option for displaying the D5 workcell
                |         messages after importing. Message is stored on the product. For workcells only.
                |     ImportCollision : defines the option for importing D5 collision queues into V5
                |         interferences objects. For workcells only.
                |     ImportFloor : defines the option for importing D5 floor into V5 Area. For workcells only.
                |     ImportUserAttr : defines the option for importing D5 user attributes into V5 knowledgeware
                |         parameters.
                |     ImportEdge : defines the option for importing D5 geometric (edge) information.
                |     ImportCoorsys : defines the option for importing D5 coorsys into V5 frames of interests
                |         (by default as DESIGN).
                |     ImportToolFrm : defines the option for importing D5 tool frame into V5 frames of interests
                |         (by default as TOOL).
                |     ImportBaseFrm : defines the option for importing D5 base frame into V5 base frames of interests
                |         (by default as BASE).
                |     ImportWclPath : defines the option for importing D5 workcell paths into V5 frames of interests
                |         (by default as MANUFACTURING).
                |     VisCoorsys : defines the visibility status at the import of D5 coorsys.
                |     VisToolFrm : defines the visibility status at the import of D5 tool frame.
                |     VisBaseFrm : defines the visibility status at the import of D5 base frame.
                |     VisWclPath : defines the visibility status at the import of D5 workcell paths.
                |     TypeCoorsys : defines the V5 frame of interest matching type when importing D5 coorsys.
                |     TypeToolFrm : defines the V5 frame of interest matching type when importing D5 tool frame.
                |     TypeBaseFrm : defines the V5 frame of interest matching type when importing D5 base frame.
                |     TypeWclPath : defines the V5 frame of interest matching type when importing D5 workcell paths.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.import_d5_setting_att = com_object

    def get_import_annotation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportAnnotationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportAnnotation
                |     parameter.
                |     Role:Retrieves the state of the ImportAnnotation parameter in the current
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
        return self.import_d5_setting_att.GetImportAnnotationInfo(io_admin_level, io_locked)

    def get_import_base_frm_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportBaseFrmInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportBaseFrm
                |     parameter.
                |     Role:Retrieves the state of the ImportBaseFrm parameter in the current
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
        return self.import_d5_setting_att.GetImportBaseFrmInfo(io_admin_level, io_locked)

    def get_import_collision_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportCollisionInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportCollision
                |     parameter.
                |     Role:Retrieves the state of the ImportCollision parameter in the current
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
        return self.import_d5_setting_att.GetImportCollisionInfo(io_admin_level, io_locked)

    def get_import_config_file_expanded(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportConfigFileExpanded() As CATBSTR
                | 
                |     Returns the ImportConfigFile parameter (manages expanded file
                |     pathnames).
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """
        return self.import_d5_setting_att.GetImportConfigFileExpanded()

    def get_import_config_file_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportConfigFileInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportConfigFile
                |     parameter.
                |     Role:Retrieves the state of the ImportConfigFile parameter in the current
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
        return self.import_d5_setting_att.GetImportConfigFileInfo(io_admin_level, io_locked)

    def get_import_coorsys_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportCoorsysInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportCoorsys
                |     parameter.
                |     Role:Retrieves the state of the ImportCoorsys parameter in the current
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
        return self.import_d5_setting_att.GetImportCoorsysInfo(io_admin_level, io_locked)

    def get_import_edge_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportEdgeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportEdge
                |     parameter.
                |     Role:Retrieves the state of the ImportEdge parameter in the current
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
        return self.import_d5_setting_att.GetImportEdgeInfo(io_admin_level, io_locked)

    def get_import_floor_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportFloorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportFloor
                |     parameter.
                |     Role:Retrieves the state of the ImportFloor parameter in the current
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
        return self.import_d5_setting_att.GetImportFloorInfo(io_admin_level, io_locked)

    def get_import_library_expanded(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportLibraryExpanded() As CATBSTR
                | 
                |     Returns the ImportLibrary parameter (manages expanded file
                |     pathnames).
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """
        return self.import_d5_setting_att.GetImportLibraryExpanded()

    def get_import_library_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportLibraryInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportLibrary
                |     parameter.
                |     Role:Retrieves the state of the ImportLibrary parameter in the current
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
        return self.import_d5_setting_att.GetImportLibraryInfo(io_admin_level, io_locked)

    def get_import_pdb_cache_expanded(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportPDBCacheExpanded() As CATBSTR
                | 
                |     Returns the ImportPDBCache parameter (manages expanded file
                |     pathnames).
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """
        return self.import_d5_setting_att.GetImportPDBCacheExpanded()

    def get_import_pdb_cache_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportPDBCacheInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportPDBCache
                |     parameter.
                |     Role:Retrieves the state of the ImportPDBCache parameter in the current
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
        return self.import_d5_setting_att.GetImportPDBCacheInfo(io_admin_level, io_locked)

    def get_import_recording_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportRecordingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportRecording
                |     parameter.
                |     Role:Retrieves the state of the ImportRecording parameter in the current
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
        return self.import_d5_setting_att.GetImportRecordingInfo(io_admin_level, io_locked)

    def get_import_tool_frm_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportToolFrmInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportToolFrm
                |     parameter.
                |     Role:Retrieves the state of the ImportToolFrm parameter in the current
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
        return self.import_d5_setting_att.GetImportToolFrmInfo(io_admin_level, io_locked)

    def get_import_user_attr_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportUserAttrInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportUserAttr
                |     parameter.
                |     Role:Retrieves the state of the ImportUserAttr parameter in the current
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
        return self.import_d5_setting_att.GetImportUserAttrInfo(io_admin_level, io_locked)

    def get_import_user_views_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportUserViewsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportUserViews
                |     parameter.
                |     Role:Retrieves the state of the ImportUserViews parameter in the current
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
        return self.import_d5_setting_att.GetImportUserViewsInfo(io_admin_level, io_locked)

    def get_import_wcl_message_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportWclMessageInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportWclMessage
                |     parameter.
                |     Role:Retrieves the state of the ImportWclMessage parameter in the current
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
        return self.import_d5_setting_att.GetImportWclMessageInfo(io_admin_level, io_locked)

    def get_import_wcl_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportWclPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImportWclPath
                |     parameter.
                |     Role:Retrieves the state of the ImportWclPath parameter in the current
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
        return self.import_d5_setting_att.GetImportWclPathInfo(io_admin_level, io_locked)

    def get_type_base_frm_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTypeBaseFrmInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TypeBaseFrm
                |     parameter.
                |     Role:Retrieves the state of the TypeBaseFrm parameter in the current
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
        return self.import_d5_setting_att.GetTypeBaseFrmInfo(io_admin_level, io_locked)

    def get_type_coorsys_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTypeCoorsysInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TypeCoorsys
                |     parameter.
                |     Role:Retrieves the state of the TypeCoorsys parameter in the current
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
        return self.import_d5_setting_att.GetTypeCoorsysInfo(io_admin_level, io_locked)

    def get_type_tool_frm_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTypeToolFrmInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TypeToolFrm
                |     parameter.
                |     Role:Retrieves the state of the TypeToolFrm parameter in the current
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
        return self.import_d5_setting_att.GetTypeToolFrmInfo(io_admin_level, io_locked)

    def get_type_wcl_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTypeWclPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TypeWclPath
                |     parameter.
                |     Role:Retrieves the state of the TypeWclPath parameter in the current
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
        return self.import_d5_setting_att.GetTypeWclPathInfo(io_admin_level, io_locked)

    def get_vis_base_frm_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetVisBaseFrmInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the VisBaseFrm
                |     parameter.
                |     Role:Retrieves the state of the VisBaseFrm parameter in the current
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
        return self.import_d5_setting_att.GetVisBaseFrmInfo(io_admin_level, io_locked)

    def get_vis_coorsys_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetVisCoorsysInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the VisCoorsys
                |     parameter.
                |     Role:Retrieves the state of the VisCoorsys parameter in the current
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
        return self.import_d5_setting_att.GetVisCoorsysInfo(io_admin_level, io_locked)

    def get_vis_tool_frm_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetVisToolFrmInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the VisToolFrm
                |     parameter.
                |     Role:Retrieves the state of the VisToolFrm parameter in the current
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
        return self.import_d5_setting_att.GetVisToolFrmInfo(io_admin_level, io_locked)

    def get_vis_wcl_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetVisWclPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the VisWclPath
                |     parameter.
                |     Role:Retrieves the state of the VisWclPath parameter in the current
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
        return self.import_d5_setting_att.GetVisWclPathInfo(io_admin_level, io_locked)

    def set_import_annotation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportAnnotationLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportAnnotation parameter.
                |     Role:Locks or unlocks the ImportAnnotation parameter if it is possible in
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
        return self.import_d5_setting_att.SetImportAnnotationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_annotation_lock'
        # # vba_code = """
        # # Public Function set_import_annotation_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportAnnotationLock iLocked
        # #     set_import_annotation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_base_frm_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportBaseFrmLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportBaseFrm parameter.
                |     Role:Locks or unlocks the ImportBaseFrm parameter if it is possible in the
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
        return self.import_d5_setting_att.SetImportBaseFrmLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_base_frm_lock'
        # # vba_code = """
        # # Public Function set_import_base_frm_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportBaseFrmLock iLocked
        # #     set_import_base_frm_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_collision_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportCollisionLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportCollision parameter.
                |     Role:Locks or unlocks the ImportCollision parameter if it is possible in
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
        return self.import_d5_setting_att.SetImportCollisionLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_collision_lock'
        # # vba_code = """
        # # Public Function set_import_collision_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportCollisionLock iLocked
        # #     set_import_collision_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_config_file_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportConfigFileLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportConfigFile parameter.
                |     Role:Locks or unlocks the ImportConfigFile parameter if it is possible in
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
        return self.import_d5_setting_att.SetImportConfigFileLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_config_file_lock'
        # # vba_code = """
        # # Public Function set_import_config_file_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportConfigFileLock iLocked
        # #     set_import_config_file_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_coorsys_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportCoorsysLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportCoorsys parameter.
                |     Role:Locks or unlocks the ImportCoorsys parameter if it is possible in the
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
        return self.import_d5_setting_att.SetImportCoorsysLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_coorsys_lock'
        # # vba_code = """
        # # Public Function set_import_coorsys_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportCoorsysLock iLocked
        # #     set_import_coorsys_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_edge_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportEdgeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportEdge parameter.
                |     Role:Locks or unlocks the ImportEdge parameter if it is possible in the
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
        return self.import_d5_setting_att.SetImportEdgeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_edge_lock'
        # # vba_code = """
        # # Public Function set_import_edge_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportEdgeLock iLocked
        # #     set_import_edge_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_floor_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportFloorLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportFloor parameter.
                |     Role:Locks or unlocks the ImportFloor parameter if it is possible in the
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
        return self.import_d5_setting_att.SetImportFloorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_floor_lock'
        # # vba_code = """
        # # Public Function set_import_floor_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportFloorLock iLocked
        # #     set_import_floor_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_library_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportLibraryLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportLibrary parameter.
                |     Role:Locks or unlocks the ImportLibrary parameter if it is possible in the
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
        return self.import_d5_setting_att.SetImportLibraryLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_library_lock'
        # # vba_code = """
        # # Public Function set_import_library_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportLibraryLock iLocked
        # #     set_import_library_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_pdb_cache_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportPDBCacheLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportPDBCache parameter.
                |     Role:Locks or unlocks the ImportPDBCache parameter if it is possible in the
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
        return self.import_d5_setting_att.SetImportPDBCacheLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_pdb_cache_lock'
        # # vba_code = """
        # # Public Function set_import_pdb_cache_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportPDBCacheLock iLocked
        # #     set_import_pdb_cache_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_recording_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportRecordingLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportRecording parameter.
                |     Role:Locks or unlocks the ImportRecording parameter if it is possible in
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
        return self.import_d5_setting_att.SetImportRecordingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_recording_lock'
        # # vba_code = """
        # # Public Function set_import_recording_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportRecordingLock iLocked
        # #     set_import_recording_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_tool_frm_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportToolFrmLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportToolFrm parameter.
                |     Role:Locks or unlocks the ImportToolFrm parameter if it is possible in the
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
        return self.import_d5_setting_att.SetImportToolFrmLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_tool_frm_lock'
        # # vba_code = """
        # # Public Function set_import_tool_frm_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportToolFrmLock iLocked
        # #     set_import_tool_frm_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_user_attr_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportUserAttrLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportUserAttr parameter.
                |     Role:Locks or unlocks the ImportUserAttr parameter if it is possible in the
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
        return self.import_d5_setting_att.SetImportUserAttrLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_user_attr_lock'
        # # vba_code = """
        # # Public Function set_import_user_attr_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportUserAttrLock iLocked
        # #     set_import_user_attr_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_user_views_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportUserViewsLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportUserViews parameter.
                |     Role:Locks or unlocks the ImportUserViews parameter if it is possible in
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
        return self.import_d5_setting_att.SetImportUserViewsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_user_views_lock'
        # # vba_code = """
        # # Public Function set_import_user_views_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportUserViewsLock iLocked
        # #     set_import_user_views_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_wcl_message_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportWclMessageLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportWclMessage parameter.
                |     Role:Locks or unlocks the ImportWclMessage parameter if it is possible in
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
        return self.import_d5_setting_att.SetImportWclMessageLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_wcl_message_lock'
        # # vba_code = """
        # # Public Function set_import_wcl_message_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportWclMessageLock iLocked
        # #     set_import_wcl_message_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_wcl_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportWclPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportWclPath parameter.
                |     Role:Locks or unlocks the ImportWclPath parameter if it is possible in the
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
        return self.import_d5_setting_att.SetImportWclPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_wcl_path_lock'
        # # vba_code = """
        # # Public Function set_import_wcl_path_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetImportWclPathLock iLocked
        # #     set_import_wcl_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_type_base_frm_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTypeBaseFrmLock(boolean iLocked)
                | 
                |     Locks or unlocks the TypeBaseFrm parameter.
                |     Role:Locks or unlocks the TypeBaseFrm parameter if it is possible in the
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
        return self.import_d5_setting_att.SetTypeBaseFrmLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_type_base_frm_lock'
        # # vba_code = """
        # # Public Function set_type_base_frm_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetTypeBaseFrmLock iLocked
        # #     set_type_base_frm_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_type_coorsys_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTypeCoorsysLock(boolean iLocked)
                | 
                |     Locks or unlocks the TypeCoorsys parameter.
                |     Role:Locks or unlocks the TypeCoorsys parameter if it is possible in the
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
        return self.import_d5_setting_att.SetTypeCoorsysLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_type_coorsys_lock'
        # # vba_code = """
        # # Public Function set_type_coorsys_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetTypeCoorsysLock iLocked
        # #     set_type_coorsys_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_type_tool_frm_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTypeToolFrmLock(boolean iLocked)
                | 
                |     Locks or unlocks the TypeToolFrm parameter.
                |     Role:Locks or unlocks the TypeToolFrm parameter if it is possible in the
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
        return self.import_d5_setting_att.SetTypeToolFrmLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_type_tool_frm_lock'
        # # vba_code = """
        # # Public Function set_type_tool_frm_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetTypeToolFrmLock iLocked
        # #     set_type_tool_frm_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_type_wcl_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTypeWclPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the TypeWclPath parameter.
                |     Role:Locks or unlocks the TypeWclPath parameter if it is possible in the
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
        return self.import_d5_setting_att.SetTypeWclPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_type_wcl_path_lock'
        # # vba_code = """
        # # Public Function set_type_wcl_path_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetTypeWclPathLock iLocked
        # #     set_type_wcl_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_vis_base_frm_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetVisBaseFrmLock(boolean iLocked)
                | 
                |     Locks or unlocks the VisBaseFrm parameter.
                |     Role:Locks or unlocks the VisBaseFrm parameter if it is possible in the
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
        return self.import_d5_setting_att.SetVisBaseFrmLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_vis_base_frm_lock'
        # # vba_code = """
        # # Public Function set_vis_base_frm_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetVisBaseFrmLock iLocked
        # #     set_vis_base_frm_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_vis_coorsys_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetVisCoorsysLock(boolean iLocked)
                | 
                |     Locks or unlocks the VisCoorsys parameter.
                |     Role:Locks or unlocks the VisCoorsys parameter if it is possible in the
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
        return self.import_d5_setting_att.SetVisCoorsysLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_vis_coorsys_lock'
        # # vba_code = """
        # # Public Function set_vis_coorsys_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetVisCoorsysLock iLocked
        # #     set_vis_coorsys_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_vis_tool_frm_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetVisToolFrmLock(boolean iLocked)
                | 
                |     Locks or unlocks the VisToolFrm parameter.
                |     Role:Locks or unlocks the VisToolFrm parameter if it is possible in the
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
        return self.import_d5_setting_att.SetVisToolFrmLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_vis_tool_frm_lock'
        # # vba_code = """
        # # Public Function set_vis_tool_frm_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetVisToolFrmLock iLocked
        # #     set_vis_tool_frm_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_vis_wcl_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetVisWclPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the VisWclPath parameter.
                |     Role:Locks or unlocks the VisWclPath parameter if it is possible in the
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
        return self.import_d5_setting_att.SetVisWclPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_vis_wcl_path_lock'
        # # vba_code = """
        # # Public Function set_vis_wcl_path_lock(import_d5_setting_att)
        # #     Dim iLocked (2)
        # #     import_d5_setting_att.SetVisWclPathLock iLocked
        # #     set_vis_wcl_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ImportD5SettingAtt(name="{self.name}")'
