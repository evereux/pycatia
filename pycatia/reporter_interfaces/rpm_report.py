#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class RpmReport(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RpmReport

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rpm_report = com_object

    def generate_report(self, i_xml_file_name: str, i_report_file_name: str, i_report_type: str, i_out_dtd_file_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GenerateReport(CATBSTR iXMLFileName,
                | CATBSTR iReportFileName,
                | CATBSTR iReportType,
                | CATBSTR iOutDTDFileName)
                | 
                |     This method generates a report to an output file. The definition of the
                |     report content is specified by an input XML file.
                | 
                |     Parameters:
                | 
                |         iXMLFileName
                |             XML file name for report definition. 
                |         iReportFileName
                |             The file name to output the report to. 
                |         iReportType
                |             The report type. The following list represents acceptable values:
                |             "Web Page (*.htm)" "Text (*.txt)" "Text (Tab delimited) (*.txt)" "CSV (Comma
                |             delimited) (*.csv)" "XML (*.xml)" "Excel Workbook (*.xls)"
                |             
                |         iOutDTD
                |             If iReportType is an XML file, then a .dtd file name is needed.
                |             Else send in a null string.

        :param str i_xml_file_name:
        :param str i_report_file_name:
        :param str i_report_type:
        :param str i_out_dtd_file_name:
        :rtype: None
        """
        return self.rpm_report.GenerateReport(i_xml_file_name, i_report_file_name, i_report_type, i_out_dtd_file_name)

    def __repr__(self):
        return f'RpmReport(name="{ self.name }")'
