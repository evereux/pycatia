#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class Marker2D(AnyObject):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Marker2D
                | 
                | Represents a marker 2D in a specified annotated view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.marker2_d = com_object

    @property
    def fill(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Fill() As long
                | 
                |     Returns or sets the Marker2D's filling status (1 the figure is filled, 0
                |     the figure is not filled).
                | 
                |     Example:
                | 
                |              This example retrieves the filling status of the NewMarker2D
                |              Marker2D.
                |             
                | 
                |             Dim status As Integer
                |             status = NewMarker2D.Fill

        :return: int
        """

        return self.marker2_d.Fill

    @fill.setter
    def fill(self, value):
        """
        :param int value:
        """

        self.marker2_d.Fill = value

    @property
    def frame(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Frame() As long
                | 
                |     Returns or sets the Marker2D's framing status (1 the figure is framed, 0
                |     the figure is not framed).
                | 
                |     Example:
                | 
                |              This example retrieves the framing status of the NewMarker2D
                |              Marker2D.
                |             
                | 
                |             Dim status As Integer
                |             status = NewMarker2D.Frame

        :return: int
        """

        return self.marker2_d.Frame

    @frame.setter
    def frame(self, value):
        """
        :param int value:
        """

        self.marker2_d.Frame = value

    @property
    def picture(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Picture() As CATBSTR
                | 
                |     Returns or sets the path to a picture file for a picture
                |     Marker2D.
                | 
                |     Example:
                | 
                |              This example retrieves the path to a picture file of the
                |              NewMarker2D Marker2D.
                |             
                | 
                |             Dim path As String
                |             path = NewMarker2D.Picture

        :return: str
        """

        return self.marker2_d.Picture

    @picture.setter
    def picture(self, value):
        """
        :param str value:
        """

        self.marker2_d.Picture = value

    @property
    def text(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Text() As CATBSTR
                | 
                |     Returns or sets the text for a text Marker2D.
                | 
                |     Example:
                | 
                |              This example retrieves the text of the NewMarker2D
                |              Marker2D.
                |             
                | 
                |             Dim text As String
                |             text = NewMarker2D.Text

        :return: str
        """

        return self.marker2_d.Text

    @text.setter
    def text(self, value):
        """
        :param str value:
        """

        self.marker2_d.Text = value

    @property
    def text_angle(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property TextAngle() As double
                | 
                |     Returns or sets the text's angle for a text Marker2D.
                | 
                |     Example:
                | 
                |              This example retrieves the text's angle of the NewMarker2D
                |              Marker2D.
                |             
                | 
                |             Dim angle As Double
                |             size = NewMarker2D.TextAngle

        :return: float
        """

        return self.marker2_d.TextAngle

    @text_angle.setter
    def text_angle(self, value):
        """
        :param float value:
        """

        self.marker2_d.TextAngle = value

    @property
    def text_font(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property TextFont() As CATBSTR
                | 
                |     Returns or sets the text's font for a text Marker2D.
                | 
                |     Example:
                | 
                |              This example retrieves the text's font of the NewMarker2D
                |              Marker2D.
                |             
                | 
                |             Dim font As String
                |             font = NewMarker2D.TextFont

        :return: str
        """

        return self.marker2_d.TextFont

    @text_font.setter
    def text_font(self, value):
        """
        :param str value:
        """

        self.marker2_d.TextFont = value

    @property
    def text_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property TextOrientation() As CatMarkerTextOrientation
                | 
                |     Return or set the orientation of text.
                | 
                |     Example:
                | 
                |              This example retrieves the orientation of the NewMarker2D
                |              Marker2D.
                |             
                | 
                |             Dim orientation As CatMarkerTextOrientation
                |             orientation = NewMarker2D.TextOrientation

        :return: enum cat_marker_text_orientation
        """

        return self.marker2_d.TextOrientation

    @text_orientation.setter
    def text_orientation(self, value):
        """
        :param enum cat_marker_text_orientation value:
        """

        self.marker2_d.TextOrientation = value

    @property
    def text_size(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property TextSize() As double
                | 
                |     Returns or sets the text's size for a text Marker2D.
                | 
                |     Example:
                | 
                |              This example retrieves the text's size of the NewMarker2D
                |              Marker2D.
                |             
                | 
                |             Dim size As Double
                |             size = NewMarker2D.TextSize

        :return: float
        """

        return self.marker2_d.TextSize

    @text_size.setter
    def text_size(self, value):
        """
        :param float value:
        """

        self.marker2_d.TextSize = value

    @property
    def type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Type() As CatMarker2DType (Read Only)
                | 
                |     Returns the type of the marker 2D.
                | 
                |     Example:
                | 
                |              This example retrieves the type of the NewMarker2D
                |              Marker2D.
                |             
                | 
                |             Dim type As CatMarker2DType
                |             type = NewMarker2D.Type

        :return: enum cat_marker2_d_type
        """

        return self.marker2_d.Type

    def get_positions(self, o_coordinates=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetPositions(CATSafeArrayVariant oCoordinates)
                | 
                |     Retrieves the coordinates of the positions of the
                |     Marker2D.
                | 
                |     These positions depend on the type of the Marker2D :
                | 
                |         Line: 2 positions.
                |         Arrow: 2 positions, the first being the head and the second being the
                |         tail.
                |         Rectangle: 2 positions, the first being the bottom-left corner and the
                |         second being the top-right corner.
                |         Circle: 2 positions, the first being the center and the second being a
                |         point on the circle.
                |         FreeHand: as many positions as points.
                |         Text: 1 position, the bottom-left corner.
                |         Picture: 2 positions, the first being the bottom-left corner and the
                |         second being the top-right corner. 
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The coordinates of the positions expressed as an array of variants
                |             are:
                | 
                |                 oCoordinates(0) is the X coordinate of the first
                |                 point
                |                 oCoordinates(1) is the Y coordinate of the first
                |                 point
                |                 oCoordinates(2) is the X coordinate of the second
                |                 point
                |                 oCoordinates(3) is the Y coordinate of the second
                |                 point
                |                 oCoordinates(n*2-2) is the X coordinate of the n-th
                |                 point
                |                 oCoordinates(n*2-1) is the Y coordinate of the n-th point
                |                 
                | 
                |     Example:
                | 
                |              This example retrieves the coordinates of the positions of the
                |              NewMarker2D Marker2D.
                |             
                | 
                |             Dim Coordinates (3)
                |             NewMarker2D.GetPositions Coordinates

        :param tuple o_coordinates:
        :return: None
        """
        return self.marker2_d.GetPositions(o_coordinates)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_positions'
        # # vba_code = """
        # # Public Function get_positions(marker2_d)
        # #     Dim oCoordinates (2)
        # #     marker2_d.GetPositions oCoordinates
        # #     get_positions = oCoordinates
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_positions(self, i_coordinates=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPositions(CATSafeArrayVariant iCoordinates)
                | 
                |     Sets the coordinates of the positions of the Marker2D.
                | 
                |     These positions depend on the type of the Marker2D :
                | 
                |         Line: 2 positions.
                |         Arrow: 2 positions, the first being the head and the second being the
                |         tail.
                |         Rectangle: 2 positions, the first being the bottom-left corner and the
                |         second being the top-right corner.
                |         Circle: 2 positions, the first being the center and the second being a
                |         point on the circle.
                |         FreeHand: as many positions as points.
                |         Text: 1 position, the bottom-left corner.
                |         Picture: 2 positions, the first being the bottom-left corner and the
                |         second being the top-right corner. 
                | 
                |     Parameters:
                | 
                |         iCoordinates
                |             The coordinates of the positions expressed as an array of variants
                |             are:
                | 
                |                 iCoordinates(0) is the X coordinate of the first
                |                 point
                |                 iCoordinates(1) is the Y coordinate of the first
                |                 point
                |                 iCoordinates(2) is the X coordinate of the second
                |                 point
                |                 iCoordinates(3) is the Y coordinate of the second
                |                 point
                |                 oCoordinates(n*2-2) is the X coordinate of the n-th
                |                 point
                |                 oCoordinates(n*2-1) is the Y coordinate of the n-th point
                |                 
                | 
                |     Example:
                | 
                |              This example sets the coordinates of the positions of the
                |              NewMarker2D Marker2D.
                |             
                | 
                |             Dim Coordinates (3) 'To be valuated
                |             NewMarker2D.SetPositions Coordinates

        :param tuple i_coordinates:
        :return: None
        """
        return self.marker2_d.SetPositions(i_coordinates)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_positions'
        # # vba_code = """
        # # Public Function set_positions(marker2_d)
        # #     Dim iCoordinates (2)
        # #     marker2_d.SetPositions iCoordinates
        # #     set_positions = iCoordinates
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Marker2D(name="{ self.name }")'
