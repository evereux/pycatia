#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:02:39.913626

from pycatia.system_interfaces.collection import Collection
from .drawingarrow import DrawingArrow


class DrawingArrows(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | A collection of all the drawing arrows currently managed by a drawing
                | view of drawing sheet in a drawing document.

    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingArrow)
        self.drawing_arrows = com_object

    def add(self, i_head_point_x, i_head_point_y, i_tail_point_x, i_tail_point_y):
        """
        .. note::
            CAA V5 Visual Basic help

                | Add
                | o Func Add(        iHeadPointX,
                |                    iHeadPointY,
                |                    iTailPointX,
                |                    iTailPointY) As
                | 
                | Creates a drawing arrow and adds it to the DrawingArrows
                | collection.
                |
                | Parameters:
                | iHeadPointX,iHeadPointY
                |   The x and y coordinates of head side of drawing arrow
                | iTailPointX,iTailPointY
                |   The x and y coordinates of tail side of drawing arrow
                |  Returns:
                |   The created drawing arrow
                |
                | Examples:
                | The following example creates a drawing arrow and retrieved
                | in MyArrow in the drawing view collection of the MyView
                | drawing view. This view belongs to the drawing view
                | collection of the drawing sheet Dim MyView As DrawingView
                | Set MyView = MySheet.Views.ActiveView Dim MyArrow As
                | DrawingArrow Set MyArrow = MyView.Arrows.Add(0., 0., 20.,
                | 50)

        :param float i_head_point_x:
        :param float i_head_point_y:
        :param float i_tail_point_x:
        :param float i_tail_point_y:
        :return: DrawingArrow()
        """
        return self.child_object(
            self.drawing_arrows.Add(i_head_point_x, i_head_point_y, i_tail_point_x, i_tail_point_y))

    def item(self, i_index):
        """

        .. warning::
            The index when not a string must be it's python index (indexes in python start from 0).
            collection. The COM interface index starts at 1.

        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(        iIndex) As
                | 
                | Returns a drawing arrow using its index from the
                | DrawingArrows collection.
                |
                | Parameters:
                | iIndex
                |    The index of the drawing arrow to retrieve from the collection of drawing arrows.
                |    As a numeric, this index is the rank of the drawing arrow in the collection.
                |    The index of the first drawing arrow in the collection is 1, and
                |    the index of the last drawing arrow is Count.
                | Returns:
                |   The retrieved drawing view
                |
                | Examples:
                | This example retrieves in ThisDrawingArrow the second
                | drawing arrow, in the drawing view collection of the active
                | view in the active sheet, in the active document supposed to
                | be a drawing document.
                | Dim MyView As DrawingView
                | Set MyView = MySheet.Views.ActiveView
                | Dim ThisDrawingArrow As DrawingArrow
                | Set ThisDrawingArrow = MyView.Arrows.Item(2)

        :param int i_index:
        :return: DrawingArrow()
        """

        if isinstance(i_index, int):
            i_index += 1

        return DrawingArrow(self.drawing_arrows.Item(i_index))

    def remove(self, i_index):
        """
        .. warning::
            The index when not a string must be it's python index (indexes in python start from 0).
            collection. The COM interface index starts at 1.

        .. note::
            CAA V5 Visual Basic help

                | Remove
                | o Sub Remove(iIndex)
                | 
                | Removes a drawing arrow from the DrawingArrows collection.
                |
                | Parameters:
                | iIndex
                |    The index of the drawing arrow to remove from
                |    the collection of drawing arrows.
                |    As a numeric, this index is the rank of the drawing arrow
                |    in the collection.
                |    The index of the first drawing arrow in the collection is 1, and
                |    the index of the last drawing arrow is Count.
                |
                | Examples:
                | The following example removes the third drawing arrow in the
                | drawing arrow collection of the active view of the active
                | document, supposed to be a drawing document. Dim MyView As
                | DrawingView Set MyView = MySheet.Views.ActiveView
                | MyView.DrawingArrows.Remove(3)

        :param int i_index:
        :return:
        """

        if isinstance(i_index, int):
            i_index += 1
        self.drawing_arrows.Remove(i_index)

    def __repr__(self):
        return f'DrawingArrows(name="{self.name}")'
