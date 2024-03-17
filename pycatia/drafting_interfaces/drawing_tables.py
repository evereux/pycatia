#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.drafting_interfaces.drawing_table import DrawingTable
from pycatia.system_interfaces.collection import Collection


class DrawingTables(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingTables
                | 
                | A collection of all the drawing tables currently managed by a drawing view of
                | drawing sheet in a drawing document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingTable)
        self.drawing_tables = com_object

    def add(self,
            i_position_x: float,
            i_position_y: float,
            i_number_of_row: int,
            i_number_of_column: int,
            i_row_height: float,
            i_column_width: float) -> DrawingTable:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add(double iPositionX,
                | double iPositionY,
                | long iNumberOfRow,
                | long iNumberOfColumn,
                | double iRowHeight,
                | double iColumnWidth) As DrawingTable
                | 
                |     Creates a drawing table and adds it to the DrawingTables
                |     collection.
                | 
                |     Parameters:
                | 
                |         iPositionX,iPositionY
                |             The drawing table x and y coordinates, expressed in millimeters,
                |             with respect to the drawing view coordinate system
                |             
                |         iNumberOfRow,iNumberOfColumn
                |             The drawing table number of rows and columns 
                |         iRowHeight,iColumnWidth
                |             The row height and the column width 
                | 
                |     Returns:
                |         The created drawing table 
                | 
                | Example:
                |     The following example creates an empty drawing table and retrieves it in
                |     MyTable in the drawing table collection of the active view MyView of the
                |     drawing sheet MySheet.
                | 
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.ActiveView
                |      Dim MyTable As DrawingTable
                |      Set MyTable = MyView.Tables.Add(100., 100., 2, 2, 20., 50.)

        :param float i_position_x:
        :param float i_position_y:
        :param int i_number_of_row:
        :param int i_number_of_column:
        :param float i_row_height:
        :param float i_column_width:
        :rtype: DrawingTable
        """
        return DrawingTable(
            self.drawing_tables.Add(
                i_position_x,
                i_position_y,
                i_number_of_row,
                i_number_of_column,
                i_row_height,
                i_column_width
            )
        )

    def item(self, i_index: int) -> DrawingTable:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(long iIndex) As DrawingTable
                | 
                |     Returns a drawing table using its index from the DrawingTables
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing table to retrieve from the collection of
                |             drawing tables. As a numerics, this index is the rank of the drawing table in
                |             the collection. The index of the first drawing table in the collection is 1,
                |             and the index of the last drawing table is Count. 
                | 
                |     Returns:
                |         The retrieved drawing table 
                |     Example:
                |         This example retrieves in ThisDrawingTable the second drawing table, in
                |         the drawing view collection of the active view in the active sheet, in the
                |         active document supposed to be a drawing document.
                | 
                |          Dim MyView  As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          Dim ThisDrawingTable As DrawingTable
                |          Set ThisDrawingTable = MyView.Tables.Item(2)

        :param int i_index:
        :rtype: DrawingTable
        """
        return DrawingTable(self.drawing_tables.Item(i_index))

    def remove(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(long iIndex)
                | 
                |     Removes a drawing table from the DrawingTables collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing table to remove from the collection of
                |             drawing tables. As a numerics, this index is the rank of the drawing table in
                |             the collection. The index of the first drawing table in the collection is 1,
                |             and the index of the last drawing table is Count. 
                | 
                |     Example:
                |         The following example removes the third drawing table in the drawing
                |         table collection of the active view of the active document, supposed to be a
                |         drawing document.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.DrawingTables.Remove(3)

        :param int i_index:
        :return: None
        """
        return self.drawing_tables.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingTable:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingTable(self.drawing_tables.Item(n + 1))

    def __iter__(self) -> Iterator[DrawingTable]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DrawingTables(name="{self.name}")'
