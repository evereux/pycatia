from enum import Enum


class AbqConcForceLoad_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_concentrated_force.ABQConcentratedForce.load_type
    """
    POINTLOAD = 0
    DISTRIBUTEDLOAD = 1
    LOADDENSITY = 2


class AbqDatOutputVarType(Enum):
    """
    pycatia.abq_automation_interfaces.abq_data_output_request.ABQDataOutputRequest.set_specified_output_variables
    pycatia.abq_automation_interfaces.abq_data_output_request.ABQDataOutputRequest.unset_output_type
    """
    ABQDATOUTPUTTYPE_NODE = 0
    ABQDATOUTPUTTYPE_ELEMENT = 1
    ABQDATOUTPUTTYPE_CONTACT = 2
    ABQDATOUTPUTTYPE_ENERGY = 3


class AbqEntityType(Enum):
    """
    pycatia.abq_automation_interfaces.abq_image_query.ABQImageQuery.export_group_image_data
    pycatia.abq_automation_interfaces.abq_image_query.ABQImageQuery.export_image_data
    """
    ABQ_NONE = 0
    ABQ_NODE = 1
    ABQ_ELEMENT = 2


class AbqLocalCsysType(Enum):
    """
    pycatia.abq_automation_interfaces.abq_concentrated_force.ABQConcentratedForce.load_type
    pycatia.abq_automation_interfaces.abq_concentrated_force.ABQConcentratedForce.set_use_coordinate_system_type
    pycatia.abq_automation_interfaces.abq_displacement_bc.ABQDisplacementBC.get_use_coordinate_system_type
    pycatia.abq_automation_interfaces.abq_displacement_bc.ABQDisplacementBC.set_use_coordinate_system_type
    """
    ABQ_CARTESIAN = 0
    ABQ_CYLINDRICAL = 1
    ABQ_SPHERICAL = 2
    ABQ_DEFAULTAXIS = 3


class AbqMsFrequencyType(Enum):
    """
    pycatia.abq_automation_interfaces.abq_mass_scaling.ABQMassScaling.frequency_type
    """
    ABQ_INTERVAL = 0
    ABQ_INCREMENT = 1


class AbqMsTargetMethod(Enum):
    """
    pycatia.abq_automation_interfaces.abq_mass_scaling.ABQMassScaling.target_method
    """
    ABQ_BELOW_MIN = 0
    ABQ_UNIFORM = 1
    ABQ_SET_EQUAL = 2


class AbqOutputAtSecPts(Enum):
    """
    pycatia.abq_automation_interfaces.abqfh_output_request.ABQFHOutputRequest.output_at_def_or_all_sec_pts
    """
    ABQDEFAULTSECPTS = 0
    ABQALLSECPTS = 1


class AbqOutputRequestType(Enum):
    """
    pycatia.abq_automation_interfaces.abq_output_requests.ABQOutputRequests.add
    pycatia.abq_automation_interfaces.abq_output_requests.ABQOutputRequests.item
    pycatia.abq_automation_interfaces.abq_output_requests.ABQOutputRequests.remove
    """
    ABQFIELD = 0
    ABQHISTORY = 1
    ABQDATA = 2


class AbqOutputVariableType(Enum):
    """
    pycatia.abq_automation_interfaces.abqfh_output_request.ABQFHOutputRequest.pre_select_default_or_all
    """
    ABQPRESELECTEDEFVAR = 0
    ABQALLVAR = 1


class AbqRequestedModesOption(Enum):
    """
    pycatia.abq_automation_interfaces.abq_frequency_step.ABQFrequencyStep.requested_modes_option
    """
    ABQ_ALL = 0
    ABQ_VALUE = 1


class AbqRestartOption(Enum):
    """
    pycatia.abq_automation_interfaces.abq_job.ABQJob.restart_request_option
    """
    ABQ_RESTART_NONE = 0
    ABQ_RESTART_EVERYINC = 1
    ABQ_RESTART_SPECINC = 2
    ABQ_RESTART_NUMINT = 3
    ABQ_RESTART_LASTINC = 4


class AbqRestartReadOption(Enum):
    """
    pycatia.abq_automation_interfaces.abq_job.ABQJob.restart_read_option
    pycatia.abq_automation_interfaces.abq_job.ABQJob.restart_read_step_selection_option
    """
    ABQ_RESTART_END_OF_STEP = 0
    ABQ_RESTART_INTERVAL = 1


class AbqRestartReadStepSelOption(Enum):
    """
    pycatia.abq_automation_interfaces.abq_job.ABQJob.restart_read_step_selection_option
    """
    ABQ_STEP_OBJECT = 0
    ABQ_STEP_NUMBER = 1


class AccuracyType(Enum):
    """
    pycatia.dnb_robot_interfaces.generic_accuracy_profile.GenericAccuracyProfile.get_accuracy_type
    pycatia.dnb_robot_interfaces.generic_accuracy_profile.GenericAccuracyProfile.set_accuracy_type
    """
    ACCURACY_TYPE_DISTANCE = 0
    ACCURACY_TYPE_SPEED = 1


class AdjustMethod_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_surface_to_surface_contact.ABQSurfaceToSurfaceContact.adjust_method
    """
    NOADJUST = 0
    OVERCLOSED = 1
    TOLERANCE = 2


class AutoTimeIncrementMethod(Enum):
    """
    pycatia.abq_automation_interfaces.abq_explicit_dynamics_step.ABQExplicitDynamicsStep.auto_time_increment_method
    """
    ABQ_ATI_GLOBAL = 0
    ABQ_ATI_ELEMENT_BY_ELEMENT = 1


class Cat3DColorInheritanceMode(Enum):
    """
    pycatia.drafting_interfaces.drawing_view_generative_behavior.DrawingViewGenerativeBehavior.color_inheritance_mode
    """
    cat3DColorInheritanceModeOff = 0
    cat3DColorInheritanceModeOn = 1


class Cat3DXmlGeomRepresentationType(Enum):
    """
    pycatia.threed_xml_interfaces.export_3d_xml_setting_att.Export3DXmlSettingAtt.geometry_representation_format
    """
    cat3DXmlExact = 0
    cat3DXmlTessellation = 1
    cat3DXmlCompressedTessellation = 2
    cat3DXmlDynamicTessellation = 3
    cat3DXmlStaticTessellation = 4
    cat3DXmlXmlTessellation = 5


class Cat3DXmlPprSaveConfig(Enum):
    """
    pycatia.threed_xml_interfaces.export_3d_xml_setting_att.Export3DXmlSettingAtt.ppr_save_config
    """
    cat3DXmlProductAndResourceList = 0
    cat3DXmlProductList = 1
    cat3DXmlResourceList = 2


class CatAlgorithmType(Enum):
    """
    pycatia.knowledge_interfaces.optimization.Optimization.algorithm_type
    """
    catSimulatedAnnealing = 0
    catGradient = 1
    catCAAalgorithm = 2
    catLocalForConstraints = 3


class CatAnalysisSetSearchType(Enum):
    """
    pycatia.analysis_interfaces.analysis_sets.AnalysisSets.item
    """
    catAnalysisSetSearchIn = 0
    catAnalysisSetSearchOut = 1
    catAnalysisSetSearchNeutral = 2
    catAnalysisSetSearchAll = 3


class CatAnalysisSetType(Enum):
    """
    pycatia.analysis_interfaces.analysis_sets.AnalysisSets.add
    pycatia.analysis_interfaces.analysis_sets.AnalysisSets.add_existing_set
    pycatia.analysis_interfaces.analysis_sets.AnalysisSets.item
    """
    catAnalysisSetIn = 0
    catAnalysisSetOut = 1
    catAnalysisSetNeutral = 2


class CatAnnotatedViewBehavior(Enum):
    """
    pycatia.navigator_interfaces.annotated_view.AnnotatedView.behavior_mode
    """
    CatAnnotatedViewBehaviorLink = 0
    CatAnnotatedViewBehaviorUnlink = 1


class CatAnnotationSetType(Enum):
    """
    pycatia.cat_tps_interfaces.annotation_set.AnnotationSet.annotation_set_type
    """
    catAnnotationSetStandard = 0
    catAnnotationSetLight = 1
    catAnnotationSetResult = 2


class CatArrangeStyle(Enum):
    """
    pycatia.in_interfaces.windows.Windows.arrange
    """
    catArrangeCascade = 0
    catArrangeTiledHorizontal = 1
    catArrangeTiledVertical = 2


class CatArrangementAreaVisuMode(Enum):
    """
    pycatia.arrangement_interfaces.arrangement_area.ArrangementArea.visu_mode
    """
    CatArrangementAreaVisuModeFlat = 0
    CatArrangementAreaVisuModeSolid = 1


class CatArrangementItemResVisuMode(Enum):
    """
    pycatia.arrangement_interfaces.arrangement_item_reservation.ArrangementItemReservation.visu_mode
    """
    CatArrangementItemReservationVisuModeAxis = 0
    CatArrangementItemReservationVisuModeFlat = 1
    CatArrangementItemReservationVisuModeSolid = 2


class CatArrangementRouteSection(Enum):
    """
    pycatia.arrangement_interfaces.arrangement_boundary.ArrangementBoundary.section_type
    pycatia.arrangement_interfaces.arrangement_pathway.ArrangementPathway.section_type
    pycatia.arrangement_interfaces.arrangement_run.ArrangementRun.section_type
    """
    CatArrangementRouteSectionNone = 0
    CatArrangementRouteSectionRectangular = 1
    CatArrangementRouteSectionRound = 2
    CatArrangementRouteSectionFlatOval = 3
    CatArrangementRouteSectionRadiusCorner = 4
    CatArrangementRouteSectionDoubleRidge = 5


class CatArrangementRouteVisuMode(Enum):
    """
    pycatia.arrangement_interfaces.arrangement_pathway.ArrangementPathway.visu_mode
    pycatia.arrangement_interfaces.arrangement_boundary.ArrangementBoundary.visu_mode
    pycatia.arrangement_interfaces.arrangement_boundary.ArrangementBoundary.visu_mode
    """
    CatArrangementRouteVisuModeCurve = 0
    CatArrangementRouteVisuModeFlat = 1
    CatArrangementRouteVisuModeSolid = 2


class CatAsmAutoSwitchToDesignMode(Enum):
    """
    pycatia.assembly_interfaces.assembly_general_setting_att.AssemblyGeneralSettingAtt.auto_switch_to_design_mode
    """
    catAutoSwitchAvailable = 0
    catAutoSwitchUnavailable = 1


class CatAsmConstraintCreationMode(Enum):
    """
    pycatia.assembly_interfaces.assembly_constraint_setting_att.AssemblyConstraintSettingAtt.constraint_creation_mode
    """
    catUseAnyGeometry = 0
    catUsePublishedGeometryChildLevel = 1
    catUsePublishedGeometryAnyLevel = 2


class CatAsmExtendMoveToFixT(Enum):
    """
    pycatia.assembly_interfaces.assembly_general_setting_att.AssemblyGeneralSettingAtt.move_with_fix_t_extend_mode
    """
    catNeverExtendMoveToFixT = 0
    catAskIfExtendMoveToFixT = 1
    catAlwaysExtendMoveToFixT = 2


class CatAsmPasteComponentMode(Enum):
    """
    pycatia.assembly_interfaces.assembly_constraint_setting_att.AssemblyConstraintSettingAtt.paste_component_mode
    """
    catPasteWithoutCsts = 0
    catPasteWithCstOnCopy = 1
    catPasteWithCstOnCut = 2
    catPasteWithCstOnCopyAndCut = 3


class CatAsmQuickConstraintMode(Enum):
    """
    pycatia.assembly_interfaces.assembly_constraint_setting_att.AssemblyConstraintSettingAtt.quick_constraint_mode
    """
    catSpecifiedOrder = 0
    catVerifiedConstraintFirst = 1


class CatAsmRedundancyMode(Enum):
    """
    pycatia.assembly_interfaces.assembly_constraint_setting_att.AssemblyConstraintSettingAtt.redundancy_mode
    """
    catUnChecked = 0
    catChecked = 1


class CatAsmUpdateMode(Enum):
    """
    pycatia.assembly_interfaces.assembly_general_setting_att.AssemblyGeneralSettingAtt.auto_update_mode
    """
    catManualUpdate = 0
    catAutomaticUpdate = 1


class CatAsmUpdateStatusComputeMode(Enum):
    """
    pycatia.assembly_interfaces.assembly_general_setting_att.AssemblyGeneralSettingAtt.update_status_mode
    """
    catManualCompute = 0
    catAutomaticCompute = 1


class CatAxisOrientationType(Enum):
    """
    pycatia.analysis_interfaces.analysis_image.AnalysisImage.export_data_in_any_user_axis
    pycatia.analysis_interfaces.analysis_image.AnalysisImage.export_data_in_global_axis
    pycatia.analysis_interfaces.analysis_image.AnalysisImage.export_data_in_manual_axis
    pycatia.analysis_interfaces.analysis_image.AnalysisImage.export_data_in_user_axis
    """
    catSamCoordinateSystem_Cartesian = 0
    catSamCoordinateSystem_Cylindrical = 1
    catSamCoordinateSystem_Spherical = 2
    catSamCoordinateSystem_Undefined = 3


class CatAxisSystemAxisType(Enum):
    """
    pycatia.mec_mod_interfaces.axis_system.AxisSystem.x_axis_type
    pycatia.mec_mod_interfaces.axis_system.AxisSystem.y_axis_type
    pycatia.mec_mod_interfaces.axis_system.AxisSystem.z_axis_type
    """
    catAxisSystemAxisSameDirection = 0
    catAxisSystemAxisByCoordinates = 1
    catAxisSystemAxisOppositeDirection = 2


class CatAxisSystemMainType(Enum):
    """
    pycatia.mec_mod_interfaces.axis_system.AxisSystem.type
    """
    catAxisSystemStandard = 0
    catAxisSystemAxisRotation = 1
    catAxisSystemEulerAngles = 2
    catAxisSystemExplicit = 3


class CatAxisSystemOriginType(Enum):
    """
    pycatia.mec_mod_interfaces.axis_system.AxisSystem.origin_type
    """
    catAxisSystemOriginByPoint = 0
    catAxisSystemOriginByCoordinates = 1


class CatBackFaceCullingMode(Enum):
    """
    pycatia.in_interfaces.visualization_setting_att.VisualizationSettingAtt.get_back_face_culling_mode
    pycatia.in_interfaces.visualization_setting_att.VisualizationSettingAtt.put_back_face_culling_mode
    """
    CATBackFaceCullingOnSolidFaces = 0
    CATBackFaceCullingOnAllFaces = 1
    CATBackFaceCullingOnStandAloneFaces = 2
    CATBackFaceCullingOnNoFaces = 3


class CatBannerPosition(Enum):
    """
    pycatia.in_interfaces.page_setup.PageSetup.banner_position
    """
    catBannerPositionNone = 0
    catBannerPositionBottom = 1
    catBannerPositionTop = 2
    catBannerPositionLeft = 3
    catBannerPositionRight = 4


class CatBlankingMode(Enum):
    """
    pycatia.drafting_interfaces.drawing_text_properties.DrawingTextProperties.blanking
    """
    catBlankingInactive = 0
    catBlankingActive = 1
    catBlankingOnGeom = 2


class CatCameraType(Enum):
    """
    pycatia.in_interfaces.camera.Camera.type
    """
    catCamera2D = 0
    catCamera3D = 1


class CatCaptureFormat(Enum):
    """
    pycatia.in_interfaces.viewer.Viewer.capture_to_file
    """
    catCaptureFormatCGM = 0
    catCaptureFormatEMF = 1
    catCaptureFormatTIFF = 2
    catCaptureFormatTIFFGreyScale = 3
    catCaptureFormatBMP = 4
    catCaptureFormatJPEG = 5


class CatCdHoleMode(Enum):
    """
    pycatia.part_interfaces.hole.Hole.counter_drilled_mode
    """
    catCDModeNoCountersunkDiameter = 0
    catCDModeCountersunkDiameter = 1


class CatChamferMode(Enum):
    """
    pycatia.part_interfaces.chamfer.Chamfer.angle
    pycatia.part_interfaces.chamfer.Chamfer.length2
    pycatia.part_interfaces.chamfer.Chamfer.mode
    """
    catTwoLengthChamfer = 0
    catLengthAngleChamfer = 1


class CatChamferOrientation(Enum):
    """
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_chamfer
    pycatia.part_interfaces.chamfer.Chamfer.orientation
    """
    catNoReverseChamfer = 0
    catReverseChamfer = 1


class CatChamferPropagation(Enum):
    """
    pycatia.part_interfaces.chamfer.Chamfer.propagation
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_chamfer
    """
    catTangencyChamfer = 0
    catMinimalChamfer = 1


class CatCircularPatternParameters(Enum):
    """
    pycatia.part_interfaces.circ_pattern.CircPattern.circular_pattern_parameters
    pycatia.part_interfaces.close_surface.CloseSurface.circular_pattern_parameters
    """
    catInstancesandAngularSpacing = 0
    catCompleteCrown = 1
    catUnequalAngularSpacing = 2


class CatClashComputationType(Enum):
    """
    pycatia.space_analyses_interfaces.clash.Clash.computation_type
    """
    catClashComputationTypeBetweenAll = 0
    catClashComputationTypeInsideOne = 1
    catClashComputationTypeAgainstAll = 2
    catClashComputationTypeBetweenTwo = 3


class CatClashExportType(Enum):
    """
    pycatia.space_analyses_interfaces.clash.Clash.export
    pycatia.space_analyses_interfaces.clash_result.ClashResult.export
    """
    CatClashExportTypeXMLResultOnly = 0


class CatClashImportType(Enum):
    """
    pycatia.space_analyses_interfaces.clash_results.ClashResults.add_from_xml
    """
    CatClashImportTypeClashOnly = 0
    CatClashImportTypeStructureAndClash = 1


class CatClashInterferenceType(Enum):
    """
    pycatia.space_analyses_interfaces.clash.Clash.interference_type
    """
    catClashInterferenceTypeContact = 0
    catClashInterferenceTypeClearance = 1
    catClashInterferenceAuthorizedPenetration = 2
    catClashInterferenceCaseRule = 3


class CatClippingFrameReframeOnMode(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_setting_att.Layout2DSettingAtt.clipping_frame_reframe_on_mode
    """
    catOnViewContent = 0
    catOnViewBackground = 1


class CatClippingMode(Enum):
    """
    pycatia.in_interfaces.viewer_3d.Viewer3D.clipping_mode
    pycatia.in_interfaces.viewer_3d.Viewer3D.far_limit
    pycatia.in_interfaces.viewer_3d.Viewer3D.near_limit
    """
    catClippingModeClear = 0
    catClippingModeNear = 1
    catClippingModeFar = 2
    catClippingModeNearAndFar = 3


class CatCompositesType(Enum):
    """
    pycatia.caa_composites_interfaces.composites_services.CompositesServices.get_composites_type
    """
    Unknown = 0
    Stacking = 1
    PlyGroup = 2
    Sequence = 3
    CutPieceGroup = 4
    Ply = 5
    Core = 6
    CutPiece = 7


class CatConflictComparison(Enum):
    """
    pycatia.space_analyses_interfaces.conflict.Conflict.comparison_info
    """
    catConflictComparisonNew = 0
    catConflictComparisonOld = 1
    catConflictComparisonNo = 2


class CatConflictStatus(Enum):
    """
    pycatia.space_analyses_interfaces.conflict.Conflict.status
    """
    catConflictStatusNotInspected = 0
    catConflictStatusRelevant = 1
    catConflictStatusIrrelevant = 2
    catConflictStatusSolved = 3


class CatConflictType(Enum):
    """
    pycatia.space_analyses_interfaces.conflict.Conflict.type

    """
    catConflictTypeClash = 0
    catConflictTypeContact = 1
    catConflictTypeClearance = 2


class CatConstraintAngleSector(Enum):
    """
    pycatia.mec_mod_interfaces.constraint.Constraint.angle_sector
    """
    catCstAngleSector0 = 0
    catCstAngleSector1 = 1
    catCstAngleSector2 = 2
    catCstAngleSector3 = 3


class CatConstraintDistConfig(Enum):
    """
    pycatia.mec_mod_interfaces.constraint.Constraint.distance_config
    """
    catCstDCUnspec = 0
    catCstDCParallel = 1
    catCstDCParallelSameOrient = 2
    catCstDCParallelOppOrient = 3


class CatConstraintDistDirection(Enum):
    """
    pycatia.mec_mod_interfaces.constraint.Constraint.distance_direction
    """
    catCstDistDirectionNone = 0
    catCstDistDirection1 = 1
    catCstDistDirection2 = 2
    catCstDistDirection3 = 3


class CatConstraintMode(Enum):
    """
    pycatia.mec_mod_interfaces.constraint.Constraint.mode
    """
    catCstModeDrivingDimension = 0
    catCstModeDrivenDimension = 1


class CatConstraintOrientation(Enum):
    """
    pycatia.mec_mod_interfaces.constraint.Constraint.orientation
    """
    catCstOrientSame = 0
    catCstOrientOpposite = 1
    catCstOrientUndefined = 2


class CatConstraintRefAxis(Enum):
    """
    pycatia.mec_mod_interfaces.constraint.Constraint.reference_axis
    """
    catCstRefAxisX = 0
    catCstRefAxisY = 1
    catCstRefAxisZ = 2


class CatConstraintRefType(Enum):
    """
    pycatia.mec_mod_interfaces.constraint.Constraint.reference_type
    """
    catCstRefTypeRelative = 0
    catCstRefTypeFixInSpace = 1


class CatConstraintSide(Enum):
    """
    pycatia.mec_mod_interfaces.constraint.Constraint.side
    """
    catCstSidePositive = 0
    catCstSideNegative = 1
    catCstSideSameAsValue = 2
    catCstSideOppositeToValue = 3
    catCstSideUndefined = 4


class CatConstraintStatus(Enum):
    """
    pycatia.mec_mod_interfaces.constraint.Constraint.status
    """
    catCstStatusOK = 0
    catCstStatusKOStronglyNotSatisfied = 1
    catCstStatusKOWrongOrientOrSide = 2
    catCstStatusKOWrongValue = 3
    catCstStatusKOWrongGeomEltType = 4
    catCstStatusKOBroken = 5


class CatConstraintType(Enum):
    """
    pycatia.mec_mod_interfaces.constraint.Constraint.type
    pycatia.mec_mod_interfaces.constraints.Constraints.add_bi_elt_cst
    pycatia.mec_mod_interfaces.constraints.Constraints.add_mono_elt_cst
    pycatia.mec_mod_interfaces.constraints.Constraints.add_tri_elt_cst
    """
    catCstTypeReference = 0
    catCstTypeDistance = 1
    catCstTypeOn = 2
    catCstTypeConcentricity = 3
    catCstTypeTangency = 4
    catCstTypeLength = 5
    catCstTypeAngle = 6
    catCstTypePlanarAngle = 7
    catCstTypeParallelism = 8
    catCstTypeAxisParallelism = 9
    catCstTypeHorizontality = 10
    catCstTypePerpendicularity = 11
    catCstTypeAxisPerpendicularity = 12
    catCstTypeVerticality = 13
    catCstTypeRadius = 14
    catCstTypeSymmetry = 15
    catCstTypeMidPoint = 16
    catCstTypeEquidistance = 17
    catCstTypeMajorRadius = 18
    catCstTypeMinorRadius = 19
    catCstTypeSurfContact = 20
    catCstTypeLinContact = 21
    catCstTypePoncContact = 22
    catCstTypeChamfer = 23
    catCstTypeChamferPerpend = 24
    catCstTypeAnnulContact = 25
    catCstTypeCylinderRadius = 26
    catCstTypeStContinuity = 27
    catCstTypeStDistance = 28
    catCstTypeSdContinuity = 29
    catCstTypeSdShape = 30


class CatCsHoleMode(Enum):
    """
    pycatia.part_interfaces.hole.Hole.counter_sunk_mode
    """
    catCSModeDepthAngle = 0
    catCSModeDepthDiameter = 1
    catCSModeAngleDiameter = 2


class CatDedicatedFilterType(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_setting_att.Layout2DSettingAtt.dedicated_filter_type
    """
    catDisplayInBackground = 0
    catMaskInBackground = 1


class CatDescriptionLengthType(Enum):
    """
    pycatia.general_knowledge_interfaces.expert_rule_base_runtime.ExpertRuleBaseRuntime.report_description_length
    """
    ShortText = 0
    LongText = 1


class CatDftWeldFinishSymbol(Enum):
    """
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.get_finish_symbol
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.set_finish_symbol
    """
    catFinishWeldingNone = 0
    catDftLetterCWelding = 1
    catDftLetterFWelding = 2
    catDftLetterGWelding = 3
    catDftLetterHWelding = 4
    catDftLetterMWelding = 5
    catDftLetterRWelding = 6
    catDftLetterUWelding = 7


class CatDftWeldingTail(Enum):
    """
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.welding_tail
    """
    catDftWeldingTailNO = 0
    catDftWeldingTailYES = 1


class CatDimAnalyse(Enum):
    """
    pycatia.drafting_interfaces.drawing_dimension.DrawingDimension.dim_status
    """
    catDimOnGenItems = 0
    catUnUpdatableDim = 1
    catFakeDim = 2
    catDrivingDim = 3
    catBrokenDim = 4
    catTrueDim = 5
    catBasic = 6
    cat3DDrivableDim = 7
    cat3DDrivedDim = 8
    catIsolatedDim = 9
    catDimOnHideGeom = 10
    cat3DFeatureDim = 11


class CatDimDualDisplay(Enum):
    """
    pycatia.drafting_interfaces.drawing_dimension.DrawingDimension.dual_value
    """
    catDualNone = 0
    catDualBellow = 1
    catDualFractional = 2
    catDualSideBySide = 3


class CatDimFake(Enum):
    """
    pycatia.drafting_interfaces.drawing_dim_value.DrawingDimValue.fake_dim_type
    """
    catDimFakeNone = 0
    catDimFakeNumValue = 1
    catDimFakeText = 2


class CatDimFrame(Enum):
    """
    pycatia.drafting_interfaces.drawing_dim_value.DrawingDimValue.value_framed_element
    pycatia.drafting_interfaces.drawing_dim_value.DrawingDimValue.value_framed_group
    pycatia.drafting_interfaces.drawing_dimension.DrawingDimension.value_frame
    """
    catFraNone = 0
    catFraCircle = 1
    catFraScoredCircle = 2
    catFraDiamondShaped = 3
    catFraSquare = 4
    catFraRectangle = 5
    catFraOblong = 6
    catFraRightFlag = 7
    catFraRightTriangle = 8


class CatDimFramedElement(Enum):
    """
    pycatia.drafting_interfaces.drawing_dim_value.DrawingDimValue.value_framed_element
    """
    catFraValue = 0
    catFraValueTol = 1
    catFraValueTolText = 2


class CatDimFramedGroup(Enum):
    """
    pycatia.drafting_interfaces.drawing_dim_value.DrawingDimValue.value_framed_group
    """
    catFraMain = 0
    catFraDual = 1
    catFraMainAndDual = 2
    catFraBoth = 3


class CatDimLineGraphRep(Enum):
    """
    pycatia.drafting_interfaces.drawing_dim_line.DrawingDimLine.dim_line_graph_rep
    """
    catDimLine1Part = 0
    catDimLine2Parts = 1
    catDimLineLeader1Part = 2
    catDimLineLeader2Part = 3


class CatDimLineRep(Enum):
    """
    pycatia.drafting_interfaces.drawing_dim_line.DrawingDimLine.dim_line_rep
    pycatia.drafting_interfaces.drawing_dimensions.DrawingDimensions.add
    pycatia.drafting_interfaces.drawing_dimensions.DrawingDimensions.add2
    """
    catDimUndef = 0
    catDimHoriz = 1
    catDimVert = 2
    catDimAuto = 3
    catDimUserDefined = 4
    catDimTrueDim = 5
    catDimParallel = 6
    catDimOffset = 7


class CatDimMode(Enum):
    """

    """
    catDimClassical = 0
    catDimCumulate = 1
    catDimHalfDim = 2
    catDimChained = 3
    catDimStacked = 4
    catDimCumulatesystem = 5
    catDimHalfDimSystem = 6


class CatDimOrientation(Enum):
    """
    pycatia.drafting_interfaces.drawing_dim_line.DrawingDimLine.dim_line_orientation
    pycatia.drafting_interfaces.drawing_dimension.DrawingDimension.value_orientation
    """
    catHorizontal = 0
    catVertical = 1
    catParallel = 2
    catPerpandicular = 3
    catAngle = 4


class CatDimReference(Enum):
    """
    pycatia.drafting_interfaces.drawing_dim_line.DrawingDimLine.dim_line_reference
    pycatia.drafting_interfaces.drawing_dimension.DrawingDimension.value_reference
    """
    catScreen = 0
    catView = 1
    catDimLine = 2


class CatDimScore(Enum):
    """
    pycatia.drafting_interfaces.drawing_dim_value.DrawingDimValue.scoring_mode

    """
    catDimScoreNone = 0
    catDimUnderScored = 1
    catDimScored = 2
    catCATDrwDimOverScored = 3


class CatDimSymbols(Enum):
    """
    pycatia.drafting_interfaces.drawing_dim_line.DrawingDimLine.get_symb_type
    pycatia.drafting_interfaces.drawing_dim_line.DrawingDimLine.set_symb_type
    """
    catDimSymbNone = 0
    catDimSymbOpenArrow = 1
    catDimSymbClosedArrow = 2
    catDimSymbFilledArrow = 3
    catDimSymbSymArrow = 4
    catDimSymbSlash = 5
    catDimSymbCircle = 6
    catDimSymbFilledCircle = 7
    catDimSymbScoredCircle = 8
    catDimSymbCircledCross = 9
    catDimSymbTriangle = 10
    catDimSymbFilledTriangle = 11
    catDimSymbCross = 12
    catDimSymbXCross = 13


class CatDimType(Enum):
    """
    pycatia.drafting_interfaces.drawing_dimension.DrawingDimension.dim_type
    pycatia.drafting_interfaces.drawing_dimensions.DrawingDimensions.add
    pycatia.drafting_interfaces.drawing_dimensions.DrawingDimensions.add2
    """
    catDimDistance = 0
    catDimDistanceOffset = 1
    catDimLength = 2
    catDimLengthCurvilinear = 3
    catDimAngle = 4
    catDimRadius = 5
    catDimRadiusTangent = 6
    catDimRadiusCylinder = 7
    catDimRadiusEdge = 8
    catDimDiameter = 9
    catDimDiameterTangent = 10
    catDimDiameterCylinder = 11
    catDimDiameterEdge = 12
    catDimDiameterCone = 13
    catDimChamfer = 14
    catDimSlope = 15
    catDimLengthCircular = 16
    catDimRadiusFillet = 17
    catDimDiameterTorus = 18
    catDimRadiusTorus = 19
    catDimDistanceMin = 20


class CatDistanceComputationType(Enum):
    """
    pycatia.space_analyses_interfaces.distance.Distance.computation_type
    """
    catDistanceComputationTypeInsideOne = 0
    catDistanceComputationTypeAgainstAll = 1
    catDistanceComputationTypeBetweenTwo = 2


class CatDistanceMeasureType(Enum):
    """
    pycatia.space_analyses_interfaces.distance.Distance.measure_type
    """
    catDistanceMeasureTypeMinimum = 0
    catDistanceMeasureTypeAlongX = 1
    catDistanceMeasureTypeAlongY = 2
    catDistanceMeasureTypeAlongZ = 3
    catDistanceMeasureTypeBand = 4


class CatDmuGroupPreviewHiddenObjectsDisplayMode(Enum):
    """
    pycatia.navigator_interfaces.n_4D_navigator_setting_att.N4DNavigatorSettingAtt.dmu_group_preview_hidden_objects_display_mode
    """
    CatDMUGroupPreviewShowHidden = 0
    CatDMUGroupPreviewShowHiddenCustom = 1


class CatDocContextualPriority(Enum):
    """
    pycatia.in_interfaces.documentation_setting_att.DocumentationSettingAtt.priority
    """
    CATDocContextualTechDoc = 0
    CATDocContextualUserComp = 1


class CatDraftMode(Enum):
    """
    pycatia.part_interfaces.draft.Draft.mode
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_draft
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_volumic_draft
    """
    catStandardDraftMode = 0
    catReflectKeepFaceDraftMode = 1
    catReflectKeepEdgeDraftMode = 2


class CatDraftMultiselectionMode(Enum):
    """
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_draft
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_volumic_draft
    pycatia.part_interfaces.draft_domain.DraftDomain.multiselection_mode
    """
    catNoneDraftMultiselectionMode = 0
    catDraftMultiselectionByNeutralMode = 1


class CatDraftNeutralPropagationMode(Enum):
    """
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_draft
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_volumic_draft
    pycatia.part_interfaces.draft_domain.DraftDomain.neutral_propagation_mode
    """
    catNoneDraftNeutralPropagationMode = 0
    catSmoothDraftNeutralPropagationMode = 1


class CatDrawingStandard(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_root.Layout2DRoot.standard
    pycatia.cat_sch_platform_interfaces.schematic_root.SchematicRoot.get_drawing_standard
    pycatia.cat_sch_platform_interfaces.schematic_root.SchematicRoot.set_drawing_standard
    pycatia.drafting_interfaces.drawing_document.DrawingDocument.standard
    """
    catANSI = 0
    catISO = 1
    catJIS = 2


class CatDrawingViewType(Enum):
    """
    pycatia.drafting_interfaces.drawing_view.DrawingView.view_type
    """
    catViewBackground = 0
    catViewFront = 1
    catViewLeft = 2
    catViewRight = 3
    catViewTop = 4
    catViewBottom = 5
    catViewRear = 6
    catViewAuxiliary = 7
    catViewIsom = 8
    catViewSection = 9
    catViewSectionCut = 10
    catViewDetail = 11
    catViewUntyped = 12
    catViewMain = 13
    catViewPure_Sketch = 14
    catViewUnfolded = 15


class CatDrwNewSheetFrom(Enum):
    """
    pycatia.drafting_interfaces.drafting_setting_att.DraftingSettingAtt.create_new_sheet_from
    """
    catDrwFirstSheet = 0
    catDrwStyle = 1


class CatDxfExportBlocksEnum(Enum):
    """
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.export_blocks
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.set_export_blocks
    """
    catDxfExportBlocksEnumNone = 0
    catDxfExportBlocksEnum1Level = 1
    catDxfExportBlocksEnumFull = 2


class CatDxfExportModeEnum(Enum):
    """
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.export_mode
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.set_export_mode
    """
    catDxfExportModeEnumSemantic = 0
    catDxfExportModeEnumGraphic = 1


class CatDxfExportSheetsEnum(Enum):
    """
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.export_sheets
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.set_export_sheets
    """
    catDxfExportSheetsEnumAll = 0
    catDxfExportSheetsEnumOnlyCurrent = 1


class CatDxfExportVersionEnum(Enum):
    """
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.export_version
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.set_export_version
    """
    catDxfExportVersionEnumR12 = 0
    catDxfExportVersionEnumR13 = 1
    catDxfExportVersionEnumR14 = 2
    catDxfExportVersionEnum2000 = 3
    catDxfExportVersionEnum2004 = 4
    catDxfExportVersionEnum2007 = 5
    catDxfExportVersionEnum2010 = 6
    catDxfExportVersionEnum2013 = 7


class CatDxfImportCreateEndPointsEnum(Enum):
    """
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.import_end_points
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.set_import_end_points
    """
    catDxfImportCreateEndPointsEnumNever = 0
    catDxfImportCreateEndPointsEnumFewEntities = 1
    catDxfImportCreateEndPointsEnumAlways = 2


class CatDxfImportDimensionsEnum(Enum):
    """
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.import_dimensions
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.set_import_dimensions
    """
    catDxfImportDimensionsEnumDimensions = 0
    catDxfImportDimensionsEnumDetails = 1
    catDxfImportDimensionsEnumGeometry = 2


class CatDxfImportUnitEnum(Enum):
    """
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.import_unit
    pycatia.cat_dde_settings_interfaces.dxf_setting_att.DxfSettingAtt.set_import_unit
    """
    catDxfImportUnitEnumMillimeter = 0
    catDxfImportUnitEnumCentimeter = 1
    catDxfImportUnitEnumMeter = 2
    catDxfImportUnitEnumInch = 3
    catDxfImportUnitEnumFoot = 4
    catDxfImportUnitEnumScaleFactor = 5
    catDxfImportUnitEnumAutomatic = 6


class CatElectronicType(Enum):
    """
    pycatia.pcb_board_base.pcb_object.PCBObject.electronic_type
    """
    BOARD = 0
    PANEL = 1
    COMPONENT = 2
    AREA = 3
    PCBHOLE = 4
    PCBPATTERN = 5
    NOPCBBEHAVIOUR = 6


class CatFileSelectionMode(Enum):
    """
    pycatia.in_interfaces.application.Application.file_selection_box
    """
    CatFileSelectionModeOpen = 0
    CatFileSelectionModeSave = 1


class CatFileType(Enum):
    """
    pycatia.product_structure_interfaces.product.Product.extract_bom
    """
    catFileTypeText = 0
    catFileTypeMotif = 1
    catFileTypeHTML = 2


class CatFilletBitangencyType(Enum):
    """
    pycatia.part_interfaces.var_rad_edge_fillet.VarRadEdgeFillet.bitangency_type
    """
    catSphereBitangencyType = 0
    catCircleBitangencyType = 1


class CatFilletBoundaryRelimitation(Enum):
    """
    pycatia.part_interfaces.fillet.Fillet.fillet_boundary_relimitation
    """
    catAutomaticFilletBoundaryRelimitation = 0
    catUVFilletBoundaryRelimitation = 1
    catConnectFilletBoundaryRelimitation = 2
    catMinimumFilletBoundaryRelimitation = 3
    catMaximumFilletBoundaryRelimitation = 4


class CatFilletEdgePropagation(Enum):
    """
    pycatia.part_interfaces.edge_fillet.EdgeFillet.edge_propagation
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_edge_fillet_with_constant_radius
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_edge_fillet_with_varying_radius
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_solid_edge_fillet_with_constant_radius
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_solid_edge_fillet_with_varying_radius
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_surface_edge_fillet_with_constant_radius
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_surface_edge_fillet_with_varying_radius
    """
    catMinimalFilletEdgePropagation = 0
    catTangencyFilletEdgePropagation = 1


class CatFilletRepresentation(Enum):
    """
    pycatia.drafting_interfaces.drawing_view_generative_behavior.DrawingViewGenerativeBehavior.fillet_representation
    """
    catFilletRepNone = 0
    catFilletRepBoundary = 1
    catFilletRepSymbolic = 2
    catFilletRepOriginalEdge = 3
    catFilletRepProjectedOriginalEdge = 4


class CatFilletTrimSupport(Enum):
    """
    pycatia.part_interfaces.fillet.Fillet.fillet_trim_support
    """
    catTrimFilletSupport = 0
    catNoTrimFilletSupport = 1


class CatFilletVariation(Enum):
    """
    pycatia.part_interfaces.var_rad_edge_fillet.VarRadEdgeFillet.fillet_variation
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_edge_fillet_with_varying_radius
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_solid_edge_fillet_with_varying_radius
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_surface_edge_fillet_with_varying_radius
    """
    catLinearFilletVariation = 0
    catCubicFilletVariation = 1


class CatFittingShuttleVector(Enum):
    """
    ?
    """
    CATFittingShuttleVectorX = 0
    CATFittingShuttleVectorY = 1
    CATFittingShuttleVectorZ = 2


class CatFullSceneAntiAliasingMode(Enum):
    """
    pycatia.in_interfaces.visualization_setting_att.VisualizationSettingAtt.full_scene_anti_aliasing_mode
    """
    CATFSAAMode_Deactivated = 0
    CATFSAAMode_2xSuperSampling = 1
    CATFSAAMode_4xSuperSampling = 2
    CATFSAAMode_8xSuperSampling = 3
    CATFSAAMode_16xSuperSampling = 4


class CatFunctOrientationDirection(Enum):
    """
    pycatia.funct_system_interfaces.functional_action.FunctionalAction.orientation_direction
    """
    CATFunctNotOriented = 0
    CATFunctOrientedUnidirectional = 1
    CATFunctOrientedBidirectional = 2


class CatGenConferencing(Enum):
    """
    pycatia.in_interfaces.general_session_setting_att.GeneralSessionSettingAtt.conferencing
    """
    NetMeeting = 0
    Backbone = 1


class CatGenDataSave(Enum):
    """
    pycatia.in_interfaces.general_session_setting_att.GeneralSessionSettingAtt.auto_save
    """
    NoAutoBackup = 0
    AutoBackupEvery = 1
    IncrBackup = 2


class CatGenUiStyle(Enum):
    """
    pycatia.in_interfaces.general_session_setting_att.GeneralSessionSettingAtt.ui_style
    """
    UIStyleP1 = 0
    UIStyleP2 = 1
    UIStyleP3 = 2


class CatGeometricType(Enum):
    """
    pycatia.sketcher_interfaces.geometric_element.GeometricElement.geometric_type
    """
    catGeoTypeUnknown = 0
    catGeoTypeAxis2D = 1
    catGeoTypePoint2D = 2
    catGeoTypeLine2D = 3
    catGeoTypeControlPoint2D = 4
    catGeoTypeCircle2D = 5
    catGeoTypeHyperbola2D = 6
    catGeoTypeParabola2D = 7
    catGeoTypeEllipse2D = 8
    catGeoTypeSpline2D = 9
    catGeoTypePoint = 10
    catGeoTypeLine = 11
    catGeoTypePlane = 12


class CatGridPositionMode(Enum):
    """
    pycatia.space_analyses_interfaces.sectioning_setting_att.SectioningSettingAtt.grid_position_mode
    """
    catGridPositionMode_Absolute = 0
    catGridPositionMode_Relative = 1


class CatHiddenLineMode(Enum):
    """
    pycatia.drafting_interfaces.drawing_view_generative_behavior.DrawingViewGenerativeBehavior.hidden_line_mode
    """
    catHlrModeOff = 0
    catHlrModeOn = 1


class CatHoleAnchorMode(Enum):
    """
    pycatia.assembly_interfaces.assembly_hole.AssemblyHole.anchor_mode
    pycatia.part_interfaces.hole.Hole.anchor_mode
    """
    catExtremPointHoleAnchor = 0
    catMiddlePointHoleAnchor = 1


class CatHoleBottomType(Enum):
    """
    pycatia.assembly_interfaces.assembly_hole.AssemblyHole.bottom_type
    pycatia.part_interfaces.hole.Hole.bottom_type
    """
    catFlatHoleBottom = 0
    catVHoleBottom = 1
    catTrimmedHoleBottom = 2


class CatHoleThreadSide(Enum):
    """
    pycatia.part_interfaces.hole.Hole.thread_side
    """
    catRightThreadSide = 0
    catLeftThreadSide = 1


class CatHoleThreadStandard(Enum):
    """
    pycatia.part_interfaces.hole.Hole.create_standard_thread_design_table
    """
    catHoleMetricThinPitch = 0
    catHoleMetricThickPitch = 1


class CatHoleThreadingMode(Enum):
    """
    pycatia.part_interfaces.hole.Hole.threading_mode
    """
    catThreadedHoleThreading = 0
    catSmoothHoleThreading = 1


class CatHoleType(Enum):
    """
    pycatia.assembly_interfaces.assembly_hole.AssemblyHole.type
    pycatia.part_interfaces.hole.Hole.type
    """
    catSimpleHole = 0
    catTaperedHole = 1
    catCounterboredHole = 2
    catCountersunkHole = 3
    catCounterdrilledHole = 4


class CatIg2ExportModeEnum(Enum):
    """
    pycatia.cat_dde_settings_interfaces.ig2_setting_att.Ig2SettingAtt.export_mode
    pycatia.cat_dde_settings_interfaces.ig2_setting_att.Ig2SettingAtt.set_export_mode
    """
    catIg2ExportModeEnumSemantic = 0
    catIg2ExportModeEnumStructured = 1
    catIg2ExportModeEnumGraphic = 2


class CatIg2ExportSheetsEnum(Enum):
    """
    pycatia.cat_dde_settings_interfaces.ig2_setting_att.Ig2SettingAtt.export_sheets
    pycatia.cat_dde_settings_interfaces.ig2_setting_att.Ig2SettingAtt.set_export_sheets
    """
    catIg2ExportSheetsEnumAll = 0
    catIg2ExportSheetsEnumOnlyCurrent = 1


class CatIg2ImportCreateEndPointsEnum(Enum):
    """
    pycatia.cat_dde_settings_interfaces.ig2_setting_att.Ig2SettingAtt.import_end_points
    pycatia.cat_dde_settings_interfaces.ig2_setting_att.Ig2SettingAtt.set_import_end_points
    """
    catIg2ImportCreateEndPointsEnumNever = 0
    catIg2ImportCreateEndPointsEnumFewEntities = 1
    catIg2ImportCreateEndPointsEnumAlways = 2


class CatIg2ImportDestinationViewEnum(Enum):
    """
    pycatia.cat_dde_settings_interfaces.ig2_setting_att.Ig2SettingAtt.import_destination_view
    pycatia.cat_dde_settings_interfaces.ig2_setting_att.Ig2SettingAtt.set_import_destination_view
    """
    catIg2ImportDestinationViewEnumWorkingViews = 0
    catIg2ImportDestinationViewEnumBackground = 1


class CatIg2ImportDimensionsEnum(Enum):
    """
    pycatia.cat_dde_settings_interfaces.ig2_setting_att.Ig2SettingAtt.import_dimensions
    pycatia.cat_dde_settings_interfaces.ig2_setting_att.Ig2SettingAtt.set_import_dimensions
    """
    catIg2ImportDimensionsEnumDimensions = 0
    catIg2ImportDimensionsEnumDetails = 1
    catIg2ImportDimensionsEnumGeometry = 2


class CatIg2ImportUnitEnum(Enum):
    """
    pycatia.cat_dde_settings_interfaces.ig2_setting_att.Ig2SettingAtt.import_unit
    pycatia.cat_dde_settings_interfaces.ig2_setting_att.Ig2SettingAtt.set_import_unit
    """
    catIg2ImportUnitEnumMillimeter = 0
    catIg2ImportUnitEnumCentimeter = 1
    catIg2ImportUnitEnumMeter = 2
    catIg2ImportUnitEnumInch = 3
    catIg2ImportUnitEnumFoot = 4
    catIg2ImportUnitEnumAutomatic = 5


class CatImageRotation(Enum):
    """
    pycatia.in_interfaces.page_setup.PageSetup.rotation
    """
    catImageNoRotation = 0
    catImageRotation90 = 1
    catImageRotation180 = 2
    catImageRotation270 = 3
    catImageBestRotation = 4


class CatImageViewMode(Enum):
    """
    pycatia.drafting_interfaces.drawing_view_generative_behavior.DrawingViewGenerativeBehavior.image_view_mode
    """
    catImageModeOff = 0
    catImageModeHRD = 1


class CatInsureViewNamesUniquenessScope(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_setting_att.Layout2DSettingAtt.insure_view_names_uniqueness_scope
    """
    catInSheet = 0
    catInLayout = 1


class CatJustification(Enum):
    """
    pycatia.drafting_interfaces.drawing_text_properties.DrawingTextProperties.justification
    """
    catLeft = 0
    catCenter = 1
    catRight = 2


class CatLightingMode(Enum):
    """
    pycatia.in_interfaces.viewer_3d.Viewer3D.lighting_mode
    """
    catInfiniteLightSource = 0
    catNeonLightSource = 1


class CatLimitMode(Enum):
    """
    pycatia.part_interfaces.limit.Limit.limit_mode
    """
    catOffsetLimit = 0
    catUpToNextLimit = 1
    catUpToLastLimit = 2
    catUpToPlaneLimit = 3
    catUpToSurfaceLimit = 4
    catUpThruNextLimit = 5


class CatManipAutoInsertMode(Enum):
    """
    ?
    """
    CATOnMouseRelease = 0
    CATWhileMouseMoving = 1


class CatManipClashMode(Enum):
    """
    ?
    """
    CATManipClashModeNo = 0
    CATManipClashModeOn = 1
    CATManipClashModeStop = 2


class CatManufacturingPrecedenceType(Enum):
    """
    pycatia.manufacturing_interfaces.manufacturing_precedences.ManufacturingPrecedences.add_operation
    pycatia.manufacturing_interfaces.manufacturing_precedence.ManufacturingPrecedence.precedence_type
    """
    catPrecedenceTypeJustBefore = 0
    catPrecedenceTypeBefore = 1


class CatMarker2DType(Enum):
    """
    pycatia.navigator_interfaces.marker_2D.Marker2D.type
    """
    catMarker2DTypeLine = 0
    catMarker2DTypeArrow = 1
    catMarker2DTypeRectangle = 2
    catMarker2DTypeCircle = 3
    catMarker2DTypeFreeHand = 4
    catMarker2DTypeText = 5
    catMarker2DTypePicture = 6


class CatMarker3DType(Enum):
    """
    pycatia.navigator_interfaces.marker_3D.Marker3D.type
    """
    catMarker3DTypeText = 0


class CatMarkerTextOrientation(Enum):
    """
    pycatia.navigator_interfaces.marker_2D.Marker2D.text_orientation
    pycatia.navigator_interfaces.marker_3D.Marker3D.text_orientation
    """
    CatMarkerTextOrientationRight = 0
    CatMarkerTextOrientationUp = 1
    CatMarkerTextOrientationLeft = 2
    CatMarkerTextOrientationDown = 3


class CatMeasurableName(Enum):
    """
    pycatia.space_analyses_interfaces.measurable.Measurable.geometry_name
    """
    CatMeasurableUnknown = 0
    CatMeasurable = 1
    CatMeasurableVolume = 2
    CatMeasurableSurface = 3
    CatMeasurableCylinder = 4
    CatMeasurableSphere = 5
    CatMeasurableCone = 6
    CatMeasurablePlane = 7
    CatMeasurableCurve = 8
    CatMeasurableCircle = 9
    CatMeasurableLine = 10
    CatMeasurablePoint = 11
    CatMeasurableAxisSystem = 12


class CatMergeMode(Enum):
    """
    pycatia.part_interfaces.sweep.Sweep.merge_mode
    """
    catMergeOff = 0
    catMergeOn = 1


class CatMultiSelectionMode(Enum):
    """
    pycatia.in_interfaces.selection.Selection.select_element3
    """
    CATMonoSel = 0
    CATMultiSelTriggWhenSelPerf = 1
    CATMultiSelTriggWhenUserValidatesSelection = 2


class CatNavigationStyle(Enum):
    """
    pycatia.in_interfaces.viewer_3d.Viewer3D.navigation_style
    """
    catNavigationExamine = 0
    catNavigationWalk = 1
    catNavigationFly = 2


class CatOptimizationType(Enum):
    """
    pycatia.knowledge_interfaces.optimization.Optimization.optimization_type
    """
    catMinimum = 0
    catMaximum = 1
    catTargetValue = 2
    catOnlyBoundedVariation = 3
    catNone = 4
    catCstOnly = 5


class CatOutPutFormatType(Enum):
    """
    pycatia.general_knowledge_interfaces.expert_rule_base_runtime.ExpertRuleBaseRuntime.report_output_format
    """
    KWEHtml = 0
    KWEText = 1
    KWEPrint = 2
    KWEEmail = 3


class CatPaperOrientation(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_sheet.Layout2DSheet.orientation
    pycatia.drafting_interfaces.drawing_sheet.DrawingSheet.orientation
    pycatia.in_interfaces.page_setup.PageSetup.orientation
    pycatia.in_interfaces.printer.Printer.orientation
    """
    catPaperPortrait = 0
    catPaperLandscape = 1
    catPaperBestFit = 2


class CatPaperSize(Enum):
    """
    pycatia.in_interfaces.printer.Printer.paper_size
    pycatia.drafting_2dL_interfaces.layout_2d_sheet.Layout2DSheet.paper_size
    pycatia.drafting_interfaces.drawing_sheet.DrawingSheet.paper_size
    pycatia.in_interfaces.page_setup.PageSetup.paper_size
    """
    catPaperLetter = 0
    catPaperLegal = 1
    catPaperA0 = 2
    catPaperA1 = 3
    catPaperA2 = 4
    catPaperA3 = 5
    catPaperA4 = 6
    catPaperA = 7
    catPaperB = 8
    catPaperC = 9
    catPaperD = 10
    catPaperE = 11
    catPaperF = 12
    catPaperUser = 13


class CatPartElementsNamingMode(Enum):
    """
    pycatia.mec_mod_interfaces.part_infrastructure_setting_att.PartInfrastructureSettingAtt.naming_mode
    """
    catNoNamingCheck = 0
    catNamingCheckUnderSameNode = 1
    catNamingCheckWithinUIActiveObject = 2


class CatPartSurfaceElementsLocation(Enum):
    """
    pycatia.mec_mod_interfaces.part_infrastructure_setting_att.PartInfrastructureSettingAtt.surface_elements_location
    """
    catPartBodyLocation = 0
    catXGSLocation = 1


class CatPartUpdateMode(Enum):
    """
    pycatia.mec_mod_interfaces.part_infrastructure_setting_att.PartInfrastructureSettingAtt.update_mode
    """
    catManualUpdate = 0
    catAutomaticUpdate = 1


class CatPictureFormat(Enum):
    """
    pycatia.drafting_interfaces.drawing_picture.DrawingPicture.format
    """
    catPictureNONE = 0
    catPicturePNG = 1
    catPictureJPEG = 2
    catPictureCCITTG3 = 3


class CatPointsProjectionMode(Enum):
    """
    pycatia.drafting_interfaces.drawing_view_generative_behavior.DrawingViewGenerativeBehavior.points_projection_mode
    """
    catPointsProjectionModeOff = 0
    catPointsProjectionModeOn = 1


class CatPrintColor(Enum):
    """
    pycatia.in_interfaces.page_setup.PageSetup.color
    """
    catColorTrueColor = 0
    catColorGreyScale = 1
    catColorMonochrome = 2


class CatPrintLineCap(Enum):
    """
    pycatia.in_interfaces.page_setup.PageSetup.line_cap
    """
    catPrintFlat = 0
    catPrintSquare = 1
    catPrintRound = 2


class CatPrintLineSpecification(Enum):
    """
    pycatia.in_interfaces.page_setup.PageSetup.line_type_specification
    pycatia.in_interfaces.page_setup.PageSetup.line_width_specification
    """
    catPrintAbsolute = 0
    catPrintScaled = 1
    catPrintNoThickness = 2


class CatPrintQuality(Enum):
    """
    pycatia.in_interfaces.page_setup.PageSetup.quality
    """
    catPrintQualityDraft = 0
    catPrintQualityLow = 1
    catPrintQualityMedium = 2
    catPrintQualityHigh = 3
    catPrintQualityCustom = 4


class CatPrintRenderingMode(Enum):
    """
    pycatia.in_interfaces.page_setup.PageSetup.print_rendering_mode
    """
    catPrintRenderingModeDefault = 0
    catPrintRenderingModeWireframe = 1
    catPrintRenderingModeHiddenLineRemoval = 2
    catPrintRenderingModeShadingWithTriangles = 3
    catPrintRenderingModeDynamicHiddenLineRemoval = 4
    catPrintRenderingModeOnScreen = 5


class CatPrinterDirState(Enum):
    """
    pycatia.in_interfaces.printers_setting_att.PrintersSettingAtt.add_printer_directory
    pycatia.in_interfaces.printers_setting_att.PrintersSettingAtt.get_printer_directory_state
    pycatia.in_interfaces.printers_setting_att.PrintersSettingAtt.modify_printer_directory_state
    """
    CatPrinterDirFree = 0
    CatPrinterDirProtect = 1


class CatPrismExtrusionDirection(Enum):
    """
    pycatia.part_interfaces.prism.Prism.direction_type
    pycatia.assembly_interfaces.assembly_pocket.AssemblyPocket.direction_type
    """
    catNormalToSketchDirection = 0
    catNotNormalToSketchDirection = 1


class CatPrismOrientation(Enum):
    """
    pycatia.assembly_interfaces.assembly_pocket.AssemblyPocket.direction_orientation
    pycatia.part_interfaces.prism.Prism.direction_orientation
    """
    catRegularOrientation = 0
    catInverseOrientation = 1


class CatProductSource(Enum):
    """
    pycatia.product_structure_interfaces.product.Product.source
    pycatia.osm_interfaces.scene.Scene.get_source
    """
    catProductSourceUnknown = 0
    catProductMade = 1
    catProductBought = 2


class CatProjViewType(Enum):
    """
    pycatia.drafting_interfaces.drawing_view_generative_behavior.DrawingViewGenerativeBehavior.define_projection_view
    """
    catRightView = 0
    catLeftView = 1
    catTopView = 2
    catBottomView = 3
    catRearView = 4


class CatProjectionMode(Enum):
    """
    pycatia.in_interfaces.viewpoint_3d.ViewPoint3D.projection_mode
    pycatia.navigator_interfaces.annotated_view.AnnotatedView.projection_mode
    """
    catProjectionConic = 0
    catProjectionCylindric = 1
    catProjectionUndefined = 2


class CatPspIdlApplicationId(Enum):
    """
    pycatia.cat_plant_ship_interfaces.psp_object.PSPObject.application_id
    pycatia.cat_plant_ship_interfaces.psp_workbench.PSPWorkbench.get_application
    """
    catPspIDLCATPiping = 0
    catPspIDLCATHVAC = 1
    catPspIDLCATEquipment = 2
    catPspIDLCATWaveguide = 3
    catPspIDLCATTubing = 4
    catPspIDLCATHanger = 5
    catPspIDLCATRaceway = 6
    catPspIDLCATConduit = 7
    catPspIDLCATCompAccess = 8
    catPspIDLCATElectrical = 9
    catPspIDLCATPID = 10
    catPspIDLCATHVACDiagram = 11
    catPspIDLCATTubingDiagram = 12
    catPspIDLCATWaveguideDiagram = 13
    catPspIDLCATElectricalDiagram = 14


class CatPspIdlAttrDataType(Enum):
    """
    pycatia.cat_plant_ship_interfaces.psp_attribute.PSPAttribute.get_type
    """
    catPspIDLInteger = 0
    catPspIDLDouble = 1
    catPspIDLString = 2
    catPspIDLMultiString = 3
    catPspIDLBoolean = 4


class CatPspIdlDomainId(Enum):
    """
    pycatia.cat_plant_ship_interfaces.psp_connectable.PSPConnectable.connectors
    pycatia.cat_plant_ship_interfaces.psp_app_factory.PSPAppFactory.list_physicals
    pycatia.cat_plant_ship_interfaces.psp_attribute.PSPAttribute.list_attributes
    pycatia.cat_plant_ship_interfaces.psp_object.PSPObject.domain_id
    """
    catPspIDLNone = 0
    catPspIDLCATPIP = 1
    catPspIDLCATINS = 2
    catPspIDLCATHVA = 3
    catPspIDLCATEQT = 4
    catPspIDLCATTUB = 5
    catPspIDLCATMLD = 6
    catPspIDLCATWVG = 7
    catPspIDLCATRWY = 8
    catPspIDLCATCND = 9
    catPspIDLCATHGR = 10
    catPspIDLCATCAM = 11
    catPspIDLCATELE = 12


class CatPspIdlFlowCapability(Enum):
    """
    pycatia.cat_plant_ship_interfaces.psp_cntr_flow.PSPCntrFlow.flow_capability
    """
    catPspIDLFlowCapability_Undefined = 0
    catPspIDLFlowCapability_InDirection = 1
    catPspIDLFlowCapability_OutDirection = 2
    catPspIDLFlowCapability_InOutDirection = 3


class CatPspIdlFlowReality(Enum):
    """
    pycatia.cat_plant_ship_interfaces.psp_cntr_flow.PSPCntrFlow.flow_reality
    """
    catPspIDLFlowReality_Undefined = 0
    catPspIDLFlowReality_InDirection = 1
    catPspIDLFlowReality_OutDirection = 2
    catPspIDLFlowReality_InOutDirection = 3


class CatPspIdlFunctionStatus(Enum):
    """
    pycatia.cat_plant_ship_interfaces.psp_functional.PSPFunctional.function_status
    """
    catPspIDLFuncUndefined = 0
    catPspIDLInFuncNet = 1
    catPspIDLFuncNetPhysType = 2
    catPspIDLFuncNetPhysNoPos = 3
    catPspIDLFuncNoNetPhys = 4
    catPspIDLFuncNetPhys = 5


class CatPspIdlPartConnectorType(Enum):
    """
    pycatia.cat_plant_ship_interfaces.psp_phsyical_product.PSPPhsyicalProduct.add_connector
    pycatia.cat_plant_ship_interfaces.psp_part_connector.PSPPartConnector.align_type
    pycatia.cat_plant_ship_interfaces.psp_part_connector.PSPPartConnector.clock_type
    pycatia.cat_plant_ship_interfaces.psp_part_connector.PSPPartConnector.face_type
    pycatia.cat_plant_ship_interfaces.psp_part_connector.PSPPartConnector.set_alignment_connector
    pycatia.cat_plant_ship_interfaces.psp_part_connector.PSPPartConnector.set_face_connector
    pycatia.cat_plant_ship_interfaces.psp_part_connector.PSPPartConnector.set_orientation_connector
    """
    catPspIDLPartCtrTypeNotRecognized = 0
    catPspIDLPartCtrTypeFace = 1
    catPspIDLPartCtrTypeSupport = 2
    catPspIDLPartCtrTypeCenter = 3
    catPspIDLPartCtrTypeTop = 4
    catPspIDLPartCtrTypeBottom = 5
    catPspIDLPartCtrTypeLeft = 6
    catPspIDLPartCtrTypeRight = 7
    catPspIDLPartCtrTypeTopLeft = 8
    catPspIDLPartCtrTypeTopRight = 9
    catPspIDLPartCtrTypeBottomLeft = 10
    catPspIDLPartCtrTypeBottomRight = 11
    catPspIDLPartCtrTypeCircular = 12
    catPspIDLPartCtrTypeRectangular = 13
    catPspIDLPartCtrTypeUpOnly = 14


class CatRectangularPatternParameters(Enum):
    """
    pycatia.part_interfaces.rect_pattern.RectPattern.first_rectangular_pattern_parameters
    pycatia.part_interfaces.rect_pattern.RectPattern.second_rectangular_pattern_parameters
    """
    catInstancesandSpacing = 0
    catUnequalSpacing = 1


class CatRenderingMode(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_sheet.Layout2DSheet.print_out
    pycatia.drafting_2dL_interfaces.layout_2d_sheet.Layout2DSheet.print_to_file
    pycatia.drafting_2dL_interfaces.layout_2d_root.Layout2DRoot.rendering_mode
    pycatia.in_interfaces.viewer_3d.Viewer3D.rendering_mode
    """
    catRenderShading = 0
    catRenderShadingWithEdges = 1
    catRenderWireFrame = 2
    catRenderHiddenLinesRemoval = 3
    catRenderQuickHiddenLinesRemoval = 4
    catRenderMaterial = 5
    catRenderMaterialWithEdges = 6
    catRenderShadingWithEdgesAndHiddenEdges = 7
    catRenderShadingWithEdgesWithoutSmoothEdges = 8
    catRenderWireFrameWithoutSmoothEdgesWithoutVertices = 9
    catRenderWireFrameWithHalfSmoothEdgesWithoutVertices = 10
    catRenderShadingWithEdgesWithOutlines = 11
    catRenderQuickHiddenLinesRemovalWithoutVertices = 12
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithOutlines = 13
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithOutlinesWithoutVertices = 14
    catRenderWireFrameWithHalfSmoothEdgeWithOutlinesWithoutVertices = 15
    catRenderWireFrameWithOutlinesWithoutSmoothEdgesWithoutVertices = 16
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithoutSmoothEdgesWithoutVertices = 17
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithHalfSmoothEdgeWithoutVertices = 18
    catRenderQuickHiddenLinesRemovalWithoutSmoothEdgesWithoutVertices = 19
    catRenderQuickHiddenLinesRemovalWithHalfSmoothEdgeWithoutVertices = 20
    catRenderShadingWithEdgesWithHalfSmoothEdgeWithoutVertices = 21
    catRenderShadingWithEdgesWithHalfSmoothEdge = 22


class CatRepType(Enum):
    """
    pycatia.product_structure_interfaces.product.Product.add_shape_representation
    pycatia.product_structure_interfaces.product.Product.get_shape_representation
    pycatia.product_structure_interfaces.product.Product.has_shape_representation
    pycatia.product_structure_interfaces.product.Product.remove_shape_representation
    """
    catRep3D = 0
    catRep2D = 1
    catRepText = 2


class CatRepresentationMode(Enum):
    """
    pycatia.drafting_interfaces.drawing_view_generative_behavior.DrawingViewGenerativeBehavior.representation_mode
    """
    catExactMode = 0
    catPolyhedricMode = 1
    catVisualMode = 2


class CatSacSettingsEnum(Enum):
    """
    pycatia.navigator_interfaces.n_4D_navigator_setting_att.N4DNavigatorSettingAtt.insert_mode
    """
    CatSacSettingsEnumNoInsert = 0
    CatSacSettingsEnumAutomatic = 1
    CatSacSettingsEnumUserPrompt = 2


class CatSampledAnalysisMode(Enum):
    """
    pycatia.fitting_interfaces.sampled.Sampled.bind_analysis
    """
    CatSampledAnalysisOff = 0
    CatSampledAnalysisOn = 1
    CatSampledAnalysisStop = 2
    CatSampledAnalysisVerbose = 3


class CatSampledSplitType(Enum):
    """
    pycatia.fitting_interfaces.sampled.Sampled.split
    """
    CatSampledSplitOnSeg = 0
    CatSampledSplitOnShot = 1


class CatSceneType(Enum):
    """
    pycatia.osm_interfaces.product_scene.ProductScene.type
    """
    CatSceneTypeDelta = 0
    CatSceneTypeFull = 1


class CatSchIdlApplicationId(Enum):
    """
    pycatia.cat_sch_platform_interfaces.schematic_root.SchematicRoot.get_application_object_factory
    """
    catSchIDLCATPID = 0
    catSchIDLCATHVACDiagram = 1
    catSchIDLCATWaveguideDiagram = 2
    catSchIDLCATTubingDiagram = 3
    catSchIDLCATElectricalDiagram = 4


class CatSchIdlArrowFrequency(Enum):
    """
    ?
    """
    catSchIDLArrowAllSegs = 0
    catSchIDLArrowAllButLastSeg = 1
    catSchIDLArrowInteriorSegs = 2
    catSchIDLArrowMiddleSeg = 3


class CatSchIdlArrowPosition(Enum):
    """
    ?
    """
    catSchIDLMidSegArrow = 0
    catSchIDLEndSegArrow = 1


class CatSchIdlArrowStyle(Enum):
    """
    ?
    """
    catSchIDLFillArrow = 0
    catSchIDLNotFillArrow = 1
    catSchIDLStandardArrow = 2


class CatSchIdlCntrFlowCapability(Enum):
    """
    pycatia.cat_sch_platform_interfaces.sch_app_cntr_flow.SchAppCntrFlow.app_get_flow_capability
    pycatia.cat_sch_platform_interfaces.sch_app_cntr_flow.SchAppCntrFlow.app_set_flow_capability
    """
    catSchIDLCntrFlowCapability_Undefined = 0
    catSchIDLCntrFlowCapability_InDirection = 1
    catSchIDLCntrFlowCapability_OutDirection = 2
    catSchIDLCntrFlowCapability_InOutDirection = 3


class CatSchIdlCntrFlowReality(Enum):
    """
    pycatia.cat_sch_platform_interfaces.sch_app_cntr_flow.SchAppCntrFlow.app_get_flow_reality
    pycatia.cat_sch_platform_interfaces.sch_app_cntr_flow.SchAppCntrFlow.app_set_flow_capability
    pycatia.cat_sch_platform_interfaces.sch_app_cntr_flow.SchAppCntrFlow.app_set_flow_reality
    """
    catSchIDLCntrFlowReality_Undefined = 0
    catSchIDLCntrFlowReality_InDirection = 1
    catSchIDLCntrFlowReality_OutDirection = 2
    catSchIDLCntrFlowReality_InOutDirection = 3


class CatSchIdlCntrSymbolType(Enum):
    """
    pycatia.cat_sch_platform_interfaces.sch_grr_cntr.SchGRRCntr.get_symbol
    pycatia.cat_sch_platform_interfaces.sch_grr_cntr.SchGRRCntr.set_symbol
    """
    catSchIDLCntrSymbol_Undefined = 0
    catSchIDLCntrSymbol_Point = 1
    catSchIDLCntrSymbol_PtVector = 2
    catSchIDLCntrSymbol_OnOffSheet = 3
    catSchIDLCntrSymbol_LineBoundary = 4


class CatSchIdlDisplayMode(Enum):
    """
    ?
    """
    catSchIDLDisplayMode_Default = 0
    catSchIDLDisplayMode_Alternate = 1


class CatSchIdlExtensionType(Enum):
    """
    pycatia.cat_sch_platform_interfaces.schematic_extension.SchematicExtension.add_extension
    pycatia.cat_sch_platform_interfaces.schematic_extension.SchematicExtension.remove_extension
    """
    catSchIDLComponent_Extension = 0
    catSchIDLRoute_Extension = 1
    catSchIDLCompConnector_Extension = 2
    catSchIDLRouteConnector_Extension = 3
    catSchIDLZone_Extension = 4


class CatSchIdlGapPriority(Enum):
    """
    pycatia.cat_sch_platform_interfaces.sch_app_gap_priority.SchAppGapPriority.app_choose_gap_priority
    """
    catSchIDLGapThisRoute = 0
    catSchIDLGapInputRoute = 1
    catSchIDLGapNoPriority = 2
    catSchIDLGapHorizontalSeg = 3
    catSchIDLGapVerticalSeg = 4


class CatSchIdlGapStyle(Enum):
    """
    ?
    """
    catSchIDLBlankGap = 0
    catSchIDLJumpGap = 1
    catSchIDLWavyGap = 2


class CatSchIdlInternalFlowStatus(Enum):
    """
    pycatia.cat_sch_platform_interfaces.sch_internal_flow.SchInternalFlow.get_status
    pycatia.cat_sch_platform_interfaces.sch_internal_flow.SchInternalFlow.set_status
    """
    catSchIDLInternFlowStatus_Undefined = 0
    catSchIDLInternFlowStatus_Open = 1
    catSchIDLInternFlowStatus_Close = 2


class CatSchIdlInternalFlowType(Enum):
    """
    pycatia.cat_sch_platform_interfaces.sch_internal_flow.SchInternalFlow.get_insertion_type
    """
    catSchIDLInternFlowType_Undefined = 0
    catSchIDLInternFlowType_Corner = 1
    catSchIDLInternFlowType_Linear = 2


class CatSchIdlMultiImageStatus(Enum):
    """
    pycatia.cat_sch_platform_interfaces.sch_app_multi_image.SchAppMultiImage.app_is_up_to_date
    """
    catSchIDLImage_IsUpToDate = 0
    catSchIDLImage_MasterNotFound = 1
    catSchIDLImage_MasterDocNotFound = 2
    catSchIDLImage_InvalidReference = 3
    catSchIDLImage_AttrsNotUpToDate = 4


class CatSchIdlRouteAlternateGraphicStyle(Enum):
    """
    pycatia.cat_sch_platform_interfaces.sch_route_alternate_graphic.SchRouteAlternateGraphic.remove_all_alternate_graphics_of_style
    pycatia.cat_sch_platform_interfaces.sch_grr_route_alternate.SchGRRRouteAlternate.get_alternate_style
    """
    catSchIDLRouteAlternateGraphicStyle_ellipse = 0


class CatSchIdlRouteCompressMode(Enum):
    """
    pycatia.cat_sch_platform_interfaces.sch_grr_route.SchGRRRoute.set_path
    pycatia.cat_sch_platform_interfaces.sch_grr_route.SchGRRRoute.set_path2
    pycatia.cat_sch_platform_interfaces.sch_grr_route.SchGRRRoute.set_path3
    """
    catSchIDLCompressOff = 0
    catSchIDLCompressOn = 1


class CatSchIdlRouteMode(Enum):
    """
    pycatia.cat_sch_platform_interfaces.sch_base_factory.SchBaseFactory.create_route_and_connect_to_objects
    pycatia.cat_sch_platform_interfaces.sch_route.SchRoute.reshape_extremity2
    """
    catSchIDLRouteMode_Undefined = 0
    catSchIDLRouteMode_HorizontalVertical = 1
    catSchIDLRouteMode_HorizontalVertical45 = 2
    catSchIDLRouteMode_PointToPoint = 3
    catSchIDLRouteMode_AroundObject = 4


class CatSchIdlRouteSymbolUpdateMode(Enum):
    """
    pycatia.cat_sch_platform_interfaces.sch_grr_route.SchGRRRoute.set_path3
    """
    catSchIDLSymbolUpdateOff = 0
    catSchIDLSymbolUpdateOn = 1


class CatSchIdlRouteUnsetGapsMode(Enum):
    """
    pycatia.cat_sch_platform_interfaces.sch_grr_route.SchGRRRoute.compress2
    pycatia.cat_sch_platform_interfaces.sch_grr_route.SchGRRRoute.set_path2
    pycatia.cat_sch_platform_interfaces.sch_grr_route.SchGRRRoute.set_path3
    """
    catSchIDLUnsetGapsOff = 0
    catSchIDLUnsetGapsOn = 1


class CatSchIdlgrrRouteReshapeMode(Enum):
    """
    pycatia.cat_sch_platform_interfaces.sch_grr_route2.SchGRRRoute2.get_reshape_mode
    pycatia.cat_sch_platform_interfaces.sch_grr_route2.SchGRRRoute2.set_reshape_mode
    """
    catSchIDLFixedShapeOff = 0
    catSchIDLFixedShapeOn = 1


class CatScriptLanguage(Enum):
    """
    pycatia.system_interfaces.system_service.SystemService.evaluate
    pycatia.in_interfaces.macros_setting_att.MacrosSettingAtt.get_language_editor
    pycatia.in_interfaces.macros_setting_att.MacrosSettingAtt.set_language_editor
    """
    CATVBScriptLanguage = 0
    CATVBALanguage = 1
    CATBasicScriptLanguage = 2
    CATJavaLanguage = 3
    CATJScriptLanguage = 4


class CatScriptLibraryType(Enum):
    """
    pycatia.system_interfaces.system_service.SystemService.execute_script
    """
    catScriptLibraryTypeDocument = 0
    catScriptLibraryTypeDirectory = 1
    catScriptLibraryTypeVBAProject = 2


class CatSearchContextScope(Enum):
    """
    pycatia.in_interfaces.search_setting_att.SearchSettingAtt.default_power_input_context_scope
    """
    Everywhere = 0
    InWorkbench = 1
    FromWorkbench = 2
    FromSelection = 3
    VisibleOnScreen = 4


class CatSecWindowOpenMode(Enum):
    """
    pycatia.in_interfaces.search_setting_att.SearchSettingAtt.default_power_input_context_scope
    """
    catSecWindow_DefaultSize = 0
    catSecWindow_TileVertically = 1


class CatSectionBehavior(Enum):
    """
    pycatia.space_analyses_interfaces.section.Section.behavior
    """
    catSectionBehaviorManual = 0
    catSectionBehaviorAutomatic = 1
    catSectionBehaviorFreeze = 2


class CatSectionClippingMode(Enum):
    """
    pycatia.space_analyses_interfaces.sectioning_setting_att.SectioningSettingAtt.clipping_mode
    """
    catSection_Software = 0
    catSection_OpenGL = 1


class CatSectionGridStyle(Enum):
    """
    pycatia.space_analyses_interfaces.sectioning_setting_att.SectioningSettingAtt.grid_style
    """
    catSectionGridStyle_Lines = 0
    catSectionGridStyle_Crosses = 1


class CatSectionPlaneNormal(Enum):
    """
    pycatia.space_analyses_interfaces.sectioning_setting_att.SectioningSettingAtt.plane_normal
    """
    catSectionNormal_X = 0
    catSectionNormal_Y = 1
    catSectionNormal_Z = 2


class CatSectionPlaneOrigin(Enum):
    """
    pycatia.space_analyses_interfaces.sectioning_setting_att.SectioningSettingAtt.plane_origin
    """
    catSectionOrigin_0 = 0
    catSectionOrigin_Selection = 1


class CatSectionType(Enum):
    """
    pycatia.space_analyses_interfaces.section.Section.type
    """
    catSectionTypePlane = 0
    catSectionTypeSlice = 1
    catSectionTypeBox = 2


class CatSelectionFilter(Enum):
    """
    pycatia.in_interfaces.selected_element.SelectedElement.type
    pycatia.in_interfaces.selection.Selection.select_element2
    """
    ZeroDim = 0
    MonoDim = 1
    MonoDimInfinite = 2
    RectilinearMonoDim = 3
    RectilinearMonoDimInfinite = 4
    BiDim = 5
    BiDimInfinite = 6
    PlanarBiDim = 7
    PlanarBiDimInfinite = 8
    CylindricalBiDim = 9
    TriDim = 10


class CatSewingIntersectionMode(Enum):
    """
    pycatia.part_interfaces.sew_surface.SewSurface.sewing_intersection_mode
    """
    catSewingNoIntersect = 0
    catSewingIntersect = 1


class CatSheetGenViewsPosMode(Enum):
    """
    pycatia.drafting_interfaces.drawing_sheet.DrawingSheet.gen_views_pos_mode
    """
    catFixedCG = 0
    catFixedAxis = 1


class CatSheetProjectionMethod(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_sheet.Layout2DSheet.projection_method
    pycatia.drafting_interfaces.drawing_sheet.DrawingSheet.projection_method
    """
    catFirstAngle = 0
    catThirdAngle = 1


class CatShowResultType(Enum):
    """
    pycatia.general_knowledge_interfaces.expert_rule_base_runtime.ExpertRuleBaseRuntime.report_show_result
    """
    ByRule = 0
    ByObject = 1
    ByState = 2


class CatShuttleMoveMode(Enum):
    """
    pycatia.fitting_interfaces.shuttle.Shuttle.move_mode
    """
    CatShuttle = 0
    CatAxis = 1


class CatShuttleVector(Enum):
    """
    pycatia.fitting_interfaces.shuttle.Shuttle.vector
    """
    CatShuttleVectorX = 0
    CatShuttleVectorY = 1
    CatShuttleVectorZ = 2


class CatSolveType(Enum):
    """
    pycatia.general_knowledge_interfaces.expert_rule_base_runtime.ExpertRuleBaseRuntime.solve_type
    """
    ManualSolveType = 0
    AutomaticOptimizedSolveType = 1
    AutomaticCompleteSolveType = 2


class CatSpecsAndGeomWindowLayout(Enum):
    """
    pycatia.in_interfaces.specs_and_geom_window.SpecsAndGeomWindow.layout
    """
    catWindowSpecsOnly = 0
    catWindowGeomOnly = 1
    catWindowSpecsAndGeom = 2


class CatSpecsLayout(Enum):
    """
    pycatia.in_interfaces.specs_viewer.SpecsViewer.layout
    """
    catSpecsViewerHorizontalIndented = 0
    catSpecsViewerHorizontalUp = 1
    catSpecsViewerHorizontalCentered = 2
    catSpecsViewerVerticalCentered = 3
    catSpecsViewerHorizontalRelational = 4
    catSpecsViewerVerticalRelational = 5


class CatSplitSide(Enum):
    """
    pycatia.part_interfaces.replace_face.ReplaceFace.splitting_side
    pycatia.assembly_interfaces.assembly_features.AssemblyFeatures.add_assembly_split
    pycatia.assembly_interfaces.assembly_split.AssemblySplit.splitting_side
    pycatia.part_interfaces.sew_surface.SewSurface.sewing_side
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_replace_face
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_sew_surface
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_split
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_surfacic_sew_surface
    pycatia.part_interfaces.shape_factory.ShapeFactory.add_new_volume_sew_surface
    """
    catPositiveSide = 0
    catNegativeSide = 1


class CatStrCreationMode(Enum):
    """
    ?
    """
    catStrPartMode = 0
    catStrSheetMetalMode = 1


class CatStrCutbackType(Enum):
    """
    pycatia.structure_interfaces.str_cutback.StrCutback.type
    pycatia.structure_interfaces.str_member.StrMember.create_cutback
    """
    catStrNoneType = 0
    catStrNormalType = 1
    catStrWeldedType = 2
    catStrMiteredType = 3
    catStrNotchingType = 4


class CatStrLinkMode(Enum):
    """
    ?
    """
    catStrWithLinkMode = 0
    catStrNoLinkMode = 1
    catStrRefRefWithLinkMode = 2
    catStrRefRefNoLinkMode = 3


class CatStrMaterialOrientation(Enum):
    """
    pycatia.structure_interfaces.str_object_factory.StrObjectFactory.add_dim_member_with_support
    pycatia.structure_interfaces.str_object_factory.StrObjectFactory.add_plate
    pycatia.structure_interfaces.str_object_factory.StrObjectFactory.add_plate_on_surface
    pycatia.structure_interfaces.str_object_factory.StrObjectFactory.add_rectangular_end_plate
    """
    catStrStandardOrientation = 0
    catStrReverseOrientation = 1


class CatStrMemberExtremity(Enum):
    """
    pycatia.structure_interfaces.str_object_factory.StrObjectFactory.add_def_ext_on_member
    pycatia.structure_interfaces.str_object_factory.StrObjectFactory.add_rectangular_end_plate
    """
    catStartExtremity = 0
    catEndExtremity = 1
    catBothExtremity = 2


class CatStrPlacementPoint(Enum):
    """
    ?
    """
    catStrDefault = 0
    catStrBottomLeft = 1
    catStrBottomCenter = 2
    catStrBottomRight = 3
    catStrCenterLeft = 4
    catStrCenterCenter = 5
    catStrCenterRight = 6
    catStrTopLeft = 7
    catStrTopCenter = 8
    catStrTopRight = 9
    catStrGravity = 10
    catStrGravityBottom = 11
    catStrGravityLeft = 12
    catStrGravityRight = 13
    catStrGravityTop = 14
    catStrUserPoint = 15


class CatStrPlaneMode(Enum):
    """
    pycatia.structure_interfaces.str_object_factory.StrObjectFactory.add_dim_member_on_plane
    pycatia.structure_interfaces.str_object_factory.StrObjectFactory.add_dim_member_with_support
    pycatia.structure_interfaces.str_object_factory.StrObjectFactory.add_member_from_dir
    pycatia.structure_interfaces.str_object_factory.StrObjectFactory.add_member_from_math_plane
    """
    catStrNoneMode = 0
    catStrOnPlane = 1
    catStrParallelToPlane = 2


class CatStrSectionProperties(Enum):
    """
    pycatia.structure_interfaces.str_section.StrSection.get_property
    """
    CatStrArea = 0
    CatStrInertiaXX = 1
    CatStrInertiaYY = 2
    CatStrModuleInertiaX = 3
    CatStrModuleInertiaY = 4
    CatStrGirationModuleX = 5
    CatStrGirationModuleY = 6


class CatSymbolType(Enum):
    """
    pycatia.drafting_interfaces.drawing_arrow.DrawingArrow.head_symbol
    pycatia.drafting_interfaces.drawing_arrow.DrawingArrow.tail_symbol
    pycatia.drafting_interfaces.drawing_leader.DrawingLeader.head_symbol
    """
    catNotUsed = 0
    catCross = 1
    catPlus = 2
    catConcentric = 3
    catCoincident = 4
    catFullCircle = 5
    catFullSquare = 6
    catStar = 7
    catDot = 8
    catSmallDot = 9
    catMisc1 = 10
    catMisc2 = 11
    catFullCircle2 = 12
    catFullSquare2 = 13
    catOpenArrow = 14
    catUnfilledArrow = 15
    catBlankedArrow = 16
    catFilledArrow = 17
    catUnfilledCircle = 18
    catBlankedCircle = 19
    catFilledCircle = 20
    catCrossedCircle = 21
    catBlankedSquare = 22
    catFilledSquare = 23
    catBlankedTriangle = 24
    catFilledTriangle = 25
    catManipulatorSquare = 26
    catMamipulatorDiamond = 27
    catManipulatorCircle = 28
    catManipulatorTriangle = 29
    catDoubleOpenArrow = 30
    catWave = 31


class CatTableBorderType(Enum):
    """
    pycatia.drafting_interfaces.drawing_table.DrawingTable.get_cell_border_type
    """
    CatTableNone = 0
    CatTableLeft = 1
    CatTableTop = 2
    CatTableRight = 3
    CatTableBottom = 4
    CatTableBackSlashed = 5
    CatTableSlashed = 6
    CatTableHorStrikedOut = 7
    CatTableVerStrikedOut = 8
    CatTableOutLine = 9
    CatTableInside = 10
    CatTableCross = 11


class CatTableComputeMode(Enum):
    """
    pycatia.drafting_interfaces.drawing_table.DrawingTable.compute_mode
    """
    CatTableComputeOFF = 0
    CatTableComputeON = 1


class CatTableInvertMode(Enum):
    """
    pycatia.drafting_interfaces.drawing_table.DrawingTable.invert_mode
    """
    CatInvertColumn = 0
    CatInvertRow = 1
    CatInvertAll = 2


class CatTablePosition(Enum):
    """
    pycatia.drafting_interfaces.drawing_table.DrawingTable.anchor_point
    pycatia.drafting_interfaces.drawing_table.DrawingTable.get_cell_alignment
    pycatia.drafting_interfaces.drawing_table.DrawingTable.set_cell_alignment
    """
    CatTableTopLeft = 0
    CatTableMiddleLeft = 1
    CatTableBottomLeft = 2
    CatTableTopCenter = 3
    CatTableMiddleCenter = 4
    CatTableBottomCenter = 5
    CatTableTopRight = 6
    CatTableMiddleRight = 7
    CatTableBottomRight = 8


class CatTextAnchorPosition(Enum):
    """
    pycatia.drafting_interfaces.drawing_text.DrawingText.anchor_position
    pycatia.drafting_interfaces.drawing_text_properties.DrawingTextProperties.anchor_point
    """
    catUnsusedValue1 = 0
    catTopLeft = 1
    catMiddleLeft = 2
    catBottomLeft = 3
    catTopCenter = 4
    catMiddleCenter = 5
    catBottomCenter = 6
    catTopRight = 7
    catMiddleRight = 8
    catBottomRight = 9
    catUnsusedValue2 = 10
    catCapLeft = 11
    catHalfLeft = 12
    catBaseLeft = 13
    catCapCenter = 14
    catHalfCenter = 15
    catBaseCenter = 16
    catCapRight = 17
    catHalfRight = 18
    catBaseRight = 19


class CatTextFlipMode(Enum):
    """
    pycatia.drafting_interfaces.drawing_text_properties.DrawingTextProperties.mirror
    """
    catTextNoFlip = 0
    catTextHorizontalFlip = 1
    catTextVerticalFlip = 2
    catTextHorizontalAndVerticalFlip = 3
    catTextAutoFlip = 4


class CatTextFrameType(Enum):
    """
    pycatia.drafting_interfaces.drawing_text_properties.DrawingTextProperties.frame_type
    pycatia.drafting_interfaces.drawing_text_properties.DrawingTextProperties.activate_frame
    pycatia.drafting_interfaces.drawing_text.DrawingText.frame_type
    pycatia.drafting_interfaces.drawing_text.DrawingText.activate_frame
    """
    catNone = 0
    catRectangle = 1
    catSquare = 2
    catCircle = 3
    catScoredCircle = 4
    catDiamond = 5
    catTriangle = 6
    catRightFlag = 7
    catLeftFlag = 8
    catBothFlag = 9
    catOblong = 10
    catEllipse = 11
    catCustom = 12


class CatTextProperty(Enum):
    """
    pycatia.drafting_interfaces.drawing_text.DrawingText.get_parameter_on_sub_string
    pycatia.drafting_interfaces.drawing_text.DrawingText.set_parameter_on_sub_string
    """
    catBold = 0
    catItalic = 1
    catUnderline = 2
    catOverline = 3
    catStrikethrough = 4
    catSubscript = 5
    catSuperscript = 6
    catFontSize = 7
    catParagraph = 8
    catPlain = 9
    catColor = 10
    catFontName = 11
    catBorder = 12
    catAlignment = 13
    catCharRatio = 14
    catCharSpacing = 15
    catKerning = 16


class CatThreadLinkedTo(Enum):
    """
    pycatia.drafting_interfaces.drawing_thread.DrawingThread.type
    pycatia.drafting_interfaces.drawing_thread.DrawingThread.is_linked_to
    """
    catNotDefined = 0
    catNoLink = 1
    cat2DPoint = 2
    cat2DCircle = 3
    cat3DGeom = 4
    cat3DHole = 5
    cat3DThread = 6


class CatThreadPolarity(Enum):
    """
    pycatia.part_interfaces.thread.Thread.set_explicit_polarity
    """
    catThread = 0
    catTap = 1


class CatThreadSide(Enum):
    """
    pycatia.part_interfaces.thread.Thread.side
    """
    catRightSide = 0
    catLeftSide = 1


class CatThreadStandard(Enum):
    """
    pycatia.part_interfaces.thread.Thread.create_standard_thread_design_table
    """
    catMetricThinPitch = 0
    catMetricThickPitch = 1


class CatThreadType(Enum):
    """
    pycatia.drafting_interfaces.drawing_thread.DrawingThread.type
    """
    catThreaded = 0
    catTaped = 1


class CatTreeOrientationEnum(Enum):
    """
    pycatia.in_interfaces.tree_viz_manip_setting_att.TreeVizManipSettingAtt.orientation
    """
    catTreeOrientationVertical = 0
    catTreeOrientationHorizontal = 1


class CatTreeSizeTypeEnum(Enum):
    """
    pycatia.in_interfaces.tree_viz_manip_setting_att.TreeVizManipSettingAtt.size_type
    """
    catTreeSizeTypeFixedSize = 0
    catTreeSizeTypeTextDependentSize = 1


class CatTreeTypeEnum(Enum):
    """
    pycatia.in_interfaces.tree_viz_manip_setting_att.TreeVizManipSettingAtt.type
    """
    catTreeTypeClassical = 0
    catTreeTypeStructural = 1
    catTreeTypeHistorical = 2
    catTreeTypeRelational = 3


class CatView2DModeVisu(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_view.Layout2DView.visu_2d_mode
    """
    catView2DModeNotActivated = 0
    catView2DModeNoShow = 1


class CatViewBackgroundMode(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_setting_att.Layout2DSettingAtt.view_background_mode
    """
    catStandard = 0
    catInvisible = 1
    catUnpickable = 2
    catLowIntensity = 3
    catUnpickableLowIntensity = 4


class CatViewFilterCreationMode(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_setting_att.Layout2DSettingAtt.view_filter_creation_mode
    """
    catDefaultFilter = 0
    catDisplayFilterDialogBox = 1
    catDedicatedFilter = 2


class CatViewSide(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_views.Layout2DViews.add_related
    """
    catTopSide = 0
    catBottomSide = 1
    catLeftSide = 2
    catRightSide = 3
    catTLCorner = 4
    catTRCorner = 5
    catBLCorner = 6
    catBRCorner = 7


class CatViewType(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_views.Layout2DViews.add_auxiliary
    pycatia.drafting_2dL_interfaces.layout_2d_views.Layout2DViews.add_from_3d_plane
    """
    catAuxiliaryView = 0
    catSectionView = 1
    catSectionCutView = 2


class CatVisLayerType(Enum):
    """
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_layer
    pycatia.in_interfaces.vis_property_set.VisPropertySet.set_layer
    """
    catVisLayerBasic = 0
    catVisLayerNone = 1


class CatVisPropertyPick(Enum):
    """
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_pick
    pycatia.in_interfaces.vis_property_set.VisPropertySet.set_pick
    """
    catVisPropertyPickAttr = 0
    catVisPropertyNoPickAttr = 1


class CatVisPropertyShow(Enum):
    """
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_show
    pycatia.in_interfaces.vis_property_set.VisPropertySet.set_show
    """
    catVisPropertyShowAttr = 0
    catVisPropertyNoShowAttr = 1


class CatVisPropertyStatus(Enum):
    """
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_layer
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_pick
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_real_color
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_real_inheritance
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_real_line_type
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_real_opacity
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_real_width
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_show
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_symbol_type
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_visible_color
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_visible_inheritance
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_visible_line_type
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_visible_opacity
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_visible_width
    """
    catVisPropertyDefined = 0
    catVisPropertyUnDefined = 1


class CatVisPropertyType(Enum):
    """
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_real_inheritance
    pycatia.in_interfaces.vis_property_set.VisPropertySet.get_visible_inheritance
    """
    catVisPropertyLineType = 0
    catVisPropertyWidth = 1
    catVisPropertyColor = 2
    catVisPropertyOpacity = 3


class CatVisuBackgroundMode(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_view.Layout2DView.visu_background
    """
    catNoBackground = 0
    catPick = 1
    catNoPick = 2
    catLowIntPick = 3
    catLowIntNoPick = 4


class CatVisuIn3DMode(Enum):
    """
    pycatia.drafting_2dL_interfaces.layout_2d_sheet.Layout2DSheet.visu_in_3d
    pycatia.drafting_2dL_interfaces.layout_2d_root.Layout2DRoot.visu_in_3d
    pycatia.drafting_2dL_interfaces.layout_2d_view.Layout2DView.visu_in_3d
    """
    catShowAll = 0
    catHideAll = 1


class CatVisualizationType(Enum):
    """
    pycatia.general_knowledge_interfaces.expert_rule_base_runtime.ExpertRuleBaseRuntime.text_visualization
    """
    Passed = 0
    Failed = 1
    Both = 2


class CatWeldAdditionalSymbol(Enum):
    """
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.get_additional_symbol
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.set_additional_symbol
    """
    catNoneAddWelding = 0
    catFlatWelding = 1
    catConvexWelding = 2
    catConcaveWelding = 3
    catFlushWelding = 4
    catSmoothWelding = 5


class CatWelding(Enum):
    """
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.get_additional_symbol
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.get_finish_symbol
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.get_symbol
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.set_additional_symbol
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.set_finish_symbol
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.set_symbol
    """
    catNoneWelding = 0
    catFirstWelding = 1
    catSecondWelding = 2


class CatWeldingField(Enum):
    """
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.get_finish_symbol
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.get_symbol
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.get_text_range
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.set_finish_symbol
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.set_symbol
    """
    catWeldingNone = 0
    catWeldingFieldOne = 1
    catWeldingFieldTwo = 2
    catWeldingFieldThree = 3
    catWeldingFieldFour = 4
    catWeldingFieldFive = 5
    catWeldingFieldSix = 6
    catWeldingFieldSeven = 7


class CatWeldingSide(Enum):
    """
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.identification_line_side
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.welding_side
    """
    catWeldingUp = 0
    catWeldingDown = 1


class CatWeldingSymbol(Enum):
    """
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.get_symbol
    pycatia.drafting_interfaces.drawing_welding.DrawingWelding.set_symbol
    pycatia.drafting_interfaces.drawing_weldings.DrawingWeldings.add
    """
    catNoneMainWelding = 0
    catSquareWelding = 1
    catVGrooveWelding = 2
    catHVGrooveWelding = 3
    catYGrooveWelding = 4
    catHYGrooveWelding = 5
    catUGrooveWelding = 6
    catHUGrooveWelding = 7
    catFilletWelding = 8
    catCFlangeWelding = 9
    catEFlangeWelding = 10
    catVFlareWelding = 11
    catHVFlareWelding = 12
    catSpotWelding = 13
    catBackWelding = 14
    catHVOGrooveWelding = 15
    catVOGrooveWelding = 16
    catPlugWelding = 17
    catMRWelding = 18
    catMWelding = 19
    catRechargWelding = 20
    catSpotJISWelding = 21
    catEFlangeISOWelding = 22
    catSeamWelding = 23
    catScarfWelding = 24
    catStudWelding = 25
    catEdgeWelding = 26
    catMeltThruWelding = 27
    catSurfaceJointWelding = 28
    catInclinedJointWelding = 29


class CatWindowState(Enum):
    """
    pycatia.in_interfaces.window.Window.window_state
    """
    catWindowStateMaximized = 0
    catWindowStateMinimized = 1
    catWindowStateNormal = 2


class CatWorkModeType(Enum):
    """
    pycatia.product_structure_interfaces.product.Product.apply_work_mode
    """
    DEFAULT_MODE = 0
    VISUALIZATION_MODE = 1
    DESIGN_MODE = 2


class CatftaDimConfigureSnapping(Enum):
    """
    pycatia.cat_tps_interfaces.fta_setting_att.FTASettingAtt.dim_configure_snapping
    """
    CATFTADimSnappingUndefined = 0
    CATFTADimSnappingOnGrid = 1
    CATFTADimSnappingValue = 2
    CATFTADimSnappingBoth = 3


class CatftaDimCreateOn(Enum):
    """
    pycatia.cat_tps_interfaces.fta_setting_att.FTASettingAtt.dim_create_on
    """
    CATFTADimCreateOnUndefined = 0
    CATFTADimCreateOnCenter = 1
    CATFTADimCreateOnEdge = 2


class CatftaLeaderAssociativity(Enum):
    """
    pycatia.cat_tps_interfaces.fta_infra_setting_att.FtaInfraSettingAtt.leader_associativity
    """
    CATFTALeaderAssociativityUndefined = 0
    CATFTALeaderAssociativityFree = 1
    CATFTALeaderAssociativityPerpendicular = 2


class Catv4Iv4V5SpecDraftMigrationEnum(Enum):
    """
    pycatia.catia_v4_interfaces.spec_v4_setting_att.SpecV4SettingAtt.draft_feature_migration_mode
    """
    squareMode = 0
    coneMode = 1


class Catv4Iv5V4AssociativityModeEnum(Enum):
    """
    pycatia.catia_v4_interfaces.v4_writing_setting_att.V4WritingSettingAtt.asso_mode
    """
    AssociativeMode = 0
    NonAssociativeMode = 1
    NonAssociativityModeAndNoSolidCreation = 2


class Catv4Iv5V4ErrorFeatureCreationEnum(Enum):
    """
    pycatia.catia_v4_interfaces.v4_writing_setting_att.V4WritingSettingAtt.mode_error_display
    """
    NeverCreateErrorFeatures = 0
    CreateAnErrorFeatureAfterUserAgreement = 1
    AlwaysCreateErrorFeatures = 2


class Catv4Iv5V4InternalCurveCreationEnum(Enum):
    """
    pycatia.catia_v4_interfaces.v4_writing_setting_att.V4WritingSettingAtt.mode_create_display
    """
    AllCurvesAreCreated = 0
    OnlyConicsAreCreated = 1
    NoInternalCurveIsCreated = 2


class Cd5SaveItem_Status(Enum):
    """
    pycatia.eno_cd5_interfaces.cd5_save_item.CD5SaveItem.status

    """
    CD5SaveItem_New = 0
    CD5SaveItem_Modified = 1
    CD5SaveItem_Exists = 2
    CD5SaveItem_ECNameNotUnique = 3
    CD5SaveItem_ModifiedNotLockedByYou = 4
    CD5SaveItem_Obsolete = 5
    CD5SaveItem_UUIDConflict = 6
    CD5SaveItem_NotFound = 7


class Cd5SaveOperation_Scope(Enum):
    """
    pycatia.eno_cd5_interfaces.cd5_engine_v6_r2014x.CD5EngineV6R2014x.create_save_operation
    """
    CD5SaveOperation_ActiveDocument = 0
    CD5SaveOperation_CurrentEditor = 1
    CD5SaveOperation_Session = 2


class ContactStiffness_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_mech_conn_behavior.ABQMechConnBehavior.contact_stiffness
    """
    DEFAULT = 0
    STIFF_VALUE = 1


class DistributionType(Enum):
    """
    pycatia.abq_automation_interfaces.abq_temperature.ABQTemperature.distribution
    pycatia.abq_automation_interfaces.abq_temperature.ABQTemperature.distribution
    """
    UNIFORM = 0
    JOB = 1
    USERDEFINED = 2
    JOB_USERDEFINED = 3


class DmuTrackMoveMode(Enum):
    """
    pycatia.fitting_interfaces.track.Track.move_mode
    """
    DMUTrackSpeedMode = 0
    DMUTrackTimeMode = 1


class DnbActBehaviorType(Enum):
    """
    ?
    """
    DNBBehaviorProcess = 0
    DNBBehaviorParent = 1


class DnbAnalysisLevel(Enum):
    """
    ?
    """
    DNBAnalysisLevelOff = 0
    DNBAnalysisLevelHighlight = 1
    DNBAnalysisLevelVerbose = 2
    DNBAnalysisLevelInterrupt = 3


class DnbAssignStatus(Enum):
    """
    pycatia.dnb_fastener_interfaces.dnb_fastener_item_services.DnbFastenerItemServices.assign_fastener_to_process
    pycatia.dnb_fastener_interfaces.dnb_fastener_item_services.DnbFastenerItemServices.assign_fastener_to_resource
    """
    DNBUnknownState = 0
    DNBSuccess = 1
    DNBAlreadyAssigned = 2
    DNBInvalidObjetAssignment = 3
    DNBInvalidProcessVersion = 4
    DNBPartsNotLoaded = 5


class DnbAuxilliaryDeviceType(Enum):
    """
    pycatia.dnb_robot_interfaces.aux_devices_mgt.AuxDevicesMgt.define_aux_devices
    pycatia.dnb_robot_interfaces.aux_devices_mgt.AuxDevicesMgt.get_aux_devices_type
    """
    AuxilliaryDeviceType_RailTrackGantry = 0
    AuxilliaryDeviceType_EndOfArmTooling = 1
    AuxilliaryDeviceType_WorkpiecePositioner = 2
    AuxilliaryDeviceType_Conveyor = 3


class DnbHlnkBehaviorType(Enum):
    """
    ?
    """
    DNBBehaviorContinue = 0
    DNBBehaviorPause = 1


class DnbSimGraphUpdateMode(Enum):
    """
    ?
    """
    DNBSimGraphUpdateDisabled = 0
    DNBSimGraphUpdateEnabled = 1


class DnbSimInitStateAttr(Enum):
    """
    pycatia.dnb_simulation_interfaces.simulation_init_state.SimulationInitState.restore_initial_state
    pycatia.dnb_simulation_interfaces.simulation_init_state.SimulationInitState.restore_initial_state_list
    pycatia.dnb_simulation_interfaces.simulation_init_state.SimulationInitState.save_initial_state
    pycatia.dnb_simulation_interfaces.simulation_init_state.SimulationInitState.save_initial_state_list
    """
    DNBVisInitStateAttr = 0
    DNBPosInitStateAttr = 1
    DNBColInitStateAttr = 2
    DNBOpacInitStateAttr = 3
    DNBVisPosInitStateAttr = 4
    DNBVisColInitStateAttr = 5
    DNBVisOpacInitStateAttr = 6
    DNBVisPosColInitStateAttr = 7
    DNBVisPosOpacInitStateAttr = 8
    DNBVisColOpacInitStateAttr = 9
    DNBPosColInitStateAttr = 10
    DNBPosOpacInitStateAttr = 11
    DNBPosColOpacInitStateAttr = 12
    DNBColOpacInitStateAttr = 13
    DNBAllInitStateAttr = 14


class DnbSimNavigationMode(Enum):
    """
    ?
    """
    DNBSimNavigationModeStep = 0
    DNBSimNavigationModeAnimate = 1


class DnbVisualizationMode(Enum):
    """
    ?
    """
    DNBVisualizationModeHighlight = 0
    DNBVisualizationModeCurves = 1


class DNBIAMfgAssemblyType(Enum):
    """
    pycatia.dnb_dpm_interfaces.mfg_assembly.MfgAssembly.ma_type
    pycatia.dnb_dpm_interfaces.mfg_assembly_factory.MfgAssemblyFactory.create_mfg_assembly
    pycatia.dnb_dpm_interfaces.mfg_assembly_factory.MfgAssemblyFactory.get_number_of_all_mfg_assy
    pycatia.dnb_dpm_interfaces.mfg_assembly_factory.MfgAssemblyFactory.retrive_all_mfg_assy
    """
    manufacturingAssembly = 0
    manufacturingKit = 1
    assemblySpecTree = 2
    manufacturingOutput = 3
    notSpecified = 4


class DNBPPRRemoveStatus(Enum):
    """
    pycatia.dnb_fastener_interfaces.fastener.Fastener.remove_from_ppr
    """
    DNBFastenerUnknownStatus = 0
    DNBFastenerAssignedStatus = 1
    DNBFastenerSuccessStatus = 2


class DNBTCPTraceLegends(Enum):
    """
    pycatia.dnb_robot_interfaces.tcp_trace.TCPTrace.get_legends_visibility
    pycatia.dnb_robot_interfaces.tcp_trace.TCPTrace.set_legends_visibility
    """
    DNBTCPTraceLegendAllLegend = 0
    DNBTCPTraceLegendName = 1
    DNBTCPTraceLegendX = 2
    DNBTCPTraceLegendY = 3
    DNBTCPTraceLegendZ = 4
    DNBTCPTraceLegendYaw = 5
    DNBTCPTraceLegendPitch = 6
    DNBTCPTraceLegendRoll = 7
    DNBTCPTraceLegendCycleTime = 8
    DNBTCPTraceLegendHighlight = 9
    DNBTCPTraceLegendAlwaysVisible = 10


class DNBTCPTraceReps(Enum):
    """
    pycatia.dnb_robot_interfaces.tcp_trace.TCPTrace.get_colour
    pycatia.dnb_robot_interfaces.tcp_trace.TCPTrace.get_legends_visibility
    pycatia.dnb_robot_interfaces.tcp_trace.TCPTrace.get_thickness
    pycatia.dnb_robot_interfaces.tcp_trace.TCPTrace.get_type
    pycatia.dnb_robot_interfaces.tcp_trace.TCPTrace.get_visibility
    pycatia.dnb_robot_interfaces.tcp_trace.TCPTrace.set_color
    pycatia.dnb_robot_interfaces.tcp_trace.TCPTrace.set_legends_visibility
    pycatia.dnb_robot_interfaces.tcp_trace.TCPTrace.set_thickness
    pycatia.dnb_robot_interfaces.tcp_trace.TCPTrace.set_type
    pycatia.dnb_robot_interfaces.tcp_trace.TCPTrace.set_visibility
    pycatia.dnb_robot_interfaces.tcp_trace_manager_graphics.TCPTraceManagerGraphics.set_next_thickness
    pycatia.dnb_robot_interfaces.tcp_trace_manager_graphics.TCPTraceManagerGraphics.set_next_type
    pycatia.dnb_robot_interfaces.tcp_trace_manager_graphics.TCPTraceManagerGraphics.set_trace_next_colour
    """
    DNBTCPTraceRepAllRep = 0
    DNBTCPTraceRepPoint = 1
    DNBTCPTraceRepLine = 2
    DNBTCPTraceRepAxis = 3


class ElemBehavEnum(Enum):
    """
    pycatia.abq_automation_interfaces.abq_global_element_assignment.ABQGlobalElementAssignment.get_element_properties
    pycatia.abq_automation_interfaces.abq_global_element_assignment.ABQGlobalElementAssignment.set_element_properties
    """
    BEHAVIOR_NONE = 0
    SHELL = 1
    MEMBRANE = 2
    SOLID3D = 3
    CONTINUUM_SHELL = 4
    BEAM = 5
    GASKET = 6


class ElemIdEnum(Enum):
    """
    pycatia.abq_automation_interfaces.abq_global_element_assignment.ABQGlobalElementAssignment.get_element_properties
    pycatia.abq_automation_interfaces.abq_global_element_assignment.ABQGlobalElementAssignment.set_element_properties
    """
    TET_LINEAR = 0
    TET_PARABOLIC = 1
    HEX_LINEAR = 2
    HEX_PARABOLIC = 3
    WEDG_LINEAR = 4
    WEDG_PARABOLIC = 5
    TRI_LINEAR = 6
    TRI_PARABOLIC = 7
    QUAD_LINEAR = 8
    QUAD_PARABOLIC = 9
    LINE_LINEAR = 10
    LINE_PARABOLIC = 11


class FixedTimeIncrementMethod(Enum):
    """
    pycatia.abq_automation_interfaces.abq_explicit_dynamics_step.ABQExplicitDynamicsStep.fixed_time_increment_method
    pycatia.abq_automation_interfaces.abq_explicit_dynamics_step.ABQExplicitDynamicsStep.user_defined_time_increment_value
    """
    ABQ_FTI_ELEMENT_BY_ELEMENT = 0
    ABQ_FTI_USER_DEFINED = 1


class FormulationOption_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_surface_to_surface_contact.ABQSurfaceToSurfaceContact.formulation_option
    pycatia.abq_automation_interfaces.abq_fastened_connection_enhancement.ABQFastenedConnectionEnhancement.formulation_option
    pycatia.abq_automation_interfaces.abq_fastened_pair.ABQFastenedPair.formulation_option
    """
    SOLVERDEFAULT = 0
    SURFACETOSURFACE = 1
    NODETOSURFACE = 2


class Formulation_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_mech_conn_behavior.ABQMechConnBehavior.formulation
    """
    FRICTIONLESS = 0
    PENALTY = 1


class FrameVisibility(Enum):
    """
    ?
    dnb_d5_interfaces.?
    """
    VisNo = 0
    VisYes = 1
    VisRetain = 2


class GeometricalFeatureType(Enum):
    """
    pycatia.hybrid_shape_interfaces.hybrid_shape_factory.HybridShapeFactory.get_geometrical_feature_type
    """
    Unknown = 0
    Point = 1
    Curve = 2
    Line = 3
    Circle = 4
    Surface = 5
    Plane = 6
    Solid_Volume = 7


class HTSActivityGroupMotionBasis(Enum):
    """
    pycatia.dnb_human_sim_interfaces.human_activity_group.HumanActivityGroup.motion_basis
    """
    HAGMOTBASIS_DEFAULT = 0
    HAGMOTBASIS_USERSPEED = 1
    HAGMOTBASIS_USERTIME = 2


class HTSBodyPoseOptions(Enum):
    """
    pycatia.dnb_human_sim_interfaces.walk_activity.WalkActivity.body_pose
    """
    BODYPOSE_CURRENT = 0
    BODYPOSE_RESET = 1


class HTSEndEffector(Enum):
    """
    pycatia.dnb_human_sim_interfaces.move_to_posture_activity.MoveToPostureActivity.get_part_relation
    pycatia.dnb_human_sim_interfaces.move_to_posture_activity.MoveToPostureActivity.set_part_relation
    pycatia.dnb_human_sim_interfaces.move_to_posture_activity.MoveToPostureActivity.set_part_relation_with_offset
    """
    EE_LEFTHAND = 0
    EE_RIGHTHAND = 1
    EE_LEFTLEG = 2
    EE_RIGHTLEG = 3
    EE_LINEOFSIGHT = 4
    EE_BODY = 5
    EE_NECK = 6


class HTSHand(Enum):
    """
    pycatia.dnb_human_sim_interfaces.pick_activity.PickActivity.picking_hand
    pycatia.dnb_human_sim_interfaces.human_activity_group_factory.HumanActivityGroupFactory.create_pick
    pycatia.dnb_human_sim_interfaces.human_acts_factory.HumanActsFactory.create_pick
    """
    HAND_RIGHT = 0
    HAND_LEFT = 1


class HTSManikinReferential(Enum):
    """
    pycatia.dnb_human_sim_interfaces.move_to_posture_activity.MoveToPostureActivity.referential
    """
    REF_EYEPOINT = 0
    REF_HPOINT = 1
    REF_LEFTFOOT = 2
    REF_RIGHTFOOT = 3
    REF_LOWESTFOOT = 4
    REF_CROTCH = 5
    REF_LEFTHAND = 6
    REF_RIGHTHAND = 7
    REF_BETWEENFEET = 8
    REF_HPOINTPROJECTION = 9


class HTSMotionBasis(Enum):
    """
    pycatia.dnb_human_sim_interfaces.move_to_posture_activity.MoveToPostureActivity.motion_basis
    """
    MOTBASIS_SPEED = 0
    MOTBASIS_TIME = 1


class HTSPickType(Enum):
    """
    pycatia.dnb_human_sim_interfaces.pick_activity.PickActivity.pick_type
    pycatia.dnb_human_sim_interfaces.human_activity_group_factory.HumanActivityGroupFactory.create_pick
    pycatia.dnb_human_sim_interfaces.human_acts_factory.HumanActsFactory.create_pick
    """
    SINGLE_HAND = 0
    BOTH_HANDS = 1


class HTSSearchIntensity(Enum):
    """
    pycatia.dnb_human_sim_interfaces.collision_free_walk.CollisionFreeWalk.search_intensity
    pycatia.dnb_human_sim_interfaces.human_activity_group_factory.HumanActivityGroupFactory.create_collision_free_walk_bwd_on_arr_area
    pycatia.dnb_human_sim_interfaces.human_activity_group_factory.HumanActivityGroupFactory.create_collision_free_walk_bwd_on_plane
    pycatia.dnb_human_sim_interfaces.human_activity_group_factory.HumanActivityGroupFactory.create_collision_free_walk_fwd_on_arr_area
    pycatia.dnb_human_sim_interfaces.human_activity_group_factory.HumanActivityGroupFactory.create_collision_free_walk_fwd_on_plane
    pycatia.dnb_human_sim_interfaces.human_acts_factory.HumanActsFactory.create_collision_free_walk_bwd_on_arr_area
    pycatia.dnb_human_sim_interfaces.human_acts_factory.HumanActsFactory.create_collision_free_walk_bwd_on_plane
    pycatia.dnb_human_sim_interfaces.human_acts_factory.HumanActsFactory.create_collision_free_walk_fwd_on_arr_area
    pycatia.dnb_human_sim_interfaces.human_acts_factory.HumanActsFactory.create_collision_free_walk_fwd_on_plane
    """
    FINESEARCH = 0
    NORMALSEARCH = 1
    COARSESEARCH = 2


class HTSStrideOptions(Enum):
    """
    pycatia.dnb_human_sim_interfaces.walk_activity.WalkActivity.stride
    """
    STRIDE_SHORT = 0
    STRIDE_MEDIUM = 1
    STRIDE_LONG = 2


class HTSSwingOptions(Enum):
    """
    pycatia.dnb_human_sim_interfaces.walk_activity.WalkActivity.swing
    """
    SWING_BOTHARMS = 0
    SWING_LEFTARM = 1
    SWING_RIGHTARM = 2
    SWING_CURRENT = 3


class HTSWalkMotionBasis(Enum):
    """
    pycatia.dnb_human_sim_interfaces.walk_activity.WalkActivity.motion_basis
    """
    WALKMOTBASIS_DEFAULT = 0
    WALKMOTBASIS_USERSPEED = 1
    WALKMOTBASIS_USERTIME = 2


class Incrementation_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_general_static_step.ABQGeneralStaticStep.time_incrementation_method
    pycatia.abq_automation_interfaces.abq_explicit_dynamics_step.ABQExplicitDynamicsStep.time_incrementation_method
    pycatia.abq_automation_interfaces.abq_heat_transfer_step.ABQHeatTransferStep.time_incrementation_method
    """
    AUTO_INCREMENT = 0
    FIXED_INCREMENT = 1


class InitialThickness_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_gasket_property.ABQGasketProperty.initial_thickness_type
    """
    USE_NODAL_COORDINATES = 0
    INITIAL_THICKNESS_SPECIFY = 1


class ItemAssignmentType(Enum):
    """
    pycatia.dnb_work_interfaces.wi_text_access_ei.WITextAccessEi.get_geom_referred_by_annotation
    pycatia.dmaps_interfaces.items.Items.add_by_assignment_type
    pycatia.dmaps_interfaces.items.Items.count_by_assignment_type
    pycatia.dmaps_interfaces.items.Items.item_by_assignment_type
    pycatia.dmaps_interfaces.items.Items.remove_by_assignment_type
    pycatia.dnb_ekp_interfaces.ekp_services.EkpServices.assign_er
    pycatia.dnb_ekp_interfaces.ekp_services.EkpServices.assign_er_with_fta
    pycatia.dnb_ekp_interfaces.ekp_services.EkpServices.get_assigned_er
    pycatia.dnb_ekp_interfaces.ekp_services.EkpServices.remove_er_assignment
    pycatia.dnb_ekp_interfaces.ekp_services.EkpServices.remove_er_with_fta
    pycatia.dnb_work_interfaces.wi_text.WIText.get_geom_associated_to_annotation
    """
    ProcessProcesses = 0
    ProcessFirstProcesses = 1
    ProcessRemoves = 2
    ProcessImplementsRequirementPartial = 3
    ProcessImplementsRequirementComplete = 4
    productviewpoint = 5
    productvisualization = 6


class Job_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_job.ABQJob.type
    
    """
    ANALYSIS = 0
    DATACHECK = 1
    CONTINUE = 2
    FROMINPUTFILE = 3
    SYNTAXCHECK = 4
    RESTART = 5


class MaxStiffness_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_mech_conn_behavior.ABQMechConnBehavior.max_stiffness
    """
    MAX_STIFF_DEFAULT = 0
    MAX_STIFF_VALUE = 1


class MemoryUnit_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_job.ABQJob.memory_unit
    """
    MEGABYTES = 0
    PERCENT = 1


class MotionBasis(Enum):
    """
    pycatia.dnb_robot_interfaces.generic_motion_profile.GenericMotionProfile.get_motion_basis
    pycatia.dnb_robot_interfaces.generic_motion_profile.GenericMotionProfile.set_motion_basis
    pycatia.dnb_device_activity_interfaces.move_home_act.MoveHomeAct.motion_basis
    pycatia.dnb_device_activity_interfaces.move_joints_act.MoveJointsAct.motion_basis
    pycatia.dnb_human_sim_interfaces.human_activity_group.HumanActivityGroup.motion_basis
    pycatia.dnb_human_sim_interfaces.move_to_posture_activity.MoveToPostureActivity.motion_basis
    pycatia.dnb_human_sim_interfaces.walk_activity.WalkActivity.motion_basis
    """
    MOTION_ABSOLUTE = 0
    MOTION_PERCENT = 1
    MOTION_TIME = 2


class ParallelMethodStdType(Enum):
    """
    pycatia.abq_automation_interfaces.abq_job.ABQJob.parallelization_method_standard
    """
    TREE = 0
    SUPERNODE = 1


class PositionToleranceType(Enum):
    """
    pycatia.abq_automation_interfaces.abq_fastened_pair.ABQFastenedPair.position_tolerance
    pycatia.abq_automation_interfaces.abq_fastened_connection_enhancement.ABQFastenedConnectionEnhancement.position_tolerance
    """
    COMPUTED = 0
    SPECIFIED = 1


class PressureOverclosure_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_mech_conn_behavior.ABQMechConnBehavior.pressure_overclosure
    """
    HARD = 0
    EXPONENTIAL = 1
    LINEAR = 2
    TABULAR = 3


class RasterLevelOfDetail(Enum):
    """
    ?
    Precision for views generated as raster (DPI).
    """
    LowQuality = 0
    NormalQuality = 1
    HighQuality = 2
    Customize = 3


class ResponseType(Enum):
    """
    pycatia.abq_automation_interfaces.abq_heat_transfer_step.ABQHeatTransferStep.response
    """
    STEADY_STATE = 0
    TRANSIENT = 1


class Sliding_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_surface_to_surface_contact.ABQSurfaceToSurfaceContact.sliding
    """
    FINITE = 0
    SMALL = 1


class SPMDistributionMode(Enum):
    """
    pycatia.analysis_interfaces.analysis_color_map.AnalysisColorMap.distribution_mode
    """
    SPM_LINEAR = 0
    SPM_HISTOGRAM = 1
    SPM_LOG = 2


class SpringDef_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_spring_connection_property.ABQSpringConnectionProperty.spring_definition
    pycatia.abq_automation_interfaces.abq_damper_connection_property.ABQDamperConnectionProperty.damper_def
    """
    ABQ_LINE = 0
    ABQ_NON_LINEAR = 1


class SpringDof_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_spring_connection_property.ABQSpringConnectionProperty.get_linear_stiffness
    pycatia.abq_automation_interfaces.abq_spring_connection_property.ABQSpringConnectionProperty.get_non_linear_stiffness
    pycatia.abq_automation_interfaces.abq_spring_connection_property.ABQSpringConnectionProperty.read_stiffness_data_from_file
    pycatia.abq_automation_interfaces.abq_spring_connection_property.ABQSpringConnectionProperty.remove_dof
    pycatia.abq_automation_interfaces.abq_spring_connection_property.ABQSpringConnectionProperty.set_linear_stiffness
    pycatia.abq_automation_interfaces.abq_spring_connection_property.ABQSpringConnectionProperty.set_non_linear_stiffness
    pycatia.abq_automation_interfaces.abq_damper_connection_property.ABQDamperConnectionProperty.get_linear_damping
    pycatia.abq_automation_interfaces.abq_damper_connection_property.ABQDamperConnectionProperty.get_non_linear_damping
    pycatia.abq_automation_interfaces.abq_damper_connection_property.ABQDamperConnectionProperty.read_damping_data_from_file
    pycatia.abq_automation_interfaces.abq_damper_connection_property.ABQDamperConnectionProperty.remove_dof
    pycatia.abq_automation_interfaces.abq_damper_connection_property.ABQDamperConnectionProperty.set_linear_damping
    pycatia.abq_automation_interfaces.abq_damper_connection_property.ABQDamperConnectionProperty.set_non_linear_damping
    """
    U1_DOF = 0
    U2_DOF = 1
    U3_DOF = 2
    UR1_DOF = 3
    UR2_DOF = 4
    UR3_DOF = 5


class SpringTypeType(Enum):
    """
    pycatia.abq_automation_interfaces.abq_spring_connection_property.ABQSpringConnectionProperty.spring_type
    """
    AXIAL = 0
    GENERAL = 1


class StabilizationStiffness_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_gasket_property.ABQGasketProperty.stabilization_stiffness_type
    """
    STABILIZATION_DEFAULT = 0
    STABILIZATION_SPECIFY = 1


class Stabilization_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_general_static_step.ABQGeneralStaticStep.stabilization_method
    """
    NONE = 0
    DISSIPATION = 1
    FACTOR = 2


class SWKAnthroSex(Enum):
    """
    pycatia.dnb_human_modeling_interfaces.swk_hmi_workbench.SWKHmiWorkbench.create_left_forearm
    pycatia.dnb_human_modeling_interfaces.swk_hmi_workbench.SWKHmiWorkbench.create_manikin
    pycatia.dnb_human_modeling_interfaces.swk_hmi_workbench.SWKHmiWorkbench.create_right_forearm
    """
    Male = 0
    Female = 1


class SWKPostureSpec(Enum):
    """
    pycatia.dnb_human_modeling_interfaces.swk_body.SWKBody.set_posture
    """
    SWKPostureSpecDefault = 0
    SWKPostureSpecStand = 1
    SWKPostureSpecSit = 2
    SWKPostureSpecReach = 3
    SWKPostureSpecExtendedReach = 4
    SWKPostureSpecSpan = 5
    SWKPostureSpecKneel = 6
    SWKPostureSpecInitial = 7


class TimeSpan_Type(Enum):
    """
    pycatia.abq_automation_interfaces.abq_smooth_step_amplitude.ABQSmoothStepAmplitude.time_span
    pycatia.abq_automation_interfaces.abq_tabular_amplitude.ABQTabularAmplitude.time_span
    """
    STEP_TIME = 0
    TOTAL_TIME = 1
