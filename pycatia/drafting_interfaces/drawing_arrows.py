#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.drafting_interfaces.drawing_arrow import DrawingArrow
from pycatia.system_interfaces.collection import Collection


class DrawingArrows(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingArrows
                | 
                | A collection of all the drawing arrows currently managed by a drawing view of
                | drawing sheet in a drawing document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingArrow)
        self.drawing_arrows = com_object

    def add(self,
            i_head_point_x: float,
            i_head_point_y: float,
            i_tail_point_x: float,
            i_tail_point_y: float) -> DrawingArrow:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add(double iHeadPointX,
                | double iHeadPointY,
                | double iTailPointX,
                | double iTailPointY) As DrawingArrow
                | 
                |     Creates a drawing arrow and adds it to the DrawingArrows
                |     collection.
                | 
                |     Parameters:
                | 
                |         iHeadPointX,iHeadPointY
                |             The x and y coordinates of head side of drawing arrow
                |             
                |         iTailPointX,iTailPointY
                |             The x and y coordinates of tail side of drawing arrow
                |             
                | 
                |     Returns:
                |         The created drawing arrow 
                | 
                | Example:
                |     The following example creates a drawing arrow and retrieved in MyArrow in
                |     the drawing view collection of the MyView drawing view. This view belongs to
                |     the drawing view collection of the drawing sheet
                | 
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.ActiveView
                |      Dim MyArrow As DrawingArrow
                |      Set MyArrow = MyView.Arrows.Add(0., 0., 20., 50)

        :param float i_head_point_x:
        :param float i_head_point_y:
        :param float i_tail_point_x:
        :param float i_tail_point_y:
        :rtype: DrawingArrow
        """
        return DrawingArrow(self.drawing_arrows.Add(i_head_point_x, i_head_point_y, i_tail_point_x, i_tail_point_y))

    def item(self, i_index: int) -> DrawingArrow:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(long iIndex) As DrawingArrow
                | 
                |     Returns a drawing arrow using its index from the DrawingArrows
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing arrow to retrieve from the collection of
                |             drawing arrows. As a numerics, this index is the rank of the drawing arrow in
                |             the collection. The index of the first drawing arrow in the collection is 1,
                |             and the index of the last drawing arrow is Count. 
                | 
                |     Returns:
                |         The retrieved drawing view 
                |     Example:
                |         This example retrieves in ThisDrawingArrow the second drawing arrow, in
                |         the drawing view collection of the active view in the active sheet, in the
                |         active document supposed to be a drawing document.
                | 
                |          Dim MyView  As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          Dim ThisDrawingArrow As DrawingArrow
                |          Set ThisDrawingArrow = MyView.Arrows.Item(2)

        :param int i_index:
        :rtype: DrawingArrow
        """
        return DrawingArrow(self.drawing_arrows.Item(i_index))

    def remove(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(long iIndex)
                | 
                |     Removes a drawing arrow from the DrawingArrows collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing arrow to remove from the collection of
                |             drawing arrows. As a numerics, this index is the rank of the drawing arrow in
                |             the collection. The index of the first drawing arrow in the collection is 1,
                |             and the index of the last drawing arrow is Count. 
                | 
                |     Example:
                |         The following example removes the third drawing arrow in the drawing
                |         arrow collection of the active view of the active document, supposed to be a
                |         drawing document.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.DrawingArrows.Remove(3)

        :param int i_index:
        :rtype: None
        """
        return self.drawing_arrows.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingArrow:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingArrow(self.drawing_arrows.Item(n + 1))

    def __iter__(self) -> Iterator[DrawingArrow]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DrawingArrows(name="{self.name}")'
