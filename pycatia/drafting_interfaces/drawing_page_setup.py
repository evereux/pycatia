#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.page_setup import PageSetup


class DrawingPageSetup(PageSetup):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.PageSetup
                |                         DrawingPageSetup
                | 
                | Represents the page setup for the drawing documents.
                | 
                | The page setup is the object that stores data which defines how your documents
                | and images are actually printed on paper. This data includes namely the paper
                | size, the orientation, the bottom, top, right, and left margins, the zoom
                | factor, the banner, the printing quality, the choice of the best orientation,
                | and the choice to fit either the drawing sheet format or the printer
                | format.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_page_setup = com_object

    @property
    def choose_best_orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ChooseBestOrientation() As boolean
                | 
                |     Activates or deactivates the choice of the best
                |     orientation.
                | 
                |     Example:
                |         This example requests the best orientation to be chosen for
                |         MySheet.
                | 
                |          MySheet.DrawingPageSetUp.ChooseBestOrientation = TRUE

        :rtype: bool
        """

        return self.drawing_page_setup.ChooseBestOrientation

    @choose_best_orientation.setter
    def choose_best_orientation(self, value: bool):
        """
        :param bool value:
        """

        self.drawing_page_setup.ChooseBestOrientation = value

    @property
    def fit_to_printer_format(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FitToPrinterFormat() As boolean
                | 
                |     Fits the format of the print to the printer format.
                | 
                |     Example:
                |         This example turns this calculation on.
                | 
                |          MySheet.DrawingPageSetUp.FitToPrinterFormat = TRUE

        :rtype: bool
        """

        return self.drawing_page_setup.FitToPrinterFormat

    @fit_to_printer_format.setter
    def fit_to_printer_format(self, value: bool):
        """
        :param bool value:
        """

        self.drawing_page_setup.FitToPrinterFormat = value

    @property
    def fit_to_sheet_format(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FitToSheetFormat() As boolean
                | 
                |     Fits the format of the print to the sheet format.
                | 
                |     Example:
                |         This example turns this calculation on.
                | 
                |          MySheet.DrawingPageSetUp.FitToSheetFormat = TRUE

        :rtype: bool
        """

        return self.drawing_page_setup.FitToSheetFormat

    @fit_to_sheet_format.setter
    def fit_to_sheet_format(self, value: bool):
        """
        :param bool value:
        """

        self.drawing_page_setup.FitToSheetFormat = value

    def __repr__(self):
        return f'DrawingPageSetup(name="{ self.name }")'
