#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController
from pycatia.system_interfaces.system_service import SystemService


class MeasureSettingAtt(SettingController):
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
                |                         MeasureSettingAtt
                | 
                | The interface to access a CATIAMeasureSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.measure_setting_att = com_object

    @property
    def box_display(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BoxDisplay() As boolean
                | 
                |     Returns or sets the BoxDisplay parameter .
                | 
                |     Measure label background is filled if BoxDisplay is True ; there are only
                |     borders if BoxDisplay is False.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.measure_setting_att.BoxDisplay

    @box_display.setter
    def box_display(self, value: bool):
        """
        :param bool value:
        """

        self.measure_setting_att.BoxDisplay = value

    @property
    def line_width(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LineWidth() As short
                | 
                |     Returns or sets the LineWidth parameter.
                | 
                |     The line width index, which ranges from 1 to 63.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.measure_setting_att.LineWidth

    @line_width.setter
    def line_width(self, value: int):
        """
        :param int value:
        """

        self.measure_setting_att.LineWidth = value

    @property
    def part_update_status(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PartUpdateStatus() As boolean
                | 
                |     Returns or sets the PartUpdateStatus parameter .
                | 
                |     Part is automatically updated if PartUpdateStatus is true.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.measure_setting_att.PartUpdateStatus

    @part_update_status.setter
    def part_update_status(self, value: bool):
        """
        :param bool value:
        """

        self.measure_setting_att.PartUpdateStatus = value

    @property
    def product_update_status(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ProductUpdateStatus() As boolean
                | 
                |     Returns or sets the ProductUpdateStatus parameter .
                | 
                |     Product is automatically updated if PartUpdateStatus is
                |     true.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.measure_setting_att.ProductUpdateStatus

    @product_update_status.setter
    def product_update_status(self, value: bool):
        """
        :param bool value:
        """

        self.measure_setting_att.ProductUpdateStatus = value

    @property
    def tilde_display(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TildeDisplay() As boolean
                | 
                |     Returns or sets the TildeDisplay parameter.
                | 
                |     If TildeDisplay is TRUE, a tilde displayed for approximate
                |     measurement.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.measure_setting_att.TildeDisplay

    @tilde_display.setter
    def tilde_display(self, value: bool):
        """
        :param bool value:
        """

        self.measure_setting_att.TildeDisplay = value

    def get_box_display_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBoxDisplayInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the BoxDisplay
                |     parameter.
                |     Role:Retrieves the state of the BoxDisplay parameter in the current
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
        return self.measure_setting_att.GetBoxDisplayInfo(io_admin_level, io_locked)

    def get_label_color(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetLabelColor(long oR,
                | long oG,
                | long oB)
                | 
                |     Returns the LabelColor parameter.
                | 
                |     Parameters:
                | 
                |         oR
                |             the red component of the color. 
                |         oG
                |             the green component of the color. 
                |         oB
                |             the blue component of the color.
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :rtype: tuple
        """
        return self.measure_setting_att.GetLabelColor()

    def get_label_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLabelColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LabelColor
                |     parameter.
                |     Role:Retrieves the state of the LabelColor parameter in the current
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
        return self.measure_setting_att.GetLabelColorInfo(io_admin_level, io_locked)

    def get_line_width_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLineWidthInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LineWidth
                |     parameter.
                |     Role:Retrieves the state of the LineWidth parameter in the current
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
        return self.measure_setting_att.GetLineWidthInfo(io_admin_level, io_locked)

    def get_part_update_status_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPartUpdateStatusInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PartUpdateStatus
                |     parameter.
                |     Role:Retrieves the state of the PartUpdateStatus parameter in the current
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
        return self.measure_setting_att.GetPartUpdateStatusInfo(io_admin_level, io_locked)

    def get_product_update_status_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetProductUpdateStatusInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ProductUpdateStatus
                |     parameter.
                |     Role:Retrieves the state of the ProductUpdateStatus parameter in the
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
        return self.measure_setting_att.GetProductUpdateStatusInfo(io_admin_level, io_locked)

    def get_text_color(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetTextColor(long oR,
                | long oG,
                | long oB)
                | 
                |     Returns the TextColor parameter .
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: tuple
        """

        vba_function_name = 'get_text_color'
        vba_code = """
        Public Function get_text_color(measurable)
            Dim oR long
            Dim oG long
            Dim oB long
            inertia.GetTextColor oR oG oB
            get_principal_moments = (oR, oG, oB)
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_text_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetTextColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TextColor
                |     parameter.
                |     Role:Retrieves the state of the TextColor parameter in the current
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
        return self.measure_setting_att.GetTextColorInfo(io_admin_level, io_locked)

    def get_tilde_display_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetTildeDisplayInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TildeDisplay
                |     parameter.
                |     Role:Retrieves the state of the TildeDisplay parameter in the current
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
        return self.measure_setting_att.GetTildeDisplayInfo(io_admin_level, io_locked)

    def set_box_display_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBoxDisplayLock(boolean iLocked)
                | 
                |     Locks or unlocks the BoxDisplay parameter.
                |     Role:Locks or unlocks the BoxDisplay parameter if it is possible in the
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
        return self.measure_setting_att.SetBoxDisplayLock(i_locked)

    def set_label_color(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLabelColor(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the LabelColor parameter.
                | 
                |     Parameters:
                | 
                |         oR
                |             the red component of the color. 
                |         oG
                |             the green component of the color. 
                |         oB
                |             the blue component of the color.
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.measure_setting_att.SetLabelColor(i_r, i_g, i_b)

    def set_label_color_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLabelColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the LabelColor parameter.
                |     Role:Locks or unlocks the LabelColor parameter if it is possible in the
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
        return self.measure_setting_att.SetLabelColorLock(i_locked)

    def set_line_width_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLineWidthLock(boolean iLocked)
                | 
                |     Locks or unlocks the LineWidth parameter.
                |     Role:Locks or unlocks the LineWidth parameter if it is possible in the
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
        return self.measure_setting_att.SetLineWidthLock(i_locked)

    def set_part_update_status_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPartUpdateStatusLock(boolean iLocked)
                | 
                |     Locks or unlocks the PartUpdateStatus parameter.
                |     Role:Locks or unlocks the PartUpdateStatus parameter if it is possible in
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
        return self.measure_setting_att.SetPartUpdateStatusLock(i_locked)

    def set_product_update_status_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetProductUpdateStatusLock(boolean iLocked)
                | 
                |     Locks or unlocks the ProductUpdateStatus parameter.
                |     Role:Locks or unlocks the Xxx parameter if it is possible in the current
                |     administrative context. In user mode this method will always return
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
        return self.measure_setting_att.SetProductUpdateStatusLock(i_locked)

    def set_text_color(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTextColor(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the TextColor parameter .
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.measure_setting_att.SetTextColor(i_r, i_g, i_b)

    def set_text_color_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTextColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the TextColor parameter.
                |     Role:Locks or unlocks the TextColor parameter if it is possible in the
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
        return self.measure_setting_att.SetTextColorLock(i_locked)

    def set_tilde_display_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTildeDisplayLock(boolean iLocked)
                | 
                |     Locks or unlocks the TildeDisplay parameter.
                |     Role:Locks or unlocks the TildeDisplay parameter if it is possible in the
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
        return self.measure_setting_att.SetTildeDisplayLock(i_locked)

    def __repr__(self):
        return f'MeasureSettingAtt(name="{self.name}")'
