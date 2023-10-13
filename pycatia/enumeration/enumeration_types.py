#! /usr/bin/python3.9

abq_conc_force_load_type = (
    "POINTLOAD",
    "DISTRIBUTEDLOAD",
    "LOADDENSITY",
)

abq_dat_output_var_type = (
    "ABQDATOUTPUTTYPE_NODE",
    "ABQDATOUTPUTTYPE_ELEMENT",
    "ABQDATOUTPUTTYPE_CONTACT",
    "ABQDATOUTPUTTYPE_ENERGY",
)

abq_entity_type = (
    "ABQ_NONE",
    "ABQ_NODE",
    "ABQ_ELEMENT",
)

abq_local_csys_type = (
    "ABQ_CARTESIAN",
    "ABQ_CYLINDRICAL",
    "ABQ_SPHERICAL",
    "ABQ_DEFAULTAXIS",
)

abq_ms_frequency_type = (
    "ABQ_INTERVAL",
    "ABQ_INCREMENT",
)

abq_ms_target_method = (
    "ABQ_BELOW_MIN",
    "ABQ_UNIFORM",
    "ABQ_SET_EQUAL",
)

abq_output_at_sec_pts = (
    "ABQDEFAULTSECPTS",
    "ABQALLSECPTS",
)

abq_output_request_type = (
    "ABQFIELD",
    "ABQHISTORY",
    "ABQDATA",
)

abq_output_variable_type = (
    "ABQPRESELECTEDEFVAR",
    "ABQALLVAR",
)

abq_requested_modes_option = (
    "ABQ_ALL",
    "ABQ_VALUE",
)

abq_restart_option = (
    "ABQ_RESTART_NONE",
    "ABQ_RESTART_EVERYINC",
    "ABQ_RESTART_SPECINC",
    "ABQ_RESTART_NUMINT",
    "ABQ_RESTART_LASTINC",
)

abq_restart_read_option = (
    "ABQ_RESTART_END_OF_STEP",
    "ABQ_RESTART_INTERVAL",
)

abq_restart_read_step_sel_option = (
    "ABQ_STEP_OBJECT",
    "ABQ_STEP_NUMBER",
)

accuracy_type = (
    "ACCURACY_TYPE_DISTANCE",
    "ACCURACY_TYPE_SPEED",
)

adjust_method_type = (
    "NOADJUST",
    "OVERCLOSED",
    "TOLERANCE",
)

auto_time_increment_method = (
    "ABQ_ATI_GLOBAL",
    "ABQ_ATI_ELEMENT_BY_ELEMENT",
)

cat3_d_color_inheritance_mode = (
    "cat3DColorInheritanceModeOff",
    "cat3DColorInheritanceModeOn",
)

cat3_d_xml_geom_representation_type = (
    "cat3DXmlExact",
    "cat3DXmlTessellation",
    "cat3DXmlCompressedTessellation",
    "cat3DXmlDynamicTessellation",
    "cat3DXmlStaticTessellation",
    "cat3DXmlXmlTessellation",
)

cat3_d_xml_ppr_save_config = (
    "cat3DXmlProductAndResourceList",
    "cat3DXmlProductList",
    "cat3DXmlResourceList",
)

cat_algorithm_type = (
    "catSimulatedAnnealing",
    "catGradient",
    "catCAAalgorithm",
    "catLocalForConstraints",
)

cat_analysis_set_search_type = (
    "catAnalysisSetSearchIn",
    "catAnalysisSetSearchOut",
    "catAnalysisSetSearchNeutral",
    "catAnalysisSetSearchAll",
)

cat_analysis_set_type = (
    "catAnalysisSetIn",
    "catAnalysisSetOut",
    "catAnalysisSetNeutral",
)

cat_annotated_view_behavior = (
    "CatAnnotatedViewBehaviorLink",
    "CatAnnotatedViewBehaviorUnlink",
)

cat_annotation_set_type = (
    "catAnnotationSetStandard",
    "catAnnotationSetLight",
    "catAnnotationSetResult",
)

cat_arrange_style = (
    "catArrangeCascade",
    "catArrangeTiledHorizontal",
    "catArrangeTiledVertical",
)

cat_arrangement_area_visu_mode = (
    "CatArrangementAreaVisuModeFlat",
    "CatArrangementAreaVisuModeSolid",
)

cat_arrangement_item_res_visu_mode = (
    "CatArrangementItemReservationVisuModeAxis",
    "CatArrangementItemReservationVisuModeFlat",
    "CatArrangementItemReservationVisuModeSolid",
)

cat_arrangement_route_section = (
    "CatArrangementRouteSectionNone",
    "CatArrangementRouteSectionRectangular",
    "CatArrangementRouteSectionRound",
    "CatArrangementRouteSectionFlatOval",
    "CatArrangementRouteSectionRadiusCorner",
    "CatArrangementRouteSectionDoubleRidge",
)

cat_arrangement_route_visu_mode = (
    "CatArrangementRouteVisuModeCurve",
    "CatArrangementRouteVisuModeFlat",
    "CatArrangementRouteVisuModeSolid",
)

cat_asm_auto_switch_to_design_mode = (
    "catAutoSwitchAvailable",
    "catAutoSwitchUnavailable",
)

cat_asm_constraint_creation_mode = (
    "catUseAnyGeometry",
    "catUsePublishedGeometryChildLevel",
    "catUsePublishedGeometryAnyLevel",
)

cat_asm_extend_move_to_fix_t = (
    "catNeverExtendMoveToFixT",
    "catAskIfExtendMoveToFixT",
    "catAlwaysExtendMoveToFixT",
)

cat_asm_paste_component_mode = (
    "catPasteWithoutCsts",
    "catPasteWithCstOnCopy",
    "catPasteWithCstOnCut",
    "catPasteWithCstOnCopyAndCut",
)

cat_asm_quick_constraint_mode = (
    "catSpecifiedOrder",
    "catVerifiedConstraintFirst",
)

cat_asm_redundancy_mode = (
    "catUnChecked",
    "catChecked",
)

cat_asm_update_mode = (
    "catManualUpdate",
    "catAutomaticUpdate",
)

cat_asm_update_status_compute_mode = (
    "catManualCompute",
    "catAutomaticCompute",
)

cat_axis_orientation_type = (
    "catSamCoordinateSystem_Cartesian",
    "catSamCoordinateSystem_Cylindrical",
    "catSamCoordinateSystem_Spherical",
    "catSamCoordinateSystem_Undefined",
)

cat_axis_system_axis_type = (
    "catAxisSystemAxisSameDirection",
    "catAxisSystemAxisByCoordinates",
    "catAxisSystemAxisOppositeDirection",
)

cat_axis_system_main_type = (
    "catAxisSystemStandard",
    "catAxisSystemAxisRotation",
    "catAxisSystemEulerAngles",
    "catAxisSystemExplicit",
)

cat_axis_system_origin_type = (
    "catAxisSystemOriginByPoint",
    "catAxisSystemOriginByCoordinates",
)

cat_back_face_culling_mode = (
    "CATBackFaceCullingOnSolidFaces",
    "CATBackFaceCullingOnAllFaces",
    "CATBackFaceCullingOnStandAloneFaces",
    "CATBackFaceCullingOnNoFaces",
)

cat_banner_position = (
    "catBannerPositionNone",
    "catBannerPositionBottom",
    "catBannerPositionTop",
    "catBannerPositionLeft",
    "catBannerPositionRight",
)

cat_blanking_mode = (
    "catBlankingInactive",
    "catBlankingActive",
    "catBlankingOnGeom",
)

cat_camera_type = (
    "catCamera2D",
    "catCamera3D",
)

cat_capture_format = (
    "catCaptureFormatCGM",
    "catCaptureFormatEMF",
    "catCaptureFormatTIFF",
    "catCaptureFormatTIFFGreyScale",
    "catCaptureFormatBMP",
    "catCaptureFormatJPEG",
)

cat_chamfer_mode = (
    "catTwoLengthChamfer",
    "catLengthAngleChamfer",
)

cat_chamfer_orientation = (
    "catNoReverseChamfer",
    "catReverseChamfer",
)

cat_chamfer_propagation = (
    "catTangencyChamfer",
    "catMinimalChamfer",
)

cat_circular_pattern_parameters = (
    "catInstancesandAngularSpacing",
    "catCompleteCrown",
    "catUnequalAngularSpacing",
)

cat_clash_computation_type = (
    "catClashComputationTypeBetweenAll",
    "catClashComputationTypeInsideOne",
    "catClashComputationTypeAgainstAll",
    "catClashComputationTypeBetweenTwo",
)

cat_clash_export_type = (
    "CatClashExportTypeXMLResultOnly",
)

cat_clash_import_type = (
    "CatClashImportTypeClashOnly",
    "CatClashImportTypeStructureAndClash",
)

cat_clash_interference_type = (
    "catClashInterferenceTypeContact",
    "catClashInterferenceTypeClearance",
    "catClashInterferenceAuthorizedPenetration",
    "catClashInterferenceCaseRule",
)

cat_clipping_frame_reframe_on_mode = (
    "catOnViewContent",
    "catOnViewBackground",
)

cat_clipping_mode = (
    "catClippingModeClear",
    "catClippingModeNear",
    "catClippingModeFar",
    "catClippingModeNearAndFar",
)

cat_conflict_comparison = (
    "catConflictComparisonNew",
    "catConflictComparisonOld",
    "catConflictComparisonNo",
)

cat_conflict_status = (
    "catConflictStatusNotInspected",
    "catConflictStatusRelevant",
    "catConflictStatusIrrelevant",
    "catConflictStatusSolved",
)

cat_conflict_type = (
    "catConflictTypeClash",
    "catConflictTypeContact",
    "catConflictTypeClearance",
)

cat_constraint_angle_sector = (
    "catCstAngleSector0",
    "catCstAngleSector1",
    "catCstAngleSector2",
    "catCstAngleSector3",
)

cat_constraint_dist_config = (
    "catCstDCUnspec",
    "catCstDCParallel",
    "catCstDCParallelSameOrient",
    "catCstDCParallelOppOrient",
)

cat_constraint_dist_direction = (
    "catCstDistDirectionNone",
    "catCstDistDirection1",
    "catCstDistDirection2",
    "catCstDistDirection3",
)

cat_constraint_mode = (
    "catCstModeDrivingDimension",
    "catCstModeDrivenDimension",
)

cat_constraint_orientation = (
    "catCstOrientSame",
    "catCstOrientOpposite",
    "catCstOrientUndefined",
)

cat_constraint_ref_axis = (
    "catCstRefAxisX",
    "catCstRefAxisY",
    "catCstRefAxisZ",
)

cat_constraint_ref_type = (
    "catCstRefTypeRelative",
    "catCstRefTypeFixInSpace",
)

cat_constraint_side = (
    "catCstSidePositive",
    "catCstSideNegative",
    "catCstSideSameAsValue",
    "catCstSideOppositeToValue",
    "catCstSideUndefined",
)

cat_constraint_status = (
    "catCstStatusOK",
    "catCstStatusKOStronglyNotSatisfied",
    "catCstStatusKOWrongOrientOrSide",
    "catCstStatusKOWrongValue",
    "catCstStatusKOWrongGeomEltType",
    "catCstStatusKOBroken",
)

cat_constraint_type = (
    "catCstTypeReference",
    "catCstTypeDistance",
    "catCstTypeOn",
    "catCstTypeConcentricity",
    "catCstTypeTangency",
    "catCstTypeLength",
    "catCstTypeAngle",
    "catCstTypePlanarAngle",
    "catCstTypeParallelism",
    "catCstTypeAxisParallelism",
    "catCstTypeHorizontality",
    "catCstTypePerpendicularity",
    "catCstTypeAxisPerpendicularity",
    "catCstTypeVerticality",
    "catCstTypeRadius",
    "catCstTypeSymmetry",
    "catCstTypeMidPoint",
    "catCstTypeEquidistance",
    "catCstTypeMajorRadius",
    "catCstTypeMinorRadius",
    "catCstTypeSurfContact",
    "catCstTypeLinContact",
    "catCstTypePoncContact",
    "catCstTypeChamfer",
    "catCstTypeChamferPerpend",
    "catCstTypeAnnulContact",
    "catCstTypeCylinderRadius",
    "catCstTypeStContinuity",
    "catCstTypeStDistance",
    "catCstTypeSdContinuity",
    "catCstTypeSdShape",
)

cat_cs_hole_mode = (
    "catCSModeDepthAngle",
    "catCSModeDepthDiameter",
    "catCSModeAngleDiameter",
)

cat_dedicated_filter_type = (
    "catDisplayInBackground",
    "catMaskInBackground",
)

cat_description_length_type = (
    "ShortText",
    "LongText",
)

cat_dft_weld_finish_symbol = (
    "catFinishWeldingNone",
    "catDftLetterCWelding",
    "catDftLetterFWelding",
    "catDftLetterGWelding",
    "catDftLetterHWelding",
    "catDftLetterMWelding",
    "catDftLetterRWelding",
    "catDftLetterUWelding",
)

cat_dft_welding_tail = (
    "catDftWeldingTailNO",
    "catDftWeldingTailYES",
)

cat_dim_analyse = (
    "catDimOnGenItems",
    "catUnUpdatableDim",
    "catFakeDim",
    "catDrivingDim",
    "catBrokenDim",
    "catTrueDim",
    "catBasic",
    "cat3DDrivableDim",
    "cat3DDrivedDim",
    "catIsolatedDim",
    "catDimOnHideGeom",
    "cat3DFeatureDim",
)

cat_dim_dual_display = (
    "catDualNone",
    "catDualBellow",
    "catDualFractional",
    "catDualSideBySide",
)

cat_dim_fake = (
    "catDimFakeNone",
    "catDimFakeNumValue",
    "catDimFakeText",
)

cat_dim_frame = (
    "catFraNone",
    "catFraCircle",
    "catFraScoredCircle",
    "catFraDiamondShaped",
    "catFraSquare",
    "catFraRectangle",
    "catFraOblong",
    "catFraRightFlag",
    "catFraRightTriangle",
)

cat_dim_framed_element = (
    "catFraValue",
    "catFraValueTol",
    "catFraValueTolText",
)

cat_dim_framed_group = (
    "catFraMain",
    "catFraDual",
    "catFraMainAndDual",
    "catFraBoth",
)

cat_dim_line_graph_rep = (
    "catDimLine1Part",
    "catDimLine2Parts",
    "catDimLineLeader1Part",
    "catDimLineLeader2Part",
)

cat_dim_line_rep = (
    "catDimUndef",
    "catDimHoriz",
    "catDimVert",
    "catDimAuto",
    "catDimUserDefined",
    "catDimTrueDim",
    "catDimParallel",
    "catDimOffset",
)

cat_dim_mode = (
    "catDimClassical",
    "catDimCumulate",
    "catDimHalfDim",
    "catDimChained",
    "catDimStacked",
    "catDimCumulatesystem",
    "catDimHalfDimSystem",
)

cat_dim_orientation = (
    "catHorizontal",
    "catVertical",
    "catParallel",
    "catPerpandicular",
    "catAngle",
)

cat_dim_reference = (
    "catScreen",
    "catView",
    "catDimLine",
)

cat_dim_score = (
    "catDimScoreNone",
    "catDimUnderScored",
    "catDimScored",
    "catCATDrwDimOverScored",
)

cat_dim_symbols = (
    "catDimSymbNone",
    "catDimSymbOpenArrow",
    "catDimSymbClosedArrow",
    "catDimSymbFilledArrow",
    "catDimSymbSymArrow",
    "catDimSymbSlash",
    "catDimSymbCircle",
    "catDimSymbFilledCircle",
    "catDimSymbScoredCircle",
    "catDimSymbCircledCross",
    "catDimSymbTriangle",
    "catDimSymbFilledTriangle",
    "catDimSymbCross",
    "catDimSymbXCross",
)

cat_dim_type = (
    "catDimDistance",
    "catDimDistanceOffset",
    "catDimLength",
    "catDimLengthCurvilinear",
    "catDimAngle",
    "catDimRadius",
    "catDimRadiusTangent",
    "catDimRadiusCylinder",
    "catDimRadiusEdge",
    "catDimDiameter",
    "catDimDiameterTangent",
    "catDimDiameterCylinder",
    "catDimDiameterEdge",
    "catDimDiameterCone",
    "catDimChamfer",
    "catDimSlope",
    "catDimLengthCircular",
    "catDimRadiusFillet",
    "catDimDiameterTorus",
    "catDimRadiusTorus",
    "catDimDistanceMin",
)

cat_distance_computation_type = (
    "catDistanceComputationTypeInsideOne",
    "catDistanceComputationTypeAgainstAll",
    "catDistanceComputationTypeBetweenTwo",
)

cat_distance_measure_type = (
    "catDistanceMeasureTypeMinimum",
    "catDistanceMeasureTypeAlongX",
    "catDistanceMeasureTypeAlongY",
    "catDistanceMeasureTypeAlongZ",
    "catDistanceMeasureTypeBand",
)

cat_dmu_group_preview_hidden_objects_display_mode = (
    "CatDMUGroupPreviewShowHidden",
    "CatDMUGroupPreviewShowHiddenCustom",
)

cat_doc_contextual_priority = (
    "CATDocContextualTechDoc",
    "CATDocContextualUserComp",
)

cat_draft_mode = (
    "catStandardDraftMode",
    "catReflectKeepFaceDraftMode",
    "catReflectKeepEdgeDraftMode",
)

cat_draft_multiselection_mode = (
    "catNoneDraftMultiselectionMode",
    "catDraftMultiselectionByNeutralMode",
)

cat_draft_neutral_propagation_mode = (
    "catNoneDraftNeutralPropagationMode",
    "catSmoothDraftNeutralPropagationMode",
)

cat_drawing_standard = (
    "catANSI",
    "catISO",
    "catJIS",
)

cat_drawing_view_type = (
    "catViewBackground",
    "catViewFront",
    "catViewLeft",
    "catViewRight",
    "catViewTop",
    "catViewBottom",
    "catViewRear",
    "catViewAuxiliary",
    "catViewIsom",
    "catViewSection",
    "catViewSectionCut",
    "catViewDetail",
    "catViewUntyped",
    "catViewMain",
    "catViewPure_Sketch",
    "catViewUnfolded",
)

cat_drw_new_sheet_from = (
    "catDrwFirstSheet",
    "catDrwStyle",
)

cat_dxf_export_blocks_enum = (
    "catDxfExportBlocksEnumNone",
    "catDxfExportBlocksEnum1Level",
    "catDxfExportBlocksEnumFull",
)

cat_dxf_export_mode_enum = (
    "catDxfExportModeEnumSemantic",
    "catDxfExportModeEnumGraphic",
)

cat_dxf_export_sheets_enum = (
    "catDxfExportSheetsEnumAll",
    "catDxfExportSheetsEnumOnlyCurrent",
)

cat_dxf_export_version_enum = (
    "catDxfExportVersionEnumR12",
    "catDxfExportVersionEnumR13",
    "catDxfExportVersionEnumR14",
    "catDxfExportVersionEnum2000",
    "catDxfExportVersionEnum2004",
    "catDxfExportVersionEnum2007",
)

cat_dxf_import_create_end_points_enum = (
    "catDxfImportCreateEndPointsEnumNever",
    "catDxfImportCreateEndPointsEnumFewEntities",
    "catDxfImportCreateEndPointsEnumAlways",
)

cat_dxf_import_dimensions_enum = (
    "catDxfImportDimensionsEnumDimensions",
    "catDxfImportDimensionsEnumDetails",
    "catDxfImportDimensionsEnumGeometry",
)

cat_dxf_import_unit_enum = (
    "catDxfImportUnitEnumMillimeter",
    "catDxfImportUnitEnumCentimeter",
    "catDxfImportUnitEnumMeter",
    "catDxfImportUnitEnumInch",
    "catDxfImportUnitEnumFoot",
    "catDxfImportUnitEnumScaleFactor",
    "catDxfImportUnitEnumAutomatic",
)

cat_electronic_type = (
    "BOARD",
    "PANEL",
    "COMPONENT",
    "AREA",
    "PCBHOLE",
    "PCBPATTERN",
    "NOPCBBEHAVIOUR",
)

cat_file_selection_mode = (
    "CatFileSelectionModeOpen",
    "CatFileSelectionModeSave",
)

cat_file_type = (
    "catFileTypeText",
    "catFileTypeMotif",
    "catFileTypeHTML",
)

cat_fillet_bitangency_type = (
    "catSphereBitangencyType",
    "catCircleBitangencyType",
)

cat_fillet_boundary_relimitation = (
    "catAutomaticFilletBoundaryRelimitation",
    "catUVFilletBoundaryRelimitation",
    "catConnectFilletBoundaryRelimitation",
    "catMinimumFilletBoundaryRelimitation",
    "catMaximumFilletBoundaryRelimitation",
)

cat_fillet_edge_propagation = (
    "catMinimalFilletEdgePropagation",
    "catTangencyFilletEdgePropagation",
)

cat_fillet_representation = (
    "catFilletRepNone",
    "catFilletRepBoundary",
    "catFilletRepSymbolic",
    "catFilletRepOriginalEdge",
    "catFilletRepProjectedOriginalEdge",
)

cat_fillet_trim_support = (
    "catTrimFilletSupport",
    "catNoTrimFilletSupport",
)

cat_fillet_variation = (
    "catLinearFilletVariation",
    "catCubicFilletVariation",
)

cat_fitting_shuttle_vector = (
    "CATFittingShuttleVectorX",
    "CATFittingShuttleVectorY",
    "CATFittingShuttleVectorZ",
)

cat_full_scene_anti_aliasing_mode = (
    "CATFSAAMode_Deactivated",
    "CATFSAAMode_2xSuperSampling",
    "CATFSAAMode_4xSuperSampling",
    "CATFSAAMode_8xSuperSampling",
    "CATFSAAMode_16xSuperSampling",
)

cat_funct_orientation_direction = (
    "CATFunctNotOriented",
    "CATFunctOrientedUnidirectional",
    "CATFunctOrientedBidirectional",
)

cat_gen_conferencing = (
    "NetMeeting",
    "Backbone",
)

cat_gen_data_save = (
    "NoAutoBackup",
    "AutoBackupEvery",
    "IncrBackup",
)

cat_gen_ui_style = (
    "UIStyleP1",
    "UIStyleP2",
    "UIStyleP3",
)

cat_geometric_type = (
    "catGeoTypeUnknown",
    "catGeoTypeAxis2D",
    "catGeoTypePoint2D",
    "catGeoTypeLine2D",
    "catGeoTypeControlPoint2D",
    "catGeoTypeCircle2D",
    "catGeoTypeHyperbola2D",
    "catGeoTypeParabola2D",
    "catGeoTypeEllipse2D",
    "catGeoTypeSpline2D",
    "catGeoTypePoint",
    "catGeoTypeLine",
    "catGeoTypePlane",
)

cat_grid_position_mode = (
    "catGridPositionMode_Absolute",
    "catGridPositionMode_Relative",
)

cat_hidden_line_mode = (
    "catHlrModeOff",
    "catHlrModeOn",
)

cat_hole_anchor_mode = (
    "catExtremPointHoleAnchor",
    "catMiddlePointHoleAnchor",
)

cat_hole_bottom_type = (
    "catFlatHoleBottom",
    "catVHoleBottom",
    "catTrimmedHoleBottom",
)

cat_hole_thread_side = (
    "catRightThreadSide",
    "catLeftThreadSide",
)

cat_hole_thread_standard = (
    "catHoleMetricThinPitch",
    "catHoleMetricThickPitch",
)

cat_hole_threading_mode = (
    "catThreadedHoleThreading",
    "catSmoothHoleThreading",
)

cat_hole_type = (
    "catSimpleHole",
    "catTaperedHole",
    "catCounterboredHole",
    "catCountersunkHole",
    "catCounterdrilledHole",
)

cat_ig2_export_mode_enum = (
    "catIg2ExportModeEnumSemantic",
    "catIg2ExportModeEnumStructured",
    "catIg2ExportModeEnumGraphic",
)

cat_ig2_export_sheets_enum = (
    "catIg2ExportSheetsEnumAll",
    "catIg2ExportSheetsEnumOnlyCurrent",
)

cat_ig2_import_create_end_points_enum = (
    "catIg2ImportCreateEndPointsEnumNever",
    "catIg2ImportCreateEndPointsEnumFewEntities",
    "catIg2ImportCreateEndPointsEnumAlways",
)

cat_ig2_import_destination_view_enum = (
    "catIg2ImportDestinationViewEnumWorkingViews",
    "catIg2ImportDestinationViewEnumBackground",
)

cat_ig2_import_dimensions_enum = (
    "catIg2ImportDimensionsEnumDimensions",
    "catIg2ImportDimensionsEnumDetails",
    "catIg2ImportDimensionsEnumGeometry",
)

cat_ig2_import_unit_enum = (
    "catIg2ImportUnitEnumMillimeter",
    "catIg2ImportUnitEnumCentimeter",
    "catIg2ImportUnitEnumMeter",
    "catIg2ImportUnitEnumInch",
    "catIg2ImportUnitEnumFoot",
    "catIg2ImportUnitEnumAutomatic",
)

cat_image_rotation = (
    "catImageNoRotation",
    "catImageRotation90",
    "catImageRotation180",
    "catImageRotation270",
    "catImageBestRotation",
)

cat_image_view_mode = (
    "catImageModeOff",
    "catImageModeHRD",
)

cat_insure_view_names_uniqueness_scope = (
    "catInSheet",
    "catInLayout",
)

cat_justification = (
    "catLeft",  # The text is left justified.
    "catCenter",  # The text is centered.
    "catRight",  # The text is right justified.
)

cat_lighting_mode = (
    "catInfiniteLightSource",
    "catNeonLightSource",
)

cat_limit_mode = (
    "catOffsetLimit",
    "catUpToNextLimit",
    "catUpToLastLimit",
    "catUpToPlaneLimit",
    "catUpToSurfaceLimit",
    "catUpThruNextLimit",
)

cat_manip_auto_insert_mode = (
    "CATOnMouseRelease",
    "CATWhileMouseMoving",
)

cat_manip_clash_mode = (
    "CATManipClashModeNo",
    "CATManipClashModeOn",
    "CATManipClashModeStop",
)

cat_manufacturing_precedence_type = (
    "catPrecedenceTypeJustBefore",
    "catPrecedenceTypeBefore",
)

cat_marker2_d_type = (
    "catMarker2DTypeLine",
    "catMarker2DTypeArrow",
    "catMarker2DTypeRectangle",
    "catMarker2DTypeCircle",
    "catMarker2DTypeFreeHand",
    "catMarker2DTypeText",
    "catMarker2DTypePicture",
)

cat_marker3_d_type = (
    "catMarker3DTypeText",
)

cat_marker_text_orientation = (
    "CatMarkerTextOrientationRight",
    "CatMarkerTextOrientationUp",
    "CatMarkerTextOrientationLeft",
    "CatMarkerTextOrientationDown",
)

cat_measurable_name = (
    "CatMeasurableUnknown",
    "CatMeasurable",
    "CatMeasurableVolume",
    "CatMeasurableSurface",
    "CatMeasurableCylinder",
    "CatMeasurableSphere",
    "CatMeasurableCone",
    "CatMeasurablePlane",
    "CatMeasurableCurve",
    "CatMeasurableCircle",
    "CatMeasurableLine",
    "CatMeasurablePoint",
    "CatMeasurableAxisSystem",
)

cat_merge_mode = (
    "catMergeOff",
    "catMergeOn",
)

cat_multi_selection_mode = (
    "CATMonoSel",
    "CATMultiSelTriggWhenSelPerf",
    "CATMultiSelTriggWhenUserValidatesSelection",
)

cat_navigation_style = (
    "catNavigationExamine",
    "catNavigationWalk",
    "catNavigationFly",
)

cat_optimization_type = (
    "catMinimum",
    "catMaximum",
    "catTargetValue",
    "catOnlyBoundedVariation",
    "catNone",
    "catCstOnly",
)

cat_out_put_format_type = (
    "KWEHtml",
    "KWEText",
    "KWEPrint",
    "KWEEmail",
)

cat_paper_orientation = (
    "catPaperPortrait",
    "catPaperLandscape",
    "catPaperBestFit",
)

cat_paper_size = (
    "catPaperLetter",
    "catPaperLegal",
    "catPaperA0",
    "catPaperA1",
    "catPaperA2",
    "catPaperA3",
    "catPaperA4",
    "catPaperA",
    "catPaperB",
    "catPaperC",
    "catPaperD",
    "catPaperE",
    "catPaperF",
    "catPaperUser",
)

cat_part_elements_naming_mode = (
    "catNoNamingCheck",
    "catNamingCheckUnderSameNode",
    "catNamingCheckWithinUIActiveObject",
)

cat_part_surface_elements_location = (
    "catPartBodyLocation",
    "catXGSLocation",
)

cat_part_update_mode = (
    "catManualUpdate",
    "catAutomaticUpdate",
)

cat_picture_format = (
    "catPictureNONE",
    "catPicturePNG",
    "catPictureJPEG",
    "catPictureCCITTG3",
)

cat_points_projection_mode = (
    "catPointsProjectionModeOff",
    "catPointsProjectionModeOn",
)

cat_print_color = (
    "catColorTrueColor",
    "catColorGreyScale",
    "catColorMonochrome",
)

cat_print_line_cap = (
    "catPrintFlat",
    "catPrintSquare",
    "catPrintRound",
)

cat_print_line_specification = (
    "catPrintAbsolute",
    "catPrintScaled",
    "catPrintNoThickness",
)

cat_print_quality = (
    "catPrintQualityDraft",
    "catPrintQualityLow",
    "catPrintQualityMedium",
    "catPrintQualityHigh",
    "catPrintQualityCustom",
)

cat_print_rendering_mode = (
    "catPrintRenderingModeDefault",
    "catPrintRenderingModeWireframe",
    "catPrintRenderingModeHiddenLineRemoval",
    "catPrintRenderingModeShadingWithTriangles",
    "catPrintRenderingModeDynamicHiddenLineRemoval",
    "catPrintRenderingModeOnScreen",
)

cat_printer_dir_state = (
    "CatPrinterDirFree",
    "CatPrinterDirProtect",
)

cat_prism_extrusion_direction = (
    "catNormalToSketchDirection",
    "catNotNormalToSketchDirection",
)

cat_prism_orientation = (
    "catRegularOrientation",
    "catInverseOrientation",
)

cat_product_source = (
    "catProductSourceUnknown",
    "catProductMade",
    "catProductBought",
)

cat_proj_view_type = (
    "catRightView",
    "catLeftView",
    "catTopView",
    "catBottomView",
    "catRearView",
)

cat_projection_mode = (
    "catProjectionConic",
    "catProjectionCylindric",
    "catProjectionUndefined",
)

cat_psp_idl_application_id = (
    "catPspIDLCATPiping",
    "catPspIDLCATHVAC",
    "catPspIDLCATEquipment",
    "catPspIDLCATWaveguide",
    "catPspIDLCATTubing",
    "catPspIDLCATHanger",
    "catPspIDLCATRaceway",
    "catPspIDLCATConduit",
    "catPspIDLCATCompAccess",
    "catPspIDLCATElectrical",
    "catPspIDLCATPID",
    "catPspIDLCATHVACDiagram",
    "catPspIDLCATTubingDiagram",
    "catPspIDLCATWaveguideDiagram",
    "catPspIDLCATElectricalDiagram",
)

cat_psp_idl_attr_data_type = (
    "catPspIDLInteger",
    "catPspIDLDouble",
    "catPspIDLString",
    "catPspIDLMultiString",
    "catPspIDLBoolean",
)

cat_psp_idl_domain_id = (
    "catPspIDLNone",
    "catPspIDLCATPIP",
    "catPspIDLCATINS",
    "catPspIDLCATHVA",
    "catPspIDLCATEQT",
    "catPspIDLCATTUB",
    "catPspIDLCATMLD",
    "catPspIDLCATWVG",
    "catPspIDLCATRWY",
    "catPspIDLCATCND",
    "catPspIDLCATHGR",
    "catPspIDLCATCAM",
    "catPspIDLCATELE",
)

cat_psp_idl_flow_capability = (
    "catPspIDLFlowCapability_Undefined",
    "catPspIDLFlowCapability_InDirection",
    "catPspIDLFlowCapability_OutDirection",
    "catPspIDLFlowCapability_InOutDirection",
)

cat_psp_idl_flow_reality = (
    "catPspIDLFlowReality_Undefined",
    "catPspIDLFlowReality_InDirection",
    "catPspIDLFlowReality_OutDirection",
    "catPspIDLFlowReality_InOutDirection",
)

cat_psp_idl_function_status = (
    "catPspIDLFuncUndefined",
    "catPspIDLInFuncNet",
    "catPspIDLFuncNetPhysType",
    "catPspIDLFuncNetPhysNoPos",
    "catPspIDLFuncNoNetPhys",
    "catPspIDLFuncNetPhys",
)

cat_psp_idl_part_connector_type = (
    "catPspIDLPartCtrTypeNotRecognized",
    "catPspIDLPartCtrTypeFace",
    "catPspIDLPartCtrTypeSupport",
    "catPspIDLPartCtrTypeCenter",
    "catPspIDLPartCtrTypeTop",
    "catPspIDLPartCtrTypeBottom",
    "catPspIDLPartCtrTypeLeft",
    "catPspIDLPartCtrTypeRight",
    "catPspIDLPartCtrTypeTopLeft",
    "catPspIDLPartCtrTypeTopRight",
    "catPspIDLPartCtrTypeBottomLeft",
    "catPspIDLPartCtrTypeBottomRight",
    "catPspIDLPartCtrTypeCircular",
    "catPspIDLPartCtrTypeRectangular",
    "catPspIDLPartCtrTypeUpOnly",
)

cat_rectangular_pattern_parameters = (
    "catInstancesandSpacing",
    "catUnequalSpacing",
)

cat_rendering_mode = (
    "catRenderShading",
    "catRenderShadingWithEdges",
    "catRenderWireFrame",
    "catRenderHiddenLinesRemoval",
    "catRenderQuickHiddenLinesRemoval",
    "catRenderMaterial",
    "catRenderMaterialWithEdges",
    "catRenderShadingWithEdgesAndHiddenEdges",
    "catRenderShadingWithEdgesWithoutSmoothEdges",
    "catRenderWireFrameWithoutSmoothEdgesWithoutVertices",
    "catRenderWireFrameWithHalfSmoothEdgesWithoutVertices",
    "catRenderShadingWithEdgesWithOutlines",
    "catRenderQuickHiddenLinesRemovalWithoutVertices",
    "catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithOutlines",
    "catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithOutlinesWithoutVertices",
    "catRenderWireFrameWithHalfSmoothEdgeWithOutlinesWithoutVertices",
    "catRenderWireFrameWithOutlinesWithoutSmoothEdgesWithoutVertices",
    "catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithoutSmoothEdgesWithoutVertices",
    "catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithHalfSmoothEdgeWithoutVertices",
    "catRenderQuickHiddenLinesRemovalWithoutSmoothEdgesWithoutVertices",
    "catRenderQuickHiddenLinesRemovalWithHalfSmoothEdgeWithoutVertices",
    "catRenderShadingWithEdgesWithHalfSmoothEdgeWithoutVertices",
    "catRenderShadingWithEdgesWithHalfSmoothEdge",
)

cat_rep_type = (
    "catRep3D",
    "catRep2D",
    "catRepText",
)

cat_representation_mode = (
    "catExactMode",
    "catPolyhedricMode",
    "catVisualMode",
)

cat_sac_settings_enum = (
    "CatSacSettingsEnumNoInsert",
    "CatSacSettingsEnumAutomatic",
    "CatSacSettingsEnumUserPrompt",
)

cat_sampled_analysis_mode = (
    "CatSampledAnalysisOff",
    "CatSampledAnalysisOn",
    "CatSampledAnalysisStop",
    "CatSampledAnalysisVerbose",
)

cat_sampled_split_type = (
    "CatSampledSplitOnSeg",
    "CatSampledSplitOnShot",
)

cat_scene_type = (
    "CatSceneTypeDelta",
    "CatSceneTypeFull",
)

cat_sch_idl_application_id = (
    "catSchIDLCATPID",
    "catSchIDLCATHVACDiagram",
    "catSchIDLCATWaveguideDiagram",
    "catSchIDLCATTubingDiagram",
    "catSchIDLCATElectricalDiagram",
)

cat_sch_idl_arrow_frequency = (
    "catSchIDLArrowAllSegs",
    "catSchIDLArrowAllButLastSeg",
    "catSchIDLArrowInteriorSegs",
    "catSchIDLArrowMiddleSeg",
)

cat_sch_idl_arrow_position = (
    "catSchIDLMidSegArrow",
    "catSchIDLEndSegArrow",
)

cat_sch_idl_arrow_style = (
    "catSchIDLFillArrow",
    "catSchIDLNotFillArrow",
    "catSchIDLStandardArrow",
)

cat_sch_idl_cntr_flow_capability = (
    "catSchIDLCntrFlowCapability_Undefined",
    "catSchIDLCntrFlowCapability_InDirection",
    "catSchIDLCntrFlowCapability_OutDirection",
    "catSchIDLCntrFlowCapability_InOutDirection",
)

cat_sch_idl_cntr_flow_reality = (
    "catSchIDLCntrFlowReality_Undefined",
    "catSchIDLCntrFlowReality_InDirection",
    "catSchIDLCntrFlowReality_OutDirection",
    "catSchIDLCntrFlowReality_InOutDirection",
)

cat_sch_idl_cntr_symbol_type = (
    "catSchIDLCntrSymbol_Undefined",
    "catSchIDLCntrSymbol_Point",
    "catSchIDLCntrSymbol_PtVector",
    "catSchIDLCntrSymbol_OnOffSheet",
    "catSchIDLCntrSymbol_LineBoundary",
)

cat_sch_idl_display_mode = (
    "catSchIDLDisplayMode_Default",
    "catSchIDLDisplayMode_Alternate",
)

cat_sch_idl_extension_type = (
    "catSchIDLComponent_Extension",
    "catSchIDLRoute_Extension",
    "catSchIDLCompConnector_Extension",
    "catSchIDLRouteConnector_Extension",
    "catSchIDLZone_Extension",
)

cat_sch_idl_gap_priority = (
    "catSchIDLGapThisRoute",
    "catSchIDLGapInputRoute",
    "catSchIDLGapNoPriority",
    "catSchIDLGapHorizontalSeg",
    "catSchIDLGapVerticalSeg",
)

cat_sch_idl_gap_style = (
    "catSchIDLBlankGap",
    "catSchIDLJumpGap",
    "catSchIDLWavyGap",
)

cat_sch_idl_internal_flow_status = (
    "catSchIDLInternFlowStatus_Undefined",
    "catSchIDLInternFlowStatus_Open",
    "catSchIDLInternFlowStatus_Close",
)

cat_sch_idl_internal_flow_type = (
    "catSchIDLInternFlowType_Undefined",
    "catSchIDLInternFlowType_Corner",
    "catSchIDLInternFlowType_Linear",
)

cat_sch_idl_multi_image_status = (
    "catSchIDLImage_IsUpToDate",
    "catSchIDLImage_MasterNotFound",
    "catSchIDLImage_MasterDocNotFound",
    "catSchIDLImage_InvalidReference",
    "catSchIDLImage_AttrsNotUpToDate",
)

cat_sch_idl_route_alternate_graphic_style = (
    "catSchIDLRouteAlternateGraphicStyle_ellipse",
)

cat_sch_idl_route_compress_mode = (
    "catSchIDLCompressOff",
    "catSchIDLCompressOn",
)

cat_sch_idl_route_mode = (
    "catSchIDLRouteMode_Undefined",
    "catSchIDLRouteMode_HorizontalVertical",
    "catSchIDLRouteMode_HorizontalVertical45",
    "catSchIDLRouteMode_PointToPoint",
    "catSchIDLRouteMode_AroundObject",
)

cat_sch_idl_route_symbol_update_mode = (
    "catSchIDLSymbolUpdateOff",
    "catSchIDLSymbolUpdateOn",
)

cat_sch_idl_route_unset_gaps_mode = (
    "catSchIDLUnsetGapsOff",
    "catSchIDLUnsetGapsOn",
)

cat_sch_idlgrr_route_reshape_mode = (
    "catSchIDLFixedShapeOff",
    "catSchIDLFixedShapeOn",
)

cat_script_language = (
    "CATVBScriptLanguage",
    "CATVBALanguage",
    "CATBasicScriptLanguage",
    "CATJavaLanguage",
    "CATJScriptLanguage",
)

cat_script_library_type = (
    "catScriptLibraryTypeDocument",
    "catScriptLibraryTypeDirectory",
    "catScriptLibraryTypeVBAProject",
)

cat_search_context_scope = (
    "Everywhere",
    "InWorkbench",
    "FromWorkbench",
    "FromSelection",
    "VisibleOnScreen",
)

cat_sec_window_open_mode = (
    "catSecWindow_DefaultSize",
    "catSecWindow_TileVertically",
)

cat_section_behavior = (
    "catSectionBehaviorManual",
    "catSectionBehaviorAutomatic",
    "catSectionBehaviorFreeze",
)

cat_section_clipping_mode = (
    "catSection_Software",
    "catSection_OpenGL",
)

cat_section_grid_style = (
    "catSectionGridStyle_Lines",
    "catSectionGridStyle_Crosses",
)

cat_section_plane_normal = (
    "catSectionNormal_X",
    "catSectionNormal_Y",
    "catSectionNormal_Z",
)

cat_section_plane_origin = (
    "catSectionOrigin_0",
    "catSectionOrigin_Selection",
)

cat_section_type = (
    "catSectionTypePlane",
    "catSectionTypeSlice",
    "catSectionTypeBox",
)

cat_selection_filter = (
    "ZeroDim",
    "MonoDim",
    "MonoDimInfinite",
    "RectilinearMonoDim",
    "RectilinearMonoDimInfinite",
    "BiDim",
    "BiDimInfinite",
    "PlanarBiDim",
    "PlanarBiDimInfinite",
    "CylindricalBiDim",
    "TriDim",
)

cat_sewing_intersection_mode = (
    "catSewingNoIntersect",
    "catSewingIntersect",
)

cat_sheet_gen_views_pos_mode = (
    "catFixedCG",
    "catFixedAxis",
)

cat_sheet_projection_method = (
    "catFirstAngle",
    "catThirdAngle",
)

cat_show_result_type = (
    "ByRule",
    "ByObject",
    "ByState",
)

cat_shuttle_move_mode = (
    "CatShuttle",
    "CatAxis",
)

cat_shuttle_vector = (
    "CatShuttleVectorX",
    "CatShuttleVectorY",
    "CatShuttleVectorZ",
)

cat_solve_type = (
    "ManualSolveType",
    "AutomaticOptimizedSolveType",
    "AutomaticCompleteSolveType",
)

cat_specs_and_geom_window_layout = (
    "catWindowSpecsOnly",
    "catWindowGeomOnly",
    "catWindowSpecsAndGeom",
)

cat_specs_layout = (
    "catSpecsViewerHorizontalIndented",
    "catSpecsViewerHorizontalUp",
    "catSpecsViewerHorizontalCentered",
    "catSpecsViewerVerticalCentered",
    "catSpecsViewerHorizontalRelational",
    "catSpecsViewerVerticalRelational",
)

cat_split_side = (
    "catPositiveSide",
    "catNegativeSide",
)

cat_str_creation_mode = (
    "catStrPartMode",
    "catStrSheetMetalMode",
)

cat_str_cutback_type = (
    "catStrNoneType",
    "catStrNormalType",
    "catStrWeldedType",
    "catStrMiteredType",
    "catStrNotchingType",
)

cat_str_link_mode = (
    "catStrWithLinkMode",
    "catStrNoLinkMode",
    "catStrRefRefWithLinkMode",
    "catStrRefRefNoLinkMode",
)

cat_str_material_orientation = (
    "catStrStandardOrientation",
    "catStrReverseOrientation",
)

cat_str_member_extremity = (
    "catStartExtremity",
    "catEndExtremity",
    "catBothExtremity",
)

cat_str_placement_point = (
    "catStrDefault",
    "catStrBottomLeft",
    "catStrBottomCenter",
    "catStrBottomRight",
    "catStrCenterLeft",
    "catStrCenterCenter",
    "catStrCenterRight",
    "catStrTopLeft",
    "catStrTopCenter",
    "catStrTopRight",
    "catStrGravity",
    "catStrGravityBottom",
    "catStrGravityLeft",
    "catStrGravityRight",
    "catStrGravityTop",
    "catStrUserPoint",
)

cat_str_plane_mode = (
    "catStrNoneMode",
    "catStrOnPlane",
    "catStrParallelToPlane",
)

cat_str_section_properties = (
    "CatStrArea",
    "CatStrInertiaXX",
    "CatStrInertiaYY",
    "CatStrModuleInertiaX",
    "CatStrModuleInertiaY",
    "CatStrGirationModuleX",
    "CatStrGirationModuleY",
)

cat_symbol_type = (
    "catNotUsed",
    "catCross",
    "catPlus",
    "catConcentric",
    "catCoincident",
    "catFullCircle",
    "catFullSquare",
    "catStar",
    "catDot",
    "catSmallDot",
    "catMisc1",
    "catMisc2",
    "catFullCircle2",
    "catFullSquare2",
    "catOpenArrow",
    "catUnfilledArrow",
    "catBlankedArrow",
    "catFilledArrow",
    "catUnfilledCircle",
    "catBlankedCircle",
    "catFilledCircle",
    "catCrossedCircle",
    "catBlankedSquare",
    "catFilledSquare",
    "catBlankedTriangle",
    "catFilledTriangle",
    "catManipulatorSquare",
    "catMamipulatorDiamond",
    "catManipulatorCircle",
    "catManipulatorTriangle",
    "catDoubleOpenArrow",
    "catWave",
)

cat_table_border_type = (
    "CatTableNone",
    "CatTableLeft",
    "CatTableTop",
    "CatTableRight",
    "CatTableBottom",
    "CatTableBackSlashed",
    "CatTableSlashed",
    "CatTableHorStrikedOut",
    "CatTableVerStrikedOut",
    "CatTableOutLine",
    "CatTableInside",
    "CatTableCross",
)

cat_table_compute_mode = (
    "CatTableComputeOFF",
    "CatTableComputeON",
)

cat_table_invert_mode = (
    "CatInvertColumn",
    "CatInvertRow",
    "CatInvertAll",
)

cat_table_position = (
    "CatTableTopLeft",
    "CatTableMiddleLeft",
    "CatTableBottomLeft",
    "CatTableTopCenter",
    "CatTableMiddleCenter",
    "CatTableBottomCenter",
    "CatTableTopRight",
    "CatTableMiddleRight",
    "CatTableBottomRight",
)

cat_text_anchor_position = (
    "catUnsusedValue1",
    "catTopLeft",
    "catMiddleLeft",
    "catBottomLeft",
    "catTopCenter",
    "catMiddleCenter",
    "catBottomCenter",
    "catTopRight",
    "catMiddleRight",
    "catBottomRight",
    "catUnsusedValue2",
    "catCapLeft",
    "catHalfLeft",
    "catBaseLeft",
    "catCapCenter",
    "catHalfCenter",
    "catBaseCenter",
    "catCapRight",
    "catHalfRight",
    "catBaseRight",
)

cat_text_flip_mode = (
    "catTextNoFlip",
    "catTextHorizontalFlip",
    "catTextVerticalFlip",
    "catTextHorizontalAndVerticalFlip",
    "catTextAutoFlip",
)

cat_text_frame_type = (
    "catNone",
    "catRectangle",
    "catSquare",
    "catCircle",
    "catScoredCircle",
    "catDiamond",
    "catTriangle",
    "catRightFlag",
    "catLeftFlag",
    "catBothFlag",
    "catOblong",
    "catEllipse",
    "catCustom",
)

cat_text_property = (
    "catBold",  # The text is formatted as bold.
    "catItalic",  # The text is formatted as italic.
    "catUnderline",  # The text is underlined.
    "catOverline",  # The text is overlined.
    "catStrikethrough",  # The text is formatted as strike through.
    "catSubscript",  # The text is formatted as subscript.
    "catSuperscript",  # The text is formatted as superscript
    "catFontSize",  # The font size. This value is expressed in mm.
    "catParagraph",  # To consider a piece of the text as a paragraph
    "catPlain",  # Internal use only.
    "catColor",  # Color of the characters
    "catFontName",  # The name of the font used.
    "catBorder",  #
    "catAlignment",  # Alignment of the piece of text.
    "catCharRatio",  # Ratio between character height and width.
    # The value is a percentage of the font size and corresponds to the ratio height by width.
    "catCharSpacing",  # Space between each character.
    # The value is a percentage of the font size (maybe a negative value).
    "catKerning",
)

cat_thread_linked_to = (
    "catNotDefined",
    "catNoLink",
    "cat2DPoint",
    "cat2DCircle",
    "cat3DGeom",
    "cat3DHole",
    "cat3DThread",
)

cat_thread_polarity = (
    "catThread",
    "catTap",
)

cat_thread_side = (
    "catRightSide",
    "catLeftSide",
)

cat_thread_standard = (
    "catMetricThinPitch",
    "catMetricThickPitch",
)

cat_thread_type = (
    "catThreaded",
    "catTaped",
)

cat_tree_orientation_enum = (
    "catTreeOrientationVertical",
    "catTreeOrientationHorizontal",
)

cat_tree_size_type_enum = (
    "catTreeSizeTypeFixedSize",
    "catTreeSizeTypeTextDependentSize",
)

cat_tree_type_enum = (
    "catTreeTypeClassical",
    "catTreeTypeStructural",
    "catTreeTypeHistorical",
    "catTreeTypeRelational",
)

cat_view2_d_mode_visu = (
    "catView2DModeNotActivated",
    "catView2DModeNoShow",
)

cat_view_background_mode = (
    "catStandard",
    "catInvisible",
    "catUnpickable",
    "catLowIntensity",
    "catUnpickableLowIntensity",
)

cat_view_filter_creation_mode = (
    "catDefaultFilter",
    "catDisplayFilterDialogBox",
    "catDedicatedFilter",
)

cat_view_side = (
    "catTopSide",
    "catBottomSide",
    "catLeftSide",
    "catRightSide",
    "catTLCorner",
    "catTRCorner",
    "catBLCorner",
    "catBRCorner",
)

cat_view_type = (
    "catAuxiliaryView",
    "catSectionView",
    "catSectionCutView",
)

cat_vis_layer_type = (
    "catVisLayerBasic",
    "catVisLayerNone",
)

cat_vis_property_pick = (
    "catVisPropertyPickAttr",
    "catVisPropertyNoPickAttr",
)

cat_vis_property_show = (
    "catVisPropertyShowAttr",
    "catVisPropertyNoShowAttr",
)

cat_vis_property_status = (
    "catVisPropertyDefined",
    "catVisPropertyUnDefined",
)

cat_vis_property_type = (
    "catVisPropertyLineType",
    "catVisPropertyWidth",
    "catVisPropertyColor",
    "catVisPropertyOpacity",
)

cat_visu_background_mode = (
    "catNoBackground",
    "catPick",
    "catNoPick",
    "catLowIntPick",
    "catLowIntNoPick",
)

cat_visu_in3_d_mode = (
    "catShowAll",
    "catHideAll",
)

cat_visualization_type = (
    "Passed",
    "Failed",
    "Both",
)

cat_weld_additional_symbol = (
    "catNoneAddWelding",
    "catFlatWelding",
    "catConvexWelding",
    "catConcaveWelding",
    "catFlushWelding",
    "catSmoothWelding",
)

cat_welding = (
    "catNoneWelding",
    "catFirstWelding",
    "catSecondWelding",
)

cat_welding_field = (
    "catWeldingNone",
    "catWeldingFieldOne",
    "catWeldingFieldTwo",
    "catWeldingFieldThree",
    "catWeldingFieldFour",
    "catWeldingFieldFive",
    "catWeldingFieldSix",
    "catWeldingFieldSeven",
)

cat_welding_side = (
    "catWeldingUp",
    "catWeldingDown",
)

cat_welding_symbol = (
    "catNoneMainWelding",
    "catSquareWelding",
    "catVGrooveWelding",
    "catHVGrooveWelding",
    "catYGrooveWelding",
    "catHYGrooveWelding",
    "catUGrooveWelding",
    "catHUGrooveWelding",
    "catFilletWelding",
    "catCFlangeWelding",
    "catEFlangeWelding",
    "catVFlareWelding",
    "catHVFlareWelding",
    "catSpotWelding",
    "catBackWelding",
    "catHVOGrooveWelding",
    "catVOGrooveWelding",
    "catPlugWelding",
    "catMRWelding",
    "catMWelding",
    "catRechargWelding",
    "catSpotJISWelding",
    "catEFlangeISOWelding",
    "catSeamWelding",
    "catScarfWelding",
    "catStudWelding",
    "catEdgeWelding",
    "catMeltThruWelding",
    "catSurfaceJointWelding",
    "catInclinedJointWelding",
)

cat_window_state = (
    "catWindowStateMaximized",
    "catWindowStateMinimized",
    "catWindowStateNormal",
)

cat_work_mode_type = (
    "DEFAULT_MODE",
    "VISUALIZATION_MODE",
    "DESIGN_MODE",
)

catfta_dim_configure_snapping = (
    "CATFTADimSnappingUndefined",
    "CATFTADimSnappingOnGrid",
    "CATFTADimSnappingValue",
    "CATFTADimSnappingBoth",
)

catfta_dim_create_on = (
    "CATFTADimCreateOnUndefined",
    "CATFTADimCreateOnCenter",
    "CATFTADimCreateOnEdge",
)

catfta_leader_associativity = (
    "CATFTALeaderAssociativityUndefined",
    "CATFTALeaderAssociativityFree",
    "CATFTALeaderAssociativityPerpendicular",
)

catv4_iv4_v5_spec_draft_migration_enum = (
    "squareMode",
    "coneMode",
)

catv4_iv5_v4_associativity_mode_enum = (
    "AssociativeMode",
    "NonAssociativeMode",
    "NonAssociativityModeAndNoSolidCreation",
)

catv4_iv5_v4_error_feature_creation_enum = (
    "NeverCreateErrorFeatures",
    "CreateAnErrorFeatureAfterUserAgreement",
    "AlwaysCreateErrorFeatures",
)

catv4_iv5_v4_internal_curve_creation_enum = (
    "AllCurvesAreCreated",
    "OnlyConicsAreCreated",
    "NoInternalCurveIsCreated",
)

cd5_save_item_status = (
    "CD5SaveItem_New",
    "CD5SaveItem_Modified",
    "CD5SaveItem_Exists",
    "CD5SaveItem_ECNameNotUnique",
    "CD5SaveItem_ModifiedNotLockedByYou",
    "CD5SaveItem_Obsolete",
    "CD5SaveItem_UUIDConflict",
    "CD5SaveItem_NotFound",
)

cd5_save_operation_scope = (
    "CD5SaveOperation_ActiveDocument",
    "CD5SaveOperation_CurrentEditor",
    "CD5SaveOperation_Session",
)

contact_stiffness_type = (
    "DEFAULT",
    "STIFF_VALUE",
)

distribution_type = (
    "UNIFORM",
    "JOB",
    "USERDEFINED",
    "JOB_USERDEFINED",
)

dmu_track_move_mode = (
    "DMUTrackSpeedMode",
    "DMUTrackTimeMode",
)

dnb_act_behavior_type = (
    "DNBBehaviorProcess",
    "DNBBehaviorParent",
)

dnb_analysis_level = (
    "DNBAnalysisLevelOff",
    "DNBAnalysisLevelHighlight",
    "DNBAnalysisLevelVerbose",
    "DNBAnalysisLevelInterrupt",
)

dnb_assign_status = (
    "DNBUnknownState",
    "DNBSuccess",
    "DNBAlreadyAssigned",
    "DNBInvalidObjetAssignment",
    "DNBInvalidProcessVersion",
    "DNBPartsNotLoaded",
)

dnb_auxilliary_device_type = (
    "AuxilliaryDeviceType_RailTrackGantry",
    "AuxilliaryDeviceType_EndOfArmTooling",
    "AuxilliaryDeviceType_WorkpiecePositioner",
    "AuxilliaryDeviceType_Conveyor",
)

dnb_hlnk_behavior_type = (
    "DNBBehaviorContinue",
    "DNBBehaviorPause",
)

dnb_sim_graph_update_mode = (
    "DNBSimGraphUpdateDisabled",
    "DNBSimGraphUpdateEnabled",
)

dnb_sim_init_state_attr = (
    "DNBVisInitStateAttr",
    "DNBPosInitStateAttr",
    "DNBColInitStateAttr",
    "DNBOpacInitStateAttr",
    "DNBVisPosInitStateAttr",
    "DNBVisColInitStateAttr",
    "DNBVisOpacInitStateAttr",
    "DNBVisPosColInitStateAttr",
    "DNBVisPosOpacInitStateAttr",
    "DNBVisColOpacInitStateAttr",
    "DNBPosColInitStateAttr",
    "DNBPosOpacInitStateAttr",
    "DNBPosColOpacInitStateAttr",
    "DNBColOpacInitStateAttr",
    "DNBAllInitStateAttr",
)

dnb_sim_navigation_mode = (
    "DNBSimNavigationModeStep",
    "DNBSimNavigationModeAnimate",
)

dnb_visualization_mode = (
    "DNBVisualizationModeHighlight",
    "DNBVisualizationModeCurves",
)

dnbia_mfg_assembly_type = (
    "manufacturingAssembly",
    "manufacturingKit",
    "assemblySpecTree",
    "manufacturingOutput",
    "notSpecified",
)

dnbppr_remove_status = (
    "DNBFastenerUnknownStatus",
    "DNBFastenerAssignedStatus",
    "DNBFastenerSuccessStatus",
)

dnbtcp_trace_legends = (
    "DNBTCPTraceLegendAllLegend",
    "DNBTCPTraceLegendName",
    "DNBTCPTraceLegendX",
    "DNBTCPTraceLegendY",
    "DNBTCPTraceLegendZ",
    "DNBTCPTraceLegendYaw",
    "DNBTCPTraceLegendPitch",
    "DNBTCPTraceLegendRoll",
    "DNBTCPTraceLegendCycleTime",
    "DNBTCPTraceLegendHighlight",
    "DNBTCPTraceLegendAlwaysVisible",
)

dnbtcp_trace_reps = (
    "DNBTCPTraceRepAllRep",
    "DNBTCPTraceRepPoint",
    "DNBTCPTraceRepLine",
    "DNBTCPTraceRepAxis",
)

elem_behav_enum = (
    "BEHAVIOR_NONE",
    "SHELL",
    "MEMBRANE",
    "SOLID3D",
    "CONTINUUM_SHELL",
    "BEAM",
    "GASKET",
)

elem_id_enum = (
    "TET_LINEAR",
    "TET_PARABOLIC",
    "HEX_LINEAR",
    "HEX_PARABOLIC",
    "WEDG_LINEAR",
    "WEDG_PARABOLIC",
    "TRI_LINEAR",
    "TRI_PARABOLIC",
    "QUAD_LINEAR",
    "QUAD_PARABOLIC",
    "LINE_LINEAR",
    "LINE_PARABOLIC",
)

fixed_time_increment_method = (
    "ABQ_FTI_ELEMENT_BY_ELEMENT",
    "ABQ_FTI_USER_DEFINED",
)

formulation_option_type = (
    "SOLVERDEFAULT",
    "SURFACETOSURFACE",
    "NODETOSURFACE",
)

formulation_type = (
    "FRICTIONLESS",
    "PENALTY",
)

frame_visibility = (
    "VisNo",
    "VisYes",
    "VisRetain",
)

hts_activity_group_motion_basis = (
    "HAGMOTBASIS_DEFAULT",
    "HAGMOTBASIS_USERSPEED",
    "HAGMOTBASIS_USERTIME",
)

hts_body_pose_options = (
    "BODYPOSE_CURRENT",
    "BODYPOSE_RESET",
)

hts_end_effector = (
    "EE_LEFTHAND",
    "EE_RIGHTHAND",
    "EE_LEFTLEG",
    "EE_RIGHTLEG",
    "EE_LINEOFSIGHT",
    "EE_BODY",
    "EE_NECK",
)

hts_hand = (
    "HAND_RIGHT",
    "HAND_LEFT",
)

hts_manikin_referential = (
    "REF_EYEPOINT",
    "REF_HPOINT",
    "REF_LEFTFOOT",
    "REF_RIGHTFOOT",
    "REF_LOWESTFOOT",
    "REF_CROTCH",
    "REF_LEFTHAND",
    "REF_RIGHTHAND",
    "REF_BETWEENFEET",
    "REF_HPOINTPROJECTION",
)

hts_motion_basis = (
    "MOTBASIS_SPEED",
    "MOTBASIS_TIME",
)

hts_pick_type = (
    "SINGLE_HAND",
    "BOTH_HANDS",
)

hts_search_intensity = (
    "FINESEARCH",
    "NORMALSEARCH",
    "COARSESEARCH",
)

hts_stride_options = (
    "STRIDE_SHORT",
    "STRIDE_MEDIUM",
    "STRIDE_LONG",
)

hts_swing_options = (
    "SWING_BOTHARMS",
    "SWING_LEFTARM",
    "SWING_RIGHTARM",
    "SWING_CURRENT",
)

hts_walk_motion_basis = (
    "WALKMOTBASIS_DEFAULT",
    "WALKMOTBASIS_USERSPEED",
    "WALKMOTBASIS_USERTIME",
)

incrementation_type = (
    "AUTO_INCREMENT",
    "FIXED_INCREMENT",
)

initial_thickness_type = (
    "USE_NODAL_COORDINATES",
    "INITIAL_THICKNESS_SPECIFY",
)

item_assignment_type = (
    "ProcessProcesses",
    "ProcessFirstProcesses",
    "ProcessRemoves",
    "ProcessImplementsRequirementPartial",
    "ProcessImplementsRequirementComplete",
    "productviewpoint",
    "productvisualization",
)

job_type = (
    "ANALYSIS",
    "DATACHECK",
    "CONTINUE",
    "FROMINPUTFILE",
    "SYNTAXCHECK",
    "RESTART",
)

max_stiffness_type = (
    "MAX_STIFF_DEFAULT",
    "MAX_STIFF_VALUE",
)

memory_unit_type = (
    "MEGABYTES",
    "PERCENT",
)

motion_basis = (
    "MOTION_ABSOLUTE",
    "MOTION_PERCENT",
    "MOTION_TIME",
)

parallel_method_std_type = (
    "TREE",
    "SUPERNODE",
)

position_tolerance_type = (
    "COMPUTED",
    "SPECIFIED",
)

pressure_overclosure_type = (
    "HARD",
    "EXPONENTIAL",
    "LINEAR",
    "TABULAR",
)

raster_level_of_detail = (
    "LowQuality",
    "NormalQuality",
    "HighQuality",
    "Customize",
)

response_type = (
    "STEADY_STATE",
    "TRANSIENT",
)

sliding_type = (
    "FINITE",
    "SMALL",
)

spm_distribution_mode = (
    "SPM_LINEAR",
    "SPM_HISTOGRAM",
    "SPM_LOG",
)

spring_def_type = (
    "ABQ_LINE",
    "ABQ_NON_LINEAR",
)

spring_dof_type = (
    "U1_DOF",
    "U2_DOF",
    "U3_DOF",
    "UR1_DOF",
    "UR2_DOF",
    "UR3_DOF",
)

spring_type_type = (
    "AXIAL",
    "GENERAL",
)

stabilization_stiffness_type = (
    "STABILIZATION_DEFAULT",
    "STABILIZATION_SPECIFY",
)

stabilization_type = (
    "NONE",
    "DISSIPATION",
    "FACTOR",
)

swk_anthro_sex = (
    "Male",
    "Female"
)

swk_posture_spec = (
    "SWKPostureSpecDefault",
    "SWKPostureSpecStand",
    "SWKPostureSpecSit",
    "SWKPostureSpecReach",
    "SWKPostureSpecExtendedReach",
    "SWKPostureSpecSpan",
    "SWKPostureSpecKneel",
    "SWKPostureSpecInitial",
)

time_span_type = (
    "STEP_TIME",
    "TOTAL_TIME",
)

geometrical_feature_type = (
    'Unknown',
    'Point',
    'Curve',
    'Line',
    'Circle',
    'Surface',
    'Plane',
    'Solid / Volume'
)
