#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class MultiCADSettingAtt(SettingController):
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
                |                         MultiCADSettingAtt

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.multi_cad_setting_att = com_object

    @property
    def annotation_3d_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Annotation3DMode() As boolean
                | 
                |     Returns or sets the Annotation 3D mode R18sp3 on env. variable

        :rtype: bool
        """

        return self.multi_cad_setting_att.Annotation3DMode

    @annotation_3d_mode.setter
    def annotation_3d_mode(self, value: bool):
        """
        :param bool value:
        """

        self.multi_cad_setting_att.Annotation3DMode = value

    @property
    def conversion_technology(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConversionTechnology() As long
                | 
                |     Returns or sets the Conversion Technology

        :rtype: int
        """

        return self.multi_cad_setting_att.ConversionTechnology

    @conversion_technology.setter
    def conversion_technology(self, value: int):
        """
        :param int value:
        """

        self.multi_cad_setting_att.ConversionTechnology = value

    @property
    def link_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LinkMode() As long
                | 
                |     Returns or sets the Link Mode

        :rtype: int
        """

        return self.multi_cad_setting_att.LinkMode

    @link_mode.setter
    def link_mode(self, value: int):
        """
        :param int value:
        """

        self.multi_cad_setting_att.LinkMode = value

    @property
    def output_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OutputPath() As CATBSTR
                | 
                |     Returns or sets the Output Path

        :rtype: str
        """

        return self.multi_cad_setting_att.OutputPath

    @output_path.setter
    def output_path(self, value: str):
        """
        :param str value:
        """

        self.multi_cad_setting_att.OutputPath = value

    @property
    def parts_parameter_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PartsParameterMode() As long
                | 
                |     Returns or sets the parts parameterization mode

        :rtype: int
        """

        return self.multi_cad_setting_att.PartsParameterMode

    @parts_parameter_mode.setter
    def parts_parameter_mode(self, value: int):
        """
        :param int value:
        """

        self.multi_cad_setting_att.PartsParameterMode = value

    @property
    def pro_e_instance_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ProEInstanceMode() As boolean
                | 
                |     Returns or sets the ProEInstanceMode

        :rtype: bool
        """

        return self.multi_cad_setting_att.ProEInstanceMode

    @pro_e_instance_mode.setter
    def pro_e_instance_mode(self, value: bool):
        """
        :param bool value:
        """

        self.multi_cad_setting_att.ProEInstanceMode = value

    @property
    def pro_e_instance_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ProEInstanceName() As CATBSTR
                | 
                |     Returns or sets the ProEInstanceName

        :rtype: str
        """

        return self.multi_cad_setting_att.ProEInstanceName

    @pro_e_instance_name.setter
    def pro_e_instance_name(self, value: str):
        """
        :param str value:
        """

        self.multi_cad_setting_att.ProEInstanceName = value

    @property
    def pro_e_quilts_read(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ProEQuiltsRead() As boolean
                | 
                |     Returns or sets the ProEQuiltsRead

        :rtype: bool
        """

        return self.multi_cad_setting_att.ProEQuiltsRead

    @pro_e_quilts_read.setter
    def pro_e_quilts_read(self, value: bool):
        """
        :param bool value:
        """

        self.multi_cad_setting_att.ProEQuiltsRead = value

    @property
    def pro_e_simp_rep_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ProESimpRepMode() As boolean
                | 
                |     Returns or sets the ProESimpRepMode

        :rtype: bool
        """

        return self.multi_cad_setting_att.ProESimpRepMode

    @pro_e_simp_rep_mode.setter
    def pro_e_simp_rep_mode(self, value: bool):
        """
        :param bool value:
        """

        self.multi_cad_setting_att.ProESimpRepMode = value

    @property
    def pro_e_simp_rep_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ProESimpRepName() As CATBSTR
                | 
                |     Returns or sets the ProESimpRepName

        :rtype: str
        """

        return self.multi_cad_setting_att.ProESimpRepName

    @pro_e_simp_rep_name.setter
    def pro_e_simp_rep_name(self, value: str):
        """
        :param str value:
        """

        self.multi_cad_setting_att.ProESimpRepName = value

    @property
    def save_coorsys_in_cgr(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SaveCoorsysInCgr() As boolean
                | 
                |     Returns or sets the Save Coordinate Systems in CGR

        :rtype: bool
        """

        return self.multi_cad_setting_att.SaveCoorsysInCgr

    @save_coorsys_in_cgr.setter
    def save_coorsys_in_cgr(self, value: bool):
        """
        :param bool value:
        """

        self.multi_cad_setting_att.SaveCoorsysInCgr = value

    @property
    def translator_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TranslatorMode() As long
                | 
                |     Returns or sets the Translator mode

        :rtype: int
        """

        return self.multi_cad_setting_att.TranslatorMode

    @translator_mode.setter
    def translator_mode(self, value: int):
        """
        :param int value:
        """

        self.multi_cad_setting_att.TranslatorMode = value

    @property
    def ug_active_layers_only(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UGActiveLayersOnly() As boolean
                | 
                |     Returns or sets the UGActiveLayersOnly

        :rtype: bool
        """

        return self.multi_cad_setting_att.UGActiveLayersOnly

    @ug_active_layers_only.setter
    def ug_active_layers_only(self, value: bool):
        """
        :param bool value:
        """

        self.multi_cad_setting_att.UGActiveLayersOnly = value

    @property
    def ug_drawing_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UGDrawingName() As CATBSTR
                | 
                |     Returns or sets the UGDrawingName

        :rtype: str
        """

        return self.multi_cad_setting_att.UGDrawingName

    @ug_drawing_name.setter
    def ug_drawing_name(self, value: str):
        """
        :param str value:
        """

        self.multi_cad_setting_att.UGDrawingName = value

    @property
    def ug_layer_numbers(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UGLayerNumbers() As CATBSTR
                | 
                |     Returns or sets the UGLayerNumbers

        :rtype: str
        """

        return self.multi_cad_setting_att.UGLayerNumbers

    @ug_layer_numbers.setter
    def ug_layer_numbers(self, value: str):
        """
        :param str value:
        """

        self.multi_cad_setting_att.UGLayerNumbers = value

    @property
    def ug_open_surfaces(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UGOpenSurfaces() As boolean
                | 
                |     Returns or sets the UGOpenSurfaces

        :rtype: bool
        """

        return self.multi_cad_setting_att.UGOpenSurfaces

    @ug_open_surfaces.setter
    def ug_open_surfaces(self, value: bool):
        """
        :param bool value:
        """

        self.multi_cad_setting_att.UGOpenSurfaces = value

    @property
    def ug_reference_set(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UgReferenceSet() As CATBSTR
                | 
                |     Returns or sets the UgReferenceSet

        :rtype: str
        """

        return self.multi_cad_setting_att.UgReferenceSet

    @ug_reference_set.setter
    def ug_reference_set(self, value: str):
        """
        :param str value:
        """

        self.multi_cad_setting_att.UgReferenceSet = value

    @property
    def visu_format_unit(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property VisuFormatUnit() As float
                | 
                |     Returns or sets the Unit for Visu Format (number of milimeters per unit of
                |     the file)

        :rtype: float
        """

        return self.multi_cad_setting_att.VisuFormatUnit

    @visu_format_unit.setter
    def visu_format_unit(self, value: float):
        """
        :param float value:
        """

        self.multi_cad_setting_att.VisuFormatUnit = value

    def get_annotation_3d_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAnnotation3DModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Annotation3DMode
                |     parameter.
                |     Role:Retrieves the state of the Annotation3DMode parameter in the current
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
        return self.multi_cad_setting_att.GetAnnotation3DModeInfo(io_admin_level, io_locked)

    def get_conversion_technology_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetConversionTechnologyInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ConversionTechnology
                |     parameter.
                |     Role:Retrieves the state of the ConversionTechnology parameter in the
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
        return self.multi_cad_setting_att.GetConversionTechnologyInfo(io_admin_level, io_locked)

    def get_link_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLinkModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LinkMode
                |     parameter.
                |     Role:Retrieves the state of the LinkMode parameter in the current
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
        return self.multi_cad_setting_att.GetLinkModeInfo(io_admin_level, io_locked)

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
        return self.multi_cad_setting_att.GetOutputPathInfo(io_admin_level, io_locked)

    def get_parts_parameter_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPartsParameterModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PartsParameterMode
                |     parameter.
                |     Role:Retrieves the state of the PartsParameterMode parameter in the current
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
        return self.multi_cad_setting_att.GetPartsParameterModeInfo(io_admin_level, io_locked)

    def get_pro_e_instance_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProEInstanceModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ProEInstanceMode
                |     parameter.
                |     Role:Retrieves the state of the ProEInstanceMode parameter in the current
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
        return self.multi_cad_setting_att.GetProEInstanceModeInfo(io_admin_level, io_locked)

    def get_pro_e_instance_name_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProEInstanceNameInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ProEInstanceName
                |     parameter.
                |     Role:Retrieves the state of the ProEInstanceName parameter in the current
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
        return self.multi_cad_setting_att.GetProEInstanceNameInfo(io_admin_level, io_locked)

    def get_pro_e_quilts_read_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProEQuiltsReadInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ProEQuiltsRead
                |     parameter.
                |     Role:Retrieves the state of the ProEQuiltsRead parameter in the current
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
        return self.multi_cad_setting_att.GetProEQuiltsReadInfo(io_admin_level, io_locked)

    def get_pro_e_simp_rep_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProESimpRepModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ProESimpRepMode
                |     parameter.
                |     Role:Retrieves the state of the ProESimpRepMode parameter in the current
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
        return self.multi_cad_setting_att.GetProESimpRepModeInfo(io_admin_level, io_locked)

    def get_pro_e_simp_rep_name_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProESimpRepNameInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ProESimpRepName
                |     parameter.
                |     Role:Retrieves the state of the ProESimpRepName parameter in the current
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
        return self.multi_cad_setting_att.GetProESimpRepNameInfo(io_admin_level, io_locked)

    def get_save_coorsys_in_cgr_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSaveCoorsysInCgrInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SaveCoorsysInCgr
                |     parameter.
                |     Role:Retrieves the state of the SaveCoorsysInCgr parameter in the current
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
        return self.multi_cad_setting_att.GetSaveCoorsysInCgrInfo(io_admin_level, io_locked)

    def get_translator_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTranslatorModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Translator mode
                |     parameter.
                |     Role:Retrieves the state of the Translator mode parameter in the current
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
        return self.multi_cad_setting_att.GetTranslatorModeInfo(io_admin_level, io_locked)

    def get_ug_active_layers_only_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUGActiveLayersOnlyInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the UGActiveLayersOnly
                |     parameter.
                |     Role:Retrieves the state of the UGActiveLayersOnly parameter in the current
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
        return self.multi_cad_setting_att.GetUGActiveLayersOnlyInfo(io_admin_level, io_locked)

    def get_ug_drawing_name_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUGDrawingNameInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the UGDrawingName
                |     parameter.
                |     Role:Retrieves the state of the UGDrawingName parameter in the current
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
        return self.multi_cad_setting_att.GetUGDrawingNameInfo(io_admin_level, io_locked)

    def get_ug_layer_numbers_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUGLayerNumbersInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the UGLayerNumbers
                |     parameter.
                |     Role:Retrieves the state of the UGLayerNumbers parameter in the current
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
        return self.multi_cad_setting_att.GetUGLayerNumbersInfo(io_admin_level, io_locked)

    def get_ug_open_surfaces_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUGOpenSurfacesInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the UGOpenSurfaces
                |     parameter.
                |     Role:Retrieves the state of the UGOpenSurfaces parameter in the current
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
        return self.multi_cad_setting_att.GetUGOpenSurfacesInfo(io_admin_level, io_locked)

    def get_ug_reference_set_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUgReferenceSetInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the UgReferenceSet
                |     parameter.
                |     Role:Retrieves the state of the UgReferenceSet parameter in the current
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
        return self.multi_cad_setting_att.GetUgReferenceSetInfo(io_admin_level, io_locked)

    def get_visu_format_unit_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetVisuFormatUnitInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the VisuFormatUnit
                |     parameter.
                |     Role:Retrieves the state of the VisuFormatUnit parameter in the current
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
        return self.multi_cad_setting_att.GetVisuFormatUnitInfo(io_admin_level, io_locked)

    def set_annotation_3d_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAnnotation3DModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Annotation3DMode parameter.
                |     Role:Locks or unlocks the Annotation3DMode parameter if it is possible in
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
        return self.multi_cad_setting_att.SetAnnotation3DModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_annotation3_d_mode_lock'
        # # vba_code = """
        # # Public Function set_annotation3_d_mode_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetAnnotation3DModeLock iLocked
        # #     set_annotation3_d_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_conversion_technology_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetConversionTechnologyLock(boolean iLocked)
                | 
                |     Locks or unlocks the ConversionTechnology parameter.
                |     Role:Locks or unlocks the ConversionTechnology parameter if it is possible
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
        return self.multi_cad_setting_att.SetConversionTechnologyLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_conversion_technology_lock'
        # # vba_code = """
        # # Public Function set_conversion_technology_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetConversionTechnologyLock iLocked
        # #     set_conversion_technology_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_link_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLinkModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the LinkMode parameter.
                |     Role:Locks or unlocks the LinkMode parameter if it is possible in the
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
        return self.multi_cad_setting_att.SetLinkModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_link_mode_lock'
        # # vba_code = """
        # # Public Function set_link_mode_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetLinkModeLock iLocked
        # #     set_link_mode_lock = iLocked
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
        return self.multi_cad_setting_att.SetOutputPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_output_path_lock'
        # # vba_code = """
        # # Public Function set_output_path_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetOutputPathLock iLocked
        # #     set_output_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_parts_parameter_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPartsParameterModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the PartsParameterMode parameter.
                |     Role:Locks or unlocks the PartsParameterMode parameter if it is possible in
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
        return self.multi_cad_setting_att.SetPartsParameterModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_parts_parameter_mode_lock'
        # # vba_code = """
        # # Public Function set_parts_parameter_mode_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetPartsParameterModeLock iLocked
        # #     set_parts_parameter_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pro_e_instance_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProEInstanceModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ProEInstanceMode parameter.
                |     Role:Locks or unlocks the ProEInstanceMode parameter if it is possible in
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
        return self.multi_cad_setting_att.SetProEInstanceModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pro_e_instance_mode_lock'
        # # vba_code = """
        # # Public Function set_pro_e_instance_mode_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetProEInstanceModeLock iLocked
        # #     set_pro_e_instance_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pro_e_instance_name_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProEInstanceNameLock(boolean iLocked)
                | 
                |     Locks or unlocks the ProEInstanceName parameter.
                |     Role:Locks or unlocks the ProEInstanceName parameter if it is possible in
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
        return self.multi_cad_setting_att.SetProEInstanceNameLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pro_e_instance_name_lock'
        # # vba_code = """
        # # Public Function set_pro_e_instance_name_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetProEInstanceNameLock iLocked
        # #     set_pro_e_instance_name_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pro_e_quilts_read_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProEQuiltsReadLock(boolean iLocked)
                | 
                |     Locks or unlocks the ProEQuiltsRead parameter.
                |     Role:Locks or unlocks the ProEQuiltsRead parameter if it is possible in the
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
        return self.multi_cad_setting_att.SetProEQuiltsReadLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pro_e_quilts_read_lock'
        # # vba_code = """
        # # Public Function set_pro_e_quilts_read_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetProEQuiltsReadLock iLocked
        # #     set_pro_e_quilts_read_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pro_e_simp_rep_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProESimpRepModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ProESimpRepMode parameter.
                |     Role:Locks or unlocks the ProESimpRepMode parameter if it is possible in
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
        return self.multi_cad_setting_att.SetProESimpRepModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pro_e_simp_rep_mode_lock'
        # # vba_code = """
        # # Public Function set_pro_e_simp_rep_mode_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetProESimpRepModeLock iLocked
        # #     set_pro_e_simp_rep_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pro_e_simp_rep_name_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProESimpRepNameLock(boolean iLocked)
                | 
                |     Locks or unlocks the ProESimpRepName parameter.
                |     Role:Locks or unlocks the ProESimpRepName parameter if it is possible in
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
        return self.multi_cad_setting_att.SetProESimpRepNameLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pro_e_simp_rep_name_lock'
        # # vba_code = """
        # # Public Function set_pro_e_simp_rep_name_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetProESimpRepNameLock iLocked
        # #     set_pro_e_simp_rep_name_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_save_coorsys_in_cgr_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSaveCoorsysInCgrLock(boolean iLocked)
                | 
                |     Locks or unlocks the SaveCoorsysInCgr parameter.
                |     Role:Locks or unlocks the SaveCoorsysInCgr parameter if it is possible in
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
        return self.multi_cad_setting_att.SetSaveCoorsysInCgrLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_save_coorsys_in_cgr_lock'
        # # vba_code = """
        # # Public Function set_save_coorsys_in_cgr_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetSaveCoorsysInCgrLock iLocked
        # #     set_save_coorsys_in_cgr_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_translator_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTranslatorModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Translator mode parameter.
                |     Role:Locks or unlocks the Translator mode parameter if it is possible in
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
        return self.multi_cad_setting_att.SetTranslatorModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_translator_mode_lock'
        # # vba_code = """
        # # Public Function set_translator_mode_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetTranslatorModeLock iLocked
        # #     set_translator_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ug_active_layers_only_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUGActiveLayersOnlyLock(boolean iLocked)
                | 
                |     Locks or unlocks the UGActiveLayersOnly parameter.
                |     Role:Locks or unlocks the UGActiveLayersOnly parameter if it is possible in
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
        return self.multi_cad_setting_att.SetUGActiveLayersOnlyLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ug_active_layers_only_lock'
        # # vba_code = """
        # # Public Function set_ug_active_layers_only_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetUGActiveLayersOnlyLock iLocked
        # #     set_ug_active_layers_only_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ug_drawing_name_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUGDrawingNameLock(boolean iLocked)
                | 
                |     Locks or unlocks the UGDrawingName parameter.
                |     Role:Locks or unlocks the UGDrawingName parameter if it is possible in the
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
        return self.multi_cad_setting_att.SetUGDrawingNameLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ug_drawing_name_lock'
        # # vba_code = """
        # # Public Function set_ug_drawing_name_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetUGDrawingNameLock iLocked
        # #     set_ug_drawing_name_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ug_layer_numbers_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUGLayerNumbersLock(boolean iLocked)
                | 
                |     Locks or unlocks the UGLayerNumbers parameter.
                |     Role:Locks or unlocks the UGLayerNumbers parameter if it is possible in the
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
        return self.multi_cad_setting_att.SetUGLayerNumbersLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ug_layer_numbers_lock'
        # # vba_code = """
        # # Public Function set_ug_layer_numbers_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetUGLayerNumbersLock iLocked
        # #     set_ug_layer_numbers_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ug_open_surfaces_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUGOpenSurfacesLock(boolean iLocked)
                | 
                |     Locks or unlocks the UGOpenSurfaces parameter.
                |     Role:Locks or unlocks the UGOpenSurfaces parameter if it is possible in the
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
        return self.multi_cad_setting_att.SetUGOpenSurfacesLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ug_open_surfaces_lock'
        # # vba_code = """
        # # Public Function set_ug_open_surfaces_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetUGOpenSurfacesLock iLocked
        # #     set_ug_open_surfaces_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ug_reference_set_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUgReferenceSetLock(boolean iLocked)
                | 
                |     Locks or unlocks the UgReferenceSet parameter.
                |     Role:Locks or unlocks the UgReferenceSet parameter if it is possible in the
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
        return self.multi_cad_setting_att.SetUgReferenceSetLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ug_reference_set_lock'
        # # vba_code = """
        # # Public Function set_ug_reference_set_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetUgReferenceSetLock iLocked
        # #     set_ug_reference_set_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_visu_format_unit_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetVisuFormatUnitLock(boolean iLocked)
                | 
                |     Locks or unlocks the VisuFormatUnit parameter.
                |     Role:Locks or unlocks the VisuFormatUnit parameter if it is possible in the
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
        return self.multi_cad_setting_att.SetVisuFormatUnitLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_visu_format_unit_lock'
        # # vba_code = """
        # # Public Function set_visu_format_unit_lock(multi_cad_setting_att)
        # #     Dim iLocked (2)
        # #     multi_cad_setting_att.SetVisuFormatUnitLock iLocked
        # #     set_visu_format_unit_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MultiCADSettingAtt(name="{self.name}")'
