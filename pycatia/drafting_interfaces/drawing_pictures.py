#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pathlib import Path
from typing import Iterator

from pycatia.exception_handling.exceptions import CATIAApplicationException
from pycatia.drafting_interfaces.drawing_picture import DrawingPicture
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class DrawingPictures(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingPictures
                | 
                | A collection of all the drawing pictures currently managed by a drawing view of
                | drawing sheet in a drawing document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingPicture)
        self.drawing_pictures = com_object

    def add(self, i_drawing_picture_path: Path, i_position_x: float, i_position_y: float) -> DrawingPicture:
        """

        When passing a path of the image file to this function it's recommended to use the absolute path or the method
        may not work. Otherwise, Path library will try and determine the absolute path if it can.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add(CATBSTR iDrawingPicturePath,
                | double iPositionX,
                | double iPositionY) As DrawingPicture
                | 
                |     Inserts a drawing picture in the drawing view and adds it to the
                |     DrawingPictures collection.
                | 
                |     Parameters:
                | 
                |         iDrawingPicturePath
                |             The path of the picture file (ex : "C:/tmp/ball.bmp") .
                |         iPositionX,iPositionY
                |             The drawing picture x and y coordinates, expressed in millimeters,
                |             with respect to the drawing view coordinate system
                |             
                | 
                |     Returns:
                |         The inserted drawing picture 
                | 
                | Example:
                |     The following example inserts a drawing picture from a given picture file
                |     path The MyView is the active view in the active drawing
                |     sheet
                | 
                |      Dim MySheet As DrawingSheet
                |      Set MySheet = CATIA.ActiveDocument.Sheets.ActiveSheet
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.ActiveView
                |      Dim MyDrawingPicture1 As DrawingPicture
                |      Set MyDrawingPicture1 = MyView.Pictures.Add("C:/tmp/ball.bmp", 100., 50.)

        :param Path i_drawing_picture_path:
        :param float i_position_x:
        :param float i_position_y:
        :rtype: DrawingPicture
        """

        absolute_path = i_drawing_picture_path.absolute()
        if not absolute_path.is_file():
            raise CATIAApplicationException(f'Could not find image file: "{absolute_path}".')
        return DrawingPicture(self.drawing_pictures.Add(absolute_path, i_position_x, i_position_y))

    def item(self, i_index: cat_variant) -> DrawingPicture:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As DrawingPicture
                | 
                |     Returns a drawing picture using its index or its name from the
                |     DrawingPictures collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the drawing picture to retrieve from the
                |             collection of drawing pictures. As a numerics, this index is the rank of the
                |             drawing picture in the collection. The index of the first drawing picture in
                |             the collection is 1, and the index of the last drawing picture is Count. As a
                |             string, it is the name you assigned to the drawing picture using the
                |             
                | 
                |         AnyObject.Name property 
                |     Returns:
                |         The retrieved drawing picture 
                | 
                | Example:
                |     This example retrieves in ThisDrawingPicture the second drawing picture,
                |     MyView in the drawing view collection of the active sheet in the active
                |     document, supposed to be a drawing document.
                | 
                |      Dim MySheet As DrawingSheet
                |      Set MySheet = CATIA.ActiveDocument.Sheets.ActiveSheet
                |      Dim MyView  As DrawingView
                |      Set MyView  = MySheet.Views.ActiveView
                |      Dim ThisDrawingPicture As DrawingPicture
                |      Set ThisDrawingPicture = MyView.Pictures.Item(2)

        :param cat_variant i_index:
        :rtype: DrawingPicture
        """
        return DrawingPicture(self.drawing_pictures.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a drawing picture from the DrawingPictures
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing picture to remove from the collection of
                |             drawing pictures. As a numerics, this index is the rank of the drawing picture
                |             in the collection. The index of the first drawing picture in the collection is
                |             1, and the index of the last drawing picture is Count. As a string, it is the
                |             name you assigned to the drawing picture using the
                |             
                | 
                |         AnyObject.Name property 
                | 
                | Example:
                |     The following example removes the third drawing picture in the drawing
                |     pictures collection of the active view of the active document, supposed to be a
                |     drawing document.
                | 
                |      Dim MyView As DrawingView
                |      Set MyView  = MySheet.Views.ActiveView
                |      MyView.Pictures.Remove(3)

        :param cat_variant i_index:
        :rtype: None
        """
        return self.drawing_pictures.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingPicture:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingPicture(self.drawing_pictures.Item(n + 1))

    def __iter__(self) -> Iterator[DrawingPicture]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DrawingPictures(name="{self.name}")'
