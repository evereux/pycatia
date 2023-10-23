#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class ViewCharacteristicCurvesSettingAtt(SettingController):
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
                |                         ViewCharacteristicCurvesSettingAtt
                | 
                | Represents the CATIA Sheet Metal Aerospace Display setting controller
                | object.
                | Role: The CATIA Sheet Metal Aerospace setting Display controller object deals
                | with the setting attributes displayed in the Aerospace Sheet Metal Design
                | Display property page. The Sheet Metal Aerospace Display property page manage
                | the visibility of Characteristic Curves in Folded and Unfolded view. THE
                | METHODS DEDICATED FOR SURFACIC FLANGE ARE USEFUL FOR BOTH SURFACIC FLANGE AND
                | SWEPT FLANGE.
                | Characteristic Curves summary :
                | BTLSupp 	Bend Tangent Line bounding the Support (Flange)
                | BTLFeat 	Bend Tangent Line bounding the Base Feature (Web or
                | Flange)
                | OML 	Outer Mold Line
                | OML2 	Second Outer Mold Line (Unfolded view)
                | IML 	Inner Mold Line
                | CLB 	Center Line of Bend
                | To access this property page:
                | 
                |     Click the Options command in the Tools menu
                |     Click + left of Mechanical Design to unfold the workbench
                |     list
                |     Click Display
                | 
                | The Sheet Metal Aerospace Display setting controller object can be retrieved as
                | an item of the setting controller collection using its name
                | "CATIStmViewCharacteristicCurvesSettingCtrl" as follows:
                | 
                |  Dim settingControllers1 As SettingControllers
                |  Set settingControllers1 = CATIA.SettingControllers
                |  Dim CATIAStmViewCharacteristicCurvesSettingAtt1 As
                |  SettingController
                |  Set CATIAStmViewCharacteristicCurvesSettingAtt1 = settingControllers1.Item("CATIStmViewCharacteristicCurvesSettingCtrl")
                |  
                | 
                | Note that there is NO default value : if a setting attribute is not set, the
                | corresponding check button will be unchecked and the setting attribute will
                | take the value "hidden" if the User clicks "OK" in the Display property page.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.view_characteristic_curves_setting_att = com_object

    @property
    def shm_view_fd_bead_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDBeadBTLFeat() As long
                | 
                |     Returns or sets SHMViewFDBeadBTLFeat setting parameter
                |     value.
                |     Role: The XXX SHMViewFDBeadBTLFeat parameter manage the visibility of the
                |     BTL Base Feature on a Bead in Folded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDBeadBTLFeat

    @shm_view_fd_bead_btl_feat.setter
    def shm_view_fd_bead_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDBeadBTLFeat = value

    @property
    def shm_view_fd_circ_stamp_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDCircStampBTLFeat() As long
                | 
                |     Returns or sets SHMViewFDCircStampBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFDCircStampBTLFeat setting parameter manage the visibility
                |     of the BTL Base Feature on a Circular Stamp in Folded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDCircStampBTLFeat

    @shm_view_fd_circ_stamp_btl_feat.setter
    def shm_view_fd_circ_stamp_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDCircStampBTLFeat = value

    @property
    def shm_view_fd_curve_stamp_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDCurveStampBTLFeat() As long
                | 
                |     Returns or sets SHMViewFDCurveStampBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFDCurveStampBTLFeat setting parameter manage the
                |     visibility of the BTL Base Feature on a Curve Stamp in Folded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDCurveStampBTLFeat

    @shm_view_fd_curve_stamp_btl_feat.setter
    def shm_view_fd_curve_stamp_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDCurveStampBTLFeat = value

    @property
    def shm_view_fd_flg_cut_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDFlgCutBTLFeat() As long
                | 
                |     Returns or sets SHMViewFDFlgCutBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFDFlgCutBTLFeat setting parameter manage the visibility of
                |     the BTL Base Feature on a Flanged Cutout in Folded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDFlgCutBTLFeat

    @shm_view_fd_flg_cut_btl_feat.setter
    def shm_view_fd_flg_cut_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDFlgCutBTLFeat = value

    @property
    def shm_view_fd_flg_cut_iml(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDFlgCutIML() As long
                | 
                |     Returns or sets SHMViewFDFlgCutIML setting parameter
                |     value.
                |     Role: The SHMViewFDFlgCutIML setting parameter manage the visibility of the
                |     IML on a Flanged Cutout in Folded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDFlgCutIML

    @shm_view_fd_flg_cut_iml.setter
    def shm_view_fd_flg_cut_iml(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDFlgCutIML = value

    @property
    def shm_view_fd_flg_cut_oml(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDFlgCutOML() As long
                | 
                |     Returns or sets SHMViewFDFlgCutOML setting parameter
                |     value.
                |     Role: The SHMViewFDFlgCutOML setting parameter manage the visibility of the
                |     OML on a Flanged Cutout in Folded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDFlgCutOML

    @shm_view_fd_flg_cut_oml.setter
    def shm_view_fd_flg_cut_oml(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDFlgCutOML = value

    @property
    def shm_view_fd_flg_hole_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDFlgHoleBTLFeat() As long
                | 
                |     Returns or sets SHMViewFDFlgHoleBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFDFlgHoleBTLFeat setting parameter manage the visibility
                |     of the BTL Base Feature on a Flanged Hole in Folded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDFlgHoleBTLFeat

    @shm_view_fd_flg_hole_btl_feat.setter
    def shm_view_fd_flg_hole_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDFlgHoleBTLFeat = value

    @property
    def shm_view_fd_flg_hole_iml(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDFlgHoleIML() As long
                | 
                |     Returns or sets SHMViewFDFlgHoleIML setting parameter
                |     value.
                |     Role: The SHMViewFDFlgHoleIML setting parameter manage the visibility of
                |     the IML on a Flanged Hole in Folded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDFlgHoleIML

    @shm_view_fd_flg_hole_iml.setter
    def shm_view_fd_flg_hole_iml(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDFlgHoleIML = value

    @property
    def shm_view_fd_flg_hole_oml(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDFlgHoleOML() As long
                | 
                |     Returns or sets SHMViewFDFlgHoleOML setting parameter
                |     value.
                |     Role: The SHMViewFDFlgHoleOML setting parameter manage the visibility of
                |     the OML on a Flanged Hole in Folded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDFlgHoleOML

    @shm_view_fd_flg_hole_oml.setter
    def shm_view_fd_flg_hole_oml(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDFlgHoleOML = value

    @property
    def shm_view_fd_other_stamp_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDOtherStampBTLFeat() As long
                | 
                |     Returns or sets SHMViewFDOtherStampBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFDOtherStampBTLFeat setting parameter manage the
                |     visibility of the BTL Base Feature on an other Stamp ( F&A -> Bridge, Louver
                |     ... ) in Folded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDOtherStampBTLFeat

    @shm_view_fd_other_stamp_btl_feat.setter
    def shm_view_fd_other_stamp_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDOtherStampBTLFeat = value

    @property
    def shm_view_fd_stiff_stamp_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDStiffStampBTLFeat() As long
                | 
                |     Returns or sets SHMViewFDStiffStampBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFDStiffStampBTLFeat setting parameter manage the
                |     visibility of the BTL Base Feature on a Stiffening Rib in Folded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDStiffStampBTLFeat

    @shm_view_fd_stiff_stamp_btl_feat.setter
    def shm_view_fd_stiff_stamp_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDStiffStampBTLFeat = value

    @property
    def shm_view_fd_surf_flg_btl_feat_bf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDSurfFlgBTLFeatBF() As long
                | 
                |     Returns or sets SHMViewFDSurfFlgBTLFeatBF setting parameter
                |     value.
                |     Role: The SHMViewFDSurfFlgBTLFeatBF setting parameter manage the visibility
                |     of the BTL Base Feature on a Surfacic Flange Brake formed in Folded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgBTLFeatBF

    @shm_view_fd_surf_flg_btl_feat_bf.setter
    def shm_view_fd_surf_flg_btl_feat_bf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgBTLFeatBF = value

    @property
    def shm_view_fd_surf_flg_btl_feat_hf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDSurfFlgBTLFeatHF() As long
                | 
                |     Returns or sets SHMViewFDSurfFlgBTLFeatHF setting parameter
                |     value.
                |     Role: The SHMViewFDSurfFlgBTLFeatHF setting parameter manage the visibility
                |     of the BTL Base Feature on a Surfacic Flange Hydro-Press formed in Folded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgBTLFeatHF

    @shm_view_fd_surf_flg_btl_feat_hf.setter
    def shm_view_fd_surf_flg_btl_feat_hf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgBTLFeatHF = value

    @property
    def shm_view_fd_surf_flg_btl_supp_bf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDSurfFlgBTLSuppBF() As long
                | 
                |     Returns or sets SHMViewFDSurfFlgBTLSuppBF setting parameter
                |     value.
                |     Role: The SHMViewFDSurfFlgBTLSuppBF setting parameter manage the visibility
                |     of the BTL Base Feature on a Surfacic Flange Brake formed in Folded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgBTLSuppBF

    @shm_view_fd_surf_flg_btl_supp_bf.setter
    def shm_view_fd_surf_flg_btl_supp_bf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgBTLSuppBF = value

    @property
    def shm_view_fd_surf_flg_btl_supp_hf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDSurfFlgBTLSuppHF() As long
                | 
                |     Returns or sets SHMViewFDSurfFlgBTLSuppHF setting parameter
                |     value.
                |     Role: The SHMViewFDSurfFlgBTLSuppHF setting parameter manage the visibility
                |     of the BTL Support on a Surfacic Flange Hydro-Press formed in Folded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgBTLSuppHF

    @shm_view_fd_surf_flg_btl_supp_hf.setter
    def shm_view_fd_surf_flg_btl_supp_hf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgBTLSuppHF = value

    @property
    def shm_view_fd_surf_flg_imlbf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDSurfFlgIMLBF() As long
                | 
                |     Returns or sets SHMViewFDSurfFlgIMLBF setting parameter
                |     value.
                |     Role: The SHMViewFDSurfFlgIMLBF setting parameter manage the visibility of
                |     the IML on a Surfacic Flange Brake formed in Folded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgIMLBF

    @shm_view_fd_surf_flg_imlbf.setter
    def shm_view_fd_surf_flg_imlbf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgIMLBF = value

    @property
    def shm_view_fd_surf_flg_imlhf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDSurfFlgIMLHF() As long
                | 
                |     Returns or sets SHMViewFDSurfFlgIMLHF setting parameter
                |     value.
                |     Role: The SHMViewFDSurfFlgIMLHF setting parameter manage the visibility of
                |     the IML on a Surfacic Flange Hydro-Press formed in Folded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgIMLHF

    @shm_view_fd_surf_flg_imlhf.setter
    def shm_view_fd_surf_flg_imlhf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgIMLHF = value

    @property
    def shm_view_fd_surf_flg_omlbf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDSurfFlgOMLBF() As long
                | 
                |     Returns or sets SHMViewFDSurfFlgOMLBF setting parameter
                |     value.
                |     Role: The SHMViewFDSurfFlgOMLBF setting parameter manage the visibility of
                |     the OML on a Surfacic Flange Brake formed in Folded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgOMLBF

    @shm_view_fd_surf_flg_omlbf.setter
    def shm_view_fd_surf_flg_omlbf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgOMLBF = value

    @property
    def shm_view_fd_surf_flg_omlhf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDSurfFlgOMLHF() As long
                | 
                |     Returns or sets SHMViewFDSurfFlgOMLHF setting parameter
                |     value.
                |     Role: The SHMViewFDSurfFlgOMLHF setting parameter manage the visibility of
                |     the OML on a Surfacic Flange Hydro-Press formed in Folded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgOMLHF

    @shm_view_fd_surf_flg_omlhf.setter
    def shm_view_fd_surf_flg_omlhf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDSurfFlgOMLHF = value

    @property
    def shm_view_fd_surf_stamp_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDSurfStampBTLFeat() As long
                | 
                |     Returns or sets SHMViewFDSurfStampBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFDSurfStampBTLFeat setting parameter manage the visibility
                |     of the BTL Base Feature on a Surface Stamp in Folded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDSurfStampBTLFeat

    @shm_view_fd_surf_stamp_btl_feat.setter
    def shm_view_fd_surf_stamp_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDSurfStampBTLFeat = value

    @property
    def shm_view_fd_user_stamp_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFDUserStampBTLFeat() As long
                | 
                |     Returns or sets SHMViewFDUserStampBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFDUserStampBTLFeat setting parameter manage the visibility
                |     of the BTL Base Feature on a User Stamp in Folded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFDUserStampBTLFeat

    @shm_view_fd_user_stamp_btl_feat.setter
    def shm_view_fd_user_stamp_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFDUserStampBTLFeat = value

    @property
    def shm_view_fp_bead_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPBeadBTLFeat() As long
                | 
                |     Returns or sets SHMViewFPBeadBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFPBeadBTLFeat setting parameter manage the visibility of
                |     the BTL Base Feature on a Bead in UnFolded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPBeadBTLFeat

    @shm_view_fp_bead_btl_feat.setter
    def shm_view_fp_bead_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPBeadBTLFeat = value

    @property
    def shm_view_fp_circ_stamp_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPCircStampBTLFeat() As long
                | 
                |     Returns or sets SHMViewFPCircStampBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFPCircStampBTLFeat setting parameter manage the visibility
                |     of the BTL Base Feature on a Circular Stamp in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPCircStampBTLFeat

    @shm_view_fp_circ_stamp_btl_feat.setter
    def shm_view_fp_circ_stamp_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPCircStampBTLFeat = value

    @property
    def shm_view_fp_curve_stamp_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPCurveStampBTLFeat() As long
                | 
                |     Returns or sets SHMViewFPCurveStampBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFPCurveStampBTLFeat setting parameter manage the
                |     visibility of the BTL Base Feature on a Curve Stamp in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPCurveStampBTLFeat

    @shm_view_fp_curve_stamp_btl_feat.setter
    def shm_view_fp_curve_stamp_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPCurveStampBTLFeat = value

    @property
    def shm_view_fp_flg_cut_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPFlgCutBTLFeat() As long
                | 
                |     Returns or sets SHMViewFPFlgCutBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFPFlgCutBTLFeat setting parameter manage the visibility of
                |     the BTL Base Feature on a Flanged Cutout in UnFolded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPFlgCutBTLFeat

    @shm_view_fp_flg_cut_btl_feat.setter
    def shm_view_fp_flg_cut_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPFlgCutBTLFeat = value

    @property
    def shm_view_fp_flg_cut_iml(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPFlgCutIML() As long
                | 
                |     Returns or sets SHMViewFPFlgCutIML setting parameter
                |     value.
                |     Role: The SHMViewFPFlgCutIML setting parameter manage the visibility of the
                |     IML on a Flanged Cutout in UnFolded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPFlgCutIML

    @shm_view_fp_flg_cut_iml.setter
    def shm_view_fp_flg_cut_iml(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPFlgCutIML = value

    @property
    def shm_view_fp_flg_cut_oml(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPFlgCutOML() As long
                | 
                |     Returns or sets SHMViewFPFlgCutOML setting parameter
                |     value.
                |     Role: The SHMViewFPFlgCutOML setting parameter manage the visibility of the
                |     OML on a Flanged Cutout in UnFolded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPFlgCutOML

    @shm_view_fp_flg_cut_oml.setter
    def shm_view_fp_flg_cut_oml(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPFlgCutOML = value

    @property
    def shm_view_fp_flg_hole_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPFlgHoleBTLFeat() As long
                | 
                |     Returns or sets SHMViewFPFlgHoleBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFPFlgHoleBTLFeat setting parameter manage the visibility
                |     of the BTL Base Feature on a Flanged Hole in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPFlgHoleBTLFeat

    @shm_view_fp_flg_hole_btl_feat.setter
    def shm_view_fp_flg_hole_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPFlgHoleBTLFeat = value

    @property
    def shm_view_fp_flg_hole_iml(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPFlgHoleIML() As long
                | 
                |     Returns or sets SHMViewFPFlgHoleIML setting parameter
                |     value.
                |     Role: The SHMViewFPFlgHoleIML setting parameter manage the visibility of
                |     the IML on a Flanged Hole in UnFolded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPFlgHoleIML

    @shm_view_fp_flg_hole_iml.setter
    def shm_view_fp_flg_hole_iml(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPFlgHoleIML = value

    @property
    def shm_view_fp_flg_hole_oml(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPFlgHoleOML() As long
                | 
                |     Returns or sets SHMViewFPFlgHoleOML setting parameter
                |     value.
                |     Role: The SHMViewFPFlgHoleOML setting parameter manage the visibility of
                |     the OML on a Flanged Hole in UnFolded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPFlgHoleOML

    @shm_view_fp_flg_hole_oml.setter
    def shm_view_fp_flg_hole_oml(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPFlgHoleOML = value

    @property
    def shm_view_fp_other_stamp_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPOtherStampBTLFeat() As long
                | 
                |     Returns or sets SHMViewFPOtherStampBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFPOtherStampBTLFeat setting parameter manage the
                |     visibility of the BTL Base Feature on an other Stamp ( F&A -> Bridge, Louver
                |     ... ) in UnFolded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPOtherStampBTLFeat

    @shm_view_fp_other_stamp_btl_feat.setter
    def shm_view_fp_other_stamp_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPOtherStampBTLFeat = value

    @property
    def shm_view_fp_stiff_stamp_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPStiffStampBTLFeat() As long
                | 
                |     Returns or sets SHMViewFPStiffStampBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFPStiffStampBTLFeat setting parameter manage the
                |     visibility of the BTL Base Feature on a Stiffening Rib in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPStiffStampBTLFeat

    @shm_view_fp_stiff_stamp_btl_feat.setter
    def shm_view_fp_stiff_stamp_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPStiffStampBTLFeat = value

    @property
    def shm_view_fp_surf_flg_btl_feat_bf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPSurfFlgBTLFeatBF() As long
                | 
                |     Returns or sets SHMViewFPSurfFlgBTLFeatBF setting parameter
                |     value.
                |     Role: The SHMViewFPSurfFlgBTLFeatBF setting parameter manage the visibility
                |     of the BTL Base Feature on a Surfacic Flange Brake formed in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgBTLFeatBF

    @shm_view_fp_surf_flg_btl_feat_bf.setter
    def shm_view_fp_surf_flg_btl_feat_bf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgBTLFeatBF = value

    @property
    def shm_view_fp_surf_flg_btl_feat_hf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPSurfFlgBTLFeatHF() As long
                | 
                |     Returns or sets SHMViewFPSurfFlgBTLFeatHF setting parameter
                |     value.
                |     Role: The SHMViewFPSurfFlgBTLFeatHF setting parameter manage the visibility
                |     of the BTL Base Feature on a Surfacic Flange Hydro-Press formed in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgBTLFeatHF

    @shm_view_fp_surf_flg_btl_feat_hf.setter
    def shm_view_fp_surf_flg_btl_feat_hf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgBTLFeatHF = value

    @property
    def shm_view_fp_surf_flg_btl_supp_bf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPSurfFlgBTLSuppBF() As long
                | 
                |     Returns or sets SHMViewFPSurfFlgBTLSuppBF setting parameter
                |     value.
                |     Role: The SHMViewFPSurfFlgBTLSuppBF setting parameter manage the visibility
                |     of the BTL Support on a Surfacic Flange Brake formed in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgBTLSuppBF

    @shm_view_fp_surf_flg_btl_supp_bf.setter
    def shm_view_fp_surf_flg_btl_supp_bf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgBTLSuppBF = value

    @property
    def shm_view_fp_surf_flg_btl_supp_hf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPSurfFlgBTLSuppHF() As long
                | 
                |     Returns or sets SHMViewFPSurfFlgBTLSuppHF setting parameter
                |     value.
                |     Role: The SHMViewFPSurfFlgBTLSuppHF setting parameter manage the visibility
                |     of the BTL Support on a Surfacic Flange Hydro-Press formed in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgBTLSuppHF

    @shm_view_fp_surf_flg_btl_supp_hf.setter
    def shm_view_fp_surf_flg_btl_supp_hf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgBTLSuppHF = value

    @property
    def shm_view_fp_surf_flg_clbbf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPSurfFlgCLBBF() As long
                | 
                |     Returns or sets SHMViewFPSurfFlgCLBBF setting parameter
                |     value.
                |     Role: The SHMViewFPSurfFlgCLBBF setting parameter manage the visibility of
                |     CLB on a Surfacic Flange Brake formed in UnFolded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgCLBBF

    @shm_view_fp_surf_flg_clbbf.setter
    def shm_view_fp_surf_flg_clbbf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgCLBBF = value

    @property
    def shm_view_fp_surf_flg_clbhf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPSurfFlgCLBHF() As long
                | 
                |     Returns or sets SHMViewFPSurfFlgCLBHF setting parameter
                |     value.
                |     Role: The SHMViewFPSurfFlgCLBHF setting parameter manage the visibility of
                |     CLB on a Surfacic Flange Hydro-Pressed formed in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgCLBHF

    @shm_view_fp_surf_flg_clbhf.setter
    def shm_view_fp_surf_flg_clbhf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgCLBHF = value

    @property
    def shm_view_fp_surf_flg_imlbf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPSurfFlgIMLBF() As long
                | 
                |     Returns or sets SHMViewFPSurfFlgIMLBF setting parameter
                |     value.
                |     Role: The SHMViewFPSurfFlgIMLBF setting parameter manage the visibility of
                |     the IML on a Surfacic Flange Brake formed in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgIMLBF

    @shm_view_fp_surf_flg_imlbf.setter
    def shm_view_fp_surf_flg_imlbf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgIMLBF = value

    @property
    def shm_view_fp_surf_flg_imlhf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPSurfFlgIMLHF() As long
                | 
                |     Returns or sets SHMViewFPSurfFlgIMLHF setting parameter
                |     value.
                |     Role: The SHMViewFPSurfFlgIMLHF setting parameter manage the visibility of
                |     the IML on a Surfacic Flange Hydro-Press formed in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgIMLHF

    @shm_view_fp_surf_flg_imlhf.setter
    def shm_view_fp_surf_flg_imlhf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgIMLHF = value

    @property
    def shm_view_fp_surf_flg_oml2_bf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPSurfFlgOML2BF() As long
                | 
                |     Returns or sets SHMViewFPSurfFlgOML2BF setting parameter
                |     value.
                |     Role: The SHMViewFPSurfFlgOML2BF setting parameter manage the visibility of
                |     he Second OML on a Surfacic Flange Brake formed in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgOML2BF

    @shm_view_fp_surf_flg_oml2_bf.setter
    def shm_view_fp_surf_flg_oml2_bf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgOML2BF = value

    @property
    def shm_view_fp_surf_flg_oml2_hf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPSurfFlgOML2HF() As long
                | 
                |     Returns or sets SHMViewFPSurfFlgOML2HF setting parameter
                |     value.
                |     Role: The SHMViewFPSurfFlgOML2HF setting parameter manage the visibility of
                |     the Second OML on a Surfacic Flange Hydro-Press formed in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgOML2HF

    @shm_view_fp_surf_flg_oml2_hf.setter
    def shm_view_fp_surf_flg_oml2_hf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgOML2HF = value

    @property
    def shm_view_fp_surf_flg_omlbf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPSurfFlgOMLBF() As long
                | 
                |     Returns or sets SHMViewFPSurfFlgOMLBF setting parameter
                |     value.
                |     Role: The SHMViewFPSurfFlgOMLBF setting parameter manage the visibility of
                |     the OML on a Surfacic Flange Brake formed in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgOMLBF

    @shm_view_fp_surf_flg_omlbf.setter
    def shm_view_fp_surf_flg_omlbf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgOMLBF = value

    @property
    def shm_view_fp_surf_flg_omlhf(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPSurfFlgOMLHF() As long
                | 
                |     Returns or sets SHMViewFPSurfFlgOMLHF setting parameter
                |     value.
                |     Role: The SHMViewFPSurfFlgOMLHF setting parameter manage the visibility of
                |     the OML on a Surfacic Flange Hydro-Press formed in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgOMLHF

    @shm_view_fp_surf_flg_omlhf.setter
    def shm_view_fp_surf_flg_omlhf(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPSurfFlgOMLHF = value

    @property
    def shm_view_fp_surf_stamp_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPSurfStampBTLFeat() As long
                | 
                |     Returns or sets SHMViewFPSurfStampBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFPSurfStampBTLFeat setting parameter manage the visibility
                |     of the BTL Base Feature on a Surface Stamp in UnFolded
                |     View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPSurfStampBTLFeat

    @shm_view_fp_surf_stamp_btl_feat.setter
    def shm_view_fp_surf_stamp_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPSurfStampBTLFeat = value

    @property
    def shm_view_fp_user_stamp_btl_feat(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SHMViewFPUserStampBTLFeat() As long
                | 
                |     Returns or sets SHMViewFPUserStampBTLFeat setting parameter
                |     value.
                |     Role: The SHMViewFPUserStampBTLFeat setting parameter manage the visibility
                |     of the BTL Base Feature on a User Stamp in UnFolded View.
                |     Legal values:
                |     1 The characteristic curve is shown
                |     0 The characteristic curve is hidden

        :rtype: int
        """

        return self.view_characteristic_curves_setting_att.SHMViewFPUserStampBTLFeat

    @shm_view_fp_user_stamp_btl_feat.setter
    def shm_view_fp_user_stamp_btl_feat(self, value: int):
        """
        :param int value:
        """

        self.view_characteristic_curves_setting_att.SHMViewFPUserStampBTLFeat = value

    def get_shm_view_fd_bead_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDBeadBTLFeatInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDBeadBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDBeadBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fd_circ_stamp_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDCircStampBTLFeatInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDCircStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDCircStampBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fd_curve_stamp_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDCurveStampBTLFeatInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDCurveStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDCurveStampBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fd_flg_cut_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDFlgCutBTLFeatInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDFlgCutBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDFlgCutBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fd_flg_cut_iml_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDFlgCutIMLInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDFlgCutIML setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDFlgCutIMLInfo(io_admin_level, io_locked)

    def get_shm_view_fd_flg_cut_oml_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDFlgCutOMLInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDFlgCutOML setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDFlgCutOMLInfo(io_admin_level, io_locked)

    def get_shm_view_fd_flg_hole_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDFlgHoleBTLFeatInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDFlgHoleBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDFlgHoleBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fd_flg_hole_iml_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDFlgHoleIMLInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDFlgHoleIML setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDFlgHoleIMLInfo(io_admin_level, io_locked)

    def get_shm_view_fd_flg_hole_oml_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDFlgHoleOMLInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDFlgHoleOML setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDFlgHoleOMLInfo(io_admin_level, io_locked)

    def get_shm_view_fd_other_stamp_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDOtherStampBTLFeatInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDOtherStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDOtherStampBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fd_stiff_stamp_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDStiffStampBTLFeatInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDStiffStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDStiffStampBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fd_surf_flg_btl_feat_bf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDSurfFlgBTLFeatBFInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDSurfFlgBTLFeatBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDSurfFlgBTLFeatBFInfo(io_admin_level, io_locked)

    def get_shm_view_fd_surf_flg_btl_feat_hf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDSurfFlgBTLFeatHFInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDSurfFlgBTLFeatHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDSurfFlgBTLFeatHFInfo(io_admin_level, io_locked)

    def get_shm_view_fd_surf_flg_btl_supp_bf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDSurfFlgBTLSuppBFInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDSurfFlgBTLSuppBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDSurfFlgBTLSuppBFInfo(io_admin_level, io_locked)

    def get_shm_view_fd_surf_flg_btl_supp_hf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDSurfFlgBTLSuppHFInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDSurfFlgBTLSuppHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDSurfFlgBTLSuppHFInfo(io_admin_level, io_locked)

    def get_shm_view_fd_surf_flg_imlbf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDSurfFlgIMLBFInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDSurfFlgIMLBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDSurfFlgIMLBFInfo(io_admin_level, io_locked)

    def get_shm_view_fd_surf_flg_imlhf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDSurfFlgIMLHFInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDSurfFlgIMLHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDSurfFlgIMLHFInfo(io_admin_level, io_locked)

    def get_shm_view_fd_surf_flg_omlbf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDSurfFlgOMLBFInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDSurfFlgOMLBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDSurfFlgOMLBFInfo(io_admin_level, io_locked)

    def get_shm_view_fd_surf_flg_omlhf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDSurfFlgOMLHFInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDSurfFlgOMLHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDSurfFlgOMLHFInfo(io_admin_level, io_locked)

    def get_shm_view_fd_surf_stamp_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDSurfStampBTLFeatInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDSurfStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDSurfStampBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fd_user_stamp_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFDUserStampBTLFeatInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFDUserStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFDUserStampBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fp_bead_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPBeadBTLFeatInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPBeadBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPBeadBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fp_circ_stamp_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPCircStampBTLFeatInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPCircStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPCircStampBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fp_curve_stamp_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPCurveStampBTLFeatInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPCurveStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPCurveStampBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fp_flg_cut_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPFlgCutBTLFeatInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPFlgCutBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPFlgCutBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fp_flg_cut_iml_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPFlgCutIMLInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPFlgCutIML setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPFlgCutIMLInfo(io_admin_level, io_locked)

    def get_shm_view_fp_flg_cut_oml_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPFlgCutOMLInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPFlgCutOML setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPFlgCutOMLInfo(io_admin_level, io_locked)

    def get_shm_view_fp_flg_hole_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPFlgHoleBTLFeatInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPFlgHoleBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPFlgHoleBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fp_flg_hole_iml_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPFlgHoleIMLInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPFlgHoleIML setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPFlgHoleIMLInfo(io_admin_level, io_locked)

    def get_shm_view_fp_flg_hole_oml_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPFlgHoleOMLInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPFlgHoleOML setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPFlgHoleOMLInfo(io_admin_level, io_locked)

    def get_shm_view_fp_other_stamp_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPOtherStampBTLFeatInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPOtherStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPOtherStampBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fp_stiff_stamp_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPStiffStampBTLFeatInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPStiffStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPStiffStampBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fp_surf_flg_btl_feat_bf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPSurfFlgBTLFeatBFInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPSurfFlgBTLFeatBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPSurfFlgBTLFeatBFInfo(io_admin_level, io_locked)

    def get_shm_view_fp_surf_flg_btl_feat_hf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPSurfFlgBTLFeatHFInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPSurfFlgBTLFeatHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPSurfFlgBTLFeatHFInfo(io_admin_level, io_locked)

    def get_shm_view_fp_surf_flg_btl_supp_bf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPSurfFlgBTLSuppBFInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPSurfFlgBTLSuppBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPSurfFlgBTLSuppBFInfo(io_admin_level, io_locked)

    def get_shm_view_fp_surf_flg_btl_supp_hf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPSurfFlgBTLSuppHFInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPSurfFlgBTLSuppHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPSurfFlgBTLSuppHFInfo(io_admin_level, io_locked)

    def get_shm_view_fp_surf_flg_clbbf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPSurfFlgCLBBFInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPSurfFlgCLBBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPSurfFlgCLBBFInfo(io_admin_level, io_locked)

    def get_shm_view_fp_surf_flg_clbhf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPSurfFlgCLBHFInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPSurfFlgCLBHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPSurfFlgCLBHFInfo(io_admin_level, io_locked)

    def get_shm_view_fp_surf_flg_imlbf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPSurfFlgIMLBFInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPSurfFlgIMLBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPSurfFlgIMLBFInfo(io_admin_level, io_locked)

    def get_shm_view_fp_surf_flg_imlhf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPSurfFlgIMLHFInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPSurfFlgIMLHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPSurfFlgIMLHFInfo(io_admin_level, io_locked)

    def get_shm_view_fp_surf_flg_oml2_bf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPSurfFlgOML2BFInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPSurfFlgOML2BF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPSurfFlgOML2BFInfo(io_admin_level, io_locked)

    def get_shm_view_fp_surf_flg_oml2_hf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPSurfFlgOML2HFInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPSurfFlgOML2HF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPSurfFlgOML2HFInfo(io_admin_level, io_locked)

    def get_shm_view_fp_surf_flg_omlbf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPSurfFlgOMLBFInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPSurfFlgOMLBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPSurfFlgOMLBFInfo(io_admin_level, io_locked)

    def get_shm_view_fp_surf_flg_omlhf_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPSurfFlgOMLHFInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPSurfFlgOMLHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPSurfFlgOMLHFInfo(io_admin_level, io_locked)

    def get_shm_view_fp_surf_stamp_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPSurfStampBTLFeatInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPSurfStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPSurfStampBTLFeatInfo(io_admin_level, io_locked)

    def get_shm_view_fp_user_stamp_btl_feat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSHMViewFPUserStampBTLFeatInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SHMViewFPUserStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.view_characteristic_curves_setting_att.GetSHMViewFPUserStampBTLFeatInfo(io_admin_level, io_locked)

    def set_shm_view_fd_bead_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDBeadBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDBeadBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDBeadBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_bead_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_bead_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDBeadBTLFeatLock iLocked
        # #     set_shm_view_fd_bead_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_circ_stamp_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDCircStampBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDCircStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDCircStampBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_circ_stamp_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_circ_stamp_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDCircStampBTLFeatLock iLocked
        # #     set_shm_view_fd_circ_stamp_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_curve_stamp_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDCurveStampBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDCurveStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDCurveStampBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_curve_stamp_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_curve_stamp_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDCurveStampBTLFeatLock iLocked
        # #     set_shm_view_fd_curve_stamp_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_flg_cut_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDFlgCutBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDFlgCutBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDFlgCutBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_flg_cut_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_flg_cut_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDFlgCutBTLFeatLock iLocked
        # #     set_shm_view_fd_flg_cut_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_flg_cut_iml_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDFlgCutIMLLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDFlgCutIML setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDFlgCutIMLLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_flg_cut_iml_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_flg_cut_iml_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDFlgCutIMLLock iLocked
        # #     set_shm_view_fd_flg_cut_iml_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_flg_cut_oml_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDFlgCutOMLLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDFlgCutOML setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDFlgCutOMLLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_flg_cut_oml_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_flg_cut_oml_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDFlgCutOMLLock iLocked
        # #     set_shm_view_fd_flg_cut_oml_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_flg_hole_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDFlgHoleBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDFlgHoleBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDFlgHoleBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_flg_hole_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_flg_hole_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDFlgHoleBTLFeatLock iLocked
        # #     set_shm_view_fd_flg_hole_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_flg_hole_iml_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDFlgHoleIMLLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDFlgHoleIML setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDFlgHoleIMLLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_flg_hole_iml_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_flg_hole_iml_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDFlgHoleIMLLock iLocked
        # #     set_shm_view_fd_flg_hole_iml_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_flg_hole_oml_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDFlgHoleOMLLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDFlgHoleOML setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDFlgHoleOMLLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_flg_hole_oml_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_flg_hole_oml_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDFlgHoleOMLLock iLocked
        # #     set_shm_view_fd_flg_hole_oml_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_other_stamp_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDOtherStampBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDOtherStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDOtherStampBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_other_stamp_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_other_stamp_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDOtherStampBTLFeatLock iLocked
        # #     set_shm_view_fd_other_stamp_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_stiff_stamp_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDStiffStampBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDStiffStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDStiffStampBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_stiff_stamp_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_stiff_stamp_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDStiffStampBTLFeatLock iLocked
        # #     set_shm_view_fd_stiff_stamp_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_surf_flg_btl_feat_bf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDSurfFlgBTLFeatBFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDSurfFlgBTLFeatBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgBTLFeatBFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_surf_flg_btl_feat_bf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_surf_flg_btl_feat_bf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgBTLFeatBFLock iLocked
        # #     set_shm_view_fd_surf_flg_btl_feat_bf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_surf_flg_btl_feat_hf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDSurfFlgBTLFeatHFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDSurfFlgBTLFeatHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgBTLFeatHFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_surf_flg_btl_feat_hf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_surf_flg_btl_feat_hf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgBTLFeatHFLock iLocked
        # #     set_shm_view_fd_surf_flg_btl_feat_hf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_surf_flg_btl_supp_bf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDSurfFlgBTLSuppBFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDSurfFlgBTLSuppBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgBTLSuppBFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_surf_flg_btl_supp_bf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_surf_flg_btl_supp_bf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgBTLSuppBFLock iLocked
        # #     set_shm_view_fd_surf_flg_btl_supp_bf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_surf_flg_btl_supp_hf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDSurfFlgBTLSuppHFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDSurfFlgBTLSuppHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgBTLSuppHFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_surf_flg_btl_supp_hf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_surf_flg_btl_supp_hf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgBTLSuppHFLock iLocked
        # #     set_shm_view_fd_surf_flg_btl_supp_hf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_surf_flg_imlbf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDSurfFlgIMLBFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDSurfFlgIMLBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgIMLBFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_surf_flg_imlbf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_surf_flg_imlbf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgIMLBFLock iLocked
        # #     set_shm_view_fd_surf_flg_imlbf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_surf_flg_imlhf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDSurfFlgIMLHFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDSurfFlgIMLHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgIMLHFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_surf_flg_imlhf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_surf_flg_imlhf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgIMLHFLock iLocked
        # #     set_shm_view_fd_surf_flg_imlhf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_surf_flg_omlbf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDSurfFlgOMLBFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDSurfFlgOMLBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgOMLBFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_surf_flg_omlbf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_surf_flg_omlbf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgOMLBFLock iLocked
        # #     set_shm_view_fd_surf_flg_omlbf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_surf_flg_omlhf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDSurfFlgOMLHFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDSurfFlgOMLHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgOMLHFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_surf_flg_omlhf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_surf_flg_omlhf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDSurfFlgOMLHFLock iLocked
        # #     set_shm_view_fd_surf_flg_omlhf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_surf_stamp_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDSurfStampBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDSurfStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDSurfStampBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_surf_stamp_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_surf_stamp_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDSurfStampBTLFeatLock iLocked
        # #     set_shm_view_fd_surf_stamp_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fd_user_stamp_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFDUserStampBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFDUserStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFDUserStampBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fd_user_stamp_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fd_user_stamp_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFDUserStampBTLFeatLock iLocked
        # #     set_shm_view_fd_user_stamp_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_bead_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPBeadBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPBeadBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPBeadBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_bead_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_bead_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPBeadBTLFeatLock iLocked
        # #     set_shm_view_fp_bead_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_circ_stamp_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPCircStampBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPCircStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPCircStampBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_circ_stamp_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_circ_stamp_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPCircStampBTLFeatLock iLocked
        # #     set_shm_view_fp_circ_stamp_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_curve_stamp_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPCurveStampBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPCurveStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPCurveStampBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_curve_stamp_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_curve_stamp_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPCurveStampBTLFeatLock iLocked
        # #     set_shm_view_fp_curve_stamp_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_flg_cut_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPFlgCutBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPFlgCutBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPFlgCutBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_flg_cut_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_flg_cut_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPFlgCutBTLFeatLock iLocked
        # #     set_shm_view_fp_flg_cut_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_flg_cut_iml_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPFlgCutIMLLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPFlgCutIML setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPFlgCutIMLLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_flg_cut_iml_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_flg_cut_iml_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPFlgCutIMLLock iLocked
        # #     set_shm_view_fp_flg_cut_iml_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_flg_cut_oml_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPFlgCutOMLLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPFlgCutOML setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPFlgCutOMLLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_flg_cut_oml_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_flg_cut_oml_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPFlgCutOMLLock iLocked
        # #     set_shm_view_fp_flg_cut_oml_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_flg_hole_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPFlgHoleBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPFlgHoleBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPFlgHoleBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_flg_hole_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_flg_hole_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPFlgHoleBTLFeatLock iLocked
        # #     set_shm_view_fp_flg_hole_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_flg_hole_iml_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPFlgHoleIMLLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPFlgHoleIML setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPFlgHoleIMLLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_flg_hole_iml_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_flg_hole_iml_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPFlgHoleIMLLock iLocked
        # #     set_shm_view_fp_flg_hole_iml_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_flg_hole_oml_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPFlgHoleOMLLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPFlgHoleOML setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPFlgHoleOMLLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_flg_hole_oml_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_flg_hole_oml_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPFlgHoleOMLLock iLocked
        # #     set_shm_view_fp_flg_hole_oml_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_other_stamp_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPOtherStampBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPOtherStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPOtherStampBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_other_stamp_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_other_stamp_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPOtherStampBTLFeatLock iLocked
        # #     set_shm_view_fp_other_stamp_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_stiff_stamp_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPStiffStampBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPStiffStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPStiffStampBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_stiff_stamp_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_stiff_stamp_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPStiffStampBTLFeatLock iLocked
        # #     set_shm_view_fp_stiff_stamp_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_surf_flg_btl_feat_bf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPSurfFlgBTLFeatBFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPSurfFlgBTLFeatBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgBTLFeatBFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_surf_flg_btl_feat_bf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_surf_flg_btl_feat_bf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgBTLFeatBFLock iLocked
        # #     set_shm_view_fp_surf_flg_btl_feat_bf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_surf_flg_btl_feat_hf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPSurfFlgBTLFeatHFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPSurfFlgBTLFeatHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgBTLFeatHFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_surf_flg_btl_feat_hf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_surf_flg_btl_feat_hf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgBTLFeatHFLock iLocked
        # #     set_shm_view_fp_surf_flg_btl_feat_hf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_surf_flg_btl_supp_bf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPSurfFlgBTLSuppBFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPSurfFlgBTLSuppBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgBTLSuppBFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_surf_flg_btl_supp_bf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_surf_flg_btl_supp_bf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgBTLSuppBFLock iLocked
        # #     set_shm_view_fp_surf_flg_btl_supp_bf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_surf_flg_btl_supp_hf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPSurfFlgBTLSuppHFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPSurfFlgBTLSuppHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgBTLSuppHFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_surf_flg_btl_supp_hf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_surf_flg_btl_supp_hf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgBTLSuppHFLock iLocked
        # #     set_shm_view_fp_surf_flg_btl_supp_hf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_surf_flg_clbbf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPSurfFlgCLBBFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPSurfFlgCLBBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgCLBBFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_surf_flg_clbbf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_surf_flg_clbbf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgCLBBFLock iLocked
        # #     set_shm_view_fp_surf_flg_clbbf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_surf_flg_clbhf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPSurfFlgCLBHFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPSurfFlgCLBHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgCLBHFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_surf_flg_clbhf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_surf_flg_clbhf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgCLBHFLock iLocked
        # #     set_shm_view_fp_surf_flg_clbhf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_surf_flg_imlbf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPSurfFlgIMLBFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPSurfFlgIMLBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgIMLBFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_surf_flg_imlbf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_surf_flg_imlbf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgIMLBFLock iLocked
        # #     set_shm_view_fp_surf_flg_imlbf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_surf_flg_imlhf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPSurfFlgIMLHFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPSurfFlgIMLHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgIMLHFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_surf_flg_imlhf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_surf_flg_imlhf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgIMLHFLock iLocked
        # #     set_shm_view_fp_surf_flg_imlhf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_surf_flg_oml2_bf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPSurfFlgOML2BFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPSurfFlgOML2BF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgOML2BFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_surf_flg_oml2_bf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_surf_flg_oml2_bf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgOML2BFLock iLocked
        # #     set_shm_view_fp_surf_flg_oml2_bf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_surf_flg_oml2_hf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPSurfFlgOML2HFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPSurfFlgOML2HF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgOML2HFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_surf_flg_oml2_hf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_surf_flg_oml2_hf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgOML2HFLock iLocked
        # #     set_shm_view_fp_surf_flg_oml2_hf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_surf_flg_omlbf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPSurfFlgOMLBFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPSurfFlgOMLBF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgOMLBFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_surf_flg_omlbf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_surf_flg_omlbf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgOMLBFLock iLocked
        # #     set_shm_view_fp_surf_flg_omlbf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_surf_flg_omlhf_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPSurfFlgOMLHFLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPSurfFlgOMLHF setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgOMLHFLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_surf_flg_omlhf_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_surf_flg_omlhf_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPSurfFlgOMLHFLock iLocked
        # #     set_shm_view_fp_surf_flg_omlhf_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_surf_stamp_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPSurfStampBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPSurfStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPSurfStampBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_surf_stamp_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_surf_stamp_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPSurfStampBTLFeatLock iLocked
        # #     set_shm_view_fp_surf_stamp_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shm_view_fp_user_stamp_btl_feat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSHMViewFPUserStampBTLFeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SHMViewFPUserStampBTLFeat setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.view_characteristic_curves_setting_att.SetSHMViewFPUserStampBTLFeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shm_view_fp_user_stamp_btl_feat_lock'
        # # vba_code = """
        # # Public Function set_shm_view_fp_user_stamp_btl_feat_lock(view_characteristic_curves_setting_att)
        # #     Dim iLocked (2)
        # #     view_characteristic_curves_setting_att.SetSHMViewFPUserStampBTLFeatLock iLocked
        # #     set_shm_view_fp_user_stamp_btl_feat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ViewCharacteristicCurvesSettingAtt(name="{self.name}")'
