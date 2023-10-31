#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class DrawingPicture(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingPicture
                | 
                | Represents a drawing picture in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_picture = com_object

    @property
    def crop_bottom(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property cropBottom() As double
                | 
                |     Returns or sets the cropBottom of the drawing picture. The cropBottom is
                |     the size of the margin on the bottom of the picture. The cropBottom, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example sets the cropBottom of the MyPicture drawing picture to 10
                |         mm
                | 
                |          MyPicture.cropBottom = 10.

        :rtype: float
        """

        return self.drawing_picture.cropBottom

    @crop_bottom.setter
    def crop_bottom(self, value: float):
        """
        :param float value:
        """

        self.drawing_picture.cropBottom = value

    @property
    def crop_left(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property cropLeft() As double
                | 
                |     Returns or sets the cropLeft of the drawing picture. The cropLeft is the
                |     size of the margin on the left of the picture. The cropLeft, like any length,
                |     is measured in millimeters.
                | 
                |     Example:
                |         This example sets the cropLeft of the MyPicture drawing picture to 10
                |         mm
                | 
                |          MyPicture.cropLeft = 10.

        :rtype: float
        """

        return self.drawing_picture.cropLeft

    @crop_left.setter
    def crop_left(self, value: float):
        """
        :param float value:
        """

        self.drawing_picture.cropLeft = value

    @property
    def crop_right(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property cropRight() As double
                | 
                |     Returns or sets the cropRight of the drawing picture. The cropRight is the
                |     size of the margin on the right of the picture. The cropRight, like any length,
                |     is measured in millimeters.
                | 
                |     Example:
                |         This example sets the cropRight of the MyPicture drawing picture to 10
                |         mm
                | 
                |          MyPicture.cropRight = 10.

        :rtype: float
        """

        return self.drawing_picture.cropRight

    @crop_right.setter
    def crop_right(self, value: float):
        """
        :param float value:
        """

        self.drawing_picture.cropRight = value

    @property
    def crop_top(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property cropTop() As double
                | 
                |     Returns or sets the cropTop of the drawing picture. The cropTop is the size
                |     of the margin on the top of the picture. The cropTop, like any length, is
                |     measured in millimeters.
                | 
                |     Example:
                |         This example sets the cropTop of the MyPicture drawing picture to 10
                |         mm
                | 
                |          MyPicture.cropTop = 10.

        :rtype: float
        """

        return self.drawing_picture.cropTop

    @crop_top.setter
    def crop_top(self, value: float):
        """
        :param float value:
        """

        self.drawing_picture.cropTop = value

    @property
    def format(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property format() As CatPictureFormat
                | 
                |     Sets the picture format.
                | 
                |     Parameters:
                | 
                |         iPictureFormat
                |             Compression format. 
                | 
                |     Returns:
                | 
                |         Legal values:
                | 
                |         S_OK
                |             Method correctly executed. 
                |         E_FAIL
                |             Method execution failed. 
                |             Reasons of the failure are not given. 
                |         E_IMPL
                |             No implementation available for this method. 
                | 
                |     See also:
                |         CatPictureFormat

        :return: enum cat_picture_format
        :rtype: int
        """

        return self.drawing_picture.format

    @format.setter
    def format(self, value: int):
        """
        :param int value: enum cat_picture_format
        """

        self.drawing_picture.format = value

    @property
    def height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property height() As double
                | 
                |     Returns or sets the height of the drawing picture. The height, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example gets the height of the MyPicture drawing
                |         picture
                | 
                |          Height = MyPicture.height

        :rtype: float
        """

        return self.drawing_picture.height

    @height.setter
    def height(self, value: float):
        """
        :param float value:
        """

        self.drawing_picture.height = value

    @property
    def ratio_lock(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ratioLock() As boolean
                | 
                |     Returns or sets the ratioLock of the drawing picture. The ratioLock is a
                |     boolean value If ratioLock is True it means that the size must not be changed
                |     by command in a interactive session.But it does not avoid size modifications
                |     thru VBScript exec (height and width still available for
                |     modification).
                | 
                |     Example:
                |         This example sets the ratioLock of the MyPicture drawing picture to
                |         True
                | 
                |          MyPicture.ratioLock = True

        :rtype: bool
        """

        return self.drawing_picture.ratioLock

    @ratio_lock.setter
    def ratio_lock(self, value: bool):
        """
        :param bool value:
        """

        self.drawing_picture.ratioLock = value

    @property
    def width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property width() As double
                | 
                |     Returns or sets the width of the drawing picture. The width, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example gets the width of the MyPicture drawing
                |         picture
                | 
                |          Width = MyPicture.width

        :rtype: float
        """

        return self.drawing_picture.width

    @width.setter
    def width(self, value: float):
        """
        :param float value:
        """

        self.drawing_picture.width = value

    @property
    def x(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property x() As double
                | 
                |     Returns or sets the x coordinate of the drawing picture position. It is
                |     expressed with respect to the view coordinate system. This coordinate, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example sets the x coordinate of the position of the MyPicture
                |         drawing picture to 5 inches. You need first to convert the 5 inches into
                |         millimeters.
                | 
                |          NewXCoordinate = 5*25.4
                |          MyPicture.x =  NewXCoordinate

        :rtype: float
        """

        return self.drawing_picture.x

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.drawing_picture.x = value

    @property
    def y(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property y() As double
                | 
                |     Returns or sets the y coordinate of the drawing picture position. It is
                |     expressed with respect to the view coordinate system. This coordinate, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example sets the y coordinate of the position of the MyPicture
                |         drawing picture to 5 inches. You need first to convert the 5 inches into
                |         millimeters.
                | 
                |          NewYCoordinate = 5*25.4
                |          MyPicture.y =  NewYCoordinate

        :rtype: float
        """

        return self.drawing_picture.y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.drawing_picture.y = value

    def get_original_height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetOriginalHeight() As double
                | 
                |     Gets the original height of the drawing picture. The height, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example gets the original height of the MyPicture drawing
                |         picture
                | 
                |          Height = MyPicture.GetOriginalHeight()

        :rtype: float
        """
        return self.drawing_picture.GetOriginalHeight()

    def get_original_width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetOriginalWidth() As double
                | 
                |     Gets the original width of the drawing picture. The width, like any length,
                |     is measured in millimeters.
                | 
                |     Example:
                |         This example gets the original width of the MyPicture drawing
                |         picture
                | 
                |          Width = MyPicture.GetOriginalWidth()

        :rtype: float
        """
        return self.drawing_picture.GetOriginalWidth()

    def __repr__(self):
        return f'DrawingPicture(name="{self.name}")'
