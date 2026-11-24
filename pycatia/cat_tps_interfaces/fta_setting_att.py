#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia import CATFTADimCreateOn, CATFTADimConfigureSnapping
from pycatia.system_interfaces.setting_controller import SettingController


class FTASettingAtt(SettingController):
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
                |                         FTASettingAtt
                | 
                | The interface to access a CATIAFTASettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def alphabetic_order(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AlphabeticOrder() As boolean
                | 
                |     Returns or sets the AlphabeticOrder setting parameter
                |     value.
                |     True if the AlphabeticOrder setting parameter is checked.
                |     Role: When set to True, the FTA 3D Annotation representations are saved in
                |     CGR. Otherwise, they are not saved.

        :rtype: bool
        """

        return self.com_object.AlphabeticOrder

    @alphabetic_order.setter
    def alphabetic_order(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AlphabeticOrder = value

    @property
    def analysis_display_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisDisplayMode() As boolean
                | 
                |     Returns the AnalysisDisplayMode parameter.

        :rtype: bool
        """

        return self.com_object.AnalysisDisplayMode

    @analysis_display_mode.setter
    def analysis_display_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AnalysisDisplayMode = value

    @property
    def angulaire_general_tol_class(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AngulaireGeneralTolClass() As long
                | 
                |     Returns or sets the Dimension general class parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.com_object.AngulaireGeneralTolClass

    @angulaire_general_tol_class.setter
    def angulaire_general_tol_class(self, value: int):
        """
        :param int value:
        """

        self.com_object.AngulaireGeneralTolClass = value

    @property
    def annot_dim_invalid(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnnotDimInvalid() As boolean
                | 
                |     Returns the AnnotDimInvalid parameter.

        :rtype: bool
        """

        return self.com_object.AnnotDimInvalid

    @annot_dim_invalid.setter
    def annot_dim_invalid(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AnnotDimInvalid = value

    @property
    def annot_dim_on_deleted_geom(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnnotDimOnDeletedGeom() As boolean
                | 
                |     Returns the AnnotDimOnDeletedGeom parameter.

        :rtype: bool
        """

        return self.com_object.AnnotDimOnDeletedGeom

    @annot_dim_on_deleted_geom.setter
    def annot_dim_on_deleted_geom(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AnnotDimOnDeletedGeom = value

    @property
    def annot_dim_on_unloaded_geom(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnnotDimOnUnloadedGeom() As boolean
                | 
                |     Returns the AnnotDimOnUnloadedGeom parameter.

        :rtype: bool
        """

        return self.com_object.AnnotDimOnUnloadedGeom

    @annot_dim_on_unloaded_geom.setter
    def annot_dim_on_unloaded_geom(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AnnotDimOnUnloadedGeom = value

    @property
    def annot_on_zero_z_setting(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnnotOnZeroZSetting() As boolean
                | 
                |     Returns the AnnotOnZeroZSetting parameter.

        :rtype: bool
        """

        return self.com_object.AnnotOnZeroZSetting

    @annot_on_zero_z_setting.setter
    def annot_on_zero_z_setting(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AnnotOnZeroZSetting = value

    @property
    def body_hide_in_capture(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BodyHideInCapture() As long
                | 
                |     Returns or sets the Visibility of Part instances, bodies and geometrical
                |     sets in Capture.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.com_object.BodyHideInCapture

    @body_hide_in_capture.setter
    def body_hide_in_capture(self, value: int):
        """
        :param int value:
        """

        self.com_object.BodyHideInCapture = value

    @property
    def cat_fta_chamfer_general_tol_class(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CATFTAChamferGeneralTolClass() As long
                | 
                |     Returns the CATFTAChamferGeneralTolClass parameter.

        :rtype: int
        """

        return self.com_object.CATFTAChamferGeneralTolClass

    @cat_fta_chamfer_general_tol_class.setter
    def cat_fta_chamfer_general_tol_class(self, value: int):
        """
        :param int value:
        """

        self.com_object.CATFTAChamferGeneralTolClass = value

    @property
    def cat_fta_edges_line_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CATFTAEdgesLineType() As long
                | 
                |     Returns the CATFTAEdgesLineType parameter.

        :rtype: int
        """

        return self.com_object.CATFTAEdgesLineType

    @cat_fta_edges_line_type.setter
    def cat_fta_edges_line_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.CATFTAEdgesLineType = value

    @property
    def cat_fta_edges_thickness(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CATFTAEdgesThickness() As long
                | 
                |     Returns the CATFTAEdgesThickness parameter.

        :rtype: int
        """

        return self.com_object.CATFTAEdgesThickness

    @cat_fta_edges_thickness.setter
    def cat_fta_edges_thickness(self, value: int):
        """
        :param int value:
        """

        self.com_object.CATFTAEdgesThickness = value

    @property
    def cat_ftauf_auto_tolerancing(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CATFTAUFAutoTolerancing() As CATBSTR
                | 
                |     Returns the CATFTAUFAutoTolerancing parameter.

        :rtype: str
        """

        return self.com_object.CATFTAUFAutoTolerancing

    @cat_ftauf_auto_tolerancing.setter
    def cat_ftauf_auto_tolerancing(self, value: str):
        """
        :param str value:
        """

        self.com_object.CATFTAUFAutoTolerancing = value

    @property
    def cat_fta_use_last_tolerances(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CATFTAUseLastTolerances() As boolean
                | 
                |     Returns the CATFTAUseLastTolerances parameter.

        :rtype: bool
        """

        return self.com_object.CATFTAUseLastTolerances

    @cat_fta_use_last_tolerances.setter
    def cat_fta_use_last_tolerances(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CATFTAUseLastTolerances = value

    @property
    def dim_after_cre(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimAfterCre() As boolean
                | 
                |     Returns or sets the Dimension After Creaation parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimAfterCre

    @dim_after_cre.setter
    def dim_after_cre(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimAfterCre = value

    @property
    def dim_after_mod(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimAfterMod() As boolean
                | 
                |     Returns or sets the Dimension After Modification
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimAfterMod

    @dim_after_mod.setter
    def dim_after_mod(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimAfterMod = value

    @property
    def dim_before_cre(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimBeforeCre() As boolean
                | 
                |     Returns or sets the Dimension Before Creation parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimBeforeCre

    @dim_before_cre.setter
    def dim_before_cre(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimBeforeCre = value

    @property
    def dim_before_mod(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimBeforeMod() As boolean
                | 
                |     Returns or sets the Dimension Before Modification
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimBeforeMod

    @dim_before_mod.setter
    def dim_before_mod(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimBeforeMod = value

    @property
    def dim_blanking_cre(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimBlankingCre() As boolean
                | 
                |     Returns or sets the Dimension Blanking Creation parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimBlankingCre

    @dim_blanking_cre.setter
    def dim_blanking_cre(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimBlankingCre = value

    @property
    def dim_blanking_mod(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimBlankingMod() As boolean
                | 
                |     Returns or sets the Dimension Blanking Modification
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimBlankingMod

    @dim_blanking_mod.setter
    def dim_blanking_mod(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimBlankingMod = value

    @property
    def dim_configure_snapping(self) -> CATFTADimConfigureSnapping:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimConfigureSnapping() As
                | CATFTADimConfigureSnapping
                | 
                |     Returns or sets the DimConfigureSnapping parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: CATFTADimConfigureSnapping
        """

        return self.com_object.DimConfigureSnapping

    @dim_configure_snapping.setter
    def dim_configure_snapping(self, value: CATFTADimConfigureSnapping):
        """
        :param CATFTADimConfigureSnapping value:
        """

        self.com_object.DimConfigureSnapping = value

    @property
    def dim_constant_offset(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimConstantOffset() As boolean
                | 
                |     Returns or sets the Constant Offset parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimConstantOffset

    @dim_constant_offset.setter
    def dim_constant_offset(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimConstantOffset = value

    @property
    def dim_create_on(self) -> CATFTADimCreateOn:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimCreateOn() As CATFTADimCreateOn
                | 
                |     Returns or sets the DimCreateOn parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: CATFTADimCreateOn
        """

        return self.com_object.DimCreateOn

    @dim_create_on.setter
    def dim_create_on(self, value: CATFTADimCreateOn):
        """
        :param CATFTADimCreateOn value:
        """

        self.com_object.DimCreateOn = value

    @property
    def dim_line_pos_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimLinePosValue() As double
                | 
                |     Returns or sets the Dimension Line Position Value
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.com_object.DimLinePosValue

    @dim_line_pos_value.setter
    def dim_line_pos_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.DimLinePosValue = value

    @property
    def dim_line_up_base_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimLineUpBaseAngle() As double
                | 
                |     Returns or sets the Dimension Line Up Base Angle
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.com_object.DimLineUpBaseAngle

    @dim_line_up_base_angle.setter
    def dim_line_up_base_angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.DimLineUpBaseAngle = value

    @property
    def dim_line_up_base_length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimLineUpBaseLength() As double
                | 
                |     Returns or sets the Dimension Line Up Base Length
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.com_object.DimLineUpBaseLength

    @dim_line_up_base_length.setter
    def dim_line_up_base_length(self, value: float):
        """
        :param float value:
        """

        self.com_object.DimLineUpBaseLength = value

    @property
    def dim_line_up_cumul(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimLineUpCumul() As boolean
                | 
                |     Returns or sets the Dimension Line Up Cululated parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimLineUpCumul

    @dim_line_up_cumul.setter
    def dim_line_up_cumul(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimLineUpCumul = value

    @property
    def dim_line_up_funnel(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimLineUpFunnel() As boolean
                | 
                |     Returns or sets the Dimension Line Up Funnel parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimLineUpFunnel

    @dim_line_up_funnel.setter
    def dim_line_up_funnel(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimLineUpFunnel = value

    @property
    def dim_line_up_offset_bet_dim_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimLineUpOffsetBetDimAngle() As double
                | 
                |     Returns gets the DimLineUpOffsetBetDimAngle parameter.
                | 
                |     Parameters:
                | 
                |         oValue
                |             Output value of the DimLineUpOffsetBetDimAngle. If return code
                |             E_FAIL oValue is not obtained. If return code S_OK oValue is obtained.

        :rtype: float
        """

        return self.com_object.DimLineUpOffsetBetDimAngle

    @dim_line_up_offset_bet_dim_angle.setter
    def dim_line_up_offset_bet_dim_angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.DimLineUpOffsetBetDimAngle = value

    @property
    def dim_line_up_offset_bet_dim_length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimLineUpOffsetBetDimLength() As double
                | 
                |     Returns gets the DimLineUpOffsetBetDimLength parameter.
                | 
                |     Parameters:
                | 
                |         oValue
                |             Output value of the DimLineUpOffsetBetDimLength. If return code
                |             E_FAIL oValue is not obtained. If return code S_OK oValue is obtained.

        :rtype: float
        """

        return self.com_object.DimLineUpOffsetBetDimLength

    @dim_line_up_offset_bet_dim_length.setter
    def dim_line_up_offset_bet_dim_length(self, value: float):
        """
        :param float value:
        """

        self.com_object.DimLineUpOffsetBetDimLength = value

    @property
    def dim_line_up_offset_to_ref_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimLineUpOffsetToRefAngle() As double
                | 
                |     Returns gets the DimLineUpOffsetToRefAngle parameter.
                | 
                |     Parameters:
                | 
                |         oValue
                |             Output value of the DimLineUpOffsetToRefAngle. If return code
                |             E_FAIL oValue is not obtained. If return code S_OK oValue is obtained.

        :rtype: float
        """

        return self.com_object.DimLineUpOffsetToRefAngle

    @dim_line_up_offset_to_ref_angle.setter
    def dim_line_up_offset_to_ref_angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.DimLineUpOffsetToRefAngle = value

    @property
    def dim_line_up_offset_to_ref_length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimLineUpOffsetToRefLength() As double
                | 
                |     Returns gets the DimLineUpOffsetToRefLength parameter.
                | 
                |     Parameters:
                | 
                |         oValue
                |             Output value of the DimLineUpOffsetToRefLength. If return code
                |             E_FAIL oValue is not obtained. If return code S_OK oValue is obtained.

        :rtype: float
        """

        return self.com_object.DimLineUpOffsetToRefLength

    @dim_line_up_offset_to_ref_length.setter
    def dim_line_up_offset_to_ref_length(self, value: float):
        """
        :param float value:
        """

        self.com_object.DimLineUpOffsetToRefLength = value

    @property
    def dim_line_up_stack(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimLineUpStack() As boolean
                | 
                |     Returns or sets the Dimension Line Up Stack parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimLineUpStack

    @dim_line_up_stack.setter
    def dim_line_up_stack(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimLineUpStack = value

    @property
    def dim_manual_positionning(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimManualPositionning() As boolean
                | 
                |     Returns or sets the Manual Positionning parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimManualPositionning

    @dim_manual_positionning.setter
    def dim_manual_positionning(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimManualPositionning = value

    @property
    def dim_move_2d_part_cre(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimMove2dPartCre() As boolean
                | 
                |     Returns or sets the Dimension Move 2D Creation parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimMove2dPartCre

    @dim_move_2d_part_cre.setter
    def dim_move_2d_part_cre(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimMove2dPartCre = value

    @property
    def dim_move_2d_part_mod(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimMove2dPartMod() As boolean
                | 
                |     Returns or sets the Dimension Move 2D Modification
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimMove2dPartMod

    @dim_move_2d_part_mod.setter
    def dim_move_2d_part_mod(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimMove2dPartMod = value

    @property
    def dim_move_dim_line_cre(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimMoveDimLineCre() As boolean
                | 
                |     Returns or sets the Dimension Move Dimension Line Creation
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimMoveDimLineCre

    @dim_move_dim_line_cre.setter
    def dim_move_dim_line_cre(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimMoveDimLineCre = value

    @property
    def dim_move_dim_line_mod(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimMoveDimLineMod() As boolean
                | 
                |     Returns or sets the Dimension Move Dimension Line Modification
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimMoveDimLineMod

    @dim_move_dim_line_mod.setter
    def dim_move_dim_line_mod(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimMoveDimLineMod = value

    @property
    def dim_move_leader_cre(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimMoveLeaderCre() As boolean
                | 
                |     Get the Dimension leader Creation parameter.
                | 
                |     Parameters:
                | 
                |         oValue
                |             Output value of the Dimension Leader creation check box status. If
                |             return code E_FAIL oValue is not obtained. If return code S_OK oValue is
                |             obtained.

        :rtype: bool
        """

        return self.com_object.DimMoveLeaderCre

    @dim_move_leader_cre.setter
    def dim_move_leader_cre(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimMoveLeaderCre = value

    @property
    def dim_move_leader_mod(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimMoveLeaderMod() As boolean
                | 
                |     Returns gets the Dimension leader modification parameter.
                | 
                |     Parameters:
                | 
                |         oValue
                |             Output value of the Dimension Leader modification check box status.
                |             If return code E_FAIL oValue is not obtained. If return code S_OK oValue is
                |             obtained.

        :rtype: bool
        """

        return self.com_object.DimMoveLeaderMod

    @dim_move_leader_mod.setter
    def dim_move_leader_mod(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimMoveLeaderMod = value

    @property
    def dim_move_sub_part(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimMoveSubPart() As boolean
                | 
                |     Returns or sets the DimMoveSubPart parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimMoveSubPart

    @dim_move_sub_part.setter
    def dim_move_sub_part(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimMoveSubPart = value

    @property
    def dim_move_value_cre(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimMoveValueCre() As boolean
                | 
                |     Returns or sets the Dimension Move Value Creation
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimMoveValueCre

    @dim_move_value_cre.setter
    def dim_move_value_cre(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimMoveValueCre = value

    @property
    def dim_move_value_mod(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimMoveValueMod() As boolean
                | 
                |     Returns or sets the Dimension Move Value Modification
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimMoveValueMod

    @dim_move_value_mod.setter
    def dim_move_value_mod(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimMoveValueMod = value

    @property
    def dim_o_run_cre(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimORunCre() As boolean
                | 
                |     Returns or sets the Dimension Over Run Creation parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimORunCre

    @dim_o_run_cre.setter
    def dim_o_run_cre(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimORunCre = value

    @property
    def dim_o_run_mod(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimORunMod() As boolean
                | 
                |     Returns or sets the Dimension Over Run Modification
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimORunMod

    @dim_o_run_mod.setter
    def dim_o_run_mod(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimORunMod = value

    @property
    def dim_ori_default_symb(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimOriDefaultSymb() As boolean
                | 
                |     Returns or sets the Dimension Orientation Default Symbol
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimOriDefaultSymb

    @dim_ori_default_symb.setter
    def dim_ori_default_symb(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimOriDefaultSymb = value

    @property
    def dim_snapping(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimSnapping() As boolean
                | 
                |     Returns or sets the Dimension Snapping parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.DimSnapping

    @dim_snapping.setter
    def dim_snapping(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DimSnapping = value

    @property
    def general_tol_class(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GeneralTolClass() As long
                | 
                |     Returns or sets the Dimension general class parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.com_object.GeneralTolClass

    @general_tol_class.setter
    def general_tol_class(self, value: int):
        """
        :param int value:
        """

        self.com_object.GeneralTolClass = value

    @property
    def highlight_def_annot(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HighlightDefAnnot() As boolean
                | 
                |     Returns or sets the Highlight Def Annot parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.HighlightDefAnnot

    @highlight_def_annot.setter
    def highlight_def_annot(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.HighlightDefAnnot = value

    @property
    def noa_creation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NoaCreation() As boolean
                | 
                |     Returns or sets the Noa Creation parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.NoaCreation

    @noa_creation.setter
    def noa_creation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.NoaCreation = value

    @property
    def non_semantic_always_upgrade(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NonSemanticAllwaysUpgrade() As boolean
                | 
                |     Returns or sets the Non SemanticAllways Upgrade parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.NonSemanticAllwaysUpgrade

    @non_semantic_always_upgrade.setter
    def non_semantic_always_upgrade(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.NonSemanticAllwaysUpgrade = value

    @property
    def non_semantic_always_upgrade_general_tol(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NonSemanticAllwaysUpgradeGeneralTol() As boolean
                | 
                |     Returns or sets the Non SemanticAllways Upgrade general tolerance
                |     parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.NonSemanticAllwaysUpgradeGeneralTol

    @non_semantic_always_upgrade_general_tol.setter
    def non_semantic_always_upgrade_general_tol(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.NonSemanticAllwaysUpgradeGeneralTol = value

    @property
    def non_semantic_dim_allowed(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NonSemanticDimAllowed() As boolean
                | 
                |     Returns or sets the Non Semantic Dim Allowed parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.NonSemanticDimAllowed

    @non_semantic_dim_allowed.setter
    def non_semantic_dim_allowed(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.NonSemanticDimAllowed = value

    @property
    def non_semantic_marked(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NonSemanticMarked() As boolean
                | 
                |     Returns or sets the Non Semantic Marked parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.NonSemanticMarked

    @non_semantic_marked.setter
    def non_semantic_marked(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.NonSemanticMarked = value

    @property
    def non_semantic_tol_allowed(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NonSemanticTolAllowed() As boolean
                | 
                |     Returns or sets the Non Semantic Tol Allowed parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.NonSemanticTolAllowed

    @non_semantic_tol_allowed.setter
    def non_semantic_tol_allowed(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.NonSemanticTolAllowed = value

    @property
    def parameters_in_tree(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ParametersInTree() As boolean
                | 
                |     Returns or sets the Parameters in tree parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.ParametersInTree

    @parameters_in_tree.setter
    def parameters_in_tree(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ParametersInTree = value

    @property
    def rotation_snap_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RotationSnapAngle() As double
                | 
                |     Returns or sets the Rotation Snap Angle parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.com_object.RotationSnapAngle

    @rotation_snap_angle.setter
    def rotation_snap_angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.RotationSnapAngle = value

    @property
    def rotation_snap_auto(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RotationSnapAuto() As boolean
                | 
                |     Returns or sets the Rotation Snap Auto parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.RotationSnapAuto

    @rotation_snap_auto.setter
    def rotation_snap_auto(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.RotationSnapAuto = value

    @property
    def sect_pattern(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectPattern() As boolean
                | 
                |     Returns or sets the Pattern of Visu setting parameter
                |     value.
                |     True if the Pattern of Visu setting parameter is checked.
                |     Role: When set to True, the FTA 3D Annotation representations are saved in
                |     CGR. Otherwise, they are not saved.

        :rtype: bool
        """

        return self.com_object.SectPattern

    @sect_pattern.setter
    def sect_pattern(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SectPattern = value

    @property
    def select_published_geometry(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SelectPublishedGeometry() As boolean
                | 
                |     Returns or sets the Slect Published Geometry parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.SelectPublishedGeometry

    @select_published_geometry.setter
    def select_published_geometry(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SelectPublishedGeometry = value

    @property
    def shifted_profile(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ShiftedProfile() As boolean
                | 
                |     Returns or sets the Shifted Profile parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.com_object.ShiftedProfile

    @shifted_profile.setter
    def shifted_profile(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ShiftedProfile = value

    @property
    def true_dimension(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TrueDimension() As boolean
                | 
                |     Returns the TrueDimension parameter.

        :rtype: bool
        """

        return self.com_object.TrueDimension

    @true_dimension.setter
    def true_dimension(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.TrueDimension = value

    def get_alphabetic_order_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetAlphabeticOrderInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the AlphabeticOrder setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetAlphabeticOrderInfo(admin_level, o_locked)

    def get_analysis_display_mode_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetAnalysisDisplayModeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the AnalysisDisplayMode
                |     parameter.
                |     Role:Retrieves the state of the AnalysisDisplayMode parameter in the
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

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetAnalysisDisplayModeInfo(admin_level, o_locked)

    def get_angulaire_general_tol_class_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetAngulaireGeneralTolClassInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension general class tolerance setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetAngulaireGeneralTolClassInfo(admin_level, o_locked)

    def get_annot_dim_invalid_colour(self, o_value_r: int, o_value_g: int, o_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub GetAnnotDimInvalidColor(long oValueR,
                | long oValueG,
                | long oValueB)
                | 
                |     Returns the AnnotDimInvalidColor parameter.

        :param int o_value_r:
        :param int o_value_g:
        :param int o_value_b:
        :rtype: None
        """
        return self.com_object.GetAnnotDimInvalidColor(o_value_r, o_value_g, o_value_b)

    def get_annot_dim_invalid_colour_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub GetAnnotDimInvalidColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the AnnotDimInvalidColor
                |     parameter.
                |     Role:Retrieves the state of the AnnotDimInvalidColor parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.com_object.GetAnnotDimInvalidColorInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_annot_dim_invalid_color_info'
        # # vba_code = """
        # # Public Function get_annot_dim_invalid_color_info(fta_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     fta_setting_att.GetAnnotDimInvalidColorInfo ioAdminLevel
        # #     get_annot_dim_invalid_color_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_annot_dim_invalid_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetAnnotDimInvalidInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Locks or unlocks the AnnotDimInvalid parameter.
                |     Role:Locks or unlocks the AnnotDimInvalid parameter if it is possible in
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

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetAnnotDimInvalidInfo(admin_level, o_locked)

    def get_annot_dim_on_deleted_geom_colour(self, o_value_r: int, o_value_g: int, o_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub GetAnnotDimOnDeletedGeomColor(long oValueR,
                | long oValueG,
                | long oValueB)
                | 
                |     Returns the AnnotDimOnDeletedGeomColor parameter.

        :param int o_value_r:
        :param int o_value_g:
        :param int o_value_b:
        :rtype: None
        """
        return self.com_object.GetAnnotDimOnDeletedGeomColor(o_value_r, o_value_g, o_value_b)

    def get_annot_dim_on_deleted_geom_colour_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub GetAnnotDimOnDeletedGeomColorInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the AnnotDimOnDeletedGeomColor
                |     parameter.
                |     Role:Retrieves the state of the AnnotDimOnDeletedGeomColor parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.com_object.GetAnnotDimOnDeletedGeomColorInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_annot_dim_on_deleted_geom_color_info'
        # # vba_code = """
        # # Public Function get_annot_dim_on_deleted_geom_color_info(fta_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     fta_setting_att.GetAnnotDimOnDeletedGeomColorInfo ioAdminLevel
        # #     get_annot_dim_on_deleted_geom_color_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_annot_dim_on_deleted_geom_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetAnnotDimOnDeletedGeomInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the AnnotDimOnDeletedGeom
                |     parameter.
                |     Role:Retrieves the state of the AnnotDimOnDeletedGeom parameter in the
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

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetAnnotDimOnDeletedGeomInfo(admin_level, o_locked)

    def get_annot_dim_on_unloaded_geom_colour(self, o_value_r: int, o_value_g: int, o_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub GetAnnotDimOnUnloadedGeomColor(long oValueR,
                | long oValueG,
                | long oValueB)
                | 
                |     Returns the AnnotDimOnUnloadedGeomColor parameter.

        :param int o_value_r:
        :param int o_value_g:
        :param int o_value_b:
        :rtype: None
        """
        return self.com_object.GetAnnotDimOnUnloadedGeomColor(o_value_r, o_value_g, o_value_b)

    def get_annot_dim_on_unloaded_geom_colour_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub GetAnnotDimOnUnloadedGeomColorInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the AnnotDimOnUnloadedGeomColor
                |     parameter.
                |     Role:Retrieves the state of the AnnotDimOnUnloadedGeomColor parameter in
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
        :param bool o_modified:
        :rtype: None
        """
        return self.com_object.GetAnnotDimOnUnloadedGeomColorInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_annot_dim_on_unloaded_geom_color_info'
        # # vba_code = """
        # # Public Function get_annot_dim_on_unloaded_geom_color_info(fta_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     fta_setting_att.GetAnnotDimOnUnloadedGeomColorInfo ioAdminLevel
        # #     get_annot_dim_on_unloaded_geom_color_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_annot_dim_on_unloaded_geom_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetAnnotDimOnUnloadedGeomInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the AnnotDimOnUnloadedGeom
                |     parameter.
                |     Role:Retrieves the state of the AnnotDimOnUnloadedGeom parameter in the
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

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetAnnotDimOnUnloadedGeomInfo(admin_level, o_locked)

    def get_annot_on_zero_z_setting_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetAnnotOnZeroZSettingInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the AnnotOnZeroZSetting
                |     parameter.
                |     Role:Retrieves the state of the AnnotOnZeroZSetting parameter in the
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

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetAnnotOnZeroZSettingInfo(admin_level, o_locked)

    def get_body_hide_in_capture_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetBodyHideInCaptureInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Visibility of Part instances, bodies and
                |     geometrical sets in Capture.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetBodyHideInCaptureInfo(admin_level, o_locked)

    def get_cat_fta_chamfer_general_tol_class_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetCATFTAChamferGeneralTolClassInfo(CATBSTR
                | AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the CATFTAChamferGeneralTolClass
                |     parameter.
                |     Role:Retrieves the state of the CATFTAChamferGeneralTolClass parameter in
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

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetCATFTAChamferGeneralTolClassInfo(admin_level, o_locked)

    def get_cat_fta_edges_colour(self, o_value_r: int, o_value_g: int, o_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub GetCATFTAEdgesColor(long oValueR,
                | long oValueG,
                | long oValueB)
                | 
                |     Returns the GetCATFTAEdgesColor parameter.

        :param int o_value_r:
        :param int o_value_g:
        :param int o_value_b:
        :rtype: None
        """
        return self.com_object.GetCATFTAEdgesColor(o_value_r, o_value_g, o_value_b)

    def get_cat_fta_edges_colour_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub GetCATFTAEdgesColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the GetCATFTAEdgesColor
                |     parameter.
                |     Role:Retrieves the state of the GetCATFTAEdgesColor parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.com_object.GetCATFTAEdgesColorInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_catfta_edges_color_info'
        # # vba_code = """
        # # Public Function get_catfta_edges_color_info(fta_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     fta_setting_att.GetCATFTAEdgesColorInfo ioAdminLevel
        # #     get_catfta_edges_color_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_cat_fta_edges_line_type_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub GetCATFTAEdgesLineTypeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the CATFTAEdgesLineType
                |     parameter.
                |     Role:Retrieves the state of the CATFTAEdgesLineType parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.com_object.GetCATFTAEdgesLineTypeInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_catfta_edges_line_type_info'
        # # vba_code = """
        # # Public Function get_catfta_edges_line_type_info(fta_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     fta_setting_att.GetCATFTAEdgesLineTypeInfo ioAdminLevel
        # #     get_catfta_edges_line_type_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_cat_fta_edges_thickness_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub GetCATFTAEdgesThicknessInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the CATFTAEdgesThickness
                |     parameter.
                |     Role:Retrieves the state of the CATFTAEdgesThickness parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.com_object.GetCATFTAEdgesThicknessInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_catfta_edges_thickness_info'
        # # vba_code = """
        # # Public Function get_catfta_edges_thickness_info(fta_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     fta_setting_att.GetCATFTAEdgesThicknessInfo ioAdminLevel
        # #     get_catfta_edges_thickness_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_cat_fta_uf_auto_tolerancing_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub GetCATFTAUFAutoTolerancingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the CATFTAUFAutoTolerancing
                |     parameter.
                |     Role:Retrieves the state of the CATFTAUFAutoTolerancing parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.com_object.GetCATFTAUFAutoTolerancingInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_catftauf_auto_tolerancing_info'
        # # vba_code = """
        # # Public Function get_catftauf_auto_tolerancing_info(fta_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     fta_setting_att.GetCATFTAUFAutoTolerancingInfo ioAdminLevel
        # #     get_catftauf_auto_tolerancing_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_cat_fta_use_last_tolerances_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetCATFTAUseLastTolerancesInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the CATFTAUseLastTolerances
                |     parameter.
                |     Role:Retrieves the state of the CATFTAUseLastTolerances parameter in the
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

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetCATFTAUseLastTolerancesInfo(admin_level, o_locked)

    def get_dim_after_cre_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimAfterCreInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension After Creation setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimAfterCreInfo(admin_level, o_locked)

    def get_dim_after_mod_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimAfterModInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension After Modification setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimAfterModInfo(admin_level, o_locked)

    def get_dim_before_cre_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimBeforeCreInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Before Creation setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimBeforeCreInfo(admin_level, o_locked)

    def get_dim_before_mod_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimBeforeModInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Before Modification setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimBeforeModInfo(admin_level, o_locked)

    def get_dim_blanking_cre_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimBlankingCreInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Blanking Creation setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimBlankingCreInfo(admin_level, o_locked)

    def get_dim_blanking_mod_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimBlankingModInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Blanking Modification setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimBlankingModInfo(admin_level, o_locked)

    def get_dim_configure_snapping_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimConfigureSnappingInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the DimMoveSubPart setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimConfigureSnappingInfo(admin_level, o_locked)

    def get_dim_constant_offset_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimConstantOffsetInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Constant Offset setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimConstantOffsetInfo(admin_level, o_locked)

    def get_dim_create_on_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimCreateOnInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the DimCreateOn setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimCreateOnInfo(admin_level, o_locked)

    def get_dim_line_pos_value_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimLinePosValueInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Line Position Value setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimLinePosValueInfo(admin_level, o_locked)

    def get_dim_line_up_base_angle_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimLineUpBaseAngleInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Line Up Base Angle setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimLineUpBaseAngleInfo(admin_level, o_locked)

    def get_dim_line_up_base_length_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimLineUpBaseLengthInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Line Up Base Length setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimLineUpBaseLengthInfo(admin_level, o_locked)

    def get_dim_line_up_cumul_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimLineUpCumulInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Line Up Cululated setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimLineUpCumulInfo(admin_level, o_locked)

    def get_dim_line_up_funnel_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimLineUpFunnelInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Line Up Funnel setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimLineUpFunnelInfo(admin_level, o_locked)

    def get_dim_line_up_offset_bet_dim_angle_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimLineUpOffsetBetDimAngleInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the DimLineUpOffsetBetDimAngle setting
                |     parameter value.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                |             Input/Output parameter, is the administration level.
                |             
                |         oLocked
                |             Input/Output parameter, is the lock status of the check button.
                |             
                |         oModified
                |             Output paramter which gives the status as boolean if the status is
                |             modified. If return code E_FAIL the values are not obtained. If return code
                |             S_OK the values are obtained.
                |             Refer to 
                | 
                |         SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimLineUpOffsetBetDimAngleInfo(admin_level, o_locked)

    def get_dim_line_up_offset_bet_dim_length_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimLineUpOffsetBetDimLengthInfo(CATBSTR
                | AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the DimLineUpOffsetBetDimLength setting
                |     parameter value.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                |             Input/Output parameter, is the administration level.
                |             
                |         oLocked
                |             Input/Output parameter, is the lock status of the check button.
                |             
                |         oModified
                |             Output paramter which gives the status as boolean if the status is
                |             modified. If return code E_FAIL the values are not obtained. If return code
                |             S_OK the values are obtained.
                |             Refer to 
                | 
                |         SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimLineUpOffsetBetDimLengthInfo(admin_level, o_locked)

    def get_dim_line_up_offset_to_ref_angle_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimLineUpOffsetToRefAngleInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the DimLineUpOffsetToRefAngle setting
                |     parameter value.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                |             Input/Output parameter, is the administration level.
                |             
                |         oLocked
                |             Input/Output parameter, is the lock status of the check button.
                |             
                |         oModified
                |             Output paramter which gives the status as boolean if the status is
                |             modified. If return code E_FAIL the values are not obtained. If return code
                |             S_OK the values are obtained.
                |             Refer to 
                | 
                |         SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimLineUpOffsetToRefAngleInfo(admin_level, o_locked)

    def get_dim_line_up_offset_to_ref_length_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimLineUpOffsetToRefLengthInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the DimLineUpOffsetToRefLength setting
                |     parameter value.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                |             Input/Output parameter, is the administration level.
                |             
                |         oLocked
                |             Input/Output parameter, is the lock status of the check button.
                |             
                |         oModified
                |             Output paramter which gives the status as boolean if the status is
                |             modified. If return code E_FAIL the values are not obtained. If return code
                |             S_OK the values are obtained.
                |             Refer to 
                | 
                |         SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimLineUpOffsetToRefLengthInfo(admin_level, o_locked)

    def get_dim_line_up_stack_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimLineUpStackInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Line Up Stack setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimLineUpStackInfo(admin_level, o_locked)

    def get_dim_manual_positioning_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimManualPositionningInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Manual Positionning setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimManualPositionningInfo(admin_level, o_locked)

    def get_dim_move_2d_part_cre_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimMove2dPartCreInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Move 2D Creation setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimMove2dPartCreInfo(admin_level, o_locked)

    def get_dim_move_2d_part_mod_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimMove2dPartModInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Move 2D Modification setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimMove2dPartModInfo(admin_level, o_locked)

    def get_dim_move_dim_line_cre_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimMoveDimLineCreInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Move Dimension Line Creation
                |     setting parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimMoveDimLineCreInfo(admin_level, o_locked)

    def get_dim_move_dim_line_mod_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimMoveDimLineModInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Move Dimension Line Modification
                |     setting parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimMoveDimLineModInfo(admin_level, o_locked)

    def get_dim_move_leader_cre_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimMoveLeaderCreInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension leader Creation setting
                |     parameter value.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                |             Input/Output parameter, is the administration level.
                |             
                |         oLocked
                |             Input/Output parameter, is the lock status of the check button.
                |             
                |         oModified
                |             Output paramter which gives the status as boolean if the status is
                |             modified. If return code E_FAIL the values are not obtained. If return code
                |             S_OK the values are obtained.
                |             Refer to 
                | 
                |         SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimMoveLeaderCreInfo(admin_level, o_locked)

    def get_dim_move_leader_mod_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimMoveLeaderModInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension leader modification setting
                |     parameter value.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                |             Input/Output parameter, is the administration level.
                |             
                |         oLocked
                |             Input/Output parameter, is the lock status of the check button.
                |             
                |         oModified
                |             Output paramter which gives the status as boolean if the status is
                |             modified. If return code E_FAIL the values are not obtained. If return code
                |             S_OK the values are obtained.
                |             Refer to 
                | 
                |         SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimMoveLeaderModInfo(admin_level, o_locked)

    def get_dim_move_sub_part_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimMoveSubPartInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the DimMoveSubPart setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimMoveSubPartInfo(admin_level, o_locked)

    def get_dim_move_value_cre_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimMoveValueCreInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Move Value Creation setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimMoveValueCreInfo(admin_level, o_locked)

    def get_dim_move_value_mod_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimMoveValueModInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Move Value Modification setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimMoveValueModInfo(admin_level, o_locked)

    def get_dim_o_run_cre_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimORunCreInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Over Run Creation setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimORunCreInfo(admin_level, o_locked)

    def get_dim_o_run_mod_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimORunModInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Over Run Modification setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimORunModInfo(admin_level, o_locked)

    def get_dim_ori_default_symb_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimOriDefaultSymbInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Orientation Default Symbol
                |     setting parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimOriDefaultSymbInfo(admin_level, o_locked)

    def get_dim_snapping_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetDimSnappingInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension Snapping setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetDimSnappingInfo(admin_level, o_locked)

    def get_general_tol_class_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetGeneralTolClassInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Dimension general class tolerance setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetGeneralTolClassInfo(admin_level, o_locked)

    def get_highlight_def_annot_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetHighlightDefAnnotInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Highlight Def Annot setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetHighlightDefAnnotInfo(admin_level, o_locked)

    def get_noa_creation_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetNoaCreationInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Noa Creation setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetNoaCreationInfo(admin_level, o_locked)

    def get_non_semantic_always_upgrade_general_tol_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetNonSemanticAllwaysUpgradeGeneralTolInfo(CATBSTR
                | AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Non Semantic Allways Upgrade general
                |     tolerance setting parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetNonSemanticAllwaysUpgradeGeneralTolInfo(admin_level, o_locked)

    def get_non_semantic_always_upgrade_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetNonSemanticAllwaysUpgradeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Non Semantic Allways Upgrade setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetNonSemanticAllwaysUpgradeInfo(admin_level, o_locked)

    def get_non_semantic_dim_allowed_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetNonSemanticDimAllowedInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Non Semantic Dim Allowed setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetNonSemanticDimAllowedInfo(admin_level, o_locked)

    def get_non_semantic_marked_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetNonSemanticMarkedInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Non Semantic Marked setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetNonSemanticMarkedInfo(admin_level, o_locked)

    def get_non_semantic_tol_allowed_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetNonSemanticTolAllowedInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Non Semantic Tol Allowed setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetNonSemanticTolAllowedInfo(admin_level, o_locked)

    def get_parameters_in_tree_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetParametersInTreeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Parameters in tree setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetParametersInTreeInfo(admin_level, o_locked)

    def get_rotation_snap_angle_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetRotationSnapAngleInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Rotation Snap Angle setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetRotationSnapAngleInfo(admin_level, o_locked)

    def get_rotation_snap_auto_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetRotationSnapAutoInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Rotation Snap Auto setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetRotationSnapAutoInfo(admin_level, o_locked)

    def get_sect_pattern_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetSectPatternInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Pattern of Visu setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetSectPatternInfo(admin_level, o_locked)

    def get_select_published_geometry_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetSelectPublishedGeometryInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Select Published Geometry setting
                |     parameter value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetSelectPublishedGeometryInfo(admin_level, o_locked)

    def get_shifted_profile_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetShiftedProfileInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the Shifted Profile setting parameter
                |     value.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetShiftedProfileInfo(admin_level, o_locked)

    def get_true_dimension_colour(self, o_value_r: int, o_value_g: int, o_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub GetTrueDimensionColor(long oValueR,
                | long oValueG,
                | long oValueB)
                | 
                |     Returns the TrueDimensionColor parameter.

        :param int o_value_r:
        :param int o_value_g:
        :param int o_value_b:
        :rtype: None
        """
        return self.com_object.GetTrueDimensionColor(o_value_r, o_value_g, o_value_b)

    def get_true_dimension_colour_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub GetTrueDimensionColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the TrueDimensionColor
                |     parameter.
                |     Role:Retrieves the state of the TrueDimensionColor parameter in the current
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
        :param bool o_modified:
        :rtype: None
        """
        return self.com_object.GetTrueDimensionColorInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_true_dimension_color_info'
        # # vba_code = """
        # # Public Function get_true_dimension_color_info(fta_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     fta_setting_att.GetTrueDimensionColorInfo ioAdminLevel
        # #     get_true_dimension_color_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_true_dimension_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Func GetTrueDimensionInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the TrueDimension
                |     parameter.
                |     Role:Retrieves the state of the TrueDimension parameter in the current
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

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.com_object.GetTrueDimensionInfo(admin_level, o_locked)

    def set_alphabetic_order_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetAlphabeticOrderLock(boolean iLocked)
                | 
                |     Locks or unlocks the AlphabeticOrder setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetAlphabeticOrderLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_alphabetic_order_lock'
        # # vba_code = """
        # # Public Function set_alphabetic_order_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetAlphabeticOrderLock iLocked
        # #     set_alphabetic_order_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_analysis_display_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetAnalysisDisplayModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the AnalysisDisplayMode parameter.
                |     Role:Locks or unlocks the AnalysisDisplayMode parameter if it is possible
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
        return self.com_object.SetAnalysisDisplayModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_analysis_display_mode_lock'
        # # vba_code = """
        # # Public Function set_analysis_display_mode_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetAnalysisDisplayModeLock iLocked
        # #     set_analysis_display_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_angulaire_general_tol_class_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetAngulaireGeneralTolClassLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension general class parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetAngulaireGeneralTolClassLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_angulaire_general_tol_class_lock'
        # # vba_code = """
        # # Public Function set_angulaire_general_tol_class_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetAngulaireGeneralTolClassLock iLocked
        # #     set_angulaire_general_tol_class_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_annot_dim_invalid_colour(self, i_value_r: int, i_value_g: int, i_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetAnnotDimInvalidColor(long iValueR,
                | long iValueG,
                | long iValueB)
                | 
                |     Sets the AnnotDimInvalidColor parameter.

        :param int i_value_r:
        :param int i_value_g:
        :param int i_value_b:
        :rtype: None
        """
        return self.com_object.SetAnnotDimInvalidColor(i_value_r, i_value_g, i_value_b)

    def set_annot_dim_invalid_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetAnnotDimInvalidColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the AnnotDimInvalidColor parameter.
                |     Role:Locks or unlocks the AnnotDimInvalidColor parameter if it is possible
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
        return self.com_object.SetAnnotDimInvalidColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_annot_dim_invalid_color_lock'
        # # vba_code = """
        # # Public Function set_annot_dim_invalid_color_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetAnnotDimInvalidColorLock iLocked
        # #     set_annot_dim_invalid_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_annot_dim_invalid_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetAnnotDimInvalidLock(boolean iLocked)
                | 
                |     Retrieves environment informations for the AnnotDimInvalid
                |     parameter.
                |     Role:Retrieves the state of the AnnotDimInvalid parameter in the current
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

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetAnnotDimInvalidLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_annot_dim_invalid_lock'
        # # vba_code = """
        # # Public Function set_annot_dim_invalid_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetAnnotDimInvalidLock iLocked
        # #     set_annot_dim_invalid_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_annot_dim_on_deleted_geom_colour(self, i_value_r: int, i_value_g: int, i_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetAnnotDimOnDeletedGeomColor(long iValueR,
                | long iValueG,
                | long iValueB)
                | 
                |     Sets the AnnotDimOnDeletedGeomColor parameter.

        :param int i_value_r:
        :param int i_value_g:
        :param int i_value_b:
        :rtype: None
        """
        return self.com_object.SetAnnotDimOnDeletedGeomColor(i_value_r, i_value_g, i_value_b)

    def set_annot_dim_on_deleted_geom_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetAnnotDimOnDeletedGeomColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the AnnotDimOnDeletedGeomColor parameter.
                |     Role:Locks or unlocks the AnnotDimOnDeletedGeomColor parameter if it is
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
        return self.com_object.SetAnnotDimOnDeletedGeomColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_annot_dim_on_deleted_geom_color_lock'
        # # vba_code = """
        # # Public Function set_annot_dim_on_deleted_geom_color_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetAnnotDimOnDeletedGeomColorLock iLocked
        # #     set_annot_dim_on_deleted_geom_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_annot_dim_on_deleted_geom_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetAnnotDimOnDeletedGeomLock(boolean iLocked)
                | 
                |     Locks or unlocks the AnnotDimOnDeletedGeom parameter.
                |     Role:Locks or unlocks the AnnotDimOnDeletedGeom parameter if it is possible
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
        return self.com_object.SetAnnotDimOnDeletedGeomLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_annot_dim_on_deleted_geom_lock'
        # # vba_code = """
        # # Public Function set_annot_dim_on_deleted_geom_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetAnnotDimOnDeletedGeomLock iLocked
        # #     set_annot_dim_on_deleted_geom_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_annot_dim_on_unloaded_geom_colour(self, i_value_r: int, i_value_g: int, i_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetAnnotDimOnUnloadedGeomColor(long iValueR,
                | long iValueG,
                | long iValueB)
                | 
                |     Sets the AnnotDimOnUnloadedGeomColor parameter.

        :param int i_value_r:
        :param int i_value_g:
        :param int i_value_b:
        :rtype: None
        """
        return self.com_object.SetAnnotDimOnUnloadedGeomColor(i_value_r, i_value_g, i_value_b)

    def set_annot_dim_on_unloaded_geom_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetAnnotDimOnUnloadedGeomColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the AnnotDimOnUnloadedGeomColor
                |     parameter.
                |     Role:Locks or unlocks the AnnotDimOnUnloadedGeomColor parameter if it is
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
        return self.com_object.SetAnnotDimOnUnloadedGeomColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_annot_dim_on_unloaded_geom_color_lock'
        # # vba_code = """
        # # Public Function set_annot_dim_on_unloaded_geom_color_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetAnnotDimOnUnloadedGeomColorLock iLocked
        # #     set_annot_dim_on_unloaded_geom_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_annot_dim_on_unloaded_geom_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetAnnotDimOnUnloadedGeomLock(boolean iLocked)
                | 
                |     Locks or unlocks the AnnotDimOnUnloadedGeom parameter.
                |     Role:Locks or unlocks the AnnotDimOnUnloadedGeom parameter if it is
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
        return self.com_object.SetAnnotDimOnUnloadedGeomLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_annot_dim_on_unloaded_geom_lock'
        # # vba_code = """
        # # Public Function set_annot_dim_on_unloaded_geom_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetAnnotDimOnUnloadedGeomLock iLocked
        # #     set_annot_dim_on_unloaded_geom_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_annot_on_zero_z_setting_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetAnnotOnZeroZSettingLock(boolean iLocked)
                | 
                |     Locks or unlocks the AnnotOnZeroZSetting parameter.
                |     Role:Locks or unlocks the AnnotOnZeroZSetting parameter if it is possible
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
        return self.com_object.SetAnnotOnZeroZSettingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_annot_on_zero_z_setting_lock'
        # # vba_code = """
        # # Public Function set_annot_on_zero_z_setting_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetAnnotOnZeroZSettingLock iLocked
        # #     set_annot_on_zero_z_setting_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_body_hide_in_capture_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetBodyHideInCaptureLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension general class parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetBodyHideInCaptureLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_body_hide_in_capture_lock'
        # # vba_code = """
        # # Public Function set_body_hide_in_capture_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetBodyHideInCaptureLock iLocked
        # #     set_body_hide_in_capture_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_cat_fta_chamfer_general_tol_class_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetCATFTAChamferGeneralTolClassLock(boolean iLocked)
                | 
                |     Locks or unlocks the CATFTAChamferGeneralTolClass
                |     parameter.
                |     Role:Locks or unlocks the CATFTAChamferGeneralTolClass parameter if it is
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
        return self.com_object.SetCATFTAChamferGeneralTolClassLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_catfta_chamfer_general_tol_class_lock'
        # # vba_code = """
        # # Public Function set_catfta_chamfer_general_tol_class_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetCATFTAChamferGeneralTolClassLock iLocked
        # #     set_catfta_chamfer_general_tol_class_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_cat_fta_edges_colour(self, i_value_r: int, i_value_g: int, i_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetCATFTAEdgesColor(long iValueR,
                | long iValueG,
                | long iValueB)
                | 
                |     Sets the GetCATFTAEdgesColor parameter.

        :param int i_value_r:
        :param int i_value_g:
        :param int i_value_b:
        :rtype: None
        """
        return self.com_object.SetCATFTAEdgesColor(i_value_r, i_value_g, i_value_b)

    def set_cat_fta_edges_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetCATFTAEdgesColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the GetCATFTAEdgesColor parameter.
                |     Role:Locks or unlocks the GetCATFTAEdgesColor parameter if it is possible
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
        return self.com_object.SetCATFTAEdgesColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_catfta_edges_color_lock'
        # # vba_code = """
        # # Public Function set_catfta_edges_color_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetCATFTAEdgesColorLock iLocked
        # #     set_catfta_edges_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_cat_fta_edges_line_type_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetCATFTAEdgesLineTypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the CATFTAEdgesLineType parameter.
                |     Role:Locks or unlocks the CATFTAEdgesLineType parameter if it is possible
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
        return self.com_object.SetCATFTAEdgesLineTypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_catfta_edges_line_type_lock'
        # # vba_code = """
        # # Public Function set_catfta_edges_line_type_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetCATFTAEdgesLineTypeLock iLocked
        # #     set_catfta_edges_line_type_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_cat_fta_edges_thickness_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetCATFTAEdgesThicknessLock(boolean iLocked)
                | 
                |     Locks or unlocks the CATFTAEdgesThickness parameter.
                |     Role:Locks or unlocks the CATFTAEdgesThickness parameter if it is possible
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
        return self.com_object.SetCATFTAEdgesThicknessLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_catfta_edges_thickness_lock'
        # # vba_code = """
        # # Public Function set_catfta_edges_thickness_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetCATFTAEdgesThicknessLock iLocked
        # #     set_catfta_edges_thickness_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_cat_ftauf_auto_tolerancing_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetCATFTAUFAutoTolerancingLock(boolean iLocked)
                | 
                |     Locks or unlocks the CATFTAUFAutoTolerancing parameter.
                |     Role:Locks or unlocks the CATFTAUFAutoTolerancing parameter if it is
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
        return self.com_object.SetCATFTAUFAutoTolerancingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_catftauf_auto_tolerancing_lock'
        # # vba_code = """
        # # Public Function set_catftauf_auto_tolerancing_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetCATFTAUFAutoTolerancingLock iLocked
        # #     set_catftauf_auto_tolerancing_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_cat_fta_use_last_tolerances_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetCATFTAUseLastTolerancesLock(boolean iLocked)
                | 
                |     Locks or unlocks the CATFTAUseLastTolerances parameter.
                |     Role:Locks or unlocks the CATFTAUseLastTolerances parameter if it is
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
        return self.com_object.SetCATFTAUseLastTolerancesLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_catfta_use_last_tolerances_lock'
        # # vba_code = """
        # # Public Function set_catfta_use_last_tolerances_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetCATFTAUseLastTolerancesLock iLocked
        # #     set_catfta_use_last_tolerances_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_after_cre_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimAfterCreLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension After Creaation parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimAfterCreLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_after_cre_lock'
        # # vba_code = """
        # # Public Function set_dim_after_cre_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimAfterCreLock iLocked
        # #     set_dim_after_cre_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_after_mod_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimAfterModLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension After Modification parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimAfterModLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_after_mod_lock'
        # # vba_code = """
        # # Public Function set_dim_after_mod_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimAfterModLock iLocked
        # #     set_dim_after_mod_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_before_cre_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimBeforeCreLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Before Creation parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimBeforeCreLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_before_cre_lock'
        # # vba_code = """
        # # Public Function set_dim_before_cre_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimBeforeCreLock iLocked
        # #     set_dim_before_cre_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_before_mod_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimBeforeModLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Before Modification parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimBeforeModLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_before_mod_lock'
        # # vba_code = """
        # # Public Function set_dim_before_mod_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimBeforeModLock iLocked
        # #     set_dim_before_mod_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_blanking_cre_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimBlankingCreLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Blanking Creation parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimBlankingCreLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_blanking_cre_lock'
        # # vba_code = """
        # # Public Function set_dim_blanking_cre_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimBlankingCreLock iLocked
        # #     set_dim_blanking_cre_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_blanking_mod_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimBlankingModLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Blanking Modification parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimBlankingModLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_blanking_mod_lock'
        # # vba_code = """
        # # Public Function set_dim_blanking_mod_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimBlankingModLock iLocked
        # #     set_dim_blanking_mod_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_configure_snapping_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimConfigureSnappingLock(boolean iLocked)
                | 
                |     Locks or unlocks the DimConfigureSnapping parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimConfigureSnappingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_configure_snapping_lock'
        # # vba_code = """
        # # Public Function set_dim_configure_snapping_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimConfigureSnappingLock iLocked
        # #     set_dim_configure_snapping_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_constant_offset_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimConstantOffsetLock(boolean iLocked)
                | 
                |     Locks or unlocks the Constant Offset parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimConstantOffsetLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_constant_offset_lock'
        # # vba_code = """
        # # Public Function set_dim_constant_offset_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimConstantOffsetLock iLocked
        # #     set_dim_constant_offset_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_create_on_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimCreateOnLock(boolean iLocked)
                | 
                |     Locks or unlocks the DimCreateOn parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimCreateOnLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_create_on_lock'
        # # vba_code = """
        # # Public Function set_dim_create_on_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimCreateOnLock iLocked
        # #     set_dim_create_on_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_line_pos_value_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimLinePosValueLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Line Position Value parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimLinePosValueLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_line_pos_value_lock'
        # # vba_code = """
        # # Public Function set_dim_line_pos_value_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimLinePosValueLock iLocked
        # #     set_dim_line_pos_value_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_line_up_base_angle_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimLineUpBaseAngleLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Line Up Base Angle parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimLineUpBaseAngleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_line_up_base_angle_lock'
        # # vba_code = """
        # # Public Function set_dim_line_up_base_angle_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimLineUpBaseAngleLock iLocked
        # #     set_dim_line_up_base_angle_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_line_up_base_length_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimLineUpBaseLengthLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Line Up Base Length parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimLineUpBaseLengthLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_line_up_base_length_lock'
        # # vba_code = """
        # # Public Function set_dim_line_up_base_length_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimLineUpBaseLengthLock iLocked
        # #     set_dim_line_up_base_length_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_line_up_cumul_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimLineUpCumulLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Line Up Cululated parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimLineUpCumulLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_line_up_cumul_lock'
        # # vba_code = """
        # # Public Function set_dim_line_up_cumul_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimLineUpCumulLock iLocked
        # #     set_dim_line_up_cumul_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_line_up_funnel_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimLineUpFunnelLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Line Up Funnel parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimLineUpFunnelLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_line_up_funnel_lock'
        # # vba_code = """
        # # Public Function set_dim_line_up_funnel_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimLineUpFunnelLock iLocked
        # #     set_dim_line_up_funnel_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_line_up_offset_bet_dim_angle_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimLineUpOffsetBetDimAngleLock(boolean iLocked)
                | 
                |     Locks or unlocks the DimLineUpOffsetBetDimAngle parameter.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             Input value of the DimLineUpOffsetBetDimAngle (lock/unlock). If
                |             return code E_FAIL iLocked is not set. If return code S_OK iLocked is
                |             set.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimLineUpOffsetBetDimAngleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_line_up_offset_bet_dim_angle_lock'
        # # vba_code = """
        # # Public Function set_dim_line_up_offset_bet_dim_angle_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimLineUpOffsetBetDimAngleLock iLocked
        # #     set_dim_line_up_offset_bet_dim_angle_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_line_up_offset_bet_dim_length_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimLineUpOffsetBetDimLengthLock(boolean iLocked)
                | 
                |     Locks or unlocks the DimLineUpOffsetBetDimLength
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             Input value of the DimLineUpOffsetBetDimLength (lock/unlock). If
                |             return code E_FAIL iLocked is not set. If return code S_OK iLocked is
                |             set.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimLineUpOffsetBetDimLengthLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_line_up_offset_bet_dim_length_lock'
        # # vba_code = """
        # # Public Function set_dim_line_up_offset_bet_dim_length_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimLineUpOffsetBetDimLengthLock iLocked
        # #     set_dim_line_up_offset_bet_dim_length_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_line_up_offset_to_ref_angle_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimLineUpOffsetToRefAngleLock(boolean iLocked)
                | 
                |     Locks or unlocks the DimLineUpOffsetToRefAngle parameter.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             Input value of the DimLineUpOffsetToRefAngle (lock/unlock). If
                |             return code E_FAIL iLocked is not set. If return code S_OK iLocked is
                |             set.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimLineUpOffsetToRefAngleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_line_up_offset_to_ref_angle_lock'
        # # vba_code = """
        # # Public Function set_dim_line_up_offset_to_ref_angle_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimLineUpOffsetToRefAngleLock iLocked
        # #     set_dim_line_up_offset_to_ref_angle_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_line_up_offset_to_ref_length_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimLineUpOffsetToRefLengthLock(boolean iLocked)
                | 
                |     Locks or unlocks the DimLineUpOffsetToRefLength parameter.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             Input value of the DimLineUpOffsetToRefLength (lock/unlock). If
                |             return code E_FAIL iLocked is not set. If return code S_OK iLocked is
                |             set.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimLineUpOffsetToRefLengthLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_line_up_offset_to_ref_length_lock'
        # # vba_code = """
        # # Public Function set_dim_line_up_offset_to_ref_length_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimLineUpOffsetToRefLengthLock iLocked
        # #     set_dim_line_up_offset_to_ref_length_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_line_up_stack_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimLineUpStackLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Line Up Stack parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimLineUpStackLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_line_up_stack_lock'
        # # vba_code = """
        # # Public Function set_dim_line_up_stack_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimLineUpStackLock iLocked
        # #     set_dim_line_up_stack_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_manual_positioning_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimManualPositionningLock(boolean iLocked)
                | 
                |     Locks or unlocks the Manual Positionning parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimManualPositionningLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_manual_positionning_lock'
        # # vba_code = """
        # # Public Function set_dim_manual_positionning_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimManualPositionningLock iLocked
        # #     set_dim_manual_positionning_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_move_2d_part_cre_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimMove2dPartCreLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Move 2D Creation parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimMove2dPartCreLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_move2d_part_cre_lock'
        # # vba_code = """
        # # Public Function set_dim_move2d_part_cre_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimMove2dPartCreLock iLocked
        # #     set_dim_move2d_part_cre_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_move_2d_part_mod_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimMove2dPartModLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Move 2D Modification parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimMove2dPartModLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_move2d_part_mod_lock'
        # # vba_code = """
        # # Public Function set_dim_move2d_part_mod_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimMove2dPartModLock iLocked
        # #     set_dim_move2d_part_mod_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_move_dim_line_cre_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimMoveDimLineCreLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Move Dimension Line Creation parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimMoveDimLineCreLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_move_dim_line_cre_lock'
        # # vba_code = """
        # # Public Function set_dim_move_dim_line_cre_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimMoveDimLineCreLock iLocked
        # #     set_dim_move_dim_line_cre_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_move_dim_line_mod_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimMoveDimLineModLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Move Dimension Line Modification parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimMoveDimLineModLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_move_dim_line_mod_lock'
        # # vba_code = """
        # # Public Function set_dim_move_dim_line_mod_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimMoveDimLineModLock iLocked
        # #     set_dim_move_dim_line_mod_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_move_leader_cre_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimMoveLeaderCreLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension leader Creation parameter.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             Input value of the Dimension leader creation check box lock/unlock
                |             status. If return code E_FAIL iLocked is not set. If return code S_OK iLocked
                |             is set.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimMoveLeaderCreLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_move_leader_cre_lock'
        # # vba_code = """
        # # Public Function set_dim_move_leader_cre_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimMoveLeaderCreLock iLocked
        # #     set_dim_move_leader_cre_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_move_leader_mod_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimMoveLeaderModLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension leader modification
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             Input value of the Dimension leader modification check box
                |             (lock/unlock). If return code E_FAIL iLocked is not set. If return code S_OK
                |             iLocked is set.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimMoveLeaderModLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_move_leader_mod_lock'
        # # vba_code = """
        # # Public Function set_dim_move_leader_mod_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimMoveLeaderModLock iLocked
        # #     set_dim_move_leader_mod_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_move_sub_part_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimMoveSubPartLock(boolean iLocked)
                | 
                |     Locks or unlocks the DimMoveSubPart parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimMoveSubPartLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_move_sub_part_lock'
        # # vba_code = """
        # # Public Function set_dim_move_sub_part_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimMoveSubPartLock iLocked
        # #     set_dim_move_sub_part_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_move_value_cre_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimMoveValueCreLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Move Value Creation parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimMoveValueCreLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_move_value_cre_lock'
        # # vba_code = """
        # # Public Function set_dim_move_value_cre_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimMoveValueCreLock iLocked
        # #     set_dim_move_value_cre_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_move_value_mod_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimMoveValueModLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Move Value Modification parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimMoveValueModLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_move_value_mod_lock'
        # # vba_code = """
        # # Public Function set_dim_move_value_mod_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimMoveValueModLock iLocked
        # #     set_dim_move_value_mod_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_o_run_cre_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimORunCreLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Over Run Creation parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimORunCreLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_o_run_cre_lock'
        # # vba_code = """
        # # Public Function set_dim_o_run_cre_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimORunCreLock iLocked
        # #     set_dim_o_run_cre_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_o_run_mod_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimORunModLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Over Run Modification parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimORunModLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_o_run_mod_lock'
        # # vba_code = """
        # # Public Function set_dim_o_run_mod_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimORunModLock iLocked
        # #     set_dim_o_run_mod_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_ori_default_symb_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimOriDefaultSymbLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Orientation Default Symbol parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimOriDefaultSymbLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_ori_default_symb_lock'
        # # vba_code = """
        # # Public Function set_dim_ori_default_symb_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimOriDefaultSymbLock iLocked
        # #     set_dim_ori_default_symb_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dim_snapping_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetDimSnappingLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension Snapping parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetDimSnappingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dim_snapping_lock'
        # # vba_code = """
        # # Public Function set_dim_snapping_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetDimSnappingLock iLocked
        # #     set_dim_snapping_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_general_tol_class_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetGeneralTolClassLock(boolean iLocked)
                | 
                |     Locks or unlocks the Dimension general class parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetGeneralTolClassLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_general_tol_class_lock'
        # # vba_code = """
        # # Public Function set_general_tol_class_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetGeneralTolClassLock iLocked
        # #     set_general_tol_class_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_highlight_def_annot_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetHighlightDefAnnotLock(boolean iLocked)
                | 
                |     Locks or unlocks the Highlight Def Annot parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetHighlightDefAnnotLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_highlight_def_annot_lock'
        # # vba_code = """
        # # Public Function set_highlight_def_annot_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetHighlightDefAnnotLock iLocked
        # #     set_highlight_def_annot_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_noa_creation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetNoaCreationLock(boolean iLocked)
                | 
                |     Locks or unlocks the Noa Creation parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetNoaCreationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_noa_creation_lock'
        # # vba_code = """
        # # Public Function set_noa_creation_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetNoaCreationLock iLocked
        # #     set_noa_creation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_non_semantic_always_upgrade_general_tol_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetNonSemanticAllwaysUpgradeGeneralTolLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the Non Semantic Allways Upgrade general tolerance
                |     parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetNonSemanticAllwaysUpgradeGeneralTolLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_non_semantic_allways_upgrade_general_tol_lock'
        # # vba_code = """
        # # Public Function set_non_semantic_allways_upgrade_general_tol_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetNonSemanticAllwaysUpgradeGeneralTolLock iLocked
        # #     set_non_semantic_allways_upgrade_general_tol_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_non_semantic_always_upgrade_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetNonSemanticAllwaysUpgradeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Non Semantic Allways Upgrade parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetNonSemanticAllwaysUpgradeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_non_semantic_allways_upgrade_lock'
        # # vba_code = """
        # # Public Function set_non_semantic_allways_upgrade_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetNonSemanticAllwaysUpgradeLock iLocked
        # #     set_non_semantic_allways_upgrade_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_non_semantic_dim_allowed_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetNonSemanticDimAllowedLock(boolean iLocked)
                | 
                |     Locks or unlocks the Non Semantic Dim Allowed parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetNonSemanticDimAllowedLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_non_semantic_dim_allowed_lock'
        # # vba_code = """
        # # Public Function set_non_semantic_dim_allowed_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetNonSemanticDimAllowedLock iLocked
        # #     set_non_semantic_dim_allowed_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_non_semantic_marked_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetNonSemanticMarkedLock(boolean iLocked)
                | 
                |     Locks or unlocks the Non Semantic Marked parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetNonSemanticMarkedLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_non_semantic_marked_lock'
        # # vba_code = """
        # # Public Function set_non_semantic_marked_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetNonSemanticMarkedLock iLocked
        # #     set_non_semantic_marked_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_non_semantic_tol_allowed_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetNonSemanticTolAllowedLock(boolean iLocked)
                | 
                |     Locks or unlocks the Non Semantic Tol Allowed parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetNonSemanticTolAllowedLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_non_semantic_tol_allowed_lock'
        # # vba_code = """
        # # Public Function set_non_semantic_tol_allowed_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetNonSemanticTolAllowedLock iLocked
        # #     set_non_semantic_tol_allowed_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_parameters_in_tree_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetParametersInTreeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Parameters in tree parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetParametersInTreeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_parameters_in_tree_lock'
        # # vba_code = """
        # # Public Function set_parameters_in_tree_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetParametersInTreeLock iLocked
        # #     set_parameters_in_tree_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rotation_snap_angle_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetRotationSnapAngleLock(boolean iLocked)
                | 
                |     Locks or unlocks the Rotation Snap Angle parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetRotationSnapAngleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rotation_snap_angle_lock'
        # # vba_code = """
        # # Public Function set_rotation_snap_angle_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetRotationSnapAngleLock iLocked
        # #     set_rotation_snap_angle_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rotation_snap_auto_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetRotationSnapAutoLock(boolean iLocked)
                | 
                |     Locks or unlocks the Rotation Snap Auto parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetRotationSnapAutoLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rotation_snap_auto_lock'
        # # vba_code = """
        # # Public Function set_rotation_snap_auto_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetRotationSnapAutoLock iLocked
        # #     set_rotation_snap_auto_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_sect_pattern_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetSectPatternLock(boolean iLocked)
                | 
                |     Locks or unlocks the Pattern of Visu setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetSectPatternLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_sect_pattern_lock'
        # # vba_code = """
        # # Public Function set_sect_pattern_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetSectPatternLock iLocked
        # #     set_sect_pattern_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_select_published_geometry_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetSelectPublishedGeometryLock(boolean iLocked)
                | 
                |     Locks or unlocks the Select Published Geometry parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetSelectPublishedGeometryLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_select_published_geometry_lock'
        # # vba_code = """
        # # Public Function set_select_published_geometry_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetSelectPublishedGeometryLock iLocked
        # #     set_select_published_geometry_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shifted_profile_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetShiftedProfileLock(boolean iLocked)
                | 
                |     Locks or unlocks the Shifted Profile parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.com_object.SetShiftedProfileLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shifted_profile_lock'
        # # vba_code = """
        # # Public Function set_shifted_profile_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetShiftedProfileLock iLocked
        # #     set_shifted_profile_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_true_dimension_color(self, i_value_r: int, i_value_g: int, i_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetTrueDimensionColor(long iValueR,
                | long iValueG,
                | long iValueB)
                | 
                |     Sets the TrueDimensionColor parameter.

        :param int i_value_r:
        :param int i_value_g:
        :param int i_value_b:
        :rtype: None
        """
        return self.com_object.SetTrueDimensionColor(i_value_r, i_value_g, i_value_b)

    def set_true_dimension_color_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetTrueDimensionColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the TrueDimensionColor parameter.
                |     Role:Locks or unlocks the TrueDimensionColor parameter if it is possible in
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
        return self.com_object.SetTrueDimensionColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_true_dimension_color_lock'
        # # vba_code = """
        # # Public Function set_true_dimension_color_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetTrueDimensionColorLock iLocked
        # #     set_true_dimension_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_true_dimension_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub SetTrueDimensionLock(boolean iLocked)
                | 
                |     Locks or unlocks the TrueDimension parameter.
                |     Role:Locks or unlocks the TrueDimension parameter if it is possible in the
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
        return self.com_object.SetTrueDimensionLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_true_dimension_lock'
        # # vba_code = """
        # # Public Function set_true_dimension_lock(fta_setting_att)
        # #     Dim iLocked (2)
        # #     fta_setting_att.SetTrueDimensionLock iLocked
        # #     set_true_dimension_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'FtaSettingAtt(name="{self.name}")'
