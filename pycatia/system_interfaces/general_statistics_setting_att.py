#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class GeneralStatisticsSettingAtt(SettingController):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         GeneralStatisticsSettingAtt
                | 
                | Interface for General statistic Controller.
                | 
                | Role: the General statistics controller is a generic interface for all the
                | thematics. One should never use it as a statistics thematic.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.general_statistics_setting_att = com_object

    @property
    def activation(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Activation() As boolean
                | 
                |     Returns or sets the activation state of the statistics
                |     thematic.
                |     Role: Returns or sets the value of statistics thematic activation.

        :return: bool
        """

        return self.general_statistics_setting_att.Activation

    @activation.setter
    def activation(self, value):
        """
        :param bool value:
        """

        self.general_statistics_setting_att.Activation = value

    @property
    def cpus(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CPUS() As boolean
                | 
                |     Returns or sets the state ot the cpu time field.
                |     Role: Returns or sets the state ot the cpu time field.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             Legal values:
                |             TRUE : the field is activated
                |             FALSE: the field is not activated

        :return: bool
        """

        return self.general_statistics_setting_att.CPUS

    @cpus.setter
    def cpus(self, value):
        """
        :param bool value:
        """

        self.general_statistics_setting_att.CPUS = value

    @property
    def cumulation_mode(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CumulationMode() As boolean
                | 
                |     Returns or sets the cumulation state of the statistics
                |     thematic.
                |     Role: Returns or sets the value of statistics thematic cumulation.

        :return: bool
        """

        return self.general_statistics_setting_att.CumulationMode

    @cumulation_mode.setter
    def cumulation_mode(self, value):
        """
        :param bool value:
        """

        self.general_statistics_setting_att.CumulationMode = value

    @property
    def date_format(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property DateFormat() As CATBSTR
                | 
                |     Returns or sets the state ot the date format field.
                |     Role: Returns or sets the state ot the date format field.
                | 
                |     Parameters:
                | 
                |         iDateFormat
                |             Legal values:
                |             StandardDate : default date format (Mon Jan 1 08:00.00 2000)
                |             NumericalDate: numerical date
                |             format(2000.001.08.00.00)
                |             NumericalDateMilliecond: numerical date
                |             format(2000.001.08.00.00.000)

        :return: str
        """

        return self.general_statistics_setting_att.DateFormat

    @date_format.setter
    def date_format(self, value):
        """
        :param str value:
        """

        self.general_statistics_setting_att.DateFormat = value

    @property
    def elps(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ELPS() As boolean
                | 
                |     Returns or sets the state ot the elapsed time field.
                |     Role: Returns or sets the state ot the elapsed time field.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             Legal values:
                |             TRUE : the field is activated
                |             FALSE: the field is not activated

        :return: bool
        """

        return self.general_statistics_setting_att.ELPS

    @elps.setter
    def elps(self, value):
        """
        :param bool value:
        """

        self.general_statistics_setting_att.ELPS = value

    @property
    def host(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property HOST() As boolean
                | 
                |     Returns or sets the state ot the host name field.
                |     Role: Returns or sets the state ot the host name field.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             Legal values:
                |             TRUE : the field is activated
                |             FALSE: the field is not activated

        :return: bool
        """

        return self.general_statistics_setting_att.HOST

    @host.setter
    def host(self, value):
        """
        :param bool value:
        """

        self.general_statistics_setting_att.HOST = value

    @property
    def output(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Output() As CATBSTR
                | 
                |     Returns or sets the output format of the statistics
                |     thematic.
                |     Role: Returns or sets the output format of the statistics
                |     thematic.
                | 
                |     Parameters:
                | 
                |         oOutputType
                |             Legal values:
                |             File :statistics are outputed in a file
                |             Console: statistics are outputed on the console (if
                |             available)

        :return: str
        """

        return self.general_statistics_setting_att.Output

    @output.setter
    def output(self, value):
        """
        :param str value:
        """

        self.general_statistics_setting_att.Output = value

    @property
    def output_file(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property OutputFile() As CATBSTR
                | 
                |     Returns or sets the path of the statistics thematic file.
                |     Role: Returns or sets the path of the statistics thematic file.

        :return: str
        """

        return self.general_statistics_setting_att.OutputFile

    @output_file.setter
    def output_file(self, value):
        """
        :param str value:
        """

        self.general_statistics_setting_att.OutputFile = value

    @property
    def output_format(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property OutputFormat() As CATBSTR
                | 
                |     Returns or sets the state ot the output format field.
                |     Role: Returns or sets the state ot the output format
                |     field.
                | 
                |     Parameters:
                | 
                |         iOutputFormat
                |             Legal values:
                |             StandardOutput: default format
                |             NoThematics : the thematic name is not repeated on each line

        :return: str
        """

        return self.general_statistics_setting_att.OutputFormat

    @output_format.setter
    def output_format(self, value):
        """
        :param str value:
        """

        self.general_statistics_setting_att.OutputFormat = value

    @property
    def rtim(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property RTIM() As boolean
                | 
                |     Returns or sets the state ot the response time field.
                |     Role: Returns or sets the state ot the response time
                |     field.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             Legal values:
                |             TRUE : the field is activated
                |             FALSE: the field is not activated

        :return: bool
        """

        return self.general_statistics_setting_att.RTIM

    @rtim.setter
    def rtim(self, value):
        """
        :param bool value:
        """

        self.general_statistics_setting_att.RTIM = value

    @property
    def them(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property THEM() As boolean
                | 
                |     Returns or sets the state ot the thematic field.
                |     Role: Returns or sets the state ot the thematic field.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             Legal values:
                |             TRUE : the field is activated
                |             FALSE: the field is not activated

        :return: bool
        """

        return self.general_statistics_setting_att.THEM

    @them.setter
    def them(self, value):
        """
        :param bool value:
        """

        self.general_statistics_setting_att.THEM = value

    @property
    def time(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property TIME() As boolean
                | 
                |     Returns or sets the state ot the time and date field.
                |     Role: Returns or sets the state ot the time and date
                |     field.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             Legal values:
                |             TRUE : the field is activated
                |             FALSE: the field is not activated

        :return: bool
        """

        return self.general_statistics_setting_att.TIME

    @time.setter
    def time(self, value):
        """
        :param bool value:
        """

        self.general_statistics_setting_att.TIME = value

    @property
    def time_unit(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property TimeUnit() As CATBSTR
                | 
                |     Returns or sets the state ot the time unit field.
                |     Role: Returns or sets the state ot the time unit field.
                | 
                |     Parameters:
                | 
                |         iTimeUnit
                |             Legal values:
                |             Second : durations are in seconds
                |             Millisecond: durations are in milliseconds

        :return: str
        """

        return self.general_statistics_setting_att.TimeUnit

    @time_unit.setter
    def time_unit(self, value):
        """
        :param str value:
        """

        self.general_statistics_setting_att.TimeUnit = value

    @property
    def upid(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property UPID() As boolean
                | 
                |     Returns or sets the state ot the user pid field.
                |     Role: Returns or sets the state ot the user pid field.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             Legal values:
                |             TRUE : the field is activated
                |             FALSE: the field is not activated

        :return: bool
        """

        return self.general_statistics_setting_att.UPID

    @upid.setter
    def upid(self, value):
        """
        :param bool value:
        """

        self.general_statistics_setting_att.UPID = value

    @property
    def user(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property USER() As boolean
                | 
                |     Returns or sets the state ot the user name field.
                |     Role: Returns or sets the state ot the user name field.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             Legal values:
                |             TRUE : the field is activated
                |             FALSE: the field is not activated

        :return: bool
        """

        return self.general_statistics_setting_att.USER

    @user.setter
    def user(self, value):
        """
        :param bool value:
        """

        self.general_statistics_setting_att.USER = value

    def get_format_mode(self, flag):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetFormatMode(long flag) As boolean
                | 
                |     Returns the format mode of the statistics thematic.
                |     Role: Returns or sets the format mode of the statistics
                |     thematic.
                | 
                |     Parameters:
                | 
                |         oFormatMode
                |             Legal values:
                |             TRUE : the thematic output is formated (field="value").
                |             FALSE: the thematic output is not formated
                |             ("value").

        :param int flag:
        :return: bool
        """
        return bool(self.general_statistics_setting_att.GetFormatMode(flag))

    def get_thematics_parameter_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetThematicsParameterInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the general statistics
                |     parameters.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.general_statistics_setting_att.GetThematicsParameterInfo(admin_level, o_locked)

    def set_format_mode(self, i_format_mode, flag):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetFormatMode(boolean iFormatMode,
                | long flag)
                | 
                |     Sets the format mode of the statistics thematic.
                |     Role: Returns or sets the format mode of the statistics
                |     thematic.
                | 
                |     Parameters:
                | 
                |         iFormatMode
                |             Legal values:
                |             TRUE : the thematic output is formated (field="value").
                |             FALSE: the thematic output is not formated
                |             ("value").

        :param bool i_format_mode:
        :param int flag:
        :return: None
        """
        return self.general_statistics_setting_att.SetFormatMode(i_format_mode, flag)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_format_mode'
        # # vba_code = """
        # # Public Function set_format_mode(general_statistics_setting_att)
        # #     Dim iFormatMode (2)
        # #     general_statistics_setting_att.SetFormatMode iFormatMode
        # #     set_format_mode = iFormatMode
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_thematics_parameter_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetThematicsParameterLock(boolean iLocked)
                | 
                |     Locks or unlocks the general statistics parameters.
                |     Role:Locks or unlocks the statistics parameters.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :return: None
        """
        return self.general_statistics_setting_att.SetThematicsParameterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_thematics_parameter_lock'
        # # vba_code = """
        # # Public Function set_thematics_parameter_lock(general_statistics_setting_att)
        # #     Dim iLocked (2)
        # #     general_statistics_setting_att.SetThematicsParameterLock iLocked
        # #     set_thematics_parameter_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'GeneralStatisticsSettingAtt(name="{ self.name }")'
