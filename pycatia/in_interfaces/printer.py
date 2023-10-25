#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class Printer(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Printer
                | 
                | Represents a printer handled by the printing subsystem.
                | This object is read only and gives access to some properties of the
                | printer.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.printer = com_object

    @property
    def device_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DeviceName() As CATBSTR (Read Only)
                | 
                |     Returns the printer device name.
                | 
                |     Example:
                |         This example displays the device name of the myPrinter
                |         printer.
                | 
                |          MsgBox myPrinter.DeviceName

        :rtype: str
        """

        return self.printer.DeviceName

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation() As CatPaperOrientation (Read Only)
                | 
                |     Returns or sets the default paper orientation.
                | 
                |     Example:
                |         This example retrieves in DefaultPaperOrientation the default paper
                |         orientation of the myPrinter printer.
                | 
                |          Dim DefaultPaperOrientation As CatPaperOrientation
                |          DefaultPaperOrientation = myPrinter.Orientation

        :return: enum cat_paper_orientation
        :rtype: int
        """

        return self.printer.Orientation

    @property
    def paper_height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PaperHeight() As float (Read Only)
                | 
                |     Returns the default paper height.
                | 
                |     Example:
                |         This example retrieves in Height the default paper height of the
                |         myPrinter printer.
                | 
                |          Dim Height
                |          Height = myPrinter.PaperHeight

        :rtype: float
        """

        return self.printer.PaperHeight

    @property
    def paper_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PaperSize() As CatPaperSize (Read Only)
                | 
                |     Returns the default paper size.
                | 
                |     Example:
                |         This example retrieves in DefaultPaperSize the default paper size of
                |         the myPrinter printer.
                | 
                |          Dim DefaultPaperSize As CatPaperSize
                |          DefaultPaperSize = myPrinter.PaperSize

        :return: enum cat_paper_size
        :rtype: int
        """

        return self.printer.PaperSize

    @property
    def paper_width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PaperWidth() As float (Read Only)
                | 
                |     Returns the default paper width.
                | 
                |     Example:
                |         This example retrieves in Witdh the default paper width of the
                |         myPrinter printer.
                | 
                |          Dim Width As float
                |          Width = myPrinter.PaperWidth

        :rtype: float
        """

        return self.printer.PaperWidth

    def __repr__(self):
        return f'Printer(name="{self.name}")'
