#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.drafting_interfaces.drawing_welding import DrawingWelding
from pycatia.system_interfaces.collection import Collection


class DrawingWeldings(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingWeldings
                | 
                | A collection of all the drawing weldings currently managed by a drawing view of
                | drawing sheet in a drawing document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingWelding)
        self.drawing_weldings = com_object

    def add(self, i_symbol: int, i_position_x: float, i_position_y: float) -> DrawingWelding:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add(CatWeldingSymbol iSymbol,
                | double iPositionX,
                | double iPositionY) As DrawingWelding
                | 
                |     Creates a drawing welding and adds it to the drawing weldings collection.
                |     This drawing welding becomes the active one.
                | 
                |     Parameters:
                | 
                |         iSymbol
                |             The drawing welding symbol to assign to the drawing welding
                |             
                |         iPositionX,iPositionY
                |             The drawing welding x and y coordinates, expressed in millimeters,
                |             and expressed with respect to the view coordinate system
                |             
                | 
                |     Returns:
                |         The created drawing welding 
                | 
                | Example:
                |     The following example creates a drawing welding, retrieved in MyWelding, in
                |     the MyView drawing view. This view belongs to the drawing view collection of
                |     the drawing sheet.
                | 
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.ActiveView
                |      Dim MyWelding As DrawingWelding
                |      Set MyWelding = 
                |         MyView.Weldings.Add(catSquareWelding, 0., 0.)

        :param int i_symbol: enum cat_welding_symbol
        :param float i_position_x:
        :param float i_position_y:
        :rtype: DrawingWelding
        """
        return DrawingWelding(self.drawing_weldings.Add(i_symbol, i_position_x, i_position_y))

    def item(self, i_index: int) -> DrawingWelding:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(long iIndex) As DrawingWelding
                | 
                |     Returns a drawing welding using its index from the drawing weldings
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing welding to retrieve from the collection of
                |             drawing weldings. As a numerics, this index is the rank of the drawing welding
                |             in the collection. The index of the first drawing welding in the collection is
                |             1, and the index of the last drawing welding is Count.
                |             
                | 
                |     Returns:
                |         The retrieved drawing welding 
                | 
                | Example:
                |     This example retrieves in ThisDrawingWelding the second drawing welding, in
                |     the drawing welding collection of the active view in the active sheet, in the
                |     active document supposed to be a drawing document.
                | 
                |      Dim MyView  As DrawingView
                |      Set MyView  = MySheet.Views.ActiveView
                |      Dim ThisDrawingWelding As DrawingWelding
                |      Set ThisDrawingWelding = MyView.Weldings.Item(2)

        :param int i_index:
        :rtype: DrawingWelding
        """
        return DrawingWelding(self.drawing_weldings.Item(i_index))

    def remove(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(long iIndex)
                | 
                |     Removes a drawing welding from the drawing weldings
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing welding to remove from the collection of
                |             drawing weldings. As a numerics, this index is the rank of the drawing text in
                |             the collection. The index of the first drawing welding in the collection is 1,
                |             and the index of the last drawing welding is Count.
                |             
                | 
                |     Example:
                |         The following example removes the third drawing welding from the
                |         drawing welding collection of the active view of the active document, supposed
                |         to be a drawing document.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.Drawing.Remove(3)

        :param int i_index:
        :rtype: None
        """
        return self.drawing_weldings.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingWelding:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingWelding(self.drawing_weldings.Item(n + 1))

    def __iter__(self) -> Iterator[DrawingWelding]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DrawingWeldings(name="{self.name}")'
