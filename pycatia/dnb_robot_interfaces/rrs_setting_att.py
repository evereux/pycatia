#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class RRSSettingAtt(SettingController):
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
                |                         RRSSettingAtt
                | 
                | Interface to handle parameters of IGRIP RRS Tools Options Tab page Role: This
                | interface is implemented by a component which represents the controller of
                | IGRIP RRS Tools Options parameter settings.
                | 
                |     Methods to set value of each parameter
                |     Methods to get value of each parameter
                |     Methods to get information on each parameter
                |     Methods to lock/unlock value of each parameter
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rrs_setting_att = com_object

    def add_new_rrs2_controller_identifier(self, i_controller_identifier: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddNewRRS2ControllerIdentifier(CATBSTR
                | iControllerIdentifier)
                | 
                |     Adds new controller identifier into the list represented by the
                |     "RRS2ControllerIdentifiers" parameter. If it is already in the list, does
                |     nothing.
                |     Role: Adds new controller identifier to "RRS2ControllerIdentifiers"
                |     list.
                | 
                |     Parameters:
                | 
                |         iControllerIdentifier
                |             Controller Identifier to be added to the list. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param str i_controller_identifier:
        :rtype: None
        """
        return self.rrs_setting_att.AddNewRRS2ControllerIdentifier(i_controller_identifier)

    def get_rcs_data_lib_dir_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRCSDataLibDirInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RCSDATA$LIB"
                |     parameter.
                |     Role:Retrieves the state of the "RCSDATA$LIB" parameter in the current
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
        return self.rrs_setting_att.GetRCSDataLibDirInfo(io_admin_level, io_locked)

    def get_rrs2_connect_downloaders_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2ConnectDownloadersInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2ConnectDownloaders"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2ConnectDownloaders" parameter in the
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
        return self.rrs_setting_att.GetRRS2ConnectDownloadersInfo(io_admin_level, io_locked)

    def get_rrs2_consistency_cmd_downloaders_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2ConsistencyCmdDownloadersInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2ConsistencyCmdDownloaders"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2ConsistencyCmdDownloaders" parameter
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
        return self.rrs_setting_att.GetRRS2ConsistencyCmdDownloadersInfo(io_admin_level, io_locked)

    def get_rrs2_controller_identifier_attributes(
            self,
            i_controller_identifier: str,
            o_rrs2_connect_downloader: str,
            o_rrs2_sim_run_downloader: str,
            o_rrs2_consistency_cmd_downloader: str,
            o_rrs2_download_during_connect: bool,
            o_rrs2_download_during_sim_run: bool,
            o_rrs2_update_program_on_download: bool,
            o_rrs2_download_in_part_coordinates: bool
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetRRS2ControllerIdentifierAttributes(CATBSTR
                | iControllerIdentifier,
                | CATBSTR oRRS2ConnectDownloader,
                | CATBSTR oRRS2SimRunDownloader,
                | CATBSTR oRRS2ConsistencyCmdDownloader,
                | boolean oRRS2DownloadDuringConnect,
                | boolean oRRS2DownloadDuringSimRun,
                | boolean oRRS2UpdateProgramOnDownload,
                | boolean oRRS2DownloadInPartCoordinates)
                | 
                |     Gets various controller identifier-specific attributes associated with a
                |     given controller identifier.
                |     Role: Gets various attributes associated with a given controller
                |     identifier.
                | 
                |     Parameters:
                | 
                |         iControllerIdentifier
                |             Controller Identifier whose attributes are requested.
                |             
                |         iControllerIdentifier
                |             Controller Identifier whose attributes are requested.
                |
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param str i_controller_identifier:
        :param str o_rrs2_connect_downloader:
        :param str o_rrs2_sim_run_downloader:
        :param str o_rrs2_consistency_cmd_downloader:
        :param bool o_rrs2_download_during_connect:
        :param bool o_rrs2_download_during_sim_run:
        :param bool o_rrs2_update_program_on_download:
        :param bool o_rrs2_download_in_part_coordinates:
        :rtype: None
        """
        return self.rrs_setting_att.GetRRS2ControllerIdentifierAttributes(
            i_controller_identifier,
            o_rrs2_connect_downloader,
            o_rrs2_sim_run_downloader,
            o_rrs2_consistency_cmd_downloader,
            o_rrs2_download_during_connect,
            o_rrs2_download_during_sim_run,
            o_rrs2_update_program_on_download,
            o_rrs2_download_in_part_coordinates
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_rrs2_controller_identifier_attributes'
        # # vba_code = """
        # # Public Function get_rrs2_controller_identifier_attributes(rrs_setting_att)
        # #     Dim iControllerIdentifier (2)
        # #     rrs_setting_att.GetRRS2ControllerIdentifierAttributes iControllerIdentifier
        # #     get_rrs2_controller_identifier_attributes = iControllerIdentifier
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_rrs2_controller_identifiers_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2ControllerIdentifiersInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2ControllerIdentifiers"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2ControllerIdentifiers" parameter in
                |     the current environment.
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
        return self.rrs_setting_att.GetRRS2ControllerIdentifiersInfo(io_admin_level, io_locked)

    def get_rrs2_delete_auto_download_files_after_xfer_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2DeleteAutoDownloadFilesAfterXferInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     "RRS2DeleteAutoDownloadFilesAfterXfer" parameter.
                |     Role:Retrieves the state of the "RRS2DeleteAutoDownloadFilesAfterXfer"
                |     parameter in the current environment.
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
        return self.rrs_setting_att.GetRRS2DeleteAutoDownloadFilesAfterXferInfo(io_admin_level, io_locked)

    def get_rrs2_dflt_controller_identifier_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2DfltControllerIdentifierInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2DfltControllerIdentifier"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2DfltControllerIdentifier" parameter in
                |     the current environment.
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
        return self.rrs_setting_att.GetRRS2DfltControllerIdentifierInfo(io_admin_level, io_locked)

    def get_rrs2_download_during_connect_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2DownloadDuringConnectInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2DownloadDuringConnect"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2DownloadDuringConnect" parameter in
                |     the current environment.
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
        return self.rrs_setting_att.GetRRS2DownloadDuringConnectInfo(io_admin_level, io_locked)

    def get_rrs2_download_during_sim_run_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2DownloadDuringSimRunInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2DownloadDuringSimRun"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2DownloadDuringSimRun" parameter in the
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
        return self.rrs_setting_att.GetRRS2DownloadDuringSimRunInfo(io_admin_level, io_locked)

    def get_rrs2_download_in_part_coordinates_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2DownloadInPartCoordinatesInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2DownloadInPartCoordinates"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2DownloadInPartCoordinates" parameter
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
        return self.rrs_setting_att.GetRRS2DownloadInPartCoordinatesInfo(io_admin_level, io_locked)

    def get_rrs2_download_log_file_name_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2DownloadLogFileNameInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2DownloadLogFileName"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2DownloadLogFileName" parameter in the
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
        return self.rrs_setting_att.GetRRS2DownloadLogFileNameInfo(io_admin_level, io_locked)

    def get_rrs2_free_play_sim_step_size_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2FreePlaySimStepSizeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2FreePlaySimStepSize"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2FreePlaySimStepSize" parameter in the
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
        return self.rrs_setting_att.GetRRS2FreePlaySimStepSizeInfo(io_admin_level, io_locked)

    def get_rrs2_main_task_processing_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2MainTaskProcessingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2MainTaskProcessing"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2MainTaskProcessing" parameter in the
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
        return self.rrs_setting_att.GetRRS2MainTaskProcessingInfo(io_admin_level, io_locked)

    def get_rrs2_motion_planner_active_during_teach_olp_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2MotionPlannerActiveDuringTeachOLPInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     "RRS2MotionPlannerActiveDuringTeachOLP" parameter.
                |     Role:Retrieves the state of the "RRS2MotionPlannerActiveDuringTeachOLP"
                |     parameter in the current environment.
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
        return self.rrs_setting_att.GetRRS2MotionPlannerActiveDuringTeachOLPInfo(io_admin_level, io_locked)

    def get_rrs2_sim_run_downloaders_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2SimRunDownloadersInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2SimRunDownloaders"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2SimRunDownloaders" parameter in the
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
        return self.rrs_setting_att.GetRRS2SimRunDownloadersInfo(io_admin_level, io_locked)

    def get_rrs2_stop_vrc_when_sim_stops_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2StopVRCWhenSimStopsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2StopVRCWhenSimStops"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2StopVRCWhenSimStops" parameter in the
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
        return self.rrs_setting_att.GetRRS2StopVRCWhenSimStopsInfo(io_admin_level, io_locked)

    def get_rrs2_update_program_on_download_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2UpdateProgramOnDownloadInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2UpdateProgramOnDownload"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2UpdateProgramOnDownload" parameter in
                |     the current environment.
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
        return self.rrs_setting_att.GetRRS2UpdateProgramOnDownloadInfo(io_admin_level, io_locked)

    def get_rrs2_use_vrc_inverse_kinematics_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2UseVRCInverseKinematicsInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2UseVRCInverseKinematics"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2UseVRCInverseKinematics" parameter in
                |     the current environment.
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
        return self.rrs_setting_att.GetRRS2UseVRCInverseKinematicsInfo(io_admin_level, io_locked)

    def get_rrs2_use_vrc_turn_limits_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRS2UseVRCTurnLimitsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS2UseVRCTurnLimits"
                |     parameter.
                |     Role:Retrieves the state of the "RRS2UseVRCTurnLimits" parameter in the
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
        return self.rrs_setting_att.GetRRS2UseVRCTurnLimitsInfo(io_admin_level, io_locked)

    def get_rrs_lib_dir_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRSLibDirInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS$LIB"
                |     parameter.
                |     Role:Retrieves the state of the "RRS$LIB" parameter in the current
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
        return self.rrs_setting_att.GetRRSLibDirInfo(io_admin_level, io_locked)

    def get_rrs_server_file_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRRSServerFileInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RRS Servers File"
                |     parameter.
                |     Role:Retrieves the state of the "RRS Servers File" parameter in the current
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
        return self.rrs_setting_att.GetRRSServerFileInfo(io_admin_level, io_locked)

    def set_rcs_data_lib_dir_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRCSDataLibDirLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RCSDATA$LIB" parameter.
                |     Role: Locks or unlocks the "RCSDATA$LIB" parameter if the operation is
                |     allowed in the current administrated environment. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRCSDataLibDirLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rcs_data_lib_dir_lock'
        # # vba_code = """
        # # Public Function set_rcs_data_lib_dir_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRCSDataLibDirLock iLocked
        # #     set_rcs_data_lib_dir_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_connect_downloaders_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2ConnectDownloadersLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2ConnectDownloaders" parameter.
                |     Role: Locks or unlocks the "RRS2ConnectDownloaders" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2ConnectDownloadersLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_connect_downloaders_lock'
        # # vba_code = """
        # # Public Function set_rrs2_connect_downloaders_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2ConnectDownloadersLock iLocked
        # #     set_rrs2_connect_downloaders_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_consistency_cmd_downloaders_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2ConsistencyCmdDownloadersLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2ConsistencyCmdDownloaders"
                |     parameter.
                |     Role: Locks or unlocks the "RRS2ConsistencyCmdDownloaders" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2ConsistencyCmdDownloadersLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_consistency_cmd_downloaders_lock'
        # # vba_code = """
        # # Public Function set_rrs2_consistency_cmd_downloaders_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2ConsistencyCmdDownloadersLock iLocked
        # #     set_rrs2_consistency_cmd_downloaders_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_controller_identifiers_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2ControllerIdentifiersLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2ControllerIdentifiers"
                |     parameter.
                |     Role: Locks or unlocks the "RRS2ControllerIdentifiers" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2ControllerIdentifiersLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_controller_identifiers_lock'
        # # vba_code = """
        # # Public Function set_rrs2_controller_identifiers_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2ControllerIdentifiersLock iLocked
        # #     set_rrs2_controller_identifiers_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_delete_auto_download_files_after_xfer_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2DeleteAutoDownloadFilesAfterXferLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the "RRS2DeleteAutoDownloadFilesAfterXfer"
                |     parameter.
                |     Role: Locks or unlocks the "RRS2DeleteAutoDownloadFilesAfterXfer" parameter
                |     if the operation is allowed in the current administrated environment. In user
                |     mode this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2DeleteAutoDownloadFilesAfterXferLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_delete_auto_download_files_after_xfer_lock'
        # # vba_code = """
        # # Public Function set_rrs2_delete_auto_download_files_after_xfer_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2DeleteAutoDownloadFilesAfterXferLock iLocked
        # #     set_rrs2_delete_auto_download_files_after_xfer_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_dflt_controller_identifier_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2DfltControllerIdentifierLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2DfltControllerIdentifier"
                |     parameter.
                |     Role: Locks or unlocks the "RRS2DfltControllerIdentifier" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2DfltControllerIdentifierLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_dflt_controller_identifier_lock'
        # # vba_code = """
        # # Public Function set_rrs2_dflt_controller_identifier_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2DfltControllerIdentifierLock iLocked
        # #     set_rrs2_dflt_controller_identifier_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_download_during_connect_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2DownloadDuringConnectLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2DownloadDuringConnect"
                |     parameter.
                |     Role: Locks or unlocks the "RRS2DownloadDuringConnect" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2DownloadDuringConnectLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_download_during_connect_lock'
        # # vba_code = """
        # # Public Function set_rrs2_download_during_connect_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2DownloadDuringConnectLock iLocked
        # #     set_rrs2_download_during_connect_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_download_during_sim_run_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2DownloadDuringSimRunLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2DownloadDuringSimRun" parameter.
                |     Role: Locks or unlocks the "RRS2DownloadDuringSimRun" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2DownloadDuringSimRunLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_download_during_sim_run_lock'
        # # vba_code = """
        # # Public Function set_rrs2_download_during_sim_run_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2DownloadDuringSimRunLock iLocked
        # #     set_rrs2_download_during_sim_run_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_download_in_part_coordinates_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2DownloadInPartCoordinatesLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2DownloadInPartCoordinates"
                |     parameter.
                |     Role: Locks or unlocks the "RRS2DownloadInPartCoordinates" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2DownloadInPartCoordinatesLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_download_in_part_coordinates_lock'
        # # vba_code = """
        # # Public Function set_rrs2_download_in_part_coordinates_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2DownloadInPartCoordinatesLock iLocked
        # #     set_rrs2_download_in_part_coordinates_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_download_log_file_name_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2DownloadLogFileNameLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2DownloadLogFileName" parameter.
                |     Role: Locks or unlocks the "RRS2DownloadLogFileName" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2DownloadLogFileNameLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_download_log_file_name_lock'
        # # vba_code = """
        # # Public Function set_rrs2_download_log_file_name_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2DownloadLogFileNameLock iLocked
        # #     set_rrs2_download_log_file_name_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_free_play_sim_step_size_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2FreePlaySimStepSizeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2FreePlaySimStepSize" parameter.
                |     Role: Locks or unlocks the "RRS2FreePlaySimStepSize" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2FreePlaySimStepSizeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_free_play_sim_step_size_lock'
        # # vba_code = """
        # # Public Function set_rrs2_free_play_sim_step_size_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2FreePlaySimStepSizeLock iLocked
        # #     set_rrs2_free_play_sim_step_size_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_main_task_processing_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2MainTaskProcessingLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2MainTaskProcessing" parameter.
                |     Role: Locks or unlocks the "RRS2MainTaskProcessing" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2MainTaskProcessingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_main_task_processing_lock'
        # # vba_code = """
        # # Public Function set_rrs2_main_task_processing_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2MainTaskProcessingLock iLocked
        # #     set_rrs2_main_task_processing_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_motion_planner_active_during_teach_olp_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2MotionPlannerActiveDuringTeachOLPLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the "RRS2MotionPlannerActiveDuringTeachOLP"
                |     parameter.
                |     Role: Locks or unlocks the "RRS2MotionPlannerActiveDuringTeachOLP"
                |     parameter if the operation is allowed in the current administrated environment.
                |     In user mode this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2MotionPlannerActiveDuringTeachOLPLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_motion_planner_active_during_teach_olp_lock'
        # # vba_code = """
        # # Public Function set_rrs2_motion_planner_active_during_teach_olp_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2MotionPlannerActiveDuringTeachOLPLock iLocked
        # #     set_rrs2_motion_planner_active_during_teach_olp_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_sim_run_downloaders_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2SimRunDownloadersLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2SimRunDownloaders" parameter.
                |     Role: Locks or unlocks the "RRS2SimRunDownloaders" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2SimRunDownloadersLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_sim_run_downloaders_lock'
        # # vba_code = """
        # # Public Function set_rrs2_sim_run_downloaders_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2SimRunDownloadersLock iLocked
        # #     set_rrs2_sim_run_downloaders_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_stop_vrc_when_sim_stops_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2StopVRCWhenSimStopsLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2StopVRCWhenSimStops" parameter.
                |     Role: Locks or unlocks the "RRS2StopVRCWhenSimStops" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2StopVRCWhenSimStopsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_stop_vrc_when_sim_stops_lock'
        # # vba_code = """
        # # Public Function set_rrs2_stop_vrc_when_sim_stops_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2StopVRCWhenSimStopsLock iLocked
        # #     set_rrs2_stop_vrc_when_sim_stops_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_update_program_on_download_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2UpdateProgramOnDownloadLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2UpdateProgramOnDownload"
                |     parameter.
                |     Role: Locks or unlocks the "RRS2UpdateProgramOnDownload" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2UpdateProgramOnDownloadLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_update_program_on_download_lock'
        # # vba_code = """
        # # Public Function set_rrs2_update_program_on_download_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2UpdateProgramOnDownloadLock iLocked
        # #     set_rrs2_update_program_on_download_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_use_vrc_inverse_kinematics_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2UseVRCInverseKinematicsLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2UseVRCInverseKinematics"
                |     parameter.
                |     Role: Locks or unlocks the "RRS2UseVRCInverseKinematics" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2UseVRCInverseKinematicsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_use_vrc_inverse_kinematics_lock'
        # # vba_code = """
        # # Public Function set_rrs2_use_vrc_inverse_kinematics_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2UseVRCInverseKinematicsLock iLocked
        # #     set_rrs2_use_vrc_inverse_kinematics_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs2_use_vrc_turn_limits_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRS2UseVRCTurnLimitsLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS2UseVRCTurnLimits" parameter.
                |     Role: Locks or unlocks the "RRS2UseVRCTurnLimits" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0 : to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRS2UseVRCTurnLimitsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs2_use_vrc_turn_limits_lock'
        # # vba_code = """
        # # Public Function set_rrs2_use_vrc_turn_limits_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRS2UseVRCTurnLimitsLock iLocked
        # #     set_rrs2_use_vrc_turn_limits_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs_lib_dir_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRSLibDirLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RRS$LIB" parameter.
                |     Role:Locks or unlocks the "RRS$LIB" parameter if it is possible in the
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
        return self.rrs_setting_att.SetRRSLibDirLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs_lib_dir_lock'
        # # vba_code = """
        # # Public Function set_rrs_lib_dir_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRSLibDirLock iLocked
        # #     set_rrs_lib_dir_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rrs_server_file_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRRSServerFileLock(boolean iLocked)
                | 
                |     Sets value of "RRS Servers File" parameter.
                |     Role: Sets value of "RRS Servers File" parameter
                | 
                |     Parameters:
                | 
                |         iServerFile
                |             New value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.rrs_setting_att.SetRRSServerFileLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rrs_server_file_lock'
        # # vba_code = """
        # # Public Function set_rrs_server_file_lock(rrs_setting_att)
        # #     Dim iLocked (2)
        # #     rrs_setting_att.SetRRSServerFileLock iLocked
        # #     set_rrs_server_file_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'RRSSettingAtt(name="{self.name}")'
