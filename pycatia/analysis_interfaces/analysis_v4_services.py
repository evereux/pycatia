#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class AnalysisV4Services(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnalysisV4Services
                | 
                | The interface to access a CATIAAnalysisV4Services.
                | 
                | This service provides tools to extract analysis information stored in V4 model
                | and session.
                | Note: The implementation of this API requires specific Licensing: V4A product
                | needs to be installed.
                | To get access to this service:
                | 
                |   Dim SAMV4Service As AnalysisV4Services 
                |   Set SAMV4Service = CATIA.GetItem("SAMV4Service")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_v4_services = com_object

    def get_storage_info(self, i_model_path: str, o_prefix: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStorageInfo(CATBSTR iModelPath,
                | CATBSTR oPrefix) As CATBSTR
                | 
                |     Gets V4 External Storage information stored in a model.
                | 
                |     Parameters:
                | 
                |         iModelPath:
                |             Path of model file.
                |         oExternal:
                |             Storage Path. 
                |         oPrefix:
                |             Directory prefix: Something like "D1998124T083802".
                |
                |     Example:
                | 
                |           This example return external storage information for a model
                |           path
                |
                |           Dim SAMV4Service As AnalysisV4Services 
                |           Set SAMV4Service = CATIA.GetItem("SAMV4Service")
                |           Dim Prefix As String 
                |           Prefix = ""
                |           Dim PathStorage As String 
                |           Dim sDocPath As String 
                |           sDocPath = "E:\\mymodel.model"
                |           PathStorage = SAMV4Service.GetStorageInfo(sDocPath,Prefix)
                |           CATIA.SystemService.Print "GetStorageInfo for Model: " &
                |           sDocPath
                |           CATIA.SystemService.Print "GetStorageInfo PathStorage: " &
                |           PathStorage & " Prefix " & Prefix

        :param str i_model_path:
        :param str o_prefix:
        :rtype: str
        """
        return self.analysis_v4_services.GetStorageInfo(i_model_path, o_prefix)

    def print_assembled_sets_info(self, i_session_path: str, i_print_path: str, i_submesh: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PrintAssembledSetsInfo(CATBSTR iSessionPath,
                | CATBSTR iPrintPath,
                | long iSubmesh)
                | 
                |     Gets sets list for a model included in a V4 Session. The generated file
                |     contains names of load, restraint, non structural mass and displacement sets
                |     for a given submesh number.
                | 
                |     Parameters:
                | 
                |         iSessionPath:
                |             Path of session file.
                |         iPrintPath:
                |             Path where to create the dump file.
                |         iSubmesh:
                |             Submesh Number of the modelo.
                |             Note that if the file already exists it will be replaced.
                |             
                | 
                |     Example:
                | 
                |           This example extract assembled sets information.
                |
                |           Dim SAMV4Service As AnalysisV4Services 
                |           Set SAMV4Service = CATIA.GetItem("SAMV4Service")
                |           Dim sSession As String 
                |           sSession = "E:\\MYSESSION.session"
                |           Dim sSumpFile As String 
                |           sSumpFile = "E:\\MyFile.txt"
                |           SAMV4Service.PrintAssembledSetsInfo sSession,sSumpFile,120

        :param str i_session_path:
        :param str i_print_path:
        :param int i_submesh:
        :rtype: None
        """
        return self.analysis_v4_services.PrintAssembledSetsInfo(i_session_path, i_print_path, i_submesh)

    def print_coupling_analysis_info(self, i_session_path: str, i_print_path: str, i_submesh: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PrintCouplingAnalysisInfo(CATBSTR iSessionPath,
                | CATBSTR iPrintPath,
                | long iSubmesh)
                | 
                |     Gets V4 Coupling analysis information.
                | 
                |     Parameters:
                | 
                |         iSessionPath:
                |             Path of the model file.
                |         iPrintPath:
                |             Path where to create the dump file.
                |         iSubmesh:
                |             Sub mesh number, the file will dump at the level of this
                |             submesh.
                |             Note that if file already exists it will be replaced.
                |
                |     Example:
                | 
                |           This example extracts sets information.
                |
                |           Dim SAMV4Service As AnalysisV4Services
                |           Set SAMV4Service = CATIA.GetItem("SAMV4Service")
                |           Dim sSession As String
                |           sSession = "E:\\MYSESSION.session"
                |           Dim sSumpFile As String
                |           sSumpFile = "E:\\MyCouplingAnalysisFile.txt"
                |           SAMV4Service.PrintCouplingAnalysisInfo sSession,sSumpFile, 120

        :param str i_session_path:
        :param str i_print_path:
        :param int i_submesh:
        :rtype: None
        """
        return self.analysis_v4_services.PrintCouplingAnalysisInfo(i_session_path, i_print_path, i_submesh)

    def print_session_info(self, i_session_path: str, i_print_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PrintSessionInfo(CATBSTR iSessionPath,
                | CATBSTR iPrintPath)
                | 
                |     Gets V4 Session information. The file is made of submesh & model name
                |     identification.
                | 
                |     Parameters:
                | 
                |         iSessionPath:
                |             Path of session file.
                |         iPrintPath:
                |             Path where to create the dump file.
                |             Note that if the file already exists it will be replaced.
                |
                |     Example:
                |
                |           This example extract session information.
                |
                |           Dim SAMV4Service As AnalysisV4Services 
                |           Set SAMV4Service = CATIA.GetItem("SAMV4Service")
                |           Dim sSession As String 
                |           sSession = "E:\\MYSESSION.session"
                |           Dim sSumpFile As String 
                |           sSumpFile = "E:\\MyFile.txt"
                |           SAMV4Service.PrintSessionInfo sSession,sSumpFile

        :param str i_session_path:
        :param str i_print_path:
        :rtype: None
        """
        return self.analysis_v4_services.PrintSessionInfo(i_session_path, i_print_path)

    def __repr__(self):
        return f'AnalysisV4Services(name="{self.name}")'
