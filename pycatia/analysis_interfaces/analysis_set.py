#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.analysis_interfaces.analysis_entities import AnalysisEntities
from pycatia.analysis_interfaces.analysis_images import AnalysisImages
from pycatia.analysis_interfaces.analysis_output_entities import AnalysisOutputEntities
from pycatia.analysis_interfaces.basic_components import BasicComponents
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.analysis_interfaces.analysis_sets import AnalysisSets


class AnalysisSet(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnalysisSet
                | 
                | Represent the analysis set object.
                | In the Analysis Model, an Analysis Set is the data dedicated to manage the
                | Analysis Entities for specific preprocessing data.
                | For example, LoadSet will manage loading conditions...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_set = com_object

    @property
    def analysis_entities(self) -> AnalysisEntities:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisEntities() As AnalysisEntities (Read Only)
                | 
                |     Returns the analysis entities collection associated to a set. The
                |     corresponding entities are default preprocessing objects.
                | 
                |     Example :
                |         This example retrieves analysis entities collection .
                | 
                |          Dim MySet As AnalysisSet
                |          Dim analysisEntities As AnalysisEntities
                |          Set analysisEntities = MySet.AnalysisEntities

        :rtype: AnalysisEntities
        """

        return AnalysisEntities(self.analysis_set.AnalysisEntities)

    @property
    def analysis_images(self) -> AnalysisImages:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisImages() As AnalysisImages (Read Only)
                | 
                |     Returns the analysis images collection associated with an analysis
                |     set.
                | 
                |     Example:
                |         This example retrieves analysisimages collection .
                | 
                |          Dim MySet As AnalysisSet
                |          Dim analysisimages As AnalysisImages
                |          Set analysisimages = MySet.AnalysisImages

        :rtype: AnalysisImages
        """

        return AnalysisImages(self.analysis_set.AnalysisImages)

    @property
    def analysis_output_entities(self) -> AnalysisOutputEntities:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisOutputEntities() As AnalysisOutputEntities (Read
                | Only)
                | 
                |     Returns the analysis entities collection associated to a set. The
                |     corresponding entities are not preprocessing features but can be used, for
                |     example to manage error features.
                | 
                |     Example:
                |         This example retrieves analysisEntities collection .
                | 
                |          Dim MySet As AnalysisSet
                |          Dim analysisEntities As AnalysisOutputEntities
                |          Set analysisEntities = MySet.AnalysisOutputEntities

        :rtype: AnalysisOutputEntities
        """

        return AnalysisOutputEntities(self.analysis_set.AnalysisOutputEntities)

    @property
    def analysis_sets(self) -> 'AnalysisSets':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisSets() As AnalysisSets (Read Only)
                | 
                |     Returns the analysis sets collection associated with an analysis set. This
                |     method will return a collection only if the set is made of other
                |     sets.
                | 
                |     Example:
                |         This example retrieves analysisSets collection .
                | 
                |          Dim MySet As AnalysisSet
                |          Dim analysisSets As AnalysisSets
                |          Set analysisSets = MySet.AnalysisSets

        :rtype: AnalysisSets
        """

        from pycatia.analysis_interfaces.analysis_sets import AnalysisSets
        return AnalysisSets(self.analysis_set.AnalysisSets)

    @property
    def basic_components(self) -> BasicComponents:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BasicComponents() As BasicComponents (Read Only)
                | 
                |     Returns the basic components collection associated with an analysis
                |     set.
                | 
                |     Example:
                |         This example retrieves basiccomponents collection .
                | 
                |          Dim MySet As AnalysisSet
                |          Dim basiccomponents As BasicComponents 
                |          Set basiccomponents = MySet.BasicComponents

        :rtype: BasicComponents
        """

        return BasicComponents(self.analysis_set.BasicComponents)

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the type of the analysis Set.
                | 
                |     Example:
                |         The following example returns TypeofSet of MySet.
                | 
                |          Dim MySet As AnalysisSet
                |          Dim TypeofSet As CATBSTR
                |          Set TypeofSet = MySet.Type

        :rtype: str
        """

        return self.analysis_set.Type

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Update()
                | 
                |     Launch the update (computation if needed) of an AnalysisSet.

        :rtype: None
        """
        return self.analysis_set.Update()

    def __repr__(self):
        return f'AnalysisSet(name="{self.name}")'
