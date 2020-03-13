#! /usr/bin/python3.6

from win32com.client import Dispatch

from .document import Document
from .documents import Documents


class CATIAApplication:
    """
    All pycatia scripts will start with the creation on the CATIAApplication() object.

    :Example:

        >>> from pycatia.base_interfaces import CATIAApplication
        >>> catia = CATIAApplication()
        >>> documents = catia.documents()
        >>> file_name = 'my_new_part.CATPart'
        >>> documents.open(file_name)

    .. note::
        CAA V5 Visual Basic help

        Represents the current CNext application and its frame window.
        The application is the root object for all the other objects you can use and access from scripts.
        It directly aggregates:

        - The document collection represented by the Documents object. This collection contains all the documents
          currently opened by the application.

        - The window collection represented by the Windows object. This collection contains all the windows currently
          opened by the application, each window displaying one of the documents contained in the document collection

        - The SystemService object, providing information about the system environment.


        The active document and the active window are two key objects for the application you can access using the
        ActiveDocument and ActiveWindow properties respectively. The active window is the window the end user is
        currently working in, and the active document is the document displayed in this active window and that the end
        user is being editing. This document sets its workshop, that is the available menus and toolbars that make it
        possible to edit it, according to its type.

        When you create or use macros for in-process access, the application is always referred to as CATIA.

    """

    def __init__(self):
        self.catia = Dispatch('CATIA.Application')

    def documents(self):
        """
        :return: :class:`Documents()`
        """

        return Documents(self.catia)

    def document(self):
        """
        :return: :class:`Document()`
        """

        return Document(self.catia)

    def refresh_display(self, state=None):
        """
        Set refresh_display to False to speed up macros.

        Set back to True on macro completion.

        .. note::
            CAA V5 Visual Basic help

            Property RefreshDisplay( ) As boolean

            Enables or disables the update of the display during the script replay. To improve performance, this update
            can be temporarily disabled by setting this property to False in the script.
            True (value set by default) if the application's display is refreshed after each method call executed in
            late binding mode . This property does not affect early binding calls nor the get methods because they are
            never followed by a refresh of the display.
            | Example:
            | This example makes the update of the CATIA application's display disabled during the script replay.
            |    CATIA.RefreshDisplay = False

        :param bool state:
        :return: bool
        """

        if state is None:
            state = self.catia.RefreshDisplay

        self.catia.RefreshDisplay = state

        return self.catia.RefreshDisplay

    def visible(self, state=None):
        """
        .. note::
            Property Visible( ) As boolean

            Returns or sets the application's window visibility.
            True if the application's window is visible to the end user.
            | Example:
            | This example makes the CATIA application's window visible.
            |   CATIA.Visibility = True

        :param bool state:
        :return: bool
        """

        if state is None:
            state = self.catia.Visible

        self.catia.Visible = state

        return self.catia.Visible

    def evaluate(self, vba_code, function_name, measurable_items, cat_script_language=0):
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

        run = self.catia.SystemService.Evaluate(
            vba_code,
            cat_script_language,
            function_name,
            measurable_items,
        )

        return run

    def execute_script(self, library_name, library_type, program_name, function_name, items):
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

        run = self.catia.SystemService.ExecuteScript(
            library_name,
            library_type,
            program_name,
            function_name,
            items
        )

        return run

    def __repr__(self):
        return 'CATIAApplication()'
