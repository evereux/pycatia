#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.drafting_interfaces.drawing_coord_dim import DrawingCoordDim
from pycatia.system_interfaces.collection import Collection


class DrawingCoordDims(Collection):
    """

    Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingCoordDims
                |
                | A collection of all the drawing Coordinate Dimension currently managed by a
                | drawing view of drawing sheet in a drawing document.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_coord_dims = com_object

    def item(self, i_index: int) -> DrawingCoordDim:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func Item(long iIndex) As DrawingCoordDim
                |     Returns a drawing CoordDim using its index from the drawing CoordDims
                |     collection.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index of the drawing CoordDim to retrieve from the collection
                |             of drawing CoordDims. As a numerics, this index is the rank of the drawing
                |             CoordDim in the collection. The index of the first drawing CoordDim in the
                |             collection is 1, and the index of the last drawing CoordDim is Count.
                |
                |     Returns:
                |         The retrieved drawing CoordDim
                |
                | Example:
                |     This example retrieves in ThisDrawingCoordDim the second drawing CoordDim,
                |     in the drawing CoordDim collection of the active view in the active sheet, in
                |     the active document supposed to be a drawing document.
                |
                |      Dim MyView  As DrawingView
                |      Set MyView  = MySheet.Views.ActiveView
                |      Dim ThisDrawingCoordDim As DrawingCoordDim
                |      Set ThisDrawingCoordDim = MyView.CoordDims.Item(2)

        :param int i_index:
        :rtype: DrawingCoordDim
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return DrawingCoordDim(self.drawing_coord_dims.Item(i_index))

    def remove(self, i_index: int) -> None:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub Remove(long iIndex)
                |     Removes a drawing CoordDim from the drawing CoordDims
                |     collection.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index of the drawing CoordDim to remove from the collection of
                |             drawing CoordDims. As a numerics, this index is the rank of the drawing text in
                |             the collection. The index of the first drawing CoordDim in the collection is 1,
                |             and the index of the last drawing CoordDim is Count.
                |
                |
                |     Example:
                |         The following example removes the third drawing CoordDim from the
                |         drawing CoordDim collection of the active view of the active document, supposed
                |         to be a drawing document.
                |
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.CoordDims.Remove(3)

        :param int i_index:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_coord_dims.Remove(i_index)

    def __repr__(self):
        return f'DrawingCoordDims(name="{self.name}")'
