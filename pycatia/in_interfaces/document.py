#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from typing import TYPE_CHECKING

from pathlib import Path

from pycatia.exception_handling import CATIAApplicationException
from pycatia.in_interfaces.cameras import Cameras
from pycatia.in_interfaces.reference import Reference
from pycatia.in_interfaces.window import Window
from pycatia.in_interfaces.workbench import Workbench
from pycatia.space_analyses_interfaces.spa_workbench import SPAWorkbench
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.in_interfaces.selection import Selection


class Document(AnyObject):
    """
        .. note::
            :class: toggle pytoggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Document
                |
                | Represents the document.
                | The document is the object handled by the operating system as a whole that
                | stores your data in files and databases. It is assigned a type determined by
                | its contents. It may contain other documents with a different type. For
                | example, a PartDocument contains a part and can be contained in a
                | ProductDocument. A workshop is associated with a document to gather all the
                | commands that can be used to create, modify, and edit the objects making up the
                | the document. These commands are arranged in menus and
                | toolbars.
                |
                | See also:
                |     PartDocument, ProductDocument, DrawingDocument

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.document = com_object

    @property
    def cameras(self) -> Cameras:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Cameras() As Cameras (Read Only)
                |
                |     Returns the document's collection of cameras.
                |
                |     Example:
                |         This example retrieves in CameraCollection the collection of cameras
                |         attached to the Doc document.
                |
                |          Dim CameraCollection As Cameras
                |          Set CameraCollection = Doc.Cameras

        :rtype: Cameras
        """

        return Cameras(self.document.Cameras)

    @property
    def current_filter(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property CurrentFilter() As CATBSTR
                |
                |     Returns or sets the current visualization filter. CurrentFilter uses the
                |     filter name and not its definition. The "All visible" filter means that all
                |     layers are visible. For all filters, remind that the current layer is always
                |     visible.
                |
                |     Example:
                |         This example makes the filter named "Filter001" as the current
                |         visualization filter for the Doc document.
                |
                |          Doc.CurrentFilter = "Filter001"

        :rtype: str
        """

        return self.document.CurrentFilter

    @current_filter.setter
    def current_filter(self, value: str):
        """
        :param str value:
        """

        self.document.CurrentFilter = value

    @property
    def current_layer(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property CurrentLayer() As CATBSTR
                |
                |     Returns or sets the current layer. CurrentLayer uses the layer name and not
                |     its number. The "None" layer means that there is no current
                |     layer.
                |
                |     Example:
                |         This example makes the layer named "Layer 3" as the current layer for
                |         the Doc document.
                |
                |          Doc.CurrentLayer = "Layer 3"

        :rtype: str
        """

        return self.document.CurrentLayer

    @current_layer.setter
    def current_layer(self, value: str):
        """
        :param str value:
        """

        self.document.CurrentLayer = value

    @property
    def is_part(self) -> bool:
        """
        Determine whether the active document is a CATPart.

        :return: bool
        """
        try:
            if self.part:
                return True
        except AttributeError:
            return False

    @property
    def is_product(self) -> bool:
        """
        Determine whether the active document is a CATProduct.

        :return: bool
        """
        if self.product.is_catproduct():
            return True
        return False

    @property
    def is_saved(self) -> bool:
        """
        Returns true if document is saved.

        .. note::
            :class: toggle

            CAA V5 Visual Basic help

            Property Saved( ) As boolean (Read Only)

            Returns whether the document has been modified, and thus needs to be saved.
            This happens when the document has changed since either its creation or its last save.
            True if the document has not been changed: the document doesn't need to be saved.
            False if the document has been changed: the document needs to be saved.

            | Example:
            | This example retrieves in HasChanged whether the Doc document needs to be saved.
            | HasChanged = NOT Doc.Saved

        :return: bool
        """

        return self.document.Saved

    @property
    def full_name(self) -> str:
        """

        .. note::
            :class: toggle

            CAA V5 Visual Basic help

            Property FullName( ) As CATBSTR (Read Only)

            | Returns the document's full file name, including its path.
            | Example:
            | This example retrieves in DocFullName the Doc document's full file name.
            |     DocFullName = Doc.FullName
            |
            | The returned value is like this:
            |     e://users//psr//Parts//MyNicePart.CATPart


        :return: str - full path document name
        """

        return str(self.path())

    @property
    def read_only(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ReadOnly() As boolean (Read Only)
                |
                |     Returns whether the file containing the document can be read only, on can
                |     be read and written.
                |     True if the file is read-only.
                |
                |     Example:
                |         This example retrieves in IsReadOnly the ability to read, and possibly
                |         to write in, the file containing the Doc document.
                |
                |          IsReadOnly = Doc.ReadOnly

        :rtype: bool
        """

        return self.document.ReadOnly

    @property
    def see_hidden_elements(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SeeHiddenElements() As boolean
                |
                |     Returns or sets the document's hidden elements visibility.
                |     True if the document's hidden elements are visible to the
                |     user.
                |
                |     Example:
                |         This example makes the Doc document's hidden elements
                |         visible.
                |
                |          Doc.SeeHiddenElements = True

        :return: bool
        """

        return self.document.SeeHiddenElements

    @see_hidden_elements.setter
    def see_hidden_elements(self, value: bool):
        """
        :param bool value:
        """

        self.document.SeeHiddenElements = value

    @property
    def selection(self) -> 'Selection':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Selection() As Selection (Read Only)
                |
                |     Returns the current selection. The current selection is the object or the
                |     set of objects the end user has selected, usually with the mouse, in the active
                |     document displayed in the active window.
                |
                |     Example:
                |         This example returns in CurSel the current selection in the Doc
                |         document
                |
                |          Dim CurSel As Selection
                |          Set CurSel = Doc.Selection

        :rtype: Selection
        """
        from pycatia.in_interfaces.selection import Selection
        return Selection(self.document.Selection)

    def activate(self) -> None:
        """
        Activates the document

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Activate()
                |
                |     Activates the document. Activating a document means that this document is
                |     the one on which the end user is now working on. This document possibly
                |     reconfigures the menu bar and toolbars with its own commands if its type is
                |     different from the type of the previous active document. The first window in
                |     the window collection which contains this document becomes the active
                |     one.
                |
                |     Example:
                |         This example activates the Doc document.
                |
                |          Doc.Activate()

        :rtype: None
        """

        return self.document.Activate()

    def close(self) -> None:
        """
        Closes the current document.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Close()
                |
                |     Closes the document. This closes all the windows displaying the document.
                |     If the document needs to be saved, the end user is prompted whether to save the
                |     document, or to close it anyway.
                |
                |     Example:
                |         This example closes the Doc document
                |
                |          Doc.Close()

        """
        self.document.Close()

    def create_filter(self, i_filter_name: str, i_filter_definition: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub CreateFilter(CATBSTR iFilterName,
                | CATBSTR iFilterDefinition)
                |
                |     Creates a new visualization filter from a name and a definition. Fails if
                |     there is already a filter named iFilterName.
                |
                |     Parameters:
                |
                |         iFilterName
                |             The filter name.
                |         iFilterDefinition
                |             The filter definition
                |         Example:
                |             This example creates the filter named "Filter001" and with "layer=
                |             2 & layer= 1" definition for the Doc document.
                |
                |              Doc.CreateFilter ("Filter001", "layer= 2 & layer=
                |              1")

        :param str i_filter_name:
        :param str i_filter_definition:
        :rtype: None
        """
        return self.document.CreateFilter(i_filter_name, i_filter_definition)

    def create_reference_from_name(self, i_label: str) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateReferenceFromName(CATBSTR iLabel) As Reference
                |
                |     Creates a reference from a GenericNaming label. Each kind of document
                |     provides a specific implementation.
                |
                |     Parameters:
                |
                |         iLabel
                |             The GenericNaming identification for an object.
                |
                |     Returns:
                |         The reference to the object.

        :param str i_label:
        :rtype: Reference
        """
        return Reference(self.document.CreateReferenceFromName(i_label))

    def get_workbench(self, workbench_name: str) -> Workbench:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetWorkbench(CATBSTR workbenchName) As Workbench
                |
                |     Returns one of the workbenches of the document.
                |
                |     Parameters:
                |
                |         workbenchName
                |             The name of the workbench
                |
                |             Example:
                |                 This example retrieves the Structural workbench on the Doc
                |                 document
                |
                |                  Doc.GetWorkbench("Structural")

        :param str workbench_name:
        :rtype: Workbench
        """
        return Workbench(self.document.GetWorkbench(workbench_name))

    def export_data(self, file_name: Path, file_type: str, overwrite=False) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic help

            Sub ExportData( CATBSTR  fileName, CATBSTR  format)

            | Exports the data contained in the document to another format.
            | Parameters:
            |   fileName
            |       The name of the exported file
            |   format
            |       The name of the format
            | Example:
            |   This example writes the Doc document in the IGES format under the IGESDoc name.
            |       Doc.ExportData("IGESDoc", "igs")


        :param Path file_name: file_name including full path.
        :param str file_type: file_type is the extension of required file_type.
                              The file_type must be supported by CATIA and the CATIA license.
        :param bool overwrite: Files will not be overwritten unless is True.
        :return:
        """
        current_dfa_setting = self.application.display_file_alerts
        if not isinstance(file_name, Path):
            file_name = Path(file_name)

        if file_name.suffix.lower() != '.' + file_type.lower():
            raise CATIAApplicationException(
                f'Filename "{file_name}" must have the same suffix as filetype "{file_type}".')

        # add filetype to filename if it hasn't been added correctly.
        if not str(file_name).endswith(file_type):
            file_name = Path(f"{file_name}.{file_type}")

        if not file_name.parent.is_dir():
            raise NotADirectoryError(f'Directory: {file_name.parent} is not a directory.')

        if overwrite is False:
            if file_name.is_file():
                raise FileExistsError(f'File: {file_name} already exists. '
                                      f'Set overwrite=True if you want to overwrite.')
        else:
            self.application.display_file_alerts = False

        # pycatia prefers full path names :-)
        if not file_name.is_absolute():
            self.logger.warning('To prevent unexpected behaviour, be explicit and use absolute filenames.')

        self.document.ExportData(file_name, file_type)

        self.application.display_file_alerts = current_dfa_setting

    def indicate_2d(self, i_message: str) -> str:
        """

        Returns a tuple in the format (status: str, (x_2d: float, y_2d: float))
        Status can be 'Normal', 'Cancel',

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Indicate2D(CATBSTR iMessage,
                | CATSafeArrayVariant ioDocumentWindowLocation) As CATBSTR
                |
                |     Runs an 2D interactive indication command.
                |     Role: Indicate2D asks to the user to select a location in the document
                |     window. It can be used:
                |     When this document is a DrawingDocument
                |
                |     When this document is a PartDocument, and a sketch is being edited (
                |     Sketch.OpenEdition has been called and Sketch.CloseEdition has not been called
                |     yet)
                |
                |     See also: Selection.IndicateOrSelectElement2D which can, in particular,
                |     enable indication and not selection (positionning the iFilterType parameter to
                |     an empty string), whichs enables to subscribe to mouse move events,
                |     positionning the iTriggeringOnPreSelection to true.
                |     Note:If the scripting language is Visual Basic for Applications or Visual
                |     Basic 6 Development Studio, then, you have to know that during the execution of
                |     an interactive selection method such as this one, no form (dialog box) must be
                |     displayed, otherwise it would lead to unpredictible results. In a form method,
                |     before calling an interactive selection method such as Document.Indicate2D, you
                |     must hide all forms, and, after the call to the method, you must show the
                |     forms.
                |
                |     Parameters:
                |
                |         iMessage
                |             A string which instructs the user that he must select a location in
                |             the document window. This string is displayed in the message area located at
                |             the left of the power input area.
                |         oDocumentWindowLocation
                |             An array made of 2 doubles: X, Y - coordinates array of the
                |             location the user specified in the document window.
                |
                |         oOutputState
                |             The state of the indication command once Indicate2D returns. It can
                |             be either "Normal" (the indication has succeeded), "Cancel" (the user wants to
                |             cancel the VB command, which must exit immediately, see the oOutputState
                |             parameter of the Selection.SelectElement2 method), "Undo" or "Redo". About the use of
                |             "Undo" and "Redo", see the example of the Selection.SelectElement2 method.
                |
                |     Example:
                |
                |           The following example suppose a drawing document is currently edited.
                |           It asks the end user to select a
                |          location in the current drawing window, and creates a text (see
                |
                |
                |     DrawingText ) at the specified location:
                |
                |      Set Document = CATIA.ActiveDocument
                |      Set Selection = Document.Selection
                |      Set DrawingSheets = Document.Sheets
                |      Set DrawingSheet = DrawingSheets.ActiveSheet
                |      Set DrawingViews = DrawingSheet.Views
                |      Set DrawingView = DrawingViews.ActiveView
                |      Set DrawingTexts = DrawingView.Texts
                |      'We propose to the user that he specify a location in the drawing window
                |      Dim DrawingWindowLocation(1)
                |      Status=Document.Indicate2D("select a location into the drawing
                |      window",DrawingWindowLocation)
                |      if (Status = "Cancel") then Exit Sub
                |      Set DrawingText=DrawingTexts.Add("Hello
                |      world",DrawingWindowLocation(0),DrawingWindowLocation(1))

        :param str i_message:
        :return: tuple
        """

        vba_function_name = 'indicate_2d'
        vba_code = f'''
        Public Function {vba_function_name}(document, i_message)
        Dim DrawingWindowLocation (1)
        Dim o_output(1)
        o_output(0) = document.Indicate2D(i_message, DrawingWindowLocation)
        o_output(1) = DrawingWindowLocation
        {vba_function_name} = o_output
        End Function
        '''

        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code,
            0,
            vba_function_name,
            [
                self.document,
                i_message
            ]
        )

    def indicate_3d(
            self,
            i_planar_geometric_object: AnyObject,
            i_message: str,
    ) -> str:
        """

        Returns a tuple in the format (status: str, (x_2d: float, y_2d: float), (x_3d: float, y_3d: float, z_3d: float))
        Status can be 'Normal', 'Cancel',

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Indicate3D(AnyObject iPlanarGeometricObject,
                | CATBSTR iMessage,
                | CATSafeArrayVariant ioWindowLocation2D,
                | CATSafeArrayVariant ioWindowLocation3D) As CATBSTR
                |
                |     Runs an 3D interactive indication command.
                |     Role: Indicate3D asks to the user to select a location in the document
                |     window. It cannot be used:
                |     When this document is a DrawingDocument
                |
                |     When this document is a PartDocument, and a sketch is being edited (
                |     Sketch.OpenEdition has been called and Sketch.CloseEdition has not been called
                |     yet)
                |
                |     In these cases, Indicate2D must be used.
                |     See also: Selection.IndicateOrSelectElement3D which can, in particular,
                |     enable indication and not selection (positioning the iFilterType parameter to
                |     an empty string), which enables to subscribe to mouse move events,
                |     positioning the iTriggeringOnPreSelection to true.
                |     Note:If the scripting language is Visual Basic for Applications or Visual
                |     Basic 6 Development Studio, then, you have to know that during the execution of
                |     an interactive selection method such as this one, no form (dialog box) must be
                |     displayed, otherwise it would lead to unpredictable results. In a form method,
                |     before calling an interactive selection method such as Document.Indicate2D, you
                |     must hide all forms, and, after the call to the method, you must show the
                |     forms.
                |
                |     Parameters:
                |
                |         iPlanarGeometricObject
                |             A planar geometric object.
                |             The following objects are supported:
                |
                |         HybridShapeCircle, HybridShapeCircleExplicit, HybridShapeConic, Sketch,
                |         Circle2D, Ellipse2D, Hyperbola2D, Parabola2D and Spline2D.
                |
                |     iMessage
                |         A string which instructs the user that he must select a location in the
                |         document window. This string is displayed in the message area located at the
                |         left of the power input area.
                |     oWindowLocation2D
                |         An array made of 2 doubles: X, Y - coordinates array of the location
                |         the user specified in the document window, in the input planar object
                |         coordinates system
                |     oWindowLocation3D
                |         An array made of 3 doubles: X, Y, Z - coordinates array of the location
                |         the user specified in the document window
                |     oOutputState
                |         The state of the indication command once Indicate3D returns. It can be
                |         either "Normal" (the indication has succeeded), "Cancel" (the user wants to
                |         cancel the VB command, which must exit immediately, see the oOutputState
                |         parameter of the Selection.SelectElement2 method), "Undo" or "Redo". About the
                |         use of "Undo" and "Redo", see the example of the Selection.SelectElement2
                |         method.
                |     Example:
                |
                |           The following example asks the end user to select a location in the
                |
                |          document window, on the Plane.1 plane, and creates a
                |
                |     HybridShapePointOnPlane at the specified location:
                |
                |      Set Document = CATIA.ActiveDocument
                |      Set Part  = Document.Part
                |      Set Selection = Document.Selection
                |      Set HybridShapeFactory = Part.HybridShapeFactory
                |      Set HybridShapePlane = Part.Bodies.Item("PartBody").HybridShapes.Item("Plane.1")
                |      Set PlaneReference = Part.CreateReferenceFromObject(HybridShapePlane)
                |      'We propose to the user that he select a location in the
                |      window
                |      ReDim WindowLocation2D(1),WindowLocation3D(2)
                |      Status=Document.Indicate3D(HybridShapePlane,"select a location in the
                |      document window", _
                |      WindowLocation2D,WindowLocation3D)
                |      if (Status = "Cancel") then Exit Sub
                |      Set HybridShapePointOnPlane = HybridShapeFactory.AddNewPointOnPlane( _
                |      PlaneReference,WindowLocation2D(0),WindowLocation2D(1))
                |      Part.Bodies.Item("PartBody").InsertHybridShape
                |      HybridShapePointOnPlane
                |      Part.InWorkObject = HybridShapePointOnPlane
                |      Part.Update

        :param AnyObject i_planar_geometric_object:
        :param str i_message:
        :return: str
        """
        vba_function_name = 'indicate_3d'
        vba_code = f'''
        Public Function {vba_function_name}(document, i_planar_geometric_object, i_message)
        Dim WindowLocation2D (1)
        Dim WindowLocation3D (2)
        Dim o_output(2)
        o_output(0) = document.Indicate3D(i_planar_geometric_object, i_message, WindowLocation2D, WindowLocation3D)
        o_output(1) = WindowLocation2D
        o_output(2) = WindowLocation3D
        {vba_function_name} = o_output
        End Function
        '''

        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code,
            0,
            vba_function_name,
            [
                self.document,
                i_planar_geometric_object.com_object,
                i_message
            ]
        )

    def new_window(self) -> Window:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func NewWindow() As Window
                |
                |     Duplicates the window which contains the active document. This implies
                |     creating a window, displaying the active document in this window with the same
                |     view point, making this window the active one, and adding the window to the
                |     collection of windows.
                |
                |     Example:
                |         This example creates the MyWindow new window for the Doc
                |         document.
                |
                |          Dim MyWindow As Window
                |          Set MyWindow = Doc.NewWindow()

        :return: Window
        """
        return Window(self.document.NewWindow())

    def path(self) -> Path:
        """

        Returns the pathlib.Path() object of the document fullname.

        example e://users//psr//Parts//MyNicePart.CATPart
        >>> Document.path().name
        MyNicePart.CATPart
        >>> Document.path().parent
        e://users//psr//Parts//
        >>> Document.path().suffix
        .CATPart

        :return: Path()
        """

        return Path(self.document.FullName)

    def remove_filter(self, i_filter_name) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveFilter(CATBSTR iFilterName)
                |
                |     Removes an existing visualization filter. Fails if the filter to be removed
                |     is the current filter.
                |
                |     Parameters:
                |
                |         iFilterName
                |             The filter name.
                |         Example:
                |             This example removes the filter named "Filter001" for the Doc
                |             document.
                |
                |              Doc.RemoveFilter ("Filter001")

        :param str i_filter_name:
        :rtype: None
        """
        return self.document.RemoveFilter(i_filter_name)

    def save(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Save()
                |
                |     Saves the document.
                |
                |     Example:
                |         This example saves the Doc document.
                |
                |          Doc.Save()

        :rtype: None
        """
        self.logger.info(f'Saving the current document.')
        self.document.Save()

    def save_as(self, file_name: Path, overwrite: bool = False) -> None:
        """
        Save the document to a new name.

        If overwrite is True CAA.DisplayFileAlerts is set to False.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SaveAs(CATBSTR fileName)
                |
                |     Saves the document with another name.
                |
                |     Parameters:
                |
                |         fileName
                |             The name to assign to the document
                |
                |     Example:
                |         This example saves the Doc document with the NewName
                |         name.
                |
                |          Doc.SaveAs("NewName")

        :param file_name: full pathname to new file_name
        :param bool overwrite: Files will not be overwritten unless is True.
        :return: None.
        :rtype: None
        """
        current_dfa_setting = self.application.display_file_alerts
        path_file_name = Path(file_name)

        # pycatia prefers full path names :-)
        if not path_file_name.is_absolute():
            self.logger.warning('To prevent unexpected behaviour, be explicit and use absolute filenames.')

        if overwrite is False:
            if path_file_name.is_file():
                raise FileExistsError(f'File: {path_file_name} already exists. '
                                      f'Set overwrite=True if you want to overwrite.')
        else:
            self.application.display_file_alerts = False
            # if path_file_name.is_file():
            #     self.logger.warning('File already exists. Click YES in CATIA V5.')

        self.document.SaveAs(path_file_name)

        self.application.display_file_alerts = current_dfa_setting

    def search_for_items(self, selection_objects):
        """
        # todo: This search is currently restricted to GSD objects only.
        Selection objects is a list of items to search for.
        Example: selection_objects = ['Point', 'Line']
        Example query string to search for all lines and points
        "('Generative Shape Design'.Point + 'Generative Shape Design'.Line),in"
        :param list selection_objects:
        :return Selected Automation Object:
        """

        self.logger.warning('This method may be deprecated in future versions.')

        gsd_items = [
            'Point',
            'Line'
        ]

        query_string = str()
        # build query string

        for counter, item in enumerate(selection_objects):
            boolean = str()
            if counter > 0 and not counter == len(selection_objects):
                boolean = ' + '
            if item in gsd_items:
                query_string = f"{query_string}{boolean}'Generative Shape Design'.{item}"

        query_string = f"({query_string}),in"

        selection = self.document.Selection
        selection.Search(query_string)

        selected = list()
        for i in range(0, selection.Count):
            selected.append(AnyObject(selection.Item(i + 1).Value))

        return selected

    def spa_workbench(self) -> SPAWorkbench:
        """
        :return:
        :rtype: SPAWorkbench
        """

        return SPAWorkbench(self.com_object)

    def __repr__(self):
        return f'Document(name="{self.name}")'
