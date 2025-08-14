#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class SFMStandardContourParameters(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SfmStandardContourParameters
                | 
                | Interface to access Contour Parametrs from/to the collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Parameter)
        self.sfm_standard_contour_parameters = com_object

    def get_role(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRole() As CATBSTR

        :rtype: str
        """
        return self.sfm_standard_contour_parameters.GetRole()

    def item(self, i_index: cat_variant) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Parameter
                | 
                |     Gets a Reference from the collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             [in] Index of the Reference to be retrieved. 
                |         oReference
                |             [out] Reference. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example retrieves Contour Parameters. The Values to these
                |             parameters then can be set.
                | 
                |              Dim oListCkeParms As SfmStandardContourParameters
                |              Set oListCkeParms = ObjSfmContourMgr.GetStdOpeningContourParams("Sfm_Rect")
                |              'Display List of Parameters for Selected Contour
                |              Dim NbOfParam As Long
                |              NbOfParam = oListCkeParms.Count
                |              Dim ContourParam As Parameter
                |              Dim ContourParamName As String
                |              For i = 1 To NbOfParam
                |              Set ContourParam = oListCkeParms.Item(i)
                |              ContourParamName = oListCkeParms.Item(i).Name
                |              MsgBox ContourParamName
                |              If ContourParamName = "Sfm_Width" Then
                |                 ContourParam.ValuateFromString ("1000mm")
                |                 End If
                |               If ContourParamName = "Sfm_Height" Then
                |                 ContourParam.ValuateFromString ("2000mm")
                |                  End If
                |               If ContourParamName = "Sfm_CornerRadius" Then
                |                ContourParam.ValuateFromString ("10mm")
                |                  End If
                |               Next

        :param cat_variant i_index:
        :rtype: Parameter
        """
        return Parameter(self.sfm_standard_contour_parameters.Item(i_index))

    def __repr__(self):
        return f'SFMStandardContourParameters(name="{self.name}")'
