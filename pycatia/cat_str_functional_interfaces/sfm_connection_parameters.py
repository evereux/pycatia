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


class SFMConnectionParameters(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SfmConnectionParameters
                | 
                | Interface to get the parameters defining the UDF for Slots and
                | Endcuts.
                | Role: To Get/Set the parameters of the UDF.
                | 
                | See also:
                |     SfmSlots, SfmEndcut, SfmEndcutManager
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Parameter)
        self.sfm_connection_parameters = com_object

    def item(self, i_index: cat_variant) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Parameter
                | 
                |     Gets a Item from the collection list.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             [in] Index of the item to be retrieved. 
                |         oStdConParm
                |             [out] The required parameter. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example
                |         :
                |             This example retrieves and manipulates existing BuiltIn EndCut
                |             parameters.
                | 
                |              Dim oStartEndCutObj As SfmEndcut
                |              Set oStartEndCutObj = StiffObj.GetEndcut(1) 
                |              Dim oStartEndCutType,oStartEndCutName As String
                |              Dim oLimitContextList As SfmReferences
                |              Dim oConnectionParamList As
                |              SfmConnectionParameters
                |              Dim oConnectionParamNames() As Variant
                |              oStartEndCutObj.GetEndcutinfo oStartEndCutType, oStartEndCutName,
                |              oLimitContextList, oConnectionParamList, oConnectionParamNames 
                |              
                |              ' Reading Parameters
                |              Dim SizeOfUDFParams As Long
                |              SizeOfUDFParams = oConnectionParamList.Count
                |              Dim UDFParam As Parameter
                |              Dim UDFParamName, UDFParamValue As String
                |              For i = 1 To SizeOfUDFParams
                |               Set UDFParam = oConnectionParamList.Item(i)
                |               UDFParamName = oConnectionParamNames(i - 1)
                |               UDFParamValue = UDFParam.ValueAsString
                |              Next 
                |              ' Setting Parameters
                |              For j = 1 To SizeOfUDFParams
                |               Set UDFParam = oConnectionParamList.Item(j)
                |              UDFParamName = oConnectionParamNames(j - 1)
                |              If (UDFParamName = "A1") Then
                |                 UDFParam.ValuateFromString ("16deg")
                |                 End If
                |              If (UDFParamName = "A2") Then
                |                  UDFParam.ValuateFromString ("16deg")
                |                  End If
                |              If (UDFParamName = "B") Then
                |                  UDFParam.ValuateFromString ("31deg")
                |                  End If
                |              Next

        :param cat_variant i_index:
        :rtype: Parameter
        """
        return Parameter(self.sfm_connection_parameters.Item(i_index))

    def __repr__(self):
        return f'SFMConnectionParameters(name="{self.name}")'
