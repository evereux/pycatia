#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.system_interfaces.cat_base_dispatch import CATBaseDispatch


class DrawingTextProperties(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 DrawingTextProperties
                | 
                | Represents the properties of a drawing text in a drawing view.
                | 
                | This interface is obtained from CATIADrawingText or CATIADrawingWelding
                | interface. Update method must be called after text properties modification to
                | refresh the visualization.
    
    """

    def __init__(self, com_object):
        super().__init__()
        self.drawing_text_properties = com_object

    @property
    def anchor_point(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AnchorPoint() As CatTextAnchorPosition
                | 
                |     Returns or sets the anchor point of the drawing text.
                | 
                |     Example:
                |         This example sets the AnchorPoint of the MyText drawing text to the
                |         right
                | 
                |          MyText.AnchorPoint = catRight

        :return: enum cat_text_anchor_position
        :rtype: int
        """

        return self.drawing_text_properties.AnchorPoint

    @anchor_point.setter
    def anchor_point(self, value: int):
        """
        :param int value: enum cat_text_anchor_position
        """

        self.drawing_text_properties.AnchorPoint = value

    @property
    def blanking(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Blanking() As CatBlankingMode
                | 
                |     Returns or sets the blanking mode of the drawing text.
                | 
                |     Example:
                |         This example sets the blanking mode type of MyText drawing text to
                |         active on geom
                | 
                |          MyText.Blanking = catBlankingOnGeom

        :return: enum cat_blanking_mode
        :rtype: int
        """

        return self.drawing_text_properties.Blanking

    @blanking.setter
    def blanking(self, value: int):
        """
        :param int value: enum cat_blanking_mode
        """

        self.drawing_text_properties.Blanking = value

    @property
    def bold(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Bold() As long
                | 
                |     Returns or sets the drawing text font bold property.
                |     True if the drawing text is bold formatted.
                | 
                |     Example:
                |         This example get the parameter bold on MyText drawing
                |         text.
                | 
                |          oVal = MyText.Bold

        :rtype: int
        """

        return self.drawing_text_properties.Bold

    @bold.setter
    def bold(self, value: int):
        """
        :param int value:
        """

        self.drawing_text_properties.Bold = value

    @property
    def color(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Color() As long
                | 
                |     Returns or sets the color of the drawing text.
                | 
                |     Example:
                |         This example sets the Color type of the MyText drawing text to
                |         red
                | 
                |          redCol  =-16776961 'Encoded RGBA color within long integer (R=255 G=0 
                |          B=0   A=255)
                |          MyText.Color = redCol

        :rtype: int
        """

        return self.drawing_text_properties.Color

    @color.setter
    def color(self, value: int):
        """
        :param int value:
        """

        self.drawing_text_properties.Color = value

    @property
    def font_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FontName() As CATBSTR
                | 
                |     Returns or sets the font name of the drawing text.
                | 
                |     Example:
                |         This example sets the MyText drawing text font as Courrier 10
                |         BT.
                | 
                |          MyText.SetFontName("Courrier 10 BT")

        :rtype: str
        """

        return self.drawing_text_properties.FontName

    @font_name.setter
    def font_name(self, value: str):
        """
        :param str value:
        """

        self.drawing_text_properties.FontName = value

    @property
    def font_size(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FontSize() As double
                | 
                |     Returns or sets the font size of the drawing text.
                | 
                |     Example:
                |         This example sets the MyText drawing text font size to
                |         3.5.
                | 
                |          iFontSize = 3.5
                |          MyText.SetFontSize 0, 0, iFontSize

        :rtype: float
        """

        return self.drawing_text_properties.FontSize

    @font_size.setter
    def font_size(self, value: float):
        """
        :param float value:
        """

        self.drawing_text_properties.FontSize = value

    @property
    def frame_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FrameType() As CatTextFrameType
                | 
                |     Returns or sets the frame type of the drawing text.
                | 
                |     Example:
                |         This example sets the frame type of the MyText drawing text to an
                |         ellipse
                | 
                |          MyText.FrameType = catEllipse

        :return: enum cat_text_frame_type
        :rtype: int
        """

        return self.drawing_text_properties.FrameType

    @frame_type.setter
    def frame_type(self, value: int):
        """
        :param int value: enum cat_text_frame_type
        """

        self.drawing_text_properties.FrameType = value

    @property
    def italic(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Italic() As long
                | 
                |     Returns or sets the drawing text font italic property.
                |     True if the drawing text is formatted as italic.
                | 
                |     Example:
                |         This example set the parameter Italic on MyText drawing
                |         text.
                | 
                |          MyText.Italic = 1

        :rtype: int
        """

        return self.drawing_text_properties.Italic

    @italic.setter
    def italic(self, value: int):
        """
        :param int value:
        """

        self.drawing_text_properties.Italic = value

    @property
    def justification(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Justification() As CatJustification
                | 
                |     Returns or sets the drawing text font justification
                |     property.
                |     True if the drawing text font is justified.
                | 
                |     Example:
                |         This example sets the Justification type of the MyText drawing text to
                |         the right
                | 
                |          MyText.Justification = catRight

        :return: enum cat_justification
        :rtype: int
        """

        return self.drawing_text_properties.Justification

    @justification.setter
    def justification(self, value: int):
        """
        :param int value: enum cat_justification
        """

        self.drawing_text_properties.Justification = value

    @property
    def kerning(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Kerning() As long
                | 
                |     Font kerning property.
                |     True if the drawing text font is formatted as kerning
                | 
                |     Example:
                |         This example set the parameter kerning on MyText drawing
                |         text.
                | 
                |          MyText.Kerning = 1

        :rtype: int
        """

        return self.drawing_text_properties.Kerning

    @kerning.setter
    def kerning(self, value: int):
        """
        :param int value:
        """

        self.drawing_text_properties.Kerning = value

    @property
    def mirror(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Mirror() As CatTextFlipMode
                | 
                |     Returns or sets the mirroring of the drawing text.
                | 
                |     Example:
                |         This example sets the Mirror type of the MyText drawing text to no
                |         flip
                | 
                |          MyText.Mirror = catTextNoFlip

        :return: enum cat_text_flip_mode
        :rtype: int
        """

        return self.drawing_text_properties.Mirror

    @mirror.setter
    def mirror(self, value: int):
        """
        :param int value:
        """

        self.drawing_text_properties.Mirror = value

    @property
    def overline(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Overline() As long
                | 
                |     Returns or sets the drawing text font overline property.
                |     True if the drawing text is overlined.
                | 
                |     Example:
                |         This example get the parameter Overline on MyText drawing
                |         text.
                | 
                |          oval = MyText.Overline()

        :rtype: int
        """

        return self.drawing_text_properties.Overline

    @overline.setter
    def overline(self, value: int):
        """
        :param int value:
        """

        self.drawing_text_properties.Overline = value

    @property
    def strike_thru(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property StrikeThru() As long
                | 
                |     Returns or sets the drawing text font strikethrough
                |     property.
                |     True if the drawing text font is striked through.
                | 
                |     Example:
                |         This example set the parameter StrikeThru on MyText drawing
                |         text.
                | 
                |          MyText.StrikeThru = 1

        :rtype: int
        """

        return self.drawing_text_properties.StrikeThru

    @strike_thru.setter
    def strike_thru(self, value: int):
        """
        :param int value:
        """

        self.drawing_text_properties.StrikeThru = value

    @property
    def subscript(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Subscript() As long
                | 
                |     Returns or sets the drawing text font subscript property.
                |     True if the drawing text font is formatted as subscript.
                | 
                |     Example:
                |         This example set the parameter Subscript on MyText drawing
                |         text.
                | 
                |          MyText.Subscript = 1

        :rtype: int
        """

        return self.drawing_text_properties.Subscript

    @subscript.setter
    def subscript(self, value: int):
        """
        :param int value:
        """

        self.drawing_text_properties.Subscript = value

    @property
    def superscript(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Superscript() As long
                | 
                |     Returns or sets the drawing text font superscript
                |     property.
                |     True if the drawing text font is formatted as superscript.
                | 
                |     Example:
                |         This example set the parameter Superscript on MyText drawing
                |         text.
                | 
                |          MyText.Superscript = 1

        :rtype: int
        """

        return self.drawing_text_properties.Superscript

    @superscript.setter
    def superscript(self, value: int):
        """
        :param int value:
        """

        self.drawing_text_properties.Superscript = value

    @property
    def underline(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Underline() As long
                | 
                |     Returns or sets the drawing text font underline property.
                |     True if the drawing text is underlined.
                | 
                |     Example:
                |         This example get the parameter bold on MyText drawing
                |         text.
                | 
                |          oval = MyText.Underline

        :rtype: int
        """

        return self.drawing_text_properties.Underline

    @underline.setter
    def underline(self, value: int):
        """
        :param int value:
        """

        self.drawing_text_properties.Underline = value

    def activate_frame(self, i_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ActivateFrame(CatTextFrameType iType)
                | 
                |     Activates the text frame of the drawing text.
                | 
                |     Parameters:
                | 
                |         iType
                |             The text frame type 
                | 
                |     Example:
                |         This example add a rectangle frame to MyText drawing
                |         text.
                | 
                |          CatTextFrameType itype = catRectangle
                |          MyText.ActivateFrame itype
                |          
                | Example:
                | 
                |       This example remove the frame to MyText drawing text.
                |
                |      CatTextFrameType itype = catNone
                |      MyText.ActivateFrame itype

        :param int i_type: enum cat_text_frame_type
        :rtype: None
        """
        return self.drawing_text_properties.ActivateFrame(i_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'activate_frame'
        # # vba_code = """
        # # Public Function activate_frame(drawing_text_properties)
        # #     Dim iType (2)
        # #     drawing_text_properties.ActivateFrame iType
        # #     activate_frame = iType
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Update()
                | 
                |     Update the properties of the drawing text. 
                | 
                | Example:
                |     This example update the properties to MyText drawing text.
                | 
                |      MyText.Update 
                |      
                | 
                |     Copyright © 1999-2011, Dassault Systèmes. All rights
                |     reserved.

        :rtype: None
        """
        return self.drawing_text_properties.Update()

    def __repr__(self):
        return f'DrawingTextProperties()'
