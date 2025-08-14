#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_analysis_case import ABQAnalysisCase
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ABQAnalysisCases(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ABQAnalysisCases
                | 
                | The collection of ABQAQUS analysis case objects attached to an
                | ABQAnalysisModel object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ABQAnalysisCase)
        self.abq_analysis_cases = com_object

    def add(self, i_analysis_type: str) -> ABQAnalysisCase:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(CATBSTR iAnalysisType) As ABQAnalysisCase
                | 
                |     Creates a new Abaqus analysis case and adds it to the collection of Abaqus
                |     analysis cases.
                | 
                |     Parameters:
                | 
                |         iAnalysisType
                |             The type of Analysis Case to create.
                | 
                |             Legal values:
                | 
                |             "STRUCTURAL"
                |             "THERMAL"
                |             "EXPLICIT_DYNAMICS"
                | 
                |     Returns:
                |         The Abaqus analysis case object that was created. 
                |     Example:
                |         The following example creates an Abaqus analysis case
                |         abqCase1:
                | 
                |          Dim abqCases As ABQAnalysisCases
                |          Dim abqCase1 As ABQAnalysisCase
                |          Set abqCase1 =  abqCases.Add("STRUCTURAL")

        :param str i_analysis_type:
        :rtype: ABQAnalysisCase
        """
        return ABQAnalysisCase(self.abq_analysis_cases.Add(i_analysis_type))

    def item(self, i_index: cat_variant) -> ABQAnalysisCase:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ABQAnalysisCase
                | 
                |     Returns an Abaqus analysis case using its index or its name from the
                |     ABQAnalysisCases collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus analysis case to retrieve from
                |             the collection of Abaqus analysis cases. If the index is a number, it specifies
                |             the rank of the Abaqus analysis case in the collection. The index of the first
                |             Abaqus analysis case in the collection is 1, and the index of the last case is
                |             Count. If the index is a string, it specifies the name you assigned to the case
                |             using the CATIACollection::Name property. 
                | 
                |     Returns:
                |         The specified ABQIAABQAnalysisCase. 
                |     Example:
                |         This example retrieves the fifth Abaqus analysis case in the collection
                |         and saves it in a variable called ThisCase. The example also retrieves the
                |         Abaqus analysis case named "MyCase" in the collection and saves it in a
                |         variable called ThatCase.
                | 
                |          Set CaseColl = AnalysisDoc.ABQAnalysisModel.Cases
                |          Set ThisCase = CaseColl.Item(5)
                |          Set ThatCase = CaseColl.Item("MyCase")

        :param cat_variant i_index:
        :rtype: ABQAnalysisCase
        """
        return ABQAnalysisCase(self.abq_analysis_cases.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes an Abaqus analysis case using its index or its name from the
                |     collection of Abaqus analysis cases. This function works only in CAAV5 R13
                |     onwards.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus analysis case to retrieve from
                |             the collection of Abaqus analysis cases. If the index is a number, it specifies
                |             the rank of the Abaqus analysis case in the collection. The index of the first
                |             Abaqus analysis case in the collection is 1, and the index of the last analysis
                |             case is Count. If the index is a string, it specifies the name you assigned to
                |             the analysis case using the CATIABase::Name
                |             property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.abq_analysis_cases.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(abq_analysis_cases)
        # #     Dim iIndex (2)
        # #     abq_analysis_cases.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQAnalysisCases(name="{self.name}")'
