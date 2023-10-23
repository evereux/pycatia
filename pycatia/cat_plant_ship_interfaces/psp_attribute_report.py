#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PSPAttributeReport(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspAttributeReport
                | 
                | Represents the Attribute Report.
                | Role: To generate attributes report.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_attribute_report = com_object

    def generate_report(self, i_input_format_file: str, i_outputfile: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GenerateReport(CATBSTR iInputFormatFile,
                | CATBSTR iOutputfile) As long
                | 
                |     Generate report (output format in html or CSV) and returns the status. It
                |     reports attribute data for all the selected objects in the
                |     document.
                | 
                |     Parameters:
                | 
                |         iInputFormatFile
                |             Attribute report format filename. It should contain the directory
                |             path.
                | 
                |              Note:    
                |                The format file is a text (.txt) file containing data in
                |                following
                |                order.
                |                Title=Title of the report
                |                TextFormat=HTML  or  TextFormat=CSV (Comma separated)
                |                Attrib=AttributeName likes Nominal size,EndStyle, Rating etc.
                |                Len=Integer value indicating length of attribute value
                |                and so on...
                |                Report format sample: Sample.txt
                |                Title=Piping parts report
                |                TextFormat=HTML
                |                Attrib=ID
                |                Len=15
                |                Attrib=Nominal size
                |                Len=10
                |                Attrib=Rating
                |                Len=10
                |                .... and so on  
                |
                |         iOutputfile
                |             Output filename. Full file name of the report output.
                |
                |     Returns:
                |         0 or 1. Legal values:
                |         1 : Report generation failed.
                |         0 : Report generation succeeded.
                |
                |     Example:
                |
                |          Dim objThisIntf As PspAttributeReport
                |          Dim strVar1 As CATBSTR
                |          Dim StrVar2 As CATBSTR
                |          Dim longRet    As Long
                |           ...
                |          olongRet = objThisIntf.GenerateReport (strVar1,strVar2 )

        :param str i_input_format_file:
        :param str i_outputfile:
        :rtype: int
        """
        return self.psp_attribute_report.GenerateReport(i_input_format_file, i_outputfile)

    def __repr__(self):
        return f'PSPAttributeReport(name="{self.name}")'
