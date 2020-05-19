#! /usr/bin/python3.6

from pywintypes import com_error

from pycatia.exception_handling import CATIAApplicationException

paper_sizes = [
    'catPaperLetter',  # [0]
    'catPaperLegal',  # [1]
    'catPaperA0',  # [2]
    'catPaperA1',  # [3]
    'catPaperA2',  # [4]
    'catPaperA3',  # [5]
    'catPaperA4',  # [6]
    'catPaperA',  # [7]
    'catPaperB',  # [8]
    'catPaperC',  # [9]
    'catPaperD',  # [10]
    'catPaperE',  # [11]
    'catPaperF',  # [12]
    'catPaperUser',  # [13]
]

drawing_orientation = [
    'catPaperPortrait',
    'catPaperLandscape',
    'catPaperBestFit',
]


class DrawingRoot:
    """

    """

    def __init__(self, catia):
        """

        :param catia: :class:`CATIAApplication()`
        """

        # the DrawingRoot COM object
        self.drawing_root = catia.catia.ActiveDocument.DrawingRoot

    @property
    def active_sheet(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Property ActiveSheet( ) As DrawingSheet

            | Retrieves or sets the active sheet of the drawing.
            | Warning: This method is not available with 2D Layout for 3D Design.
            | Example:
            |   This example retrieves the active sheet in the drawing of the active document, supposed to be a drawing
            |   document.
            |       CATIA.ActiveDocument.DrawingRoot.ActiveSheet


        :return:
        """

        return self.drawing_root.ActiveSheet

    @property
    def parameters(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Property Parameters( ) As Parameters (Read Only)

            | Returns the collection of parameters of the drawing document.
            | Warning: This method is not available with 2D Layout for 3D Design.
            | Example:
            |   This example retrieves in DrawingParameters the collection of parameters currently managed by the
            |   active document, supposed to be a drawing document.
            |       Dim DrawingParameters As Parameters
            |       Set DrawingParameters = CATIA.ActiveDocument.Parameters


        :return:
        """

        return self.drawing_root.Parameters

    @property
    def relations(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Property Relations( ) As Relations (Read Only)

            | Returns the collection of relations of the drawing document.
            | Warning: This method is not available with 2D Layout for 3D Design.
            | Example:
            |   This example retrieves in DrawingRelations the collection of relations currently managed by the active
            |   document, supposed to be a drawing document.
            |       Dim DrawingRelations As Relations
            |       Set DrawingRelations = CATIA.ActiveDocument.Relations

        :return:
        """

        return self.drawing_root.Relations

    @property
    def sheets(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Property Sheets( ) As DrawingSheets (Read Only)

            |Returns the collection of drawing sheets of the drawing document.
            |Warning: This method is not available with 2D Layout for 3D Design.
            |Example:
            |   This example retrieves in SheetCollection the collection of sheets currently managed by the active
            |   document, supposed to be a drawing document.
            |       Dim SheetCollection As DrawingSheets
            |       Set SheetCollection = CATIA.ActiveDocument.Sheets


        :return:
        """

        _sheets = list()
        com_sheets = self.drawing_root.Sheets

        for item in range(com_sheets.Count):
            _sheets.append(DrawingSheet(com_sheets.Item(item + 1)))

        return _sheets

    @property
    def standard(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Property Standard( ) As CatDrawingStandard

            | Returns or sets the drawing standard of the drawing document.
            | Warning: This method is not available with 2D Layout for 3D Design.
            | Example:
            |   This example sets the drawing standard of the active document, supposed to be a drawing document, to
            |   ISO.
            |       CATIA.ActiveDocument.Standard = catISO


            .. note::
            CAA V5 Visual Basic help

            | CatDrawingStandard (Enumeration)
            | enum CatDrawingStandard {
            |   catANSI,
            |   catISO,
            |   catJIS
            | }
            |
            | The standard for the drawing document.
            |
            | Values:
            |     catANSI
            | The standard is ANSI
            |     catISO
            | The standard is ISO
            |     catJIS
            | The standard is JIS


        :return:
        """

        standards = ['ANSI', 'ISO', 'JIS']

        return standards[self.drawing_root.Standard]

    def isolate(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Sub Isolate( )

            | Isolates all the drawing views of all the drawing sheets of the drawing document.
            | Warning: This method is not available with 2D Layout for 3D Design.
            | Example:
            |   This example isolates all the drawing views of all the drawing sheets of the active document, supposed
            |   to be a drawing document.
            |       CATIA.ActiveDocument.Isolate

        :return:
        """

        self.drawing_root.Isolate()

    def update(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Sub Update( )

            | Updates all the drawing sheets of the drawing document.
            | Warning: This method is not available with 2D Layout for 3D Design.
            | Example:
            |   This example updates the active document, supposed to be a drawing document.
            |       CATIA.ActiveDocument.Update

        :return:
        """

        self.drawing_root.Update()

    def reorder_sheets(self, new_sheet_order):
        """
        .. note::
            CAA V5 Visual Basic help

            Sub reorder_Sheets( CATSafeArrayVariant  iOrderedSheets)

            | Changes the positions of the sheets in this drawing according to the given ordered list. iOrderedSheets
            | is the result of a permutation applied to the list of all the sheets of this drawing, with the following
            | constraint: For every non-detail sheet, there is not any detail sheet appearing before in iOrderedSheets.
            | Example:
            |   This example inverts the sheet order of a drawing made of exactly two regular sheets.
            |       Set drwsheets = CATIA.ActiveDocument.Sheets
            |       Set drwsheetsorder =  CATIA.ActiveDocument.DrawingRoot
            |       Set sheet1 = drwsheets.item(1)
            |       Set sheet2 = drwsheets.item(2)
            |       newsheetorder = Array(sheet2, sheet1)
            |       drwsheetsorder.reorder_Sheets(newsheetorder)


        :param new_sheet_order:
        :return:
        """

        self.drawing_root.reorder_Sheets(new_sheet_order)


class DrawingSheet:
    """

    """

    def __init__(self, drawing_sheet):
        """

        :param drawing_sheet: the DrawingSheet COM object.
        """

        self.sheet = drawing_sheet

    @property
    def name(self):
        return self.sheet.Name

    @name.setter
    def name(self, name):
        self.sheet.Name = name

    @property
    def orientation(self):
        """
        CAA V5 Visual Basic help

        Property Orientation( ) As CatPaperOrientation

        | Returns or sets the paper orientation.
        | Example:
        |   This example sets the paper orientation for the MySheet drawing sheet to catPaperLandscape.
        |       MySheet.Orientation = catPaperLandscape

        :return:
        """

        return drawing_orientation[self.sheet.Orientation]

    # noinspection PyShadowingNames
    @orientation.setter
    def orientation(self, drawing_orientation):
        """

        :param int drawing_orientation: ['catPaperPortrait', 'catPaperLandscape', 'catPaperBestFit']
        :return:
        """
        self.sheet.Orientation = drawing_orientation

    @property
    def scale(self):
        return self.sheet.Scale

    @scale.setter
    def scale(self, scale):
        self.sheet.Scale = scale

    @property
    def paper_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Property PaperSize( ) As CatPaperSize

            | Returns or sets the paper size.
            | Example:
            |   This example sets the page size for the MySheet drawing sheet to catPaperA4.
            |       MySheet.PaperSize = catPaperA4


        .. note::
            CAA V5 Visual Basic help

            | CatPaperSize (Enumeration)
            | enum CatPaperSize {
            |   catPaperLetter,
            |   catPaperLegal,
            |   catPaperA0,
            |   catPaperA1,
            |   catPaperA2,
            |   catPaperA3,
            |   catPaperA4,
            |   catPaperA,
            |   catPaperB,
            |   catPaperC,
            |   catPaperD,
            |   catPaperE,
            |   catPaperF,
            |   catPaperUser
            | }
            |
            | Paper size.
            | It used by the PageSetup object for document printing.
            | Values:
            |   catPaperLetter
            |       The US Letter format (8.5 x 11")
            |   catPaperLegal
            |       The Legal format (8.5 x 14")
            |   catPaperA0
            |       The A0 ISO format (841 x 1189 mm)
            |   catPaperA1
            |       The A1 ISO format (594 x 841 mm)
            |   catPaperA2
            |       The A2 ISO format (420 x 594 mm)
            |   catPaperA3
            |       The A3 ISO format (297 x 420 mm)
            |   catPaperA4
            |       The A4 ISO format (210 x 297 mm)
            |   catPaperA
            |       The A ANSI format (8.5 x 11")
            |   catPaperB
            |       The B ANSI format (11 x 17")
            |   catPaperC
            |       The C ANSI format (17 x 22")
            |   catPaperD
            |       The D ANSI format (22 x 34")
            |   catPaperE
            |       The E ANSI format (34 x 44")
            |   catPaperF
            |       The F ANSI format (28 x 40")
            |   catPaperUser
            |       The customized format


        :return:
        """

        return self.sheet.PaperSize

    @paper_size.setter
    def paper_size(self, paper_size):

        try:
            self.sheet.PaperSize = paper_size
        except com_error:
            raise CATIAApplicationException('Ensure paper_size is available for the drawing standard.')

    @property
    def project_method(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Property ProjectionMethod( ) As CatSheetProjectionMethod

            | Returns or sets the sheet projection mode .
            | Example:
            |   This example sets the projection mode of the MySheet drawing sheet to catFirstAngle.
            |       MySheet.ProjectionMethod = catFirstAngle


        .. note::
            CAA V5 Visual Basic help

            | CatSheetProjectionMethod (Enumeration)
            | enum CatSheetProjectionMethod {
            |   catFirstAngle,
            |   catThirdAngle
            | }
            |
            | Sheet projection Method.
            |
            | Values:
            |   catFirstAngle
            |       The views are created using first angle standard
            |   catThirdAngle
            |       The views are created using third angle standard

        :return:
        """

        values = ['FirstAngle', 'ThirdAngle']

        return values[self.sheet.ProjectionMethod]

    @property
    def views(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Property Views( ) As DrawingViews (Read Only)

            | Returns the drawing view collection of the drawing sheet.
            | Warning: This method is not available with 2D Layout for 3D Design.
            | Example:
            |   This example retrieves in ViewCollection the collection of views of the MySheet drawing sheet.
            |       Dim ViewCollection As DrawingViews
            |       Set ViewCollection = MySheet.Views


        :return:
        """

        return Views(self.sheet.Views)


class Views:

    def __init__(self, views):
        """

        .. note::
            CAA V5 Visual Basic help

            A collection of all the drawing views currently managed by a drawing sheet in a drawing document.


        :param views: the DrawingViews COM object
        """

        self.views = views

    @property
    def active_view(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Property ActiveView( ) As DrawingView (Read Only)

            | Returns the active drawing view of the active drawing sheet.
            | Warning: This method is not available with 2D Layout for 3D Design.
            |   Example:
            |   The following example retrieves in ViewToWorkIn the active drawing view in the DrawingSheets collection
            |   of the document named CATDrawing1
            |       Dim MyDrawingDoc As Document
            |       Set MyDrawingDoc = CATIA.Documents.Item("CATDrawing1")
            |       Dim ViewToWorkIn As DrawingView
            |       Set ViewToWorkIn = MyDrawingDoc.Sheets.ActiveSheet.DrawingViews.ActiveView


        :return:
        """

        return DrawingView(self.views.ActiveView)

    def view_list(self):
        """

        :return:
        """

        # todo: return a list of views.

    def get_view_by_name(self, view_name):
        """

        :param str view_name:
        :return:
        """

        return DrawingView(self.views.Item(view_name))


class DrawingView:
    """

    """

    def __init__(self, drawing_view):
        """
        .. note::
            CAA V5 Visual Basic help

            Represents a drawing view in a drawing sheet.

            | The drawing view is included in a drawing sheet and contains texts,leaders, dimensions, arrows, pictures,
            | tables, 2D Geometry and 2D component.
            | Warning: This interface is not available with 2D Layout for 3D Design.


        :param drawing_view: the DrawingView COM object
        :return:
        """

        self.drawing_view = drawing_view

    @property
    def name(self):
        return self.drawing_view.Name

    @name.setter
    def name(self, name):
        self.drawing_view.Name = name

    @property
    def scale(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Property Scale( ) As double

            | Returns or sets the scale of the drawing view.
            | Warning: This method is not available with 2D Layout for 3D Design.
            | Example:
            |   This example sets the scale of the MyView drawing view to 0.5.
            |       MyView.Scale = 0.5


        :return: float
        """
        return self.drawing_view.Scale

    @scale.setter
    def scale(self, scale):
        self.drawing_view.Scale = scale

    def activate(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Sub Activate( )

            | Activates the drawing view. Activating a drawing view means that this drawing view is the one on which
            | the end-user is now working.
            | Warning: This method is not available with 2D Layout for 3D Design.
            | Example:
            |   This example activates the ViewToWorkOn drawing view.
            |       ViewToWorkOn.Activate()



        :return:
        """

        self.drawing_view.Activate()

    @property
    def generative_view_behaviour(self):
        """
        .. note::
            CAA V5 Visual Basic help

            Property GenerativeBehavior( ) As DrawingViewGenerativeBehavior (Read Only)

            | Returns the generative behavior of the drawing view.
            | Warning: This method is not available with 2D Layout for 3D Design.
            | Example:
            |   This example retrieves in MyViewGenBehavior the generative behavior of the MyView drawing view.
            |       Dim MyViewGenBehavior As DrawingViewGenerativeBehavior
            |       Set MyViewGenBehavior = MyView.GenerativeBehavior


        :return:
        """

        return self.drawing_view.GenerativeBehavior

    def get_view_name(self):
        """
        .. note::
            CAA V5 Visual Basic help

            | Sub GetViewName( CATBSTR  iViewNamePrefix,
            |                  CATBSTR  iViewNameIdent,
            |                  CATBSTR  iViewNameSuffix)
            |
            | Returns the prefix, the ident and the suffix of the name of the drawing view. The method returns an error
            | in case of 2D component reference.
            | Note: Prefix of drawing view can be also retrieved across name property defined in CATIABase
            | Warning: This method is not available with 2D Layout for 3D Design.
            | Example:
            |   This example gets the prefix, the ident, and the suffix of the name of the MyView drawing view
            |       Dim MyPrefix, MyIdent, MySuffix As CATBSTR
            |       MyView.GetViewName (MyPrefix, MyIdent, MySuffix)


        :return: tuple(prefix, ident, suffix)
        """
        return self.drawing_view.GetViewName()

    def set_view_name(self, prefix, ident, suffix):
        """
        .. note::
            CAA V5 Visual Basic help

            | Sub SetViewName( CATBSTR  iViewNamePrefix,
            |                  CATBSTR  iViewNameIdent,
            |                  CATBSTR  iViewNameSuffix)
            |
            | Sets the prefix, the ident and the suffix of the name of the drawing view. The method returns an error in
            | case of 2D component reference.
            | Note: Prefix of drawing view can be also modified across name property defined in CATIABase
            | Warning: This method is not available with 2D Layout for 3D Design.
            | Example:
            |   This example sets the prefix, the ident, and the suffix of the name of the MyView drawing view
            |   respectively to "MyPrefix", "MyIdent", and "MySuffix".
            |       MyView.SetViewName ("MyPrefix", "MyIdent", "MySuffix")


        .. warning::
            The view name will not update in the view tree. But if part is saved and reopened the view name is updated.


        :param str prefix:
        :param str ident:
        :param str suffix:
        :return:
        """

        self.drawing_view.SetViewName(prefix, ident, suffix)
