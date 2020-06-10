#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .relation import Relation


class DesignTable(Relation):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the DesignTable object.

    """

    def __init__(self, design_table):
        super().__init__(design_table)
        self.design_table = design_table

    @property
    def columns_nb(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ColumnsNb
                | o Property ColumnsNb() As short
                |
                | Returns the nb of columns in the design table file.


                | Parameters:


        """
        return self.design_table.ColumnsNb

    @property
    def configuration(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Configuration
                | o Property Configuration() As short
                |
                | Returns or sets the current configuration.  Legal values:  1 to
                | ConfigurationsNb.


                | Parameters:


        """
        return self.design_table.Configuration

    @property
    def configurations_nb(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ConfigurationsNb
                | o Property ConfigurationsNb() As short
                |
                | Returns the number of design table configurations.


                | Parameters:


        """
        return self.design_table.ConfigurationsNb

    @property
    def copy_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CopyMode
                | o Property CopyMode() As boolean
                |
                | Returns or sets whether the data contained in the file must be
                | included inside the CATIA model.


                | Parameters:


        """
        return self.design_table.CopyMode

    @property
    def file_path(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FilePath
                | o Property FilePath() As CATBSTR
                |
                | Returns or sets the path of the design table (read/write property).


                | Parameters:


        """
        return self.design_table.FilePath

    def add_association(self, i_parameter, i_sheet_column):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddAssociation
                | o Sub AddAssociation(    Parameter    iParameter,
                |                          CATBSTR    iSheetColumn)
                |
                | Adds an association between a parameter iParameter and a  column of
                | the design table.    This method does nothing if the column does not
                | exist or if  the type of the parameter isn t compliant with the column
                | type.


                | Parameters:
                | iParameter
                |  The parameter.
                |
                |  iSheetColumn
                |  The name of the column to be associated with the parameter.


        """
        return self.design_table.AddAssociation(i_parameter, i_sheet_column)

    def add_new_row(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewRow
                | o Sub AddNewRow()
                |
                | Adds a row in the design table source file.  The new row is filled in
                | with values of associated parameters. ##### Since V5R14 #####  If the
                | file contains at least one empty row between two not empty rows, the
                | behavior of this method is the same for Excel and Text files : => the
                | new row containing the current parameters values replaces the first
                | empty row found from the beginning of the file. RQ : before R14, for
                | text files, the new row was appended at the end of the file.      The
                | empty rows were never filed by this way, so that the new row was not
                | visible in Design Table dialog. ######################  Returns:  S_OK
                | if succeeded, E_FAIL else.


                | Parameters:


        """
        return self.design_table.AddNewRow()

    def cell_as_string(self, i_row, i_column):
        """
        .. note::
            CAA V5 Visual Basic help

                | CellAsString
                | o Func CellAsString(    short    iRow,
                |                         short    iColumn) As CATBSTR
                |
                | Returns the content of a specific cell.


                | Parameters:
                | iRow
                |  the index of the row where the cell is located.
                |  iColumn
                |  the index of the column where the cell is located.


        """
        return self.design_table.CellAsString(i_row, i_column)

    def remove_association(self, i_sheet_column):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAssociation
                | o Sub RemoveAssociation(    CATBSTR    iSheetColumn)
                |
                | Removes an existing association. This method does nothing if the
                | column isn t associated or  if it doesn t exist.


                | Parameters:
                | iSheetColumn
                |  The name of an associated column.


        """
        return self.design_table.RemoveAssociation(i_sheet_column)

    def synchronize(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Synchronize
                | o Sub Synchronize()
                |
                | Synchronizes the design table with its source file. If the file is
                | managed in Enovia LCA, copies this file on local disk, and
                | synchronizes design table content.
        """
        return self.design_table.Synchronize()

    def __repr__(self):
        return f'DesignTable()'
