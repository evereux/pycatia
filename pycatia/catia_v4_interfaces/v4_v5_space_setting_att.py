#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class V4V5SpaceSettingAtt(SettingController):

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
                |                         V4V5SpaceSettingAtt
                | 
                | Represents the object to handle the setting parameters of the "V4V5 Space" tab
                | page.
                | Role: This interface is implemented by a component named
                | CATV4IV4V5SpaceSettingCtrl which represents the controller of the Setting.
                | parameters displayed in the V4V5 Space Data property page. To access this
                | property page:
                | 
                |     Click the Options command in the Tools menu
                |     Click + left of General to unfold the workbench list
                |     Click Compatibility
                | 
                | 
                | The different options for V4/V5 SPACE tab are the following :
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
        self.v4_v5_space_setting_att = com_object

    @property
    def details_mode_explode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DetailsModeExplode() As long
                | 
                |     Returns or sets the activation state of mode for details migration (Explode
                |     Mode)
                |     Role: Returns or sets the state of mode for details migration.

        :rtype: int
        """

        return self.v4_v5_space_setting_att.DetailsModeExplode

    @details_mode_explode.setter
    def details_mode_explode(self, value: int):
        """
        :param int value:
        """

        self.v4_v5_space_setting_att.DetailsModeExplode = value

    @property
    def details_mode_usual(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DetailsModeUsual() As long
                | 
                |     Returns or sets the activation state of mode for details migration (Usual
                |     Mode)
                |     Role: Returns or sets the state of mode for details migration.

        :rtype: int
        """

        return self.v4_v5_space_setting_att.DetailsModeUsual

    @details_mode_usual.setter
    def details_mode_usual(self, value: int):
        """
        :param int value:
        """

        self.v4_v5_space_setting_att.DetailsModeUsual = value

    @property
    def details_mode_wireframe(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DetailsModeWireframe() As long
                | 
                |     Returns or sets the activation state of mode for details migration
                |     (WireFrame Mode)
                |     Role: Returns or sets the state of mode for details migration.

        :rtype: int
        """

        return self.v4_v5_space_setting_att.DetailsModeWireframe

    @details_mode_wireframe.setter
    def details_mode_wireframe(self, value: int):
        """
        :param int value:
        """

        self.v4_v5_space_setting_att.DetailsModeWireframe = value

    @property
    def external_max_deformation(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExternalMaxDeformation() As double
                | 
                |     Returns or sets the activation state of mode with external deformation (Gap
                |     Healing).
                |     Role: Returns or sets the activation state of mode with external
                |     deformation (Gap Healing). during a Copy/Paste As Spec.

        :rtype: float
        """

        return self.v4_v5_space_setting_att.ExternalMaxDeformation

    @external_max_deformation.setter
    def external_max_deformation(self, value: float):
        """
        :param float value:
        """

        self.v4_v5_space_setting_att.ExternalMaxDeformation = value

    @property
    def external_type_deformation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExternalTypeDeformation() As long
                | 
                |     Returns or sets the activation state of type for external deformation (Gap
                |     Healing).
                |     Role: Returns or sets the activation state of type for external deformation
                |     (Model relative or User defined value) during a Copy/Paste As Spec.

        :rtype: int
        """

        return self.v4_v5_space_setting_att.ExternalTypeDeformation

    @external_type_deformation.setter
    def external_type_deformation(self, value: int):
        """
        :param int value:
        """

        self.v4_v5_space_setting_att.ExternalTypeDeformation = value

    @property
    def internal_max_deformation(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InternalMaxDeformation() As double
                | 
                |     Returns or sets the activation state of mode with internal deformation
                |     (Curve Improvement).
                |     Role: Returns or sets the activation state of mode with internal
                |     deformation during a Copy/Paste As Spec.

        :rtype: float
        """

        return self.v4_v5_space_setting_att.InternalMaxDeformation

    @internal_max_deformation.setter
    def internal_max_deformation(self, value: float):
        """
        :param float value:
        """

        self.v4_v5_space_setting_att.InternalMaxDeformation = value

    @property
    def internal_type_deformation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InternalTypeDeformation() As long
                | 
                |     Returns or sets the activation state of type for internal deformation
                |     (Curve Improvement).
                |     Role: Returns or sets the activation state of type for internal deformation
                |     (Model relative or User defined value) during a Copy/Paste As Spec.

        :rtype: int
        """

        return self.v4_v5_space_setting_att.InternalTypeDeformation

    @internal_type_deformation.setter
    def internal_type_deformation(self, value: int):
        """
        :param int value:
        """

        self.v4_v5_space_setting_att.InternalTypeDeformation = value

    @property
    def keep_segmentation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property KeepSegmentation() As long
                | 
                |     Returns or sets the activation state of mode with segmentation (Keep V4
                |     Segmentation ).
                |     Role: Returns or sets the activation state of mode with segmentation during
                |     a Copy/Paste As Spec.

        :rtype: int
        """

        return self.v4_v5_space_setting_att.KeepSegmentation

    @keep_segmentation.setter
    def keep_segmentation(self, value: int):
        """
        :param int value:
        """

        self.v4_v5_space_setting_att.KeepSegmentation = value

    @property
    def solid_mu(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SolidMU() As CATBSTR
                | 
                |     Returns or sets the activation state of mode for isolated Solids Mock-Up
                |     migration
                |     Role: Returns or sets the state of mode for isolated Solids Mock-Up
                |     migration.

        :rtype: str
        """

        return self.v4_v5_space_setting_att.SolidMU

    @solid_mu.setter
    def solid_mu(self, value: str):
        """
        :param str value:
        """

        self.v4_v5_space_setting_att.SolidMU = value

    @property
    def text_migration(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TextMigration() As long
                | 
                |     Returns or sets the activation state of mode for 3D Text
                |     migration
                |     Role: Returns or sets the state of mode for 3D Text migration.

        :rtype: int
        """

        return self.v4_v5_space_setting_att.TextMigration

    @text_migration.setter
    def text_migration(self, value: int):
        """
        :param int value:
        """

        self.v4_v5_space_setting_att.TextMigration = value

    def get_details_mode_explode_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDetailsModeExplodeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Details Migration Mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_v5_space_setting_att.GetDetailsModeExplodeInfo(admin_level, o_locked)

    def get_details_mode_usual_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDetailsModeUsualInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Details Migration Mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_v5_space_setting_att.GetDetailsModeUsualInfo(admin_level, o_locked)

    def get_details_mode_wireframe_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDetailsModeWireframeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Details Migration Mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_v5_space_setting_att.GetDetailsModeWireframeInfo(admin_level, o_locked)

    def get_external_max_deformation_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetExternalMaxDeformationInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the ExternalMaxDeformation setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_v5_space_setting_att.GetExternalMaxDeformationInfo(admin_level, o_locked)

    def get_external_type_deformation_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetExternalTypeDeformationInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for activation mode with external
                |     deformation (Gap Healing).
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_v5_space_setting_att.GetExternalTypeDeformationInfo(admin_level, o_locked)

    def get_internal_max_deformation_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetInternalMaxDeformationInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the InternalMaxDeformation setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_v5_space_setting_att.GetInternalMaxDeformationInfo(admin_level, o_locked)

    def get_internal_type_deformation_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetInternalTypeDeformationInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for activation mode with internal
                |     deformation (Curve Improvement).
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_v5_space_setting_att.GetInternalTypeDeformationInfo(admin_level, o_locked)

    def get_keep_segmentation_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetKeepSegmentationInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the KeepSegmentation setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_v5_space_setting_att.GetKeepSegmentationInfo(admin_level, o_locked)

    def get_solid_mu_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSolidMUInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Solid Mock-Up Migration Mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_v5_space_setting_att.GetSolidMUInfo(admin_level, o_locked)

    def get_text_migration_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTextMigrationInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the 3D Text Migration setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.v4_v5_space_setting_att.GetTextMigrationInfo(admin_level, o_locked)

    def set_details_mode_explode_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDetailsModeExplodeLock(boolean iLock)
                | 
                |     Locks or unlocks the Details Migration Mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_v5_space_setting_att.SetDetailsModeExplodeLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_details_mode_explode_lock'
        # # vba_code = """
        # # Public Function set_details_mode_explode_lock(v4_v5_space_setting_att)
        # #     Dim iLock (2)
        # #     v4_v5_space_setting_att.SetDetailsModeExplodeLock iLock
        # #     set_details_mode_explode_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_details_mode_usual_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDetailsModeUsualLock(boolean iLock)
                | 
                |     Locks or unlocks the Details Migration Mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_v5_space_setting_att.SetDetailsModeUsualLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_details_mode_usual_lock'
        # # vba_code = """
        # # Public Function set_details_mode_usual_lock(v4_v5_space_setting_att)
        # #     Dim iLock (2)
        # #     v4_v5_space_setting_att.SetDetailsModeUsualLock iLock
        # #     set_details_mode_usual_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_details_mode_wireframe_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDetailsModeWireframeLock(boolean iLock)
                | 
                |     Locks or unlocks the Details Migration Mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_v5_space_setting_att.SetDetailsModeWireframeLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_details_mode_wireframe_lock'
        # # vba_code = """
        # # Public Function set_details_mode_wireframe_lock(v4_v5_space_setting_att)
        # #     Dim iLock (2)
        # #     v4_v5_space_setting_att.SetDetailsModeWireframeLock iLock
        # #     set_details_mode_wireframe_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_external_max_deformation_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExternalMaxDeformationLock(boolean iLock)
                | 
                |     Locks or unlocks the "External Control Point Maximum Deformation" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_v5_space_setting_att.SetExternalMaxDeformationLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_external_max_deformation_lock'
        # # vba_code = """
        # # Public Function set_external_max_deformation_lock(v4_v5_space_setting_att)
        # #     Dim iLock (2)
        # #     v4_v5_space_setting_att.SetExternalMaxDeformationLock iLock
        # #     set_external_max_deformation_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_external_type_deformation_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExternalTypeDeformationLock(boolean iLock)
                | 
                |     Locks or unlocks the activation mode with external deformation (Gap
                |     Healing).
                |     Role:Locks or unlocks the activation mode with external deformation if it
                |     is possible
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_v5_space_setting_att.SetExternalTypeDeformationLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_external_type_deformation_lock'
        # # vba_code = """
        # # Public Function set_external_type_deformation_lock(v4_v5_space_setting_att)
        # #     Dim iLock (2)
        # #     v4_v5_space_setting_att.SetExternalTypeDeformationLock iLock
        # #     set_external_type_deformation_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_internal_max_deformation_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetInternalMaxDeformationLock(boolean iLock)
                | 
                |     Locks or unlocks the "Internal Control Point Maximum Deformation" setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_v5_space_setting_att.SetInternalMaxDeformationLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_internal_max_deformation_lock'
        # # vba_code = """
        # # Public Function set_internal_max_deformation_lock(v4_v5_space_setting_att)
        # #     Dim iLock (2)
        # #     v4_v5_space_setting_att.SetInternalMaxDeformationLock iLock
        # #     set_internal_max_deformation_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_internal_type_deformation_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetInternalTypeDeformationLock(boolean iLock)
                | 
                |     Locks or unlocks the activation mode with internal deformation (Curve
                |     Improvement).
                |     Role:Locks or unlocks the activation mode with external deformation if it
                |     is possible
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_v5_space_setting_att.SetInternalTypeDeformationLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_internal_type_deformation_lock'
        # # vba_code = """
        # # Public Function set_internal_type_deformation_lock(v4_v5_space_setting_att)
        # #     Dim iLock (2)
        # #     v4_v5_space_setting_att.SetInternalTypeDeformationLock iLock
        # #     set_internal_type_deformation_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_keep_segmentation_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetKeepSegmentationLock(boolean iLock)
                | 
                |     Locks or unlocks the KeepSegmentation setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_v5_space_setting_att.SetKeepSegmentationLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_keep_segmentation_lock'
        # # vba_code = """
        # # Public Function set_keep_segmentation_lock(v4_v5_space_setting_att)
        # #     Dim iLock (2)
        # #     v4_v5_space_setting_att.SetKeepSegmentationLock iLock
        # #     set_keep_segmentation_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_solid_mu_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSolidMULock(boolean iLock)
                | 
                |     Locks or unlocks the Solid Mock-Up Migration Mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_v5_space_setting_att.SetSolidMULock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_solid_mu_lock'
        # # vba_code = """
        # # Public Function set_solid_mu_lock(v4_v5_space_setting_att)
        # #     Dim iLock (2)
        # #     v4_v5_space_setting_att.SetSolidMULock iLock
        # #     set_solid_mu_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_text_migration_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTextMigrationLock(boolean iLock)
                | 
                |     Locks or unlocks the 3D Text Migration setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.v4_v5_space_setting_att.SetTextMigrationLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_text_migration_lock'
        # # vba_code = """
        # # Public Function set_text_migration_lock(v4_v5_space_setting_att)
        # #     Dim iLock (2)
        # #     v4_v5_space_setting_att.SetTextMigrationLock iLock
        # #     set_text_migration_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'V4V5SpaceSettingAtt(name="{ self.name }")'
