#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
from typing import Iterator

from pycatia.navigator_interfaces.marker_3D import Marker3D
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Marker3Ds(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Marker3Ds
                | 
                | A collection of Marker3D objects.
                | 
                | The method Product.GetTechnologicalObject ("Marker3Ds") on the root product
                | retrieves this collection.

    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Marker3D)
        self.marker_3ds = com_object

    def add3_d_text(self, i_text_coordinates: tuple, i_text: str, i_object_coordinates: tuple,
                    i_object: AnyObject) -> Marker3D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add3DText(CATSafeArrayVariant iTextCoordinates,
                | CATBSTR iText,
                | CATSafeArrayVariant iObjectCoordinates,
                | AnyObject iObject) As Marker3D
                | 
                |     Creates a text marker 3D and adds it to the marker 3D collection. The
                |     bottom-left corner of the text is anchored to a given
                |     point.
                | 
                |     Parameters:
                | 
                |         iTextCoordinates
                |             The coordinates of the text anchor point
                | 
                |                 iTextCoordinates(0) is the X coordinate of the text anchor
                |                 point
                |                 iTextCoordinates(1) is the Y coordinate of the text anchor
                |                 point
                |                 iTextCoordinates(2) is the Z coordinate of the text anchor
                |                 point 
                | 
                |         iText
                |             The text 
                |         iObjectCoordinates
                |             The coordinates of the anchor of the marker 3D on the
                |             object
                | 
                |                 iObjectCoordinates(0) is the X coordinate of the object anchor
                |                 point
                |                 iObjectCoordinates(1) is the Y coordinate of the object anchor
                |                 point
                |                 iObjectCoordinates(2) is the Z coordinate of the object anchor
                |                 point 
                | 
                |         iObject
                |             The object which supports the text. 
                | 
                |     Returns:
                |         The created marker 3D 
                |     Example:
                | 
                |              This example creates a new marker 3D in the TheMarker3Ds
                |              collection.
                |             
                | 
                |             Dim NewMarker3DText As Marker3D
                |             Set NewMarker3DText = TheMarker3Ds.Add3DText(Position1, "example", Position2, Product2)

        :param tuple i_text_coordinates:
        :param str i_text:
        :param tuple i_object_coordinates:
        :param AnyObject i_object:
        :rtype: Marker3D
        """
        return Marker3D(
            self.marker_3ds.Add3DText(i_text_coordinates, i_text, i_object_coordinates, i_object.com_object))

    def item(self, i_index: cat_variant) -> Marker3D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As Marker3D
                | 
                |     Returns a marker 3D using its index from the Marker3Ds
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the marker 3D to retrieve from the
                |             collection of Marker3Ds. As a numerics, this index is the rank of the marker 3D
                |             in the collection. The index of the first Marker3D in the collection is 1, and
                |             the index of the last Marker3D is Count. As a string, it is the name you
                |             assigned to the Marker3D. 
                | 
                |     Returns:
                |         The retrieved marker 3D 
                |     Example:
                | 
                |              This example retrieves in ThisMarker3D the ninth marker
                |              3D,
                |             and in ThatMarker3D the marker 3D named
                |             Marker3D3 from the TheMarker3Ds collection. 
                |             
                | 
                |             Dim ThisMarker3D As Marker3D
                |             Set ThisMarker3D = TheMarker3Ds.Item(9)
                |             Dim ThatMarker3D As Marker3D
                |             Set ThatMarker3D = TheMarker3Ds.Item("Marker3D3")

        :param cat_variant i_index:
        :rtype: Marker3D
        """
        return Marker3D(self.marker_3ds.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a marker 3D from the Marker3Ds collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the marker 3D to retrieve from the
                |             collection of Marker3Ds. As a numerics, this index is the rank of the marker 3D
                |             in the collection. The index of the first marker 3D in the collection is 1, and
                |             the index of the last marker 3D is Count. As a string, it is the name you
                |             assigned to the marker 3D. 
                | 
                |     Example:
                | 
                |              The following example removes the tenth marker 3D and the marker
                |              3D named
                |             Marker3D2 from the TheMarker3Ds collection.
                |             
                | 
                |             TheMarker3Ds.Remove(10)
                |             TheMarker3Ds.Remove("Marker3D2")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.marker_3ds.Remove(i_index)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(marker_3ds)
        # #     Dim iIndex (2)
        # #     marker_3ds.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __getitem__(self, n: int) -> Marker3D:
        if (n + 1) > self.count:
            raise StopIteration

        return Marker3D(self.marker_3ds.Item(n + 1))

    def __iter__(self) -> Iterator[Marker3D]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Marker3Ds(name="{self.name}")'
