#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_sensor import AnalysisSensor


class AnalysisLocalSensor(AnalysisSensor):
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
                |                             AnalysisLocalSensor
                | 
                | Represent the analysis local sensor.
                | 
                | This object is a kind of AnalysisSensor based on analysis feature
                | results
                | based on a finite element selection. This sensor definition is based on an XML
                | file
                | stored in the CATIARuntimeView.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_local_sensor = com_object

    @property
    def xml_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property XMLName() As CATBSTR
                | 
                |     Returns or sets the Identifier of the sensor as defined in the XML
                |     file.
                | 
                |     Example:
                |         This example retrieves in MyXMLName the identifier of the
                |         AnalysisSensor1 object.
                | 
                |          MyObjectName = AnalysisSensor1.XMLName

        :rtype: str
        """

        return self.analysis_local_sensor.XMLName

    @xml_name.setter
    def xml_name(self, value: str):
        """
        :param str value:
        """

        self.analysis_local_sensor.XMLName = value

    def __repr__(self):
        return f'AnalysisLocalSensor(name="{self.name}")'
