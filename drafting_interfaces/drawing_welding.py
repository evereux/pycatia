#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.drafting_interfaces.drawing_leaders import DrawingLeaders
from pycatia.drafting_interfaces.drawing_text_properties import DrawingTextProperties
from pycatia.drafting_interfaces.drawing_text_range import DrawingTextRange
from pycatia.system_interfaces.any_object import AnyObject


class DrawingWelding(AnyObject):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingWelding
                | 
                | Represents a drawing welding in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_welding = com_object

    @property
    def angle(self) -> float:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Angle() As double
                | 
                |     Returns or sets the angle of the drawing text. The angle is measured
                |     between the axis system of the drawing view and the local axis system of the
                |     drawing text. The angle is measured in radians and is counted
                |     counterclockwise.
                | 
                |     Example:
                |         This example sets the angle of the MyText drawing Text to 90 degrees
                |         clockwise. You first need to compute the angle in degrees and set the minus
                |         sign to indicate the rotation is clockwise.
                | 
                |          Angle90Clockwise = -90
                |          MyText.Angle = Angle90Clockwise

        :return: float
        :rtype: float
        """

        return self.drawing_welding.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.drawing_welding.Angle = value

    @property
    def identification_line_side(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property IdentificationLineSide() As CatWeldingSide
                | 
                |     Returns or sets the welding identification line Side of the drawing welding
                |     symbol.
                |     Precondition: This property is only available for ISO
                |     standard.
                | 
                |     Example:
                |         This example sets welding identification line Side to Up
                |         .
                | 
                |          MyWeld.IdentificationLineSide = catWeldingUp

        :return: int
        :rtype: int
        """

        return self.drawing_welding.IdentificationLineSide

    @identification_line_side.setter
    def identification_line_side(self, value: int):
        """
        :param int value:
        """

        self.drawing_welding.IdentificationLineSide = value

    @property
    def leaders(self) -> DrawingLeaders:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Leaders() As DrawingLeaders (Read Only)
                | 
                |     Returns the drawing leader collection of the drawing
                |     welding.
                | 
                |     Example:
                |         This example retrieves in LeaderCollection the collection of leaders of
                |         the MyWelding drawing welding.
                | 
                |          Dim LeaderCollection As DrawingLeaders
                |          Set LeaderCollection = MyWelding.Leaders

        :return: DrawingLeaders
        :rtype: DrawingLeaders
        """

        return DrawingLeaders(self.drawing_welding.Leaders)

    @property
    def text_properties(self) -> DrawingTextProperties:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property TextProperties() As DrawingTextProperties (Read
                | Only)
                | 
                |     Returns the text properties of the drawing welding.
                | 
                |     Example:
                |         This example retrieves in TextProperties the text properties of the
                |         MyWelding drawing welding..
                | 
                |          Dim TextProperties As DrawingTextProperties
                |          Set TextProperties = MyWelding.TextProperties

        :return: DrawingTextProperties
        :rtype: DrawingTextProperties
        """

        return DrawingTextProperties(self.drawing_welding.TextProperties)

    @property
    def welding_side(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property WeldingSide() As CatWeldingSide
                | 
                |     Returns or sets the welding side of the drawing welding
                |     symbol.
                | 
                |     Example:
                |         This example sets welding side to Up .
                | 
                |          MyWeld.WeldingSide = catWeldingUp

        :return: int
        :rtype: int
        """

        return self.drawing_welding.WeldingSide

    @welding_side.setter
    def welding_side(self, value: int):
        """
        :param int value:
        """

        self.drawing_welding.WeldingSide = value

    @property
    def welding_tail(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property WeldingTail() As CatDftWeldingTail
                | 
                |     Returns or sets the welding tail of the drawing welding
                |     symbol.
                | 
                |     Example:
                |         This example displays the welding symbol tail.
                | 
                |          MyWeld.WeldingTail = catDftWeldingTailYES

        :return: int
        :rtype: int
        """

        return self.drawing_welding.WeldingTail

    @welding_tail.setter
    def welding_tail(self, value: int):
        """
        :param int value:
        """

        self.drawing_welding.WeldingTail = value

    @property
    def x(self) -> float:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property x() As double
                | 
                |     Returns or sets the x coordinate of the drawing welding. It is expressed
                |     with respect to the current view coordinate system. This coordinate, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example retrieves in X the x coordinate of the MyWelding drawing
                |         welding.
                | 
                |          X = MyWelding.x

        :return: float
        :rtype: float
        """

        return self.drawing_welding.x

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.drawing_welding.x = value

    @property
    def y(self) -> float:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property y() As double
                | 
                |     Returns or sets the y coordinate of the drawing welding. It is expressed
                |     with respect to the current view coordinate system. This coordinate, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example sets the y coordinate of the MyWelding drawing welding to
                |         5 inches. You need first to convert the 5 inches into
                |         millmeters.
                | 
                |          NewYCoordinate = 5*25.4/1000
                |          MyWelding.y = NewYCoordinate

        :return: float
        :rtype: float
        """

        return self.drawing_welding.y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.drawing_welding.y = value

    def get_additional_symbol(self, i_weld: int) -> enum cat_weld_additional_symbol:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetAdditionalSymbol(CatWelding iWeld) As
                | CatWeldAdditionalSymbol
                | 
                |     Returns the additional symbol of the drawing welding.
                | 
                |     Parameters:
                | 
                |         iWeld
                |             The xxx
                | 
                |             Example:
                |                 This example sets an concave additinal symbol on the MyWelding
                |                 drawing welding
                | 
                |                  MyWelding.Symbol = DftConcaveSymbol

        :param int i_weld:
        :return: enum cat_weld_additional_symbol
        :rtype: enum cat_weld_additional_symbol
        """
        return self.drawing_welding.GetAdditionalSymbol(i_weld.com_object)

    def get_finish_symbol(self, i_weld: int) -> enum cat_dft_weld_finish_symbol:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFinishSymbol(CatWelding iWeld) As
                | CatDftWeldFinishSymbol
                | 
                |     Returns the finish symbol of the drawing welding.
                | 
                |     Parameters:
                | 
                |         iWeld
                |             The field on which finish symbol is applied.
                | 
                |             Example:
                |                 This example returns the finish symbol on the first symbol of
                |                 the MyWelding drawing welding
                | 
                |                  MyWelding.GetFinishSymbol(catWeldingFieldOne,oFinishSymbol)

        :param int i_weld:
        :return: enum cat_dft_weld_finish_symbol
        :rtype: enum cat_dft_weld_finish_symbol
        """
        return self.drawing_welding.GetFinishSymbol(i_weld.com_object)

    def get_symbol(self, i_weld: int) -> enum cat_welding_symbol:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetSymbol(CatWelding iWeld) As CatWeldingSymbol
                | 
                |     Returns the symbol of the drawing welding.
                | 
                |     Parameters:
                | 
                |         iWeld
                |             The field on which the symbol is applied 
                |         oSymbol
                |             The welding symbol
                | 
                |             Example:
                |                 This example gets the symbol on the first field of the
                |                 MyWelding drawing welding
                | 
                |                  MyWelding.GetSymbol(catWeldingFieldOne,oSymbol)

        :param int i_weld:
        :return: enum cat_welding_symbol
        :rtype: enum cat_welding_symbol
        """
        return self.drawing_welding.GetSymbol(i_weld.com_object)

    def get_text_range(self, i_field: int) -> DrawingTextRange:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetTextRange(CatWeldingField iField) As
                | DrawingTextRange
                | 
                |     Returns the field of the drawing welding in a drawing text
                |     range.
                | 
                |     Parameters:
                | 
                |         iField
                |             The drawing welding field 
                | 
                |     Returns:
                |         The drawing text range that corresponds to the drawing welding field
                |         
                | 
                | Example:
                |     This example retrieves the xxx.
                | 
                |      Dim textRange As DrawingTextRange
                |      Set textRange = MyWelding.GetTextRange (catWeldingUp)

        :param int i_field:
        :return: DrawingTextRange
        :rtype: DrawingTextRange
        """
        return DrawingTextRange(self.drawing_welding.GetTextRange(i_field.com_object))

    def set_additional_symbol(self, i_symbol: int, iweld: int) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetAdditionalSymbol(CatWeldAdditionalSymbol iSymbol,
                | CatWelding iweld)
                | 
                |     Sets the additional symbol of the drawing welding.
                | 
                |     Parameters:
                | 
                |         iSymbol
                |             The welding additional symbol 
                |         iWeld
                |             The xxx
                | 
                |             Example:
                |                 This example sets an concave additinal symbol on the MyWelding
                |                 drawing welding
                | 
                |                  MyWelding.Symbol = DftConcaveSymbol

        :param int i_symbol:
        :param int iweld:
        :return: None
        :rtype: None
        """
        return self.drawing_welding.SetAdditionalSymbol(i_symbol.com_object, iweld.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_additional_symbol'
        # # vba_code = """
        # # Public Function set_additional_symbol(drawing_welding)
        # #     Dim iSymbol (2)
        # #     drawing_welding.SetAdditionalSymbol iSymbol
        # #     set_additional_symbol = iSymbol
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_finish_symbol(self, i_finish_symbol: int, i_weld: int) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetFinishSymbol(CatDftWeldFinishSymbol iFinishSymbol,
                | CatWelding iWeld)
                | 
                |     Sets the finish symbol of the drawing welding.
                | 
                |     Parameters:
                | 
                |         iFinishSymbol
                |             The finish welding symbol 
                |         iWeld
                |             The field on which finish symbol will be applied.
                | 
                |             Example:
                |                 This example sets the finish symbol on the first symbol of the
                |                 MyWelding drawing welding
                | 
                |                 
                |                 MyWelding.GetFinishSymbol(catWeldingFieldOne,catDftLetterCWelding)

        :param int i_finish_symbol:
        :param int i_weld:
        :return: None
        :rtype: None
        """
        return self.drawing_welding.SetFinishSymbol(i_finish_symbol.com_object, i_weld.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_finish_symbol'
        # # vba_code = """
        # # Public Function set_finish_symbol(drawing_welding)
        # #     Dim iFinishSymbol (2)
        # #     drawing_welding.SetFinishSymbol iFinishSymbol
        # #     set_finish_symbol = iFinishSymbol
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_symbol(self, i_symbol: int, iweld: int) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetSymbol(CatWeldingSymbol iSymbol,
                | CatWelding iweld)
                | 
                |     Sets the symbol of the drawing welding.
                | 
                |     Parameters:
                | 
                |         iSymbol
                |             The welding symbol 
                |         iWeld
                |             The field on which the symbol is applied
                | 
                |             Example:
                |                 This example sets a symbol on the first field of the MyWelding
                |                 drawing welding
                | 
                |                  MyWelding.SetSymbol(catSquareWelding,catWeldingFieldOne)

        :param int i_symbol:
        :param int iweld:
        :return: None
        :rtype: None
        """
        return self.drawing_welding.SetSymbol(i_symbol.com_object, iweld.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_symbol'
        # # vba_code = """
        # # Public Function set_symbol(drawing_welding)
        # #     Dim iSymbol (2)
        # #     drawing_welding.SetSymbol iSymbol
        # #     set_symbol = iSymbol
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DrawingWelding(name="{ self.name }")'
