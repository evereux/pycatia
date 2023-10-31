#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class MigrBatchSettingAtt(SettingController):
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
                |                         MigrBatchSettingAtt
                | 
                | Represents the object to handle the setting parameters of the "Migration Batch"
                | tab page.
                | Role: This interface is implemented by a component named
                | CATV4IMigrBatchSettingCtrl which represents the controller of the Setting. The
                | setting parameters of the tab are the following:
                | 
                |     "Format"
                |     "V4 Part Definition"
                |     "Conversion Mode"
                |     "Display Report Attribute"
                |     "Initial Drawing Path "
                |     "Projection of Space for transparent views"
                |     "Mapping Files Location for Saving "
                |     "Specified Directory "
                |     "Mapping Files Location for Retrieving "
                |     "Interface Name"
                | 
                | To access this property page:
                | 
                |     Click the Options command in the Tools menu
                |     Click + left of General to unfold the workbench list
                |     Click Compatibility
                |     Click on the Migration Batch
                |     tabpage 
                | 
                | 
                | This interface defines:
                | 
                |     A method to get each parameter
                |     A method to set the value of each parameter
                |     A method to lock/unlock each parameter
                |     A method to retrieve the informations concerning each
                |     parameter
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.migr_batch_setting_att = com_object

    @property
    def affiche_attribut(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Affiche_Attribut() As CATBSTR
                | 
                |     Retrieves or sets the state of the "Display Report Attribute" setting
                |     parameter.
                |     Role: This functionality allows the visualization of 3D elements attributes
                |     in the Migration Report. For each element, the list of its attributes is
                |     displayed with their names and values.

        :rtype: str
        """

        return self.migr_batch_setting_att.Affiche_Attribut

    @affiche_attribut.setter
    def affiche_attribut(self, value: str):
        """
        :param str value:
        """

        self.migr_batch_setting_att.Affiche_Attribut = value

    @property
    def mapping_file_save_mode(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Mapping_File_Save_Mode() As CATBSTR
                | 
                |     Retrieves or sets the state of the "Mapping Files Location for Saving"
                |     setting parameter.
                |     Role: The "Mapping Files Location for Saving " mode enables you to store a
                |     file which indicates the pointed entities in V4 MML Solids and which allows to
                |     retrieve associativity in CATIA V5. You can specify the directory path of your
                |     choice: Batch Target Directory, Model Directory or Specified Directory.

        :rtype: str
        """

        return self.migr_batch_setting_att.Mapping_File_Save_Mode

    @mapping_file_save_mode.setter
    def mapping_file_save_mode(self, value: str):
        """
        :param str value:
        """

        self.migr_batch_setting_att.Mapping_File_Save_Mode = value

    @property
    def mapping_saving_file(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Mapping_Saving_File() As CATBSTR
                | 
                |     Retrieves or sets the state of the "Specified Directory" setting
                |     parameter.
                |     Role: The "Specified Directory" mode enables you to find pointed entities
                |     in V4 MML Solids and to retrieve associativity in CATIA V5. You can specify the
                |     directory path of your choice.

        :rtype: str
        """

        return self.migr_batch_setting_att.Mapping_Saving_File

    @mapping_saving_file.setter
    def mapping_saving_file(self, value: str):
        """
        :param str value:
        """

        self.migr_batch_setting_att.Mapping_Saving_File = value

    @property
    def migration_format(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Migration_Format() As CATBSTR
                | 
                |     Retrieves or sets the state of the "Format" setting
                |     parameter.
                |     Role: The "Format" mode enables you to select the format of the Migration
                |     in Batch Mode: AS SPEC or AS RESULT.

        :rtype: str
        """

        return self.migr_batch_setting_att.Migration_Format

    @migration_format.setter
    def migration_format(self, value: str):
        """
        :param str value:
        """

        self.migr_batch_setting_att.Migration_Format = value

    @property
    def migration_interface(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Migration_Interface() As CATBSTR
                | 
                |     Retrieves or sets the "Migration Interace" setting
                |     parameter.
                |     Role: This option allows you to customize migrations from CATIA V4 to CATIA
                |     V5. You can choose how your applicative data will be migrated by writing source
                |     code

        :rtype: str
        """

        return self.migr_batch_setting_att.Migration_Interface

    @migration_interface.setter
    def migration_interface(self, value: str):
        """
        :param str value:
        """

        self.migr_batch_setting_att.Migration_Interface = value

    @property
    def migration_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Migration_Type() As CATBSTR
                | 
                |     Retrieves or sets the state of the "Conversion Mode" setting
                |     parameter.
                |     Role: The "Conversion Mode" mode enables you to separate the treatment of
                |     SPACE data and DRAW data when a model is migrated.

        :rtype: str
        """

        return self.migr_batch_setting_att.Migration_Type

    @migration_type.setter
    def migration_type(self, value: str):
        """
        :param str value:
        """

        self.migr_batch_setting_att.Migration_Type = value

    @property
    def search_list_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Search_List_Size() As long
                | 
                |     Retrieves or sets the size of the "Mapping Files Location for Retrieving"
                |     list.
                |     Role: This setting enables to retrieve the size of the "Mapping Files
                |     Location for Retrieving" list.

        :rtype: int
        """

        return self.migr_batch_setting_att.Search_List_Size

    @search_list_size.setter
    def search_list_size(self, value: int):
        """
        :param int value:
        """

        self.migr_batch_setting_att.Search_List_Size = value

    @property
    def start_up_model_for_drawing(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StartUp_Model_For_Drawing() As CATBSTR
                | 
                |     Retrieves or sets the state of the "Initial Drawing Path" setting
                |     parameter.
                |     Role: The "Initial Drawing Path" mode enables you to specify a .CATDrawing
                |     document which will serve as a template. The standard used by this document
                |     will be used during the migration.

        :rtype: str
        """

        return self.migr_batch_setting_att.StartUp_Model_For_Drawing

    @start_up_model_for_drawing.setter
    def start_up_model_for_drawing(self, value: str):
        """
        :param str value:
        """

        self.migr_batch_setting_att.StartUp_Model_For_Drawing = value

    @property
    def v4_part_definition(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property V4_Part_Definition() As CATBSTR
                | 
                |     Retrieves or sets the state of the "V4 Part Definition" setting
                |     parameter.
                |     Role: The "V4 Part Definition" mode enables you to define the CATParts
                |     obtained after the migration: A CATPart by Geometric Set or A CATPart by Solid.
                |     .

        :rtype: str
        """

        return self.migr_batch_setting_att.V4_Part_Definition

    @v4_part_definition.setter
    def v4_part_definition(self, value: str):
        """
        :param str value:
        """

        self.migr_batch_setting_att.V4_Part_Definition = value

    @property
    def visu_mode_2d(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Visu_Mode_2D() As CATBSTR
                | 
                |     Retrieves or sets the state of the "Projection of Space for transparent
                |     views" setting parameter.
                |     Role: The "Projection of Space for transparent views" mode enables you to
                |     specify what kind of projection mode you want to use for transparent views
                |     during the migration: NHR, HLR or the same projection mode as the V4 model.

        :rtype: str
        """

        return self.migr_batch_setting_att.Visu_Mode_2D

    @visu_mode_2d.setter
    def visu_mode_2d(self, value: str):
        """
        :param str value:
        """

        self.migr_batch_setting_att.Visu_Mode_2D = value

    def get_affiche_attribut_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAffiche_AttributInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "Display Report Attribute" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.migr_batch_setting_att.GetAffiche_AttributInfo(admin_level, o_locked)

    def get_mapping_file_save_mode_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMapping_File_Save_ModeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "Mapping Files Location for Saving" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.migr_batch_setting_att.GetMapping_File_Save_ModeInfo(admin_level, o_locked)

    def get_mapping_saving_file_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMapping_Saving_FileInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "Specified Directory" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.migr_batch_setting_att.GetMapping_Saving_FileInfo(admin_level, o_locked)

    def get_migration_format_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMigration_FormatInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "Format" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.migr_batch_setting_att.GetMigration_FormatInfo(admin_level, o_locked)

    def get_migration_interface_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMigration_InterfaceInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "Migration Interface" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.migr_batch_setting_att.GetMigration_InterfaceInfo(admin_level, o_locked)

    def get_migration_type_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMigration_TypeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "Conversion" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.migr_batch_setting_att.GetMigration_TypeInfo(admin_level, o_locked)

    def get_search_mapping_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSearch_Mapping_List() As CATSafeArrayVariant
                | 
                |     Retrieves the state of the "Mapping Files Location for Retrieving" setting
                |     parameter.
                |     Role: The "Mapping Files Location for Retrieving " mode enables you to
                |     store a list of mapping tables.

        :rtype: tuple
        """
        return self.migr_batch_setting_att.GetSearch_Mapping_List()

    def get_start_up_model_for_drawing_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStartUp_Model_For_DrawingInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "Initial Drawing Path" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.migr_batch_setting_att.GetStartUp_Model_For_DrawingInfo(admin_level, o_locked)

    def get_v4_part_definition_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetV4_Part_DefinitionInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "V4 Part Definition" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.migr_batch_setting_att.GetV4_Part_DefinitionInfo(admin_level, o_locked)

    def get_visu_mode_2d_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetVisu_Mode_2DInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the "Projection of Space for transparent views"
                |     setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.migr_batch_setting_att.GetVisu_Mode_2DInfo(admin_level, o_locked)

    def put_search_mapping_list(self, i_rel_path: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutSearch_Mapping_List(CATSafeArrayVariant iRelPath)
                | 
                |     Sets the state of the "Mapping Files Location for Retrieving" setting
                |     parameter.
                |     Role: The "Mapping Files Location for Retrieving " mode enables you to
                |     store a list of mapping tables.

        :param tuple i_rel_path:
        :rtype: None
        """
        return self.migr_batch_setting_att.PutSearch_Mapping_List(i_rel_path)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_search_mapping_list'
        # # vba_code = """
        # # Public Function put_search_mapping_list(migr_batch_setting_att)
        # #     Dim iRelPath (2)
        # #     migr_batch_setting_att.PutSearch_Mapping_List iRelPath
        # #     put_search_mapping_list = iRelPath
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_affiche_attribut_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAffiche_AttributLock(boolean iLock)
                | 
                |     Locks or unlocks the "Display Report Attribute" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.migr_batch_setting_att.SetAffiche_AttributLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_affiche_attribut_lock'
        # # vba_code = """
        # # Public Function set_affiche_attribut_lock(migr_batch_setting_att)
        # #     Dim iLock (2)
        # #     migr_batch_setting_att.SetAffiche_AttributLock iLock
        # #     set_affiche_attribut_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_mapping_file_save_mode_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMapping_File_Save_ModeLock(boolean iLock)
                | 
                |     Locks or unlocks the "Mapping Files Location for Saving" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.migr_batch_setting_att.SetMapping_File_Save_ModeLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_mapping_file_save_mode_lock'
        # # vba_code = """
        # # Public Function set_mapping_file_save_mode_lock(migr_batch_setting_att)
        # #     Dim iLock (2)
        # #     migr_batch_setting_att.SetMapping_File_Save_ModeLock iLock
        # #     set_mapping_file_save_mode_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_mapping_saving_file_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMapping_Saving_FileLock(boolean iLock)
                | 
                |     Locks or unlocks the "Specified Directory" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.migr_batch_setting_att.SetMapping_Saving_FileLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_mapping_saving_file_lock'
        # # vba_code = """
        # # Public Function set_mapping_saving_file_lock(migr_batch_setting_att)
        # #     Dim iLock (2)
        # #     migr_batch_setting_att.SetMapping_Saving_FileLock iLock
        # #     set_mapping_saving_file_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_migration_format_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMigration_FormatLock(boolean iLock)
                | 
                |     Locks or unlocks the "Format" setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.migr_batch_setting_att.SetMigration_FormatLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_migration_format_lock'
        # # vba_code = """
        # # Public Function set_migration_format_lock(migr_batch_setting_att)
        # #     Dim iLock (2)
        # #     migr_batch_setting_att.SetMigration_FormatLock iLock
        # #     set_migration_format_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_migration_interface_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMigration_InterfaceLock(boolean iLock)
                | 
                |     Locks or unlocks the "Migration Interface" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.migr_batch_setting_att.SetMigration_InterfaceLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_migration_interface_lock'
        # # vba_code = """
        # # Public Function set_migration_interface_lock(migr_batch_setting_att)
        # #     Dim iLock (2)
        # #     migr_batch_setting_att.SetMigration_InterfaceLock iLock
        # #     set_migration_interface_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_migration_type_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMigration_TypeLock(boolean iLock)
                | 
                |     Locks or unlocks the "Conversion" setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.migr_batch_setting_att.SetMigration_TypeLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_migration_type_lock'
        # # vba_code = """
        # # Public Function set_migration_type_lock(migr_batch_setting_att)
        # #     Dim iLock (2)
        # #     migr_batch_setting_att.SetMigration_TypeLock iLock
        # #     set_migration_type_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_start_up_model_for_drawing_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStartUp_Model_For_DrawingLock(boolean iLock)
                | 
                |     Locks or unlocks the "Initial Drawing Path" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.migr_batch_setting_att.SetStartUp_Model_For_DrawingLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_start_up_model_for_drawing_lock'
        # # vba_code = """
        # # Public Function set_start_up_model_for_drawing_lock(migr_batch_setting_att)
        # #     Dim iLock (2)
        # #     migr_batch_setting_att.SetStartUp_Model_For_DrawingLock iLock
        # #     set_start_up_model_for_drawing_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_v4_part_definition_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetV4_Part_DefinitionLock(boolean iLock)
                | 
                |     Locks or unlocks the "V4 Part Definition" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.migr_batch_setting_att.SetV4_Part_DefinitionLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_v4_part_definition_lock'
        # # vba_code = """
        # # Public Function set_v4_part_definition_lock(migr_batch_setting_att)
        # #     Dim iLock (2)
        # #     migr_batch_setting_att.SetV4_Part_DefinitionLock iLock
        # #     set_v4_part_definition_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_visu_mode_2d_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetVisu_Mode_2DLock(boolean iLock)
                | 
                |     Locks or unlocks the "Projection of Space for transparent views" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.migr_batch_setting_att.SetVisu_Mode_2DLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_visu_mode_2_d_lock'
        # # vba_code = """
        # # Public Function set_visu_mode_2_d_lock(migr_batch_setting_att)
        # #     Dim iLock (2)
        # #     migr_batch_setting_att.SetVisu_Mode_2DLock iLock
        # #     set_visu_mode_2_d_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MigrBatchSettingAtt(name="{self.name}")'
