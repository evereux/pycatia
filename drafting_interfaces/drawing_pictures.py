#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.drafting_interfaces.drawing_picture import DrawingPicture
from pycatia.system_interfaces.collection import Collection


class DrawingPictures(Collection):
    """
        .. note::
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
        super().__init__(com_object)
        self.drawing_pictures = com_object

    def add(self, i_drawing_picture_path, i_position_x, i_position_y):
        """
        .. note::
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

        :param str i_drawing_picture_path:
        :param float i_position_x:
        :param float i_position_y:
        :return: DrawingPicture
        """
        return DrawingPicture(self.drawing_pictures.Add(i_drawing_picture_path, i_position_x, i_position_y))

    def item(self, i_index):
        """
        .. note::
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

        :param CATVariant i_index:
        :return: DrawingPicture
        """
        return DrawingPicture(self.drawing_pictures.Item(i_index))

    def remove(self, i_index):
        """
        .. note::
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

        :param CATVariant i_index:
        :return: None
        """
        return self.drawing_pictures.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(drawing_pictures)
        # #     Dim iIndex (2)
        # #     drawing_pictures.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DrawingPictures(name="{self.name}")'
