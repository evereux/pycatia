#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class VrmlSettingAtt(SettingController):
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
                |                         VrmlSettingAtt
                | 
                | The interface to access a CATIAVrmlSettingAtt.
                | This interface may be used to read or modify in the
                | CATIA\\Tools\\Option\\General\\Compatibility.... the settings values of the VRML
                | sheet.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.vrml_setting_att = com_object

    @property
    def export_edges(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExportEdges() As boolean
                | 
                |     Returns or sets the ExportEdges parameter (exported Vrml files will or will
                |     not contains edge informations).
                | 
                |     Parameters:
                | 
                |         oExportEdges
                |             - iExportEdges Value of ExportEdges parameter. Legal
                |             values:
                |             TRUE : exported Vrml files will contain edge informations.
                |             FALSE : exported Vrml files will not contain edge informations.

        :rtype: bool
        """

        return self.vrml_setting_att.ExportEdges

    @export_edges.setter
    def export_edges(self, value: bool):
        """
        :param bool value:
        """

        self.vrml_setting_att.ExportEdges = value

    @property
    def export_normals(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExportNormals() As boolean
                | 
                |     Returns or sets the ExportNormals parameter (exported Vrml files will or
                |     will not contains normal informations).
                | 
                |     Parameters:
                | 
                |         oExportNormals
                |             - iExportNormals Value of ExportNormals parameter. Legal
                |             values:
                |             TRUE : exported Vrml files will contain normal informations.
                |             FALSE : exported Vrml files will not contain normal informations.

        :rtype: bool
        """

        return self.vrml_setting_att.ExportNormals

    @export_normals.setter
    def export_normals(self, value: bool):
        """
        :param bool value:
        """

        self.vrml_setting_att.ExportNormals = value

    @property
    def export_texture(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExportTexture() As boolean
                | 
                |     Returns or sets the ExportTexture parameter (exported Vrml files will or
                |     will not contains texture informations).
                | 
                |     Parameters:
                | 
                |         oExportTexture
                |             - iExportTexture Value of ExportTexture parameter. Legal
                |             values:
                |             TRUE : exported Vrml files will contain texture informations.
                |             FALSE : exported Vrml files will not contain texture informations.

        :rtype: bool
        """

        return self.vrml_setting_att.ExportTexture

    @export_texture.setter
    def export_texture(self, value: bool):
        """
        :param bool value:
        """

        self.vrml_setting_att.ExportTexture = value

    @property
    def export_texture_file(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExportTextureFile() As long
                | 
                |     Returns or sets the ExportTextureFile parameter (Textures will be exported
                |     in the vrml file containing the geometry or in external
                |     files).
                | 
                |     Parameters:
                | 
                |         oExportTextureFile
                |             - iExportTextureFile Value of ExportTextureFile parameter. Legal
                |             values:
                |             0 : Textures are exported in the Vrml file containing the geometry.
                |             1 : Texture are exported in external files.

        :rtype: int
        """

        return self.vrml_setting_att.ExportTextureFile

    @export_texture_file.setter
    def export_texture_file(self, value: int):
        """
        :param int value:
        """

        self.vrml_setting_att.ExportTextureFile = value

    @property
    def export_texture_format(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExportTextureFormat() As long
                | 
                |     Returns or sets the ExportTextureFormat parameter.
                | 
                |     Parameters:
                | 
                |         oExportTextureFormat
                |             - iExportTextureFormat Value of ExportTextureFormat parameter.
                |             Legal values:
                |             NOT APPLICABLE

        :rtype: int
        """

        return self.vrml_setting_att.ExportTextureFormat

    @export_texture_format.setter
    def export_texture_format(self, value: int):
        """
        :param int value:
        """

        self.vrml_setting_att.ExportTextureFormat = value

    @property
    def export_version(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExportVersion() As long
                | 
                |     Returns or sets the ExportVersion parameter (version of exported Vrml
                |     files).
                | 
                |     Parameters:
                | 
                |         oExportVersion
                |             - iExportVersion Value of Import Unit parameter. Legal
                |             values:
                |             1 : VRML 1.0.
                |             2 : VRML 97 (VRML 2.0).

        :rtype: int
        """

        return self.vrml_setting_att.ExportVersion

    @export_version.setter
    def export_version(self, value: int):
        """
        :param int value:
        """

        self.vrml_setting_att.ExportVersion = value

    @property
    def import_crease_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ImportCreaseAngle() As double
                | 
                |     Returns or sets the ImportCreaseAngle parameter. The crease angle affects
                |     how DEFAULT normals are generated. If the angle between the geometric normals
                |     of two adjacent faces is less than the crease angle, normals will be calculated
                |     so that the faces are smooth-shaded across the edge. Otherwise, normals will be
                |     calculated so that a lighting discontinuity across the edge is
                |     produce.
                | 
                |     Parameters:
                | 
                |         oImportCreaseAngle
                |             - iImportCreaseAngle Value of ImportCreaseAngle parameter. Legal
                |             values:
                |             [0,inf]

        :rtype: float
        """

        return self.vrml_setting_att.ImportCreaseAngle

    @import_crease_angle.setter
    def import_crease_angle(self, value: float):
        """
        :param float value:
        """

        self.vrml_setting_att.ImportCreaseAngle = value

    @property
    def import_unit(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ImportUnit() As long
                | 
                |     Returns or sets the ImportUnit parameter (unit of imported Vrml
                |     files).
                | 
                |     Parameters:
                | 
                |         oImportUnit
                |             - iImportUnit Value of Import Unit parameter. Legal
                |             values:
                |             0 : Millimeter.
                |             1 : Centimeter.
                |             2 : Meter.

        :rtype: int
        """

        return self.vrml_setting_att.ImportUnit

    @import_unit.setter
    def import_unit(self, value: int):
        """
        :param int value:
        """

        self.vrml_setting_att.ImportUnit = value

    def get_export_background_color(self, io_r: int, io_g: int, io_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetExportBackgroundColor(long ioR,
                | long ioG,
                | long ioB)
                | 
                |     Returns the ExportBackgroundColor parameter (Background color of exported
                |     Vrml files). Value of ExportBackgroundColor parameter. Legal
                |     values:
                |     R [0,255] G [0,255] B [0,255]

        :param int io_r:
        :param int io_g:
        :param int io_b:
        :rtype: None
        """
        return self.vrml_setting_att.GetExportBackgroundColor(io_r, io_g, io_b)

    def get_export_background_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetExportBackgroundColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ExportBackgroundColor setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.vrml_setting_att.GetExportBackgroundColorInfo(io_admin_level, io_locked)

    def get_export_edges_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetExportEdgesInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ExportEdges setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.vrml_setting_att.GetExportEdgesInfo(io_admin_level, io_locked)

    def get_export_normals_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetExportNormalsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ExportNormals setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.vrml_setting_att.GetExportNormalsInfo(io_admin_level, io_locked)

    def get_export_texture_file_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetExportTextureFileInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ExportTextureFile setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.vrml_setting_att.GetExportTextureFileInfo(io_admin_level, io_locked)

    def get_export_texture_format_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetExportTextureFormatInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ExportTextureFormat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.vrml_setting_att.GetExportTextureFormatInfo(io_admin_level, io_locked)

    def get_export_texture_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetExportTextureInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ExportTexture setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.vrml_setting_att.GetExportTextureInfo(io_admin_level, io_locked)

    def get_export_version_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetExportVersionInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ExportVersion setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.vrml_setting_att.GetExportVersionInfo(io_admin_level, io_locked)

    def get_import_crease_angle_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetImportCreaseAngleInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ImportCreaseAngle setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.vrml_setting_att.GetImportCreaseAngleInfo(io_admin_level, io_locked)

    def get_import_unit_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetImportUnitInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ImportUnit setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.vrml_setting_att.GetImportUnitInfo(io_admin_level, io_locked)

    def set_export_background_color(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExportBackgroundColor(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the ExportBackgroundColor parameter (Background color of exported Vrml
                |     files). Value of ExportBackgroundColor parameter. Legal
                |     values:
                |     R [0,255] G [0,255] B [0,255]

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.vrml_setting_att.SetExportBackgroundColor(i_r, i_g, i_b)

    def set_export_background_color_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExportBackgroundColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the ExportBackgroundColor setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.vrml_setting_att.SetExportBackgroundColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_background_color_lock'
        # # vba_code = """
        # # Public Function set_export_background_color_lock(vrml_setting_att)
        # #     Dim iLocked (2)
        # #     vrml_setting_att.SetExportBackgroundColorLock iLocked
        # #     set_export_background_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_edges_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExportEdgesLock(boolean iLocked)
                | 
                |     Locks or unlocks the ExportEdges setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.vrml_setting_att.SetExportEdgesLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_edges_lock'
        # # vba_code = """
        # # Public Function set_export_edges_lock(vrml_setting_att)
        # #     Dim iLocked (2)
        # #     vrml_setting_att.SetExportEdgesLock iLocked
        # #     set_export_edges_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_normals_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExportNormalsLock(boolean iLocked)
                | 
                |     Locks or unlocks the ExportNormals setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.vrml_setting_att.SetExportNormalsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_normals_lock'
        # # vba_code = """
        # # Public Function set_export_normals_lock(vrml_setting_att)
        # #     Dim iLocked (2)
        # #     vrml_setting_att.SetExportNormalsLock iLocked
        # #     set_export_normals_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_texture_file_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExportTextureFileLock(boolean iLocked)
                | 
                |     Locks or unlocks the ExportTextureFile setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.vrml_setting_att.SetExportTextureFileLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_texture_file_lock'
        # # vba_code = """
        # # Public Function set_export_texture_file_lock(vrml_setting_att)
        # #     Dim iLocked (2)
        # #     vrml_setting_att.SetExportTextureFileLock iLocked
        # #     set_export_texture_file_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_texture_format_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExportTextureFormatLock(boolean iLocked)
                | 
                |     Locks or unlocks the ExportTextureFormat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.vrml_setting_att.SetExportTextureFormatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_texture_format_lock'
        # # vba_code = """
        # # Public Function set_export_texture_format_lock(vrml_setting_att)
        # #     Dim iLocked (2)
        # #     vrml_setting_att.SetExportTextureFormatLock iLocked
        # #     set_export_texture_format_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_texture_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExportTextureLock(boolean iLocked)
                | 
                |     Locks or unlocks the ExportTexture setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.vrml_setting_att.SetExportTextureLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_texture_lock'
        # # vba_code = """
        # # Public Function set_export_texture_lock(vrml_setting_att)
        # #     Dim iLocked (2)
        # #     vrml_setting_att.SetExportTextureLock iLocked
        # #     set_export_texture_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_version_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExportVersionLock(boolean iLocked)
                | 
                |     Locks or unlocks the ExportVersion setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.vrml_setting_att.SetExportVersionLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_version_lock'
        # # vba_code = """
        # # Public Function set_export_version_lock(vrml_setting_att)
        # #     Dim iLocked (2)
        # #     vrml_setting_att.SetExportVersionLock iLocked
        # #     set_export_version_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_crease_angle_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetImportCreaseAngleLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportCreaseAngle setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.vrml_setting_att.SetImportCreaseAngleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_crease_angle_lock'
        # # vba_code = """
        # # Public Function set_import_crease_angle_lock(vrml_setting_att)
        # #     Dim iLocked (2)
        # #     vrml_setting_att.SetImportCreaseAngleLock iLocked
        # #     set_import_crease_angle_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_unit_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetImportUnitLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImportLock setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.vrml_setting_att.SetImportUnitLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_unit_lock'
        # # vba_code = """
        # # Public Function set_import_unit_lock(vrml_setting_att)
        # #     Dim iLocked (2)
        # #     vrml_setting_att.SetImportUnitLock iLocked
        # #     set_import_unit_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'VrmlSettingAtt(name="{self.name}")'
