#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2025-09-13 14:18:55.806894

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from pycatia.system_interfaces.any_object import AnyObject


class PageSetup(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PageSetup
                |
                | Represents the page setup.
                | The page setup is the object that stores data which defines how your documents
                | and images are actually printed on paper. This data includes namely the paper
                | size, the orientation, the bottom, top, right, and left margins, the zoom
                | factor, the banner, and the printing quality.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.page_setup = com_object

    @property
    def banner(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property Banner() As CATBSTR
                |     Returns or sets the banner text. The banner text is added to the print and
                |     can include variables, such as the user who prints, the date and time of
                |     printing. Available variables are:
                |
                |     $USER
                |         The user name
                |     $HOST
                |         The workstation name
                |     $SCALE
                |         The print scale
                |     $TIME
                |         The print time
                |     $DATE
                |         The print date
                |     $DAY
                |         The print day
                |     $MONTH
                |         The print month
                |     $YEAR
                |         The print year
                |
                |     The default banner is:
                |
                |      Printed by $USER on $DATE $TIME
                |
                |
                |     Example:
                |         This example sets the banner text to the following:
                |         Printed by $USER at scale $SCALE on $MONTH/$DAY/$YEAR
                |         for the SetupForMyPrint page setup.
                |
                |          SetupForMyPrint.Banner = "Printed by $USER at scale $SCALE on $MONTH/$DAY/$YEAR"

        :return: str
        """

        return self.page_setup.Banner

    @banner.setter
    def banner(self, value: str):
        """
        :param str value:
        """

        self.page_setup.Banner = value

    @property
    def banner_position(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property BannerPosition() As CatBannerPosition
                |     Returns or sets the banner position. The banner can be located on the top,
                |     bottom, left, or right side of the page. catBannerPositionNone removes the
                |     banner.
                |
                |     Example:
                |         This example sets the banner on the top side of the page for the
                |         SetupForMyPrint page setup.
                |
                |          SetupForMyPrint.BannerPosition = CatBannerPositionTop

        :return: int
        """

        return self.page_setup.BannerPosition

    @banner_position.setter
    def banner_position(self, value: int):
        """
        :param int value:
        """

        self.page_setup.BannerPosition = value

    @property
    def banner_size(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property BannerSize() As float
                |     Returns or sets Banner Size. Banner size could range from 0.1 mm to 10.0 mm
                |     Default value is 2.4 mm
                |
                |     Example:
                |         This example sets banner size for the SetupForMyPrint page
                |         setup.
                |
                |          SetupForMyPrint.BannerSize = 1.1

        :return: float
        """

        return self.page_setup.BannerSize

    @banner_size.setter
    def banner_size(self, value: float):
        """
        :param float value:
        """

        self.page_setup.BannerSize = value

    @property
    def bottom(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property Bottom() As float
                |     Returns or sets the lower left corner location with respect to the bottom
                |     of the sheet of paper. This is the distance of the document or the image to
                |     print lower left corner to the paper lower left corner.
                |
                |     Example:
                |         This example sets the location of the lower left corner of the document
                |         or the image to print at 40 mm from the paper lower left corner for the
                |         SetupForMyPrint page setup.
                |
                |          SetupForMyPrint.Bottom = 40

        :return: float
        """

        return self.page_setup.Bottom

    @bottom.setter
    def bottom(self, value: float):
        """
        :param float value:
        """

        self.page_setup.Bottom = value

    @property
    def bottom_margin(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property BottomMargin() As float
                |     Returns or sets the bottom margin. The bottom margin is a strip in which
                |     nothing is printed, located at the bottom of the page, which height is
                |     expressed in mm.
                |
                |     Example:
                |         This example sets the bottom margin for the SetupForMyPrint page setup
                |         to 10 mm.
                |
                |          SetupForMyPrint.BottomMargin = 10

        :return: float
        """

        return self.page_setup.BottomMargin

    @bottom_margin.setter
    def bottom_margin(self, value: float):
        """
        :param float value:
        """

        self.page_setup.BottomMargin = value

    @property
    def color(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property Color() As CatPrintColor
                |     Returns or sets the color mode to use when printing.
                |
                |     Example:
                |         This example sets the color mode to GreyScale for the SetupForMyPrint
                |         page setup.
                |
                |          SetupForMyPrint.Color = catColorGreyScale

        :return: int
        """

        return self.page_setup.Color

    @color.setter
    def color(self, value: int):
        """
        :param int value:
        """

        self.page_setup.Color = value

    @property
    def dpi(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property Dpi() As float
                |     Returns or sets the printing dpi.
                |
                |     Example:
                |         This example sets the printing dpi for the SetupForMyPrint page
                |         setup.
                |
                |          SetupForMyPrint.Dpi = 150.

        :return: float
        """

        return self.page_setup.Dpi

    @dpi.setter
    def dpi(self, value: float):
        """
        :param float value:
        """

        self.page_setup.Dpi = value

    @property
    def gamma(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property Gamma() As float
                |     Returns or sets Gamma factor for print. Gamma value could range from 0.1 to
                |     5.0 Default value is 1.0
                |
                |     Example:
                |         This example sets Gamma factor for the SetupForMyPrint page
                |         setup.
                |
                |          SetupForMyPrint.Gamma = 1.2

        :return: float
        """

        return self.page_setup.Gamma

    @gamma.setter
    def gamma(self, value: float):
        """
        :param float value:
        """

        self.page_setup.Gamma = value

    @property
    def left(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property Left() As float
                |     Returns or sets the lower left corner location with respect to the left of
                |     the sheet of paper. This is the distance of the document or the image to print
                |     lower left corner to the paper lower left corner.
                |
                |     Example:
                |         This example sets the location of the lower left corner of the document
                |         or the image to print at 25 mm from the paper lower left corner for the
                |         SetupForMyPrint page setup.
                |
                |          SetupForMyPrint.Left = 25

        :return: float
        """

        return self.page_setup.Left

    @left.setter
    def left(self, value: float):
        """
        :param float value:
        """

        self.page_setup.Left = value

    @property
    def left_margin(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property LeftMargin() As float
                |     Returns or sets the left margin. The left margin is a strip in which
                |     nothing is printed, located at the left of the page, which width is expressed
                |     in mm.
                |
                |     Example:
                |         This example sets the left margin for the SetupForMyPrint page setup to
                |         10 mm.
                |
                |          SetupForMyPrint.LeftMargin = 10

        :return: float
        """

        return self.page_setup.LeftMargin

    @left_margin.setter
    def left_margin(self, value: float):
        """
        :param float value:
        """

        self.page_setup.LeftMargin = value

    @property
    def line_cap(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property LineCap() As CatPrintLineCap
                |     Returns or sets Line cap for print. Refer to CatPrintLineCap Default value
                |     is catPrintFlat
                |
                |     Example:
                |         This example sets Line cap for the SetupForMyPrint page
                |         setup.
                |
                |          SetupForMyPrint.LineCap = catPrintFlat

        :return: int
        """

        return self.page_setup.LineCap

    @line_cap.setter
    def line_cap(self, value: int):
        """
        :param int value:
        """

        self.page_setup.LineCap = value

    @property
    def line_type_overlapping_check(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property LineTypeOverlappingCheck() As boolean
                |     Returns or sets text Line type overlap check option for print. Default
                |     value is FALSE
                |
                |     Example:
                |         This example sets Line type overlapping check option for the
                |         SetupForMyPrint page setup.
                |
                |          SetupForMyPrint.LineTypeOverlappingCheck = True

        :return: bool
        """

        return self.page_setup.LineTypeOverlappingCheck

    @line_type_overlapping_check.setter
    def line_type_overlapping_check(self, value: bool):
        """
        :param bool value:
        """

        self.page_setup.LineTypeOverlappingCheck = value

    @property
    def line_type_specification(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property LineTypeSpecification() As CatPrintLineSpecification
                |     Returns or sets Line type specification for print. Refer to
                |     CatPrintLineSpecification Default value is
                |     catPrintAbsolute
                |
                |     Example:
                |         This example sets Line type specification for the SetupForMyPrint page
                |         setup.
                |
                |          SetupForMyPrint.LineTypeSpecification = catPrintAbsolute

        :return: int
        """

        return self.page_setup.LineTypeSpecification

    @line_type_specification.setter
    def line_type_specification(self, value: int):
        """
        :param int value:
        """

        self.page_setup.LineTypeSpecification = value

    @property
    def line_width_specification(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property LineWidthSpecification() As CatPrintLineSpecification
                |     Returns or sets Line width specification for print. Refer to
                |     CatPrintLineSpecification Default value is
                |     catPrintAbsolute
                |
                |     Example:
                |         This example sets Line width specification for the SetupForMyPrint page
                |         setup.
                |
                |          SetupForMyPrint.LineWidthSpecification = catPrintAbsolute

        :return: int
        """

        return self.page_setup.LineWidthSpecification

    @line_width_specification.setter
    def line_width_specification(self, value: int):
        """
        :param int value:
        """

        self.page_setup.LineWidthSpecification = value

    @property
    def logo(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property Logo() As CATBSTR
                |     Returns or sets the file containing the logo image. The logo is printed
                |     with the banner.
                |
                |     Example:
                |         This example sets the logo file to the following file:
                |         e:\\users\\psr\\Images\\Logo.tif for the SetupForMyPrint page
                |         setup.
                |
                |          SetupForMyPrint.Logo = "e:\\users\\psr\\Images\\Logo.tif"

        :return: str
        """

        return self.page_setup.Logo

    @logo.setter
    def logo(self, value: str):
        """
        :param str value:
        """

        self.page_setup.Logo = value

    @property
    def logo_visibility(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property LogoVisibility() As boolean
                |     Returns or sets LogoVisibility option for print. Default value is
                |     FALSE
                |
                |     Example:
                |         This example sets LogoVisibility option for the SetupForMyPrint page
                |         setup.
                |
                |          SetupForMyPrint.LogoVisibility = True

        :return: bool
        """

        return self.page_setup.LogoVisibility

    @logo_visibility.setter
    def logo_visibility(self, value: bool):
        """
        :param bool value:
        """

        self.page_setup.LogoVisibility = value

    @property
    def maximum_size(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property MaximumSize() As boolean
                |     Returns or sets whether the document or the image should be printed at the
                |     maximum size with respect to the page size and margins.
                |     True if the document or the image is printed with the maximum size. This
                |     overrides the location properties, that is Left and Bottom, and the Zoom
                |     property values.
                |
                |     Example:
                |         This example requests to print the document or the image with the
                |         SetupForMyPrint page setup at maximum size.
                |
                |          SetupForMyPrint.MaximumSize = True

        :return: bool
        """

        return self.page_setup.MaximumSize

    @maximum_size.setter
    def maximum_size(self, value: bool):
        """
        :param bool value:
        """

        self.page_setup.MaximumSize = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property Orientation() As CatPaperOrientation
                |     Returns or sets the paper orientation.
                |
                |     Example:
                |         This example sets the paper orientation for the SetupForMyPrint page
                |         setup to catPaperLandscape.
                |
                |          SetupForMyPrint.Orientation = catPaperLandscape

        :return: int
        """

        return self.page_setup.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.page_setup.Orientation = value

    @property
    def paper_height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property PaperHeight() As float
                |     Returns or sets the paper height.
                |
                |     Example:
                |         This example sets the page height for the SetupForMyPrint page setup to
                |         297 mm..
                |
                |          SetupForMyPrint.PaperHeight = 297

        :return: float
        """

        return self.page_setup.PaperHeight

    @paper_height.setter
    def paper_height(self, value: float):
        """
        :param float value:
        """

        self.page_setup.PaperHeight = value

    @property
    def paper_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property PaperSize() As CatPaperSize
                |     Returns or sets the paper size.
                |
                |     Example:
                |         This example sets the page size for the SetupForMyPrint page setup to
                |         catPaperA4.
                |
                |          SetupForMyPrint.PaperSize = catPaperA4

        :return: int
        """

        return self.page_setup.PaperSize

    @paper_size.setter
    def paper_size(self, value: int):
        """
        :param int value:
        """

        self.page_setup.PaperSize = value

    @property
    def paper_width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property PaperWidth() As float
                |     Returns or sets the paper width.
                |
                |     Example:
                |         This example sets the page width for the SetupForMyPrint page setup to
                |         210 mm..
                |
                |          SetupForMyPrint.PaperWidth = 210

        :return: float
        """

        return self.page_setup.PaperWidth

    @paper_width.setter
    def paper_width(self, value: float):
        """
        :param float value:
        """

        self.page_setup.PaperWidth = value

    @property
    def print_rendering_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property PrintRenderingMode() As CatPrintRenderingMode
                |     Returns or sets the printing rendering mode.
                |
                |     Example:
                |         This example sets the printing rendering mode for the SetupForMyPrint
                |         page setup.
                |
                |          SetupForMyPrint.PrintRenderingMode = CatPrintRenderingModeDefault

        :return: int
        """

        return self.page_setup.PrintRenderingMode

    @print_rendering_mode.setter
    def print_rendering_mode(self, value: int):
        """
        :param int value:
        """

        self.page_setup.PrintRenderingMode = value

    @property
    def quality(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property Quality() As CatPrintQuality
                |     Returns or sets the printing quality. Refer to
                |     CatPrintQuality
                |
                |     Example:
                |         This example sets the printing quality to draft for the SetupForMyPrint
                |         page setup.
                |
                |          SetupForMyPrint.Quality = catPrintQualityDraft

        :return: int
        """

        return self.page_setup.Quality

    @quality.setter
    def quality(self, value: int):
        """
        :param int value:
        """

        self.page_setup.Quality = value

    @property
    def right_margin(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property RightMargin() As float
                |     Returns or sets the right margin. The right margin is a strip in which
                |     nothing is printed, located at the right of the page, which width is expressed
                |     in mm.
                |
                |     Example:
                |         This example sets the right margin for the SetupForMyPrint page setup
                |         to 12 mm.
                |
                |          SetupForMyPrint.RightMargin = 12

        :return: float
        """

        return self.page_setup.RightMargin

    @right_margin.setter
    def right_margin(self, value: float):
        """
        :param float value:
        """

        self.page_setup.RightMargin = value

    @property
    def rotation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property Rotation() As CatImageRotation
                |     Returns or sets the rotation of the document or the image to print.
                |     Rotations angles can be 0, 90, 180, and 270 degrees counted
                |     clockwise.
                |
                |     Example:
                |         This example sets the rotation to 90 degrees clockwise for the
                |         SetupForMyPrint page setup.
                |
                |          SetupForMyPrint.Rotation = catImageRotation90

        :return: int
        """

        return self.page_setup.Rotation

    @rotation.setter
    def rotation(self, value: int):
        """
        :param int value:
        """

        self.page_setup.Rotation = value

    @property
    def scaling1_to1(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property Scaling1To1() As boolean
                |     Returns or sets whether the document or the image should be printed with a
                |     zoom factor equals to 1 and the image to print lower left corner on the paper
                |     lower corner.
                |     True if the document or the image is printed with the zoom factor equals to
                |     1 and the image to print lower left corner on the paper lower corner. This
                |     overrides the location properties, that is Left and Bottom, and the Zoom
                |     property values.
                |
                |     Example:
                |         This example requests to print the document or the image with the
                |         SetupForMyPrint page setup.
                |
                |          SetupForMyPrint.Scaling1To1 = True

        :return: bool
        """

        return self.page_setup.Scaling1To1

    @scaling1_to1.setter
    def scaling1_to1(self, value: bool):
        """
        :param bool value:
        """

        self.page_setup.Scaling1To1 = value

    @property
    def text_blanking(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property TextBlanking() As boolean
                |     Returns or sets the text blanking option in print Text will be printed in
                |     blanking rectangle Default value is FALSE
                |
                |     Example:
                |         This example sets the text blanking option for the SetupForMyPrint page
                |         setup.
                |
                |          SetupForMyPrint.TextBlanking = True

        :return: bool
        """

        return self.page_setup.TextBlanking

    @text_blanking.setter
    def text_blanking(self, value: bool):
        """
        :param bool value:
        """

        self.page_setup.TextBlanking = value

    @property
    def text_scaling(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property TextScaling() As boolean
                |     Returns or sets text scaling option for print. Default value is
                |     TRUE
                |
                |     Example:
                |         This example sets text scaling option for the SetupForMyPrint page
                |         setup.
                |
                |          SetupForMyPrint.TextScaling = True

        :return: bool
        """

        return self.page_setup.TextScaling

    @text_scaling.setter
    def text_scaling(self, value: bool):
        """
        :param bool value:
        """

        self.page_setup.TextScaling = value

    @property
    def top_margin(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property TopMargin() As float
                |     Returns or sets the top margin. The top margin is a strip in which nothing
                |     is printed, located at the top of the page, which height is expressed in
                |     mm.
                |
                |     Example:
                |         This example sets the top margin for the SetupForMyPrint page setup to
                |         15 mm.
                |
                |          SetupForMyPrint.TopMargin = 15

        :return: float
        """

        return self.page_setup.TopMargin

    @top_margin.setter
    def top_margin(self, value: float):
        """
        :param float value:
        """

        self.page_setup.TopMargin = value

    @property
    def use3_d_accuracy(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property Use3DAccuracy() As boolean
                |     Returns or sets Use3DAccuracy option for print. Default value is
                |     FALSE
                |
                |     Example:
                |         This example sets Use3DAccuracy option for the SetupForMyPrint page
                |         setup.
                |
                |          SetupForMyPrint.Use3DAccuracy = True

        :return: bool
        """

        return self.page_setup.Use3DAccuracy

    @use3_d_accuracy.setter
    def use3_d_accuracy(self, value: bool):
        """
        :param bool value:
        """

        self.page_setup.Use3DAccuracy = value

    @property
    def use_image_size(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property UseImageSize() As boolean
                |     Returns or sets the paper size to the image size.
                |
                |     Example:
                |         This example sets the paper size to image size for the SetupForMyPrint
                |         page setup.
                |
                |          SetupForMyPrint.UseImageSize = True

        :return: bool
        """

        return self.page_setup.UseImageSize

    @use_image_size.setter
    def use_image_size(self, value: bool):
        """
        :param bool value:
        """

        self.page_setup.UseImageSize = value

    @property
    def white_vectors_in_black(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property WhiteVectorsInBlack() As boolean
                |     Returns or sets the white vectors in black option. white vectors will be
                |     printed in black if set to True Default value is TRUE
                |
                |     Example:
                |         This example sets the Print White Vectors In Black option for the
                |         SetupForMyPrint page setup.
                |
                |          SetupForMyPrint.WhiteVectorsInBlack = True

        :return: bool
        """

        return self.page_setup.WhiteVectorsInBlack

    @white_vectors_in_black.setter
    def white_vectors_in_black(self, value: bool):
        """
        :param bool value:
        """

        self.page_setup.WhiteVectorsInBlack = value

    @property
    def zoom(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2025-09-13 14:18:55.806894)
                | Property Zoom() As float
                |     Returns or sets the zoom factor to use when printing.
                |
                |     Example:
                |         This example sets the zoom factor to 1.5 for the SetupForMyPrint page
                |         setup.
                |
                |          SetupForMyPrint.Zoom = 1.5

        :return: float
        """

        return self.page_setup.Zoom

    @zoom.setter
    def zoom(self, value: float):
        """
        :param float value:
        """

        self.page_setup.Zoom = value

    def __repr__(self):
        return f'PageSetup(name="{self.name}")'
