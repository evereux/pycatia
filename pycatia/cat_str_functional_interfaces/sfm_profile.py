#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_connection_parameters import SFMConnectionParameters
from pycatia.cat_str_functional_interfaces.sfm_endcut import SFMEndcut
from pycatia.cat_str_functional_interfaces.sfm_object import SFMObject
from pycatia.cat_str_functional_interfaces.sfm_references import SFMReferences
from pycatia.cat_str_functional_interfaces.sfm_slots import SFMSlots
from pycatia.in_interfaces.reference import Reference
from pycatia.in_interfaces.references import References


class SFMProfile(SFMObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATStrFunctionalInterfaces.SfmObject
                |                         SfmProfile
                | 
                | Interface to manage the structure frame modeling member object Role: Allows
                | accessing and setting of member's data.
                | 
                | See also:
                |     SfmFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_profile = com_object

    @property
    def anchor_point(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnchorPoint() As CATBSTR
                | 
                |     Returns or sets the member's anchor point.
                | 
                |     Example:
                |         This example retrieves in AnchorPointName the anchor point name of the
                |         SfmProfile feature.
                | 
                |          Dim AnchorPointName As String
                |          Set AnchorPointName = SfmProfile.AnchorPoint

        :rtype: str
        """

        return self.sfm_profile.AnchorPoint

    @anchor_point.setter
    def anchor_point(self, value: str):
        """
        :param str value:
        """

        self.sfm_profile.AnchorPoint = value

    @property
    def section_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectionName() As CATBSTR
                | 
                |     Returns or sets the member's section name.
                | 
                |     Example:
                |         This example retrieves in Name the name of section user by the
                |         SfmProfile feature.
                | 
                |          Dim Name As String
                |          Set Name = SfmProfile.SectionName

        :rtype: str
        """

        return self.sfm_profile.SectionName

    @section_name.setter
    def section_name(self, value: str):
        """
        :param str value:
        """

        self.sfm_profile.SectionName = value

    @property
    def split_profiles(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SplitProfiles() As References (Read Only)
                | 
                |     Returns the SplitProfiles.
                | 
                |     Example:
                |         This example retrieves SplitProfiles list of the
                |         Stiffener.
                | 
                |          Dim SplitStiffeners As References
                |          Set SplitStiffeners = SuperStiffener.SplitProfiles
                |          Dim SplitStiffener1 As Reference
                |          Set SplitStiffener1 = SplitStiffeners.Item(1)
                |          Set SelctionObj = CATIA.ActiveDocument.Selection
                |          SelctionObj.Add SplitStiffener1
                |          Dim SplitStiff1 As SfmStiffener
                |          Set SplitStiff1 = SelctionObj.FindObject("CATIASfmStiffener")

        :rtype: References
        """

        return References(self.sfm_profile.SplitProfiles)

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Support() As Reference (Read Only)
                | 
                |     Returns the member's support.
                | 
                |     Example:
                |         This example retrieves in Support the support of the SfmProfile
                |         feature.
                | 
                |          Dim Support As Reference
                |          Set Support = SfmProfile.Support

        :rtype: Reference
        """

        return Reference(self.sfm_profile.Support)

    def add_endcut(
            self,
            i_extremity_index: int,
            i_endcut_type: str,
            i_endcut_name: str,
            i_list_context: SFMReferences,
            i_list_parameters: SFMConnectionParameters
    ) -> SFMEndcut:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddEndcut(long iExtremityIndex,
                | CATBSTR iEndcutType,
                | CATBSTR iEndcutName,
                | SfmReferences iListContext,
                | SfmConnectionParameters iListParameters) As SfmEndcut
                | 
                |     Creates Endcut on a SuperProfile.Use the method to create as well as edit
                |     the endcut.
                | 
                |     Parameters:
                | 
                |         iExtremityIndex
                |             [in] The extremity on which endcut is to be applied(1-Start,2-End).
                |             
                |         iEndcutType
                |             [in] The type of Endcut(Snipe,Trim,Weld). 
                |         iEndcutName
                |             [in] Name of the Endcut. 
                |         iListContext
                |             [in] Context inputs for contextual endcuts or cutbacks.Not required
                |             for Custom. 
                |         iListParameters
                |             [in] The list of Parameters. 
                |         oSfmProfileEndCut
                |             [out] The created Endcut. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example creates a new contextual endcut on Stiifener Start
                |             extremity.
                | 
                |              ' First read the specifications required for
                |              endcut
                |              Dim FactoryObj As SfmOperationFactory
                |              Set FactoryObj = PartObj.GetCustomerFactory("SfmOperationFactory")
                |              Dim EndCutManagerObj As SfmEndcutManager
                |              Set EndCutManagerObj = FactoryObj.GetEndcutManager
                |              Dim ListOfContextNames, ListOfUDFParamNames As
                |              Variant
                |              Dim ListOfUDFParameters As
                |              SfmConnectionParameters
                |              EndCutManagerObj.GetEndcutSpecifications "Tee", "Snipe",
                |              "T-CTX-PLATE", ListOfContextNames, ListOfUDFParameters,
                |              ListOfUDFParamNames
                |              ' Read the Name of Context
                |              Dim SizeOfContextNames As Long
                |              SizeOfContext = UBound(ListOfContextNames)
                |              Dim ContextName As String
                |              For i = 0 To SizeOfContext  
                |               ContextName = ListOfContextNames(i)
                |              Next
                |              ' Read and Set the Parameter Values
                |              Dim SizeOfUDFParams As Long
                |              SizeOfUDFParams = ListOfUDFParameters.Count
                |              Dim UDFParam As Parameter
                |              For i = 1 To SizeOfUDFParams  
                |               Set UDFParam = ListOfUDFParameters.Item(i)
                |               Dim UDFParamName,UDFParamValue As String
                |               UDFParamName = ListOfUDFParamNames(j - 1)
                |               UDFParamValue = UDFParam.ValueAsString
                |              'Redefine Param Value
                |               If (UDFParamName = "Snipe Radius") Then
                |                 UDFParam.ValuateFromString ("52mm")
                |               End If
                |              Next
                |              ' Define the Context
                |              Dim FactoryRef As SfmFunctionFactory
                |              Set FactoryRef = PartObj.GetCustomerFactory("SfmFunctionFactory")
                |              Dim ListOfContexts As SfmReferences
                |              Set ListOfContexts = FactoryRef.SfmReferences
                |              Dim Limit As Reference
                |              Set Limit = PartObj.CreateReferenceFromObject(SfmSuperPlateObj)
                |              ListOfContexts.Add Limit
                |              ' Create the Endcut
                |              Dim EndCutObj As SfmEndcut
                |              Set EndCutObj = SfmStiffenerObj.AddEndcut(1, "Snipe", "T-CTX-PLATE", ListOfContexts, ListOfUDFParameters)
                |              ' For Non Conetxtual Endcuts pass Nothing for
                |              iListContext
                |              Set EndCutObj = SfmStiffenerObj.AddEndcut(1, "Snipe", "Web_Snipe_Radius", Nothing, ListOfUDFParameters)

        :param int i_extremity_index:
        :param str i_endcut_type:
        :param str i_endcut_name:
        :param SFMReferences i_list_context:
        :param SFMConnectionParameters i_list_parameters:
        :rtype: SFMEndcut
        """
        return SFMEndcut(
            self.sfm_profile.AddEndcut(
                i_extremity_index,
                i_endcut_type,
                i_endcut_name,
                i_list_context.com_object,
                i_list_parameters.com_object
            )
        )

    def get_end_coord(self, o_coord: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetEndCoord(CATSafeArrayVariant oCoord)
                | 
                |     Retrieves the coordinates of the member's end extremity.
                | 
                |     Example
                |     :
                |         This example retrieves in EndExtr the end extremity coordinates of the
                |         SfmProfile feature.
                | 
                |          SfmProfile.GetEndCoord EndExtr

        :param tuple o_coord:
        :rtype: None
        """
        return self.sfm_profile.GetEndCoord(o_coord)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_end_coord'
        # # vba_code = """
        # # Public Function get_end_coord(sfm_profile)
        # #     Dim oCoord (2)
        # #     sfm_profile.GetEndCoord oCoord
        # #     get_end_coord = oCoord
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_endcut(self, i_extremity_index: int) -> SFMEndcut:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetEndcut(long iExtremityIndex) As SfmEndcut
                | 
                |     Retrieves Existing Endcut on Profile.
                | 
                |     Parameters:
                | 
                |         iExtremityIndex
                |             [in] Extremity of Profile(1-Start,2-End). 
                |         oSfmEndcut
                |             [out] Retrieved Endcut. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example gets the Existing Endcut.
                | 
                |              Dim EndCutObj As SfmEndcut
                |              Set EndCutObj = ProfileObj.GetEndcut(1)

        :param int i_extremity_index:
        :rtype: SFMEndcut
        """
        return SFMEndcut(self.sfm_profile.GetEndcut(i_extremity_index))

    def get_profile_limit(self, i_extremity_index: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProfileLimit(long iExtremityIndex) As Reference
                | 
                |     Returns the limit at an Extremity of a Profile.
                | 
                |     Parameters:
                | 
                |         iExtremityIndex
                |             [in] Extremity of Profile(1-Start,2-End). 
                |         oLimit
                |             [out] Existing Limit. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example retrieves the Start Limit of a
                |             Stiffener.
                | 
                |              Dim ProfileLimit As Reference
                |              Set ProfileLimit = SuperStiffenerObj.GetProfileLimit(1)

        :param int i_extremity_index:
        :rtype: Reference
        """
        return Reference(self.sfm_profile.GetProfileLimit(i_extremity_index))

    def get_section_axis(
            self,
            i_abside: float,
            i_origin: tuple,
            io_vector1: tuple,
            io_vector2: tuple,
            io_vector3: tuple
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetSectionAxis(double iAbside,
                | CATSafeArrayVariant iOrigin,
                | CATSafeArrayVariant ioVector1,
                | CATSafeArrayVariant ioVector2,
                | CATSafeArrayVariant ioVector3)
                | 
                |     Retrieves the axis system of the section at a given location on the
                |     member's support.
                | 
                |     Example:
                |         This example retrieves in Origin, Vector1, Vector2, Vector3 the section
                |         axis at the start extremity of the SfmProfile feature.
                | 
                |          Dim Origin, Vector1, Vector2, Vector3 As 
                |          SfmProfile.GetSectionAxis 0., Origin, Vector1, Vector2,
                |          Vector3

        :param float i_abside:
        :param tuple i_origin:
        :param tuple io_vector1:
        :param tuple io_vector2:
        :param tuple io_vector3:
        :rtype: None
        """
        return self.sfm_profile.GetSectionAxis(
            i_abside,
            i_origin,
            io_vector1,
            io_vector2,
            io_vector3
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_section_axis'
        # # vba_code = """
        # # Public Function get_section_axis(sfm_profile)
        # #     Dim iAbside (2)
        # #     sfm_profile.GetSectionAxis iAbside
        # #     get_section_axis = iAbside
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_slots_on_profile(self) -> SFMSlots:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSlotsOnProfile() As SfmSlots
                | 
                |     Retrieves Slots on Profile.
                | 
                |     Parameters:
                | 
                |         oSfmSlots
                |             [out] Slots. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example gets the Slots.
                | 
                |              Dim SlotsonProfile As SfmSlots
                |              Set SlotsonProfile = ProfileObj.GetSlotsOnProfile

        :rtype: SFMSlots
        """
        return SFMSlots(self.sfm_profile.GetSlotsOnProfile())

    def get_start_coord(self, o_coord: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetStartCoord(CATSafeArrayVariant oCoord)
                | 
                |     Retrieves the coordinates of the member's start extremity.
                | 
                |     Example
                |     :
                |         This example retrieves in StartExtr the start extremity coordinates of
                |         the SfmProfile feature.
                | 
                |          SfmProfile.GetStartCoord StartExtr

        :param tuple o_coord:
        :rtype: None
        """
        return self.sfm_profile.GetStartCoord(o_coord)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_start_coord'
        # # vba_code = """
        # # Public Function get_start_coord(sfm_profile)
        # #     Dim oCoord (2)
        # #     sfm_profile.GetStartCoord oCoord
        # #     get_start_coord = oCoord
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_endcut(self, i_extremity_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveEndcut(long iExtremityIndex)
                | 
                |     Removes Existing Endcut on Profile.
                | 
                |     Parameters:
                | 
                |         iExtremityIndex
                |             [in] Extremity of Profile(1-Start,2-End). 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example removes the Existing Endcut.
                | 
                |              Dim EndCutObj As SfmEndcut
                |              Set EndCutObj = ProfileObj.RemoveEndcut(1)

        :param int i_extremity_index:
        :rtype: None
        """
        return self.sfm_profile.RemoveEndcut(i_extremity_index)

    def run(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Run()
                | 
                |     Compute the member's result.
                | 
                |     Example:
                |         This example builds the result of the SfmProfile
                |         feature.
                | 
                |          SfmProfile.Run

        :rtype: None
        """
        return self.sfm_profile.Run()

    def set_profile_limit(self, i_extremity_index: int, i_limit: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProfileLimit(long iExtremityIndex,
                | Reference iLimit)
                | 
                |     Sets the limit at an Extremity of a Profile.
                | 
                |     Parameters:
                | 
                |         iExtremityIndex
                |             [in] Extremity of Profile(1-Start,2-End). 
                |         iLimit
                |             [in] New Limit to add. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example sets the limit at the Extremity.
                | 
                |              Set StiffenerLimit = ObjPart.FindObjectByName("CROSS.115")
                |              Dim LimitRef As Reference
                |              Set LimitRef = ObjPart.CreateReferenceFromObject(StiffenerLimit)
                |              SuperStiffener.SetProfileLimit 2, LimitRef

        :param int i_extremity_index:
        :param Reference i_limit:
        :rtype: None
        """
        return self.sfm_profile.SetProfileLimit(i_extremity_index, i_limit.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_profile_limit'
        # # vba_code = """
        # # Public Function set_profile_limit(sfm_profile)
        # #     Dim iExtremityIndex (2)
        # #     sfm_profile.SetProfileLimit iExtremityIndex
        # #     set_profile_limit = iExtremityIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SFMProfile(name="{self.name}")'
