#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class RenderingSettingAtt(SettingController):
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
                |                         RenderingSettingAtt
                | 
                | The interface to access a CATIARenderingSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rendering_setting_att = com_object

    @property
    def engine_interface(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EngineInterface() As CATBSTR
                | 
                |     Returns or sets the EngineInterface parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.rendering_setting_att.EngineInterface

    @engine_interface.setter
    def engine_interface(self, value: str):
        """
        :param str value:
        """

        self.rendering_setting_att.EngineInterface = value

    @property
    def output_height(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OutputHeight() As short
                | 
                |     Returns or sets the OutputHeight parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.rendering_setting_att.OutputHeight

    @output_height.setter
    def output_height(self, value: int):
        """
        :param int value:
        """

        self.rendering_setting_att.OutputHeight = value

    @property
    def output_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OutputPath() As CATBSTR
                | 
                |     Returns or sets the OutputPath parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.rendering_setting_att.OutputPath

    @output_path.setter
    def output_path(self, value: str):
        """
        :param str value:
        """

        self.rendering_setting_att.OutputPath = value

    @property
    def output_size_from(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OutputSizeFrom() As short
                | 
                |     Returns or sets the OutputSizeFrom parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is
                |     delegated.
                | 
                |     Parameters:
                | 
                |         OutputSizeFrom
                |             where to get the image size for a QuickRender. Legal
                |             values:
                |             1 : same size as viewpoint.
                |             2 : fixed size. Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.rendering_setting_att.OutputSizeFrom

    @output_size_from.setter
    def output_size_from(self, value: int):
        """
        :param int value:
        """

        self.rendering_setting_att.OutputSizeFrom = value

    @property
    def output_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OutputType() As short
                | 
                |     Returns or sets the OutputType parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is
                |     delegated.
                | 
                |     Parameters:
                | 
                |         OutputType
                |             where to save the image after a QuickRender. Legal
                |             values:
                |             1 : image saved to default file.
                |             2 : save image to specific file.

        :rtype: int
        """

        return self.rendering_setting_att.OutputType

    @output_type.setter
    def output_type(self, value: int):
        """
        :param int value:
        """

        self.rendering_setting_att.OutputType = value

    @property
    def output_width(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OutputWidth() As short
                | 
                |     Returns or sets the OutputWidth parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.rendering_setting_att.OutputWidth

    @output_width.setter
    def output_width(self, value: int):
        """
        :param int value:
        """

        self.rendering_setting_att.OutputWidth = value

    @property
    def save_auto_increment(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SaveAutoIncrement() As boolean
                | 
                |     Returns or sets the SaveAutoIncrement parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.rendering_setting_att.SaveAutoIncrement

    @save_auto_increment.setter
    def save_auto_increment(self, value: bool):
        """
        :param bool value:
        """

        self.rendering_setting_att.SaveAutoIncrement = value

    def get_engine_interface_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetEngineInterfaceInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the EngineInterface
                |     parameter.
                |     Role:Retrieves the state of the EngineInterface parameter in the current
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
        return self.rendering_setting_att.GetEngineInterfaceInfo(io_admin_level, io_locked)

    def get_output_height_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOutputHeightInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the OutputHeight
                |     parameter.
                |     Role:Retrieves the state of the OutputHeight parameter in the current
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
        return self.rendering_setting_att.GetOutputHeightInfo(io_admin_level, io_locked)

    def get_output_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOutputPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the OutputPath
                |     parameter.
                |     Role:Retrieves the state of the OutputPath parameter in the current
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
        return self.rendering_setting_att.GetOutputPathInfo(io_admin_level, io_locked)

    def get_output_size_from_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOutputSizeFromInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the OutputSizeFrom
                |     parameter.
                |     Role:Retrieves the state of the OutputSizeFrom parameter in the current
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
        return self.rendering_setting_att.GetOutputSizeFromInfo(io_admin_level, io_locked)

    def get_output_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOutputTypeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the OutputType
                |     parameter.
                |     Role:Retrieves the state of the OutputType parameter in the current
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
        return self.rendering_setting_att.GetOutputTypeInfo(io_admin_level, io_locked)

    def get_output_width_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOutputWidthInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the OutputWidth
                |     parameter.
                |     Role:Retrieves the state of the OutputWidth parameter in the current
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
        return self.rendering_setting_att.GetOutputWidthInfo(io_admin_level, io_locked)

    def get_save_auto_increment_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSaveAutoIncrementInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SaveAutoIncrement
                |     parameter.
                |     Role:Retrieves the state of the SaveAutoIncrement parameter in the current
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
        return self.rendering_setting_att.GetSaveAutoIncrementInfo(io_admin_level, io_locked)

    def set_engine_interface_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetEngineInterfaceLock(boolean iLocked)
                | 
                |     Locks or unlocks the EngineInterface parameter.
                |     Role:Locks or unlocks the EngineInterface parameter if it is possible in
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
        return self.rendering_setting_att.SetEngineInterfaceLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_engine_interface_lock'
        # # vba_code = """
        # # Public Function set_engine_interface_lock(rendering_setting_att)
        # #     Dim iLocked (2)
        # #     rendering_setting_att.SetEngineInterfaceLock iLocked
        # #     set_engine_interface_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_output_height_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOutputHeightLock(boolean iLocked)
                | 
                |     Locks or unlocks the OutputHeight parameter.
                |     Role:Locks or unlocks the OutputHeight parameter if it is possible in the
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
        return self.rendering_setting_att.SetOutputHeightLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_output_height_lock'
        # # vba_code = """
        # # Public Function set_output_height_lock(rendering_setting_att)
        # #     Dim iLocked (2)
        # #     rendering_setting_att.SetOutputHeightLock iLocked
        # #     set_output_height_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_output_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOutputPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the OutputPath parameter.
                |     Role:Locks or unlocks the OutputPath parameter if it is possible in the
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
        return self.rendering_setting_att.SetOutputPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_output_path_lock'
        # # vba_code = """
        # # Public Function set_output_path_lock(rendering_setting_att)
        # #     Dim iLocked (2)
        # #     rendering_setting_att.SetOutputPathLock iLocked
        # #     set_output_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_output_size_from_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOutputSizeFromLock(boolean iLocked)
                | 
                |     Locks or unlocks the OutputSizeFrom parameter.
                |     Role:Locks or unlocks the OutputSizeFrom parameter if it is possible in the
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
        return self.rendering_setting_att.SetOutputSizeFromLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_output_size_from_lock'
        # # vba_code = """
        # # Public Function set_output_size_from_lock(rendering_setting_att)
        # #     Dim iLocked (2)
        # #     rendering_setting_att.SetOutputSizeFromLock iLocked
        # #     set_output_size_from_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_output_type_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOutputTypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the OutputType parameter.
                |     Role:Locks or unlocks the OutputType parameter if it is possible in the
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
        return self.rendering_setting_att.SetOutputTypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_output_type_lock'
        # # vba_code = """
        # # Public Function set_output_type_lock(rendering_setting_att)
        # #     Dim iLocked (2)
        # #     rendering_setting_att.SetOutputTypeLock iLocked
        # #     set_output_type_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_output_width_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOutputWidthLock(boolean iLocked)
                | 
                |     Locks or unlocks the OutputWidth parameter.
                |     Role:Locks or unlocks the OutputWidth parameter if it is possible in the
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
        return self.rendering_setting_att.SetOutputWidthLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_output_width_lock'
        # # vba_code = """
        # # Public Function set_output_width_lock(rendering_setting_att)
        # #     Dim iLocked (2)
        # #     rendering_setting_att.SetOutputWidthLock iLocked
        # #     set_output_width_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_save_auto_increment_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSaveAutoIncrementLock(boolean iLocked)
                | 
                |     Locks or unlocks the SaveAutoIncrement parameter.
                |     Role:Locks or unlocks the SaveAutoIncrement parameter if it is possible in
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
        return self.rendering_setting_att.SetSaveAutoIncrementLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_save_auto_increment_lock'
        # # vba_code = """
        # # Public Function set_save_auto_increment_lock(rendering_setting_att)
        # #     Dim iLocked (2)
        # #     rendering_setting_att.SetSaveAutoIncrementLock iLocked
        # #     set_save_auto_increment_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'RenderingSettingAtt(name="{self.name}")'
