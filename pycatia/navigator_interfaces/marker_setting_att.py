#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class MarkerSettingAtt(SettingController):
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
                |                         MarkerSettingAtt
                | 
                | Interface to handle the Marker settings
                | 
                | The different settings are:
                | 
                | MarkerAutoUpdate
                | Update on product structure modifications and scenes
                | activation.
                | 
                | 
                | MarkerDefaultsColor
                | 
                | 
                | MarkerDefaultsWeight
                | 
                | 
                | MarkerDefaultsDashed
                | 
                | 
                | Marker2DAutoNaming
                | 
                | 
                | Marker3DAutoNaming
                | 
                | 
                | MarkerTextColor2D
                | 
                | 
                | MarkerTextWeight2D
                | 
                | 
                | MarkerTextDashed2D
                | 
                | 
                | MarkerTextDefaultsFont2D
                | 
                | 
                | MarkerTextDefaultsSize2D
                | 
                | 
                | MarkerTextColor3D
                | 
                | 
                | MarkerTextWeight3D
                | 
                | 
                | MarkerTextDashed3D
                | 
                | 
                | MarkerTextDefaultsFont3D
                | 
                | 
                | MarkerTextDefaultsSize3D

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.marker_setting_att = com_object

    @property
    def marker_2d_auto_naming(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Marker2DAutoNaming() As boolean
                | 
                |     Returns or sets the activation state for 2D annotations automatic naming
                |     (TRUE naming is automatic, FALSE the naming is not automatic).

        :rtype: bool
        """

        return self.marker_setting_att.Marker2DAutoNaming

    @marker_2d_auto_naming.setter
    def marker_2d_auto_naming(self, value: bool):
        """
        :param bool value:
        """

        self.marker_setting_att.Marker2DAutoNaming = value

    @property
    def marker_3d_auto_naming(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Marker3DAutoNaming() As boolean
                | 
                |     Returns or sets the activation state for 3D annotations automatic naming
                |     (TRUE naming is automatic, FALSE the naming is not automatic).

        :rtype: bool
        """

        return self.marker_setting_att.Marker3DAutoNaming

    @marker_3d_auto_naming.setter
    def marker_3d_auto_naming(self, value: bool):
        """
        :param bool value:
        """

        self.marker_setting_att.Marker3DAutoNaming = value

    @property
    def marker_defaults_dashed(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerDefaultsDashed() As long
                | 
                |     Returns or sets the default dashed value of an annotation (oValue the
                |     dashed value).

        :rtype: int
        """

        return self.marker_setting_att.MarkerDefaultsDashed

    @marker_defaults_dashed.setter
    def marker_defaults_dashed(self, value: int):
        """
        :param int value:
        """

        self.marker_setting_att.MarkerDefaultsDashed = value

    @property
    def marker_defaults_weight(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerDefaultsWeight() As long
                | 
                |     Returns or sets the default weight value of an annotation (oValue the
                |     weight value).

        :rtype: int
        """

        return self.marker_setting_att.MarkerDefaultsWeight

    @marker_defaults_weight.setter
    def marker_defaults_weight(self, value: int):
        """
        :param int value:
        """

        self.marker_setting_att.MarkerDefaultsWeight = value

    @property
    def marker_text_dashed_2d(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerTextDashed2D() As long
                | 
                |     Returns or sets the default dashed value of a 2D text annotation (oValue
                |     the dashed value).

        :rtype: int
        """

        return self.marker_setting_att.MarkerTextDashed2D

    @marker_text_dashed_2d.setter
    def marker_text_dashed_2d(self, value: int):
        """
        :param int value:
        """

        self.marker_setting_att.MarkerTextDashed2D = value

    @property
    def marker_text_dashed_3d(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerTextDashed3D() As long
                | 
                |     Returns or sets the default dashed value of a 3D text annotation (oValue
                |     the dashed value).

        :rtype: int
        """

        return self.marker_setting_att.MarkerTextDashed3D

    @marker_text_dashed_3d.setter
    def marker_text_dashed_3d(self, value: int):
        """
        :param int value:
        """

        self.marker_setting_att.MarkerTextDashed3D = value

    @property
    def marker_text_defaults_font_2d(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerTextDefaultsFont2D() As CATBSTR
                | 
                |     Returns or sets the default font of a 2D annotation (oValue the font name).

        :rtype: str
        """

        return self.marker_setting_att.MarkerTextDefaultsFont2D

    @marker_text_defaults_font_2d.setter
    def marker_text_defaults_font_2d(self, value: str):
        """
        :param str value:
        """

        self.marker_setting_att.MarkerTextDefaultsFont2D = value

    @property
    def marker_text_defaults_font_3d(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerTextDefaultsFont3D(CATBSTR iValue)
                | 
                |     Returns or sets the default font of a 3D annotation (oValue the font name).

        :rtype: str
        """

        return self.marker_setting_att.MarkerTextDefaultsFont3D

    @marker_text_defaults_font_3d.setter
    def marker_text_defaults_font_3d(self, value: str):
        """
        :param str value:
        """

        self.marker_setting_att.MarkerTextDefaultsFont3D = value

    @property
    def marker_text_defaults_size_2d(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerTextDefaultsSize2D() As long
                | 
                |     Returns or sets the default size value of a 2d annotation (oValue the size
                |     value)..

        :rtype: int
        """

        return self.marker_setting_att.MarkerTextDefaultsSize2D

    @marker_text_defaults_size_2d.setter
    def marker_text_defaults_size_2d(self, value: int):
        """
        :param int value:
        """

        self.marker_setting_att.MarkerTextDefaultsSize2D = value

    @property
    def marker_text_defaults_size_3d(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerTextDefaultsSize3D(long iValue)
                | 
                |     Returns or sets the default size value of a 3d annotation (oValue the size
                |     value)..

        :rtype: int
        """

        return self.marker_setting_att.MarkerTextDefaultsSize3D

    @marker_text_defaults_size_3d.setter
    def marker_text_defaults_size_3d(self, value: int):
        """
        :param int value:
        """

        self.marker_setting_att.MarkerTextDefaultsSize3D = value

    @property
    def marker_text_weight_2d(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerTextWeight2D() As long
                | 
                |     Returns or sets the default weight value of a 2D text annotation (oValue
                |     the weight value).

        :rtype: int
        """

        return self.marker_setting_att.MarkerTextWeight2D

    @marker_text_weight_2d.setter
    def marker_text_weight_2d(self, value: int):
        """
        :param int value:
        """

        self.marker_setting_att.MarkerTextWeight2D = value

    @property
    def marker_text_weight_3d(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerTextWeight3D(long iValue)
                | 
                |     Returns or sets the default weight value of a 3D text annotation (oValue
                |     the weight value).

        :rtype: int
        """

        return self.marker_setting_att.MarkerTextWeight3D

    @marker_text_weight_3d.setter
    def marker_text_weight_3d(self, value: int):
        """
        :param int value:
        """

        self.marker_setting_att.MarkerTextWeight3D = value

    def get_marker_2d_auto_naming_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarker2DAutoNamingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Marker2DAutoNaming
                |     parameter.
                |     Role:Retrieves the state of the Marker2DAutoNaming parameter in the current
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
        return self.marker_setting_att.GetMarker2DAutoNamingInfo(io_admin_level, io_locked)

    def get_marker_3d_auto_naming_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarker3DAutoNamingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Marker3DAutoNaming
                |     parameter.
                |     Role:Retrieves the state of the Marker3DAutoNaming parameter in the current
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
        return self.marker_setting_att.GetMarker3DAutoNamingInfo(io_admin_level, io_locked)

    def get_marker_defaults_color(self, o_red: int, o_green: int, o_blue: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetMarkerDefaultsColor(long oRed,
                | long oGreen,
                | long oBlue)
                | 
                |     Returns the default color of an annotation (oRed, oGreen, oBlue: RGB values
                |     of the color).

        :param int o_red:
        :param int o_green:
        :param int o_blue:
        :rtype: None
        """
        return self.marker_setting_att.GetMarkerDefaultsColor(o_red, o_green, o_blue)

    def get_marker_defaults_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerDefaultsColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerDefaultsColor
                |     parameter.
                |     Role:Retrieves the state of the MarkerDefaultsColor parameter in the
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
        return self.marker_setting_att.GetMarkerDefaultsColorInfo(io_admin_level, io_locked)

    def get_marker_defaults_dashed_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerDefaultsDashedInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerDefaultsDashed
                |     parameter.
                |     Role:Retrieves the state of the MarkerDefaultsDashed parameter in the
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
        return self.marker_setting_att.GetMarkerDefaultsDashedInfo(io_admin_level, io_locked)

    def get_marker_defaults_weight_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerDefaultsWeightInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerDefaultsWeight
                |     parameter.
                |     Role:Retrieves the state of the MarkerDefaultsWeight parameter in the
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
        return self.marker_setting_att.GetMarkerDefaultsWeightInfo(io_admin_level, io_locked)

    def get_marker_text_color_2d(self, o_red: int, o_green: int, o_blue: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetMarkerTextColor2D(long oRed,
                | long oGreen,
                | long oBlue)
                | 
                |     Returns the default color of a 2D text annotation (oRed, oGreen, oBlue: RGB
                |     values of the color).

        :param int o_red:
        :param int o_green:
        :param int o_blue:
        :rtype: None
        """
        return self.marker_setting_att.GetMarkerTextColor2D(o_red, o_green, o_blue)

    def get_marker_text_color_2d_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerTextColor2DInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerTextColor2D
                |     parameter.
                |     Role:Retrieves the state of the MarkerTextColor2D parameter in the current
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
        return self.marker_setting_att.GetMarkerTextColor2DInfo(io_admin_level, io_locked)

    def get_marker_text_color_3d(self, o_red: int, o_green: int, o_blue: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetMarkerTextColor3D(long oRed,
                | long oGreen,
                | long oBlue)
                | 
                |     Returns the default color of a 3D text annotation (oRed, oGreen, oBlue: RGB
                |     values of the color).

        :param int o_red:
        :param int o_green:
        :param int o_blue:
        :rtype: None
        """
        return self.marker_setting_att.GetMarkerTextColor3D(o_red, o_green, o_blue)

    def get_marker_text_color_3d_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerTextColor3DInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerTextColor3D
                |     parameter.
                |     Role:Retrieves the state of the MarkerTextColor3D parameter in the current
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
        return self.marker_setting_att.GetMarkerTextColor3DInfo(io_admin_level, io_locked)

    def get_marker_text_dashed_2d_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerTextDashed2DInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerTextDashed2D
                |     parameter.
                |     Role:Retrieves the state of the MarkerTextDashed2D parameter in the current
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
        return self.marker_setting_att.GetMarkerTextDashed2DInfo(io_admin_level, io_locked)

    def get_marker_text_dashed_3d_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerTextDashed3DInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerTextDashed3D
                |     parameter.
                |     Role:Retrieves the state of the MarkerTextDashed3D parameter in the current
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
        return self.marker_setting_att.GetMarkerTextDashed3DInfo(io_admin_level, io_locked)

    def get_marker_text_defaults_font_2d_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerTextDefaultsFont2DInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerDefaultsFont2D
                |     parameter.
                |     Role:Retrieves the state of the MarkerDefaultsFont2D parameter in the
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
        return self.marker_setting_att.GetMarkerTextDefaultsFont2DInfo(io_admin_level, io_locked)

    def get_marker_text_defaults_font_3d_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerTextDefaultsFont3DInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerDefaultsFont3D
                |     parameter.
                |     Role:Retrieves the state of the MarkerDefaultsFont3D parameter in the
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
        return self.marker_setting_att.GetMarkerTextDefaultsFont3DInfo(io_admin_level, io_locked)

    def get_marker_text_defaults_size_2d_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerTextDefaultsSize2DInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerDefaultsSize2D
                |     parameter.
                |     Role:Retrieves the state of the MarkerDefaultsSize2D parameter in the
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
        return self.marker_setting_att.GetMarkerTextDefaultsSize2DInfo(io_admin_level, io_locked)

    def get_marker_text_defaults_size_3d_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerTextDefaultsSize3DInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerDefaultsSize3D
                |     parameter.
                |     Role:Retrieves the state of the MarkerDefaultsSize3D parameter in the
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
        return self.marker_setting_att.GetMarkerTextDefaultsSize3DInfo(io_admin_level, io_locked)

    def get_marker_text_weight_2d_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerTextWeight2DInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerTextWeight2D
                |     parameter.
                |     Role:Retrieves the state of the MarkerTextWeight2D parameter in the current
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
        return self.marker_setting_att.GetMarkerTextWeight2DInfo(io_admin_level, io_locked)

    def get_marker_text_weight_3d_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerTextWeight3DInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerTextWeight3D
                |     parameter.
                |     Role:Retrieves the state of the MarkerTextWeight3D parameter in the current
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
        return self.marker_setting_att.GetMarkerTextWeight3DInfo(io_admin_level, io_locked)

    def set_marker_2d_auto_naming_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarker2DAutoNamingLock(boolean iLocked)
                | 
                |     Locks or unlocks the Marker2DAutoNaming parameter.
                |     Role:Locks or unlocks the Marker2DAutoNaming parameter if it is possible in
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
        return self.marker_setting_att.SetMarker2DAutoNamingLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_2d_auto_naming_lock'
        # # vba_code = """
        # # Public Function set_marker_2d_auto_naming_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarker2DAutoNamingLock iLocked
        # #     set_marker_2d_auto_naming_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_3d_auto_naming_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarker3DAutoNamingLock(boolean iLocked)
                | 
                |     Locks or unlocks the Marker3DAutoNaming parameter.
                |     Role:Locks or unlocks the Marker3DAutoNaming parameter if it is possible in
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
        return self.marker_setting_att.SetMarker3DAutoNamingLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_3d_auto_naming_lock'
        # # vba_code = """
        # # Public Function set_marker_3d_auto_naming_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarker3DAutoNamingLock iLocked
        # #     set_marker_3d_auto_naming_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_defaults_color(self, i_red: int, i_green: int, i_blue: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerDefaultsColor(long iRed,
                | long iGreen,
                | long iBlue)
                | 
                |     Sets the default color of an annotation (iRed, iGreen, iBlue: RGB values
                |     for the desired color)

        :param int i_red:
        :param int i_green:
        :param int i_blue:
        :rtype: None
        """
        return self.marker_setting_att.SetMarkerDefaultsColor(i_red, i_green, i_blue)

    def set_marker_defaults_color_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerDefaultsColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerDefaultsColor parameter.
                |     Role:Locks or unlocks the MarkerDefaultsColor parameter if it is possible
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
        return self.marker_setting_att.SetMarkerDefaultsColorLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_defaults_color_lock'
        # # vba_code = """
        # # Public Function set_marker_defaults_color_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarkerDefaultsColorLock iLocked
        # #     set_marker_defaults_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_defaults_dashed_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerDefaultsDashedLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerDefaultsDashed parameter.
                |     Role:Locks or unlocks the MarkerDefaultsDashed parameter if it is possible
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
        return self.marker_setting_att.SetMarkerDefaultsDashedLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_defaults_dashed_lock'
        # # vba_code = """
        # # Public Function set_marker_defaults_dashed_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarkerDefaultsDashedLock iLocked
        # #     set_marker_defaults_dashed_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_defaults_weight_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerDefaultsWeightLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerDefaultsWeight parameter.
                |     Role:Locks or unlocks the MarkerDefaultsColor parameter if it is possible
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
        return self.marker_setting_att.SetMarkerDefaultsWeightLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_defaults_weight_lock'
        # # vba_code = """
        # # Public Function set_marker_defaults_weight_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarkerDefaultsWeightLock iLocked
        # #     set_marker_defaults_weight_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_text_color_2d(self, i_red: int, i_green: int, i_blue: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextColor2D(long iRed,
                | long iGreen,
                | long iBlue)
                | 
                |     Sets the default color of a 2D text annotation (iRed, iGreen, iBlue: RGB
                |     values for the desired color).

        :param int i_red:
        :param int i_green:
        :param int i_blue:
        :rtype: None
        """
        return self.marker_setting_att.SetMarkerTextColor2D(i_red, i_green, i_blue)

    def set_marker_text_color_2d_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextColor2DLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerTextColor2D parameter.
                |     Role:Locks or unlocks the MarkerTextColor2D parameter if it is possible in
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
        return self.marker_setting_att.SetMarkerTextColor2DLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_text_color_2d_lock'
        # # vba_code = """
        # # Public Function set_marker_text_color_2d_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarkerTextColor2DLock iLocked
        # #     set_marker_text_color_2d_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_text_color_3d(self, i_red: int, i_green: int, i_blue: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextColor3D(long iRed,
                | long iGreen,
                | long iBlue)
                | 
                |     Sets the default color of a 3D text annotation (iRed, iGreen, iBlue: RGB
                |     values for the desired color).

        :param int i_red:
        :param int i_green:
        :param int i_blue:
        :rtype: None
        """
        return self.marker_setting_att.SetMarkerTextColor3D(i_red, i_green, i_blue)

    def set_marker_text_color_3d_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextColor3DLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerTextColor3D parameter.
                |     Role:Locks or unlocks the MarkerTextColor3D parameter if it is possible in
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
        return self.marker_setting_att.SetMarkerTextColor3DLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_text_color_3d_lock'
        # # vba_code = """
        # # Public Function set_marker_text_color_3d_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarkerTextColor3DLock iLocked
        # #     set_marker_text_color_3d_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_text_dashed_2d_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextDashed2DLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerTextDashed parameter.
                |     Role:Locks or unlocks the MarkerTextDashed2D parameter if it is possible in
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
        return self.marker_setting_att.SetMarkerTextDashed2DLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_text_dashed_2d_lock'
        # # vba_code = """
        # # Public Function set_marker_text_dashed_2d_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarkerTextDashed2DLock iLocked
        # #     set_marker_text_dashed_2d_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_text_dashed_3d_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextDashed3DLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerTextDashed3D parameter.
                |     Role:Locks or unlocks the MarkerTextDashed3D parameter if it is possible in
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
        return self.marker_setting_att.SetMarkerTextDashed3DLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_text_dashed_3d_lock'
        # # vba_code = """
        # # Public Function set_marker_text_dashed_3d_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarkerTextDashed3DLock iLocked
        # #     set_marker_text_dashed_3d_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_text_defaults_font_2d_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextDefaultsFont2DLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerDefaultsFont2D parameter.
                |     Role:Locks or unlocks the MarkerDefaultsFont2D parameter if it is possible
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
        return self.marker_setting_att.SetMarkerTextDefaultsFont2DLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_text_defaults_font_2d_lock'
        # # vba_code = """
        # # Public Function set_marker_text_defaults_font_2d_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarkerTextDefaultsFont2DLock iLocked
        # #     set_marker_text_defaults_font_2d_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_text_defaults_font_3d_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextDefaultsFont3DLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerDefaultsFont3D parameter.
                |     Role:Locks or unlocks the MarkerDefaultsSize3D parameter if it is possible
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
        return self.marker_setting_att.SetMarkerTextDefaultsFont3DLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_text_defaults_font_3d_lock'
        # # vba_code = """
        # # Public Function set_marker_text_defaults_font_3d_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarkerTextDefaultsFont3DLock iLocked
        # #     set_marker_text_defaults_font_3d_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_text_defaults_size_2d_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextDefaultsSize2DLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerDefaultsSize2D parameter.
                |     Role:Locks or unlocks the MarkerDefaultsSize3D parameter if it is possible
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
        return self.marker_setting_att.SetMarkerTextDefaultsSize2DLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_text_defaults_size_2d_lock'
        # # vba_code = """
        # # Public Function set_marker_text_defaults_size_2d_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarkerTextDefaultsSize2DLock iLocked
        # #     set_marker_text_defaults_size_2d_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_text_defaults_size_3d_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextDefaultsSize3DLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerDefaultsSize3D parameter.
                |     Role:Locks or unlocks the MarkerDefaultsSize3D parameter if it is possible
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
        return self.marker_setting_att.SetMarkerTextDefaultsSize3DLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_text_defaults_size_3d_lock'
        # # vba_code = """
        # # Public Function set_marker_text_defaults_size_3d_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarkerTextDefaultsSize3DLock iLocked
        # #     set_marker_text_defaults_size_3d_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_text_weight_2d_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextWeight2DLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerTextWeight2D parameter.
                |     Role:Locks or unlocks the MarkerTextWeight2D parameter if it is possible in
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
        return self.marker_setting_att.SetMarkerTextWeight2DLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_text_weight_2d_lock'
        # # vba_code = """
        # # Public Function set_marker_text_weight_2d_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarkerTextWeight2DLock iLocked
        # #     set_marker_text_weight_2d_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_text_weight_3d_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextWeight3DLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerTextWeight3D parameter.
                |     Role:Locks or unlocks the MarkerTextWeight3D parameter if it is possible in
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
        return self.marker_setting_att.SetMarkerTextWeight3DLock(i_locked)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_text_weight_3d_lock'
        # # vba_code = """
        # # Public Function set_marker_text_weight_3d_lock(marker_setting_att)
        # #     Dim iLocked (2)
        # #     marker_setting_att.SetMarkerTextWeight3DLock iLocked
        # #     set_marker_text_weight_3d_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MarkerSettingAtt(name="{self.name}")'
