#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

import os
from pathlib import Path

from pycatia.drafting_interfaces.drawing_page_setup import DrawingPageSetup
from pycatia.drafting_interfaces.drawing_views import DrawingViews
from pycatia.drafting_interfaces.print_area import PrintArea
from pycatia.system_interfaces.any_object import AnyObject


class DrawingSheet(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingSheet
                | 
                | Represents a drawing sheet of the drawing document.
                | 
                | The drawing sheet is included in a drawing document and contains drawing
                | views.
                | Warning: This interface is not available with 2D Layout for 3D
                | Design.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_sheet = com_object

    @property
    def gen_views_pos_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GenViewsPosMode() As CatSheetGenViewsPosMode
                | 
                |     Returns or sets the generative views position stability
                |     mode.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example sets the stability mode of the MySheet drawing sheet so
                |         that after an update, existing and unmodified geometries don't move
                |         globally.
                | 
                |          MySheet.GenViewsPosMode = catFixedAxis

        :return: int
        :rtype: int
        """

        return self.drawing_sheet.GenViewsPosMode

    @gen_views_pos_mode.setter
    def gen_views_pos_mode(self, value: int):
        """
        :param int value:
        """

        self.drawing_sheet.GenViewsPosMode = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Orientation() As CatPaperOrientation
                | 
                |     Returns or sets the paper orientation.
                | 
                |     Example:
                |         This example sets the paper orientation for the MySheet drawing sheet
                |         to catPaperLandscape.
                | 
                |          MySheet.Orientation = catPaperLandscape

        :return: int
        :rtype: int
        """

        return self.drawing_sheet.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param enum cat_paper_orientation value:
        """

        self.drawing_sheet.Orientation = value

    @property
    def page_setup(self) -> DrawingPageSetup:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PageSetup() As DrawingPageSetup (Read Only)
                | 
                |     Returns the page setup.
                | 
                |     Example:
                |         This example returns the page setup for the MySheet drawing
                |         sheet.
                | 
                |          Dim MySheetPageSetup As DrawingPageSetup
                |          Set MySheetPageSetup = MySheet.PageSetup

        :return: DrawingPageSetup
        :rtype: DrawingPageSetup
        """

        return DrawingPageSetup(self.drawing_sheet.PageSetup)

    @property
    def paper_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PaperSize() As CatPaperSize
                | 
                |     Returns or sets the paper size.
                | 
                |     Example:
                |         This example sets the page size for the MySheet drawing sheet to
                |         catPaperA4.
                | 
                |          MySheet.PaperSize = catPaperA4

        :return: int
        :rtype: int
        """

        return self.drawing_sheet.PaperSize

    @paper_size.setter
    def paper_size(self, value: int):
        """
        :param int value:
        """

        self.drawing_sheet.PaperSize = value

    @property
    def print_area(self) -> PrintArea:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PrintArea() As PrintArea (Read Only)
                | 
                |     Returns the print area definition object.
                | 
                |     Example:
                |         This example returns the print area for the MySheet drawing
                |         sheet.
                | 
                |          Dim MyPrintArea As PrintArea
                |          Set MyPrintArea = MySheet.PrintArea

        :return: PrintArea
        :rtype: PrintArea
        """

        return PrintArea(self.drawing_sheet.PrintArea)

    @property
    def projection_method(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ProjectionMethod() As CatSheetProjectionMethod
                | 
                |     Returns or sets the sheet projection mode .
                | 
                |     Example:
                |         This example sets the projection mode of the MySheet drawing sheet to
                |         catFirstAngle.
                | 
                |          MySheet.ProjectionMethod = catFirstAngle

        :return: int
        :rtype: int
        """

        return self.drawing_sheet.ProjectionMethod

    @projection_method.setter
    def projection_method(self, value: int):
        """
        :param int value:
        """

        self.drawing_sheet.ProjectionMethod = value

    @property
    def scale(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Scale() As double
                | 
                |     Returns or sets the scale of the drawing sheet.
                | 
                |     Example:
                |         This example sets the scale of the MySheet drawing sheet to
                |         0.5.
                | 
                |          MySheet.Scale = 0.5

        :return: float
        :rtype: float
        """

        return self.drawing_sheet.Scale

    @scale.setter
    def scale(self, value: float):
        """
        :param float value:
        """

        self.drawing_sheet.Scale = value

    @property
    def scale2(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Scale2() As double
                | 
                |     Returns or sets the scale of the drawing sheet (Workaround for VBA
                |     keyword).
                | 
                |     Example:
                |         This example sets the scale of the MySheet drawing sheet to
                |         0.5.
                | 
                |          MySheet.Scale2 = 0.5

        :return: float
        :rtype: float
        """

        return self.drawing_sheet.Scale2

    @scale2.setter
    def scale2(self, value: float):
        """
        :param float value:
        """

        self.drawing_sheet.Scale2 = value

    @property
    def views(self) -> DrawingViews:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Views() As DrawingViews (Read Only)
                | 
                |     Returns the drawing view collection of the drawing sheet.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in ViewCollection the collection of views of the
                |         MySheet drawing sheet.
                | 
                |          Dim ViewCollection As DrawingViews
                |          Set ViewCollection = MySheet.Views

        :return: DrawingViews
        :rtype: DrawingViews
        """

        return DrawingViews(self.drawing_sheet.Views)

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Activate()
                | 
                |     Activates the drawing sheet. Activating a drawing sheet means that this
                |     drawing sheet is the one on which the end user is now working. The window in
                |     the application's window collection which contains this drawing sheet becomes
                |     the active one.
                | 
                |     Example:
                |         This example activates the MySheet drawing sheet.
                | 
                |          MySheet.Activate

        :return: None
        :rtype: None
        """
        return self.drawing_sheet.Activate()

    def force_update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ForceUpdate()
                | 
                |     Forces the update of all the drawing views of the drawing sheet. This
                |     update redraws all the views, whether their pointed objects have been modified
                |     since the drawing sheet creation or last update or not. These pointed objects
                |     can be CATIA Version 4 models, or CATIA Version 5 parts or
                |     assemblies.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example forces the update of all the drawing views in the MySheet
                |         drawing sheet.
                | 
                |          MySheet.ForceUpdate

        :return: None
        :rtype: None
        """
        return self.drawing_sheet.ForceUpdate()

    def generate_dimensions(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GenerateDimensions()
                | 
                |     Generates dimensions in all the drawing views of the drawing sheet. These
                |     dimensions are generated from the constraints of the pointed 3D part(s). One
                |     dimension only is generated for a given constraint. Only dimensions for the
                |     following constraints are generated: distance, length, angle, radius, and
                |     diameter.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example generates the dimensions for all the views in the MySheet
                |         drawing sheet.
                | 
                |          MySheet.GenerateDimensions

        :return: None
        :rtype: None
        """
        return self.drawing_sheet.GenerateDimensions()

    def get_paper_height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPaperHeight() As double
                | 
                |     Gets the paper width of the drawing sheet.
                | 
                |     Parameters:
                | 
                |         oPaperHeight
                | 
                |             Example:
                |                 This example get the height of the
                |                 DrawingSheet1.
                | 
                |                  DrawingSheet1.GetPaperHeight oPaperHeight

        :return: float
        :rtype: float
        """
        return self.drawing_sheet.GetPaperHeight()

    def get_paper_width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPaperWidth() As double
                | 
                |     Gets the paper width of the drawing sheet.
                | 
                |     Parameters:
                | 
                |         oPaperWidth
                | 
                |             Example:
                |                 This example get the width of the
                |                 DrawingSheet1.
                | 
                |                  DrawingSheet1.GetPaperWidth oPaperWidth

        :return: float
        :rtype: float
        """
        return self.drawing_sheet.GetPaperWidth()

    def is_detail(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func IsDetail() As boolean
                | 
                |     Checks whether the sheet is a detail sheet.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                |     TRUE if the sheet is a detail sheet.
                | 
                |     Example:
                |         This example checks whether MySheet is a detail sheet.
                | 
                |          IsDetail = MySheet.IsDetail

        :return: bool
        :rtype: bool
        """
        return self.drawing_sheet.IsDetail()

    def isolate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Isolate()
                | 
                |     Isolates the drawing sheet.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example isolates the MySheet drawing sheet.
                | 
                |          MySheet.Isolate

        :return: None
        :rtype: None
        """
        return self.drawing_sheet.Isolate()

    def print_out(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub PrintOut()
                | 
                |     Prints the drawing sheet according to its page setup on the default
                |     printer.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example prints the DrawingSheet1 on the default
                |         printer.
                | 
                |          DrawingSheet1.PrintOut

        :return: None
        :rtype: None
        """
        return self.drawing_sheet.PrintOut()

    def print_to_file(self, file_name: Path, overwrite=False) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub PrintToFile(CATBSTR fileName)
                | 
                |     Prints the drawing sheet according its page setup in a file instead of
                |     being sent to a printer.
                | 
                |     Parameters:
                | 
                |         fileName
                |             The full pathname of the file receiving the data.
                |             Warning: This method is not available with 2D Layout for 3D Design.
                |             
                | 
                |     Example:
                |         This example prints the DrawingSheet1 in a file.
                | 
                |          DrawingSheet1.PrintToFile "e://temp//sheet1.prn"

        :param Path file_name: file_name including full path.
        :param bool overwrite: Files will not be overwritten unless is True.
        :return: None
        :rtype: None
        """

        if not isinstance(file_name, Path):
            file_name = Path(file_name)

        if str(file_name.parent) == '.':
            self.logger.warning('Full path to print file expected. Assuming current working directory.')
            file_name = Path(os.getcwd(), file_name)

        if not file_name.parent.is_dir():
            raise NotADirectoryError(f'Directory {file_name.parent} is not a directory.')

        if overwrite is False and file_name.is_file():
            raise FileExistsError(f'File: {file_name} already exists. '
                                  f'Set overwrite=True if you want to overwrite.')

        # pycatia prefers full path names :-)
        if not file_name.is_absolute():
            self.logger.warning('To prevent unexpected behaviour, be explicit and use absolute filenames.')

        self.drawing_sheet.PrintToFile(file_name)

    def set_as_detail(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetAsDetail()
                | 
                |     Sets the sheet as a detail sheet. You can now create views into this sheet
                |     that will be taken as details. A detail is made to be reuse as dittos in
                |     views.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example changes the MySheet into a detail sheet.
                | 
                |          MySheet.SetAsDetail

        :return: None
        :rtype: None
        """
        return self.drawing_sheet.SetAsDetail()

    def set_paper_height(self, o_paper_height: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPaperHeight(double oPaperHeight)
                | 
                |     Sets the paper width of the drawing sheet, available on user
                |     format.
                | 
                |     Parameters:
                | 
                |         iPaperHeight
                | 
                |             Example:
                |                 This example set the height of the
                |                 DrawingSheet1.
                | 
                |                  DrawingSheet1.PaperSize = catPaperUser
                |                  DrawingSheet1.SetPaperHeight iPaperHeight

        :param float o_paper_height:
        :return: None
        :rtype: None
        """
        return self.drawing_sheet.SetPaperHeight(o_paper_height)

    def set_paper_width(self, o_paper_width: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPaperWidth(double oPaperWidth)
                | 
                |     Sets the paper width of the drawing sheet, available on user
                |     format.
                | 
                |     Parameters:
                | 
                |         iPaperWidth
                | 
                |             Example:
                |                 This example set the width of the
                |                 DrawingSheet1.
                | 
                |                  DrawingSheet1.PaperSize = catPaperUser
                |                  DrawingSheet1.SetPaperWidth iPaperWidth

        :param float o_paper_width:
        :return: None
        :rtype: None
        """
        return self.drawing_sheet.SetPaperWidth(o_paper_width)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Update()
                | 
                |     Updates the drawing views of the drawing sheet. This update redraws all the
                |     views whose pointed objects have been modified since the drawing sheet creation
                |     or last update, but do not redraw the views whose pointed have not been
                |     modifed. These pointed objects can be CATIA Version 4 models, or CATIA Version
                |     5 parts or assemblies.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example updates the drawing views in the MySheet drawing
                |         sheet.
                | 
                |          MySheet.Update

        :return: None
        :rtype: None
        """
        return self.drawing_sheet.Update()

    def reorder_views(self, i_ordered_views: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub reorder_Views(CATSafeArrayVariant iOrderedViews)
                | 
                |     Changes the positions of the views in this sheet according to the given
                |     ordered list. iOrderedViews is the result of a permutation applied to the list
                |     of all the views of this sheet with the following constraint: the two first
                |     elements of the list must be respectively the sheet's mainview and background
                |     view.
                | 
                |     Example:
                |         This example modifies the views order of a sheet made of a mainview, a
                |         backgroundview and two user-created views. (user-created views are
                |         inverted).
                | 
                |          Set drwviewsorder = CATIA.ActiveDocument.Sheets.ActiveSheet
                |          Set drwviews = drwviewsorder.Views
                |          Set mainview = drwviews.item(1)
                |          Set backview = drwviews.item(2)
                |          Set view1 = drwviews.item(3)
                |          Set view2 = drwviews.item(4)
                |          newvieworder = Array(mainview, backview, view2, view1)
                |          drwviewsorder.reorder_Views(newvieworder)

        :param tuple i_ordered_views:
        :return: None
        :rtype: None
        """
        return self.drawing_sheet.reorder_Views(i_ordered_views)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'reorder_views'
        # # vba_code = """
        # # Public Function reorder_views(drawing_sheet)
        # #     Dim iOrderedViews (2)
        # #     drawing_sheet.reorder_Views iOrderedViews
        # #     reorder_views = iOrderedViews
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DrawingSheet(name="{self.name}")'
