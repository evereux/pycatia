#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25

from pycatia.in_interfaces.pagesetup import PageSetup


class DrawingPageSetup(PageSetup):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the page setup for the drawing documents.The page setup is
                | the object that stores data which defines how your documents and
                | images are actually printed on paper.  This data includes namely the
                | paper size, the orientation, the bottom, top, right, and left margins,
                | the zoom factor, the banner, the printing quality, the choice of the
                | best orientation, and the choice to fit either the drawing sheet
                | format or the printer format.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_page_setup = com_object

    @property
    def choose_best_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ChooseBestOrientation
                | o Property ChooseBestOrientation(    ) As
                | 
                | Activates or deactivates the choice of the best orientation. Example:
                | This example requests the best orientation to be chosen for MySheet.
                | MySheet.DrawingPageSetUp.ChooseBestOrientation = TRUE

        :return: bool
        """
        return self.drawing_page_setup.ChooseBestOrientation

    @choose_best_orientation.setter
    def choose_best_orientation(self, value):
        self.drawing_page_setup.ChooseBestOrientation = value

    @property
    def fit_to_printer_format(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FitToPrinterFormat
                | o Property FitToPrinterFormat(    ) As
                | 
                | Fits the format of the print to the printer format. Example: This
                | example turns this calculation on.
                | MySheet.DrawingPageSetUp.FitToPrinterFormat = TRUE

        :return: bool
        """
        return self.drawing_page_setup.FitToPrinterFormat

    @property
    def fit_to_sheet_format(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FitToSheetFormat
                | o Property FitToSheetFormat(    ) As
                | 
                | Fits the format of the print to the sheet format. Example: This
                | example turns this calculation on.
                | MySheet.DrawingPageSetUp.FitToSheetFormat = TRUE

        :return: bool
        """
        return self.drawing_page_setup.FitToSheetFormat

    def __repr__(self):
        return f'DrawingPageSetup()'
