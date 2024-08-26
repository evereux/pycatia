#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.drafting_interfaces.drawing_text_properties import DrawingTextProperties
from pycatia.system_interfaces.any_object import AnyObject


class DrawingCoordDim(AnyObject):
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
                |                     DrawingCoordDim
                |
                | Represents a drawing Coordinate Dimension in a drawing view.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_coord_dim = com_object

    @property
    def angle(self) -> float:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property Angle() As double
                |     Returns or sets the angle of the drawing coordinate dimension. The angle is
                |     measured between the axis system of the drawing view and the local axis system
                |     of the drawing coordinate dimension. The angle is measured in radians and is
                |     counted counterclockwise.
                |
                |     Example:
                |         This example sets the angle of the MyCoordDim drawing Text to 90
                |         degrees clockwise. You first need to compute the angle in degrees and set the
                |         minus sign to indicate the rotation is clockwise.
                |
                |          Angle90Clockwise = -90
                |          MyCoordDim.Angle = Angle90Clockwise

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_coord_dim.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.drawing_coord_dim.Angle = value

    @property
    def text_properties(self) -> DrawingTextProperties:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property TextProperties() As DrawingTextProperties (Read Only)
                |     Returns the text properties of the drawing coordinate
                |     dimension.
                |
                |     Example:
                |         This example retrieves in TextProperties the text properties of the
                |         MyCoordDim drawing coordinate dimension..
                |
                |          Dim TextProperties As DrawingTextProperties
                |          Set TextProperties = MyCoordDim.TextProperties

        :rtype: DrawingTextProperties
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return DrawingTextProperties(self.drawing_coord_dim.TextProperties)

    @property
    def x(self) -> float:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property x() As double
                |     Returns or sets the x coordinate of the drawing coordinate dimension. It is
                |     expressed with respect to the current view coordinate system. This coordinate,
                |     like any length, is measured in millimeters.
                |
                |     Example:
                |         This example retrieves in X the x coordinate of the MyCoordDim drawing
                |         coordinate dimension.
                |
                |          X = MyCoordDim.x

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_coord_dim.x

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.drawing_coord_dim.x = value

    @property
    def y(self) -> float:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property y() As double
                |     Returns or sets the y coordinate of the drawing coordinate dimension. It is
                |     expressed with respect to the current view coordinate system. This coordinate,
                |     like any length, is measured in millimeters.
                |
                |     Example:
                |         This example sets the y coordinate of the MyCoordDim drawing coordinate
                |         dimension to 5 inches. You need first to convert the 5 inches into
                |         millmeters.
                |
                |          NewYCoordinate = 5*25.4/1000
                |          MyCoordDim.y = NewYCoordinate

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_coord_dim.y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.drawing_coord_dim.y = value

    def get_coord_values(self, o_type: int, o_x: float, o_y: float, o_z: float) -> None:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub GetCoordValues(long oType,double oX,double oY,double oZ)
                |     Returns the value of the drawing coordinate dimension.
                |
                |     Parameters:
                |
                |         oType
                |             oType (0: 2D coordinate dimension, 1: 3D coordinate dimension).
                |
                |         oX
                |             X value.
                |         oY
                |             Y value.
                |         oZ
                |             Z value (=0. if 2D coordinate dimension).
                |
                |             Example:
                |                 This example gets the type, x, y and z of the MyCoordDim
                |                 drawing CoordDim
                |
                |                  MyCoordDim.GetCoordValues(oType, oX, oY, oZ)

        :param int o_type:
        :param float o_x:
        :param float o_y:
        :param float o_z:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_coord_dim.GetCoordValues(o_type, o_x, o_y, o_z)

    def __repr__(self):
        return f'DrawingCoordDim(name="{self.name}")'
