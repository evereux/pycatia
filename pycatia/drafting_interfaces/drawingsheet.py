#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:56:40.651039

from pycatia.system_interfaces.base_object import AnyObject


class DrawingSheet(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents a drawing sheet of the drawing document.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_sheet = com_object

    @property
    def gen_views_pos_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GenViewsPosMode
                | o Property GenViewsPosMode(    ) As
                |
                | Returns or sets the generative views position stability
                | mode. Warning: This method is not available with 2D Layout
                | for 3D Design. Example: This example sets the stability mode
                | of the MySheet drawing sheet so that after an update,
                | existing and unmodified geometries don't move globally.
                | MySheet.GenViewsPosMode = catFixedAxis

        :return:
        """
        return self.drawing_sheet.GenViewsPosMode

    @gen_views_pos_mode.setter
    def gen_views_pos_mode(self, value):
        """
            :param type value:
        """
        self.drawing_sheet.GenViewsPosMode = value

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(    ) As
                |
                | Returns or sets the paper orientation. Example: This example
                | sets the paper orientation for the MySheet drawing sheet to
                | catPaperLandscape. MySheet.Orientation = catPaperLandscape


        :return:
        """
        return self.drawing_sheet.Orientation

    @orientation.setter
    def orientation(self, value):
        """
            :param type value:
        """
        self.drawing_sheet.Orientation = value

    @property
    def page_setup(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PageSetup
                | o Property PageSetup(    ) As   (Read Only)
                |
                | Returns the page setup. Example: This example returns the
                | page setup for the MySheet drawing sheet. Dim
                | MySheetPageSetup As DrawingPageSetup Set MySheetPageSetup =
                | MySheet.PageSetup

        :return:
        """
        return self.drawing_sheet.PageSetup

    @property
    def paper_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PaperSize
                | o Property PaperSize(    ) As
                |
                | Returns or sets the paper size. Example: This example sets
                | the page size for the MySheet drawing sheet to catPaperA4.
                | MySheet.PaperSize = catPaperA4

        :return:
        """
        return self.drawing_sheet.PaperSize

    @paper_size.setter
    def paper_size(self, value):
        """
            :param type value:
        """
        self.drawing_sheet.PaperSize = value

    @property
    def print_area(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PrintArea
                | o Property PrintArea(    ) As   (Read Only)
                |
                | Returns the print area definition object. Example: This
                | example returns the print area for the MySheet drawing
                | sheet. Dim MyPrintArea As PrintArea Set MyPrintArea =
                | MySheet.PrintArea

        :return:
        """
        return self.drawing_sheet.PrintArea

    @property
    def projection_method(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ProjectionMethod
                | o Property ProjectionMethod(    ) As
                |
                | Returns or sets the sheet projection mode . Example: This
                | example sets the projection mode of the MySheet drawing
                | sheet to catFirstAngle. MySheet.ProjectionMethod =
                | catFirstAngle

        :return:
        """
        return self.drawing_sheet.ProjectionMethod

    @projection_method.setter
    def projection_method(self, value):
        """
            :param type value:
        """
        self.drawing_sheet.ProjectionMethod = value

    @property
    def scale(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Scale
                | o Property Scale(    ) As
                |
                | Returns or sets the scale of the drawing sheet. Example:
                | This example sets the scale of the MySheet drawing sheet to
                | 0.5. MySheet.Scale = 0.5

        :return:
        """
        return self.drawing_sheet.Scale

    @scale.setter
    def scale(self, value):
        """
            :param type value:
        """
        self.drawing_sheet.Scale = value

    @property
    def scale2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Scale2
                | o Property Scale2(    ) As
                |
                | Returns or sets the scale of the drawing sheet (Workaround
                | for VBA keyword). Example: This example sets the scale of
                | the MySheet drawing sheet to 0.5. MySheet.Scale2 = 0.5

        :return:
        """
        return self.drawing_sheet.Scale2

    @scale2.setter
    def scale2(self, value):
        """
            :param type value:
        """
        self.drawing_sheet.Scale2 = value

    @property
    def views(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Views
                | o Property Views(    ) As   (Read Only)
                |
                | Returns the drawing view collection of the drawing sheet.
                | Warning: This method is not available with 2D Layout for 3D
                | Design. Example: This example retrieves in ViewCollection
                | the collection of views of the MySheet drawing sheet. Dim
                | ViewCollection As DrawingViews Set ViewCollection =
                | MySheet.Views

        :return:
        """
        return self.drawing_sheet.Views

    def activate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Activate
                | o Sub Activate(    )
                |
                | Activates the drawing sheet. Activating a drawing sheet
                | means that this drawing sheet is the one on which the end
                | user is now working. The window in the application's window
                | collection which contains this drawing sheet becomes the
                | active one. Example: This example activates the MySheet
                | drawing sheet. MySheet.Activate

        :return:
        """
        return self.drawing_sheet.Activate()

    def force_update(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ForceUpdate
                | o Sub ForceUpdate(    )
                |
                | Forces the update of all the drawing views of the drawing
                | sheet. This update redraws all the views, whether their
                | pointed objects have been modified since the drawing sheet
                | creation or last update or not. These pointed objects can be
                | CATIA Version 4 models, or CATIA Version 5 parts or
                | assemblies. Warning: This method is not available with 2D
                | Layout for 3D Design. Example: This example forces the
                | update of all the dawing views in the MySheet drawing sheet.
                | MySheet.ForceUpdate

        :return:
        """
        return self.drawing_sheet.ForceUpdate()

    def generate_dimensions(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GenerateDimensions
                | o Sub GenerateDimensions(    )
                |
                | Generates dimensions in all the drawing views of the drawing
                | sheet. These dimensions are generated from the constraints
                | of the pointed 3D part(s). One dimension only is generated
                | for a given constraint. Only dimensions for the following
                | constraints are generated: distance, length, angle, radius,
                | and diameter. Warning: This method is not available with 2D
                | Layout for 3D Design. Example: This example generates the
                | dimensions for all the views in the MySheet drawing sheet.
                | MySheet.GenerateDimensions

        :return:
        """
        return self.drawing_sheet.GenerateDimensions()

    def get_paper_height(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPaperHeight
                | o Func GetPaperHeight(    ) As
                |
                | Gets the paper width of the drawing sheet.
                |
                | Parameters:
                | oPaperHeight
                |
                | Examples:
                | This example get the height of the DrawingSheet1.
                | DrawingSheet1.GetPaperHeight oPaperHeight

        :return:
        """
        return self.drawing_sheet.GetPaperHeight()

    def get_paper_width(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPaperWidth
                | o Func GetPaperWidth(    ) As
                |
                | Gets the paper width of the drawing sheet.
                |
                | Parameters:
                | oPaperWidth
                |
                | Examples:
                | This example get the width of the DrawingSheet1.
                | DrawingSheet1.GetPaperWidth oPaperWidth

        :return:
        """
        return self.drawing_sheet.GetPaperWidth()

    def is_detail(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsDetail
                | o Func IsDetail(    ) As
                |
                | Checks whether the sheet is a detail sheet. Warning: This
                | method is not available with 2D Layout for 3D Design. TRUE
                | if the sheet is a detail sheet. Example: This example checks
                | whether MySheet is a detail sheet. IsDetail =
                | MySheet.IsDetail

        :return:
        """
        return self.drawing_sheet.IsDetail()

    def isolate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Isolate
                | o Sub Isolate(    )
                |
                | Isolates the drawing sheet. Warning: This method is not
                | available with 2D Layout for 3D Design. Example: This
                | example isolates the MySheet drawing sheet. MySheet.Isolate

        :return:
        """
        return self.drawing_sheet.Isolate()

    def print_out(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PrintOut
                | o Sub PrintOut(    )
                |
                | Prints the drawing sheet according to its page setup on the
                | default printer. Warning: This method is not available with
                | 2D Layout for 3D Design. Example: This example prints the
                | DrawingSheet1 on the default printer. DrawingSheet1.PrintOut

        :return:
        """
        return self.drawing_sheet.PrintOut()

    def print_to_file(self, file_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | PrintToFile
                | o Sub PrintToFile(        fileName)
                |
                | Prints the drawing sheet according its page setup in a file
                | instead of being sent to a printer.
                |
                | Parameters:
                | fileName
                |    The full pathname of the file receiving the data.
                |  Warning: This method is not available with 2D Layout for 3D Design.
                |
                | Examples:
                | This example prints the DrawingSheet1 in a file.
                | DrawingSheet1.PrintToFile "e:\\temp\\sheet1.prn"

        :param file_name:
        :return:
        """
        return self.drawing_sheet.PrintToFile(file_name)

    def set_as_detail(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAsDetail
                | o Sub SetAsDetail(    )
                |
                | Sets the sheet as a detail sheet. You can now create views
                | into this sheet that will be taken as details. A detail is
                | made to be reuse as dittos in views. Warning: This method is
                | not available with 2D Layout for 3D Design. Example: This
                | example changes the MySheet into a detail sheet.
                | MySheet.SetAsDetail

        :return:
        """
        return self.drawing_sheet.SetAsDetail()

    def set_paper_height(self, o_paper_height):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPaperHeight
                | o Sub SetPaperHeight(        oPaperHeight)
                |
                | Sets the paper width of the drawing sheet, avalaible on user
                | format.
                |
                | Parameters:
                | iPaperHeight
                |
                | Examples:
                | This example set the height of the DrawingSheet1.
                | DrawingSheet1.PaperSize = catPaperUser
                | DrawingSheet1.SetPaperHeight iPaperHeight

        :param o_paper_height:
        :return:
        """
        return self.drawing_sheet.SetPaperHeight(o_paper_height)

    def set_paper_width(self, o_paper_width):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPaperWidth
                | o Sub SetPaperWidth(        oPaperWidth)
                |
                | Sets the paper width of the drawing sheet, avalaible on user
                | format.
                |
                | Parameters:
                | iPaperWidth
                |
                | Examples:
                | This example set the width of the DrawingSheet1.
                | DrawingSheet1.PaperSize = catPaperUser
                | DrawingSheet1.SetPaperWidth iPaperWidth

        :param o_paper_width:
        :return:
        """
        return self.drawing_sheet.SetPaperWidth(o_paper_width)

    def update(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Update
                | o Sub Update(    )
                |
                | Updates the drawing views of the drawing sheet. This update
                | redraws all the views whose pointed objects have been
                | modified since the drawing sheet creation or last update,
                | but do not redraw the views whose pointed have not been
                | modifed. These pointed objects can be CATIA Version 4
                | models, or CATIA Version 5 parts or assemblies. Warning:
                | This method is not available with 2D Layout for 3D Design.
                | Example: This example updates the drawing views in the
                | MySheet drawing sheet. MySheet.Update

        :return:
        """
        return self.drawing_sheet.Update()

    def reorder__views(self, i_ordered_views):
        """
        .. note::
            CAA V5 Visual Basic help

                | reorder_Views
                | o Sub reorder_Views(        iOrderedViews)
                |
                | Changes the positions of the views in this sheet according
                | to the given ordered list. iOrderedViews is the result of a
                | permutation applied to the list of all the views of this
                | sheet with the following constraint: the two first elements
                | of the list must be respectively the sheet's mainview and
                | background view. Example: This example modifies the views
                | order of a sheet made of a mainview, a backgroundview and
                | two user-created views. (user-created views are inverted).
                | Set drwviewsorder = CATIA.ActiveDocument.Sheets.ActiveSheet
                | Set drwviews = drwviewsorder.Views Set mainview =
                | drwviews.item(1) Set backview = drwviews.item(2) Set view1 =
                | drwviews.item(3) Set view2 = drwviews.item(4) newvieworder =
                | Array(mainview, backview, view2, view1)
                | drwviewsorder.reorder_Views(newvieworder)

        :param i_ordered_views:
        :return:
        """
        return self.drawing_sheet.reorder_Views(i_ordered_views)

    def __repr__(self):
        return f'DrawingSheet(name="{self.name}")'
