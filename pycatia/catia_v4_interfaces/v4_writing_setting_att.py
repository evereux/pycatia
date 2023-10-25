#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class V4WritingSettingAtt(SettingController):
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
                |                         V4WritingSettingAtt
                | 
                | Represents the Saving As V4 Data setting controller object.
                | Role: The Saving As V4 Data setting controller object deals with the setting
                | parameters displayed in the Saving As V4 Data property page. To access this
                | property page:
                | 
                |     Click the Options command in the Tools menu
                |     Click + left of General to unfold the workbench list
                |     Click Compatibility
                | 
                | 
                | The different options for V4/V5SPEC tab:
                | The Writing Code Page
                | The Model Dimension
                | The Model Unit
                | The Initial Model File Path
                | The Associativity Mode
                | The Layer For Non Associative Data
                | The Error Feature Creation if the Save is not complete
                | The Curves Associated To Face Boundaries Creation
                | The V4 Model File Name In Capitals Letters
                | The Small Edges And Faces Cleaning Tolerance
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.v4_writing_setting_att = com_object

    @property
    def asso_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Asso_mode() As CATV4IV5V4AssociativityModeEnum
                | 
                |     Returns or sets the associativity mode of migration.
                |     Role: Returns or sets the associativity mode of migration.If non
                |     associative mode is chosen, it is possible to create or not the solid.

        :return: enum catv4_iv5_v4_associativity_mode_enum
        :rtype: int
        """

        return self.v4_writing_setting_att.Asso_mode

    @asso_mode.setter
    def asso_mode(self, value: int):
        """
        :param int value: enum catv4_iv5_v4_associativity_mode_enum
        """

        self.v4_writing_setting_att.Asso_mode = value

    @property
    def clean_tol_check(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CleanTolCheck() As boolean
                | 
                |     Returns or sets the small edges and faces cleaning tolerance
                |     activation.
                |     Role: Returns or sets the small edges and faces cleaning tolerance
                |     activation.

        :rtype: bool
        """

        return self.v4_writing_setting_att.CleanTolCheck

    @clean_tol_check.setter
    def clean_tol_check(self, value: bool):
        """
        :param bool value:
        """

        self.v4_writing_setting_att.CleanTolCheck = value

    @property
    def clean_tol_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CleanTolValue() As double
                | 
                |     Returns or sets the small edges and faces cleaning tolerance value if
                |     activated.
                |     Role: Returns or sets the small edges and faces cleaning tolerance value if
                |     activated.

        :rtype: float
        """

        return self.v4_writing_setting_att.CleanTolValue

    @clean_tol_value.setter
    def clean_tol_value(self, value: float):
        """
        :param float value:
        """

        self.v4_writing_setting_att.CleanTolValue = value

    @property
    def code_page_dest(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Code_page_Dest() As long
                | 
                |     Returns or sets the activation state of the writing code
                |     page.
                |     Role: Returns or sets the value of the writing code page.

        :rtype: int
        """

        return self.v4_writing_setting_att.Code_page_Dest

    @code_page_dest.setter
    def code_page_dest(self, value: int):
        """
        :param int value:
        """

        self.v4_writing_setting_att.Code_page_Dest = value

    @property
    def initial_model_file_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Initial_Model_File_Path() As CATBSTR
                | 
                |     Returns or sets the initial model file path.
                |     Role: Returns or sets the initial model file path.

        :rtype: str
        """

        return self.v4_writing_setting_att.Initial_Model_File_Path

    @initial_model_file_path.setter
    def initial_model_file_path(self, value: str):
        """
        :param str value:
        """

        self.v4_writing_setting_att.Initial_Model_File_Path = value

    @property
    def layer_for_no_asso(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Layer_for_No_Asso() As long
                | 
                |     Returns or sets the layer for not associative data.
                |     Role: Returns or sets the layer for not associative data.

        :rtype: int
        """

        return self.v4_writing_setting_att.Layer_for_No_Asso

    @layer_for_no_asso.setter
    def layer_for_no_asso(self, value: int):
        """
        :param int value:
        """

        self.v4_writing_setting_att.Layer_for_No_Asso = value

    @property
    def mode_create_display(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ModeCreateDisplay() As
                | CATV4IV5V4InternalCurveCreationEnum
                | 
                |     Returns or sets the curves associated to faces'boundaries creation
                |     option.
                |     Role: Returns or sets the curves associated to faces'boundaries creation
                |     option.

        :return: enum catv4_iv5_v4_internal_curve_creation_enum
        :rtype: int
        """

        return self.v4_writing_setting_att.ModeCreateDisplay

    @mode_create_display.setter
    def mode_create_display(self, value: int):
        """
        :param int value: enum catv4_iv5_v4_internal_curve_creation_enum
        """

        self.v4_writing_setting_att.ModeCreateDisplay = value

    @property
    def mode_error_display(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ModeErrorDisplay() As
                | CATV4IV5V4ErrorFeatureCreationEnum
                | 
                |     Returns or sets the error feature creation option.
                |     Role: Returns or sets the error feature creation option.

        :return: enum catv4_iv5_v4_error_feature_creation_enum
        :rtype: int
        """

        return self.v4_writing_setting_att.ModeErrorDisplay

    @mode_error_display.setter
    def mode_error_display(self, value: int):
        """
        :param int value: enum catv4_iv5_v4_error_feature_creation_enum
        """

        self.v4_writing_setting_att.ModeErrorDisplay = value

    @property
    def model_dimension(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Model_Dimension() As double
                | 
                |     Returns or sets the model dimension.
                |     Role: Returns or sets the model dimension.

        :rtype: float
        """

        return self.v4_writing_setting_att.Model_Dimension

    @model_dimension.setter
    def model_dimension(self, value: float):
        """
        :param float value:
        """

        self.v4_writing_setting_att.Model_Dimension = value

    @property
    def model_factor(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Model_Factor() As double
                | 
                |     Returns or sets the model factor.
                |     Role: Returns or sets the model factor that manages the conversion of model
                |     dimension in millimeters.

        :rtype: float
        """

        return self.v4_writing_setting_att.Model_Factor

    @model_factor.setter
    def model_factor(self, value: float):
        """
        :param float value:
        """

        self.v4_writing_setting_att.Model_Factor = value

    @property
    def model_file_name(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Model_File_Name() As boolean
                | 
                |     Returns or sets the model file name in capital letters
                |     option.
                |     Role: Returns or sets the model file name in capital letters option.

        :rtype: bool
        """

        return self.v4_writing_setting_att.Model_File_Name

    @model_file_name.setter
    def model_file_name(self, value: bool):
        """
        :param bool value:
        """

        self.v4_writing_setting_att.Model_File_Name = value

    @property
    def model_unit(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Model_Unit() As long
                | 
                |     Returns or sets the model unit.
                |     Role: Returns or sets the model unit.

        :rtype: int
        """

        return self.v4_writing_setting_att.Model_Unit

    @model_unit.setter
    def model_unit(self, value: int):
        """
        :param int value:
        """

        self.v4_writing_setting_att.Model_Unit = value

    def get_asso_mode_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAsso_modeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Asso_mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_writing_setting_att.GetAsso_modeInfo(admin_level, o_locked)

    def get_clean_tol_check_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCleanTolCheckInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the CleanTolCheck setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_writing_setting_att.GetCleanTolCheckInfo(admin_level, o_locked)

    def get_clean_tol_value_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCleanTolValueInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the CleanTolValue setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_writing_setting_att.GetCleanTolValueInfo(admin_level, o_locked)

    def get_code_page_dest_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCode_page_DestInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Code_page_Dest setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_writing_setting_att.GetCode_page_DestInfo(admin_level, o_locked)

    def get_initial_model_file_path_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetInitial_Model_File_PathInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Initial_Model_File_Path setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_writing_setting_att.GetInitial_Model_File_PathInfo(admin_level, o_locked)

    def get_layer_for_no_asso_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLayer_for_No_AssoInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Layer_for_No_Asso setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_writing_setting_att.GetLayer_for_No_AssoInfo(admin_level, o_locked)

    def get_mode_create_display_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetModeCreateDisplayInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the ModeCreateDisplay setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_writing_setting_att.GetModeCreateDisplayInfo(admin_level, o_locked)

    def get_mode_error_display_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetModeErrorDisplayInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the ModeErrorDisplay setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_writing_setting_att.GetModeErrorDisplayInfo(admin_level, o_locked)

    def get_model_dimension_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetModel_DimensionInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Model_Dimension setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_writing_setting_att.GetModel_DimensionInfo(admin_level, o_locked)

    def get_model_factor_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetModel_FactorInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Model_Factor setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_writing_setting_att.GetModel_FactorInfo(admin_level, o_locked)

    def get_model_file_name_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetModel_File_NameInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Model_File_Name setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_writing_setting_att.GetModel_File_NameInfo(admin_level, o_locked)

    def get_model_unit_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetModel_UnitInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Model_Unit setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_writing_setting_att.GetModel_UnitInfo(admin_level, o_locked)

    def set_asso_mode_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAsso_modeLock(boolean iLock)
                | 
                |     Locks or unlocks the Asso_mode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_writing_setting_att.SetAsso_modeLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_asso_mode_lock'
        # # vba_code = """
        # # Public Function set_asso_mode_lock(v4_writing_setting_att)
        # #     Dim iLock (2)
        # #     v4_writing_setting_att.SetAsso_modeLock iLock
        # #     set_asso_mode_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_clean_tol_check_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCleanTolCheckLock(boolean iLock)
                | 
                |     Locks or unlocks the CleanTolCheck setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_writing_setting_att.SetCleanTolCheckLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_clean_tol_check_lock'
        # # vba_code = """
        # # Public Function set_clean_tol_check_lock(v4_writing_setting_att)
        # #     Dim iLock (2)
        # #     v4_writing_setting_att.SetCleanTolCheckLock iLock
        # #     set_clean_tol_check_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_clean_tol_value_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCleanTolValueLock(boolean iLock)
                | 
                |     Locks or unlocks the CleanTolValue setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_writing_setting_att.SetCleanTolValueLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_clean_tol_value_lock'
        # # vba_code = """
        # # Public Function set_clean_tol_value_lock(v4_writing_setting_att)
        # #     Dim iLock (2)
        # #     v4_writing_setting_att.SetCleanTolValueLock iLock
        # #     set_clean_tol_value_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_code_page_dest_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCode_page_DestLock(boolean iLock)
                | 
                |     Locks or unlocks the Code_page_Dest setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_writing_setting_att.SetCode_page_DestLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_code_page_dest_lock'
        # # vba_code = """
        # # Public Function set_code_page_dest_lock(v4_writing_setting_att)
        # #     Dim iLock (2)
        # #     v4_writing_setting_att.SetCode_page_DestLock iLock
        # #     set_code_page_dest_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_initial_model_file_path_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetInitial_Model_File_PathLock(boolean iLock)
                | 
                |     Locks or unlocks the Initial_Model_File_Path setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_writing_setting_att.SetInitial_Model_File_PathLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_initial_model_file_path_lock'
        # # vba_code = """
        # # Public Function set_initial_model_file_path_lock(v4_writing_setting_att)
        # #     Dim iLock (2)
        # #     v4_writing_setting_att.SetInitial_Model_File_PathLock iLock
        # #     set_initial_model_file_path_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_layer_for_no_asso_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLayer_for_No_AssoLock(boolean iLock)
                | 
                |     Locks or unlocks the Layer_for_No_Asso setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_writing_setting_att.SetLayer_for_No_AssoLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_layer_for_no_asso_lock'
        # # vba_code = """
        # # Public Function set_layer_for_no_asso_lock(v4_writing_setting_att)
        # #     Dim iLock (2)
        # #     v4_writing_setting_att.SetLayer_for_No_AssoLock iLock
        # #     set_layer_for_no_asso_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_mode_create_display_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetModeCreateDisplayLock(boolean iLock)
                | 
                |     Locks or unlocks the ModeCreateDisplay setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_writing_setting_att.SetModeCreateDisplayLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_mode_create_display_lock'
        # # vba_code = """
        # # Public Function set_mode_create_display_lock(v4_writing_setting_att)
        # #     Dim iLock (2)
        # #     v4_writing_setting_att.SetModeCreateDisplayLock iLock
        # #     set_mode_create_display_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_mode_error_display_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetModeErrorDisplayLock(boolean iLock)
                | 
                |     Locks or unlocks the ModeErrorDisplay setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_writing_setting_att.SetModeErrorDisplayLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_mode_error_display_lock'
        # # vba_code = """
        # # Public Function set_mode_error_display_lock(v4_writing_setting_att)
        # #     Dim iLock (2)
        # #     v4_writing_setting_att.SetModeErrorDisplayLock iLock
        # #     set_mode_error_display_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_model_dimension_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetModel_DimensionLock(boolean iLock)
                | 
                |     Locks or unlocks the Model_Dimension setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_writing_setting_att.SetModel_DimensionLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_model_dimension_lock'
        # # vba_code = """
        # # Public Function set_model_dimension_lock(v4_writing_setting_att)
        # #     Dim iLock (2)
        # #     v4_writing_setting_att.SetModel_DimensionLock iLock
        # #     set_model_dimension_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_model_factor_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetModel_FactorLock(boolean iLock)
                | 
                |     Locks or unlocks the Model_Factor setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_writing_setting_att.SetModel_FactorLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_model_factor_lock'
        # # vba_code = """
        # # Public Function set_model_factor_lock(v4_writing_setting_att)
        # #     Dim iLock (2)
        # #     v4_writing_setting_att.SetModel_FactorLock iLock
        # #     set_model_factor_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_model_file_name_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetModel_File_NameLock(boolean iLock)
                | 
                |     Locks or unlocks the Model_File_Name setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_writing_setting_att.SetModel_File_NameLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_model_file_name_lock'
        # # vba_code = """
        # # Public Function set_model_file_name_lock(v4_writing_setting_att)
        # #     Dim iLock (2)
        # #     v4_writing_setting_att.SetModel_File_NameLock iLock
        # #     set_model_file_name_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_model_unit_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetModel_UnitLock(boolean iLock)
                | 
                |     Locks or unlocks the Model_Unit setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_writing_setting_att.SetModel_UnitLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_model_unit_lock'
        # # vba_code = """
        # # Public Function set_model_unit_lock(v4_writing_setting_att)
        # #     Dim iLock (2)
        # #     v4_writing_setting_att.SetModel_UnitLock iLock
        # #     set_model_unit_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'V4WritingSettingAtt(name="{self.name}")'
