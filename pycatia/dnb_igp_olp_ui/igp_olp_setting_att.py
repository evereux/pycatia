#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class IgpOlpSettingAtt(SettingController):
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
                |                         IgpOlpSettingAtt
                | 
                | Represents the Offline Programming setting controller object.
                | Role: The Offline Programming setting controller object deals with the setting
                | attributes displayed in the IGRIP/Offline Programming property page. To access
                | this property page:
                | 
                |     Click the Options command in the Tools menu
                |     Click IGRIP
                |     Right scroll to display the property pages titles until you get Offline
                |     Programming
                |     Click Offline Programming
                | 
                | The Offline Programming setting controller object can be retrieved as an item
                | of the setting controller collection using its name "DNBIgpOlpAutoSettingCtrl"
                | as follows:
                | 
                |  Dim settingControllers1 As SettingControllers
                |  Set settingControllers1 = CATIA.SettingControllers
                |  Dim DNBIAIgpOlpSettingAtt1 As SettingController
                |  Set DNBIAIgpOlpSettingAtt1 = settingControllers1.Item("DNBIgpOlpAutoSettingCtrl")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.igp_olp_setting_att = com_object

    @property
    def downloader(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Downloader() As CATBSTR
                | 
                |     Returns or sets value of OLP Translator parameter.
                |     Role: The OLP Translator setting parameter stores the name of currently
                |     selected downloader, also known as the XSLT translator.

        :rtype: str
        """

        return self.igp_olp_setting_att.Downloader

    @downloader.setter
    def downloader(self, value: str):
        """
        :param str value:
        """

        self.igp_olp_setting_att.Downloader = value

    @property
    def downloader_dir(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DownloaderDir() As CATBSTR
                | 
                |     Returns or sets value of OLP Translator Directory
                |     parameter.
                |     Role: The OLP Translator Directory setting parameter stores the full file
                |     path to directory where OLP downloaders, also known as XSLT translators, are
                |     stored.

        :rtype: str
        """

        return self.igp_olp_setting_att.DownloaderDir

    @downloader_dir.setter
    def downloader_dir(self, value: str):
        """
        :param str value:
        """

        self.igp_olp_setting_att.DownloaderDir = value

    @property
    def existing_task_treatment(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExistingTaskTreatment() As long
                | 
                |     Returns or sets value of OLP Existing Task Treatment On Upload
                |     parameter.
                |     Role: The OLP Existing Task Treatment On Upload setting parameter
                |     determines how will the existing robot tasks with identical names as the tasks
                |     to be uploaded be treated during upload.
                |     Legal values:
                |     2 Delete existing robot tasks and all the referenced tags
                |     1 Delete existing robot tasks only
                |     0 Do not delete existing robot tasks

        :rtype: int
        """

        return self.igp_olp_setting_att.ExistingTaskTreatment

    @existing_task_treatment.setter
    def existing_task_treatment(self, value: int):
        """
        :param int value:
        """

        self.igp_olp_setting_att.ExistingTaskTreatment = value

    @property
    def java_class_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property JavaClassPath() As CATBSTR
                | 
                |     Returns or sets value of OLP Java Class Path parameter.
                |     Role: The OLP Java Class Path setting parameter stores the full file path
                |     to Java JAR files required to proper functioning of OLP download.

        :rtype: str
        """

        return self.igp_olp_setting_att.JavaClassPath

    @java_class_path.setter
    def java_class_path(self, value: str):
        """
        :param str value:
        """

        self.igp_olp_setting_att.JavaClassPath = value

    @property
    def java_exe(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property JavaExe() As CATBSTR
                | 
                |     Returns or sets value of OLP Java Executable parameter.
                |     Role: The OLP Java Executable setting parameter stores the full file path
                |     to java.exe file of Java JRE 1_4_1, or later.

        :rtype: str
        """

        return self.igp_olp_setting_att.JavaExe

    @java_exe.setter
    def java_exe(self, value: str):
        """
        :param str value:
        """

        self.igp_olp_setting_att.JavaExe = value

    @property
    def nrl_dir(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NRLDir() As CATBSTR
                | 
                |     Returns or sets value of NRL configuration file directory
                |     parameter.
                |     Role: The NRL configuration file directory parameter stores the full file
                |     path to directory where NRL configuration files are stored.

        :rtype: str
        """

        return self.igp_olp_setting_att.NRLDir

    @nrl_dir.setter
    def nrl_dir(self, value: str):
        """
        :param str value:
        """

        self.igp_olp_setting_att.NRLDir = value

    @property
    def nrl_teach_dialog_display_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NRLTeachDialogDisplayMode() As long
                | 
                |     Returns or sets value of OLPNRLTeachDialogDisplay
                |     parameter.
                |     Role: The OLPNRLTeachDialogDisplay setting parameter determines whether NRL
                |     Teach dialog will be displayed while creating and/or V5 editing of RobotMotion
                |     activities.
                |     Legal values:
                |     1 NRL Teach dialog will be hidden
                |     0 NRL Teach dialog will remain displayed

        :rtype: int
        """

        return self.igp_olp_setting_att.NRLTeachDialogDisplayMode

    @nrl_teach_dialog_display_mode.setter
    def nrl_teach_dialog_display_mode(self, value: int):
        """
        :param int value:
        """

        self.igp_olp_setting_att.NRLTeachDialogDisplayMode = value

    @property
    def robot_program_dir(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RobotProgramDir() As CATBSTR
                | 
                |     Returns or sets value of OLP Directory parameter.
                |     Role: The OLP Directory setting parameter stores the full file path to
                |     directory where native robot language programs on upload should be stored.

        :rtype: str
        """

        return self.igp_olp_setting_att.RobotProgramDir

    @robot_program_dir.setter
    def robot_program_dir(self, value: str):
        """
        :param str value:
        """

        self.igp_olp_setting_att.RobotProgramDir = value

    @property
    def uploader(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Uploader() As CATBSTR
                | 
                |     Returns or sets value of OLP Parser parameter.
                |     Role: The OLP Parser setting parameter stores the name of currently
                |     selected uploader, also known as the Java Parser.

        :rtype: str
        """

        return self.igp_olp_setting_att.Uploader

    @uploader.setter
    def uploader(self, value: str):
        """
        :param str value:
        """

        self.igp_olp_setting_att.Uploader = value

    @property
    def uploader_dir(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UploaderDir() As CATBSTR
                | 
                |     Returns or sets value of OLP Parser Directory parameter.
                |     Role: The OLP Parser Directory setting parameter stores the full file path
                |     to directory where OLP uploaders, also known as Java Parsers, are stored.

        :rtype: str
        """

        return self.igp_olp_setting_att.UploaderDir

    @uploader_dir.setter
    def uploader_dir(self, value: str):
        """
        :param str value:
        """

        self.igp_olp_setting_att.UploaderDir = value

    @property
    def xml_dir(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property XMLDir() As CATBSTR
                | 
                |     Returns or sets value of OLP XML Directory parameter.
                |     Role: The OLP XML Directory setting parameter stores the full file path to
                |     directory where XML file created during download, named simResult.xml, is
                |     stored.

        :rtype: str
        """

        return self.igp_olp_setting_att.XMLDir

    @xml_dir.setter
    def xml_dir(self, value: str):
        """
        :param str value:
        """

        self.igp_olp_setting_att.XMLDir = value

    @property
    def xml_schema(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property XMLSchema() As CATBSTR
                | 
                |     Returns or sets value of OLP XML Schema parameter.
                |     Role: The OLP XML Schema setting parameter stores the full file path to an
                |     W3C XML Schema file, used for XML file validation on upload, is stored.

        :rtype: str
        """

        return self.igp_olp_setting_att.XMLSchema

    @xml_schema.setter
    def xml_schema(self, value: str):
        """
        :param str value:
        """

        self.igp_olp_setting_att.XMLSchema = value

    def get_downloader_dir_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDownloaderDirInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OLP Translator Directory setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.igp_olp_setting_att.GetDownloaderDirInfo(io_admin_level, io_locked)

    def get_downloader_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDownloaderInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OLP Translator setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.igp_olp_setting_att.GetDownloaderInfo(io_admin_level, io_locked)

    def get_existing_task_treatment_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetExistingTaskTreatmentInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OLP Existing Task Treatment On Upload
                |     setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.igp_olp_setting_att.GetExistingTaskTreatmentInfo(io_admin_level, io_locked)

    def get_java_class_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetJavaClassPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OLP Java Class Path setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.igp_olp_setting_att.GetJavaClassPathInfo(io_admin_level, io_locked)

    def get_java_exe_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetJavaExeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OLP Java Executable setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.igp_olp_setting_att.GetJavaExeInfo(io_admin_level, io_locked)

    def get_nrl_dir_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetNRLDirInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the NRL configuration file directory setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.igp_olp_setting_att.GetNRLDirInfo(io_admin_level, io_locked)

    def get_nrl_teach_dialog_display_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetNRLTeachDialogDisplayModeInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OLPNRLTeachDialogDisplay setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.igp_olp_setting_att.GetNRLTeachDialogDisplayModeInfo(io_admin_level, io_locked)

    def get_robot_program_dir_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRobotProgramDirInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OLP Directory setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.igp_olp_setting_att.GetRobotProgramDirInfo(io_admin_level, io_locked)

    def get_uploader_dir_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUploaderDirInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OLP Parser Directory setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.igp_olp_setting_att.GetUploaderDirInfo(io_admin_level, io_locked)

    def get_uploader_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUploaderInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OLP Parser setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.igp_olp_setting_att.GetUploaderInfo(io_admin_level, io_locked)

    def get_xml_dir_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetXMLDirInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OLP XML Directory setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.igp_olp_setting_att.GetXMLDirInfo(io_admin_level, io_locked)

    def get_xml_schema_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetXMLSchemaInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OLP XML Schema setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.igp_olp_setting_att.GetXMLSchemaInfo(io_admin_level, io_locked)

    def set_downloader_dir_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDownloaderDirLock(boolean iLocked)
                | 
                |     Locks or unlocks the OLP Translator Directory setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.igp_olp_setting_att.SetDownloaderDirLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_downloader_dir_lock'
        # # vba_code = """
        # # Public Function set_downloader_dir_lock(igp_olp_setting_att)
        # #     Dim iLocked (2)
        # #     igp_olp_setting_att.SetDownloaderDirLock iLocked
        # #     set_downloader_dir_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_downloader_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDownloaderLock(boolean iLocked)
                | 
                |     Locks or unlocks the OLP Translator setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.igp_olp_setting_att.SetDownloaderLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_downloader_lock'
        # # vba_code = """
        # # Public Function set_downloader_lock(igp_olp_setting_att)
        # #     Dim iLocked (2)
        # #     igp_olp_setting_att.SetDownloaderLock iLocked
        # #     set_downloader_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_existing_task_treatment_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExistingTaskTreatmentLock(boolean iLocked)
                | 
                |     Locks or unlocks the OLP Existing Task Treatment On Upload
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.igp_olp_setting_att.SetExistingTaskTreatmentLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_existing_task_treatment_lock'
        # # vba_code = """
        # # Public Function set_existing_task_treatment_lock(igp_olp_setting_att)
        # #     Dim iLocked (2)
        # #     igp_olp_setting_att.SetExistingTaskTreatmentLock iLocked
        # #     set_existing_task_treatment_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_java_class_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetJavaClassPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the OLP Java Class Path parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.igp_olp_setting_att.SetJavaClassPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_java_class_path_lock'
        # # vba_code = """
        # # Public Function set_java_class_path_lock(igp_olp_setting_att)
        # #     Dim iLocked (2)
        # #     igp_olp_setting_att.SetJavaClassPathLock iLocked
        # #     set_java_class_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_java_exe_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetJavaExeLock(boolean iLocked)
                | 
                |     Locks or unlocks the OLP Java Executable parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.igp_olp_setting_att.SetJavaExeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_java_exe_lock'
        # # vba_code = """
        # # Public Function set_java_exe_lock(igp_olp_setting_att)
        # #     Dim iLocked (2)
        # #     igp_olp_setting_att.SetJavaExeLock iLocked
        # #     set_java_exe_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_nrl_dir_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetNRLDirLock(boolean iLocked)
                | 
                |     Locks or unlocks the NRL configuration file directory setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.igp_olp_setting_att.SetNRLDirLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_nrl_dir_lock'
        # # vba_code = """
        # # Public Function set_nrl_dir_lock(igp_olp_setting_att)
        # #     Dim iLocked (2)
        # #     igp_olp_setting_att.SetNRLDirLock iLocked
        # #     set_nrl_dir_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_nrl_teach_dialog_display_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetNRLTeachDialogDisplayModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the OLPNRLTeachDialogDisplay parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.igp_olp_setting_att.SetNRLTeachDialogDisplayModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_nrl_teach_dialog_display_mode_lock'
        # # vba_code = """
        # # Public Function set_nrl_teach_dialog_display_mode_lock(igp_olp_setting_att)
        # #     Dim iLocked (2)
        # #     igp_olp_setting_att.SetNRLTeachDialogDisplayModeLock iLocked
        # #     set_nrl_teach_dialog_display_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_robot_program_dir_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRobotProgramDirLock(boolean iLocked)
                | 
                |     Locks or unlocks the OLP Directory setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.igp_olp_setting_att.SetRobotProgramDirLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_robot_program_dir_lock'
        # # vba_code = """
        # # Public Function set_robot_program_dir_lock(igp_olp_setting_att)
        # #     Dim iLocked (2)
        # #     igp_olp_setting_att.SetRobotProgramDirLock iLocked
        # #     set_robot_program_dir_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_uploader_dir_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUploaderDirLock(boolean iLocked)
                | 
                |     Locks or unlocks the OLP Parser Directory setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.igp_olp_setting_att.SetUploaderDirLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_uploader_dir_lock'
        # # vba_code = """
        # # Public Function set_uploader_dir_lock(igp_olp_setting_att)
        # #     Dim iLocked (2)
        # #     igp_olp_setting_att.SetUploaderDirLock iLocked
        # #     set_uploader_dir_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_uploader_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUploaderLock(boolean iLocked)
                | 
                |     Locks or unlocks the OLP Parser setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.igp_olp_setting_att.SetUploaderLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_uploader_lock'
        # # vba_code = """
        # # Public Function set_uploader_lock(igp_olp_setting_att)
        # #     Dim iLocked (2)
        # #     igp_olp_setting_att.SetUploaderLock iLocked
        # #     set_uploader_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_xml_dir_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetXMLDirLock(boolean iLocked)
                | 
                |     Locks or unlocks the OLP XML Directory setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.igp_olp_setting_att.SetXMLDirLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_xml_dir_lock'
        # # vba_code = """
        # # Public Function set_xml_dir_lock(igp_olp_setting_att)
        # #     Dim iLocked (2)
        # #     igp_olp_setting_att.SetXMLDirLock iLocked
        # #     set_xml_dir_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_xml_schema_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetXMLSchemaLock(boolean iLocked)
                | 
                |     Locks or unlocks the OLP XML Schema setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.igp_olp_setting_att.SetXMLSchemaLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_xml_schema_lock'
        # # vba_code = """
        # # Public Function set_xml_schema_lock(igp_olp_setting_att)
        # #     Dim iLocked (2)
        # #     igp_olp_setting_att.SetXMLSchemaLock iLocked
        # #     set_xml_schema_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'IgpOlpSettingAtt(name="{self.name}")'
