#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.drafting_interfaces.drawing_leader import DrawingLeader
from pycatia.system_interfaces.collection import Collection


class DrawingLeaders(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingLeaders
                | 
                | A collection of all the drawing leaders currently managed by a drawing view of
                | drawing sheet in a drawing document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingLeader)
        self.drawing_leaders = com_object

    def add(self, i_head_point_x: float, i_head_point_y: float) -> DrawingLeader:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add(double iHeadPointX,
                | double iHeadPointY) As DrawingLeader
                | 
                |     Creates a drawing leader and adds it to the DrawingLeaders
                |     collection.
                | 
                |     Parameters:
                | 
                |         iHeadPointX,iHeadPointY
                |             The x and y coordinates of head side of drawing leader
                |             
                | 
                |     Returns:
                |         The created drawing leader 
                | 
                | Example:
                |     The following example creates a drawing leader and retrieved in MyLeader in
                |     the drawing text collection of the MyText drawing text. This text belongs to
                |     the drawing text collection of the drawing view
                | 
                |      Dim MyTexts As DrawingTexts
                |      Set MyTexts = MySheet.Views.ActiveView
                |      Dim MyText As DrawingText
                |      Set MyText = MyTexts.Item(1)
                |      Dim MyLeader As DrawingLeader
                |      Set MyLeader = MyText.Leaders.Add(20., 50)

        :param float i_head_point_x:
        :param float i_head_point_y:
        :rtype: DrawingLeader
        """
        return DrawingLeader(self.drawing_leaders.Add(i_head_point_x, i_head_point_y))

    def item(self, i_index: int) -> DrawingLeader:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(long iIndex) As DrawingLeader
                | 
                |     Returns a drawing leader using its index from the DrawingLeaders
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing leader to retrieve from the collection of
                |             drawing arrows. As a numerics, this index is the rank of the drawing leader in
                |             the collection. The index of the first drawing leader in the collection is 1,
                |             and the index of the last drawing leader is Count.
                |             
                | 
                |     Returns:
                |         The retrieved drawing view 
                |     Example:
                |         This example retrieves in ThisDrawingLeader the second drawing leader,
                |         in the drawing view collection of the active view in the active sheet, in the
                |         active document supposed to be a drawing document.
                | 
                |          Dim MyView  As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          Dim ThisDrawingLeader As DrawingLeader
                |          Set ThisDrawingLeader = MyView.Leaders.Item(2)

        :param int i_index:
        :rtype: DrawingLeader
        """
        return DrawingLeader(self.drawing_leaders.Item(i_index))

    def remove(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(long iIndex)
                | 
                |     Removes a drawing leader from the DrawingLeaders
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing leader to remove from the collection of
                |             drawing leaders. As a numerics, this index is the rank of the drawing leader in
                |             the collection. The index of the first drawing leader in the collection is 1,
                |             and the index of the last drawing leader is Count.
                |             
                | 
                |     Example:
                |         The following example removes the third drawing leader in the drawing
                |         leader collection of the active view of the active document, supposed to be a
                |         drawing document.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.DrawingLeaders.Remove(3)

        :param int i_index:
        :rtype: None
        """
        return self.drawing_leaders.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingLeader:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingLeader(self.drawing_leaders.Item(n + 1))

    def __iter__(self) -> Iterator[DrawingLeader]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DrawingLeaders(name="{self.name}")'
