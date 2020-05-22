#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25

from pathlib import Path

from pycatia.system_interfaces.base_object import AnyObject
from pycatia.in_interfaces.document import Document
from pycatia.in_interfaces.documents import Documents


class Application(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the current CNext application and its frame window.The
                | application is the root object for all the other objects you can use
                | and access from scripts. It directly aggregates.

    """

    def __init__(self, com_object):
        super().__init__(com_object)

    @property
    def active_document(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ActiveDocument
                | o Property ActiveDocument(    ) As   (Read Only)
                | 
                | Returns the active document. The active document is the document the
                | end user is being editing.
                | Example:
                | This example retrieves in ActiveDoc the active document of the CATIA application.
                | Dim ActiveDoc As Document
                | Set ActiveDoc = CATIA.ActiveDocument

        :return: Document()
        """
        return Document(self.application.ActiveDocument)

    @property
    def active_printer(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ActivePrinter
                | o Property ActivePrinter(    ) As Printer
                | 
                | Returns or sets the active printer. The active printer is the printer
                | on which documents are printed
                | Example:
                | This example retrieves in ActivePrinter the active printer of the CATIA application.
                | Dim ActivePrinter As Printer
                | Set ActivePrinter = CATIA.ActivePrinter

        :return:
        """
        return self.application.ActivePrinter

    @property
    def active_window(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ActiveWindow
                | o Property ActiveWindow(    ) As Window   (Read Only)
                | 
                | Returns the active window. The active window is the window in which
                | the end user is currently editing the active document.
                |
                | Example:
                | This example retrieves in ActiveWin the active window of the CATIA
                | application.
                | Dim ActiveWin As Window
                | Set ActiveWin = CATIA.ActiveWindow

        :return:
        """
        return self.application.ActiveWindow

    @property
    def cache_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CacheSize
                | o Property CacheSize(    ) As
                | 
                | Returns or sets the default local cache size used by the application.
                |
                | Example:
                | This example sets the cache size for by the CATIA application
                | to those defined in LocalCacheSize.
                | LocalCacheSize = 10
                | CATIA.CacheSize = LocalCacheSize

        :return:
        """
        return self.application.CacheSize

    @property
    def caption(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Caption
                | o Property Caption(    ) As
                | 
                | Returns or sets the application's window title. This title is
                | displayed in the application's window title bar.
                |
                | Example:
                | This example retrieves in Title the CATIA application's window title.
                | Title = CATIA.Caption
                | The returned value is like this:
                | CNext

        :return: str
        """
        return self.application.Caption

    @property
    def display_file_alerts(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DisplayFileAlerts
                | o Property DisplayFileAlerts(    ) As
                | 
                | Returns or sets the application ability to display file alerts. True
                | if the application enables file alert display.  True is the default. A
                | file alert is, for example, the dialog box that prompts you that the
                | file you want to save is in read only mode, or that the file you want
                | to close needs to be saved. It could be handy to disable these file
                | alerts for automation since they may freeze your macro execution,
                | waiting for an end user input in the  displayed dialog box.
                |
                | Example:
                | This example disables file alerts for the CATIA application.
                | CATIA.DisplayFileAlerts = False

        :return: bool
        """
        return self.application.DisplayFileAlerts

    @property
    def documents(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Documents
                | o Property Documents(    ) As   (Read Only)
                | 
                | Returns the collection of documents currently managed by the
                | application.
                |
                | Example:
                | This example retrieves in DocCollection the collection of documents
                | currently managed by the CATIA application.
                | Dim DocCollection As Documents
                | Set DocCollection = CATIA.Documents

        :return: Documents()
        """
        return Documents(self.application.Documents)

    @property
    def file_search_order(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FileSearchOrder
                | o Property FileSearchOrder(    ) As CATBSTR
                | 
                | Returns or sets the default path concatenation. Role: This property
                | returns or sets the default path concatenation used by Other folders
                | setting of the Linked Documents Localization function.      The
                | primary aim of the Linked Documents Localization function is to
                | resolve document links and to manage the strategy that will be used to
                | locate your linked documents.
                |
                | Example:
                | This example sets the paths to
                | search for by the CATIA application to those defined in
                | PathConcatenation.
                | PathConcatenation = "/u/users/fbq/db/model:/u/users/psr/db/model"
                | CATIA.FileSearchOrder = PathConcatenation
                |
                | These methods require the installation of CATIA -
                | PPR xPDM Gateway 1 Product (PX1) In case this product is not granted,
                | the first invocation to one of the methods will fail.

        :return: str
        """
        return self.application.FileSearchOrder

    @property
    def file_system(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FileSystem
                | o Property FileSystem(    ) As FileSystem  (Read Only)
                | 
                | Returns the file system. The file system provides access to a
                | computer's file system.
                |
                | Example: This example retrieves in AppliFileSys the file system of the CATIA application.
                | Dim AppliFileSys As FileSystem
                | Set AppliFileSys = CATIA.FileSystem

        :return:
        """
        return self.application.FileSystem

    @property
    def full_name(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FullName
                | o Property FullName(    ) As   (Read Only)
                | 
                | Returns the application's executable file full name, including its
                | path. This name is the name of the executable file used to start the
                | application.
                |
                | Example: This example retrieves in ApplicationFullName
                | the CATIA application's executable file full name.
                | ApplicationFullName = CATIA.FullName
                | The returned value is like this:
                | \\lisa\\cxr1arel\\bsf\\alpha_a\\code\\bin\\CNEXT.exe


        :return: str
        """
        return self.application.FullName

    @property
    def hso_synchronized(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HSOSynchronized
                | o Property HSOSynchronized(    ) As
                | 
                | For selection performance purposes, returns or sets the HSO
                | synchronization in comparison with the CSO. Role: Precises if, for all
                | object instances, the HSO (Highlighted Set of Objects) is synchronized
                | in comparison with the CSO (Current Set of Objects). Valid values
                | are:True: In this case, Selection methods work directly with CATIA's
                | CSO, to reflect instantly the changes made in Automation Selection.
                | This ensures correct selection results, but may impact performance in
                | certain cases. This is the default value at the beginning of a CATIA
                | session. False: In this case, Selection methods work with an internal
                | SO buffer, which allows faster execution when performing a large
                | number of CSO-independent Selection calls, or when performing a single
                | Selection call working on a large number of objects (usually the
                | Search method). This may also prevent the features from blinking
                | between two user interactions.Note: even if this property is set to
                | False, the HSO is synchronized in comparison with the CSO at the
                | beginning of the following methods: Selection.SelectElement2Selection.S
                | electElement3Selection.SelectElement4Selection.IndicateOrSelectElement
                | 2DSelection.IndicateOrSelectElement3DApplication.StartCommandCAUTION:
                | If you use the False value of this property, you must make sure to
                | reset it to True for CATIA's CSO to reflect properly the changes made
                | in Automation Selection. For example, it should be reset to True
                | before interactive parts of your script: MsgBox, InputBox calls, VBA
                | forms updates and so on.

        :return:
        """
        return self.application.HSOSynchronized

    @property
    def height(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Height
                | o Property Height(    ) As
                | 
                | Returns or sets the height of the application's frame window. The
                | height is expressed in pixels.
                |
                | Example: This example sets the height of the CATIA application's frame window to 300 pixels.
                | CATIA.Height = 300

        :return:
        """
        return self.application.Height

    @height.setter
    def height(self, value):
        self.application.Height = value

    @property
    def interactive(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Interactive
                | o Property Interactive(    ) As
                | 
                | Returns or sets the application sensitivity to end user interactions.
                | True if the application is end user interaction sensitive.  Example:
                | This example makes the CATIA application sensitive to end user
                | interactions.  CATIA.Interactive = True

        :return: bool
        """
        return self.application.Interactive

    @interactive.setter
    def interactive(self, value):
        self.application.Interactive = value

    @property
    def left(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Left
                | o Property Left(    ) As
                | 
                | Returns or sets the distance from the application's frame window left
                | side to the left side of the screen. This distance is expressed in
                | pixels.
                |
                | Example:
                | This example sets the distance from the CATIA application's frame window
                | left side to the left side of the screen to 150 pixels.
                | CATIA.Left = 150

        :return: float
        """
        return self.application.Left

    @left.setter
    def left(self, value):
        self.application.Left = value

    @property
    def local_cache(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | LocalCache
                | o Property LocalCache(    ) As
                | 
                | Returns or sets the default local cache path used by the application.
                | Example: This example sets the cache path for by the CATIA application
                | to those defined in LocalCachePath.  LocalCachePath= "/tmp/cache"
                | CATIA.LocalCache = LocalCachePath

        :return: str
        """
        return self.application.LocalCache

    @local_cache.setter
    def local_cache(self, value):
        self.application.LocalCache = value

    @property
    def path(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Path
                | o Property Path(    ) As   (Read Only)
                | 
                | Returns the path of the application's executable files.
                |
                | Example: This example retrieves in ApplicationPath the path where the CATIA
                | application executable files are located.
                | ApplicationPath = CATIA.Path
                | The returned value is like this:
                | \\lisa\\cxr1arel\\bsf\\alpha_a\\code\\bin

        :return: Path()
        """
        return Path(self.application.Path)

    @property
    def printers(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Printers
                | o Property Printers(    ) As   (Read Only)
                | 
                | Returns the collection of the printers currently managed by the
                | application.
                |
                | Example:
                | This example retrieves in PrintersCollection the
                | collection of the printers currently managed by the CATIA application.
                | Dim PrintersCollection As Windows
                | Set PrintersCollection = CATIA.Printers

        :return:
        """
        return self.application.Printers

    @property
    def refresh_display(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RefreshDisplay
                | o Property RefreshDisplay(    ) As
                | 
                | Enables or disables the update of the display during the script
                | replay. To improve performance, this update can be temporarily
                | disabled by setting  this property to False in the script. True (value
                | set by default) if the application's display is refreshed after each
                | method call  executed in late binding mode . This property does not
                | affect early binding calls nor the get methods because they are never
                | followed  by a refresh of the display.
                |
                | Example: This example makes the update of the CATIA application's display
                | disabled during the script replay.
                | CATIA.RefreshDisplay = False

        :return: bool
        """
        return self.application.RefreshDisplay

    @refresh_display.setter
    def refresh_display(self, value):
        self.application.RefreshDisplay = value

    @property
    def status_bar(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | StatusBar
                | o Property StatusBar(    ) As
                | 
                | Returns or sets the text displayed in the application's window status
                | bar.
                |
                | Example: This example retrieves in Text the text displayed in
                | the CATIA application's window status bar.
                | Text = CATIA.StatusBar
                | The returned value is like this:
                | Welcome to CATIA CxR1

        :return: str
        """
        return self.application.StatusBar

    @status_bar.setter
    def status_bar(self, value):
        self.application.StatusBar = value

    @property
    def system_configuration(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SystemConfiguration
                | o Property SystemConfiguration(    ) As   (Read Only)
                | 
                | Returns the system configuration object (an object which provides
                | access to system or configuration dependent resources).
                |
                | Parameters:
                | oConfiguration
                |  The system configuration object.

        :return:
        """
        return self.application.SystemConfiguration

    @property
    def system_service(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SystemService
                | o Property SystemService(    ) As   (Read Only)
                | 
                | Returns system services. Example: This example retrieves in
                | AppliSysSer the CATIA application's system services.  Dim AppliSysSer
                | As SystemService Set AppliSysSer = CATIA.SystemService

        :return:
        """
        return self.application.SystemService

    @property
    def top(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Top
                | o Property Top(    ) As
                | 
                | Returns or sets the distance from the application'si frame window top
                | to the top of the screen. This distance is expressed in pixels.
                |
                | Example:
                | This example sets the distance from the CATIA  application's
                | frame window top to the top of the screen to 50 pixels.
                | CATIA.Top = 50

        :return: float
        """
        return self.application.Top

    @top.setter
    def top(self, value):
        self.application.Top = value

    @property
    def undo_redo_lock(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UndoRedoLock
                | o Property UndoRedoLock(    ) As
                | 
                | Returns or sets the application status about Undo/Redo. True if the
                | Undo/Redo mechanism is locked.  False is the default. Since Undo/Redo
                | mechanism uses lots of memory, it can be useful to disable it during
                | consuming operations. Then Undo and Redo stacks are flushed and no
                | model modification is kept until the Undo/Redo mechanism is unlocked.
                | It is mandatory to unlock it before the end of the macro.
                |
                | Example:
                | This example disables Undo/Redo mechanism until it is unlocked.
                | CATIA.UndoRedoLock = True

        :return: bool
        """
        return self.application.UndoRedoLock

    @undo_redo_lock.setter
    def undo_redo_lock(self, value):
        self.application.UndoRedoLock = value

    @property
    def visible(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Visible
                | o Property Visible(    ) As
                | 
                | Returns or sets the application's window visibility. True if the
                | application's window is visible to the end user.
                |
                | Example: This
                | example makes the CATIA application's window visible.
                | CATIA.Visibility = True

        :return: bool
        """
        return self.application.Visible

    @visible.setter
    def visible(self, value):
        """
        :param bool value:
        """
        self.application.Visible = value

    @property
    def width(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Width
                | o Property Width(    ) As
                | 
                | Returns or sets the width of the application's frame window. The width
                | is expressed in pixels.
                |
                | Example:
                | This example sets the width of the CATIA application's frame window to 350 pixels.
                | CATIA.Width = 350

        :return: int
        """
        return self.application.Width

    @width.setter
    def width(self, value):
        self.application.width = value

    @property
    def windows(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Windows
                | o Property Windows(    ) As   (Read Only)
                | 
                | Returns the collection of windows currently managed by the
                | application.
                | Example:
                | This example retrieves in WinCollection the
                | collection of windows currently managed by the CATIA application.
                | Dim WinCollection As Windows
                | Set WinCollection = CATIA.Windows

        :return:
        """
        return self.application.Windows

    def create_send_to(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateSendTo
                | o Func CreateSendTo(    ) As
                | 
                | Creates a Send TO.  Role:This method creates a  instance. Warning :
                | CATIASendToService interface requires  the installation of CATIA - PPR
                | xPDM Gateway 1 Product (PX1) In case this product is not granted, the
                | first invocation to one of CATIASendToService methods will fail.

        :return:
        """
        return self.application.CreateSendTo()

    def disable_new_undo_redo_transaction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DisableNewUndoRedoTransaction
                | o Sub DisableNewUndoRedoTransaction(    )
                | 
                | Prevents new Undo/Redo transaction creation.  If too many Undo/Redo
                | transactions are created during macro execution, it may affect
                | performance. So it is valuable to prevent Undo/Redo transaction
                | creation during macro execution when lots of data are created, deleted
                | or modified. Note: preventing Undo/Redo transaction creation must not
                | be done when a selection is required in the macro  Do not forget to
                | call  at the end of the macro or before selection to restore the
                | common behavior.
                |
                | Example:
                | This example prevents new transactions to
                | be created, which may increase performance.
                | CATIA.DisableNewUndoRedoTransaction()

        :return:
        """
        return self.application.DisableNewUndoRedoTransaction()

    def enable_new_undo_redo_transaction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EnableNewUndoRedoTransaction
                | o Sub EnableNewUndoRedoTransaction(    )
                | 
                | Allows new Undo/Redo transaction creation.
                |
                | Example: This example
                | restores the common behavior after  has been called.
                | CATIA.EnableNewUndoRedoTransaction()

        :return:
        """
        return self.application.EnableNewUndoRedoTransaction()

    def execute_script(
        self, library_name, library_type, program_name, function_name, items
    ):
        """

        .. note::
            CAA V5 Visual Basic help

            | Func ExecuteScript( CATBSTR  iLibraryName,
            |   CatScriptLibraryType  iType,
            |   CATBSTR  iProgramName,
            |   CATBSTR  iFunctionName,
            |   CATSafeArrayVariant  iParameters) As CATVariant
            |
            | Executes a scripted function.
            | Parameters:
            |   iLibraryName
            |       The library in which the script is contained
            |   iLibraryType
            |       The type of the library
            |   iProgramName
            |       The name of the program in the library
            |   iFunctionName
            |       The name of the function to invoke
            |   iParameters
            |       An array of parameters for the function
            |   Result
            |       The value returned by the function (if any)
            |
            | Example:
            | This example executes the function CATMain in the program Macro1.catvbs contained by Part1.CATPart
            |   Dim params()
            |   CATIA.SystemService.ExecuteScript"Part1.CATPart",
            |       catScriptLibraryTypeDocument,
            |       "Macro1.catvbs",
            |       "CATMain",
            |       params

        :param str library_name: Full path to location of catia script.
        :param int library_type:  An integer representing the library type selection from list()
         CatScriptLibraryType[catScriptLibraryTypeDocument, catScriptLibraryTypeDirectory,
         catScriptLibraryTypeVBAProject]
        :param str program_name: file name of script.
        :param str function_name: Name of function to call within script.
        :param list items: List of items to pass to script.
        :return:
        """

        run = self.com_object.SystemService.ExecuteScript(
            library_name, library_type, program_name, function_name, items
        )

        return run

    def evaluate(
        self, vba_code, function_name, measurable_items, cat_script_language=0
    ):
        """

        .. note::
            CATIA V5 Visual Basic help

            | Func Evaluate( CATBSTR  iScriptText,
            |       CATScriptLanguage  iLanguage,
            |       CATBSTR  iFunctionName,
            |       CATSafeArrayVariant  iParameters) As CATVariant
            |
            | Evaluates a scripted function.
            | Parameters:
            |   iScriptText
            | The program text
            |   iLanguage
            | The language the program is written in
            |   iFunctionName
            | The name of the function to invoke
            |   iParameters
            | An array of parameters for the function
            |   Result
            | The value returned by the function (if any)
            | Example:
            | This example executes the function CATMain from the CodeToEvaluate string
            |   Dim params()
            |   Dim codeToEvaluate
            |   CodeToEvaluate = "Sub CATMain()" & vbNewLine & _
            |                   "MsgBox " & chr(34) & "Hello World" & chr(34) & vbNewLine & _
            |                   "End Sub"
            |   CATIA.SystemService.Evaluate CodeToEvaluate, CATVBScriptLanguage, "CATMain", params


        :param str vba_code: String containing script to run.
        :param str function_name: Name of function within vba script.
        :param list measurable_items: list of items to pass to script.
        :param int cat_script_language: An integer representing the language selection from list()
         [CATVBScriptLanguage, CATVBALanguage, CATBasicScriptLanguage, CATJavaLanguage,
         CATJScriptLanguage]
        :return:
        """

        run = self.application.SystemService.Evaluate(
            vba_code, cat_script_language, function_name, measurable_items,
        )

        return run

    def file_selection_box(self, i_title, i_extension, i_mode):
        """
        .. note::
            CAA V5 Visual Basic help

                | FileSelectionBox
                | o Func FileSelectionBox(iTitle,
                |                         iExtension,
                |                         iMode) As
                |
                | Displays a modal dialog box which can be used to select / enter the
                | name of a file to open / save.
                |
                | Parameters:
                | iTitle
                |  The title of the dialog box.
                | iExtension
                |   A file extension filter.
                | iMode
                |   The mode in which to run the dialog box (either CatFileSelectionModeOpen or
                |   CatFileSelectionModeSave.
                | oFilePath
                |   The return string containing the full path of the selected file, or a zero-length
                |   string if the user selects Cancel.
                |
                | Examples:
                | This example asks the user to select a text file and prints the path of the selected
                | file.
                | filepath = CATIA.FileSelectionBox("Select a text file", "\*.txt", CatFileSelectionModeOpen)
                | CATIA.SystemServices.Print "The selected file is " & filepath

        :param i_title:
        :param i_extension:
        :param i_mode:
        :return:
        """
        return self.application.FileSelectionBox(i_title, i_extension, i_mode)

    def get_workbench_id(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetWorkbenchId
                | o Func GetWorkbenchId(    ) As
                | 
                | Returns the identifier of the CATIA current workbench.
                |
                | Parameters:
                | WoworkbenchId
                |   The id of the current workbench.

        :return:
        """
        return self.application.GetWorkbenchId()

    def help(self, i_help_id):
        """
        .. note::
            CAA V5 Visual Basic help

                | Help
                | o Sub Help(        iHelpID)
                | 
                | Displays application's online help.
                |
                | Parameters:
                | iHelpID
                |    Identifier of the help message to display
                |
                | Examples:
                | This example displays the string referred to by the HelpKey
                | message key in the message catalog concatenation.
                | 
                | CATIA.Help("HelpKey")

        :param i_help_id:
        :return:
        """
        return self.application.Help(i_help_id)

    def quit(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Quit
                | o Sub Quit(    )
                | 
                | Exits the application and closes all open documents.
                | Example: This example exits the CATIA application
                | and closes all its open documents.
                | CATIA.Quit()

        :return:
        """
        return self.application.Quit()

    def start_command(self, i_command_id):
        """
        .. note::
            CAA V5 Visual Basic help

                | StartCommand
                | o Sub StartCommand(        iCommandId)
                | 
                | Starts a CATIA command. Role:This method starts a command and executes
                | it until its first interaction. Please notice interactions such as
                | selections you could add after in your macro will not work.
                | StartCommand is useful to execute one-shot (not interactive) commands,
                | it is not safe for interactive commands.
                |
                | Parameters:
                | iCommandId
                |  The id of the command to be started. This id can be the name of the 
                |  command or its alias.

        :param i_command_id:
        :return:
        """
        return self.application.StartCommand(i_command_id)

    def start_workbench(self, iworkbench_id):
        """
        .. note::
            CAA V5 Visual Basic help

                | StartWorkbench
                | o Sub StartWorkbench(        iworkbenchId)
                | 
                | Starts a CATIA workbench.
                |
                | Parameters:
                | iworkbenchId
                |  The id of the workbench to be started.

        :param iworkbench_id:
        :return:
        """
        return self.application.StartWorkbench(iworkbench_id)

    def __repr__(self):
        return f'Application(name="{self.name}")'
