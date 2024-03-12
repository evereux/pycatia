#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.navigator_interfaces.marker_2D import Marker2D
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Marker2Ds(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Marker2Ds
                | 
                | A collection of Marker2Ds objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Marker2D)
        self.marker_2ds = com_object

    def add2_d_arrow(self, i_coordinates: tuple) -> Marker2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add2DArrow(CATSafeArrayVariant iCoordinates) As
                | Marker2D
                | 
                |     Creates an arrow marker 2D and adds it to the marker 2D collection. The
                |     arrow is defined using the coordinates of its head and tail
                |     points.
                | 
                |     Parameters:
                | 
                |         iCoordinates
                |             The coordinates
                | 
                |                 iCoordinates(0) is the X coordinate of the head
                |                 point
                |                 iCoordinates(1) is the Y coordinate of the head
                |                 point
                |                 iCoordinates(2) is the X coordinate of the tail
                |                 point
                |                 iCoordinates(3) is the Y coordinate of the tail point
                |                 
                | 
                |     Returns:
                |         The created marker 2D 
                |     Example:
                | 
                |              This example creates a new marker 2D in the TheMarker2Ds
                |              collection.
                |             
                | 
                |             Dim NewMarker2DArrow As Marker2D
                |             Set NewMarker2DArrow = TheMarker2Ds.Add2DArrow(Positions)

        :param tuple i_coordinates:
        :rtype: Marker2D
        """
        return Marker2D(self.marker_2ds.Add2DArrow(i_coordinates))

    def add2_d_circle(self, i_coordinates: tuple, i_fill_status: int) -> Marker2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add2DCircle(CATSafeArrayVariant iCoordinates,
                | long iFillStatus) As Marker2D
                | 
                |     Creates a circle marker 2D and adds it to the marker 2D collection. The
                |     circle is defined using the coordinates of its center and a point through which
                |     it passes.
                | 
                |     Parameters:
                | 
                |         iCoordinates
                |             The coordinates
                | 
                |                 iCoordinates(0) is the X coordinate of the
                |                 center
                |                 iCoordinates(1) is the Y coordinate of the
                |                 center
                |                 iCoordinates(2) is the X coordinate of the a point on the
                |                 circle
                |                 iCoordinates(3) is the Y coordinate of the a point on the
                |                 circle 
                | 
                |         iFillStatus
                |             The filling status (1 the figure is filled, 0 the figure is not
                |             filled). 
                | 
                |     Returns:
                |         The created marker 2D 
                |     Example:
                | 
                |              This example creates a new marker 2D in the TheMarker2Ds
                |              collection.
                |             
                | 
                |             Dim NewMarker2DCircle As Marker2D
                |             Set NewMarker2DCircle = TheMarker2Ds.Add2DCircle(Positions, 0)

        :param tuple i_coordinates:
        :param int i_fill_status:
        :rtype: Marker2D
        """
        return Marker2D(self.marker_2ds.Add2DCircle(i_coordinates, i_fill_status))

    def add2_d_free_hand(self, i_coordinates: tuple) -> Marker2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add2DFreeHand(CATSafeArrayVariant iCoordinates) As
                | Marker2D
                | 
                |     Creates a free hand drawing marker 2D and adds it to the marker 2D
                |     collection. The free hand drawing is defined using the coordinates of a series
                |     of points.
                | 
                |     Parameters:
                | 
                |         iCoordinates
                |             The coordinates
                | 
                |                 iCoordinates(0) is the X coordinate of the first
                |                 point
                |                 iCoordinates(1) is the Y coordinate of the first
                |                 point
                |                 iCoordinates(2) is the X coordinate of the second
                |                 point
                |                 iCoordinates(3) is the Y coordinate of the second
                |                 point
                |                 iCoordinates(n*2-2) is the X coordinate of the n-th
                |                 point
                |                 iCoordinates(n*2-1) is the Y coordinate of the n-th point
                |                 
                | 
                |     Returns:
                |         The created marker 2D 
                |     Example:
                | 
                |              This example creates a new marker 2D in the TheMarker2Ds
                |              collection.
                |             
                | 
                |             Dim NewMarker2DFreeHand As Marker2D
                |             Set NewMarker2DFreeHand = TheMarker2Ds.Add2DFreeHand(Positions)

        :param tuple i_coordinates:
        :rtype: Marker2D
        """
        return Marker2D(self.marker_2ds.Add2DFreeHand(i_coordinates))

    def add2_d_line(self, i_coordinates: tuple) -> Marker2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add2DLine(CATSafeArrayVariant iCoordinates) As
                | Marker2D
                | 
                |     Creates a line marker 2D and adds it to the marker 2D collection. The line
                |     segment is defined using the coordinates of its two
                |     endpoints.
                | 
                |     Parameters:
                | 
                |         iCoordinates
                |             The coordinates of the endpoints
                | 
                |                 iCoordinates(0) is the X coordinate of the first
                |                 endpoint
                |                 iCoordinates(1) is the Y coordinate of the first
                |                 endpoint
                |                 iCoordinates(2) is the X coordinate of the second
                |                 endpoint
                |                 iCoordinates(3) is the Y coordinate of the second endpoint
                |                 
                | 
                |     Returns:
                |         The created marker 2D 
                |     Example:
                | 
                |              This example creates a new marker 2D in the TheMarker2Ds
                |              collection.
                |             
                | 
                |             Dim NewMarker2DLine As Marker2D
                |             Set NewMarker2DLine = TheMarker2Ds.Add2DLine(Positions)

        :param tuple i_coordinates:
        :rtype: Marker2D
        """
        return Marker2D(self.marker_2ds.Add2DLine(i_coordinates))

    def add2_d_picture(self, i_coordinates: tuple, i_path: str) -> Marker2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add2DPicture(CATSafeArrayVariant iCoordinates,
                | CATBSTR iPath) As Marker2D
                | 
                |     Creates a picture marker 2D and adds it to the marker 2D collection. The
                |     picture is defined as a rectangle whose bottom-left and top-right corners are
                |     given.
                | 
                |     Parameters:
                | 
                |         iCoordinates
                |             The coordinates of the corners
                | 
                |                 iCoordinates(0) is the X coordinate of the bottom-left
                |                 point
                |                 iCoordinates(1) is the Y coordinate of the bottom-left
                |                 point
                |                 iCoordinates(2) is the X coordinate of the top-right
                |                 point
                |                 iCoordinates(3) is the Y coordinate of the top-right point
                |                 
                | 
                |         iPath
                |             The path to the picture file 
                | 
                |     Returns:
                |         The created marker 2D 
                |     Example:
                | 
                |              This example creates a new marker 2D in the TheMarker2Ds
                |              collection.
                |             
                | 
                |             Dim NewMarker2DPicture As Marker2D
                |             Set NewMarker2DPicture = TheMarker2Ds.Add2DPicture(Positions, "e:\\picture.bmp")

        :param tuple i_coordinates:
        :param str i_path:
        :rtype: Marker2D
        """
        return Marker2D(self.marker_2ds.Add2DPicture(i_coordinates, i_path))

    def add2_d_rectangle(self, i_coordinates: tuple, i_fill_status: int) -> Marker2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add2DRectangle(CATSafeArrayVariant iCoordinates,
                | long iFillStatus) As Marker2D
                | 
                |     Creates a rectangle marker 2D and adds it to the marker 2D collection. The
                |     rectangle is defined using the coordinates of its bottom-left and top-right
                |     corners.
                | 
                |     Parameters:
                | 
                |         iCoordinates
                |             The coordinates
                | 
                |                 iCoordinates(0) is the X coordinate of the bottom-left
                |                 point
                |                 iCoordinates(1) is the Y coordinate of the bottom-left
                |                 point
                |                 iCoordinates(2) is the X coordinate of the top-right
                |                 point
                |                 iCoordinates(3) is the Y coordinate of the top-right point
                |                 
                | 
                |         iFillStatus
                |             The filling status (1 the figure is filled, 0 the figure is not
                |             filled). 
                | 
                |     Returns:
                |         The created marker 2D 
                |     Example:
                | 
                |              This example creates a new marker 2D in the TheMarker2Ds
                |              collection.
                |             
                | 
                |             Dim NewMarker2DRectangle As Marker2D
                |             Set NewMarker2DRectangle = TheMarker2Ds.Add2DRectangle(Positions, 0)

        :param tuple i_coordinates:
        :param int i_fill_status:
        :rtype: Marker2D
        """
        return Marker2D(self.marker_2ds.Add2DRectangle(i_coordinates, i_fill_status))

    def add2_d_text(self, i_coordinates: tuple, i_text: str) -> Marker2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add2DText(CATSafeArrayVariant iCoordinates,
                | CATBSTR iText) As Marker2D
                | 
                |     Creates a text marker 2D and adds it to the marker 2D collection. The text
                |     is anchored using the coordinates of its bottom-left
                |     point.
                | 
                |     Parameters:
                | 
                |         iCoordinates
                |             The coordinates
                | 
                |                 iCoordinates(0) is the X coordinate of the bottom-left
                |                 point
                |                 iCoordinates(1) is the Y coordinate of the bottom-left point
                |                 
                | 
                |         iText
                |             The text 
                | 
                |     Returns:
                |         The created marker 2D 
                |     Example:
                | 
                |              This example creates a new marker 2D in the TheMarker2Ds
                |              collection.
                |             
                | 
                |             Dim NewMarker2DText As Marker2D
                |             Set NewMarker2DText = TheMarker2Ds.Add2DText(Positions, "example")

        :param tuple i_coordinates:
        :param str i_text:
        :rtype: Marker2D
        """
        return Marker2D(self.marker_2ds.Add2DText(i_coordinates, i_text))

    def item(self, i_index: cat_variant) -> Marker2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As Marker2D
                | 
                |     Returns a marker 2D using its index from the Marker2Ds
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the marker 2D to retrieve from the collection of
                |             Marker2Ds. As a numerics, this index is the rank of the marker 2D in the
                |             collection. The index of the first marker 2D in the collection is 1, and the
                |             index of the last marker 2D is Count. 
                | 
                |     Returns:
                |         The retrieved marker 2D 
                |     Example:
                | 
                |              This example retrieves in ThisMarker2D the ninth marker 2D
                |              
                |             from the TheMarker2Ds collection. 
                |             
                | 
                |             Dim ThisMarker2D As Marker2D
                |             Set ThisMarker2D = TheMarker2Ds.Item(9)

        :param cat_variant i_index:
        :rtype: Marker2D
        """
        return Marker2D(self.marker_2ds.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a marker 2D from the Marker2Ds collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the marker 2D to retrieve from he collection of
                |             Marker2Ds. As a numerics, this index is the rank of the marker 2D in the
                |             collection. The index of the first marker 2D in the collection is 1, and the
                |             index of the last marker 2D is Count. 
                | 
                |     Example:
                | 
                |              The following example removes the tenth marker 2D from the
                |              TheMarker2Ds collection.
                |             
                | 
                |             TheMarker2Ds.Remove(10)

        :param cat_variant i_index:
        :rtype: None
        """
        return self.marker_2ds.Remove(i_index)

    def __getitem__(self, n: int) -> Marker2D:
        if (n + 1) > self.count:
            raise StopIteration

        return Marker2D(self.marker_2ds.Item(n + 1))

    def __iter__(self) -> Iterator[Marker2D]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Marker2Ds(name="{self.name}")'
