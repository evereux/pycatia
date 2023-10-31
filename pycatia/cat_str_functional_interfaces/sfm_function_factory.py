#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_opening import SFMOpening
from pycatia.cat_str_functional_interfaces.sfm_references import SFMReferences
from pycatia.cat_str_functional_interfaces.sfm_standard_contour_parameters import SFMStandardContourParameters
from pycatia.cat_str_functional_interfaces.sfm_standard_opening import SFMStandardOpening
from pycatia.cat_str_functional_interfaces.sfm_standard_pos_strategy_parameters import SFMStandardPosStrategyParameters
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.factory import Factory
from pycatia.mec_mod_interfaces.part import Part
from pycatia.system_interfaces.any_object import AnyObject


class SFMFunctionFactory(Factory):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Factory
                |                         SfmFunctionFactory
                | 
                | Gets the Function Factory.
                | 
                | Example:
                |     This Example Retrieves SfmFunctionFactory from Part.
                | 
                |      Set part1 = partDocument1.Part
                |      Dim Factory As SfmFunctionFactory
                |      Set Factory =  part1.GetCustomerFactory("SfmFunctionFactory")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_function_factory = com_object

    @property
    def sfm_references(self) -> SFMReferences:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SfmReferences() As SfmReferences (Read Only)
                | 
                |     Gets the list of Sfm References. Use it to prepare a list of U & V
                |     References for Standard Opening.
                | 
                |     Example:
                |         This example populates a list for U References. Use the Add Method to
                |         add a reference to the list.
                | 
                |          Dim Factory As SfmFunctionFactory
                |          Set Factory = Part1.GetCustomerFactory("SfmFunctionFactory") 
                |          Dim Uref1 As Reference
                |          Set Uref1 = Part1.FindObjectByName("CROSS.95")
                |          Dim UrefList As SfmReferences
                |          Set UrefList = Factory.SfmReferences
                |          UrefList.Add Uref1

        :rtype: SFMReferences
        """

        return SFMReferences(self.sfm_function_factory.SfmReferences)

    def create_opening(
            self,
            i_category: str,
            i_mode: int,
            i_intersecting_element: Reference,
            i_sfm_object: Reference
    ) -> SFMOpening:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateOpening(CATBSTR iCategory,
                | long iMode,
                | Reference iIntersectingElement,
                | Reference iSfmObject) As SfmOpening
                | 
                |     Creates Opening on SuperPlate or a Profile using a sketch or
                |     3DObject.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Category of Opening 
                |         iMode
                |             [in] Enter 1: To Create Opening Using Sketch Mode Enter 0: To
                |             Create Opening Using 3D Object Mode 
                |         iIntersectingElement
                |             [in] Sketch or 3D Object 
                |         iSfmObject
                |             [in] Object on which Opening is to be created. 
                |         oOpening
                |             [out] Created Opening 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example Creates Opening on the Plate using Sketch Mode. The
                |             Factory is retrieved from the Part.
                | 
                |               'Retrieve the Factory
                |               Set Factory =  part1.GetCustomerFactory("SfmFunctionFactory")
                |               Set sketch = part1.FindObjectByName("Sketch.1")
                |               Set sketchref = part1.CreateReferenceFromObject(sketch)
                |               Set plate = part1.FindObjectByName("Deck_117")
                |               Set plateref = part1.CreateReferenceFromObject(plate)
                |               'Create Opening
                |               Dim OpeningRes as SfmOpening
                |               Set OpeningRes = Factory.CreateOpening("FunctionalOpening",1,sketchref, plateref)

        :param str i_category:
        :param int i_mode:
        :param Reference i_intersecting_element:
        :param Reference i_sfm_object:
        :rtype: SFMOpening
        """
        return SFMOpening(
            self.sfm_function_factory.CreateOpening(
                i_category,
                i_mode,
                i_intersecting_element.com_object,
                i_sfm_object.com_object
            )
        )

    def create_standard_opening(
            self,
            i_category: str,
            i_contour_name: str,
            i_list_contour_params: SFMStandardContourParameters,
            i_pos_strategy_name: str,
            i_position_strategy_parms: SFMStandardPosStrategyParameters,
            isp_target_sfm_object: Reference
    ) -> SFMStandardOpening:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateStandardOpening(CATBSTR iCategory,
                | CATBSTR iContourName,
                | SfmStandardContourParameters iListContourParams,
                | CATBSTR iPosStrategyName,
                | SfmStandardPosStrategyParameters iPositionStrategyParms,
                | Reference ispTargetSfmObject) As SfmStandardOpening
                | 
                |     Creates a StandardOpening on SuperPlate.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             [in] Category of Opening 
                |         iContourName
                |             [in] Name of the Contour. To Get List of Available contour names
                |             ,please see CATIASfmOpeningContoursMgr 
                |         iListContourParams
                |             [in] List of Conotour Parameters for selected Contour For Setting
                |             these parameters,Please see CATIASfmOpeningContoursMgr
                |             
                |         iPosStrategyName
                |             [in] Name of the Position Strategy. Legal
                |             Values:"CATSfmPosOffsetOffset",
                |                    "CATSfmPosHalfHeightOffset",
                |                    "CATSfmPosMidDistOffset",
                |                    "CATSfmPosMidDistMidDist",
                |                    "CATSfmPosHalfHeightMidDist"
                |             Please see CATIASfmPositioningStrategyManager
                |             
                |         iPositionStrategyParms
                |             [in ] List of Parameters for Positioning the Contour. See
                |             CATIASfmStandardPosStrategyParameters 
                |         ispTargetSfmObject
                |             [in ] Object on which Opening will be created 
                |         ospOpening
                |             [out] Created Opening 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This Creates Opening on the Plate using StandardOpening Mode.The
                |             Factory is retrieved from the Part
                | 
                |               'Get the Factory
                |               Set Factory =  part1.GetCustomerFactory("SfmFunctionFactory")
                |               Dim StdOpening as SfmStandardOpening
                |               Set StdOpening = Factory.CreateStandardOpening("FunctionalOpening",
                |                                                              "Sfm_Rect",
                |                                                              oListCkeParms,
                |                                                              "CATSfmPosMidDistMidDist",
                |                                                              PositionStrategyParms,
                |                                                              plateref)

        :param str i_category:
        :param str i_contour_name:
        :param SFMStandardContourParameters i_list_contour_params:
        :param str i_pos_strategy_name:
        :param SFMStandardPosStrategyParameters i_position_strategy_parms:
        :param Reference isp_target_sfm_object:
        :rtype: SFMStandardOpening
        """
        return SFMStandardOpening(
            self.sfm_function_factory.CreateStandardOpening(
                i_category,
                i_contour_name,
                i_list_contour_params.com_object,
                i_pos_strategy_name,
                i_position_strategy_parms.com_object,
                isp_target_sfm_object.com_object
            )
        )

    def get_opening_mgr(self, i_prt_part: Part, i_mgr_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOpeningMgr(Part iPrtPart,
                | CATBSTR iMgrName) As CATBaseDispatch
                | 
                |     Gets the Opening Manager.Use this manager to get SfmOpeningContoursMgr or
                |     SfmPositioningStrategyManager. Use SfmOpeningContoursMgr to
                |     GetAvailableStdOpeningContours and GetStdOpeningContourParams Methods.See
                |     CATIASfmOpeningContoursMgr Use SfmPositioningStrategyManager to manage Position
                |     of contour.See CATIASfmPositioningStrategyManager
                | 
                |     Parameters:
                | 
                |         iPrtPart
                |             [in] Part which contains the plate on which opening is to be
                |             created. 
                |         iMgrName
                |             [in] SfmOpeningContoursMgr: Use to Get Contour Manager.
                |             SfmPositioningStrategyManager: Use to Get Position Strategy Manager
                |             
                |         oSfmOpeningMgr
                |             [out] Manager Object 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This Example gets the Manager from Factory.
                | 
                |               'Get the Factory
                |               Set Factory =  part1.GetCustomerFactory("SfmFunctionFactory")
                |               'Retrieve the Contour Manager
                |               Dim ObjSfmContourMgr As SfmOpeningContoursMgr
                |               Set ObjSfmContourMgr = Factory.GetOpeningMgr(Part1, "SfmOpeningContoursMgr")
                |               'Retrieve the Postion Strategy Manager
                |               Dim ObjSfmPosStrategyMgr  As
                |               SfmPositioningStrategyManager
                |               Set ObjSfmPosStrategyMgr = Factory.GetOpeningMgr(Part1, "SfmPositioningStrategyManager")

        :param Part i_prt_part:
        :param str i_mgr_name:
        :rtype: AnyObject
        """
        return self.sfm_function_factory.GetOpeningMgr(i_prt_part.com_object, i_mgr_name)

    def __repr__(self):
        return f'SFMFunctionFactory(name="{self.name}")'
