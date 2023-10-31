#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.drafting_interfaces.drawing_text_properties import DrawingTextProperties
from pycatia.system_interfaces.cat_base_dispatch import CATBaseDispatch


class DrawingTextRange(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 DrawingTextRange
                | 
                | Represents a drawing text range, or contiguous area, in a drawing
                | text.
                | 
                | A range is a contiguous area in a drawing text defined by the position of a
                | starting and ending character, or by the position of a starting character and a
                | length expressed in number of characters.
    
    """

    def __init__(self, com_object):
        super().__init__()
        self.drawing_text_range = com_object

    @property
    def length(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Length() As long (Read Only)
                | 
                |     Returns the number of characters of the drawing text
                |     range.
                | 
                |     Example:
                |         This example retrieves in NbChar the number of characters of the
                |         MyTextRange drawing text range.
                | 
                |          NbChar = MyTextRange.Length

        :rtype: int
        """

        return self.drawing_text_range.Length

    @property
    def start(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Start() As long (Read Only)
                | 
                |     Returns the starting character position of the drawing text
                |     range.
                | 
                |     Example:
                |         This example retrieves in StartCharPosthe starting character position
                |         of the MyTextRange drawing text range.
                | 
                |          StartCharPos = MyTextRange.Start

        :rtype: int
        """

        return self.drawing_text_range.Start

    @property
    def text(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Text() As CATBSTR
                | 
                |     Returns or sets the character string making up the drawing text
                |     range.
                | 
                |     Example:
                |         This example sets in text the character string that makes up the
                |         MyTextRange drawing text range.
                | 
                |          MyTextRange.Text = text
                |          Set MyTextProperties = MyTextRange.TextProperties
                |          MyTextProperties.Update
                |          
                | 
                |     See also:
                |         DrawingTextProperties.Update

        :rtype: str
        """

        return self.drawing_text_range.Text

    @text.setter
    def text(self, value: str):
        """
        :param str value:
        """

        self.drawing_text_range.Text = value

    @property
    def text_properties(self) -> DrawingTextProperties:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property TextProperties() As DrawingTextProperties (Read
                | Only)
                | 
                |     Deprecated:
                |         V5R18 use DrawingWelding.TextProperties This method has not to be used
                |         to manage the text range properties. Text properties is only applied on the
                |         whole text, not on a sub text identified by a text range. Returns the drawing
                |         text range properties.
                | 
                |         Example:
                |             This example returns in Prop the text properties of the MyTextRange
                |             drawing text range.
                | 
                |              Dim Prop As CATIADrawingTextProperties
                |              Set Prop = MyTextRange.TextProperties(String)

        :rtype: DrawingTextProperties
        """

        return DrawingTextProperties(self.drawing_text_range.TextProperties)

    def get_text_range(self, i_start: int, i_end: int) -> 'DrawingTextRange':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetTextRange(long iStart,
                | long iEnd) As DrawingTextRange
                | 
                |     Returns a drawing text range within another drawing text range. The text
                |     range is retrieved using its starting and ending character
                |     positions.
                | 
                |     Parameters:
                | 
                |         iStart
                |             The position of the drawing text range starting character
                |             
                |         iEnd
                |             The position of the drawing text range ending character
                |             
                | 
                |     Example:
                |         This example retrieves in extractedTextRange the drawing text range
                |         that begins at the eighth character and end at the fifteenth character of the
                |         MyTextRange drawing text range.
                | 
                |          Dim extractedTextRange As DrawingTextRange
                |          start = 8
                |          end = 15
                |          extractedTextRange = MyTextRange.GetTextRange(start, end)

        :param int i_start:
        :param int i_end:
        :rtype: DrawingTextRange
        """
        return DrawingTextRange(self.drawing_text_range.GetTextRange(i_start, i_end))

    def insert_after(self, i_string: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub InsertAfter(CATBSTR iString)
                | 
                |     Inserts a character string at the end of the drawing text
                |     range.
                | 
                |     Parameters:
                | 
                |         iString
                |             The character string to be added 
                | 
                |     Example:
                |         This example inserts the String character string at the end of the
                |         MyTextRange drawing text range.
                | 
                |          String = "String to insert after"
                |          MyTextRange.InsertAfter(String)
                |          Set MyTextProperties = MyTextRange.TextProperties
                |          MyTextProperties.Update
                |          
                | 
                | See also:
                |     DrawingTextProperties.Update

        :param str i_string:
        :rtype: None
        """
        return self.drawing_text_range.InsertAfter(i_string)

    def insert_before(self, i_string: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub InsertBefore(CATBSTR iString)
                | 
                |     Inserts a character string at the beginning of the drawing text
                |     range.
                | 
                |     Parameters:
                | 
                |         iString
                |             The character string to be added 
                | 
                |     Example:
                |         This example inserts the String character string at the beginning of
                |         the MyTextRange drawing text range.
                | 
                |          String = "String to insert before"
                |          MyTextRange.InsertBefore(String)
                |          Set MyTextProperties = MyTextRange.TextProperties
                |          MyTextProperties.Update
                |          
                | 
                | See also:
                |     DrawingTextProperties.Update
                | 
                |     Copyright © 1999-2011, Dassault Systèmes. All rights
                |     reserved.

        :param str i_string:
        :return: None
        """
        return self.drawing_text_range.InsertBefore(i_string)

    def __repr__(self):
        return f'DrawingTextRange()'
