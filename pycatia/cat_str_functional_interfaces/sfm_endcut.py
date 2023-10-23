#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_connection_parameters import SFMConnectionParameters
from pycatia.cat_str_functional_interfaces.sfm_references import SFMReferences
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class SFMEndcut(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfmEndcut
                | 
                | Interface to manage the EndCut on Super Profile.
                | Role: Allows managing (mainly retreiving parameters)on existing
                | EndCut.
                | 
                | See also:
                |     SfmProfile, SfmEndcutManager, SfmConnectionParameters
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_endcut = com_object

    def get_connection_coordinate(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetConnectionCoordinate() As CATSafeArrayVariant
                | 
                |     Gets thelocation of existing endcut.
                | 
                |     Parameters:
                | 
                |         oCoordinate
                |             [out] The Coordinates. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example
                |         :
                |             The example retrieves endcut Coordinates defined on start
                |             end.
                | 
                |              Dim EndcutObj As SfmEndcut
                |              Set EndcutObj = StiffObj.GetEndcut(1)
                |              Dim Coord() As Variant
                |              Dim x,y,z as Double
                |              Coord() = EndcutObj.GetConnectionCoordinate
                |              x = Coord(0)
                |              y = Coord(1)
                |              z = Coord(2)

        :rtype: tuple
        """
        return self.sfm_endcut.GetConnectionCoordinate()

    def get_endcutinfo(
            self,
            o_type_of_endcut: str,
            o_name_of_endcut: str,
            o_list_of_endcut_contexts: SFMReferences,
            o_list_of_endcut_params: SFMConnectionParameters,
            o_list_of_end_cut_param_names: tuple
    ) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetEndcutinfo(CATBSTR oTypeOfEndcut,
                | CATBSTR oNameOfEndcut,
                | SfmReferences oListOfEndcutContexts,
                | SfmConnectionParameters oListOfEndcutParams,
                | CATSafeArrayVariant oListOfEndCutParamNames)
                | 
                |     Gets the information on existing Endcut.
                | 
                |     Parameters:
                | 
                |         oTypeOfEndcut
                |             [out] Type of Endcut(Snipe,Trim,Weld). 
                |         oNameOfEndcut
                |             [out] Name of the Endcut. 
                |         oListOfEndcutContexts
                |             [out] List of Contexts (Limits) defined for Cutbacks and Contextual
                |             Endcuts. The list will be empty for custom UDF based endcuts.
                |             
                |         oListOfEndcutParams
                |             [out] List of Parameters set when defining the Endcut.
                |             
                |         oListOfEndCutParamNames
                |             [out] List of Parameter Names set when defining the Endcut.
                |             
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example
                |         :
                |             The example retrieves endcut information.
                | 
                |              Dim EndcutObj As SfmEndcut
                |              Set EndcutObj = StiffObj.GetEndcut(1)
                |              Dim EndCutName, EndCutType As String
                |              Dim ContextList  As SfmReferences
                |              Dim ParamList As SfmConnectionParameters
                |              Dim ParamNamesList() As Variant
                |              EndcutObj.GetEndcutinfo EndCutType, EndCutName, ContextList,
                |              ParamList, ParamNamesList

        :param str o_type_of_endcut:
        :param str o_name_of_endcut:
        :param SFMReferences o_list_of_endcut_contexts:
        :param SFMConnectionParameters o_list_of_endcut_params:
        :param tuple o_list_of_end_cut_param_names:
        :rtype: cat_variant
        """
        return self.sfm_endcut.GetEndcutinfo(
            o_type_of_endcut,
            o_name_of_endcut,
            o_list_of_endcut_contexts.com_object,
            o_list_of_endcut_params.com_object,
            o_list_of_end_cut_param_names
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_endcutinfo'
        # # vba_code = """
        # # Public Function get_endcutinfo(sfm_endcut)
        # #     Dim oTypeOfEndcut (2)
        # #     sfm_endcut.GetEndcutinfo oTypeOfEndcut
        # #     get_endcutinfo = oTypeOfEndcut
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
                |         Example
                |         :
                |             The example Updates the Connection Set.
                | 
                |              Dim EndcutObj As SfmEndcut
                |              Set EndcutObj = StiffObj.GetEndcut(1)
                |              EndcutObj.UpdateConnectionsSet

        :rtype: None
        """
        return self.sfm_endcut.UpdateConnectionsSet()

    def __repr__(self):
        return f'SFMEndcut(name="{self.name}")'
