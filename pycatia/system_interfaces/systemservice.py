#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:56:40.651039

from pycatia.system_interfaces.base_object import AnyObject


class SystemService(AnyObject):
    """
    .. note::
        CAA V5 Visual Basic help

            | Represents an object which provides system services.


    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.system_service = com_object

    def environ(self, i_env_string):
        """
        .. note::
            CAA V5 Visual Basic help

                | Environ
                | o Func Environ(        iEnvString) As
                | 
                | Returns the value of an environment variable.
                |
                | Parameters:
                | iEnvString
                |    The name of the environment variable

                |                | Examples:
                | This example retrieves the value of the PATH variable in the
                | Value string. Value = CATIA.SystemService.Environ("PATH")

        :param i_env_string:
        :return:
        """
        return self.system_service.Environ(i_env_string)

    def evaluate(self, i_script_text, i_language, i_function_name, i_parameters):
        """
        .. note::
            CAA V5 Visual Basic help

                | Evaluate
                | o Func Evaluate(        iScriptText,
                |                         iLanguage,
                |                         iFunctionName,
                |                         iParameters) As
                | 
                | Evaluates a scripted function.
                |
                | Parameters:
                | iScriptText
                |  The program text
                |  
                |  iLanguage
                |  The language the program is written in
                |  
                |  iFunctionName
                |  The name of the function to invoke
                |  
                |  iParameters
                |  An array of parameters for the function
                |  
                |  oResult
                |  The value returned by the function (if any)
                |
                | Examples:
                | This example executes the function CATMain from the
                | CodeToEvaluate string
                | Dim params()
                | Dim codeToEvaluate
                | CodeToEvaluate = "Sub CATMain()" & vbNewLine & _ "MsgBox " &
                | chr(34) & "Hello World" & chr(34) & vbNewLine & _ "End Sub"
                | CATIA.SystemService.Evaluate CodeToEvaluate,
                | CATVBScriptLanguage, "CATMain", params

        :param i_script_text:
        :param i_language:
        :param i_function_name:
        :param i_parameters:
        :return:
        """
        return self.system_service.Evaluate(
            i_script_text, i_language, i_function_name, i_parameters
        )

    def execute_background_processus(self, i_executable_path):
        """
        .. note::
            CAA V5 Visual Basic help

                | ExecuteBackgroundProcessus
                | o Func ExecuteBackgroundProcessus(        iExecutablePath) As
                | 
                | Executes an asynchronous process. This process is launched
                | in background and ExecuteBackgroundProcess doesn't wait for
                | it to complete. If the executable to run needs a specific
                | environment to works correctly (for example environment
                | variables like PATH or LD_LIBRARY_PATH correctly set), this
                | environment must have been set in order to make this method
                | succeed. If this executable needs to be launched from a
                | window, this method will fail.
                |
                | Parameters:
                | iExecutablePath
                |    The path of the executable to run and its arguments
                | 		If the executable is not present in the PATH environment variable, you must specify its
                |  	complete absolute path. If this path contains blanks, you must enclose it with the simple
                | 		quote character ''' : 
                | 		for example CATIA.SystemService.ExecuteBackgroundProcess "'C:\\Program Files\\myApp\\myApp.exe'
                |       myArg".
                |
                |  Returns:
                |     Non significative return code. It's never the asynchronous process return code
                |
                | Examples:
                | This example executes the command located at and doesn't
                | wait the end of its execution.
                | CATIA.SystemService.ExecuteBackgroundProcessus

        :param i_executable_path:
        :return:
        """
        return self.system_service.ExecuteBackgroundProcessus(i_executable_path)

    def execute_processus(self, i_executable_path):
        """
        .. note::
            CAA V5 Visual Basic help

                | ExecuteProcessus
                | o Func ExecuteProcessus(        iExecutablePath) As
                | 
                | Executes a synchronous process. If this process is
                | succesfully launched, ExecuteProcessus waits for it to
                | terminate and returns the process return code. If the
                | executable to run needs a specific environment to works
                | correctly (for example environment variables like PATH or
                | LD_LIBRARY_PATH correctly set), this environment must have
                | been set in order to make this method succeed. If this
                | executable needs to be launched from a window, this method
                | will fail.
                |
                | Parameters:
                | iExecutablePath
                |    The path of the executable to run and its arguments.
                |        If the executable is not present in the PATH environment variable,
                |        you must specify its complete absolute path.
                |        If this executable path contains blanks, you must enclose it with the simple quote
                |       character ''' :
                |             for example CATIA.SystemService.ExecuteProcessus "'C:\\Program Files\\myApp\\myApp.exe'
                |             myArg".
                |        On Windows, to run a batch file you must execute the command interpreter :
                |             set the executable to cmd.exe 
                |             set the arguments to the following ones : /c plus the name of the batch file. 
                |             For example CATIA.SystemService.ExecuteProcessus "cmd.exe /c E:\\MyBatchFile.bat"
                |        On Windows, an argument that contains a blank must be doubly enclosed ; first with the
                |        single quote character then,
                |             inside the single enclosing quote, with the double quote character.
                |             For example CATIA.SystemService.ExecuteProcessus "cmd.exe /c '" & Chr$(34) &
                |              "E:\\My Bat File.bat" & Chr$(34) & "'"
                |  Returns:
                |     The synchronous process return code
                |
                | Examples:
                | This example executes the command located at waits for it to
                | end, and returns its return code. ReturnCode =
                | CATIA.SystemService.ExecuteProcessus("")

        :param i_executable_path:
        :return:
        """
        return self.system_service.ExecuteProcessus(i_executable_path)

    def execute_script(
            self, i_library_name, i_type, i_program_name, i_function_name, i_parameters
    ):
        """
        .. note::
            CAA V5 Visual Basic help

                | ExecuteScript
                | o Func ExecuteScript(        iLibraryName,
                |                              iType,
                |                              iProgramName,
                |                              iFunctionName,
                |                              iParameters) As
                | 
                | Executes a scripted function.
                |
                | Parameters:
                | iLibraryName
                |  The library in which the script is contained
                |  iLibraryType
                |  The type of the library
                |  iProgramName
                |  The name of the program in the library
                |  iFunctionName
                |  The name of the function to invoke
                |  iParameters
                |  An array of parameters for the function
                |  oResult
                |  The value returned by the function (if any)
                |
                | Examples:
                | This example executes the function CATMain in the program
                | Macro1.catvbs contained by Part1.CATPart Dim params()
                | CATIA.SystemService.ExecuteScript"Part1.CATPart",
                | catScriptLibraryTypeDocument, "Macro1.catvbs", "CATMain",
                | params

        :param i_library_name:
        :param i_type:
        :param i_program_name:
        :param i_function_name:
        :param i_parameters:
        :return:
        """
        return self.system_service.ExecuteScript(
            i_library_name, i_type, i_program_name, i_function_name, i_parameters
        )

    def print(self, i_string):
        """
        .. note::
            CAA V5 Visual Basic help

                | Print
                | o Sub Print(        iString)
                | 
                | Prints a string on stdout.
                |
                | Parameters:
                | iString
                |    The string to print
                |
                | Examples:
                | This example prints the string "Hello world!".
                | CATIA.SystemService.Print("Hello world!")

        :param i_string:
        :return:
        """
        return self.system_service.Print(i_string)

    def __repr__(self):
        return f"SystemService()"
