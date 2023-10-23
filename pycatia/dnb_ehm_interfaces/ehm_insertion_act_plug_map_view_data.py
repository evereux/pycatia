#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity


class EhmInsertionActPlugMapViewData(Activity):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMAPSInterfaces.Activity
                |                         EHMInsertionActPlugMapViewData
                | 
                | Interface to access Plug Map view data associated to an Insertion
                | activity.
                | 
                | Role: Component that implement DNBIAEHMInsertionActPlugMapViewData is
                | DNBEHMModel.
                | 
                | When using DNBIAEHMInsertionActPlugMapViewData interface in C++, query from
                | interface DNBIEHMInsertionActivity.
                | When using from VB Script, use GetTechnologicalObject to get handle to
                | interface.
                | 
                | PlugMap Data consists of 2 parts namely Connector data & inserted wires
                | data.
                | To get data about inserted wires, first get the number of wires using
                | method
                | get_NumInsertedWires, then set index of wire using put_WireID and then access
                | information about that wire.
                | Please note that default returned string for all PROPERTY of type CATBSTR is
                | "UnSet".
                | 
                | Sample Code in VB Script is as given below
                | '---- InsertionAct is activity for Plug Map view data.
                | Dim InsertionAct As Activity
                | Set InsertionAct = get activity DNBEHMInsertionAct.1
                | Set PlugMapData = InsertionAct.GetTechnologicalObject( "EHMInsertionActPlugMapViewData" )
                | Dim ConnectorName As String
                | ConnectorName = PlugMapData.ConnectorName
                | Dim NumInsertedWires, ii As Integer
                | NumInsertedWires = PlugMapData.NumInsertedWires
                | Dim TerminationName, WireName, ContactName As String
                | For ii = 1 to NumInsertedWires
                | PlugMapData.WireID = ii
                | TerminationName = PlugMapData.TerminationName
                | WireName = PlugMapData.WireName
                | Next
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.ehm_insertion_act_plug_map_view_data = com_object

    @property
    def connector_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConnectorName() As CATBSTR (Read Only)
                | 
                |     Gets ConnectorName.
                | 
                |     Parameters:
                | 
                |         oConnectorName
                |             the Connector Name. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.ConnectorName

    @property
    def connector_part_number(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConnectorPartNumber() As CATBSTR (Read Only)
                | 
                |     Gets Connector Part Number.
                | 
                |     Parameters:
                | 
                |         oConnectorPartNumber
                |             the Connector Part Number. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.ConnectorPartNumber

    @property
    def connector_ref_designator(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConnectorRefDesignator() As CATBSTR (Read Only)
                | 
                |     Gets Connector Reference Designator.
                | 
                |     Parameters:
                | 
                |         oConnectorRefDesignator
                |             the Connector Reference Designator. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.ConnectorRefDesignator

    @property
    def connector_sub_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConnectorSubType() As CATBSTR (Read Only)
                | 
                |     Gets Connector Sub Type.
                | 
                |     Parameters:
                | 
                |         oConnectorSubType
                |             the Connector Sub Type. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.ConnectorSubType

    @property
    def connector_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConnectorType() As CATBSTR (Read Only)
                | 
                |     Gets Connector Type.
                | 
                |     Parameters:
                | 
                |         oConnectorType
                |             the Connector Type. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.ConnectorType

    @property
    def contact_elec_barrel_diameter(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ContactElecBarrelDiameter() As double (Read Only)
                | 
                |     Gets Contact Elec Barrel Diameter.
                | 
                |     Parameters:
                | 
                |         oContactElecBarrelDiameter
                |             the Contact Elec Barrel Diameter. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: float
        """

        return self.ehm_insertion_act_plug_map_view_data.ContactElecBarrelDiameter

    @property
    def contact_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ContactName() As CATBSTR (Read Only)
                | 
                |     Gets Contact Name.
                | 
                |     Parameters:
                | 
                |         oContactName
                |             the Contact Name. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.ContactName

    @property
    def contact_part_number(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ContactPartNumber() As CATBSTR (Read Only)
                | 
                |     Gets Contact Part Number.
                | 
                |     Parameters:
                | 
                |         oContactPartNumber
                |             the Contact Part Number. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.ContactPartNumber

    @property
    def contact_ref_designator(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ContactRefDesignator() As CATBSTR (Read Only)
                | 
                |     Gets Contact Reference Designator.
                | 
                |     Parameters:
                | 
                |         oContactRefDesignator
                |             the Contact Ref Designator. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.ContactRefDesignator

    @property
    def contact_sub_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ContactSubType() As CATBSTR (Read Only)
                | 
                |     Gets Contact Sub Type.
                | 
                |     Parameters:
                | 
                |         oContactSubType
                |             the Contact Sub Type. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.ContactSubType

    @property
    def contact_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ContactType() As CATBSTR (Read Only)
                | 
                |     Gets Contact Type.
                | 
                |     Parameters:
                | 
                |         oContactType
                |             the Contact Type. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.ContactType

    @property
    def num_inserted_wires(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumInsertedWires() As long (Read Only)
                | 
                |     Gets the number of inserted wires.
                | 
                |     Parameters:
                | 
                |         NumInsertedWires
                |             the number of inserted wires. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the wire ID is set successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: int
        """

        return self.ehm_insertion_act_plug_map_view_data.NumInsertedWires

    @property
    def termination_id_number(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TerminationIDNumber() As CATBSTR (Read Only)
                | 
                |     Gets Termination ID Number.
                | 
                |     Parameters:
                | 
                |         oTerminationIDNumber.
                |             the Termination ID Number 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.TerminationIDNumber

    @property
    def termination_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TerminationName() As CATBSTR (Read Only)
                | 
                |     Gets Termination Name.
                | 
                |     Parameters:
                | 
                |         oTerminationName
                |             the Termination Name. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.TerminationName

    @property
    def termination_number(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TerminationNumber() As CATBSTR (Read Only)
                | 
                |     Gets Termination Number.
                | 
                |     Parameters:
                | 
                |         oTerminationNumber
                |             the Termination Number. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.TerminationNumber

    @property
    def termination_ref_designator(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TerminationRefDesignator() As CATBSTR (Read Only)
                | 
                |     Gets Termination Reference Designator.
                | 
                |     Parameters:
                | 
                |         oTerminationRefDesignator
                |             the Termination Ref Designator. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.TerminationRefDesignator

    @property
    def termination_sub_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TerminationSubType() As CATBSTR (Read Only)
                | 
                |     Gets Termination Sub Type.
                | 
                |     Parameters:
                | 
                |         oTerminationSubType
                |             the Termination Sub Type. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.TerminationSubType

    @property
    def termination_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TerminationType() As CATBSTR (Read Only)
                | 
                |     Gets Termination Type.
                | 
                |     Parameters:
                | 
                |         oTerminationType
                |             the Termination Type. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.TerminationType

    @property
    def wire_colour(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WireColor() As CATBSTR (Read Only)
                | 
                |     Gets Wire Color.
                | 
                |     Parameters:
                | 
                |         oWireColor
                |             the Wire Color. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.WireColor

    @property
    def wire_diameter(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WireDiameter() As double (Read Only)
                | 
                |     Gets Wire Diameter.
                | 
                |     Parameters:
                | 
                |         oWireDiameter
                |             the Wire Diameter. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: float
        """

        return self.ehm_insertion_act_plug_map_view_data.WireDiameter

    @property
    def wire_id(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WireID(long iWireID) (Write Only)
                | 
                |     Sets the index of wire.
                | 
                |     Parameters:
                | 
                |         iWireID
                |             Index of wire between 1 & NumInsertedWires associated to an
                |             Insertion Activity. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the wire ID is set successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: int
        """

        return self.ehm_insertion_act_plug_map_view_data.WireID

    @wire_id.setter
    def wire_id(self, value: int):
        """
        :param int value:
        """

        self.ehm_insertion_act_plug_map_view_data.WireID = value

    @property
    def wire_length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WireLength() As double (Read Only)
                | 
                |     Gets Wire Length.
                | 
                |     Parameters:
                | 
                |         oWireLength
                |             the Wire Length. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: float
        """

        return self.ehm_insertion_act_plug_map_view_data.WireLength

    @property
    def wire_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WireName() As CATBSTR (Read Only)
                | 
                |     Gets Wire Name.
                | 
                |     Parameters:
                | 
                |         oWireName
                |             the Wire Name. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.WireName

    @property
    def wire_part_number(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WirePartNumber() As CATBSTR (Read Only)
                | 
                |     Gets Wire Part Number.
                | 
                |     Parameters:
                | 
                |         oWirePartNumber
                |             the Wire Part Number. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.WirePartNumber

    @property
    def wire_ref_designator(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WireRefDesignator() As CATBSTR (Read Only)
                | 
                |     Gets Wire Reference Designator.
                | 
                |     Parameters:
                | 
                |         oWireRefDesignator
                |             the Wire Ref Designator. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.WireRefDesignator

    @property
    def wire_separation_code(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WireSeparationCode() As CATBSTR (Read Only)
                | 
                |     Gets Wire Separation Code.
                | 
                |     Parameters:
                | 
                |         oWireSeparationCode
                |             the Wire Separation Code. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.WireSeparationCode

    @property
    def wire_signal_id(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WireSignalID() As CATBSTR (Read Only)
                | 
                |     Gets Wire Signal ID.
                | 
                |     Parameters:
                | 
                |         oWireSignalID
                |             the Wire Signal ID. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.WireSignalID

    @property
    def wire_sub_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WireSubType() As CATBSTR (Read Only)
                | 
                |     Gets Wire Sub Type.
                | 
                |     Parameters:
                | 
                |         oWireSubType
                |             the Wire Sub Type. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.WireSubType

    @property
    def wire_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WireType() As CATBSTR (Read Only)
                | 
                |     Gets Wire Type.
                | 
                |     Parameters:
                | 
                |         oWireType
                |             the Wire Type. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :rtype: str
        """

        return self.ehm_insertion_act_plug_map_view_data.WireType

    def __repr__(self):
        return f'EhmInsertionActPlugMapViewData(name="{self.name}")'
