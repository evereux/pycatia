#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class CacheSettingAtt(SettingController):

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
                |                         CacheSettingAtt
                | 
                | Represents the base object to handle the parameters of the
                | cache.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cache_setting_att = com_object

    @property
    def activation_mode(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ActivationMode() As boolean
                | 
                |     Returns or sets the activation state of cache.
                |     Role: Returns or sets the value of cache activation.

        :return: bool
        """

        return self.cache_setting_att.ActivationMode

    @activation_mode.setter
    def activation_mode(self, value):
        """
        :param bool value:
        """

        self.cache_setting_att.ActivationMode = value

    @property
    def cache_max_size_mo(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CacheMaxSizeMo() As long
                | 
                |     Returns or sets the value of the cache maximum size.
                |     Role: Returns or sets the value of the maximum allowed cache size in Mo

        :return: int
        """

        return self.cache_setting_att.CacheMaxSizeMo

    @cache_max_size_mo.setter
    def cache_max_size_mo(self, value):
        """
        :param int value:
        """

        self.cache_setting_att.CacheMaxSizeMo = value

    @property
    def lod_mode(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property LODMode() As boolean
                | 
                |     Returns or sets the LOD generation mode parameter.
                |     Role: Returns or sets the value of the LOD generation mode.

        :return: bool
        """

        return self.cache_setting_att.LODMode

    @lod_mode.setter
    def lod_mode(self, value):
        """
        :param bool value:
        """

        self.cache_setting_att.LODMode = value

    @property
    def local_path(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property LocalPath() As CATBSTR
                | 
                |     Retrieves or sets the cache local path.
                |     Role: Retrieves or sets the value of the cache local path. If the local
                |     path is defined with environment variables then this method return the
                |     unexpansed form.

        :return: str
        """

        return self.cache_setting_att.LocalPath

    @local_path.setter
    def local_path(self, value):
        """
        :param str value:
        """

        self.cache_setting_att.LocalPath = value

    @property
    def released_voxel(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ReleasedVoxel() As float
                | 
                |     Returns or sets the released voxel parameter.
                |     Role: Returns or sets the value of the released voxel parameter.

        :return: float
        """

        return self.cache_setting_att.ReleasedVoxel

    @released_voxel.setter
    def released_voxel(self, value):
        """
        :param float value:
        """

        self.cache_setting_att.ReleasedVoxel = value

    @property
    def size_control(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property SizeControl() As boolean
                | 
                |     Return or sets the cache size control.
                |     Role: Returns or sets the cache size control. The cache use this parameter
                |     in conjunction with the maxixum allowed cache size. If it is turned off, the
                |     cache size has no limit.

        :return: bool
        """

        return self.cache_setting_att.SizeControl

    @size_control.setter
    def size_control(self, value):
        """
        :param bool value:
        """

        self.cache_setting_att.SizeControl = value

    @property
    def timestamp_mode(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property TimestampMode() As boolean
                | 
                |     Retrieves or sets the timestamp control.
                |     Role: If the timestamp control is turned on, the cache will verify if the
                |     cached object is uptodate with the master object. If not a new cached view will
                |     be generated.
                |     If the timestamp control is turned off, the cache will consider that the
                |     cached views are always uptodate with their master object.

        :return: bool
        """

        return self.cache_setting_att.TimestampMode

    @timestamp_mode.setter
    def timestamp_mode(self, value):
        """
        :param bool value:
        """

        self.cache_setting_att.TimestampMode = value

    @property
    def utc_time_format(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property UTCTimeFormat() As boolean
                | 
                |     Retrieves or sets the the cache timestamp format.
                |     Role: If the timestamp format is set to TRUE, then the time used used as
                |     timestamp by the cache is expressed in UTC format (GMT), in the other case the
                |     local time is used. The default format is local time.

        :return: bool
        """

        return self.cache_setting_att.UTCTimeFormat

    @utc_time_format.setter
    def utc_time_format(self, value):
        """
        :param bool value:
        """

        self.cache_setting_att.UTCTimeFormat = value

    def get_activation_mode_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetActivationModeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Cache activation mode.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.cache_setting_att.GetActivationModeInfo(admin_level, o_locked)

    def get_cache_max_size_mo_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetCacheMaxSizeMoInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the Cache maximum
                |     size.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.cache_setting_att.GetCacheMaxSizeMoInfo(admin_level, o_locked)

    def get_lod_mode_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetLODModeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the LOD generation
                |     mode.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.cache_setting_att.GetLODModeInfo(admin_level, o_locked)

    def get_local_path_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetLocalPathInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the Cache local
                |     path.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.cache_setting_att.GetLocalPathInfo(admin_level, o_locked)

    def get_release_path(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetReleasePath() As CATSafeArrayVariant
                | 
                |     Retieves the cache release paths.
                |     Role: Sets the cache release paths in a symbolic format.
                | 
                |     Parameters:
                | 
                |         ioRelPath
                |             a CATSafeArrayVariant of CATBSTR. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: tuple
        """
        return tuple(self.cache_setting_att.GetReleasePath())

    def get_release_path_info(self, admin_level, locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetReleasePathInfo(CATBSTR AdminLevel,
                | CATBSTR Locked) As boolean
                | 
                |     Retrieves environment informations for the Cache release
                |     path.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str locked:
        :return: None
        """
        return self.cache_setting_att.GetReleasePathInfo(admin_level, locked)

    def get_released_voxel_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetReleasedVoxelInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the Cache released
                |     voxel.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.cache_setting_att.GetReleasedVoxelInfo(admin_level, o_locked)

    def get_size_control_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetSizeControlInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the size control
                |     mode.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.cache_setting_att.GetSizeControlInfo(admin_level, o_locked)

    def get_timestamp_mode_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetTimestampModeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the timestamp control
                |     mode.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.cache_setting_att.GetTimestampModeInfo(admin_level, o_locked)

    def get_utc_time_format_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetUTCTimeFormatInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the timestamp control
                |     mode.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.cache_setting_att.GetUTCTimeFormatInfo(admin_level, o_locked)

    def put_release_path(self, i_rel_path):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub PutReleasePath(CATSafeArrayVariant iRelPath)
                | 
                |     Sets the cache release paths.
                |     Role: Sets the cache release paths in a symbolic format.
                | 
                |     Parameters:
                | 
                |         iRelPath
                |             a CATSafeArrayVariant of CATBSTR. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param tuple i_rel_path:
        :return: None
        """
        return self.cache_setting_att.PutReleasePath(i_rel_path)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_release_path'
        # # vba_code = """
        # # Public Function put_release_path(cache_setting_att)
        # #     Dim iRelPath (2)
        # #     cache_setting_att.PutReleasePath iRelPath
        # #     put_release_path = iRelPath
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_activation_mode_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetActivationModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Cache Activation mode.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.cache_setting_att.SetActivationModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_activation_mode_lock'
        # # vba_code = """
        # # Public Function set_activation_mode_lock(cache_setting_att)
        # #     Dim iLocked (2)
        # #     cache_setting_att.SetActivationModeLock iLocked
        # #     set_activation_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_cache_max_size_mo_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetCacheMaxSizeMoLock(boolean iLocked)
                | 
                |     Locks the paramater Cache maximum size.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.cache_setting_att.SetCacheMaxSizeMoLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_cache_max_size_mo_lock'
        # # vba_code = """
        # # Public Function set_cache_max_size_mo_lock(cache_setting_att)
        # #     Dim iLocked (2)
        # #     cache_setting_att.SetCacheMaxSizeMoLock iLocked
        # #     set_cache_max_size_mo_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_lod_mode_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetLODModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the LOD generation mode.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.cache_setting_att.SetLODModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_lod_mode_lock'
        # # vba_code = """
        # # Public Function set_lod_mode_lock(cache_setting_att)
        # #     Dim iLocked (2)
        # #     cache_setting_att.SetLODModeLock iLocked
        # #     set_lod_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_local_path_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetLocalPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the cache local path parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.cache_setting_att.SetLocalPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_local_path_lock'
        # # vba_code = """
        # # Public Function set_local_path_lock(cache_setting_att)
        # #     Dim iLocked (2)
        # #     cache_setting_att.SetLocalPathLock iLocked
        # #     set_local_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_release_path_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetReleasePathLock(boolean iLocked)
                | 
                |     Locks or unlocks the cache local path parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.cache_setting_att.SetReleasePathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_release_path_lock'
        # # vba_code = """
        # # Public Function set_release_path_lock(cache_setting_att)
        # #     Dim iLocked (2)
        # #     cache_setting_att.SetReleasePathLock iLocked
        # #     set_release_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_released_voxel_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetReleasedVoxelLock(boolean iLocked)
                | 
                |     Locks or unlocks the released voxel parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.cache_setting_att.SetReleasedVoxelLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_released_voxel_lock'
        # # vba_code = """
        # # Public Function set_released_voxel_lock(cache_setting_att)
        # #     Dim iLocked (2)
        # #     cache_setting_att.SetReleasedVoxelLock iLocked
        # #     set_released_voxel_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_size_control_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetSizeControlLock(boolean iLocked)
                | 
                |     Locks or unlocks the cache size control parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.cache_setting_att.SetSizeControlLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_size_control_lock'
        # # vba_code = """
        # # Public Function set_size_control_lock(cache_setting_att)
        # #     Dim iLocked (2)
        # #     cache_setting_att.SetSizeControlLock iLocked
        # #     set_size_control_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_timestamp_mode_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetTimestampModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the timestamp control in cache.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.cache_setting_att.SetTimestampModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_timestamp_mode_lock'
        # # vba_code = """
        # # Public Function set_timestamp_mode_lock(cache_setting_att)
        # #     Dim iLocked (2)
        # #     cache_setting_att.SetTimestampModeLock iLocked
        # #     set_timestamp_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_utc_time_format_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetUTCTimeFormatLock(boolean iLocked)
                | 
                |     Locks or unlocks the timestamp format.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.cache_setting_att.SetUTCTimeFormatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_utc_time_format_lock'
        # # vba_code = """
        # # Public Function set_utc_time_format_lock(cache_setting_att)
        # #     Dim iLocked (2)
        # #     cache_setting_att.SetUTCTimeFormatLock iLocked
        # #     set_utc_time_format_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'CacheSettingAtt(name="{ self.name }")'
