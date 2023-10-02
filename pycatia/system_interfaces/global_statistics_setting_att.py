#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class GlobalStatisticsSettingAtt(SettingController):

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
                |                         GlobalStatisticsSettingAtt
                | 
                | Interface for Global statistic Controller
                | Role: the global statistics controller manages the values of all or only a part
                | of the attributes available for all the statistics thematics.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.global_statistics_setting_att = com_object

    @property
    def buffer_size(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property BufferSize() As long
                | 
                |     Returns or sets the size of buffer.
                |     Role: Returns or sets the size of the buffer.
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :return: int
        """

        return self.global_statistics_setting_att.BufferSize

    @buffer_size.setter
    def buffer_size(self, value):
        """
        :param int value:
        """

        self.global_statistics_setting_att.BufferSize = value

    @property
    def copy_directory(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CopyDirectory() As CATBSTR
                | 
                |     Returns or sets the path of the copy directory.
                |     Role: Returns or sets the path of the directory where the copy files are
                |     located.
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :return: str
        """

        return self.global_statistics_setting_att.CopyDirectory

    @copy_directory.setter
    def copy_directory(self, value):
        """
        :param str value:
        """

        self.global_statistics_setting_att.CopyDirectory = value

    @property
    def max_copy_file(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property MaxCopyFile() As long
                | 
                |     Returns or sets the maximum number of copy files.
                |     Role: Returns or sets the value of the maximum number of statistics files
                |     copies.
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :return: int
        """

        return self.global_statistics_setting_att.MaxCopyFile

    @max_copy_file.setter
    def max_copy_file(self, value):
        """
        :param int value:
        """

        self.global_statistics_setting_att.MaxCopyFile = value

    @property
    def max_size_per_file(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property MaxSizePerFile() As long
                | 
                |     Returns or sets the maximum size per file.
                |     Role: Returns or sets the value of the maximum size of statistics
                |     files.
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :return: int
        """

        return self.global_statistics_setting_att.MaxSizePerFile

    @max_size_per_file.setter
    def max_size_per_file(self, value):
        """
        :param int value:
        """

        self.global_statistics_setting_att.MaxSizePerFile = value

    def get_thematics_parameter_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetThematicsParameterInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the global statistics
                |     parameters.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.global_statistics_setting_att.GetThematicsParameterInfo(admin_level, o_locked)

    def set_thematics_parameter_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetThematicsParameterLock(boolean iLocked)
                | 
                |     Locks or unlocks the global statistics parameters.
                |     Role:Locks or unlocks the global statistics parameters.
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
        return self.global_statistics_setting_att.SetThematicsParameterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_thematics_parameter_lock'
        # # vba_code = """
        # # Public Function set_thematics_parameter_lock(global_statistics_setting_att)
        # #     Dim iLocked (2)
        # #     global_statistics_setting_att.SetThematicsParameterLock iLocked
        # #     set_thematics_parameter_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'GlobalStatisticsSettingAtt(name="{ self.name }")'
