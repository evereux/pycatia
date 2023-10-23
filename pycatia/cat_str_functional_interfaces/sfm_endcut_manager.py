#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_connection_parameters import SFMConnectionParameters
from pycatia.system_interfaces.any_object import AnyObject


class SFMEndcutManager(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfmEndcutManager
                | 
                | Interface to get information on available endcuts from
                | catalog.
                | Role: Allows to see avaiable endcuts and their reuired inputs.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_endcut_manager = com_object

    def get_available_endcuts(self, i_section_family: str, i_endcut_type: str) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAvailableEndcuts(CATBSTR iSectionFamily,
                | CATBSTR iEndcutType) As CATSafeArrayVariant
                | 
                |     Gets the list of available endcuts for a given family and type from the
                |     catalog.
                | 
                |     Parameters:
                | 
                |         iSectionFamily
                |             [in] The name of the Section Family(Tee,Angle,Bulb).
                |             
                |         iType
                |             [in] The Type of Endcut(Snipe,Trim,Weld). 
                |         oListEndcutNames
                |             [out] A list of the available Endcuts. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example retrieves the list of avaliable Endcuts for Tee
                |             ProfileType and Snipe EndcutType.
                | 
                |              Dim FactoryObj As SfmOperationFactory
                |              Set FactoryObj = PartObj.GetCustomerFactory("SfmOperationFactory")
                |              Dim EndCutManagerObj As SfmEndcutManager
                |              Set EndCutManagerObj = FactoryObj.GetEndcutManager
                |              Dim ListOfEndCutNames() As Variant
                |              ListOfEndCutNames = EndCutManagerObj.GetAvailableEndcuts("Tee", "Snipe")

        :param str i_section_family:
        :param str i_endcut_type:
        :rtype: tuple
        """
        return self.sfm_endcut_manager.GetAvailableEndcuts(i_section_family, i_endcut_type)

    def get_endcut_specifications(
            self,
            i_section_family: str,
            i_endcut_type: str,
            i_endcut_name: str,
            o_list_of_context_names: tuple,
            o_list_end_cut_parameters: SFMConnectionParameters,
            o_list_of_end_cut_param_names: tuple
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetEndcutSpecifications(CATBSTR iSectionFamily,
                | CATBSTR iEndcutType,
                | CATBSTR iEndcutName,
                | CATSafeArrayVariant oListOfContextNames,
                | SfmConnectionParameters oListEndCutParameters,
                | CATSafeArrayVariant oListOfEndCutParamNames)
                | 
                |     Gets the Specifications required to define a particular
                |     Endcut.
                | 
                |     Parameters:
                | 
                |         iSectionFamily
                |             [in] The Section Family(Tee,Angle,Bulb). 
                |         iEndcutType
                |             [in] The EndcutType(Snipe,Trim,Weld). 
                |         iEndcutName
                |             [in] The Name of the Endcut sought from GetAvailableEndcuts Method.
                |             
                |         oListOfContextNames
                |             [out] The Limit Names for the Endcut(Cutbacks & Contextual only).
                |             The List will be empty for Cutom Endcut. 
                |         oListEndCutParameters
                |             [out] A list of Parameters published by the UDF. The default values
                |             can be read using this output. 
                |         oListOfEndCutParamNames
                |             [out] A list of Parameter Names published by the UDF.
                |
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example retrieves the list of avaliable Endcuts for Tee
                |             ProfileType and Snipe EndcutType.
                | 
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

        :param str i_section_family:
        :param str i_endcut_type:
        :param str i_endcut_name:
        :param tuple o_list_of_context_names:
        :param SFMConnectionParameters o_list_end_cut_parameters:
        :param tuple o_list_of_end_cut_param_names:
        :rtype: None
        """
        return self.sfm_endcut_manager.GetEndcutSpecifications(
            i_section_family,
            i_endcut_type,
            i_endcut_name,
            o_list_of_context_names,
            o_list_end_cut_parameters.com_object,
            o_list_of_end_cut_param_names
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_endcut_specifications'
        # # vba_code = """
        # # Public Function get_endcut_specifications(sfm_endcut_manager)
        # #     Dim iSectionFamily (2)
        # #     sfm_endcut_manager.GetEndcutSpecifications iSectionFamily
        # #     get_endcut_specifications = iSectionFamily
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SFMEndcutManager(name="{self.name}")'
