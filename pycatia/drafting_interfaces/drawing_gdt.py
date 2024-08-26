#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.drafting_interfaces.drawing_leaders import DrawingLeaders
from pycatia.drafting_interfaces.drawing_text_properties import DrawingTextProperties
from pycatia.drafting_interfaces.drawing_text_range import DrawingTextRange
from pycatia.system_interfaces.any_object import AnyObject


class DrawingGDT(AnyObject):
    """

    Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingGDT
                |
                | Represents a drawing GDT in a drawing view.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_gdt = com_object

    @property
    def angle(self) -> float:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property Angle() As double
                |     Returns or sets the angle of the drawing GDT. The angle is measured between
                |     the axis system of the drawing view and the local axis system of the drawing
                |     GDT. The angle is measured in radians and is counted
                |     counterclockwise.
                |
                |     Example:
                |         This example sets the angle of the MyGDT drawing GDT to 90 degrees
                |         clockwise. You first need to compute the angle in degrees and set the minus
                |         sign to indicate the rotation is clockwise.
                |
                |          Angle90Clockwise = -90
                |          MyGDT.Angle = Angle90Clockwise

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_gdt.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.drawing_gdt.Angle = value

    @property
    def leaders(self) -> DrawingLeaders:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property Leaders() As DrawingLeaders (Read Only)
                |     Returns the drawing leader collection of the drawing GDT.
                |
                |     Example:
                |         This example retrieves in LeaderCollection the collection of leaders of
                |         the MyGDT drawing GDT.
                |
                |          Dim LeaderCollection As DrawingLeaders
                |          Set LeaderCollection = MyGDT.Leaders

        :rtype: DrawingLeaders
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return DrawingLeaders(self.drawing_gdt.Leaders)

    @property
    def row_number(self) -> int:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property RowNumber() As long (Read Only)
                |     Returns the number of lines in the GDT
                |
                |     Returns:
                |         The number of line in the GDT
                |
                |         Example:
                |             This example retrieves in rowNumber the row number of the MyGDT
                |             drawing GDT
                |
                |              rowNumber = MyGDT.RowNumber

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_gdt.RowNumber

    @property
    def text_properties(self) -> DrawingTextProperties:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property TextProperties() As DrawingTextProperties (Read Only)
                |     Returns the text properties of the drawing GDT.
                |
                |     Example:
                |         This example retrieves in TextProperties the text properties of the
                |         MyGDT drawing GDT..
                |
                |          Dim TextProperties As DrawingTextProperties
                |          Set TextProperties = MyGDT.TextProperties

        :rtype: DrawingTextProperties
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return DrawingTextProperties(self.drawing_gdt.TextProperties)

    @property
    def x(self) -> float:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property x() As double
                |     Returns or sets the x coordinate of the drawing GDT. It is expressed with
                |     respect to the current view coordinate system. This coordinate, like any
                |     length, is measured in millimeters.
                |
                |     Example:
                |         This example retrieves in X the x coordinate of the MyGDT drawing
                |         GDT.
                |
                |          X = MyGDT.x

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_gdt.x

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.drawing_gdt.x = value

    @property
    def y(self) -> float:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property y() As double
                |     Returns or sets the y coordinate of the drawing GDT. It is expressed with
                |     respect to the current view coordinate system. This coordinate, like any
                |     length, is measured in millimeters.
                |
                |     Example:
                |         This example sets the y coordinate of the MyGDT drawing GDT to 5
                |         inches. You need first to convert the 5 inches into
                |         millmeters.
                |
                |          NewYCoordinate = 5*25.4/1000
                |          MyGDT.y = NewYCoordinate

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_gdt.y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.drawing_gdt.y = value

    def get_reference_number(self, i_row_number: int) -> int:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetReferenceNumber(long iRowNumber) As long
                |     Returns the number of references in a row of the GDT.
                |
                |     Parameters:
                |
                |         iRowNumber
                |             The number of the row to analyse.
                |
                |     Returns:
                |         The number of references in this row.
                |
                |         Example:
                |             This example gets the reference number of the MyGDT drawing
                |             GDT
                |
                |              MyGDT.GetReferenceNumber(iRowNumber, oRefNumber)

        :param int i_row_number:
        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_gdt.GetReferenceNumber(i_row_number)

    def get_text_range(self, i_row_number: int, i_number: int) -> DrawingTextRange:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetTextRange(long iRowNumber,long iNumber) As
                | DrawingTextRange
                |     Returns the CATIADrawingTextRange of tolerance value and reference
                |     value.
                |
                |     Parameters:
                |
                |         iRowNumber
                |             The number of the row to analyse If iRowNumber equals 0 to analyse
                |             upper text or lower text. If iRowNumber is greater than 0 analyse tolerance
                |             value or reference value.
                |         iNumber
                |             The modifier to analyse in this row:
                |             If iRowNumber equals 0 and iNumber = 0 represent upper text
                |             If iRowNumber equals 0 and iNumber = 1 represent lower text
                |             If iRowNumber is greater than 0 and iNumber equals 0 to analyse tolerance value
                |             If iRowNumber is greater than 0 and iNumber is greater than 0 to analyse reference value.
                |
                |     Returns:
                |         The CATIADrawingTextRange which is specified. If there is no textrange
                |         which is corresponded above, then NULL is given back.
                |         This example gets the TextRange on the specified line and modifier of
                |         the MyGDT drawing GDT
                |
                |          MyGDT.GetTextRange(iRowNumber, iNumber, oTextRange)

        :param int i_row_number:
        :param int i_number:
        :rtype: DrawingTextRange
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return DrawingTextRange(self.drawing_gdt.GetTextRange(i_row_number, i_number))

    def get_tolerance_type(self, i_row_number: int) -> int:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetToleranceType(long iRowNumber) As long
                |     Returns the symbol used in the row of the GDT.
                |
                |     Parameters:
                |
                |         iRowNumber
                |             The number of the row to analyze.
                |
                |     Returns:
                |         The symbol in this row.
                |         0 : No GDT symbol. The specified row will be remove
                |         1 : Straightness GDT symbol
                |         2 : Flatness GDT symbol
                |         3 : Circularity GDT symbol
                |         4 : Cilindricity GDT symbol
                |         5 : Line profile GDT symbol
                |         6 : Surface profile GDT symbol
                |         7 : Angularity GDT symbol
                |         8 : Perpendicularity GDT symbol
                |         9 : Parallelism GDT symbol
                |         10 : Position GDT symbol
                |         11 : Concentricity GDT symbol
                |         12 : Symmetry
                |         13 : Circular runout GDT symbol
                |         14 : Total runout GDT symbol
                |
                |         Example:
                |             This example gets the symbol on the specified line of the MyGDT
                |             drawing GDT
                |
                |              MyGDT.GetToleranceType(iRowNumber, oGDTSymbol)

        :param int i_row_number:
        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_gdt.GetToleranceType(i_row_number)

    def set_tolerance_type(self, i_row_number: int, i_gdt_symbol: int) -> None:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetToleranceType(long iRowNumber,long iGDTSymbol)
                |     Sets the symbol used in the row of the GDT.
                |
                |     Parameters:
                |
                |         iRowNumber
                |             The number of the row analyse. If the row doesn't exist, it will be
                |             created
                |         iGDTSymbol
                |             The symbol to use in this row.
                |
                |     See also:
                |         CATIADrawingGDT::GetToleranceType
                |         This example sets a symbol on a specified line of the MyGDT drawing
                |         GDT
                |
                |          MyGDT.SetToleranceType(iRowNumber, iGDTSymbol)

        :param int i_row_number:
        :param int i_gdt_symbol:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_gdt.SetToleranceType(i_row_number, i_gdt_symbol)

    def __repr__(self):
        return f'DrawingGDT(name="{self.name}")'
