#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class MfgHubSettingAtt(SettingController):
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
                |                         MfgHubSettingAtt
                | 
                | Represents the Manufacturing Hub setting controller object.
                | Role: The HubSettingAtt1 setting controller object deals with the setting
                | attributes displayed in the PPR Hub property page. To access this property
                | page:
                | 
                |     Click the Options command in the Tools menu
                |     Click + left of Digital Process for Manufacturing to unfold the workbench
                |     list
                |     Right scroll to display the property pages titles until you get PPR
                |     Hub
                |     Click PPR Hub
                | 
                | The New Elements setting controller object can be retrieved as an item of the
                | setting controller collection using its name "HubSettingAtt1" as
                | follows:
                | 
                |  Dim settingControllers1 As SettingControllers
                |  Set settingControllers1 = CATIA.SettingControllers
                |  Dim HubSettingAtt1 as DNBMHIMfgHubSettingCtrl
                |  set HubSettingAtt1 = settingControllers1.Item( "DNBMHIMfgHubSettingCtrl" )
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mfg_hub_setting_att = com_object

    @property
    def append_context_chk_b(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AppendContextChkB() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the AppendContextChkB
                |     attribute.
                | 
                |     A TRUE value indicates that the loaded context will be appended to the
                |     existing context in the V5 process document

        :rtype: bool
        """

        return self.mfg_hub_setting_att.AppendContextChkB

    @append_context_chk_b.setter
    def append_context_chk_b(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.AppendContextChkB = value

    @property
    def apply_label_eff_to_alt_child(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ApplyLabelEffToAltChild() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the ApplyLabelEffToAltChild
                |     attribute.
                | 
                |     A TRUE value indicates that the label effectivity will be applied to all
                |     components associated with the Alternative

        :rtype: bool
        """

        return self.mfg_hub_setting_att.ApplyLabelEffToAltChild

    @apply_label_eff_to_alt_child.setter
    def apply_label_eff_to_alt_child(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.ApplyLabelEffToAltChild = value

    @property
    def auto_load_mfg_ctx(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AutoLoadMfgCtx() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the AutoLoadMfgCtx
                |     parameter.
                | 
                |     A TRUE value indicates that the manufacturing context is automatically
                |     (computed and) loaded into the V5 process document during load

        :rtype: bool
        """

        return self.mfg_hub_setting_att.AutoLoadMfgCtx

    @auto_load_mfg_ctx.setter
    def auto_load_mfg_ctx(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.AutoLoadMfgCtx = value

    @property
    def auto_load_srv_mfg_ctx(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AutoLoadSrvMfgCtx() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the AutoLoadSrvMfgCtx
                |     parameter.
                | 
                |     A TRUE value indicates that the existing volumetric context is to be
                |     automatically loaded into the V5 process document during load

        :rtype: bool
        """

        return self.mfg_hub_setting_att.AutoLoadSrvMfgCtx

    @auto_load_srv_mfg_ctx.setter
    def auto_load_srv_mfg_ctx(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.AutoLoadSrvMfgCtx = value

    @property
    def auto_load_vol_ctx(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AutoLoadVolCtx() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the AutoLoadVolCtx
                |     parameter.
                | 
                |     A TRUE value indicates that the existing volumetric context is to be
                |     automatically loaded into the V5 process document during load

        :rtype: bool
        """

        return self.mfg_hub_setting_att.AutoLoadVolCtx

    @auto_load_vol_ctx.setter
    def auto_load_vol_ctx(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.AutoLoadVolCtx = value

    @property
    def disable_shape_roll_up(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DisableShapeRollUp() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the DisableShapeRollUp
                |     attribute.
                | 
                |     A TRUE value indicates that the Shape Rollup won't be added during load

        :rtype: bool
        """

        return self.mfg_hub_setting_att.DisableShapeRollUp

    @disable_shape_roll_up.setter
    def disable_shape_roll_up(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.DisableShapeRollUp = value

    @property
    def issue_repository_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IssueRepositoryPath() As CATBSTR
                | 
                |     Retrieves (or sets, if not initialized) the IssueRepositoryPath
                |     attribute.
                | 
                |     Parameters:
                | 
                |         oIssueRepositoryPath
                |             [out] Path stored in settings (or default path if none stored)
                |             
                | 
                |     Returns:
                |         S_OK if everything ran ok

        :rtype: str
        """

        return self.mfg_hub_setting_att.IssueRepositoryPath

    @issue_repository_path.setter
    def issue_repository_path(self, value: str):
        """
        :param str value:
        """

        self.mfg_hub_setting_att.IssueRepositoryPath = value

    @property
    def link_send_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LinkSendMode() As short
                | 
                |     Retrieves (or sets, if not initialized) the LinkSendMode
                |     attribute.
                | 
                |     Parameters:
                | 
                |         ioLinkSendMode
                |             [inout] The value stored in settings (or default value if none
                |             stored) Legal values:
                |             0: If link location is to be sent
                |             1: If link itself is to be sent (as attachment) 
                | 
                |     Returns:
                |         S_OK if everything ran ok

        :rtype: int
        """

        return self.mfg_hub_setting_att.LinkSendMode

    @link_send_mode.setter
    def link_send_mode(self, value: int):
        """
        :param int value:
        """

        self.mfg_hub_setting_att.LinkSendMode = value

    @property
    def load_3d_state_and_pos(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Load3dStateAndPos() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the Load3dStateAndPos
                |     parameter.
                | 
                |     A TRUE value indicates that the ENOVIA product geometry will be loaded from
                |     ENOVIA database.

        :rtype: bool
        """

        return self.mfg_hub_setting_att.Load3dStateAndPos

    @load_3d_state_and_pos.setter
    def load_3d_state_and_pos(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.Load3dStateAndPos = value

    @property
    def load_all_child_proc_mfg_ctx(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadAllChildProcMfgCtx() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadAllChildProcMfgCtx
                |     parameter.
                | 
                |     If set to TRUE than during load of manufacturing context the child
                |     processes of the previous processes will also be considered

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadAllChildProcMfgCtx

    @load_all_child_proc_mfg_ctx.setter
    def load_all_child_proc_mfg_ctx(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadAllChildProcMfgCtx = value

    @property
    def load_assoc_prd_res_child(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadAssocPrdResChild() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadAssocPrdResChild
                |     parameter.
                | 
                |     A TRUE value indicates that the associated prdres children will be loaded
                |     from the database.

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadAssocPrdResChild

    @load_assoc_prd_res_child.setter
    def load_assoc_prd_res_child(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadAssocPrdResChild = value

    @property
    def load_child_proc_mfg_ctx(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadChildProcMfgCtx() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadChildProcMfgCtx
                |     parameter.
                | 
                |     If set to TRUE than during load of manufacturing context the child
                |     processes of the previous processes will also be considered

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadChildProcMfgCtx

    @load_child_proc_mfg_ctx.setter
    def load_child_proc_mfg_ctx(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadChildProcMfgCtx = value

    @property
    def load_ctx_with_file_geometry(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadCtxWithFileGeometry() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadCtxWithFileGeometry
                |     parameter.
                | 
                |     A TRUE value indicates that the existing volumetric context is to be
                |     automatically loaded into the V5 process document during load

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadCtxWithFileGeometry

    @load_ctx_with_file_geometry.setter
    def load_ctx_with_file_geometry(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadCtxWithFileGeometry = value

    @property
    def load_disp_mfg_ctx(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadDispMfgCtx() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadDispMfgCtx
                |     parameter.
                | 
                |     A TRUE value indicates that the manufacturing context is display in the V5
                |     process document

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadDispMfgCtx

    @load_disp_mfg_ctx.setter
    def load_disp_mfg_ctx(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadDispMfgCtx = value

    @property
    def load_duplicates_in_context_tree_chk_b(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadDuplicatesInContextTreeChkB() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadDuplicatesChkB
                |     attribute.
                | 
                |     A TRUE value indicates that the duplicate objects will be loaded in the
                |     context in the V5 process document

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadDuplicatesInContextTreeChkB

    @load_duplicates_in_context_tree_chk_b.setter
    def load_duplicates_in_context_tree_chk_b(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadDuplicatesInContextTreeChkB = value

    @property
    def load_env_geom_from_en_vdb(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadENVGeomFromENVdb() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadENVGeomFromENVdb
                |     parameter.
                | 
                |     A TRUE value indicates that the ENOVIA product geometry will be loaded from
                |     ENOVIA database.

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadENVGeomFromENVdb

    @load_env_geom_from_en_vdb.setter
    def load_env_geom_from_en_vdb(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadENVGeomFromENVdb = value

    @property
    def load_feed_proc_mfg_ctx(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadFeedProcMfgCtx() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadFeedProcMfgCtx
                |     parameter.
                | 
                |     A TRUE value indicates that during load the manufacturing context will also
                |     include products / resource of the feeder process of the previous processes in
                |     process graph

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadFeedProcMfgCtx

    @load_feed_proc_mfg_ctx.setter
    def load_feed_proc_mfg_ctx(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadFeedProcMfgCtx = value

    @property
    def load_mfg_assembly(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadMfgAssmbly() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadMfgAssmbly
                |     parameter.
                | 
                |     A TRUE value indicates that the Manufacturing Assemblies related to process
                |     will be loaded when a PPRHub project is opened in V5

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadMfgAssmbly

    @load_mfg_assembly.setter
    def load_mfg_assembly(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadMfgAssmbly = value

    @property
    def load_mfg_kits(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadMfgKits() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadMfgKits
                |     parameter.
                | 
                |     A TRUE value indicates tthat the Manufacturing Kits related to process will
                |     be loaded when a PPRHub project is opened in V5

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadMfgKits

    @load_mfg_kits.setter
    def load_mfg_kits(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadMfgKits = value

    @property
    def load_pss_data(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadPSSData() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadPSSData
                |     attribute.
                | 
                |     A TRUE value indicates that the PSS data will be loaded from the database.

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadPSSData

    @load_pss_data.setter
    def load_pss_data(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadPSSData = value

    @property
    def load_prd_res_user_attribs(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadPrdResUserAttribs() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadPrdResUserAttribs
                |     parameter.

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadPrdResUserAttribs

    @load_prd_res_user_attribs.setter
    def load_prd_res_user_attribs(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadPrdResUserAttribs = value

    @property
    def load_res_geo(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadResGeo() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadResGeo
                |     parameter.
                | 
                |     A TRUE value indicates tthat the Geometries related to Resource will be
                |     loaded when a PPRHub project is opened in V5

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadResGeo

    @load_res_geo.setter
    def load_res_geo(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadResGeo = value

    @property
    def load_unconstrained_mfg_ctx(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LoadUnconstrainedMfgCtx() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LoadUnconstrainedMfgCtx
                |     parameter.
                | 
                |     A TRUE value indicates that on load the manufacturing context will also
                |     include products / resource of the processes not linked in the process graph
                |     containing loaded process

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LoadUnconstrainedMfgCtx

    @load_unconstrained_mfg_ctx.setter
    def load_unconstrained_mfg_ctx(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LoadUnconstrainedMfgCtx = value

    @property
    def lock_assigned_prd_on_load(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LockAssignedPrdOnLoad() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the LockAssignedPrdOnLoad
                |     parameter.
                | 
                |     If set to TRUE than on load all the products assigned to process(es) will
                |     be locked in WRITE mode

        :rtype: bool
        """

        return self.mfg_hub_setting_att.LockAssignedPrdOnLoad

    @lock_assigned_prd_on_load.setter
    def lock_assigned_prd_on_load(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.LockAssignedPrdOnLoad = value

    @property
    def mail_client_launch_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MailClientLaunchMode() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the MailClientLaunchMode
                |     attribute.
                | 
                |     Parameters:
                | 
                |         ioMailClientLaunchMode
                |             [inout] The value stored in settings (or default value if none
                |             stored) Legal values:
                |             1: If mail client is to be launched
                |             0: If mail client is not to be launched 
                | 
                |     Returns:
                |         S_OK if everything ran ok

        :rtype: bool
        """

        return self.mfg_hub_setting_att.MailClientLaunchMode

    @mail_client_launch_mode.setter
    def mail_client_launch_mode(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.MailClientLaunchMode = value

    @property
    def mfg_ctx_prev_proc_relation_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MfgCtxPrevProcRelationType() As short
                | 
                |     Retrieves the MfgCtxPrevProcRelationType parameter
                | 
                |     The valid integer values (0,1) define the type of Process Traversal
                |     Relations to consider while computing Manufacturing Context

        :rtype: int
        """

        return self.mfg_hub_setting_att.MfgCtxPrevProcRelationType

    @mfg_ctx_prev_proc_relation_type.setter
    def mfg_ctx_prev_proc_relation_type(self, value: int):
        """
        :param int value:
        """

        self.mfg_hub_setting_att.MfgCtxPrevProcRelationType = value

    @property
    def only_load_ctx_with_geometry(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OnlyLoadCtxWithGeometry() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the OnlyLoadCtxWithGeometry
                |     parameter.
                | 
                |     A TRUE value indicates that the existing volumetric context is to be
                |     automatically loaded into the V5 process document during load

        :rtype: bool
        """

        return self.mfg_hub_setting_att.OnlyLoadCtxWithGeometry

    @only_load_ctx_with_geometry.setter
    def only_load_ctx_with_geometry(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.OnlyLoadCtxWithGeometry = value

    @property
    def open_mode_for_load(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OpenModeForLoad() As long
                | 
                |     Retrieves (or sets, if not initialized) the OpenModeForLoad
                |     attribute.
                | 
                |     Parameters:
                | 
                |         oOpenModeForLoad[out]
                |             The mode with which the data will be loaded in hub. The possible
                |             values are as follows 0: Read-Write Mode (Default) 1: Partial Read Only Mode 2:
                |             Read Only mode

        :rtype: int
        """

        return self.mfg_hub_setting_att.OpenModeForLoad

    @open_mode_for_load.setter
    def open_mode_for_load(self, value: int):
        """
        :param int value:
        """

        self.mfg_hub_setting_att.OpenModeForLoad = value

    @property
    def pack_and_go_repository_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PackAndGoRepositoryPath() As CATBSTR
                | 
                |     Retrieves (or sets, if not initialized) the PackAndGoRepositoryPath
                |     attribute.
                | 
                |     Parameters:
                | 
                |         ioPackAndGoRepositoryPath
                |             [out] Path stored in settings (or default path if none stored)
                |             
                | 
                |     Returns:
                |         S_OK if everything ran ok

        :rtype: str
        """

        return self.mfg_hub_setting_att.PackAndGoRepositoryPath

    @pack_and_go_repository_path.setter
    def pack_and_go_repository_path(self, value: str):
        """
        :param str value:
        """

        self.mfg_hub_setting_att.PackAndGoRepositoryPath = value

    @property
    def post_load_script_option(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PostLoadScriptOption() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the PostLoadScriptOption
                |     attribute.
                | 
                |     A TRUE value indicates that the provided script in the editor will be
                |     executed post Load

        :rtype: bool
        """

        return self.mfg_hub_setting_att.PostLoadScriptOption

    @post_load_script_option.setter
    def post_load_script_option(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.PostLoadScriptOption = value

    @property
    def post_load_script_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PostLoadScriptPath() As CATBSTR
                | 
                |     Retrieves (or sets, if not initialized) the PostLoadScriptPath
                |     attribute.
                | 
                |     Parameters:
                | 
                |         oPostLoadScriptPath
                |             [out] Path stored in settings (or default path if none stored)
                |             
                | 
                |     Returns:
                |         S_OK if everything ran ok

        :rtype: str
        """

        return self.mfg_hub_setting_att.PostLoadScriptPath

    @post_load_script_path.setter
    def post_load_script_path(self, value: str):
        """
        :param str value:
        """

        self.mfg_hub_setting_att.PostLoadScriptPath = value

    @property
    def post_load_vba_module(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PostLoadVBAModule() As CATBSTR
                | 
                |     Retrieves (or sets, if not initialized) the PostLoadVBAModule
                |     attribute.
                | 
                |     Parameters:
                | 
                |         ioPostLoadVBAModule
                |             [inout] VBA Module name stored in settings 
                | 
                |     Returns:
                |         S_OK if everything ran ok

        :rtype: str
        """

        return self.mfg_hub_setting_att.PostLoadVBAModule

    @post_load_vba_module.setter
    def post_load_vba_module(self, value: str):
        """
        :param str value:
        """

        self.mfg_hub_setting_att.PostLoadVBAModule = value

    @property
    def prev_proc_parse_type_for_mfg_ctx(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PrevProcParseTypeForMfgCtx() As short
                | 
                |     Retrieves or sets the PrevProcParseTypeForMfgCtx
                |     parameter.
                | 
                |     The valid integer values (0,1,2) define extent of parsing previous process
                |     in the loaded process' parent process structure

        :rtype: int
        """

        return self.mfg_hub_setting_att.PrevProcParseTypeForMfgCtx

    @prev_proc_parse_type_for_mfg_ctx.setter
    def prev_proc_parse_type_for_mfg_ctx(self, value: int):
        """
        :param int value:
        """

        self.mfg_hub_setting_att.PrevProcParseTypeForMfgCtx = value

    @property
    def proc_prod_relations(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ProcProdRelations() As CATSafeArrayVariant
                | 
                |     Retrieves (or sets, if not initialized) the ProcProdRelations
                |     attribute.
                | 
                |     A safe array of process - product relations to be loaded

        :rtype: tuple
        """

        return self.mfg_hub_setting_att.ProcProdRelations

    @proc_prod_relations.setter
    def proc_prod_relations(self, value: tuple):
        """
        :param tuple value:
        """

        self.mfg_hub_setting_att.ProcProdRelations = value

    @property
    def proc_res_relations(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ProcResRelations() As CATSafeArrayVariant
                | 
                |     Retrieves (or sets, if not initialized) the ProcResRelations
                |     attribute.
                | 
                |     A safe array of process - resource relations to be loaded

        :rtype: tuple
        """

        return self.mfg_hub_setting_att.ProcResRelations

    @proc_res_relations.setter
    def proc_res_relations(self, value: tuple):
        """
        :param tuple value:
        """

        self.mfg_hub_setting_att.ProcResRelations = value

    @property
    def rmv_not_assgn_prd_res_on_sync(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RmvNotAssgnPrdResOnSync() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the RmvNotAssgnPrdResOnSync
                |     parameter.
                | 
                |     If set to TRUE than on synchronization during load the products or
                |     resources that are not assigned to any loaded processes will be removed from
                |     the V5 document.

        :rtype: bool
        """

        return self.mfg_hub_setting_att.RmvNotAssgnPrdResOnSync

    @rmv_not_assgn_prd_res_on_sync.setter
    def rmv_not_assgn_prd_res_on_sync(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.RmvNotAssgnPrdResOnSync = value

    @property
    def save_control_flow_in_pro_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SaveControlFlowInPROMode() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the SaveControlFlowInPROMode
                |     attribute.
                | 
                |     A TRUE value indicates that the Control flow will be saved to the database
                |     in Partial Read only mode

        :rtype: bool
        """

        return self.mfg_hub_setting_att.SaveControlFlowInPROMode

    @save_control_flow_in_pro_mode.setter
    def save_control_flow_in_pro_mode(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.SaveControlFlowInPROMode = value

    @property
    def save_ppr_no_detailing(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SavePPRNoDetailing() As boolean
                | 
                |     Returns (or sets, if not initialized) the SavePPRNoDetailing
                |     parameter.
                | 
                |     A TRUE value indicates that simulation detailing data is NOT saved in PPR
                |     hub during save.

        :rtype: bool
        """

        return self.mfg_hub_setting_att.SavePPRNoDetailing

    @save_ppr_no_detailing.setter
    def save_ppr_no_detailing(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.SavePPRNoDetailing = value

    @property
    def save_relation_to_un_exposed_part(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SaveRelationToUnExposedPart() As boolean
                | 
                |     Returns (or sets, if not initialized) the SaveRelationToUnExposedPart
                |     parameter.
                | 
                |     A TRUE value indicates that the relation to unexposed part will be saved in
                |     the database

        :rtype: bool
        """

        return self.mfg_hub_setting_att.SaveRelationToUnExposedPart

    @save_relation_to_un_exposed_part.setter
    def save_relation_to_un_exposed_part(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.SaveRelationToUnExposedPart = value

    @property
    def save_show_effctvt_panel(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SaveShowEffctvtPanel() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the SaveShowEffctvtPanel
                |     parameter.
                | 
                |     If set to TRUE (and SavePPRNoDetailing is TRUE) a panel is displayed
                |     showing effectivity filter information

        :rtype: bool
        """

        return self.mfg_hub_setting_att.SaveShowEffctvtPanel

    @save_show_effctvt_panel.setter
    def save_show_effctvt_panel(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.SaveShowEffctvtPanel = value

    @property
    def save_v5_calc_time(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SaveV5CalcTime() As boolean
                | 
                |     Returns (or sets, if not initialized) the SaveV5CalcTime
                |     parameter.
                | 
                |     A TRUE value indicates that the calculated cycle time for V5 process should
                |     be assigned to corresponding E5 process attribure on save

        :rtype: bool
        """

        return self.mfg_hub_setting_att.SaveV5CalcTime

    @save_v5_calc_time.setter
    def save_v5_calc_time(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.SaveV5CalcTime = value

    @property
    def show_only_filtered_objects(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ShowOnlyFilteredObjects() As boolean
                | 
                |     Retrieves (or sets, if not initialized) the ShowOnlyFilteredObjects
                |     attribute.
                | 
                |     A TRUE value indicates that the Only Filtered objects will be shown in
                |     Search Results

        :rtype: bool
        """

        return self.mfg_hub_setting_att.ShowOnlyFilteredObjects

    @show_only_filtered_objects.setter
    def show_only_filtered_objects(self, value: bool):
        """
        :param bool value:
        """

        self.mfg_hub_setting_att.ShowOnlyFilteredObjects = value

    def get_append_context_chk_b_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAppendContextChkBInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AppendContextChkB
                |     parameter.
                |     Role:Retrieves the state of the AppendContextChkB parameter in the current
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
        return self.mfg_hub_setting_att.GetAppendContextChkBInfo(io_admin_level, io_locked)

    def get_apply_label_eff_to_alt_child_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetApplyLabelEffToAltChildInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ApplyLabelEffToAltChild
                |     parameter.
                |     Role:Retrieves the state of the ApplyLabelEffToAltChild parameter in the
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
        return self.mfg_hub_setting_att.GetApplyLabelEffToAltChildInfo(io_admin_level, io_locked)

    def get_auto_load_mfg_ctx_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAutoLoadMfgCtxInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AutoLoadMfgCtx
                |     parameter.
                |     Role:Retrieves the state of the AutoLoadMfgCtx parameter in the current
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
        return self.mfg_hub_setting_att.GetAutoLoadMfgCtxInfo(io_admin_level, io_locked)

    def get_auto_load_srv_mfg_ctx_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAutoLoadSrvMfgCtxInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AutoLoadSrvMfgCtx
                |     parameter.
                |     Role:Retrieves the state of the AutoLoadSrvMfgCtx parameter in the current
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
        return self.mfg_hub_setting_att.GetAutoLoadSrvMfgCtxInfo(io_admin_level, io_locked)

    def get_auto_load_vol_ctx_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAutoLoadVolCtxInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AutoLoadVolCtx
                |     parameter.
                |     Role:Retrieves the state of the AutoLoadVolCtx parameter in the current
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
        return self.mfg_hub_setting_att.GetAutoLoadVolCtxInfo(io_admin_level, io_locked)

    def get_disable_shape_roll_up_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDisableShapeRollUpInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DisableShapeRollUp
                |     parameter.
                |     Role:Retrieves the state of the DisableShapeRollUp parameter in the current
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
        return self.mfg_hub_setting_att.GetDisableShapeRollUpInfo(io_admin_level, io_locked)

    def get_issue_repository_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetIssueRepositoryPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves the state of the IssueRepositoryPath parameter.
                | 
                |     Parameters:
                | 
                |         oInfo
                |             Address of an object CATSettingInfo. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.mfg_hub_setting_att.GetIssueRepositoryPathInfo(io_admin_level, io_locked)

    def get_link_send_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLinkSendModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves the state of the LinkSendMode parameter.
                | 
                |     Parameters:
                | 
                |         oInfo
                |             Address of an object CATSettingInfo. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.mfg_hub_setting_att.GetLinkSendModeInfo(io_admin_level, io_locked)

    def get_load_3d_state_and_pos_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoad3dStateAndPosInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Load3dStateAndPos
                |     parameter.
                |     Role:Retrieves the state of the Load3dStateAndPos parameter in the current
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
        return self.mfg_hub_setting_att.GetLoad3dStateAndPosInfo(io_admin_level, io_locked)

    def get_load_all_child_proc_mfg_ctx_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadAllChildProcMfgCtxInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadAllChildProcMfgCtx
                |     parameter.
                |     Role:Retrieves the state of the LoadAllChildProcMfgCtx parameter in the
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
        return self.mfg_hub_setting_att.GetLoadAllChildProcMfgCtxInfo(io_admin_level, io_locked)

    def get_load_assoc_prd_res_child_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadAssocPrdResChildInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadAssocPrdResChild
                |     parameter.
                |     Role:Retrieves the state of the LoadAssocPrdResChild parameter in the
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
        return self.mfg_hub_setting_att.GetLoadAssocPrdResChildInfo(io_admin_level, io_locked)

    def get_load_child_proc_mfg_ctx_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadChildProcMfgCtxInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadChildProcMfgCtx
                |     parameter.
                |     Role:Retrieves the state of the LoadChildProcMfgCtx parameter in the
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
        return self.mfg_hub_setting_att.GetLoadChildProcMfgCtxInfo(io_admin_level, io_locked)

    def get_load_ctx_with_file_geometry_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadCtxWithFileGeometryInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadCtxWithFileGeometry
                |     parameter.
                |     Role:Retrieves the state of the LoadCtxWithFileGeometry parameter in the
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
        return self.mfg_hub_setting_att.GetLoadCtxWithFileGeometryInfo(io_admin_level, io_locked)

    def get_load_disp_mfg_ctx_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadDispMfgCtxInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadDispMfgCtx
                |     parameter.
                |     Role:Retrieves the state of the LoadDispMfgCtx parameter in the current
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
        return self.mfg_hub_setting_att.GetLoadDispMfgCtxInfo(io_admin_level, io_locked)

    def get_load_duplicates_in_context_tree_chk_b_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadDuplicatesInContextTreeChkBInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadDuplicatesChkB
                |     parameter.
                |     Role:Retrieves the state of the LoadDuplicatesChkB parameter in the current
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
        return self.mfg_hub_setting_att.GetLoadDuplicatesInContextTreeChkBInfo(io_admin_level, io_locked)

    def get_load_env_geom_from_en_vdb_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadENVGeomFromENVdbInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadENVGeomFromENVdb
                |     parameter.
                |     Role:Retrieves the state of the LoadENVGeomFromENVdb parameter in the
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
        return self.mfg_hub_setting_att.GetLoadENVGeomFromENVdbInfo(io_admin_level, io_locked)

    def get_load_feed_proc_mfg_ctx_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadFeedProcMfgCtxInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadFeedProcMfgCtx
                |     parameter.
                |     Role:Retrieves the state of the LoadFeedProcMfgCtx parameter in the current
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
        return self.mfg_hub_setting_att.GetLoadFeedProcMfgCtxInfo(io_admin_level, io_locked)

    def get_load_mfg_assmbly_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadMfgAssmblyInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadMfgAssmbly
                |     parameter.
                |     Role:Retrieves the state of the LoadMfgAssmbly parameter in the current
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
        return self.mfg_hub_setting_att.GetLoadMfgAssmblyInfo(io_admin_level, io_locked)

    def get_load_mfg_kits_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadMfgKitsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadMfgKits
                |     parameter.
                |     Role:Retrieves the state of the LoadMfgKits parameter in the current
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
        return self.mfg_hub_setting_att.GetLoadMfgKitsInfo(io_admin_level, io_locked)

    def get_load_pss_data_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadPSSDataInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadPSSData
                |     parameter.
                |     Role:Retrieves the state of the LoadPSSData parameter in the current
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
        return self.mfg_hub_setting_att.GetLoadPSSDataInfo(io_admin_level, io_locked)

    def get_load_prd_res_user_attribs_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadPrdResUserAttribsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadPrdResUserAttribs
                |     parameter.
                |     Role:Retrieves the state of the LoadPrdResUserAttribs parameter in the
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
        return self.mfg_hub_setting_att.GetLoadPrdResUserAttribsInfo(io_admin_level, io_locked)

    def get_load_res_geo_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadResGeoInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadResGeo
                |     parameter.
                |     Role:Retrieves the state of the LoadResGeo parameter in the current
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
        return self.mfg_hub_setting_att.GetLoadResGeoInfo(io_admin_level, io_locked)

    def get_load_unconstrained_mfg_ctx_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadUnconstrainedMfgCtxInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LoadUnconstrainedMfgCtx
                |     parameter.
                |     Role:Retrieves the state of the LoadUnconstrainedMfgCtx parameter in the
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
        return self.mfg_hub_setting_att.GetLoadUnconstrainedMfgCtxInfo(io_admin_level, io_locked)

    def get_lock_assigned_prd_on_load_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLockAssignedPrdOnLoadInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LockAssignedPrdOnLoad
                |     parameter.
                |     Role:Retrieves the state of the LockAssignedPrdOnLoad parameter in the
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
        return self.mfg_hub_setting_att.GetLockAssignedPrdOnLoadInfo(io_admin_level, io_locked)

    def get_mail_client_launch_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMailClientLaunchModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves the state of the MailClientLaunchMode parameter.
                | 
                |     Parameters:
                | 
                |         oInfo
                |             Address of an object CATSettingInfo. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.mfg_hub_setting_att.GetMailClientLaunchModeInfo(io_admin_level, io_locked)

    def get_mfg_ctx_prev_proc_relation_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMfgCtxPrevProcRelationTypeInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment information for the MfgCtxPrevProcRelationType
                |     parameter
                |     Role:Retrieves the state of the MfgCtxPrevProcRelationType parameter in the
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
        return self.mfg_hub_setting_att.GetMfgCtxPrevProcRelationTypeInfo(io_admin_level, io_locked)

    def get_only_load_ctx_with_geometry_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOnlyLoadCtxWithGeometryInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the OnlyLoadCtxWithGeometry
                |     parameter.
                |     Role:Retrieves the state of the OnlyLoadCtxWithGeometry parameter in the
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
        return self.mfg_hub_setting_att.GetOnlyLoadCtxWithGeometryInfo(io_admin_level, io_locked)

    def get_open_mode_for_load_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOpenModeForLoadInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the OpenModeForLoad
                |     parameter.
                |     Role:Retrieves the value of the OpenModeForLoad parameter in the current
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
        return self.mfg_hub_setting_att.GetOpenModeForLoadInfo(io_admin_level, io_locked)

    def get_pack_and_go_repository_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPackAndGoRepositoryPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves the state of the PackAndGoRepositoryPath
                |     parameter.
                | 
                |     Parameters:
                | 
                |         oInfo
                |             Address of an object CATSettingInfo. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.mfg_hub_setting_att.GetPackAndGoRepositoryPathInfo(io_admin_level, io_locked)

    def get_post_load_script_option_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPostLoadScriptOptionInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PostLoadScriptOption
                |     parameter.
                |     Role:Retrieves the state of the PostLoadScriptOption parameter in the
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
        return self.mfg_hub_setting_att.GetPostLoadScriptOptionInfo(io_admin_level, io_locked)

    def get_post_load_script_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPostLoadScriptPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves the state of the PostLoadScriptPath parameter.
                | 
                |     Parameters:
                | 
                |         oInfo
                |             Address of an object CATSettingInfo. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.mfg_hub_setting_att.GetPostLoadScriptPathInfo(io_admin_level, io_locked)

    def get_post_load_vba_module_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPostLoadVBAModuleInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves the state of the PostLoadVBAModule parameter.
                | 
                |     Parameters:
                | 
                |         oInfo
                |             Address of an object CATSettingInfo. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.mfg_hub_setting_att.GetPostLoadVBAModuleInfo(io_admin_level, io_locked)

    def get_prev_proc_parse_type_for_mfg_ctx_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPrevProcParseTypeForMfgCtxInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PrevProcParseTypeForMfgCtx
                |     parameter.
                |     Role:Retrieves the state of the PrevProcParseTypeForMfgCtx parameter in the
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
        return self.mfg_hub_setting_att.GetPrevProcParseTypeForMfgCtxInfo(io_admin_level, io_locked)

    def get_proc_prod_relations_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProcProdRelationsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ProcProdRelations
                |     parameter.
                |     Role:Retrieves the state of the ProcProdRelations parameter in the current
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
        return self.mfg_hub_setting_att.GetProcProdRelationsInfo(io_admin_level, io_locked)

    def get_proc_res_relations_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProcResRelationsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ProcResRelations
                |     parameter.
                |     Role:Retrieves the state of the ProcResRelations parameter in the current
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
        return self.mfg_hub_setting_att.GetProcResRelationsInfo(io_admin_level, io_locked)

    def get_rmv_not_assgn_prd_res_on_sync_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRmvNotAssgnPrdResOnSyncInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RmvNotAssgnPrdResOnSync
                |     parameter.
                |     Role:Retrieves the state of the RmvNotAssgnPrdResOnSync parameter in the
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
        return self.mfg_hub_setting_att.GetRmvNotAssgnPrdResOnSyncInfo(io_admin_level, io_locked)

    def get_save_control_flow_in_pro_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSaveControlFlowInPROModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SaveControlFlowInPROMode
                |     parameter.
                |     Role:Retrieves the state of the SaveControlFlowInPROMode parameter in the
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
        return self.mfg_hub_setting_att.GetSaveControlFlowInPROModeInfo(io_admin_level, io_locked)

    def get_save_ppr_no_detailing_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSavePPRNoDetailingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SavePPRNoDetailing
                |     parameter.
                |     Role:Retrieves the state of the SavePPRNoDetailing parameter in the current
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
        return self.mfg_hub_setting_att.GetSavePPRNoDetailingInfo(io_admin_level, io_locked)

    def get_save_relation_to_un_exposed_part_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSaveRelationToUnExposedPartInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SaveRelationToUnExposedPart
                |     parameter.
                |     Role:Retrieves the state of the SaveRelationToUnExposedPart parameter in
                |     the current environment.
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
        return self.mfg_hub_setting_att.GetSaveRelationToUnExposedPartInfo(io_admin_level, io_locked)

    def get_save_show_effctvt_panel_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSaveShowEffctvtPanelInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SaveShowEffctvtPanel
                |     parameter.
                |     Role:Retrieves the state of the SaveShowEffctvtPanel parameter in the
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
        return self.mfg_hub_setting_att.GetSaveShowEffctvtPanelInfo(io_admin_level, io_locked)

    def get_save_v5_calc_time_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSaveV5CalcTimeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SaveV5CalcTime
                |     parameter.
                |     Role:Retrieves the state of the SaveV5CalcTime parameter in the current
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
        return self.mfg_hub_setting_att.GetSaveV5CalcTimeInfo(io_admin_level, io_locked)

    def get_show_only_filtered_objects_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetShowOnlyFilteredObjectsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ShowOnlyFilteredObjects
                |     parameter.
                |     Role:Retrieves the state of the ShowOnlyFilteredObjects parameter in the
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
        return self.mfg_hub_setting_att.GetShowOnlyFilteredObjectsInfo(io_admin_level, io_locked)

    def set_append_context_chk_b_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAppendContextChkBLock(boolean iLocked)
                | 
                |     Locks or unlocks the AppendContextChkB parameter.
                |     Role:Locks or unlocks the AppendContextChkB parameter if it is possible in
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
        return self.mfg_hub_setting_att.SetAppendContextChkBLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_append_context_chk_b_lock'
        # # vba_code = """
        # # Public Function set_append_context_chk_b_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetAppendContextChkBLock iLocked
        # #     set_append_context_chk_b_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_apply_label_eff_to_alt_child_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetApplyLabelEffToAltChildLock(boolean iLocked)
                | 
                |     Locks or unlocks the ApplyLabelEffToAltChild parameter.
                |     Role:Locks or unlocks the ApplyLabelEffToAltChild parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.mfg_hub_setting_att.SetApplyLabelEffToAltChildLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_apply_label_eff_to_alt_child_lock'
        # # vba_code = """
        # # Public Function set_apply_label_eff_to_alt_child_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetApplyLabelEffToAltChildLock iLocked
        # #     set_apply_label_eff_to_alt_child_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_auto_load_mfg_ctx_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAutoLoadMfgCtxLock(boolean iLocked)
                | 
                |     Locks or unlocks the AutoLoadMfgCtx parameter.
                |     Role:Locks or unlocks the AutoLoadMfgCtx parameter if it is possible in the
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
        return self.mfg_hub_setting_att.SetAutoLoadMfgCtxLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auto_load_mfg_ctx_lock'
        # # vba_code = """
        # # Public Function set_auto_load_mfg_ctx_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetAutoLoadMfgCtxLock iLocked
        # #     set_auto_load_mfg_ctx_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_auto_load_srv_mfg_ctx_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAutoLoadSrvMfgCtxLock(boolean iLocked)
                | 
                |     Locks or unlocks the AutoLoadSrvMfgCtx parameter.
                |     Role:Locks or unlocks the AutoLoadSrvMfgCtx parameter if it is possible in
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
        return self.mfg_hub_setting_att.SetAutoLoadSrvMfgCtxLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auto_load_srv_mfg_ctx_lock'
        # # vba_code = """
        # # Public Function set_auto_load_srv_mfg_ctx_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetAutoLoadSrvMfgCtxLock iLocked
        # #     set_auto_load_srv_mfg_ctx_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_auto_load_vol_ctx_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAutoLoadVolCtxLock(boolean iLocked)
                | 
                |     Locks or unlocks the AutoLoadVolCtx parameter.
                |     Role:Locks or unlocks the AutoLoadVolCtx parameter if it is possible in the
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
        return self.mfg_hub_setting_att.SetAutoLoadVolCtxLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auto_load_vol_ctx_lock'
        # # vba_code = """
        # # Public Function set_auto_load_vol_ctx_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetAutoLoadVolCtxLock iLocked
        # #     set_auto_load_vol_ctx_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_disable_shape_roll_up_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDisableShapeRollUpLock(boolean iLocked)
                | 
                |     Locks or unlocks the DisableShapeRollUp parameter.
                |     Role:Locks or unlocks the DisableShapeRollUp parameter if it is possible in
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
        return self.mfg_hub_setting_att.SetDisableShapeRollUpLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_disable_shape_roll_up_lock'
        # # vba_code = """
        # # Public Function set_disable_shape_roll_up_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetDisableShapeRollUpLock iLocked
        # #     set_disable_shape_roll_up_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_issue_repository_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetIssueRepositoryPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the IssueRepositoryPath parameter.
                |     Role: Locks or unlocks the IssueRepositoryPath parameter if the operation
                |     is allowed in the current administrated environment. In user mode this method
                |     will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.mfg_hub_setting_att.SetIssueRepositoryPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_issue_repository_path_lock'
        # # vba_code = """
        # # Public Function set_issue_repository_path_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetIssueRepositoryPathLock iLocked
        # #     set_issue_repository_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_link_send_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLinkSendModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the LinkSendMode parameter.
                |     Role: Locks or unlocks the LinkSendMode parameter if the operation is
                |     allowed in the current administrated environment. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.mfg_hub_setting_att.SetLinkSendModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_link_send_mode_lock'
        # # vba_code = """
        # # Public Function set_link_send_mode_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLinkSendModeLock iLocked
        # #     set_link_send_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_3d_state_and_pos_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoad3dStateAndPosLock(boolean iLocked)
                | 
                |     Locks or unlocks the Load3dStateAndPos parameter.
                |     Role:Locks or unlocks the Load3dStateAndPos parameter if it is possible in
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
        return self.mfg_hub_setting_att.SetLoad3dStateAndPosLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load3d_state_and_pos_lock'
        # # vba_code = """
        # # Public Function set_load3d_state_and_pos_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoad3dStateAndPosLock iLocked
        # #     set_load3d_state_and_pos_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_all_child_proc_mfg_ctx_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadAllChildProcMfgCtxLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadAllChildProcMfgCtx parameter.
                |     Role:Locks or unlocks the LoadAllChildProcMfgCtx parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.mfg_hub_setting_att.SetLoadAllChildProcMfgCtxLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_all_child_proc_mfg_ctx_lock'
        # # vba_code = """
        # # Public Function set_load_all_child_proc_mfg_ctx_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadAllChildProcMfgCtxLock iLocked
        # #     set_load_all_child_proc_mfg_ctx_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_assoc_prd_res_child_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadAssocPrdResChildLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadAssocPrdResChild parameter.
                |     Role:Locks or unlocks the LoadAssocPrdResChild parameter if it is possible
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
        return self.mfg_hub_setting_att.SetLoadAssocPrdResChildLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_assoc_prd_res_child_lock'
        # # vba_code = """
        # # Public Function set_load_assoc_prd_res_child_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadAssocPrdResChildLock iLocked
        # #     set_load_assoc_prd_res_child_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_child_proc_mfg_ctx_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadChildProcMfgCtxLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadChildProcMfgCtx parameter.
                |     Role:Locks or unlocks the LoadChildProcMfgCtx parameter if it is possible
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
        return self.mfg_hub_setting_att.SetLoadChildProcMfgCtxLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_child_proc_mfg_ctx_lock'
        # # vba_code = """
        # # Public Function set_load_child_proc_mfg_ctx_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadChildProcMfgCtxLock iLocked
        # #     set_load_child_proc_mfg_ctx_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_ctx_with_file_geometry_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadCtxWithFileGeometryLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadCtxWithFileGeometry parameter.
                |     Role:Locks or unlocks the LoadCtxWithFileGeometry parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.mfg_hub_setting_att.SetLoadCtxWithFileGeometryLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_ctx_with_file_geometry_lock'
        # # vba_code = """
        # # Public Function set_load_ctx_with_file_geometry_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadCtxWithFileGeometryLock iLocked
        # #     set_load_ctx_with_file_geometry_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_disp_mfg_ctx_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadDispMfgCtxLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadDispMfgCtx parameter.
                |     Role:Locks or unlocks the LoadDispMfgCtx parameter if it is possible in the
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
        return self.mfg_hub_setting_att.SetLoadDispMfgCtxLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_disp_mfg_ctx_lock'
        # # vba_code = """
        # # Public Function set_load_disp_mfg_ctx_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadDispMfgCtxLock iLocked
        # #     set_load_disp_mfg_ctx_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_duplicates_in_context_tree_chk_b_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadDuplicatesInContextTreeChkBLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the LoadDuplicatesChkB parameter.
                |     Role:Locks or unlocks the LoadDuplicatesChkB parameter if it is possible in
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
        return self.mfg_hub_setting_att.SetLoadDuplicatesInContextTreeChkBLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_duplicates_in_context_tree_chk_b_lock'
        # # vba_code = """
        # # Public Function set_load_duplicates_in_context_tree_chk_b_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadDuplicatesInContextTreeChkBLock iLocked
        # #     set_load_duplicates_in_context_tree_chk_b_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_env_geom_from_en_vdb_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadENVGeomFromENVdbLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadENVGeomFromENVdb parameter.
                |     Role:Locks or unlocks the LoadENVGeomFromENVdb parameter if it is possible
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
        return self.mfg_hub_setting_att.SetLoadENVGeomFromENVdbLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_env_geom_from_en_vdb_lock'
        # # vba_code = """
        # # Public Function set_load_env_geom_from_en_vdb_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadENVGeomFromENVdbLock iLocked
        # #     set_load_env_geom_from_en_vdb_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_feed_proc_mfg_ctx_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadFeedProcMfgCtxLock(boolean iLocked)
                | 
                |     Locks or unlocks the SaveV5CalcTime parameter.
                |     Role:Locks or unlocks the SaveV5CalcTime parameter if it is possible in the
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
        return self.mfg_hub_setting_att.SetLoadFeedProcMfgCtxLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_feed_proc_mfg_ctx_lock'
        # # vba_code = """
        # # Public Function set_load_feed_proc_mfg_ctx_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadFeedProcMfgCtxLock iLocked
        # #     set_load_feed_proc_mfg_ctx_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_mfg_assmbly_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadMfgAssmblyLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadMfgAssmbly parameter.
                |     Role:Locks or unlocks the LoadMfgAssmbly parameter if it is possible in the
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
        return self.mfg_hub_setting_att.SetLoadMfgAssmblyLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_mfg_assmbly_lock'
        # # vba_code = """
        # # Public Function set_load_mfg_assmbly_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadMfgAssmblyLock iLocked
        # #     set_load_mfg_assmbly_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_mfg_kits_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadMfgKitsLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadMfgKits parameter.
                |     Role:Locks or unlocks the LoadMfgKits parameter if it is possible in the
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
        return self.mfg_hub_setting_att.SetLoadMfgKitsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_mfg_kits_lock'
        # # vba_code = """
        # # Public Function set_load_mfg_kits_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadMfgKitsLock iLocked
        # #     set_load_mfg_kits_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_pss_data_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadPSSDataLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadPSSData parameter.
                |     Role:Locks or unlocks the LoadPSSData parameter if it is possible in the
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
        return self.mfg_hub_setting_att.SetLoadPSSDataLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_pss_data_lock'
        # # vba_code = """
        # # Public Function set_load_pss_data_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadPSSDataLock iLocked
        # #     set_load_pss_data_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_prd_res_user_attribs_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadPrdResUserAttribsLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadPrdResUserAttribs parameter.
                |     Role:Locks or unlocks the LoadPrdResUserAttribs parameter if it is possible
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
        return self.mfg_hub_setting_att.SetLoadPrdResUserAttribsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_prd_res_user_attribs_lock'
        # # vba_code = """
        # # Public Function set_load_prd_res_user_attribs_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadPrdResUserAttribsLock iLocked
        # #     set_load_prd_res_user_attribs_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_res_geo_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadResGeoLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadResGeo parameter.
                |     Role:Locks or unlocks the LoadResGeo parameter if it is possible in the
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
        return self.mfg_hub_setting_att.SetLoadResGeoLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_res_geo_lock'
        # # vba_code = """
        # # Public Function set_load_res_geo_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadResGeoLock iLocked
        # #     set_load_res_geo_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_unconstrained_mfg_ctx_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLoadUnconstrainedMfgCtxLock(boolean iLocked)
                | 
                |     Locks or unlocks the LoadUnconstrainedMfgCtx parameter.
                |     Role:Locks or unlocks the LoadUnconstrainedMfgCtx parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.mfg_hub_setting_att.SetLoadUnconstrainedMfgCtxLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_load_unconstrained_mfg_ctx_lock'
        # # vba_code = """
        # # Public Function set_load_unconstrained_mfg_ctx_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLoadUnconstrainedMfgCtxLock iLocked
        # #     set_load_unconstrained_mfg_ctx_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_lock_assigned_prd_on_load_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLockAssignedPrdOnLoadLock(boolean iLocked)
                | 
                |     Locks or unlocks the LockAssignedPrdOnLoad parameter.
                |     Role:Locks or unlocks the LockAssignedPrdOnLoad parameter if it is possible
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
        return self.mfg_hub_setting_att.SetLockAssignedPrdOnLoadLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_lock_assigned_prd_on_load_lock'
        # # vba_code = """
        # # Public Function set_lock_assigned_prd_on_load_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetLockAssignedPrdOnLoadLock iLocked
        # #     set_lock_assigned_prd_on_load_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_mail_client_launch_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMailClientLaunchModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the MailClientLaunchMode parameter.
                |     Role: Locks or unlocks the MailClientLaunchMode parameter if the operation
                |     is allowed in the current administrated environment. In user mode this method
                |     will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.mfg_hub_setting_att.SetMailClientLaunchModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_mail_client_launch_mode_lock'
        # # vba_code = """
        # # Public Function set_mail_client_launch_mode_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetMailClientLaunchModeLock iLocked
        # #     set_mail_client_launch_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_mfg_ctx_prev_proc_relation_type_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMfgCtxPrevProcRelationTypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the GetMfgCtxPrevProcRelationType
                |     parameter.
                |     Role:Locks or unlocks the GetMfgCtxPrevProcRelationType parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.mfg_hub_setting_att.SetMfgCtxPrevProcRelationTypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_mfg_ctx_prev_proc_relation_type_lock'
        # # vba_code = """
        # # Public Function set_mfg_ctx_prev_proc_relation_type_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetMfgCtxPrevProcRelationTypeLock iLocked
        # #     set_mfg_ctx_prev_proc_relation_type_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_only_load_ctx_with_geometry_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOnlyLoadCtxWithGeometryLock(boolean iLocked)
                | 
                |     Locks or unlocks the OnlyLoadCtxWithGeometry parameter.
                |     Role:Locks or unlocks the OnlyLoadCtxWithGeometry parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.mfg_hub_setting_att.SetOnlyLoadCtxWithGeometryLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_only_load_ctx_with_geometry_lock'
        # # vba_code = """
        # # Public Function set_only_load_ctx_with_geometry_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetOnlyLoadCtxWithGeometryLock iLocked
        # #     set_only_load_ctx_with_geometry_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_open_mode_for_load_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOpenModeForLoadLock(boolean iLocked)
                | 
                |     Locks or unlocks the OpenModeForLoad parameter.
                |     Role:Locks or unlocks the OpenModeForLoad parameter if it is possible in
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
        return self.mfg_hub_setting_att.SetOpenModeForLoadLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_open_mode_for_load_lock'
        # # vba_code = """
        # # Public Function set_open_mode_for_load_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetOpenModeForLoadLock iLocked
        # #     set_open_mode_for_load_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pack_and_go_repository_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPackAndGoRepositoryPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the PackAndGoRepositoryPath parameter.
                |     Role: Locks or unlocks the PackAndGoRepositoryPath parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.mfg_hub_setting_att.SetPackAndGoRepositoryPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pack_and_go_repository_path_lock'
        # # vba_code = """
        # # Public Function set_pack_and_go_repository_path_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetPackAndGoRepositoryPathLock iLocked
        # #     set_pack_and_go_repository_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_post_load_script_option_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPostLoadScriptOptionLock(boolean iLocked)
                | 
                |     Locks or unlocks the PostLoadScriptOption parameter.
                |     Role:Locks or unlocks the PostLoadScriptOption parameter if it is possible
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
        return self.mfg_hub_setting_att.SetPostLoadScriptOptionLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_post_load_script_option_lock'
        # # vba_code = """
        # # Public Function set_post_load_script_option_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetPostLoadScriptOptionLock iLocked
        # #     set_post_load_script_option_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_post_load_script_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPostLoadScriptPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the PostLoadScriptPath parameter.
                |     Role: Locks or unlocks the PostLoadScriptPath parameter if the operation is
                |     allowed in the current administrated environment. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.mfg_hub_setting_att.SetPostLoadScriptPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_post_load_script_path_lock'
        # # vba_code = """
        # # Public Function set_post_load_script_path_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetPostLoadScriptPathLock iLocked
        # #     set_post_load_script_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_post_load_vba_module_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPostLoadVBAModuleLock(boolean iLocked)
                | 
                |     Locks or unlocks the PostLoadVBAModule parameter.
                |     Role: Locks or unlocks the PostLoadVBAModule parameter if the operation is
                |     allowed in the current administrated environment. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.mfg_hub_setting_att.SetPostLoadVBAModuleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_post_load_vba_module_lock'
        # # vba_code = """
        # # Public Function set_post_load_vba_module_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetPostLoadVBAModuleLock iLocked
        # #     set_post_load_vba_module_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_prev_proc_parse_type_for_mfg_ctx_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPrevProcParseTypeForMfgCtxLock(boolean iLocked)
                | 
                |     Locks or unlocks the PrevProcParseTypeForMfgCtx parameter.
                |     Role:Locks or unlocks the PrevProcParseTypeForMfgCtx parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.mfg_hub_setting_att.SetPrevProcParseTypeForMfgCtxLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_prev_proc_parse_type_for_mfg_ctx_lock'
        # # vba_code = """
        # # Public Function set_prev_proc_parse_type_for_mfg_ctx_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetPrevProcParseTypeForMfgCtxLock iLocked
        # #     set_prev_proc_parse_type_for_mfg_ctx_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_proc_prod_relations_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProcProdRelationsLock(boolean iLocked)
                | 
                |     Locks or unlocks the ProcProdRelations parameter.
                |     Role:Locks or unlocks the ProcProdRelations parameter if it is possible in
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
        return self.mfg_hub_setting_att.SetProcProdRelationsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_proc_prod_relations_lock'
        # # vba_code = """
        # # Public Function set_proc_prod_relations_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetProcProdRelationsLock iLocked
        # #     set_proc_prod_relations_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_proc_res_relations_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProcResRelationsLock(boolean iLocked)
                | 
                |     Locks or unlocks the ProcResRelations parameter.
                |     Role:Locks or unlocks the ProcResRelations parameter if it is possible in
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
        return self.mfg_hub_setting_att.SetProcResRelationsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_proc_res_relations_lock'
        # # vba_code = """
        # # Public Function set_proc_res_relations_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetProcResRelationsLock iLocked
        # #     set_proc_res_relations_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rmv_not_assgn_prd_res_on_sync_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRmvNotAssgnPrdResOnSyncLock(boolean iLocked)
                | 
                |     Locks or unlocks the RmvNotAssgnPrdResOnSync parameter.
                |     Role:Locks or unlocks the RmvNotAssgnPrdResOnSync parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.mfg_hub_setting_att.SetRmvNotAssgnPrdResOnSyncLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rmv_not_assgn_prd_res_on_sync_lock'
        # # vba_code = """
        # # Public Function set_rmv_not_assgn_prd_res_on_sync_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetRmvNotAssgnPrdResOnSyncLock iLocked
        # #     set_rmv_not_assgn_prd_res_on_sync_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_save_control_flow_in_pro_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSaveControlFlowInPROModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the SaveControlFlowInPROMode parameter.
                |     Role:Locks or unlocks the SaveControlFlowInPROMode parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.mfg_hub_setting_att.SetSaveControlFlowInPROModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_save_control_flow_in_pro_mode_lock'
        # # vba_code = """
        # # Public Function set_save_control_flow_in_pro_mode_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetSaveControlFlowInPROModeLock iLocked
        # #     set_save_control_flow_in_pro_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_save_ppr_no_detailing_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSavePPRNoDetailingLock(boolean iLocked)
                | 
                |     Locks or unlocks the SavePPRNoDetailing parameter.
                |     Role:Locks or unlocks the SavePPRNoDetailing parameter if it is possible in
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
        return self.mfg_hub_setting_att.SetSavePPRNoDetailingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_save_ppr_no_detailing_lock'
        # # vba_code = """
        # # Public Function set_save_ppr_no_detailing_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetSavePPRNoDetailingLock iLocked
        # #     set_save_ppr_no_detailing_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_save_relation_to_un_exposed_part_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSaveRelationToUnExposedPartLock(boolean iLocked)
                | 
                |     Locks or unlocks the SaveRelationToUnExposedPart
                |     parameter.
                |     Role:Locks or unlocks the SaveRelationToUnExposedPart parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.mfg_hub_setting_att.SetSaveRelationToUnExposedPartLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_save_relation_to_un_exposed_part_lock'
        # # vba_code = """
        # # Public Function set_save_relation_to_un_exposed_part_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetSaveRelationToUnExposedPartLock iLocked
        # #     set_save_relation_to_un_exposed_part_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_save_show_effctvt_panel_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSaveShowEffctvtPanelLock(boolean iLocked)
                | 
                |     Locks or unlocks the SaveShowEffctvtPanel parameter.
                |     Role:Locks or unlocks the SaveShowEffctvtPanel parameter if it is possible
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
        return self.mfg_hub_setting_att.SetSaveShowEffctvtPanelLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_save_show_effctvt_panel_lock'
        # # vba_code = """
        # # Public Function set_save_show_effctvt_panel_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetSaveShowEffctvtPanelLock iLocked
        # #     set_save_show_effctvt_panel_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_save_v5_calc_time_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSaveV5CalcTimeLock(boolean iLocked)
                | 
                |     Locks or unlocks the SaveV5CalcTime parameter.
                |     Role:Locks or unlocks the SaveV5CalcTime parameter if it is possible in the
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
        return self.mfg_hub_setting_att.SetSaveV5CalcTimeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_save_v5_calc_time_lock'
        # # vba_code = """
        # # Public Function set_save_v5_calc_time_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetSaveV5CalcTimeLock iLocked
        # #     set_save_v5_calc_time_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_show_only_filtered_objects_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetShowOnlyFilteredObjectsLock(boolean iLocked)
                | 
                |     Locks or unlocks the ShowOnlyFilteredObjects parameter.
                |     Role:Locks or unlocks the ShowOnlyFilteredObjects parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.mfg_hub_setting_att.SetShowOnlyFilteredObjectsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_show_only_filtered_objects_lock'
        # # vba_code = """
        # # Public Function set_show_only_filtered_objects_lock(mfg_hub_setting_att)
        # #     Dim iLocked (2)
        # #     mfg_hub_setting_att.SetShowOnlyFilteredObjectsLock iLocked
        # #     set_show_only_filtered_objects_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MfgHubSettingAtt(name="{self.name}")'
