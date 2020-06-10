#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.drafting_interfaces.drawing_leaders import DrawingLeaders
from pycatia.system_interfaces.any_object import AnyObject


class DrawingTable(AnyObject):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingTable
                | 
                | Represents a drawing table in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_table = com_object

    @property
    def anchor_point(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property AnchorPoint() As CatTablePosition
                | 
                |     Returns or sets the anchor point of a drawing table.
                | 
                |     Parameters:
                | 
                |         iMode
                |             The invert mode to apply
                | 
                |             Example:
                |                 This example sets the anchor point of the drawing table MyTable
                |                 to bottom left.
                | 
                |                  MyTable.AnchorPoint = CatTableBottomLeft

        :return: enum cat_table_position
        """

        return self.drawing_table.AnchorPoint

    @anchor_point.setter
    def anchor_point(self, value):
        """
        :param enum cat_table_position value:
        """

        self.drawing_table.AnchorPoint = value

    @property
    def angle(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Angle() As double
                | 
                |     Returns or sets the angle orientation of a drawing table.
                | 
                |     Example:
                |         This example sets the orientation of the table MyTable to
                |         vertical.
                | 
                |          PI = 3.1415926535
                |          X = MyTable.Angle = PI/2

        :return: float
        """

        return self.drawing_table.Angle

    @angle.setter
    def angle(self, value):
        """
        :param float value:
        """

        self.drawing_table.Angle = value

    @property
    def compute_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ComputeMode() As CatTableComputeMode
                | 
                |     Returns or sets the compute mode of a drawing table. If the compute mode is
                |     set to OFF, no display of the modifications applied to a table will be
                |     computed. This allows to save much time when executing a macro. To displayed
                |     the table, set the compute mode back to ON.
                | 
                |     Example:
                |         This example sets the compute mode of the drawing table MyTable to
                |         OFF.
                | 
                |          MyTable.ComputeMode = CatTableOFF

        :return: enum cat_table_compute_mode
        """

        return self.drawing_table.ComputeMode

    @compute_mode.setter
    def compute_mode(self, value):
        """
        :param enum cat_table_compute_mode value:
        """

        self.drawing_table.ComputeMode = value

    @property
    def leaders(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Leaders() As DrawingLeaders (Read Only)
                | 
                |     Returns the drawing leader collection of the drawing
                |     table.
                | 
                |     Example:
                |         This example retrieves in LeaderCollection the collection of leaders of
                |         the MyTable drawing table.
                | 
                |          Dim LeaderCollection As DrawingLeaders
                |          Set LeaderCollection = MyTable.Leaders

        :return: DrawingLeaders
        """

        return DrawingLeaders(self.drawing_table.Leaders)

    @property
    def number_of_columns(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property NumberOfColumns() As long (Read Only)
                | 
                |     Returns the number of columns of a drawing table.
                | 
                |     Example:
                |         This example returns the number of columns of the drawing table
                |         MyTable.
                | 
                |          oNbCol = MyTable.NumberOfColumns

        :return: int
        """

        return self.drawing_table.NumberOfColumns

    @property
    def number_of_rows(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property NumberOfRows() As long (Read Only)
                | 
                |     Returns the number of rows of a drawing table.
                | 
                |     Example:
                |         This example returns the number of rows of the drawing table
                |         MyTable.
                | 
                |          oNbRow = MyTable.NumberOfRows

        :return: int
        """

        return self.drawing_table.NumberOfRows

    @property
    def x(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property x() As double
                | 
                |     Returns or sets the x coordinate of the table. It is expressed with respect
                |     to the current view coordinate system. This coordinate, like any length, is
                |     measured in mm.
                | 
                |     Example:
                |         This example retrieves the x coordinate of the table MyTable drawing
                |         table.
                | 
                |          X = MyTable.x

        :return: float
        """

        return self.drawing_table.x

    @x.setter
    def x(self, value):
        """
        :param float value:
        """

        self.drawing_table.x = value

    @property
    def y(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property y() As double
                | 
                |     Returns or sets the y coordinate of the table. It is expressed with respect
                |     to the view coordinate system. This coordinate, like any length, is measured in
                |     mm.
                | 
                |     Example:
                |         This example sets the y coordinate of the table MyTable drawing table
                |         to 5 inches. You need first to convert the 5 inches into
                |         mm.
                | 
                |          NewYCoordinate = 100
                |          MyTable.y =  NewYCoordinate

        :return: float
        """

        return self.drawing_table.y

    @y.setter
    def y(self, value):
        """
        :param float value:
        """

        self.drawing_table.y = value

    def add_column(self, i_col=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub AddColumn(long iCol)
                | 
                |     Adds a column before the indicated column.
                | 
                |     Parameters:
                | 
                |         iCol
                |             The column before which the new column will be
                |             inserted
                | 
                |             Example:
                |                 This example adds a column after the last one of the drawing
                |                 table MyTable.
                | 
                |                  iCol = 0
                |                  MyTable.AddColumn iCol

        :param int i_col:
        :return: None
        """
        return self.drawing_table.AddColumn(i_col)

    def add_row(self, i_row=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub AddRow(long iRow)
                | 
                |     Adds a row before the indicated row.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The row before which the new row will be inserted
                | 
                |             Example:
                |                 This example adds a row beetween the first row and the second
                |                 row of the drawing table MyTable.
                | 
                |                  iRow = 2
                |                  MyTable.AddRow iRow

        :param int i_row:
        :return: None
        """
        return self.drawing_table.AddRow(i_row)

    def get_cell_alignment(self, i_row=None, i_col=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetCellAlignment(long iRow,
                | long iCol) As CatTablePosition
                | 
                |     Retrieves the alignment of the pointed cell of a drawing
                |     table.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The cell row 
                |         iCol
                |             The cell column 
                |         oAlign
                |             The alignment type of the cell
                | 
                |             Example:
                |                 This example retrieves the alignment of the cell (1,3) of the
                |                 table MyTable.
                | 
                |                  iRow = 1
                |                  iCol = 3
                |                  oAlign = MyTable.GetCellAlignment(iRow, iCol)

        :param int i_row:
        :param int i_col:
        :return: None
        """
        return self.drawing_table.GetCellAlignment(i_row, i_col)

    def get_cell_border_type(self, i_row=None, i_col=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetCellBorderType(long iRow,
                | long iCol) As CatTableBorderType
                | 
                |     Retrieves the drawing text contained in the cell of a drawing
                |     table.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The cell row 
                |         iCol
                |             The cell column 
                |         oType
                |             The type of the cell border
                | 
                |             Example:
                |                 This example retrieves the border type of the cell (1, 3) of
                |                 the drawing table MyTable.
                | 
                |                  iRow = 1
                |                  iCol = 3
                |                  oType = MyTable.GetCellBorderType(iRow, iCol)
                |                  !!!! WARNING  oType is not defined as the enum does but as it
                |                  is documented in the SetCellBorderType method
                |                   if oType == 15 it means border is set to left, top, right and
                |                   bottom. 
                |                   if oType == 8  it means border is set to bottom.

        :param int i_row:
        :param int i_col:
        :return: None
        """
        return self.drawing_table.GetCellBorderType(i_row, i_col)

    def get_cell_name(self, i_row=None, i_col=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetCellName(long iRow,
                | long iCol) As CATBSTR
                | 
                |     Returns the name of a table cell.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The cell row 
                |         iCol
                |             The cell column 
                |         oName
                |             The cell name
                | 
                |             Example:
                |                 This example returns the name of the cell (1,2) of the table
                |                 MyTable.
                | 
                |                  iRow = 1
                |                  iCol = 2
                |                  oName = MyTable.GetCellName(iRow, iCol)

        :param int i_row:
        :param int i_col:
        :return: None
        """
        return self.drawing_table.GetCellName(i_row, i_col)

    def get_cell_object(self, i_row=None, i_col=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetCellObject(long iRow,
                | long iCol) As DrawingText
                | 
                |     Retrieves the object contained in the cell of a drawing
                |     table.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The cell row 
                |         iCol
                |             The cell column 
                |         oText
                |             The object contained in the cell : this object only supports font properties, color, line spacing, Super/Sub script. Do not use position and/or orientation properties on this object, it is useless.
                | 
                |             Example:
                |                 This example retrieves the drawing text MyText of the cell
                |                 (1,3) of the table MyTable.
                | 
                |                  iRow = 1
                |                  iCol = 3
                |                  Set MyText = MyTable.GetCellObject(iRow, iCol)

        :param int i_row:
        :param int i_col:
        :return: None
        """
        return self.drawing_table.GetCellObject(i_row, i_col)

    def get_cell_string(self, i_row=None, i_col=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetCellString(long iRow,
                | long iCol) As CATBSTR
                | 
                |     Returns the string contained in the cell of a drawing
                |     table.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The cell row 
                |         iCol
                |             The cell column 
                |         oString
                |             The string contained in the cell
                | 
                |             Example:
                |                 This example returns the string contained in the cell (1,4) of
                |                 the table MyTable.
                | 
                |                  iRow = 1
                |                  iCol = 4
                |                  oString = MyTable.GetCellString(iRow, iCol)

        :param int i_row:
        :param int i_col:
        :return: None
        """
        return self.drawing_table.GetCellString(i_row, i_col)

    def get_cells_merge(self, o_list_of_merge_cells=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetCellsMerge(CATSafeArrayVariant oListOfMergeCells)
                | 
                |     Returns the merge cells.
                | 
                |     Parameters:
                | 
                |         oListOfMergeCells
                |             @param oListOfMergeCells List of merge cells.
                | 
                |             Example:
                |                 This example returns the merge cells of the drawing table
                |                 MyTable.
                | 
                |                  nbrow = MyTable.NumberOfRows
                |                  nbcol = MyTable.NumberOfColumns
                |                  sizetab = nbrow*nbcol
                |                  ReDim infoMerge (sizetab-1)
                |                  MyTable.GetCellsMerge(oListOfmergeCells)

        :param tuple o_list_of_merge_cells:
        :return: None
        """
        return self.drawing_table.GetCellsMerge(o_list_of_merge_cells)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_cells_merge'
        # # vba_code = """
        # # Public Function get_cells_merge(drawing_table)
        # #     Dim oListOfMergeCells (2)
        # #     drawing_table.GetCellsMerge oListOfMergeCells
        # #     get_cells_merge = oListOfMergeCells
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_column_size(self, i_col=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetColumnSize(long iCol) As double
                | 
                |     Returns the width of a column of a drawing table.
                | 
                |     Parameters:
                | 
                |         iCol
                |             The cell column 
                |         oColSize
                |             The cell width in mm. It corresponds to the size of the widest cell
                |             of the column or at least the size set with
                |             CATIADrawingTable::SetColumnSize.
                | 
                |             Example:
                |                 This example returns the width of the column (1) of the drawing
                |                 table MyTable.
                | 
                |                  iCol = 1
                |                  oColSize = MyTable.GetColumnSize(iCol)

        :param int i_col:
        :return: float
        """
        return float(self.drawing_table.GetColumnSize(i_col))

    def get_merge_infos(self, i_row=None, i_col=None, o_first_row=None, o_first_col=None, o_nb_row=None, o_nb_col=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetMergeInfos(long iRow,
                | long iCol,
                | long oFirstRow,
                | long oFirstCol,
                | long oNbRow,
                | long oNbCol)
                | 
                |     Returns informations about a group of merge cells from a
                |     cell.
                | 
                |     Parameters:
                | 
                |         iRow
                |             @param iCol cell of merge 
                |         iFirstRow
                |             Row of the first cell of the group Column of the first cell of the
                |             group 
                |         iNbRowMerge
                |             Number of rows of the group 
                |         iNbColMerge
                |             Number of columns of the group
                | 
                |             Example:
                |                 This example returns informations of a group of merge cells
                |                 from cell (2, 3) of the drawing table MyTable.
                | 
                |                  MyTable.GetMergeInfos 2, 3, oFirstRow, oFirstCol, oNbRow,
                |                  oNbCol

        :param int i_row:
        :param int i_col:
        :param int o_first_row:
        :param int o_first_col:
        :param int o_nb_row:
        :param int o_nb_col:
        :return: None
        """
        return self.drawing_table.GetMergeInfos(i_row, i_col, o_first_row, o_first_col, o_nb_row, o_nb_col)

    def get_row_size(self, i_row=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetRowSize(long iRow) As double
                | 
                |     Returns the height of a row of a drawing table.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The cell row 
                |         oRowSize
                |             The cell height in mm. It corresponds to the size of the highest
                |             cell of the row or at least the size set with
                |             CATIADrawingTable::SetRowsize.
                | 
                |             Example:
                |                 This example returns the height of the row (1) of the drawing
                |                 table MyTable.
                | 
                |                  iRow = 1
                |                  oRowSize = MyTable.GetRowSize(iRow)

        :param int i_row:
        :return: float
        """
        return float(self.drawing_table.GetRowSize(i_row))

    def invert_mode(self, i_mode=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub InvertMode(CatTableInvertMode iMode)
                | 
                |     Sets a mode of table inversion.
                | 
                |     Example:
                |         This example swaps the columns of the drawing table
                |         MyTable.
                | 
                |          MyTable.InvertMode CatInvertColumn

        :param CatTableInvertMode i_mode:
        :return: None
        """
        return self.drawing_table.InvertMode(i_mode)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'invert_mode'
        # # vba_code = """
        # # Public Function invert_mode(drawing_table)
        # #     Dim iMode (2)
        # #     drawing_table.InvertMode iMode
        # #     invert_mode = iMode
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def merge_cells(self, i_first_row=None, i_first_col=None, i_nb_row_merge=None, i_nb_col_merge=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub MergeCells(long iFirstRow,
                | long iFirstCol,
                | long iNbRowMerge,
                | long iNbColMerge)
                | 
                |     Merges a group of cells.
                | 
                |     Parameters:
                | 
                |         iFirstRow
                |             @param iFirstCol First cell of merge 
                |         iNbRowMerge
                |             Number of rows to merge 
                |         iNbColMerge
                |             Number of columns to merge
                | 
                |             Example:
                |                 This example merges cells from cell (2, 3) to cell (4, 5) of
                |                 the drawing table MyTable.
                | 
                |                  MyTable.MergeCells 2, 3, 3, 3

        :param int i_first_row:
        :param int i_first_col:
        :param int i_nb_row_merge:
        :param int i_nb_col_merge:
        :return: None
        """
        return self.drawing_table.MergeCells(i_first_row, i_first_col, i_nb_row_merge, i_nb_col_merge)

    def move(self, i_delta_x=None, i_delta_y=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub Move(double iDeltaX,
                | double iDeltaY)
                | 
                |     Moves the table relatively to its original position.
                | 
                |     Parameters:
                | 
                |         iDeltaX
                |             The X deviation 
                |         ideltaY
                |             The Y deviation
                | 
                |             Example:
                |                 This example moves the table MyTable to 20mm in
                |                 X.
                | 
                |                  DeltaX = 20.0
                |                  DeltaY =  0.0
                |                  MyTable.Move DeltaX, DeltaY

        :param float i_delta_x:
        :param float i_delta_y:
        :return: None
        """
        return self.drawing_table.Move(i_delta_x, i_delta_y)

    def remove_column(self, i_col=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RemoveColumn(long iCol)
                | 
                |     Removes the indicated column.
                | 
                |     Parameters:
                | 
                |         iCol
                |             The column to remove
                | 
                |             Example:
                |                 This example removes the first column of the drawing table
                |                 MyTable.
                | 
                |                  iCol = 1
                |                  MyTable.RemoveColumn iCol

        :param int i_col:
        :return: None
        """
        return self.drawing_table.RemoveColumn(i_col)

    def remove_row(self, i_row=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RemoveRow(long iRow)
                | 
                |     Removes the indicated row.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The row to remove
                | 
                |             Example:
                |                 This example removes the third row of the drawing table
                |                 MyTable.
                | 
                |                  iRow = 3
                |                  MyTable.RemoveRow iRow

        :param int i_row:
        :return: None
        """
        return self.drawing_table.RemoveRow(i_row)

    def rotate(self, i_delta_angle=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub Rotate(double iDeltaAngle)
                | 
                |     Rotates the table relatively to its original position.
                | 
                |     Parameters:
                | 
                |         iDeltaAngle
                |             The angle of rotation from the current position
                | 
                |             Example:
                |                 This example rotates the table MyTable to 45
                |                 degrees.
                | 
                |                  PI = 3.1415926535
                |                  MyTable.Rotate PI/4

        :param float i_delta_angle:
        :return: None
        """
        return self.drawing_table.Rotate(i_delta_angle)

    def set_cell_alignment(self, i_row=None, i_col=None, i_align=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetCellAlignment(long iRow,
                | long iCol,
                | CatTablePosition iAlign)
                | 
                |     Sets the pointed cell alignment of a drawing table.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The cell row 
                |         iCol
                |             The cell column 
                |         iAlign
                |             The type of alignment to be applied
                | 
                |             Example:
                |                 This example sets the cell (3,2) alignment of the table MyTable
                |                 to bottom left.
                | 
                |                  iRow = 3
                |                  iCol = 2
                |                  MyTable.SetCellAlignment iRow, iCol,
                |                  CatTableBottomLeft

        :param int i_row:
        :param int i_col:
        :param CatTablePosition i_align:
        :return: None
        """
        return self.drawing_table.SetCellAlignment(i_row, i_col, i_align)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_cell_alignment'
        # # vba_code = """
        # # Public Function set_cell_alignment(drawing_table)
        # #     Dim iRow (2)
        # #     drawing_table.SetCellAlignment iRow
        # #     set_cell_alignment = iRow
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_cell_border_type(self, i_row=None, i_col=None, i_type=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetCellBorderType(long iRow,
                | long iCol,
                | long iType)
                | 
                |     Sets the pointed cell border type of a drawing table.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The cell row 
                |         iCol
                |             The cell column 
                |         iType
                |             The type of border to be applied
                | 
                |                     ----- 2 ------         --------------         
                |                     --------------
                |                     |             |        |\            |         |          
                |                     |             |        |/ |                
                |                     |             |        |
                |                     |             |        |  \          |         |         / 
                |                     |             |        |  |        
                |                     1             4        |     \ 16    |         |    32 /   
                |                     |        
                |                     |             |        |        \    |         |   /       
                |                     |             |        |        |        
                |                     |             |        |          \  |         | /         
                |                     |             |        |          |         
                |                     ----- 8 ------         --------------         
                |                     --------------  
                |              
                | 
                |             Example:
                |                 This example sets the cell (3,2) border type of the table
                |                 MyTable to right and left. (1+4)
                | 
                |                  iRow = 3
                |                  iCol = 2
                |                  MyTable.SetCellBorderType iRow, iCol, 5
                |                  
                | 
                |             Example:
                |                 This example sets the cell (1,1) border type of the table MyTable to all border out line (left, top, right and bottom). (1+2+4+8 = 15)
                | 
                |                  iRow = 3
                |                  iCol = 2
                |                  MyTable.SetCellBorderType iRow, iCol, 15

        :param int i_row:
        :param int i_col:
        :param int i_type:
        :return: None
        """
        return self.drawing_table.SetCellBorderType(i_row, i_col, i_type)

    def set_cell_name(self, i_row=None, i_col=None, i_name=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetCellName(long iRow,
                | long iCol,
                | CATBSTR iName)
                | 
                |     Sets the name of a table cell.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The cell row 
                |         iCol
                |             The cell column 
                |         iName
                |             The cell name
                | 
                |             Example:
                |                 This example sets the name of the cell (1,2) of the table
                |                 MyTable to "Cell 2".
                | 
                |                  iRow = 1
                |                  iCol = 2
                |                  iName = "Cell 2"
                |                  MyTable.SetCellName iRow, iCol, iName

        :param int i_row:
        :param int i_col:
        :param str i_name:
        :return: None
        """
        return self.drawing_table.SetCellName(i_row, i_col, i_name)

    def set_cell_object(self, i_row=None, i_col=None, i_text=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetCellObject(long iRow,
                | long iCol,
                | DrawingText iText)
                | 
                |     Sets an object in a cell of a drawing table.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The cell row 
                |         iCol
                |             The cell column 
                |         iText
                |             The Drawing Text to set in the cell
                | 
                |             Example:
                |                 This example puts the drawing text iText in the cell (1,3) of
                |                 the table MyTable.
                | 
                |                  iRow = 1
                |                  iCol = 3
                |                  MyTable.SetCellObject iRow, iCol, iText

        :param int i_row:
        :param int i_col:
        :param DrawingText i_text:
        :return: None
        """
        return self.drawing_table.SetCellObject(i_row, i_col, i_text)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_cell_object'
        # # vba_code = """
        # # Public Function set_cell_object(drawing_table)
        # #     Dim iRow (2)
        # #     drawing_table.SetCellObject iRow
        # #     set_cell_object = iRow
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_cell_string(self, i_row=None, i_col=None, i_string=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetCellString(long iRow,
                | long iCol,
                | CATBSTR iString)
                | 
                |     Fills in a table cell with a string.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The cell row 
                |         iCol
                |             The cell column 
                |         iString
                |             The Text to be set
                | 
                |             Example:
                |                 This example fills in the cell (3,2) of the table MyTable with
                |                 "Title".
                | 
                |                  iRow = 3
                |                  iCol = 2
                |                  iString = "Title"
                |                  MyTable.SetCellString iRow, iCol, iString

        :param int i_row:
        :param int i_col:
        :param str i_string:
        :return: None
        """
        return self.drawing_table.SetCellString(i_row, i_col, i_string)

    def set_column_size(self, i_col=None, i_col_size=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetColumnSize(long iCol,
                | double iColSize)
                | 
                |     Sets the width of a column of a drawing table.
                | 
                |     Parameters:
                | 
                |         iCol
                |             The cell column 
                |         iColSize
                |             The cell width in mm. If 0, the width is automatic (corresponds to
                |             the size of the widest cell of the column).
                | 
                |             Example:
                |                 This example sets the width of the column (1) of the drawing
                |                 table MyTable to 20.
                | 
                |                  iCol = 1
                |                  iColSize = 20
                |                  MyTable.SetColumnSize iCol, iColSize

        :param int i_col:
        :param float i_col_size:
        :return: None
        """
        return self.drawing_table.SetColumnSize(i_col, i_col_size)

    def set_row_size(self, i_row=None, i_row_size=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetRowSize(long iRow,
                | double iRowSize)
                | 
                |     Sets the height of a row of a drawing table.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The cell row 
                |         iRowSize
                |             The cell height in mm. If 0, the height is automatic (corresponds
                |             to the size of the highest cell of the row).
                | 
                |             Example:
                |                 This example sets the height of the row (1) of the drawing
                |                 table MyTable to 20.
                | 
                |                  iRow = 1
                |                  iRowSize = 20
                |                  MyTable.SetRowSize iRow, iRowSize

        :param int i_row:
        :param float i_row_size:
        :return: None
        """
        return self.drawing_table.SetRowSize(i_row, i_row_size)

    def un_merge_cells(self, i_row=None, i_col=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub UnMergeCells(long iRow,
                | long iCol)
                | 
                |     Unmerges a group of cells.
                | 
                |     Parameters:
                | 
                |         iRow
                |             @param iCol A cell of a merge
                | 
                |             Example:
                |                 This example unmerges a group of cells of the drawing table
                |                 MyTable from the cell (3, 5).
                | 
                |                  MyTable.UnMergeCells 3, 5

        :param int i_row:
        :param int i_col:
        :return: None
        """
        return self.drawing_table.UnMergeCells(i_row, i_col)

    def __repr__(self):
        return f'DrawingTable(name="{ self.name }")'
