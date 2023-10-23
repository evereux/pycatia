#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class ReportGenerationSheetSettingAtt(SettingController):
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
                |                         ReportGenerationSheetSettingAtt
                | 
                | The interface to access a
                | CATIAReportGenerationSheetSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.report_generation_sheet_setting_att = com_object

    @property
    def all_checks_report(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AllChecksReport() As short
                | 
                |     Returns or sets the AllChecksReport parameter.
                |     Role:Return or Set the AllChecksReport parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oAllChecksReport
                |             Legal values:
                |             0 : report of only failed checks
                |             1 : report of all checks.

        :rtype: int
        """

        return self.report_generation_sheet_setting_att.AllChecksReport

    @all_checks_report.setter
    def all_checks_report(self, value: int):
        """
        :param int value:
        """

        self.report_generation_sheet_setting_att.AllChecksReport = value

    @property
    def check_report_html(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CheckReportHtml() As short
                | 
                |     Returns or sets the CheckReportHtml parameter.
                |     Role:Return or Set the CheckReportHtml parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oCheckReportHtml
                |             Legal values:
                |             0 : to have check report in Xml
                |             1 : to have check report in Html.

        :rtype: int
        """

        return self.report_generation_sheet_setting_att.CheckReportHtml

    @check_report_html.setter
    def check_report_html(self, value: int):
        """
        :param int value:
        """

        self.report_generation_sheet_setting_att.CheckReportHtml = value

    @property
    def directory_for_input_xsl(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DirectoryForInputXsl() As CATBSTR
                | 
                |     Returns or sets the DirectoryForInputXsl parameter.
                |     Role:Return or Set the DirectoryForInputXsl parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oDirectoryForInputXsl
                |             Directory for the report file with Xml extension.

        :rtype: str
        """

        return self.report_generation_sheet_setting_att.DirectoryForInputXsl

    @directory_for_input_xsl.setter
    def directory_for_input_xsl(self, value: str):
        """
        :param str value:
        """

        self.report_generation_sheet_setting_att.DirectoryForInputXsl = value

    @property
    def report_check_advisor(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ReportCheckAdvisor() As short
                | 
                |     Returns or sets the ReportCheckAdvisor parameter.
                |     Role:Return or Set the ReportCheckAdvisor parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oReportCheckAdvisor
                |             Legal values:
                |             0 : not report of check Advisor
                |             1 : report of check Advisor.

        :rtype: int
        """

        return self.report_generation_sheet_setting_att.ReportCheckAdvisor

    @report_check_advisor.setter
    def report_check_advisor(self, value: int):
        """
        :param int value:
        """

        self.report_generation_sheet_setting_att.ReportCheckAdvisor = value

    @property
    def report_check_expert(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ReportCheckExpert() As short
                | 
                |     Returns or sets the ReportCheckExpert parameter.
                |     Role:Return or Set the ReportCheckExpert parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oReportCheckExpert
                |             Legal values:
                |             0 : not report of check Advisor
                |             1 : report of check Advisor.

        :rtype: int
        """

        return self.report_generation_sheet_setting_att.ReportCheckExpert

    @report_check_expert.setter
    def report_check_expert(self, value: int):
        """
        :param int value:
        """

        self.report_generation_sheet_setting_att.ReportCheckExpert = value

    @property
    def report_html_in_catia_session(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ReportHtmlInCatiaSession() As short
                | 
                |     Returns or sets the ReportHtmlInCatiaSession parameter.
                |     Role:Return or Set the ReportHtmlInCatiaSession parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         oReportHtmlInCatiaSession
                |             Legal values:
                |             0 : report Html outside CATIA session
                |             1 : report Html in CATIA session.

        :rtype: int
        """

        return self.report_generation_sheet_setting_att.ReportHtmlInCatiaSession

    @report_html_in_catia_session.setter
    def report_html_in_catia_session(self, value: int):
        """
        :param int value:
        """

        self.report_generation_sheet_setting_att.ReportHtmlInCatiaSession = value

    @property
    def report_objects_information(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ReportObjectsInformation() As short
                | 
                |     Returns or sets the ReportObjectsInformation parameter.
                |     Role:Return or Set the ReportObjectsInformation parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         oReportObjectsInformation
                |             Legal values:
                |             0 : not report objects information
                |             1 : report objects information.

        :rtype: int
        """

        return self.report_generation_sheet_setting_att.ReportObjectsInformation

    @report_objects_information.setter
    def report_objects_information(self, value: int):
        """
        :param int value:
        """

        self.report_generation_sheet_setting_att.ReportObjectsInformation = value

    @property
    def report_output_directory(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ReportOutputDirectory() As CATBSTR
                | 
                |     Returns or sets the ReportOutputDirectory parameter.
                |     Role:Return or Set the ReportOutputDirectory parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oReportOutputDirectory
                |             The output directory for report of checks expert and checks
                |             advisor.

        :rtype: str
        """

        return self.report_generation_sheet_setting_att.ReportOutputDirectory

    @report_output_directory.setter
    def report_output_directory(self, value: str):
        """
        :param str value:
        """

        self.report_generation_sheet_setting_att.ReportOutputDirectory = value

    @property
    def report_parameters_information(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ReportParametersInformation() As short
                | 
                |     Returns or sets the ReportParametersInformation parameter.
                |     Role:Return or Set the ReportParametersInformation parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         oReportParametersInformation
                |             Legal values:
                |             0 : not check Advisor parameter information
                |             1 : check Advisor parameter information.

        :rtype: int
        """

        return self.report_generation_sheet_setting_att.ReportParametersInformation

    @report_parameters_information.setter
    def report_parameters_information(self, value: int):
        """
        :param int value:
        """

        self.report_generation_sheet_setting_att.ReportParametersInformation = value

    @property
    def report_passed_objects(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ReportPassedObjects() As short
                | 
                |     Returns or sets the ReportPassedObjects parameter.
                |     Role:Return or Set the ReportPassedObjects parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oReportPassedObjects
                |             Legal values:
                |             0 : not report passed objects
                |             1 : report passed objects.

        :rtype: int
        """

        return self.report_generation_sheet_setting_att.ReportPassedObjects

    @report_passed_objects.setter
    def report_passed_objects(self, value: int):
        """
        :param int value:
        """

        self.report_generation_sheet_setting_att.ReportPassedObjects = value

    def get_all_checks_report_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAllChecksReportInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AllChecksReport
                |     parameter.
                |     Role:Retrieves the state of the AllChecksReport parameter in the current
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
        return self.report_generation_sheet_setting_att.GetAllChecksReportInfo(io_admin_level, io_locked)

    def get_check_report_html_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetCheckReportHtmlInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the CheckReportHtml
                |     parameter.
                |     Role:Retrieves the state of the CheckReportHtml parameter in the current
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
        return self.report_generation_sheet_setting_att.GetCheckReportHtmlInfo(io_admin_level, io_locked)

    def get_directory_for_input_xsl_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDirectoryForInputXslInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DirectoryForInputXsl
                |     parameter.
                |     Role:Retrieves the state of the DirectoryForInputXsl parameter in the
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
        return self.report_generation_sheet_setting_att.GetDirectoryForInputXslInfo(io_admin_level, io_locked)

    def get_report_check_advisor_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetReportCheckAdvisorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ReportCheckAdvisor
                |     parameter.
                |     Role:Retrieves the state of the ReportCheckAdvisor parameter in the current
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
        return self.report_generation_sheet_setting_att.GetReportCheckAdvisorInfo(io_admin_level, io_locked)

    def get_report_check_expert_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetReportCheckExpertInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ReportCheckExpert
                |     parameter.
                |     Role:Retrieves the state of the ReportCheckExpert parameter in the current
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
        return self.report_generation_sheet_setting_att.GetReportCheckExpertInfo(io_admin_level, io_locked)

    def get_report_html_in_catia_session_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetReportHtmlInCatiaSessionInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ReportHtmlInCatiaSession
                |     parameter.
                |     Role:Retrieves the state of the ReportHtmlInCatiaSession parameter in the
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
        return self.report_generation_sheet_setting_att.GetReportHtmlInCatiaSessionInfo(io_admin_level, io_locked)

    def get_report_objects_information_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetReportObjectsInformationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ReportObjectsInformation
                |     parameter.
                |     Role:Retrieves the state of the ReportObjectsInformation parameter in the
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
        return self.report_generation_sheet_setting_att.GetReportObjectsInformationInfo(io_admin_level, io_locked)

    def get_report_output_directory_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetReportOutputDirectoryInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ReportOutputDirectory
                |     parameter.
                |     Role:Retrieves the state of the ReportOutputDirectory parameter in the
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
        return self.report_generation_sheet_setting_att.GetReportOutputDirectoryInfo(io_admin_level, io_locked)

    def get_report_parameters_information_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetReportParametersInformationInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ReportParametersInformation
                |     parameter.
                |     Role:Retrieves the state of the ReportParametersInformation parameter in
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
        return self.report_generation_sheet_setting_att.GetReportParametersInformationInfo(io_admin_level, io_locked)

    def get_report_passed_objects_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetReportPassedObjectsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ReportPassedObjects
                |     parameter.
                |     Role:Retrieves the state of the ReportPassedObjects parameter in the
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
        return self.report_generation_sheet_setting_att.GetReportPassedObjectsInfo(io_admin_level, io_locked)

    def set_all_checks_report_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAllChecksReportLock(boolean iLocked)
                | 
                |     Locks or unlocks the AllChecksReport parameter.
                |     Role:Locks or unlocks the AllChecksReport parameter if it is possible in
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
        return self.report_generation_sheet_setting_att.SetAllChecksReportLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_all_checks_report_lock'
        # # vba_code = """
        # # Public Function set_all_checks_report_lock(report_generation_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     report_generation_sheet_setting_att.SetAllChecksReportLock iLocked
        # #     set_all_checks_report_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_check_report_html_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetCheckReportHtmlLock(boolean iLocked)
                | 
                |     Locks or unlocks the CheckReportHtml parameter.
                |     Role:Locks or unlocks the CheckReportHtml parameter if it is possible in
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
        return self.report_generation_sheet_setting_att.SetCheckReportHtmlLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_check_report_html_lock'
        # # vba_code = """
        # # Public Function set_check_report_html_lock(report_generation_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     report_generation_sheet_setting_att.SetCheckReportHtmlLock iLocked
        # #     set_check_report_html_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_directory_for_input_xsl_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDirectoryForInputXslLock(boolean iLocked)
                | 
                |     Locks or unlocks the DirectoryForInputXsl parameter.
                |     Role:Locks or unlocks the DirectoryForInputXsl parameter if it is possible
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
        return self.report_generation_sheet_setting_att.SetDirectoryForInputXslLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_directory_for_input_xsl_lock'
        # # vba_code = """
        # # Public Function set_directory_for_input_xsl_lock(report_generation_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     report_generation_sheet_setting_att.SetDirectoryForInputXslLock iLocked
        # #     set_directory_for_input_xsl_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_report_check_advisor_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetReportCheckAdvisorLock(boolean iLocked)
                | 
                |     Locks or unlocks the ReportCheckAdvisor parameter.
                |     Role:Locks or unlocks the ReportCheckAdvisor parameter if it is possible in
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
        return self.report_generation_sheet_setting_att.SetReportCheckAdvisorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_report_check_advisor_lock'
        # # vba_code = """
        # # Public Function set_report_check_advisor_lock(report_generation_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     report_generation_sheet_setting_att.SetReportCheckAdvisorLock iLocked
        # #     set_report_check_advisor_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_report_check_expert_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetReportCheckExpertLock(boolean iLocked)
                | 
                |     Locks or unlocks the ReportCheckExpert parameter.
                |     Role:Locks or unlocks the ReportCheckExpert parameter if it is possible in
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
        return self.report_generation_sheet_setting_att.SetReportCheckExpertLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_report_check_expert_lock'
        # # vba_code = """
        # # Public Function set_report_check_expert_lock(report_generation_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     report_generation_sheet_setting_att.SetReportCheckExpertLock iLocked
        # #     set_report_check_expert_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_report_html_in_catia_session_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetReportHtmlInCatiaSessionLock(boolean iLocked)
                | 
                |     Locks or unlocks the ReportHtmlInCatiaSession parameter.
                |     Role:Locks or unlocks the ReportHtmlInCatiaSession parameter if it is
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
        return self.report_generation_sheet_setting_att.SetReportHtmlInCatiaSessionLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_report_html_in_catia_session_lock'
        # # vba_code = """
        # # Public Function set_report_html_in_catia_session_lock(report_generation_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     report_generation_sheet_setting_att.SetReportHtmlInCatiaSessionLock iLocked
        # #     set_report_html_in_catia_session_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_report_objects_information_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetReportObjectsInformationLock(boolean iLocked)
                | 
                |     Locks or unlocks the ReportObjectsInformation parameter.
                |     Role:Locks or unlocks the ReportObjectsInformation parameter if it is
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
        return self.report_generation_sheet_setting_att.SetReportObjectsInformationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_report_objects_information_lock'
        # # vba_code = """
        # # Public Function set_report_objects_information_lock(report_generation_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     report_generation_sheet_setting_att.SetReportObjectsInformationLock iLocked
        # #     set_report_objects_information_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_report_output_directory_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetReportOutputDirectoryLock(boolean iLocked)
                | 
                |     Locks or unlocks the ReportOutputDirectory parameter.
                |     Role:Locks or unlocks the ReportOutputDirectory parameter if it is possible
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
        return self.report_generation_sheet_setting_att.SetReportOutputDirectoryLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_report_output_directory_lock'
        # # vba_code = """
        # # Public Function set_report_output_directory_lock(report_generation_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     report_generation_sheet_setting_att.SetReportOutputDirectoryLock iLocked
        # #     set_report_output_directory_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_report_parameters_information_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetReportParametersInformationLock(boolean iLocked)
                | 
                |     Locks or unlocks the ReportParametersInformation
                |     parameter.
                |     Role:Locks or unlocks the ReportParametersInformation parameter if it is
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
        return self.report_generation_sheet_setting_att.SetReportParametersInformationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_report_parameters_information_lock'
        # # vba_code = """
        # # Public Function set_report_parameters_information_lock(report_generation_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     report_generation_sheet_setting_att.SetReportParametersInformationLock iLocked
        # #     set_report_parameters_information_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_report_passed_objects_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetReportPassedObjectsLock(boolean iLocked)
                | 
                |     Locks or unlocks the ReportPassedObjects parameter.
                |     Role:Locks or unlocks the ReportPassedObjects parameter if it is possible
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
        return self.report_generation_sheet_setting_att.SetReportPassedObjectsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_report_passed_objects_lock'
        # # vba_code = """
        # # Public Function set_report_passed_objects_lock(report_generation_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     report_generation_sheet_setting_att.SetReportPassedObjectsLock iLocked
        # #     set_report_passed_objects_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ReportGenerationSheetSettingAtt(name="{self.name}")'
