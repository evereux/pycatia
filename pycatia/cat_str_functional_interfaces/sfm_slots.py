#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_connection_parameters import SFMConnectionParameters
from pycatia.cat_str_functional_interfaces.sfm_slot import SFMSlot
from pycatia.in_interfaces.reference import Reference
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class SFMSlots(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SfmSlots
                | 
                | Interface to create, remove and access existing slot.
                | Role: Allows creating,removing and accessing slot object.
                | 
                | See also:
                |     SfmSlots, SfmSuperPlate, SfmProfile, SfmConnectionParameters
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SFMSlot)
        self.sfm_slots = com_object

    def add_slot(
            self,
            i_penetrated_element: Reference,
            i_penetrating_object: Reference,
            i_slot_name: str,
            i_list_parameters: SFMConnectionParameters
    ) -> SFMSlot:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddSlot(Reference iPenetratedElement,
                | Reference iPenetratingObject,
                | CATBSTR iSlotName,
                | SfmConnectionParameters iListParameters) As SfmSlot
                | 
                |     Creates a New Slot.
                | 
                |     Parameters:
                | 
                |         iPenetratedElement
                |             [in] Object on which slot will be created(Plate/Profile).
                |             
                |         iPenetratingObject
                |             [in] Object using which slot will be created(Profile).
                |             
                |         iSlotName
                |             [in] Slot Name. 
                |         iListParameters
                |             [in] List of UDF parameters. 
                |         oSfmSlot
                |             [out] Created Slot. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example creates a new Slot on Plate.
                | 
                |              Dim PenetratedRef, PenetratingRef As Reference
                |              Set PenetratedRef = PartObj.CreateReferenceFromObject(SfmSuperPlateObj)
                |              Set PenetratingRef = PartObj.CreateReferenceFromObject(SfmSuperStiffenerObj)
                |              Dim SlotFactory As SfmOperationFactory
                |              Set SlotFactory = PartObj.GetCustomerFactory("SfmOperationFactory")
                |              Dim oListSlotParams As SfmConnectionParameters
                |              Dim oListSlotPramNames() As Variant
                |              SlotFactory.GetSlotParameters SfmSuperStiffenerObj,
                |              "Tee_Slot_thru_Plate", oListSlotParams,
                |              oListSlotPramNames
                |              Dim SlotsonPlate As SfmSlots
                |              Set SlotsonPlate = SfmSuperPlateObj.GetSlotsOnPlate
                |              Dim NewSlot As SfmSlot
                |              Set NewSlot = SlotsonPlate.AddSlot(PenetratedRef, PenetratedRef, "Tee_Slot_thru_Plate", oListSlotParams, oListSlotPramNames)

        :param Reference i_penetrated_element:
        :param Reference i_penetrating_object:
        :param str i_slot_name:
        :param SFMConnectionParameters i_list_parameters:
        :rtype: SFMSlot
        """
        return SFMSlot(
            self.sfm_slots.AddSlot(
                i_penetrated_element.com_object,
                i_penetrating_object.com_object,
                i_slot_name,
                i_list_parameters.com_object
            )
        )

    def item(self, i_index: cat_variant) -> SFMSlot:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As SfmSlot
                | 
                |     Gets existing Slot.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             [in] Index of the Slot to be retrieved. 
                |         oSfmSlot
                |             [out] The retrieved slot. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example gets existing slot on a Plate.
                | 
                |              Dim SlotsonPlate As SfmSlots
                |              Set SlotsonPlate = SfmSuperPlateObj.GetSlotsOnPlate
                |              Dim CntSlotsOnPlate As Long
                |              CntSlotsOnPlate = SlotsonPlate.Count
                |              Dim SlotObj As SfmSlot
                |              For i = 1 To CntSlotsOnPlate
                |              Set SlotObj = SlotsonPlate.Item(i)
                |              Next

        :param cat_variant i_index:
        :rtype: SFMSlot
        """
        return SFMSlot(self.sfm_slots.Item(i_index))

    def remove_slot(self, i_sfm_slot: SFMSlot) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveSlot(SfmSlot iSfmSlot)
                | 
                |     Removes Existing Slot.
                | 
                |     Parameters:
                | 
                |         iSfmSlot
                |             [in] Slot to be removed. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example removes existing slot on a Plate.
                | 
                |              Dim SlotsonPlate As SfmSlots
                |              Set SlotsonPlate = SfmSuperPlateObj.GetSlotsOnPlate
                |              Dim SlotObj As SfmSlot
                |              Set SlotObj = SlotsonPlate.Item(1)
                |              SlotsonPlate.RemoveSlot(SlotObj)

        :param SFMSlot i_sfm_slot:
        :rtype: None
        """
        return self.sfm_slots.RemoveSlot(i_sfm_slot.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_slot'
        # # vba_code = """
        # # Public Function remove_slot(sfm_slots)
        # #     Dim iSfmSlot (2)
        # #     sfm_slots.RemoveSlot iSfmSlot
        # #     remove_slot = iSfmSlot
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SFMSlots(name="{self.name}")'
