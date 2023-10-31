#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_local_entity import AnalysisLocalEntity
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class AnalysisLocalEntities(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AnalysisLocalEntities
                | 
                | The collection of local analysis entities.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=AnalysisLocalEntity)
        self.analysis_local_entities = com_object

    def add(self, i_type: str) -> AnalysisLocalEntity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(CATBSTR iType) As AnalysisLocalEntity
                | 
                |     Creates a new analysis local entity and adds it to the analysis entities
                |     collection.
                |     This collection may be extracted from an analysis entity.The Analysis local
                |     entity will be created on the Analysis entity.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of the entity to create. 
                | 
                |     Returns:
                |         The created analysis entity 
                |     Example:
                | 
                |           This example create ThisAnalysisEntity in the analysisEntities
                |           collection 
                | 
                |          The entity to create is supposed to be a pressure defined in a load
                |          set.
                | 
                |          
                | 
                |          Dim analysisEntities As CATIAAnalysisLocalEntities
                |          Dim ThisAnalysisEntity As AnalysisEntity
                |          Set ThisAnalysisEntity = analysisEntities.Add("SAMShellLocal")

        :param str i_type:
        :rtype: AnalysisLocalEntity
        """
        return AnalysisLocalEntity(self.analysis_local_entities.Add(i_type))

    def item(self, i_index: cat_variant) -> AnalysisLocalEntity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As AnalysisLocalEntity
                | 
                |     Returns an analysis entity using its index or its name from the analysis
                |     entities collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the analysis entity to retrieve from the
                |             collection of analysis entities. As a numerics, this index is the rank of the
                |             analysis entity in the collection. The index of the first analysis entity in
                |             the collection is 1, and the index of the last analysis entity is Count. As a
                |             string, it is the name you assigned to the analysis entity using the
                |             
                | 
                |         AnyObject.Name property or when creating it using the Add method.
                |         
                |     Returns:
                |         The retrieved analysis entity

        :param cat_variant i_index:
        :rtype: AnalysisLocalEntity
        """
        return AnalysisLocalEntity(self.analysis_local_entities.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Returns an analysis local entity.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the analysis entity to retrieve from the
                |             collection of analysis entities. As a numerics, this index is the rank of the
                |             analysis entity in the collection. The index of the first analysis entity in
                |             the collection is 1, and the index of the last analysis entity is Count. As a
                |             string, it is the name you assigned to the analysis entity using the
                |             
                | 
                |         AnyObject.Name property or when creating it using the Add method.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.analysis_local_entities.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(analysis_local_entities)
        # #     Dim iIndex (2)
        # #     analysis_local_entities.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AnalysisLocalEntities(name="{self.name}")'
