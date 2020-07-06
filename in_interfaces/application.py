#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25

from pywintypes import com_error

from pathlib import Path

from pycatia.enumeration.enumeration_types import cat_script_language
from pycatia.exception_handling.exceptions import CATIAApplicationException
from pycatia.in_interfaces.document import Document
from pycatia.in_interfaces.documents import Documents
from pycatia.in_interfaces.file_system import FileSystem
from pycatia.in_interfaces.printer import Printer
from pycatia.in_interfaces.printers import Printers
from pycatia.in_interfaces.send_to_service import SendToService
from pycatia.in_interfaces.system_configuration import SystemConfiguration
from pycatia.in_interfaces.window import Window
from pycatia.in_interfaces.windows import Windows
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.system_service import SystemService


class Application(AnyObject):
    """

    .. admonition:: Note

        CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.AnyObject
            |                     Application
            |
            | Represents the current CNext application and its frame window.
            | The application is the root object for all the other objects you can use and
            | access from scripts. It directly aggregates:
            |
            |     The document collection represented by the Documents object. This
            |     collection contains all the documents currently opened by the
            |     application
            |     The window collection represented by the Windows object. This collection
            |     contains all the windows currently opened by the application, each window
            |     displaying one of the documents contained in the document
            |     collection
            |     The SystemService object, providing information about the system
            |     environment.
            |
            | The active document and the active window are two key objects for the
            | application you can access using the ActiveDocument and ActiveWindow properties
            | respectively. The active window is the window the end user is currently working
            | in, and the active document is the document displayed in this active window and
            | that the end user is being editing. This document sets its workshop, that is
            | the available menus and toolbars that make it possible to edit it, according to
            | its type.
            |
            | When you create or use macros for in-process access, the application is always
            | referred to as CATIA.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)

    @property
    def active_document(self) -> Document:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property ActiveDocument() As Document (Read Only)
            |
            |     Returns the active document. The active document is the document the end
            |     user is being editing.
            |
            |     Example:
            |         This example retrieves in ActiveDoc the active document of the CATIA
            |         application.
            |
            |          Dim ActiveDoc As Document
            |          Set ActiveDoc = CATIA.ActiveDocument

        :return: Document
        :rtype: Document
        """
        try:
            return Document(self.application.ActiveDocument)
        except com_error:
            raise CATIAApplicationException('Is there an active document?')

    @property
    def active_printer(self) -> Printer:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property ActivePrinter() As Printer
            |
            |     Returns or sets the active printer. The active printer is the printer on
            |     which documents are printed
            |
            |     Example:
            |         This example retrieves in ActivePrinter the active printer of the CATIA
            |         application.
            |
            |          Dim ActivePrinter As Printer
            |          Set ActivePrinter = CATIA.ActivePrinter

        :return: Printer
        :rtype: Printer
        """

        return Printer(self.application.ActivePrinter)

    @active_printer.setter
    def active_printer(self, value: Printer):
        """
        :param Printer value:
        """

        self.application.ActivePrinter = value

    @property
    def active_window(self) -> Window:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property ActiveWindow() As Window (Read Only)
            |
            |     Returns the active window. The active window is the window in which the end
            |     user is currently editing the active document.
            |
            |     Example:
            |         This example retrieves in ActiveWin the active window of the CATIA
            |         application.
            |
            |          Dim ActiveWin As Window
            |          Set ActiveWin = CATIA.ActiveWindow

        :return: Window
        :rtype: Window
        """

        return Window(self.application.ActiveWindow)

    @property
    def cache_size(self) -> int:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property CacheSize() As long
            |
            |     Returns or sets the default local cache size used by the
            |     application.
            |
            |     Example:
            |         This example sets the cache size for by the CATIA application to those
            |         defined in LocalCacheSize.
            |
            |          LocalCacheSize= 10
            |          CATIA.CacheSize = LocalCacheSize

        :return: int
        :rtype: int
        """

        return self.application.CacheSize

    @cache_size.setter
    def cache_size(self, value: int):
        """
        :param int value:
        """

        self.application.CacheSize = value

    @property
    def caption(self) -> str:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property Caption() As CATBSTR
            |
            |     Returns or sets the application's window title. This title is displayed in
            |     the application's window title bar.
            |
            |     Example:
            |         This example retrieves in Title the CATIA application's window
            |         title.
            |
            |          Title = CATIA.Caption
            |
            |
            |         The returned value is like this:
            |
            |          CNext

        :return: str
        :rtype: str
        """

        return self.application.Caption

    @caption.setter
    def caption(self, value: str):
        """
        :param str value:
        """

        self.application.Caption = value

    @property
    def display_file_alerts(self) -> bool:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property DisplayFileAlerts() As boolean
            |
            |     Returns or sets the application ability to display file
            |     alerts.
            |     True if the application enables file alert display.
            |     True is the default. A file alert is, for example, the dialog box that
            |     prompts you that the file you want to save is in read only mode, or that the
            |     file you want to close needs to be saved. It could be handy to disable these
            |     file alerts for automation since they may freeze your macro execution, waiting
            |     for an end user input in the displayed dialog box.
            |
            |     Example:
            |         This example disables file alerts for the CATIA
            |         application.
            |
            |          CATIA.DisplayFileAlerts = False

        :return: bool
        :rtype: bool
        """

        return self.application.DisplayFileAlerts

    @display_file_alerts.setter
    def display_file_alerts(self, value: bool):
        """
        :param bool value:
        """

        self.application.DisplayFileAlerts = value

    @property
    def documents(self) -> Documents:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property Documents() As Documents (Read Only)
            |
            |     Returns the collection of documents currently managed by the
            |     application.
            |
            |     Example:
            |         This example retrieves in DocCollection the collection of documents
            |         currently managed by the CATIA application.
            |
            |          Dim DocCollection As Documents
            |          Set DocCollection = CATIA.Documents

        :return: Documents
        :rtype: Documents
        """
        return Documents(self.application.Documents)

    @property
    def file_search_order(self) -> str:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property FileSearchOrder() As CATBSTR
            |
            |     Returns or sets the default path concatenation.
            |     Role: This property returns or sets the default path concatenation used by
            |     Other folders setting of the Linked Documents Localization function. The
            |     primary aim of the Linked Documents Localization function is to resolve
            |     document links and to manage the strategy that will be used to locate your
            |     linked documents.
            |
            |     Example:
            |         This example sets the paths to search for by the CATIA application to
            |         those defined in PathConcatenation.
            |
            |          PathConcatenation = "/u/users/fbq/db/model:/u/users/psr/db/model"
            |          CATIA.FileSearchOrder = PathConcatenation
            |
            |
            |
            |     Theese methods require the installation of CATIA - PPR xPDM Gateway 1
            |     Product (PX1) In case this product is not granted, the first invocation to one
            |     of the methods will fail.

        :return: str
        :rtype: str
        """

        return self.application.FileSearchOrder

    @file_search_order.setter
    def file_search_order(self, value: str):
        """
        :param str value:
        """

        self.application.FileSearchOrder = value

    @property
    def file_system(self) -> FileSystem:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property FileSystem() As FileSystem (Read Only)
            |
            |     Returns the file system. The file system provides access to a computer's
            |     file system.
            |
            |     Example:
            |         This example retrieves in AppliFileSys the file sytem of the CATIA
            |         application.
            |
            |          Dim AppliFileSys As FileSystem
            |          Set AppliFileSys = CATIA.FileSystem

        :return: FileSystem
        :rtype: FileSystem
        """

        return FileSystem(self.application.FileSystem)

    @property
    def full_name(self) -> str:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property FullName() As CATBSTR (Read Only)
            |
            |     Returns the application's executable file full name, including its path.
            |     This name is the name of the executable file used to start the
            |     application.
            |
            |     Example:
            |         This example retrieves in ApplicationFullName the CATIA application's
            |         executable file full name.
            |
            |          ApplicationFullName = CATIA.FullName
            |
            |
            |         The returned value is like this:
            |
            |          \\\\lisa\\cxr1arel\\bsf\\alpha_a\\code\\bin\\CNEXT.exe

        :return: str
        :rtype: str
        """

        return self.application.FullName

    @property
    def hso_synchronized(self) -> bool:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property HSOSynchronized() As boolean
            |
            |     For selection performance purposes, returns or sets the HSO synchronization
            |     in comparison with the CSO.
            |     Role: Precises if, for all Selection object instances, the HSO (Highlighted
            |     Set of Objects) is synchronized in comparison with the CSO (Current Set of
            |     Objects).
            |
            |     Valid values are:
            |
            |         True: In this case, Selection methods work directly with CATIA's CSO,
            |         to reflect instantly the changes made in Automation Selection. This ensures
            |         correct selection results, but may impact performance in certain
            |         cases.
            |         This is the default value at the beginning of a CATIA
            |         session.
            |         False: In this case, Selection methods work with an internal SO buffer,
            |         which allows faster execution when performing a large number of CSO-independent
            |         Selection calls, or when performing a single Selection call working on a large
            |         number of objects (usually the Search method). This may also prevent the
            |         features from blinking between two user interactions.
            |
            |     Note: even if this property is set to False, the HSO is synchronized in
            |     comparison with the CSO at the begining of the following
            |     methods:
            |
            |         Selection.SelectElement2
            |         Selection.SelectElement3
            |         Selection.SelectElement4
            |         Selection.IndicateOrSelectElement2D
            |         Selection.IndicateOrSelectElement3D
            |         Application.StartCommand
            |
            |     CAUTION: If you use the False value of this property, you must make sure to
            |     reset it to True for CATIA's CSO to reflect properly the changes made in
            |     Automation Selection. For example, it should be reset to True before
            |     interactive parts of your script: MsgBox, InputBox calls, VBA forms updates and
            |     so on.

        :return: bool
        :rtype: bool
        """

        return self.application.HSOSynchronized

    @hso_synchronized.setter
    def hso_synchronized(self, value: bool):
        """
        :param bool value:
        """

        self.application.HSOSynchronized = value

    @property
    def height(self) -> float:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property Height() As float
            |
            |     Returns or sets the height of the application's frame window. The height is
            |     expressed in pixels.
            |
            |     Example:
            |         This example sets the height of the CATIA application's frame window to
            |         300 pixels.
            |
            |          CATIA.Height = 300

        :return: float
        :rtype: float
        """

        return self.application.Height

    @height.setter
    def height(self, value: float):
        """
        :param float value:
        """

        self.application.Height = value

    @property
    def interactive(self) -> bool:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property Interactive() As boolean
            |
            |     Returns or sets the application sensitivity to end user
            |     interactions.
            |     True if the application is end user interaction sensitive.
            |
            |     Example:
            |         This example makes the CATIA application sensitive to end user
            |         interactions.
            |
            |          CATIA.Interactive = True

        :return: bool
        :rtype: bool
        """

        return self.application.Interactive

    @interactive.setter
    def interactive(self, value: bool):
        """
        :param bool value:
        """

        self.application.Interactive = value

    @property
    def left(self) -> float:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property Left() As float
            |
            |     Returns or sets the distance from the application's frame window left side
            |     to the left side of the screen. This distance is expressed in
            |     pixels.
            |
            |     Example:
            |         This example sets the distance from the CATIA application's frame
            |         window left side to the left side of the screen to 150
            |         pixels.
            |
            |          CATIA.Left = 150

        :return: float
        :rtype: float
        """

        return self.application.Left

    @left.setter
    def left(self, value: float):
        """
        :param float value:
        """

        self.application.Left = value

    @property
    def local_cache(self) -> str:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property LocalCache() As CATBSTR
            |
            |     Returns or sets the default local cache path used by the
            |     application.
            |
            |     Example:
            |         This example sets the cache path for by the CATIA application to those
            |         defined in LocalCachePath.
            |
            |          LocalCachePath= "/tmp/cache"
            |          CATIA.LocalCache = LocalCachePath

        :return: str
        :rtype: str
        """

        return self.application.LocalCache

    @local_cache.setter
    def local_cache(self, value: str):
        """
        :param str value:
        """

        self.application.LocalCache = value

    @property
    def path(self) -> str:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property Path() As CATBSTR (Read Only)
            |
            |     Returns the path of the application's executable files.
            |
            |     Example:
            |         This example retrieves in ApplicationPath the path where the CATIA
            |         application executable files are located.
            |
            |          ApplicationPath = CATIA.Path
            |
            |
            |         The returned value is like this:
            |
            |          \\\\lisa\\cxr1arel\\bsf\\alpha_a\\code\\bin

        :return: str
        :rtype: str
        """

        return self.application.Path

    @property
    def printers(self) -> Printers:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property Printers() As Printers (Read Only)
            |
            |     Returns the collection of the printers currently managed by the
            |     application.
            |
            |     Example:
            |         This example retrieves in PrintersCollection the collection of the
            |         printers currently managed by the CATIA application.
            |
            |          Dim PrintersCollection As Windows
            |          Set PrintersCollection = CATIA.Printers

        :return: Printers
        :rtype: Printers
        """

        return Printers(self.application.Printers)

    @property
    def refresh_display(self) -> bool:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property RefreshDisplay() As boolean
            |
            |     Enables or disables the update of the display during the script replay. To
            |     improve performance, this update can be temporarely disabled by setting this
            |     property to False in the script.
            |     True (value set by default) if the application's display is refreshed after
            |     each method call executed in late binding mode . This property does not affect
            |     early binding calls nor the get methods because they are never followed by a
            |     refresh of the display.
            |
            |     Example:
            |         This example makes the update of the CATIA application's display
            |         disabled during the script replay.
            |
            |          CATIA.RefreshDisplay = False

        :return: bool
        :rtype: bool
        """

        return self.application.RefreshDisplay

    @refresh_display.setter
    def refresh_display(self, value: bool):
        """
        :param bool value:
        """

        self.application.RefreshDisplay = value

    @property
    def status_bar(self) -> str:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property StatusBar() As CATBSTR
            |
            |     Returns or sets the text displayed in the application's window status
            |     bar.
            |
            |     Example:
            |         This example retrieves in Text the text displayed in the CATIA
            |         application's window status bar.
            |
            |          Text = CATIA.StatusBar
            |
            |
            |         The returned value is like this:
            |
            |          Welcome to CATIA CxR1

        :return: str
        :rtype: str
        """

        return self.application.StatusBar

    @status_bar.setter
    def status_bar(self, value: str):
        """
        :param str value:
        """

        self.application.StatusBar = value

    @property
    def system_configuration(self) -> SystemConfiguration:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property SystemConfiguration() As SystemConfiguration (Read
            | Only)
            |
            |     Returns the system configuration object (an object which provides access to
            |     system or configuration dependent resources).
            |
            |     Parameters:
            |
            |         oConfiguration
            |             The system configuration object.

        :return: SystemConfiguration
        :rtype: SystemConfiguration
        """

        return SystemConfiguration(self.application.SystemConfiguration)

    @property
    def system_service(self) -> SystemService:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property SystemService() As SystemService (Read Only)
            |
            |     Returns system services.
            |
            |     Example:
            |         This example retrieves in AppliSysSer the CATIA application's system
            |         services.
            |
            |          Dim AppliSysSer As SystemService
            |          Set AppliSysSer = CATIA.SystemService

        :return: SystemService
        :rtype: SystemService
        """

        return SystemService(self.application.SystemService)

    @property
    def top(self) -> float:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property Top() As float
            |
            |     Returns or sets the distance from the application'si frame window top to
            |     the top of the screen. This distance is expressed in
            |     pixels.
            |
            |     Example:
            |         This example sets the distance from the CATIA application's frame
            |         window top to the top of the screen to 50 pixels.
            |
            |          CATIA.Top = 50

        :return: float
        :rtype: float
        """

        return self.application.Top

    @top.setter
    def top(self, value: float):
        """
        :param float value:
        """

        self.application.Top = value

    @property
    def undo_redo_lock(self) -> bool:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property UndoRedoLock() As boolean
            |
            |     Returns or sets the application status about Undo/Redo.
            |     True if the Undo/Redo mechanism is locked.
            |     False is the default. Since Undo/Redo mechanism uses lots of memory, it can
            |     be useful to disable it during consuming operations. Then Undo and Redo stacks
            |     are flushed and no model modification is kept until the Undo/Redo mechanism is
            |     unlocked. It is mandatory to unlock it before the end of the
            |     macro.
            |
            |     Example:
            |
            |           This example disables Undo/Redo mechanism until it is
            |           unlocked.
            |
            |
            |          CATIA.UndoRedoLock = True

        :return: bool
        :rtype: bool
        """

        return self.application.UndoRedoLock

    @undo_redo_lock.setter
    def undo_redo_lock(self, value: bool):
        """
        :param bool value:
        """

        self.application.UndoRedoLock = value

    @property
    def visible(self) -> bool:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property Visible() As boolean
            |
            |     Returns or sets the application's window visibility.
            |     True if the application's window is visible to the end
            |     user.
            |
            |     Example:
            |         This example makes the CATIA application's window
            |         visible.
            |
            |          CATIA.Visibility = True

        :return: bool
        :rtype: bool
        """

        return self.application.Visible

    @visible.setter
    def visible(self, value: bool):
        """
        :param bool value:
        """

        self.application.Visible = value

    @property
    def width(self) -> float:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property Width() As float
            |
            |     Returns or sets the width of the application's frame window. The width is
            |     expressed in pixels.
            |
            |     Example:
            |         This example sets the width of the CATIA application's frame window to
            |         350 pixels.
            |
            |          CATIA.Width = 350

        :return: float
        :rtype: float
        """

        return self.application.Width

    @width.setter
    def width(self, value: float):
        """
        :param float value:
        """

        self.application.Width = value

    @property
    def windows(self) -> Windows:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | o Property Windows() As Windows (Read Only)
            |
            |     Returns the collection of windows currently managed by the
            |     application.
            |
            |     Example:
            |         This example retrieves in WinCollection the collection of windows
            |         currently managed by the CATIA application.
            |
            |          Dim WinCollection As Windows
            |          Set WinCollection = CATIA.Windows

        :return: Windows
        :rtype: Windows
        """

        return Windows(self.application.Windows)

    def create_send_to(self) -> SendToService:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))

            | o Func CreateSendTo() As SendToService
            |
            |     Creates a Send TO.
            |     Role:This method creates a SendToService instance.
            |     Warning : CATIASendToService interface requires the
            |     installation of CATIA - PPR xPDM Gateway 1 Product (PX1)
            |     In case this product is not granted, the first invocation
            |     to one of CATIASendToService methods will fail.

        :return: SendToService
        :rtype: SendToService
        """
        return SendToService(self.application.CreateSendTo())

    def disable_new_undo_redo_transaction(self) -> None:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))

            | o Sub DisableNewUndoRedoTransaction()
            |
            |     Prevents new Undo/Redo transaction creation.
            |     If too many Undo/Redo transactions are created during macro execution, it
            |     may affect performance. So it is valuable to prevent Undo/Redo transaction
            |     creation during macro execution when lots of data are created, deleted or
            |     modified.
            |     Note: preventing Undo/Redo transaction creation must not be done when a
            |     selection is required in the macro
            |     Do not forget to call EnableNewUndoRedoTransaction at the end of the macro
            |     or before selection to restore the common behavior.
            |
            |     Example:
            |         This example prevents new transactions to be created, which may
            |         increase performance.
            |
            |          CATIA.DisableNewUndoRedoTransaction()

        :return: None
        :rtype: None
        """
        return self.application.DisableNewUndoRedoTransaction()

    def enable_new_undo_redo_transaction(self) -> None:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))

            | o Sub EnableNewUndoRedoTransaction()
            |
            |     Allows new Undo/Redo transaction creation.
            |
            |     Example:
            |         This example restores the common behavior after
            |         DisableNewUndoRedoTransaction has been called.
            |
            |          CATIA.EnableNewUndoRedoTransaction()

        :return: None
        :rtype: None
        """
        return self.application.EnableNewUndoRedoTransaction()

    def execute_script(
            self, library_name, library_type, program_name, function_name, items
    ):
        """

        .. admonition:: Note

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

        .. admonition:: Note

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

    def file_selection_box(self, i_title: str, i_extension: str, i_mode: int) -> str:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))

            | o Func FileSelectionBox(CATBSTR iTitle,
            | CATBSTR iExtension,
            | CatFileSelectionMode iMode) As CATBSTR
            |
            |     Displays a modal dialog box which can be used to select / enter the name of
            |     a file to open / save.
            |
            |     Parameters:
            |
            |         iTitle
            |             The title of the dialog box.
            |         iExtension
            |             A file extension filter.
            |         iMode
            |             The mode in which to run the dialog box (either
            |             CatFileSelectionModeOpen or CatFileSelectionModeSave.
            |
            |         oFilePath
            |             The return string containing the full path of the selected file, or
            |             a zero-length string if the user selects Cancel.
            |
            |             Example:
            |                 This example asks the user to select a text file and prints the
            |                 path of the selected file.
            |
            |                  filepath = CATIA.FileSelectionBox("Select a text file",
            |                                                     "\*.txt", CatFileSelectionModeOpen)
            |                  CATIA.SystemServices.Print "The selected file is " &
            |                  filepath

        :param str i_title:
        :param str i_extension:
        :param CatFileSelectionMode i_mode:
        :return: str
        :rtype: str
        """
        return self.application.FileSelectionBox(i_title, i_extension, i_mode)

    def get_workbench_id(self) -> str:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))

            | o Func GetWorkbenchId() As CATBSTR
            |
            |     Returns the identifier of the CATIA current workbench.
            |
            |     Parameters:
            |
            |         oworkbenchId
            |             The id of the current workbench.

        :return: str
        :rtype: str
        """
        return self.application.GetWorkbenchId()

    def help(self, i_help_id: str) -> None:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))

            | o Sub Help(CATBSTR iHelpID)
            |
            |     Displays application's online help.
            |
            |     Parameters:
            |
            |         iHelpID
            |             Identifier of the help message to display
            |
            |     Example:
            |         This example displays the string referred to by the HelpKey message key
            |         in the message catalog concatenation.
            |
            |          CATIA.Help("HelpKey")

        :param str i_help_id:
        :return: None
        :rtype: None
        """
        return self.application.Help(i_help_id)

    def message_box(self, message_text, buttons=0, title=""):
        """

        The buttons argument settings are:

        =====================   ======= ==============================================================================================================
        Constant                Value   Description
        ---------------------   ------- --------------------------------------------------------------------------------------------------------------
        vbOKOnly                0       Display OK button only.
        vbOKCancel              1       Display OK and Cancel buttons.
        vbAbortRetryIgnore      2       Display Abort, Retry, and Ignore buttons.
        vbYesNoCancel           3       Display Yes, No, and Cancel buttons.
        vbYesNo                 4       Display Yes and No buttons.
        vbRetryCancel           5       Display Retry and Cancel buttons.
        vbCritical              16      Display Critical Message icon.
        vbQuestion              32      Display Warning Query icon.
        vbExclamation           48      Display Warning Message icon.
        vbInformation           64      Display Information Message icon.
        vbDefaultButton1        0       First button is default.
        vbDefaultButton2        256     Second button is default.
        vbDefaultButton3        512     Third button is default.
        vbDefaultButton4        768     Fourth button is default.
        vbApplicationModal      0       Application modal; the user must respond to the message box before continuing work in the current application.
        vbSystemModal           4096    System modal; all applications are suspended until the user responds to the message box.
        vbMsgBoxHelpButton      16384   Adds Help button to the message box.
        vbMsgBoxSetForeground   65536   Specifies the message box window as the foreground window.
        vbMsgBoxRight           524288  Text is right-aligned.
        vbMsgBoxRtlReading      1048576 Specifies text should appear as right-to-left reading on Hebrew and Arabic systems.
        =====================   ======= ==============================================================================================================

        Return values

        ========  =====  ===========
        Constant  Value  Description
        --------  -----  -----------
        vbOK          1  OK
        vbCancel      2  Cancel
        vbAbort       3  Abort
        vbRetry       4  Retry
        vbIgnore      5  Ignore
        vbYes         6  Yes
        vbNo          7  No
        ========  =====  ===========

        Example::

        This creates a message box with the buttons abort, retry ignore and displays the Warning Query icon.

        >>> from pycatia import catia
        >>> buttons = 2 + 32
        >>> result = catia.message_box('Hello World!?', buttons=buttons, title='Asking a question.')
        >>> # result = 3 if the user presses Abort.

        :param str message_text: Text to be displayed in the message box window.
        :param int buttons: Defines the message box configuration. See example.
        :param str title: Text to be displayed in the message box title bar.
        :return: Returns an int which is representative of the button pressed.
        :rtype: int
        """
        function_name = "message_box"
        msg_box = f"Public Function {function_name}(message_text, buttons, title)\n" \
                  f"    {function_name} = MsgBox(message_text, buttons, title)\n" \
                  "End Function"

        return self.system_service.evaluate(
            msg_box,
            cat_script_language.index('CATVBScriptLanguage'),
            function_name,
            [message_text, buttons, title]
        )

    def quit(self) -> None:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))

            | o Sub Quit()
            |
            |     Exits the application and closes all open documents.
            |
            |     Example:
            |         This example exits the CATIA application and closes all its open
            |         documents.
            |
            |          CATIA.Quit()

        :return: None
        :rtype: None
        """
        return self.application.Quit()

    def start_command(self, i_command_id: str) -> None:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))

            | o Sub StartCommand(CATBSTR iCommandId)
            |
            |     Starts a CATIA command.
            |     Role:This method starts a command and executes it untill its first
            |     interaction. Please notice interactions such as selections you could add after
            |     in your macro will not work. StartCommand is useful to execute one-shot (not
            |     interactive) commands, it is not safe for interactive
            |     commands.
            |
            |     Parameters:
            |
            |         iCommandId
            |             The id of the command to be started. This id can be the name of the
            |             command or its alias.

        :param str i_command_id:
        :return: None
        :rtype: None
        """
        return self.application.StartCommand(i_command_id)

    def start_workbench(self, iworkbench_id: str) -> None:
        """
        .. admonition:: Note

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))

            | o Sub StartWorkbench(CATBSTR iworkbenchId)
            |
            |     Starts a CATIA workbench.
            |
            |     Parameters:
            |
            |         iworkbenchId
            |             The id of the workbench to be started.

        :param str iworkbench_id:
        :return: None
        :rtype: None
        """
        return self.application.StartWorkbench(iworkbench_id)

    def __repr__(self):
        return f'Application(name="{self.name}")'
