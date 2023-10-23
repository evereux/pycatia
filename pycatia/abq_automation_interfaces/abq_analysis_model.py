#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_analysis_cases import ABQAnalysisCases
from pycatia.abq_automation_interfaces.abq_properties import ABQProperties
from pycatia.system_interfaces.any_object import AnyObject


class ABQAnalysisModel(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAnalysisModel
                | 
                | Represents the Abaqus analysis model object.
                | Role: The Abaqus analysis model object contains the ABQAnalysisCases
                | collection. The Abaqus analysis model object can also be used as an Refer:
                | CATIAAnalysisModel.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_analysis_model = com_object

    @property
    def cases(self) -> ABQAnalysisCases:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Cases() As ABQAnalysisCases (Read Only)
                | 
                |     Returns the list of Abaqus analysis cases associated with the analysis
                |     model.
                | 
                |     Returns:
                |         The collection of Abaqus analysis cases. 
                |     Example:
                |         The following example retrieves the Abaqus analysis cases collection
                |         analysisCases:
                | 
                |          Dim analysisCases As ABQAnalysisCases
                |          Dim abqModel As ABQAnalysisModel
                |          Set analysisCases = abqModel.Cases

        :rtype: ABQAnalysisCases
        """

        return ABQAnalysisCases(self.abq_analysis_model.Cases)

    @property
    def properties(self) -> ABQProperties:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Properties() As ABQProperties (Read Only)
                | 
                |     Returns the list of Abaqus properties associated with the analysis
                |     model.
                | 
                |     Returns:
                |         The collection of Abaqus properties. 
                |     Example:
                |         The following example retrieves the Abaqus properties collection
                |         properties:
                | 
                |          Dim properties As ABQProperties
                |          Dim abqModel As ABQAnalysisModel
                |          Set properties = abqModel.Properties

        :rtype: ABQProperties
        """

        return ABQProperties(self.abq_analysis_model.Properties)

    def __repr__(self):
        return f'ABQAnalysisModel(name="{self.name}")'
