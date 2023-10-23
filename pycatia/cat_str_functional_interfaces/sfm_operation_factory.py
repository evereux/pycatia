#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_connection_parameters import SFMConnectionParameters
from pycatia.cat_str_functional_interfaces.sfm_endcut_manager import SFMEndcutManager
from pycatia.cat_str_functional_interfaces.sfm_profile import SFMProfile
from pycatia.mec_mod_interfaces.factory import Factory
from pycatia.types.general import cat_variant


class SFMOperationFactory(Factory):
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
                |                         SfmOperationFactory
                | 
                | Gets the Operation Factory.
                | 
                | Example:
                |     This Example Retrieves SfmOperationFactory from Part.
                | 
                |      Set part1 = partDocument1.Part
                |      Dim Factory As SfmOperationFactory
                |      Set Factory =  part1.GetCustomerFactory("SfmOperationFactory")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_operation_factory = com_object

    def get_available_slots_from_catalog(self, i_sfm_profile: SFMProfile) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAvailableSlotsFromCatalog(SfmProfile iSfmProfile) As
                | CATSafeArrayVariant
                | 
                |     Gets the list of available Slots from catalog for a given
                |     Profile(Stiffener/Member).
                | 
                |     Parameters:
                | 
                |         iSfmProfile
                |             [in] The given profile. 
                |         oListofSlotNames
                |             [out] The List of Slots available. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example retrieves the list of avaliable
                |             Slots.
                | 
                |              Dim FactoryObj As SfmOperationFactory
                |              Set FactoryObj = PartObj.GetCustomerFactory("SfmOperationFactory")
                |              Dim ListOfAvailableSlots() As Variant
                |              ListOfAvailableSlots = SlotFactoryObj.GetAvailableSlotsFromCatalog(SfmProfileObj)

        :param SFMProfile i_sfm_profile:
        :rtype: tuple
        """
        return self.sfm_operation_factory.GetAvailableSlotsFromCatalog(i_sfm_profile.com_object)

    def get_endcut_manager(self) -> SFMEndcutManager:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetEndcutManager() As SfmEndcutManager
                | 
                |     Gets the Endcut Manager.
                | 
                |     Parameters:
                | 
                |         oSfmEndcutManager
                |             [out] The retrieved Manager. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example retrieves the Endcut Manager from the
                |             Factory.
                | 
                |              Dim FactoryObj As SfmOperationFactory
                |              Set FactoryObj = PartObj.GetCustomerFactory("SfmOperationFactory")
                |              Dim EndCutManagerObj As SfmEndcutManager
                |              Set EndCutManagerObj = FactoryObj.GetEndcutManager

        :rtype: SFMEndcutManager
        """
        return SFMEndcutManager(self.sfm_operation_factory.GetEndcutManager())

    def get_slot_parameters(
            self,
            i_sfm_profile: SFMProfile,
            i_slot_name: str,
            o_list_slot_parameters: SFMConnectionParameters,
            o_list_slot_param_names: tuple
    ) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetSlotParameters(SfmProfile iSfmProfile,
                | CATBSTR iSlotName,
                | SfmConnectionParameters oListSlotParameters,
                | CATSafeArrayVariant oListSlotParamNames)
                | 
                |     Gets the Slot Parameters and Names for a slot from
                |     catalog.
                | 
                |     Parameters:
                | 
                |         iSfmProfile
                |             [in] The given profile. 
                |         iSlotName
                |             [in] Name of the Slot. 
                |         oListSlotParameters
                |             [out] The Slot UDF Parameters with deafult values.
                |             
                |         oListSlotParamNames
                |             [out] Slot Parameter Names. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example retrieves Parameters for Slot.
                | 
                |              Dim FactoryObj As SfmOperationFactory
                |              Set FactoryObj = PartObj.GetCustomerFactory("SfmOperationFactory")
                |              Dim oListSlotParams As SfmConnectionParameters
                |              Dim oListSlotPramNames() As Variant
                |              SlotFactoryObj.GetSlotParameters SfmProfileObj,
                |              "Tee_Slot_thru_Plate", oListSlotParams,
                |              oListSlotPramNames
                |              'Reading Slot Param Values
                |              Dim UDFParam As Parameter
                |              ParamCount = oListSlotParams.Count
                |              For i = 1 To ParamCount
                |              Set UDFParam = oListSlotParams.Item(i)
                |              ParamName = oListSlotPramNames(i - 1)
                |              ParamValue = UDFParam.ValueAsString
                |              End If
                |              Next

        :param SFMProfile i_sfm_profile:
        :param str i_slot_name:
        :param SFMConnectionParameters o_list_slot_parameters:
        :param tuple o_list_slot_param_names:
        :rtype: cat_variant
        """
        return self.sfm_operation_factory.GetSlotParameters(
            i_sfm_profile.com_object,
            i_slot_name,
            o_list_slot_parameters.com_object,
            o_list_slot_param_names)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_slot_parameters'
        # # vba_code = """
        # # Public Function get_slot_parameters(sfm_operation_factory)
        # #     Dim iSfmProfile (2)
        # #     sfm_operation_factory.GetSlotParameters iSfmProfile
        # #     get_slot_parameters = iSfmProfile
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SFMOperationFactory(name="{self.name}")'
