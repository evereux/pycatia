#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_connection_parameters import SFMConnectionParameters
from pycatia.in_interfaces.reference import Reference
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class SFMSlot(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfmSlot
                | 
                | Interface to Get and Set inputs to existing Slot.
                | Role: Allows managing (mainly retreiving parameters)Slots.
                | 
                | See also:
                |     SfmProfile, SfmSuperPlate, SfmSlots, SfmConnectionParameters
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_slot = com_object

    def get_cntn_detail_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCntnDetailName() As CATBSTR
                | 
                |     Gets the name of the UDF used for creating the slot.
                | 
                |     Parameters:
                | 
                |         oUDFName
                |             [in] Name of the UDF. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example gives the name of the UDF used in creating the
                |             slot.
                | 
                |              Dim SlotsonPlate As SfmSlots
                |              Set SlotsonPlate = SfmSuperPlateObj.GetSlotsOnPlate
                |              Dim SlotObj As SfmSlot
                |              Set SlotObj = SlotsonPlate.Item(1)
                |              Dim UDFName As String
                |              UDFName = SlotObj.GetCntnDetailName

        :rtype: str
        """
        return self.sfm_slot.GetCntnDetailName()

    def get_cntn_detail_parameters(
            self,
            o_list_of_slot_parameters: SFMConnectionParameters,
            o_list_of_parameter_names: tuple
    ) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetCntnDetailParameters(SfmConnectionParameters
                | oListOfSlotParameters,
                | CATSafeArrayVariant oListOfParameterNames)
                | 
                |     Gets the Information on Existing Slot.
                | 
                |     Parameters:
                | 
                |         oListOfSlotParameters
                |             [out] List of SfmConnectionParameters. 
                |         oListOfParameterNames
                |             [out] List of Parameter Names set. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This retrieves the Parameter List and Parameter Names and checks
                |             values assigned to these parameters.
                | 
                |              Dim SlotsonPlate As SfmSlots
                |              Set SlotsonPlate = SfmSuperPlateObj.GetSlotsOnPlate
                |              Dim SlotObj As SfmSlot
                |              Set SlotObj = SlotsonPlate.Item(1)
                |              Dim oListSlotParams As SfmConnectionParameters
                |              Dim ListOfParamNames() As Variant
                |              SlotObj.GetCntnDetailParametersoListSlotParams,ListOfParamNames
                |              Dim UDFParam As Parameter
                |              ParamCount = oListSlotParams.Count
                |              Dim Value As String
                |              For i = 1 To ParamCount
                |               Set UDFParam = oListSlotParams.Item(i)  
                |               Value = UDFParam.ValueAsString
                |              Next

        :param SFMConnectionParameters o_list_of_slot_parameters:
        :param tuple o_list_of_parameter_names:
        :rtype: cat_variant
        """
        return self.sfm_slot.GetCntnDetailParameters(o_list_of_slot_parameters.com_object, o_list_of_parameter_names)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_cntn_detail_parameters'
        # # vba_code = """
        # # Public Function get_cntn_detail_parameters(sfm_slot)
        # #     Dim oListOfSlotParameters (2)
        # #     sfm_slot.GetCntnDetailParameters oListOfSlotParameters
        # #     get_cntn_detail_parameters = oListOfSlotParameters
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_connection_coordinate(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetConnectionCoordinate() As CATSafeArrayVariant
                | 
                |     Gets thelocation of existing slot.
                | 
                |     Parameters:
                | 
                |         oCoordinate
                |             [out] The Coordinates. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             The example retrieves slot Coordinates defined on start
                |             end.
                | 
                |              Dim SlotsonPlate As SfmSlots
                |              Set SlotsonPlate = SfmSuperPlateObj.GetSlotsOnPlate
                |              Dim SlotObj As SfmSlot
                |              Set SlotObj = SlotsonPlate.Item(1)
                |              Dim Coord() As Variant
                |              Dim x,y,z as Double
                |              Coord() = SlotObj.GetConnectionCoordinate
                |              x = Coord(0)
                |              y = Coord(1)
                |              z = Coord(2)

        :rtype: tuple
        """
        return self.sfm_slot.GetConnectionCoordinate()

    def get_master_object(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMasterObject() As Reference
                | 
                |     Gets the Penetrating Element used in the creation of the
                |     Slot.
                | 
                |     Parameters:
                | 
                |         oPenetratingObject
                |             [out] The retrieved element(Profile). 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example gets the Master Object.
                | 
                |              Dim SlotsonPlate As SfmSlots
                |              Set SlotsonPlate = SfmSuperPlateObj.GetSlotsOnPlate
                |              Dim SlotObj As SfmSlot
                |              Set SlotObj = SlotsonPlate.Item(1)
                |              Dim oPenetratingRef As Reference
                |              Set oPenetratingRef = SlotObj.GetMasterObject

        :rtype: Reference
        """
        return Reference(self.sfm_slot.GetMasterObject())

    def get_slave_object(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSlaveObject() As Reference
                | 
                |     Gets the Penetrated Element used in the creation of the
                |     Slot.
                | 
                |     Parameters:
                | 
                |         oPenetratedObject
                |             [out] The retrieved element(Plate/Profile). 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example gets the Slave Object.
                | 
                |              Dim SlotsonPlate As SfmSlots
                |              Set SlotsonPlate = SfmSuperPlateObj.GetSlotsOnPlate
                |              Dim SlotObj As SfmSlot
                |              Set SlotObj = SlotsonPlate.Item(1)
                |              Dim oPenetratedRef As Reference
                |              Set oPenetratedRef = SlotObj.GetSlaveObject

        :rtype: Reference
        """
        return Reference(self.sfm_slot.GetSlaveObject())

    def set_slave_object(self, i_slave_object: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSlaveObject(Reference iSlaveObject)
                | 
                |     Sets/Replaces the Penetrated Element used in the creation of the
                |     Slot.
                | 
                |     Parameters:
                | 
                |         iSlaveObject
                |             [in] The retrieved element(Plate/Profile). 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example sets the Slave Object.
                | 
                |              Dim SlotsonPlate As SfmSlots
                |              Set SlotsonPlate = SfmSuperPlateObj.GetSlotsOnPlate
                |              Dim SlotObj As SfmSlot
                |              Set SlotObj = SlotsonPlate.Item(1)
                |              Dim oPenetratedRef As Reference
                |              Set oPenetratedRef = PartObj.CreateReferenceFromObject(SfmNewPlateObj)
                |              SlotObj.SetSlaveObject(oPenetratedRef)

        :param Reference i_slave_object:
        :rtype: None
        """
        return self.sfm_slot.SetSlaveObject(i_slave_object.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_slave_object'
        # # vba_code = """
        # # Public Function set_slave_object(sfm_slot)
        # #     Dim iSlaveObject (2)
        # #     sfm_slot.SetSlaveObject iSlaveObject
        # #     set_slave_object = iSlaveObject
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def update_connections_set(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UpdateConnectionsSet()
                | 
                |     Updates the Connection Set.
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             The example Updates the Connection Set.
                | 
                |              Dim SlotsonPlate As SfmSlots
                |              Set SlotsonPlate = SfmSuperPlateObj.GetSlotsOnPlate
                |              Dim SlotObj As SfmSlot
                |              Set SlotObj = SlotsonPlate.Item(1)
                |              SlotObj.UpdateConnectionsSet

        :rtype: None
        """
        return self.sfm_slot.UpdateConnectionsSet()

    def __repr__(self):
        return f'SFMSlot(name="{self.name}")'
