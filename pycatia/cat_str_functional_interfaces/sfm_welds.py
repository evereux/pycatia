#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_weld import SFMWeld
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class SFMWelds(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SfmWelds
                | 
                | Interface to manage the Structure Functional Modeler Weld object's
                | collection.
                | Role: Provides access to Weld objects as a collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SFMWeld)
        self.sfm_welds = com_object

    def item(self, i_index: cat_variant) -> SFMWeld:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As SfmWeld
                | 
                |     Gets Weld Feature.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             [in] Index of the Weld Feature to be retrieved. 
                |         oSfmWeld
                |             [out] The retrieved Weld Feature. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example gets Weld Feature.
                | 
                |              Dim Welds As SfmWelds
                |              Set Welds = Split_Plate.GetWelds(Nothing)
                |              Dim j As Integer
                |              For j = 1 To Welds.Count
                |              Dim EachWeld As SfmWeld
                |              Set EachWeld = Welds.Item(j)
                |              Next

        :param cat_variant i_index:
        :rtype: SFMWeld
        """
        return SFMWeld(self.sfm_welds.Item(i_index))

    def __repr__(self):
        return f'SFMWelds(name="{self.name}")'
