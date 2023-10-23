#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class SimTraceSettingAtt(SettingController):
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
                |                         SimTraceSettingAtt
                | 
                | Interface to handle parameters of Infrastructure-DELMIA
                | Infrastructure-Simulation Trace Tools Options Tab page.
                | Role: This interface is implemented by a component which represents the
                | controller of Simulation Trace Tools Options parameter
                | settings.
                | 
                |     Methods to set value of each parameter xxx
                |     Methods to get value of each parameter xxx
                |     Methods to get information on each parameter xxx
                |     Methods to lock/unlock value of each parameter xxx
                | 
                | Here is the list of parameters to use and their meaning:
                | 
                |     TracePointVisu: defines the option for displaying the points within a
                |     simulation trace.
                |     TracePointColor: defines the color to be used if displaying points within a
                |     simulation trace.
                |     TracePointSymbol: defines the symbol to be used if displaying points within
                |     a simulation trace.
                |     TraceLineVisu: defines the option for displaying the lines within a
                |     simulation trace.
                |     TraceLineColor: defines the color to be used if displaying lines within a
                |     simulation trace.
                |     TraceLineType: defines the line type to be used if displaying lines within
                |     a simulation trace.
                |     TraceLineThick: defines the thickness to be used if displaying lines within
                |     a simulation trace.
                |     TraceAxisVisu: defines the option for displaying the axis within a
                |     simulation trace.
                |     TraceAxisColor: defines the color to be used if displaying axis within a
                |     simulation trace.
                |     TraceAxisType: defines the line type to be used if displaying axis within a
                |     simulation trace.
                |     TraceAxisThick: defines the thickness to be used if displaying axis within
                |     a simulation trace.
                |     TraceDeletePath: defines the option for deleting the simulation trace when
                |     a new simulation is run.
                |     TraceLegend: defines the type of information to be displayed when a
                |     point/line/axis within a simulation trace is (pre)selected by the user. The
                |     values are in order:
                |         All Legend (not used).
                |         Name.
                |         X.
                |         Y.
                |         Z.
                |         Yaw.
                |         Pitch.
                |         Roll.
                |         Cycle Time.
                |         Show Legend.
                |         Always Visible (not used).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sim_trace_setting_att = com_object

    def get_trace_axis_colour_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTraceAxisColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TraceAxisColor
                |     parameter.
                |     Role:Retrieves the state of the TraceAxisColor parameter in the current
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
        return self.sim_trace_setting_att.GetTraceAxisColorInfo(io_admin_level, io_locked)

    def get_trace_axis_thick_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTraceAxisThickInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TraceAxisThick
                |     parameter.
                |     Role:Retrieves the state of the TraceAxisThick parameter in the current
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
        return self.sim_trace_setting_att.GetTraceAxisThickInfo(io_admin_level, io_locked)

    def get_trace_axis_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTraceAxisTypeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TraceAxisType
                |     parameter.
                |     Role:Retrieves the state of the TraceAxisType parameter in the current
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
        return self.sim_trace_setting_att.GetTraceAxisTypeInfo(io_admin_level, io_locked)

    def get_trace_axis_visu_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTraceAxisVisuInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TraceAxisVisu
                |     parameter.
                |     Role:Retrieves the state of the TraceAxisVisu parameter in the current
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
        return self.sim_trace_setting_att.GetTraceAxisVisuInfo(io_admin_level, io_locked)

    def get_trace_delete_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTraceDeletePathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TraceDeletePath
                |     parameter.
                |     Role:Retrieves the state of the TraceDeletePath parameter in the current
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
        return self.sim_trace_setting_att.GetTraceDeletePathInfo(io_admin_level, io_locked)

    def get_trace_legend_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTraceLegendInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TraceLegend
                |     parameter.
                |     Role:Retrieves the state of the TraceLegend parameter in the current
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
        return self.sim_trace_setting_att.GetTraceLegendInfo(io_admin_level, io_locked)

    def get_trace_line_colour_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTraceLineColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TraceLineColor
                |     parameter.
                |     Role:Retrieves the state of the TraceLineColor parameter in the current
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
        return self.sim_trace_setting_att.GetTraceLineColorInfo(io_admin_level, io_locked)

    def get_trace_line_thick_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTraceLineThickInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TraceLineThick
                |     parameter.
                |     Role:Retrieves the state of the TraceLineThick parameter in the current
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
        return self.sim_trace_setting_att.GetTraceLineThickInfo(io_admin_level, io_locked)

    def get_trace_line_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTraceLineTypeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TraceLineType
                |     parameter.
                |     Role:Retrieves the state of the TraceLineType parameter in the current
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
        return self.sim_trace_setting_att.GetTraceLineTypeInfo(io_admin_level, io_locked)

    def get_trace_line_visu_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTraceLineVisuInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TraceLineVisu
                |     parameter.
                |     Role:Retrieves the state of the TraceLineVisu parameter in the current
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
        return self.sim_trace_setting_att.GetTraceLineVisuInfo(io_admin_level, io_locked)

    def get_trace_point_colour_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTracePointColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TracePointColor
                |     parameter.
                |     Role:Retrieves the state of the TracePointColor parameter in the current
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
        return self.sim_trace_setting_att.GetTracePointColorInfo(io_admin_level, io_locked)

    def get_trace_point_symbol_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTracePointSymbolInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TracePointSymbol
                |     parameter.
                |     Role:Retrieves the state of the TracePointSymbol parameter in the current
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
        return self.sim_trace_setting_att.GetTracePointSymbolInfo(io_admin_level, io_locked)

    def get_trace_point_visu_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTracePointVisuInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TracePointVisu
                |     parameter.
                |     Role:Retrieves the state of the TracePointVisu parameter in the current
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
        return self.sim_trace_setting_att.GetTracePointVisuInfo(io_admin_level, io_locked)

    def set_trace_axis_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTraceAxisColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the TraceAxisColor parameter.
                |     Role:Locks or unlocks the TraceAxisColor parameter if it is possible in the
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
        return self.sim_trace_setting_att.SetTraceAxisColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_trace_axis_color_lock'
        # # vba_code = """
        # # Public Function set_trace_axis_color_lock(sim_trace_setting_att)
        # #     Dim iLocked (2)
        # #     sim_trace_setting_att.SetTraceAxisColorLock iLocked
        # #     set_trace_axis_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_trace_axis_thick_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTraceAxisThickLock(boolean iLocked)
                | 
                |     Locks or unlocks the TraceAxisThick parameter.
                |     Role:Locks or unlocks the TraceAxisThick parameter if it is possible in the
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
        return self.sim_trace_setting_att.SetTraceAxisThickLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_trace_axis_thick_lock'
        # # vba_code = """
        # # Public Function set_trace_axis_thick_lock(sim_trace_setting_att)
        # #     Dim iLocked (2)
        # #     sim_trace_setting_att.SetTraceAxisThickLock iLocked
        # #     set_trace_axis_thick_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_trace_axis_type_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTraceAxisTypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the TraceAxisType parameter.
                |     Role:Locks or unlocks the TraceAxisType parameter if it is possible in the
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
        return self.sim_trace_setting_att.SetTraceAxisTypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_trace_axis_type_lock'
        # # vba_code = """
        # # Public Function set_trace_axis_type_lock(sim_trace_setting_att)
        # #     Dim iLocked (2)
        # #     sim_trace_setting_att.SetTraceAxisTypeLock iLocked
        # #     set_trace_axis_type_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_trace_axis_visu_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTraceAxisVisuLock(boolean iLocked)
                | 
                |     Locks or unlocks the TraceAxisVisu parameter.
                |     Role:Locks or unlocks the TraceAxisVisu parameter if it is possible in the
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
        return self.sim_trace_setting_att.SetTraceAxisVisuLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_trace_axis_visu_lock'
        # # vba_code = """
        # # Public Function set_trace_axis_visu_lock(sim_trace_setting_att)
        # #     Dim iLocked (2)
        # #     sim_trace_setting_att.SetTraceAxisVisuLock iLocked
        # #     set_trace_axis_visu_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_trace_delete_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTraceDeletePathLock(boolean iLocked)
                | 
                |     Locks or unlocks the TraceDeletePath parameter.
                |     Role:Locks or unlocks the TraceDeletePath parameter if it is possible in
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
        return self.sim_trace_setting_att.SetTraceDeletePathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_trace_delete_path_lock'
        # # vba_code = """
        # # Public Function set_trace_delete_path_lock(sim_trace_setting_att)
        # #     Dim iLocked (2)
        # #     sim_trace_setting_att.SetTraceDeletePathLock iLocked
        # #     set_trace_delete_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_trace_legend_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTraceLegendLock(boolean iLocked)
                | 
                |     Locks or unlocks the TraceLegend parameter.
                |     Role:Locks or unlocks the TraceLegend parameter if it is possible in the
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
        return self.sim_trace_setting_att.SetTraceLegendLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_trace_legend_lock'
        # # vba_code = """
        # # Public Function set_trace_legend_lock(sim_trace_setting_att)
        # #     Dim iLocked (2)
        # #     sim_trace_setting_att.SetTraceLegendLock iLocked
        # #     set_trace_legend_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_trace_line_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTraceLineColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the TraceLineColor parameter.
                |     Role:Locks or unlocks the TraceLineColor parameter if it is possible in the
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
        return self.sim_trace_setting_att.SetTraceLineColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_trace_line_color_lock'
        # # vba_code = """
        # # Public Function set_trace_line_color_lock(sim_trace_setting_att)
        # #     Dim iLocked (2)
        # #     sim_trace_setting_att.SetTraceLineColorLock iLocked
        # #     set_trace_line_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_trace_line_thick_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTraceLineThickLock(boolean iLocked)
                | 
                |     Locks or unlocks the TraceLineThick parameter.
                |     Role:Locks or unlocks the TraceLineThick parameter if it is possible in the
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
        return self.sim_trace_setting_att.SetTraceLineThickLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_trace_line_thick_lock'
        # # vba_code = """
        # # Public Function set_trace_line_thick_lock(sim_trace_setting_att)
        # #     Dim iLocked (2)
        # #     sim_trace_setting_att.SetTraceLineThickLock iLocked
        # #     set_trace_line_thick_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_trace_line_type_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTraceLineTypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the TraceLineType parameter.
                |     Role:Locks or unlocks the TraceLineType parameter if it is possible in the
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
        return self.sim_trace_setting_att.SetTraceLineTypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_trace_line_type_lock'
        # # vba_code = """
        # # Public Function set_trace_line_type_lock(sim_trace_setting_att)
        # #     Dim iLocked (2)
        # #     sim_trace_setting_att.SetTraceLineTypeLock iLocked
        # #     set_trace_line_type_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_trace_line_visu_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTraceLineVisuLock(boolean iLocked)
                | 
                |     Locks or unlocks the TraceLineVisu parameter.
                |     Role:Locks or unlocks the TraceLineVisu parameter if it is possible in the
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
        return self.sim_trace_setting_att.SetTraceLineVisuLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_trace_line_visu_lock'
        # # vba_code = """
        # # Public Function set_trace_line_visu_lock(sim_trace_setting_att)
        # #     Dim iLocked (2)
        # #     sim_trace_setting_att.SetTraceLineVisuLock iLocked
        # #     set_trace_line_visu_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_trace_point_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTracePointColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the TracePointColor parameter.
                |     Role:Locks or unlocks the TracePointColor parameter if it is possible in
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
        return self.sim_trace_setting_att.SetTracePointColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_trace_point_color_lock'
        # # vba_code = """
        # # Public Function set_trace_point_color_lock(sim_trace_setting_att)
        # #     Dim iLocked (2)
        # #     sim_trace_setting_att.SetTracePointColorLock iLocked
        # #     set_trace_point_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_trace_point_symbol_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTracePointSymbolLock(boolean iLocked)
                | 
                |     Locks or unlocks the TracePointSymbol parameter.
                |     Role:Locks or unlocks the TracePointSymbol parameter if it is possible in
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
        return self.sim_trace_setting_att.SetTracePointSymbolLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_trace_point_symbol_lock'
        # # vba_code = """
        # # Public Function set_trace_point_symbol_lock(sim_trace_setting_att)
        # #     Dim iLocked (2)
        # #     sim_trace_setting_att.SetTracePointSymbolLock iLocked
        # #     set_trace_point_symbol_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_trace_point_visu_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTracePointVisuLock(boolean iLocked)
                | 
                |     Locks or unlocks the TracePointVisu parameter.
                |     Role:Locks or unlocks the TracePointVisu parameter if it is possible in the
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
        return self.sim_trace_setting_att.SetTracePointVisuLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_trace_point_visu_lock'
        # # vba_code = """
        # # Public Function set_trace_point_visu_lock(sim_trace_setting_att)
        # #     Dim iLocked (2)
        # #     sim_trace_setting_att.SetTracePointVisuLock iLocked
        # #     set_trace_point_visu_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SimTraceSettingAtt(name="{self.name}")'
