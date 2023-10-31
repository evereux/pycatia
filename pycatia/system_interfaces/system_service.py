#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SystemService(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SystemService
                | 
                | Represents an object which provides system services.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.system_service = com_object

    def environ(self, i_env_string):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func Environ(CATBSTR iEnvString) As CATBSTR
                | 
                |     Returns the value of an environment variable.
                | 
                |     Parameters:
                | 
                |         iEnvString
                |             The name of the environment variable 
                | 
                |     Example:
                |         This example retrieves the value of the PATH variable in the Value
                |         string.
                | 
                |          Value = CATIA.SystemService.Environ("PATH")

        :param str i_env_string:
        :return: str
        """
        return str(self.system_service.Environ(i_env_string))

    def evaluate(self, i_script_text: str, i_language: int, i_function_name: str, i_parameters: list):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func Evaluate(CATBSTR iScriptText,
                | CATScriptLanguage iLanguage,
                | CATBSTR iFunctionName,
                | CATSafeArrayVariant iParameters) As CATVariant
                | 
                |     Evaluates a scripted function.
                | 
                |     Parameters:
                | 
                |         iScriptText
                |             The program text 
                |         iLanguage
                |             The language the program is written in 
                |         iFunctionName
                |             The name of the function to invoke 
                |         iParameters
                |             An array of parameters for the function 
                |         oResult
                |             The value returned by the function (if any) 
                | 
                |     Example:
                |         This example executes the function CATMain from the CodeToEvaluate
                |         string
                | 
                |          Dim params()
                |          Dim codeToEvaluate
                |          CodeToEvaluate = "Sub CATMain()" & vbNewLine & _
                |                           "MsgBox " & chr(34) & "Hello World" & chr(34) &
                |                           vbNewLine & _
                |                           "End Sub"
                |          CATIA.SystemService.Evaluate CodeToEvaluate, CATVBScriptLanguage,
                |          "CATMain", params

        :param str i_script_text:
        :param int i_language: enum cat_script_language
        :param str i_function_name:
        :param list i_parameters:
        :return: None
        """
        return self.system_service.Evaluate(i_script_text, i_language, i_function_name, i_parameters)

    def execute_background_processus(self, i_executable_path):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func ExecuteBackgroundProcessus(CATBSTR iExecutablePath) As
                | long
                | 
                |     Executes an asynchronous process. This process is launched in background
                |     and ExecuteBackgroundProcess doesn't wait for it to complete. If the executable
                |     to run needs a specific environment to works correctly (for example environment
                |     variables like PATH or LD_LIBRARY_PATH correctly set), this environment must
                |     have been set in order to make this method succeed. If this executable needs to
                |     be launched from a window, this method will fail.
                | 
                |     Parameters:
                | 
                |         iExecutablePath
                |             The path of the executable to run and its arguments If the executable is not present in
                |             the PATH environment variable, you must specify its complete absolute path. If this path
                |             contains blanks, you must enclose it with the simple quote character ''' : for example
                |             CATIA.SystemService.ExecuteBackgroundProcess "'C:/Program Files/myApp/myApp.exe' myArg".
                | 
                |     Returns:
                |         Non significative return code. It's never the asynchronous process
                |         return code 
                | 
                | Example:
                |     This example executes the command located at
                | 
                |     and doesn't wait the end of its execution.
                | 
                |      CATIA.SystemService.ExecuteBackgroundProcessus ""

        :param str i_executable_path:
        :return: int
        """
        return int(self.system_service.ExecuteBackgroundProcessus(i_executable_path))

    def execute_processus(self, i_executable_path):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func ExecuteProcessus(CATBSTR iExecutablePath) As long
                | 
                |     Executes a synchronous process. If this process is succesfully launched,
                |     ExecuteProcessus waits for it to terminate and returns the process return code.
                |     If the executable to run needs a specific environment to works correctly (for
                |     example environment variables like PATH or LD_LIBRARY_PATH correctly set), this
                |     environment must have been set in order to make this method succeed. If this
                |     executable needs to be launched from a window, this method will
                |     fail.
                | 
                |     Parameters:
                | 
                |         iExecutablePath
                |             The path of the executable to run and its arguments. If the executable is not present in
                |             the PATH environment variable, you must specify its complete absolute path. If this
                |             executable path contains blanks, you must enclose it with the simple quote
                |             character ''' to allow the implementation to follow the whole line to the MS call
                |             (otherwise only the last part will be sent to the MS call) : Additionally, arguments
                |             with blank must be enclosed in double quote in Microsoft call (do not forget to espace
                |             double quote in VBA, with another double quote).
                |             for example CATIA.SystemService.ExecuteProcessus("'""C:/Program Files/myApp/myApp.exe""'
                |                  myArg1 '""myAr g2""'")
                |             will start the command line "C:/Program Files/myApp/myApp.exe" myArg1 "myAr g2"
                |             on Microsoft OS. On Windows, to run a batch file you must execute the command interpreter
                |             : set the executable to cmd.exe set the arguments to the following ones
                |             : /c plus the name of the batch file. For example CATIA.SystemService.ExecuteProcessus
                |             "cmd.exe /c E:/MyBatchFile.bat" On Windows, an argument that contains a blank must be
                |             doubly enclosed ; first with the single quote character then, inside the single enclosing
                |             quote, with the double quote character. For example CATIA.SystemService.ExecuteProcessus
                |             "cmd.exe /c '" & Chr$(34) & "E:/My Bat File.bat" & Chr$(34) & "'"
                | 
                |     Returns:
                |         The synchronous process return code 
                | 
                | Example:
                |     This example executes the command located at
                | 
                |     waits for it to end, and returns its return code.
                | 
                |      ReturnCode = CATIA.SystemService.ExecuteProcessus("")

        :param str i_executable_path:
        :return: int
        """
        return int(self.system_service.ExecuteProcessus(i_executable_path))

    def execute_script(
            self,
            i_library_name: str,
            i_type: int,
            i_program_name: str,
            i_function_name: str,
            i_parameters: list
    ):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func ExecuteScript(CATBSTR iLibraryName,
                | CatScriptLibraryType iType,
                | CATBSTR iProgramName,
                | CATBSTR iFunctionName,
                | CATSafeArrayVariant iParameters) As CATVariant
                | 
                |     Executes a scripted function.
                | 
                |     Parameters:
                | 
                |         iLibraryName
                |             The library in which the script is contained 
                |         iLibraryType
                |             The type of the library 
                |         iProgramName
                |             The name of the program in the library 
                |         iFunctionName
                |             The name of the function to invoke 
                |         iParameters
                |             An array of parameters for the function 
                |         oResult
                |             The value returned by the function (if any) 
                | 
                |     Example:
                |         This example executes the function CATMain in the program Macro1.catvbs
                |         contained by Part1.CATPart
                | 
                |          Dim params()
                |          CATIA.SystemService.ExecuteScript"Part1.CATPart",
                |          catScriptLibraryTypeDocument, "Macro1.catvbs", "CATMain",
                |          params

        :param str i_library_name:
        :param int i_type: enum cat_script_library_type
        :param str i_program_name:
        :param str i_function_name:
        :param tuple i_parameters:
        :return: None
        """
        return self.system_service.ExecuteScript(i_library_name, i_type, i_program_name, i_function_name, i_parameters)

    def print(self, i_string):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub Print(CATBSTR iString)
                | 
                |     Prints a string on stdout.
                | 
                |     Parameters:
                | 
                |         iString
                |             The string to print 
                | 
                |     Example:
                |         This example prints the string "Hello world!".
                | 
                |          CATIA.SystemService.Print("Hello world!")

        :param str i_string:
        :return: None
        """
        return self.system_service.Print(i_string)

    def __repr__(self):
        return f'SystemService(name="{self.name}")'
