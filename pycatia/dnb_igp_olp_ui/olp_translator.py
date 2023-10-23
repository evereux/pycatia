#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_igp_setup_interfaces.robot_task import RobotTask
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class OLPTranslator(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OLPTranslator
                | 
                | Represents the Offline Programming Translator object.
                | Role: Interface dedicated to downloading or uploading robot or device tasks and
                | formatting the output in the specified native robot language.
                | 
                | This object can be retrieved by querying on a Robot. For
                | example:
                | 
                |  Dim SelectionObject as Selection
                |  Dim RobotObject As Product
                |  Dim OLPTranslatorObject as OLPTranslator
                |  Set SelectionObject = DELMIA.ActiveDocument.Selection
                |  Set RobotObject = SelectionObject.Item2(1).Value
                |  Set OLPTranslatorObject = RobotObject.GetTechnologicalObject("OLPTranslator")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.olp_translator = com_object

    def convert_nrl_to_xml(self, i_nrl_file_name: str, i_parser_name: str, o_xml_file_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ConvertNRLToXML(CATBSTR iNRLFileName,
                | CATBSTR iParserName,
                | CATBSTR oXMLFileName)
                | 
                |     Converts NRL Program to OLP XML upload file
                | 
                |     Parameters:
                | 
                |         iNRLFileName
                |             Input NRL Robot program file. 
                |         iParserName
                |             Path to Robot program parser.
                |             Legal values:
                | 
                |                 Java parser packaged as Jar
                |                 A native parser packaged as an executable
                | 
                |         oXMLFileName
                |             Target XML output file

        :param str i_nrl_file_name:
        :param str i_parser_name:
        :param str o_xml_file_name:
        :rtype: None
        """
        return self.olp_translator.ConvertNRLToXML(i_nrl_file_name, i_parser_name, o_xml_file_name)

    def convert_xml_to_nrl(self, i_xml_file_name: str, i_xslt_file_name: str, o_nrl_target_folder: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ConvertXMLToNRL(CATBSTR iXMLFileName,
                | CATBSTR iXSLTFileName,
                | CATBSTR oNRLTargetFolder)
                | 
                |     Converts OLP XML download file to NRL Program
                | 
                |     Parameters:
                | 
                |         iXMLFileName
                |             Input XML file. 
                |         iXSLTFileName
                |             Translator file name 
                |         oNRLTargetFolder
                |             Target folder where the robot programs will be saved. Name of the
                |             program files will be auto generated.

        :param str i_xml_file_name:
        :param str i_xslt_file_name:
        :param str o_nrl_target_folder:
        :rtype: None
        """
        return self.olp_translator.ConvertXMLToNRL(i_xml_file_name, i_xslt_file_name, o_nrl_target_folder)

    def download_as_xml(
            self,
            i_robot_task: RobotTask,
            o_xml_file_name: str,
            i_is_part_coordinates: bool,
            i_is_simulated: bool,
            i_is_sub_routines: bool
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub DownloadAsXML(RobotTask iRobotTask,
                | CATBSTR oXMLFileName,
                | boolean iIsPartCoordinates,
                | boolean iIsSimulated,
                | boolean iIsSubRoutines)
                | 
                |     Downloads a Robot task as XML file
                | 
                |     Parameters:
                | 
                |         iRobotTask
                |             The robot task to download 
                |         oXMLFileName
                |             Name of XML file to be generated 
                |         iIsPartCoordinates
                |             if TRUE, the robot task will be downloaded in part coordinates of
                |             iPart if FALSE, the robot task will be downloaded in robot base coordinates
                |             
                |         iIsSimulated
                |             if TRUE, Download will be simulation verified 
                |         iIsSubRoutines
                |             if TRUE, XML will have tags marking call tasks for download as
                |             subroutines in main program file if FALSE, XML will have tags marking call
                |             tasks for download as separate files

        :param RobotTask i_robot_task:
        :param str o_xml_file_name:
        :param bool i_is_part_coordinates:
        :param bool i_is_simulated:
        :param bool i_is_sub_routines:
        :rtype: None
        """
        return self.olp_translator.DownloadAsXML(
            i_robot_task.com_object,
            o_xml_file_name,
            i_is_part_coordinates,
            i_is_simulated,
            i_is_sub_routines
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'download_as_xml'
        # # vba_code = """
        # # Public Function download_as_xml(olp_translator)
        # #     Dim iRobotTask (2)
        # #     olp_translator.DownloadAsXML iRobotTask
        # #     download_as_xml = iRobotTask
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def download_tasks(
            self,
            l_list_of_tasks: tuple,
            s_path_to_xslt_translator: str,
            s_context: str,
            b_is_part_coordinates: bool,
            b_is_subroutine: bool,
            s_log_file_name: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub DownloadTasks(CATSafeArrayVariant lListOfTasks,
                | CATBSTR sPathToXSLTTranslator,
                | CATBSTR sContext,
                | boolean bIsPartCoordinates,
                | boolean bIsSubroutine,
                | CATBSTR sLogFileName)
                | 
                |     Creates native robot language programs from V5 tasks. First the V5 Robot
                |     Offline Programming XML is generated for the given robot or device tasks in
                |     non-simulation mode. Then the XML file is supplied to the XSLT translator to
                |     create output in the corresponding native robot language.
                |     Role: Used to translate specified robot/device tasks to native robot
                |     language program(s). It is responsibility of specified xslt translator to
                |     provide the mechanism for saving its output to one or more
                |     files.
                | 
                |     Parameters:
                | 
                |         lListOfTasks
                |             List of robot or list of device tasks to download 
                |         sPathToXSLTTranslator
                |             Absolute path to XSLT translator (downloader).If this is an empty
                |             string, no XSLT translation will be done, and only OLP XML file will be
                |             created. 
                |         sContext
                |             Value that defines a context in which an XSLT translator works.
                |             This tells the translator how to format the output. Internally, the XSLT
                |             translator should have a mechanism in place on how to format its output based
                |             on this value. This value is user defined and it may impact user developed
                |             downloaders as well as RRS2 custom created downloaders. Any value of this
                |             parameter, rather the supplied default value, will be assigned to the "Context"
                |             attribute of the "OLPData" XML element. Translators should check whether the
                |             "Context" attribute exists in the "OLPData" XML element, and if it does, they
                |             should redirect the XSLT output accordingly. If the attribute does not exist,
                |             which means that the translator has been invoked during execution of "Create
                |             Robot Program" interactive command, then the translators should use OLP section
                |             markers in order to display their output in V5.
                | 
                |             Here are the section marker rules that need to be strictly
                |             followed: It is important that the entire robot program output, designated to
                |             be saved in a particular file, is enclosed between DATA FILE START and DATA
                |             FILE END markers. Translator output without any DATA FILE START and DATA FILE
                |             END elements will be displayed in one tab page, generically named "Program.1".
                |             If translator output has DATA FILE START and DATA FILE END elements (multiple
                |             pairs),but without , each enclosed section of the output will go into a
                |             separate tab page named "Program.1", "Program.2",
                |             etc.
                | 
                |             Every downloader should use ERROR INFO START ERROR INFO END
                |             elements to store any error messages, in order to display them in the
                |             information text box of Download Editor.
                | 
                |             As with error messages, release and version information will be
                |             copied from the output's VERSION INFO START VERSION INFO END markers and will
                |             be displayed in the information text box of Download
                |             Editor.
                | 
                |             All of the marker elements need to start at the beginning of a new
                |             line and to end with a new line character. The examples are
                |             below:
                | 
                |             DATA FILE START myProgram.1 ... DATA FILE END
                | 
                |             VERSION INFO START Delmia Corp. NachiAX Uploader Version 5 Release
                |             15. Copyright Delmia Corp. 1986-2003, All Rights Reserved. VERSION INFO
                |             END
                | 
                |             ERROR INFO START The error occurred during translation of Motion.1
                |             activity ERROR INFO END 
                |         bIsPartCoordinates
                |             Flag that signifies whether the download of the tasks should be in
                |             Part or Robot Base coordinates (important for a robot motion activity only).
                |             
                |         bIsSubroutine
                |             Flag that signifies whether a called Robot Task (important for call
                |             task activities only) should be downloaded as a subroutine of a main robot
                |             program, or as a separate program contained in a separate file.
                |             
                |         sLogFileName
                |             Name of the log file that an XSLT translator can use to write data
                |             to. An empty string signifies that log file is not needed. It is important to
                |             note that this is just a file name, not an absolute path to that file. This log
                |             file is supposed to be saved to a directory which is a descendant of a
                |             downloader root directory. Downloader root directory is defined in the XML
                |             through the "DownloaderRootDirectory" attribute of the "OLPData" XML
                |             element.

        :param tuple l_list_of_tasks:
        :param str s_path_to_xslt_translator:
        :param str s_context:
        :param bool b_is_part_coordinates:
        :param bool b_is_subroutine:
        :param str s_log_file_name:
        :rtype: None
        """
        return self.olp_translator.DownloadTasks(
            l_list_of_tasks,
            s_path_to_xslt_translator,
            s_context,
            b_is_part_coordinates,
            b_is_subroutine,
            s_log_file_name
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'download_tasks'
        # # vba_code = """
        # # Public Function download_tasks(olp_translator)
        # #     Dim lListOfTasks (2)
        # #     olp_translator.DownloadTasks lListOfTasks
        # #     download_tasks = lListOfTasks
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_robot_program_directory(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRobotProgramDirectory() As CATBSTR
                | 
                |     Retrieves the OLP Directory setting parameter value.
                |     Role: The OLP Directory setting parameter stores the full file path to
                |     directory where native robot language programs will be
                |     stored.
                | 
                |     Returns:
                |         The OLP Directory setting parameter value

        :rtype: str
        """
        return self.olp_translator.GetRobotProgramDirectory()

    def get_xml_file_directory(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetXMLFileDirectory() As CATBSTR
                | 
                |     Retrieves the XML Directory setting parameter value.
                |     Role: The XML Directory setting parameter stores the full file path to
                |     directory where OLP XML file created on download is stored. By default, OLP XML
                |     file name is simResult.xml.
                | 
                |     Returns:
                |         The XML Directory setting parameter value

        :rtype: str
        """
        return self.olp_translator.GetXMLFileDirectory()

    def upload_from_xml(
            self,
            i_robot_task: RobotTask,
            i_xml_file_name: str,
            i_is_part_coordinates: bool,
            i_part: Product
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UploadFromXML(RobotTask iRobotTask,
                | CATBSTR iXMLFileName,
                | boolean iIsPartCoordinates,
                | Product iPart)
                | 
                |     Upload a Robot task from XML file
                | 
                |     Parameters:
                | 
                |         iRobotTask
                |             Robot task to upload 
                |         iXMLFileName
                |             Name of source XML file 
                |         iIsPartCoordinates
                |             if TRUE, Robot task will be uploaded in part coordinates of iPart
                |             if FALSE, Robot task will be uploaded in robot base coordinates
                |             
                |         iPart
                |             Part in whose coordinates the program will be
                |             uploaded

        :param RobotTask i_robot_task:
        :param str i_xml_file_name:
        :param bool i_is_part_coordinates:
        :param Product i_part:
        :rtype: None
        """
        return self.olp_translator.UploadFromXML(
            i_robot_task.com_object,
            i_xml_file_name,
            i_is_part_coordinates,
            i_part.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'upload_from_xml'
        # # vba_code = """
        # # Public Function upload_from_xml(olp_translator)
        # #     Dim iRobotTask (2)
        # #     olp_translator.UploadFromXML iRobotTask
        # #     upload_from_xml = iRobotTask
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def upload_robot_program(
            self,
            sp_i_selected_robot: Product,
            s_path_to_robot_program_file: str,
            s_path_to_uploader_file: str,
            b_is_upload_in_part_coords: bool
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UploadRobotProgram(Product spISelectedRobot,
                | CATBSTR sPathToRobotProgramFile,
                | CATBSTR sPathToUploaderFile,
                | boolean bIsUploadInPartCoords)
                | 
                |     Creates robot or device tasks in V5 based from native robot language
                |     program file or an OLP XML file.
                |     Role: To be used to create specified robot/device tasks from native robot
                |     language program file(s) or from OLP XML file.
                | 
                |     Parameters:
                | 
                |         spISelectedRobot
                |             Robot or Move-By-Joint Device, which will own all the uploaded
                |             robot or device tasks 
                |         sPathToRobotProgramFile
                |             Absolute path to a native robot language (NRL) program file or an
                |             absolute path to OLP XML file to be uploaded 
                |         sPathToUploaderFile
                |             Absolute path to OLP uploader file. If this is specified as an
                |             empty string, the previous parameter must point to an OLP XML file. If this
                |             string is not empty, the previous parameter must point to an NRL program file.
                |             
                |         bIsUploadInPartCoords
                |             Flag that signifies whether the upload of robot programs(s) or XML
                |             file should be in Part or Robot Base coordinates (important for robot motion
                |             activities only).

        :param Product sp_i_selected_robot:
        :param str s_path_to_robot_program_file:
        :param str s_path_to_uploader_file:
        :param bool b_is_upload_in_part_coords:
        :rtype: None
        """
        return self.olp_translator.UploadRobotProgram(
            sp_i_selected_robot.com_object,
            s_path_to_robot_program_file,
            s_path_to_uploader_file,
            b_is_upload_in_part_coords
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'upload_robot_program'
        # # vba_code = """
        # # Public Function upload_robot_program(olp_translator)
        # #     Dim spISelectedRobot (2)
        # #     olp_translator.UploadRobotProgram spISelectedRobot
        # #     upload_robot_program = spISelectedRobot
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'OLPTranslator(name="{self.name}")'
