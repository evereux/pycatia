#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class Marker3D(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Marker3D
                | 
                | Represents a marker 3D.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.marker_3d = com_object

    @property
    def fill(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Fill() As long
                | 
                |     Returns or sets the marker 3D's filling status (1 the figure is filled, 0
                |     the figure is not filled).
                | 
                |     Example:
                | 
                |              This example retrieves the filling status of NewMarker3D marker
                |              3D.
                |             
                | 
                |             Dim status As Integer
                |             status = NewMarker3D.Fill

        :rtype: int
        """

        return self.marker_3d.Fill

    @fill.setter
    def fill(self, value: int):
        """
        :param int value:
        """

        self.marker_3d.Fill = value

    @property
    def frame(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Frame() As long
                | 
                |     Returns or sets the marker 3D's framing status (1 the figure is framed, 0
                |     the figure is not framed).
                | 
                |     Example:
                | 
                |              This example retrieves the framing status of NewMarker3D marker
                |              3D.
                |             
                | 
                |             Dim status As Integer
                |             status = NewMarker3D.Frame

        :rtype: int
        """

        return self.marker_3d.Frame

    @frame.setter
    def frame(self, value: int):
        """
        :param int value:
        """

        self.marker_3d.Frame = value

    @property
    def text(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Text() As CATBSTR
                | 
                |     Returns or sets the text for a text marker 3D.
                | 
                |     Example:
                | 
                |              This example reads the text of NewMarker3D marker
                |              3D.
                |             
                | 
                |             Dim text As String
                |             text = NewMarker3D.Text

        :rtype: str
        """

        return self.marker_3d.Text

    @text.setter
    def text(self, value: str):
        """
        :param str value:
        """

        self.marker_3d.Text = value

    @property
    def text_font(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TextFont() As CATBSTR
                | 
                |     Returns or sets the text's font for a marker 3D.
                | 
                |     Example:
                | 
                |              This example retrieves the text's font of NewMarker3D marker
                |              3D.
                |             
                | 
                |             Dim font As String
                |             font = NewMarker3D.TextFont

        :rtype: str
        """

        return self.marker_3d.TextFont

    @text_font.setter
    def text_font(self, value: str):
        """
        :param str value:
        """

        self.marker_3d.TextFont = value

    @property
    def text_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TextOrientation() As CatMarkerTextOrientation
                | 
                |     Returns or sets the orientation of text.
                | 
                |     Example:
                | 
                |              This example retrieves the orientation of NewMarker3D marker
                |              3D.
                |             
                | 
                |             Dim orientation As CatMarkerTextOrientation
                |             orientation = NewMarker3D.TextOrientation

        :return:  enum cat_marker_text_orientation
        :rtype: int
        """

        return self.marker_3d.TextOrientation

    @text_orientation.setter
    def text_orientation(self, value: int):
        """
        :param int value: enum cat_marker_text_orientation
        """

        self.marker_3d.TextOrientation = value

    @property
    def text_size(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TextSize() As double
                | 
                |     Returns or sets the text's size for a marker 3D.
                | 
                |     Example:
                | 
                |              This example retrieves the text's size of NewMarker3D marker
                |              3D.
                |             
                | 
                |             Dim size As Double
                |             size = NewMarker3D.TextSize

        :rtype: float
        """

        return self.marker_3d.TextSize

    @text_size.setter
    def text_size(self, value: float):
        """
        :param float value:
        """

        self.marker_3d.TextSize = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Type() As CatMarker3DType (Read Only)
                | 
                |     Returns the type of the marker 3D.
                | 
                |     Example:
                | 
                |              This example reads the type of NewMarker3D marker
                |              3D.
                |
                |             Dim type As CatMarker3DType
                |             type = NewMarker3D.Type

        :return: eum cat_marker_3d_type
        :rtype: int
        """

        return self.marker_3d.Type

    def add_object(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddObject(AnyObject iObject)
                | 
                |     Adds a link to an object.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to be linked. 
                | 
                |     Example:
                | 
                |              This example links ThisProduct to the NewMarker3D marker
                |              3D.
                |             
                | 
                |             NewMarker3D.AddObject(ThisProduct)

        :param AnyObject i_object:
        :rtype: None
        """
        return self.marker_3d.AddObject(i_object.com_object)

    def count_object(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CountObject() As long
                | 
                |     Returns the number of objects which are linked to the marker
                |     3D.
                | 
                |     Example:
                | 
                |              This example reads the number of objects in the marker3D
                |              NewMarker3D.
                |             
                | 
                |             Dim number As Integer
                |             number = NewMarker3D.CountObject

        :rtype: int
        """
        return self.marker_3d.CountObject()

    def get_object_positions(self, i_index: cat_variant, o_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetObjectPositions(CATVariant iIndex,
                | CATSafeArrayVariant oCoordinates)
                | 
                |     Retrieves the coordinates of the anchor point of the marker on the
                |     object.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the object in the marker 3D. The index of the first
                |             object is 1, and the index of the last object is CountObject.
                |             
                |         oCoordinates
                |             The coordinates of the anchor point
                | 
                |                 oCoordinates(0) is the X coordinate of the anchor
                |                 point
                |                 oCoordinates(1) is the Y coordinate of the anchor
                |                 point
                |                 oCoordinates(2) is the Z coordinate of the anchor point
                |                 
                | 
                |     Example:
                | 
                |              This example retrieves the coordinates of the anchor in the
                |              NewMarker3D marker 3D.
                |             
                | 
                |             Dim Coordinates (3)
                |             NewMarker3D.GetObjectPositions Coordinates

        :param cat_variant i_index:
        :param tuple o_coordinates:
        :rtype: None
        """
        return self.marker_3d.GetObjectPositions(i_index, o_coordinates)

    def get_text_positions(self, o_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetTextPositions(CATSafeArrayVariant oCoordinates)
                | 
                |     Retrieves the coordinates of the positions of a text marker 3D. The
                |     bottom-left corner of the text is anchored to a given
                |     point.
                | 
                |     Returns:
                |         The coordinates of the text anchor point
                | 
                |             oCoordinates(0) is the X coordinate of the text anchor
                |             point
                |             oCoordinates(1) is the Y coordinate of the text anchor
                |             point
                |             oCoordinates(2) is the Z coordinate of the text anchor point
                |             
                | 
                |     Example:
                | 
                |              This example retrieves the coordinates of the text in the
                |              NewMarker3D marker 3D.
                |             
                | 
                |             Dim Coordinates (2)
                |             NewMarker3D.GetTextPositions Coordinates

        :param tuple o_coordinates:
        :rtype: None
        """
        return self.marker_3d.GetTextPositions(o_coordinates)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_text_positions'
        # # vba_code = """
        # # Public Function get_text_positions(marker_3d)
        # #     Dim oCoordinates (2)
        # #     marker_3d.GetTextPositions oCoordinates
        # #     get_text_positions = oCoordinates
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def item_object(self, i_index: cat_variant) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func ItemObject(CATVariant iIndex) As CATBaseDispatch
                | 
                |     Returns an object which is linked to the marker 3D using its
                |     index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the object in the marker 3D. The index of the first
                |             object is 1, and the index of the last object is CountObject.
                |             
                | 
                |     Returns:
                |         The retrieved object 
                |     Example:
                | 
                |              This example retrieves in ThisObject the ninth
                |              object
                |             from the NewMarker3D marker 3D.
                |             
                | 
                |             Dim ThisObject As Marker3D
                |             Set ThisObject = NewMarker3D.ItemObject(9)

        :param cat_variant i_index:
        :rtype: AnyObject
        """
        return self.marker_3d.ItemObject(i_index)

    def remove_object(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveObject(CATVariant iIndex)
                | 
                |     Removes an object which is linked to the marker 3D using its
                |     index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the object in the marker 3D. The index of the first
                |             object is 1, and the index of the last object is CountObject.
                |             
                | 
                |     Example:
                | 
                |              This example removes the ninth object
                |             from the NewMarker3D marker 3D.
                |             
                | 
                |             NewMarker3D.RemoveObject(9)

        :param cat_variant i_index:
        :rtype: None
        """
        return self.marker_3d.RemoveObject(i_index)

    def set_object_positions(self, i_index: cat_variant, i_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetObjectPositions(CATVariant iIndex,
                | CATSafeArrayVariant iCoordinates)
                | 
                |     Sets the coordinates of the anchor point of the marker on the
                |     object.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the object in the marker 3D. The index of the first
                |             object is 1, and the index of the last object is CountObject.
                |             
                |         iCoordinates
                |             The coordinates of the anchor point
                | 
                |                 oCoordinates(0) is the X coordinate of the anchor
                |                 point
                |                 oCoordinates(1) is the Y coordinate of the anchor
                |                 point
                |                 oCoordinates(2) is the Z coordinate of the anchor point
                |                 
                | 
                |     Example:
                | 
                |              This example sets the coordinates of the anchor in the NewMarker3D
                |              marker 3D.
                |             
                | 
                |             Dim Coordinates (3)
                |             NewMarker3D.SetObjectPositions Coordinates

        :param cat_variant i_index:
        :param tuple i_coordinates:
        :rtype: None
        """
        return self.marker_3d.SetObjectPositions(i_index, i_coordinates)

    def set_text_positions(self, i_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTextPositions(CATSafeArrayVariant iCoordinates)
                | 
                |     Sets the coordinates of the positions of a text marker 3D.
                | 
                |     Parameters:
                | 
                |         iCoordinates
                |             The coordinates of the text anchor point
                | 
                |                 oCoordinates(0) is the X coordinate of the text anchor
                |                 point
                |                 oCoordinates(1) is the Y coordinate of the text anchor
                |                 point
                |                 oCoordinates(2) is the Z coordinate of the text anchor point
                |                 
                | 
                |     Example:
                | 
                |              This example sets the coordinates of the text in the NewMarker3D
                |              marker 3D.
                |             
                | 
                |             Dim Coordinates (2)
                |             NewMarker3D.SetTextPositions Coordinates

        :param tuple i_coordinates:
        :rtype: None
        """
        return self.marker_3d.SetTextPositions(i_coordinates)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_text_positions'
        # # vba_code = """
        # # Public Function set_text_positions(marker_3d)
        # #     Dim iCoordinates (2)
        # #     marker_3d.SetTextPositions iCoordinates
        # #     set_text_positions = iCoordinates
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Update()
                | 
                |     Updates the the marker 3D: that is to take into account all modifications
                |     which occur since last update.
                | 
                |     Example:
                | 
                |              This example updates the NewMarker3D marker 3D.
                |             
                | 
                |             NewMarker3D.Update

        :rtype: None
        """
        return self.marker_3d.Update()

    def __repr__(self):
        return f'Marker3D(name="{self.name}")'
