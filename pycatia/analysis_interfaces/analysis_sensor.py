#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_entity import AnalysisEntity
from pycatia.knowledge_interfaces.parameters import Parameters


class AnalysisSensor(AnalysisEntity):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATAnalysisInterfaces.AnalysisEntity
                |                         AnalysisSensor
                | 
                | Represent the analysis sensor.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_sensor = com_object

    @property
    def out_put_parameters(self) -> Parameters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OutPutParameters() As Parameters (Read Only)
                | 
                |     Returns the collection object containing the sensor
                |     parameters.
                | 
                |     Example:
                |         The following example returns in params the parameters computed by the
                |         sensor:
                | 
                |          Dim AnalysisSensor1 As AnalysisSensor
                |          Dim params As CATIAParameters
                |          Set params = AnalysisSensor1.OutPutParameters

        :rtype: Parameters
        """

        return Parameters(self.analysis_sensor.OutPutParameters)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Update()
                | 
                |     Update the sensor. Computation of OutPutParameters if
                |     needed.
                | 
                |     Example:
                |         The following example computes the sensor:
                | 
                |          Dim AnalysisSensor1 As AnalysisSensor
                |          AnalysisSensor1.Update

        :rtype: None
        """
        return self.analysis_sensor.Update()

    def __repr__(self):
        return f'AnalysisSensor(name="{self.name}")'
