#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_split_plate import SFMSplitPlate
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class SFMSplitPlates(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SfmSplitPlates
                | 
                | Interface to manage the Structure Functional Modeler Split Plates
                | object.
                | Role: Provides access to split plates of a super plate as a
                | collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SFMSplitPlate)
        self.sfm_split_plates = com_object

    def item(self, i_index: cat_variant) -> SFMSplitPlate:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As SfmSplitPlate
                | 
                |     Gets Split Plate.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             [in] Index of the Split Plate to be retrieved. 
                |         oSfmSplitPlate
                |             [out] The retrieved Split Plate. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example gets existing Split Plate of a Super
                |             Plate.
                | 
                |              Dim ListSplitPlates As SfmSplitPlates
                |              Set ListSplitPlates = SuperPlate.SplitPlatesObjects
                |              Dim Split_Plate As SfmSplitPlate
                |              Set Split_Plate = ListSplitPlates.Item(i)
                |              Next

        :param cat_variant i_index:
        :rtype: SFMSplitPlate
        """
        return SFMSplitPlate(self.sfm_split_plates.Item(i_index))

    def __repr__(self):
        return f'SFMSplitPlates(name="{self.name}")'
