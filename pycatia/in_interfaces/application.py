#! /usr/bin/python3.9
# module initially auto generated using V5Automation.chm from CATIA R25
import inspect

from pywintypes import com_error

from pathlib import Path

from pycatia.enumeration.enumeration_types import cat_script_language
from pycatia.exception_handling.exceptions import CATIAApplicationException
from pycatia.in_interfaces.document import Document
from pycatia.in_interfaces.documents import Documents
from pycatia.in_interfaces.documents import get_document_object
from pycatia.in_interfaces.file_system import FileSystem
from pycatia.in_interfaces.printer import Printer
from pycatia.in_interfaces.printers import Printers
from pycatia.in_interfaces.send_to_service import SendToService
from pycatia.in_interfaces.system_configuration import SystemConfiguration
from pycatia.in_interfaces.window import Window
from pycatia.in_interfaces.windows import Windows
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.system_service import SystemService
from pycatia.in_interfaces.setting_controllers import SettingControllers
from pycatia.types.document import document_types


class Application(AnyObject):
    """

    .. note::
        :class: toggle

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
        self.com_object = com_object

    @property
    def active_document(self) -> Document:
        """
        .. note::
            :class: toggle

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

        :rtype: Document
        """
        try:
            active_doc_com = self.com_object.ActiveDocument
            return get_document_object(active_doc_com)
        except com_error:
            raise CATIAApplicationException('Is there an active document?')

    @property
    def active_printer(self) -> Printer:
        """
        .. note::
            :class: toggle
            
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

        :rtype: Printer
        """

        return Printer(self.com_object.ActivePrinter)

    @active_printer.setter
    def active_printer(self, value: Printer):
        """
        :param Printer value:
        """

        self.com_object.ActivePrinter = value

    @property
    def active_window(self) -> Window:
        """
        .. note::
            :class: toggle
            
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

        :rtype: Window
        """

        return Window(self.com_object.ActiveWindow)

    @property
    def cache_size(self) -> int:
        """
        .. note::
            :class: toggle
            
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

        :rtype: int
        """

        return self.com_object.CacheSize

    @cache_size.setter
    def cache_size(self, value: int):
        """
        :param int value:
        """

        self.com_object.CacheSize = value

    @property
    def caption(self) -> str:
        """
        .. note::
            :class: toggle
            
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

        :rtype: str
        """

        return self.com_object.Caption

    @caption.setter
    def caption(self, value: str):
        """
        :param str value:
        """

        self.com_object.Caption = value

    @property
    def display_file_alerts(self) -> bool:
        """
        .. note::
            :class: toggle
            
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

        :rtype: bool
        """

        return self.com_object.DisplayFileAlerts

    @display_file_alerts.setter
    def display_file_alerts(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DisplayFileAlerts = value

    @property
    def documents(self) -> Documents:
        """
        .. note::
            :class: toggle
            
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

        :rtype: Documents
        """
        return Documents(self.com_object.Documents)

    @property
    def file_search_order(self) -> str:
        """
        .. note::
            :class: toggle
            
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

        :rtype: str
        """

        return self.com_object.FileSearchOrder

    @file_search_order.setter
    def file_search_order(self, value: str):
        """
        :param str value:
        """

        self.com_object.FileSearchOrder = value

    @property
    def file_system(self) -> FileSystem:
        """
        .. note::
            :class: toggle
            
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

        :rtype: FileSystem
        """

        return FileSystem(self.com_object.FileSystem)

    @property
    def full_name(self) -> str:
        """
        .. note::
            :class: toggle
            
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

        :rtype: str
        """

        return self.com_object.FullName

    @property
    def hso_synchronized(self) -> bool:
        """
        .. note::
            :class: toggle
            
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

        :rtype: bool
        """

        return self.com_object.HSOSynchronized

    @hso_synchronized.setter
    def hso_synchronized(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.HSOSynchronized = value

    @property
    def height(self) -> float:
        """
        .. note::
            :class: toggle
            
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

        :rtype: float
        """

        return self.com_object.Height

    @height.setter
    def height(self, value: float):
        """
        :param float value:
        """

        self.com_object.Height = value

    @property
    def interactive(self) -> bool:
        """
        .. note::
            :class: toggle
            
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

        :rtype: bool
        """

        return self.com_object.Interactive

    @interactive.setter
    def interactive(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Interactive = value

    @property
    def left(self) -> float:
        """
        .. note::
            :class: toggle
            
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

        :rtype: float
        """

        return self.com_object.Left

    @left.setter
    def left(self, value: float):
        """
        :param float value:
        """

        self.com_object.Left = value

    @property
    def local_cache(self) -> str:
        """
        .. note::
            :class: toggle
            
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

        :rtype: str
        """

        return self.com_object.LocalCache

    @local_cache.setter
    def local_cache(self, value: str):
        """
        :param str value:
        """

        self.com_object.LocalCache = value

    @property
    def path(self) -> Path:
        """
        .. note::
            :class: toggle
            
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

        :rtype: Path
        """

        return Path(self.com_object.Path)

    @property
    def printers(self) -> Printers:
        """
        .. note::
            :class: toggle
            
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

        :rtype: Printers
        """

        return Printers(self.com_object.Printers)

    @property
    def refresh_display(self) -> bool:
        """
        .. note::
            :class: toggle
            
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

        :rtype: bool
        """

        return self.com_object.RefreshDisplay

    @refresh_display.setter
    def refresh_display(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.RefreshDisplay = value

    @property
    def status_bar(self) -> str:
        """
        .. note::
            :class: toggle
            
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

        :rtype: str
        """

        return self.com_object.StatusBar

    @status_bar.setter
    def status_bar(self, value: str):
        """
        :param str value:
        """

        self.com_object.StatusBar = value

    @property
    def system_configuration(self) -> SystemConfiguration:
        """
        .. note::
            :class: toggle
            
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

        :rtype: SystemConfiguration
        """

        return SystemConfiguration(self.com_object.SystemConfiguration)

    @property
    def system_service(self) -> SystemService:
        """
        .. note::
            :class: toggle
            
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

        :rtype: SystemService
        """

        return SystemService(self.com_object.SystemService)

    @property
    def top(self) -> float:
        """
        .. note::
            :class: toggle
            
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

        :rtype: float
        """

        return self.com_object.Top

    @top.setter
    def top(self, value: float):
        """
        :param float value:
        """

        self.com_object.Top = value

    @property
    def undo_redo_lock(self) -> bool:
        """
        .. note::
            :class: toggle
            
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

        :rtype: bool
        """

        return self.com_object.UndoRedoLock

    @undo_redo_lock.setter
    def undo_redo_lock(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UndoRedoLock = value

    @property
    def visible(self) -> bool:
        """
        .. note::
            :class: toggle
            
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

        :rtype: bool
        """

        return self.com_object.Visible

    @visible.setter
    def visible(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Visible = value

    @property
    def width(self) -> float:
        """
        .. note::
            :class: toggle
            
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

        :rtype: float
        """

        return self.com_object.Width

    @width.setter
    def width(self, value: float):
        """
        :param float value:
        """

        self.com_object.Width = value

    @property
    def windows(self) -> Windows:
        """
        .. note::
            :class: toggle
            
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

        :rtype: Windows
        """

        return Windows(self.com_object.Windows)

    def begin_ur_concatenation(self) -> None:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub BeginURConcatenation()
                |     Start to concatenate the undo steps created during the following code.
                |     Using this API will launch a dummy command in order to close all current model
                |     transaction. This is to avoid to left the model in an unconsitent state.

        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.application.BeginURConcatenation()

    def create_send_to(self) -> SendToService:
        """
        .. note::
            :class: toggle
            
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))

            | o Func CreateSendTo() As SendToService
            |
            |     Creates a Send TO.
            |     Role:This method creates a SendToService instance.
            |     Warning : CATIASendToService interface requires the
            |     installation of CATIA - PPR xPDM Gateway 1 Product (PX1)
            |     In case this product is not granted, the first invocation
            |     to one of CATIASendToService methods will fail.

        :rtype: SendToService
        """
        return SendToService(self.com_object.CreateSendTo())

    def disable_new_undo_redo_transaction(self) -> None:
        """
        .. note::
            :class: toggle
            
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

        :rtype: None
        """
        return self.com_object.DisableNewUndoRedoTransaction()

    def enable_new_undo_redo_transaction(self) -> None:
        """
        .. note::
            :class: toggle

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

        :rtype: None
        """
        return self.com_object.EnableNewUndoRedoTransaction()

    def file_selection_box(self, i_title: str, i_extension: str, i_mode: int) -> str:
        """
        .. note::
            :class: toggle

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
            |                                                     "\\*.txt", CatFileSelectionModeOpen)
            |                  CATIA.SystemServices.Print "The selected file is " &
            |                  filepath

        :param str i_title:
        :param str i_extension:
        :param int i_mode: enum cat_file_selection_mode
        :rtype: str
        """
        return self.com_object.FileSelectionBox(i_title, i_extension, i_mode)

    def get_workbench_id(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))

            | o Func GetWorkbenchId() As CATBSTR
            |
            |     Returns the identifier of the CATIA current workbench.
            |
            |     Parameters:
            |
            |         oworkbenchId
            |             The id of the current workbench.

        :rtype: str
        """
        return self.com_object.GetWorkbenchId()

    def help(self, i_help_id: str) -> None:
        """
        .. note::
            :class: toggle

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
        :rtype: None
        """
        return self.com_object.Help(i_help_id)

    def message_box(self, message_text: str, buttons: int = 0, title: str = ""):
        """

        The button values

        =====================   ======= ========================================
        Constant                Value   Description
        ---------------------   ------- ----------------------------------------
        vbOKOnly                0       Display OK button only.
        vbOKCancel              1       Display OK and Cancel buttons.
        vbAbortRetryIgnore      2       Display Abort, Retry, and Ignore buttons
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
        vbApplicationModal      0       Application modal; the user must respond
                                        to the message box before continuing
                                        work in the current application.
        vbSystemModal           4096    System modal; all applications are
                                        suspended until the user responds to the
                                        message box.
        vbMsgBoxHelpButton      16384   Adds Help button to the message box.
        vbMsgBoxSetForeground   65536   Specifies the message box window as the
                                        foreground window.
        vbMsgBoxRight           524288  Text is right-aligned.
        vbMsgBoxRtlReading      1048576 Specifies text should appear as
                                        right-to-left reading on Hebrew and
                                        Arabic systems.
        =====================   ======= ========================================


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

    def input_box(
            self,
            prompt: str,
            title: str = '',
            default: str = ''
    ) -> str:
        """
        Display InputBox in catia.
        Default position is in the center screen.

        More information on
        https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/inputbox-function

        :param str prompt: Required. String expression displayed as the message in the dialog box.
        :param str title: Optional. The default is ''. String expression displayed in the title bar of the dialog box.
        :param str default: Optional. The default is ''. String expression displayed in the text box as the default
                                      response if no other input is provided. If you omit default, the text box is
                                      displayed empty.
        :returns: str
        """
        f_name = "input_box"
        i_box = f"Public Function {f_name}(prompt,title,default)\n" \
                f"    {f_name} = InputBox(prompt,title,default)\n" \
                "End Function"
        return self.system_service.evaluate(
            i_box,
            cat_script_language.index('CATVBScriptLanguage'),
            f_name,
            [prompt, title, default]
        )

    def quit(self) -> None:
        """
        .. note::
            :class: toggle

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

        :rtype: None
        """
        return self.com_object.Quit()

    def setting_controllers(self) -> SettingControllers:
        """
        Application.SettingControllers
        """
        return SettingControllers(self.com_object.SettingControllers)

    def start_command(self, i_command_id: str) -> None:
        """
        .. note::
            :class: toggle

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
        :rtype: None
        """
        return self.com_object.StartCommand(i_command_id)

    def start_workbench(self, iworkbench_id: str) -> None:
        """
        .. note::
            :class: toggle

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
        :rtype: None
        """
        return self.com_object.StartWorkbench(iworkbench_id)

    def stop_ur_concatenation(self, i_undo_step_name_bstr: str) -> None:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub StopURConcatenation(CATBSTR iUndoStepNameBSTR)
                |     Concatenate all the undo steps created since the start
                |     call.
                |
                |     Parameters:
                |
                |         iUndoStepNameBSTR
                |             Name of the undo step that will be created

        :param str i_undo_step_name_bstr:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.application.StopURConcatenation(i_undo_step_name_bstr)

    def __repr__(self):
        return f'Application(name="{self.name}")'
