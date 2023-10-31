#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SFMWeld(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfmWeld
                | 
                | Interface to manage the Structure Functional Modeler Weld
                | object.
                | Role: Provides access to each Weld object's attributes.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_weld = com_object

    @property
    def added_material(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AddedMaterial() As CATBSTR (Read Only)
                | 
                |     Gets Added Material.
                | 
                |     Parameters:
                | 
                |         oAddedMaterial
                |             [out] The retrieved Added Material. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example gets Weld Feature.
                | 
                |              Dim EachWeld As SfmWeld
                |              ustrAddedMaterial = EachWeld.AddedMaterial
                |              Next

        :rtype: str
        """

        return self.sfm_weld.AddedMaterial

    @property
    def edge_preparation(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EdgePreparation() As CATBSTR (Read Only)
                | 
                |     Gets Edge Preparation.
                | 
                |     Parameters:
                | 
                |         oEdgePreparation
                |             [out] The retrieved Edge Preparation. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example gets Weld Feature.
                | 
                |              Dim EachWeld As SfmWeld
                |              ustrEdgePrep = EachWeld.EdgePreparation
                |              Next

        :rtype: str
        """

        return self.sfm_weld.EdgePreparation

    @property
    def fit_up(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FitUp() As CATBSTR (Read Only)
                | 
                |     Gets Fit Up.
                | 
                |     Parameters:
                | 
                |         oFitUp
                |             [out] The retrieved Fit Up. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example gets Weld Feature.
                | 
                |              Dim EachWeld As SfmWeld
                |              ustrFitUp = EachWeld.FitUp
                |              Next

        :rtype: str
        """

        return self.sfm_weld.FitUp

    @property
    def weld_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WeldType() As CATBSTR (Read Only)
                | 
                |     Gets Weld Type.
                | 
                |     Parameters:
                | 
                |         oWeldType
                |             [out] The retrieved Weld Type. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example gets Weld Feature.
                | 
                |              Dim ListWelds As SfmWelds
                |              Set ListWelds = SplitPlate.GetWelds(Nothing)
                |              Dim WeldFeature As SfmWeld
                |              Set WeldFeature = ListWelds.Item(1)
                |              Dim EachWeld As SfmWeld
                |              ustrWeldType = EachWeld.WeldType
                |              Next

        :rtype: str
        """

        return self.sfm_weld.WeldType

    def __repr__(self):
        return f'SFMWeld(name="{self.name}")'
