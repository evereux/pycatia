#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_welds import SFMWelds
from pycatia.in_interfaces.reference import Reference
from pycatia.system_interfaces.any_object import AnyObject


class SFMSplitPlate(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfmSplitPlate
                | 
                | Interface to manage the Structure Functional Modeler Split plate
                | object.
                | Role: Provides access to weld objects on Split plate.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_split_plate = com_object

    def get_welds(self, i_operating_ele: Reference) -> SFMWelds:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetWelds(Reference iOperatingEle) As SfmWelds
                | 
                |     Gets Welds feature on operated Plate.
                | 
                |     Parameters:
                | 
                |         iOperatingEle
                |             [in] Operating element of the weld features. 
                |         oWelds
                |             [out] The retrieved Weld features. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example gets welds features of Split Plate.
                | 
                |              Dim Welds As SfmWelds
                |              Set Welds = Split_Plate.GetWelds(Nothing)

        :param Reference i_operating_ele:
        :rtype: SFMWelds
        """
        return SFMWelds(self.sfm_split_plate.GetWelds(i_operating_ele.com_object))

    def __repr__(self):
        return f'SFMSplitPlate(name="{self.name}")'
