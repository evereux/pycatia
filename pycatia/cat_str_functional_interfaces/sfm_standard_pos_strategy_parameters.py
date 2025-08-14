#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_references import SFMReferences
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.cat_base_unknown import CATBaseUnknown
from pycatia.types.general import cat_variant


class SFMStandardPosStrategyParameters(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfmStandardPosStrategyParameters
                | 
                | Sets the Required data for Positioning the Contour.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_standard_pos_strategy_parameters = com_object

    @property
    def count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Count() As long (Read Only)
                | 
                |     Returns the count of reference elements.
                | 
                |     Example
                |     :
                |         This example retrieves gets the count of the
                |         References
                | 
                |          Cnt = VrefList.Count

        :rtype: int
        """

        return self.sfm_standard_pos_strategy_parameters.Count

    def item(self, i_index: cat_variant) -> CATBaseUnknown:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As CATBaseUnknown

        :param cat_variant i_index:
        :rtype: CATBaseUnknown
        """
        return self.sfm_standard_pos_strategy_parameters.Item(i_index)

    def set_pos_param_data(
            self,
            i_pos_strategy_name: str,
            i_rotation_angle: float,
            i_uref_elem: SFMReferences,
            i_u_offset: float,
            i_v_ref_elem: SFMReferences,
            i_v_offset: float
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPosParamData(CATBSTR iPosStrategyName,
                | double iRotationAngle,
                | SfmReferences iUrefElem,
                | double iUOffset,
                | SfmReferences iVRefElem,
                | double iVOffset)
                | 
                |     Sets the Position Parameter Data for different Strategies.Different
                |     Strategies require different inputs.
                | 
                |     Parameters:
                | 
                |         iPosStrategyName
                |             [in] Legal Values:
                |             CATSfmPosOffsetOffset,CATSfmPosHalfHeightOffset,CATSfmPosMidDistOffset,CATSfmPosMidDistMidDist,CATSfmPosHalfHeightMidDist
                |             
                |         iRotationAngle
                |             [in] Enter Rotaion angle for Contour 
                |         iUrefElem
                |             [in] List of U reference Elements CATSfmPosOffsetOffset: This
                |             Strategy can take Multiple U References CATSfmPosHalfHeightOffset: This
                |             Strategy can take Multiple U References CATSfmPosMidDistOffset: This Strategy
                |             can take Multiple U References CATSfmPosMidDistMidDist: This strategy can take
                |             Multiple U References CATSfmPosHalfHeightMidDist: This strategy can take
                |             Multiple U References 
                |         iUOffset
                |             [in] Enter U Offset value 
                |         iVrefElem
                |             [in] List of V reference Elements CATSfmPosOffsetOffset: This
                |             Strategy can take only one V Reference CATSfmPosHalfHeightOffset: This Strategy
                |             does not take any V Reference CATSfmPosMidDistOffset: This Strategy can take
                |             only one V Reference CATSfmPosMidDistMidDist: This strategy can take only two V
                |             References CATSfmPosHalfHeightMidDist: This Strategy does not take any V
                |             Reference 
                |         iVOffset
                |             [in] Enter V Offset value 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example sets the data required for Positioning the Contour for
                |             CATSfmPosMidDistMidDist in details.
                | 
                |              'For MidDistance-MidDistance Strategy
                |              'Populate List for U references with 4 Reference
                |              elements
                |              Dim UrefList As SfmReferences
                |              Dim Uref1,Uref2,Uref3,Uref4 As Reference
                |              Set Uref1 = Part1.FindObjectByName("CROSS.95")
                |              Set Uref2 = Part1.FindObjectByName("CROSS.50")
                |              Set Uref3 = Part1.FindObjectByName("CROSS.25")
                |              Set Uref4 = Part1.FindObjectByName("CROSS.40")
                |              Set UrefList = Factory.SfmReferences
                |              UrefList.Add Uref1
                |              UrefList.Add Uref2
                |              UrefList.Add Uref3
                |              UrefList.Add Uref4
                |              'Populate List for V references with 2 Reference
                |              elements
                |              Dim VrefList As SfmReferences
                |              Dim Vref1,Vref2 As Reference
                |              Set Vref1 = Part1.FindObjectByName("LONG.0")
                |              Set Vref2 = Part1.FindObjectByName("LONG.10")
                |              Set VrefList = Factory.SfmReferences
                |              VrefList.Add Vref1
                |              VrefList.Add Vref2
                |              'Set the SfmStandardPosStrategyParameters
                |              Dim PositionStrategyParms As
                |              SfmStandardPosStrategyParameters
                |              Set PositionStrategyParms = ObjSfmPosStrategyMgr.GetPositioningStrategyParams("CATSfmPosMidDistMidDist")
                |              'Get the Count of U References
                |              Dim NbofURef As Long
                |              NbofURef = UrefList.Count
                |              'The Following list will will pass only first two U references.
                |              The next two references will be passed after clearing the
                |              list
                |              Dim URefListinternal As SfmReferences
                |              Set URefListinternal = Factory.SfmReferences
                |              Dim StdOpening As SfmStandardOpening
                |              ' For loop
                |              For nUrefCnt = 1 To NbofURef Step 2
                |                If (nUrefCnt + 1) <= NbofURef Then
                |                 URefListinternal.Add UrefList.Item(nUrefCnt)
                |                 URefListinternal.Add UrefList.Item(nUrefCnt +
                |                 1)
                |                 PositionStrategyParms.SetPosParamData
                |                 "CATSfmPosMidDistMidDist", 20, URefListinternal, 0, VrefList,
                |                 0
                |                 Set StdOpening = Factory.CreateStandardOpening("FunctionalOpening",
                |                                                                "Sfm_Rect",
                |                                                                oListCkeParms,
                |                                                                "CATSfmPosMidDistMidDist",
                |                                                                PositionStrategyParms,
                |                                                                plateref)
                |                 URefListinternal.ClearList
                |                End If
                |              Next
                |              Part1.Update
                |              ' Example for CATSfmPosOffsetOffset Strategy: VRefList Contains
                |              only one Reference element
                |              Dim PositionStrategyParms As
                |              SfmStandardPosStrategyParameters
                |              Set PositionStrategyParms = ObjSfmPosStrategyMgr.GetPositioningStrategyParams("CATSfmPosOffsetOffset")
                |              Dim StdOpening As SfmStandardOpening
                |              Dim URefListinternal As SfmReferences
                |              Set URefListinternal = Factory.SfmReferences
                |              For nUrefCnt = 1 To NbofURef
                |                  URefListinternal.Add UrefList.Item(nUrefCnt)
                |                  PositionStrategyParms.SetPosParamData "CATSfmPosOffsetOffset",
                |                  20, URefListinternal, 1, VrefList, 2
                |                  Set StdOpening = Factory.CreateStandardOpening("FunctionalOpening",
                |                                                                 "Sfm_Rect",
                |                                                                 oListCkeParms,
                |                                                                 "CATSfmPosOffsetOffset",
                |                                                                 PositionStrategyParms,
                |                                                                 plateref)
                |                  URefListinternal.ClearList
                |                  Part1.Update
                |               Next
                |               ' Example for CATSfmPosMidDistOffset Strategy: Uref elements are
                |               passed in group of two.VRefList Contains only one Reference element.
                |               
                |               For nUrefCnt = 1 To NbofURef Step 2
                |                  If (nUrefCnt + 1) <= NbofURef Then
                |                  URefListinternal.Add UrefList.Item(nUrefCnt)
                |                  URefListinternal.Add UrefList.Item(nUrefCnt +
                |                  1)
                |                  PositionStrategyParms.SetPosParamData
                |                  "CATSfmPosMidDistOffset", 20, URefListinternal, 0, VrefList,
                |                  22
                |                  Set StdOpening = Factory.CreateStandardOpening("FunctionalOpening",
                |                                                                 "Sfm_Rect",
                |                                                                 oListCkeParms,
                |                                                                 "CATSfmPosMidDistOffset",
                |                                                                 PositionStrategyParms,
                |                                                                 plateref)
                |                  URefListinternal.ClearList
                |                  End If
                |               Next
                |               ' Example for CATSfmPosHalfHeightOffset
                |               Strategy:
                |              For nUrefCnt = 1 To NbofURef
                |                  URefListinternal.Add UrefList.Item(nUrefCnt)
                |                  PositionStrategyParms.SetPosParamData
                |                  "CATSfmPosHalfHeightOffset", 20, URefListinternal, 0, VrefList,
                |                  0
                |                  Set StdOpening = Factory.CreateStandardOpening("FunctionalOpening",
                |                                                                 "Sfm_Rect",
                |                                                                 oListCkeParms,
                |                                                                 "CATSfmPosHalfHeightOffset",
                |                                                                 PositionStrategyParms,
                |                                                                 plateref)
                |                  URefListinternal.ClearList
                |                  Part1.Update
                |              Next
                |               ' Example for CATSfmPosHalfHeightMidDist Strategy:U Ref Elements
                |               are passed in Group of two.
                |              For nUrefCnt = 1 To NbofURef Step 2
                |                If (nUrefCnt + 1) <= NbofURef Then
                |                  URefListinternal.Add UrefList.Item(nUrefCnt)
                |                  URefListinternal.Add UrefList.Item(nUrefCnt +
                |                  1)
                |                  PositionStrategyParms.SetPosParamData
                |                  "CATSfmPosHalfHeightMidDist", 20, URefListinternal, 1, VrefList,
                |                  2
                |                  Set StdOpening = Factory.CreateStandardOpening("FunctionalOpening",
                |                                                                 "Sfm_Rect",
                |                                                                  oListCkeParms,
                |                                                                 "CATSfmPosHalfHeightMidDist",
                |                                                                 PositionStrategyParms,
                |                                                                 plateref)
                |                  URefListinternal.ClearList
                |                End If
                |              Next

        :param str i_pos_strategy_name:
        :param float i_rotation_angle:
        :param SFMReferences i_uref_elem:
        :param float i_u_offset:
        :param SFMReferences i_v_ref_elem:
        :param float i_v_offset:
        :rtype: None
        """
        return self.sfm_standard_pos_strategy_parameters.SetPosParamData(
            i_pos_strategy_name,
            i_rotation_angle,
            i_uref_elem.com_object,
            i_u_offset,
            i_v_ref_elem.com_object,
            i_v_offset
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pos_param_data'
        # # vba_code = """
        # # Public Function set_pos_param_data(sfm_standard_pos_strategy_parameters)
        # #     Dim iPosStrategyName (2)
        # #     sfm_standard_pos_strategy_parameters.SetPosParamData iPosStrategyName
        # #     set_pos_param_data = iPosStrategyName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SFMStandardPosStrategyParameters(name="{self.name}")'
