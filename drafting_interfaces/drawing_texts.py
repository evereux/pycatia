#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.drafting_interfaces.drawing_text import DrawingText
from pycatia.system_interfaces.collection import Collection


class DrawingTexts(Collection):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingTexts
                | 
                | A collection of all the drawing texts currently managed by a drawing view of
                | drawing sheet in a drawing document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_texts = com_object

    def add(self, i_drawing_text=None, i_position_x=None, i_position_y=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func Add(CATBSTR iDrawingText,
                | double iPositionX,
                | double iPositionY) As DrawingText
                | 
                |     Creates a drawing text and adds it to the DrawingTexts
                |     collection.
                | 
                |     Parameters:
                | 
                |         iDrawingText
                |             The character string that makes up the drawing text to create
                |             
                |         iPositionX,iPositionY
                |             The drawing text x and y coordinates, expressed in millimeters,
                |             with respect to the drawing view coordinate system
                |             
                | 
                |     Returns:
                |         The created drawing text 
                | 
                | Example:
                |     The following example creates a drawing text with the string ComplexText
                |     and retrieved in MyText in the drawing view collection of the MyView drawing
                |     view. This view belongs to the drawing view collection of the drawing
                |     sheet
                | 
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.ActiveView
                |      Dim MyText As DrawingText
                |      Set MyText = MyView.Texts.Add("ComplexText", 0., 0.)

        :param str i_drawing_text:
        :param float i_position_x:
        :param float i_position_y:
        :return: None
        """
        return self.drawing_texts.Add(i_drawing_text, i_position_x, i_position_y)

    def item(self, i_index=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func Item(long iIndex) As DrawingText
                | 
                |     Returns a drawing text using its index from the DrawingTexts
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing text to retrieve from the collection of
                |             drawing texts. As a numerics, this index is the rank of the drawing text in the
                |             collection. The index of the first drawing text in the collection is 1, and the
                |             index of the last drawing text is Count. 
                | 
                |     Returns:
                |         The retrieved drawing view 
                |     Example:
                |         This example retrieves in ThisDrawingText the second drawing text, in
                |         the drawing view collection of the active view in the active sheet, in the
                |         active document supposed to be a drawing document.
                | 
                |          Dim MyView  As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          Dim ThisDrawingText As DrawingText
                |          Set ThisDrawingText = MyView.Texts.Item(2)

        :param int i_index:
        :return: DrawingText
        """
        return DrawingText(self.drawing_texts.Item(i_index))

    def remove(self, i_index=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub Remove(long iIndex)
                | 
                |     Removes a drawing text from the DrawingTexts collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing text to remove from the collection of
                |             drawing texts. As a numerics, this index is the rank of the drawing text in the
                |             collection. The index of the first drawing text in the collection is 1, and the
                |             index of the last drawing text is Count. 
                | 
                |     Example:
                |         The following example removes the third drawing text in the drawing
                |         text collection of the active view of the active document, supposed to be a
                |         drawing document.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.DrawingTexts.Remove(3)

        :param int i_index:
        :return: None
        """
        return self.drawing_texts.Remove(i_index)

    def __repr__(self):
        return f'DrawingTexts(name="{ self.name }")'
