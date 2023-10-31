#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_sensor import AnalysisSensor


class AnalysisGlobalSensor(AnalysisSensor):
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
                |                         CATAnalysisInterfaces.AnalysisSensor
                |                             AnalysisGlobalSensor
                | 
                | Represent the analysis global sensor.
                | 
                | This object is a kind of AnalysisSensor based on analysis feature global
                | results. For example, extract the Energy value of a solution.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_global_sensor = com_object

    def get_identifier(self, o_type_bstr: str, o_sub_type_bstr: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetIdentifier(CATBSTR oTypeBSTR,
                | CATBSTR oSubTypeBSTR)
                | 
                |     Retreives the Physical type and sub physical type that will be computed by
                |     the sensor.
                | 
                |     Parameters:
                | 
                |         oTypeBSTR
                |             The physical type identifier. 
                |         oSubTypeBSTR
                |             The "sub" physical type identifier.

        :param str o_type_bstr:
        :param str o_sub_type_bstr:
        :rtype: None
        """
        return self.analysis_global_sensor.GetIdentifier(o_type_bstr, o_sub_type_bstr)

    def set_identifier(self, i_type_bstr: str, i_sub_type_bstr: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetIdentifier(CATBSTR iTypeBSTR,
                | CATBSTR iSubTypeBSTR)
                | 
                |     Sets the Physical type and sub physical type that will be computed by the
                |     sensor.
                | 
                |     Parameters:
                | 
                |         iTypeBSTR
                |             The physical type identifier. 
                |         iSubTypeBSTR
                |             The "sub" physical type identifier.

        :param str i_type_bstr:
        :param str i_sub_type_bstr:
        :rtype: None
        """
        return self.analysis_global_sensor.SetIdentifier(i_type_bstr, i_sub_type_bstr)

    def __repr__(self):
        return f'AnalysisGlobalSensor(name="{self.name}")'
