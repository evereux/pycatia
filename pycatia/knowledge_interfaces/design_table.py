#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import TYPE_CHECKING

from pycatia.knowledge_interfaces.relation import Relation

if TYPE_CHECKING:
    from pycatia.knowledge_interfaces.parameter import Parameter

class DesignTable(Relation):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.KnowledgeObject
                |                        KnowledgeInterfaces.KnowledgeActivateObject
                |                             KnowledgeInterfaces.Relation
                |                                 DesignTable
                | 
                | Represents the DesignTable object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.design_table = com_object

    @property
    def columns_nb(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ColumnsNb() As short (Read Only)
                | 
                |     Returns the nb of columns in the design table file.

        :rtype: int
        """

        return self.design_table.ColumnsNb

    @property
    def configuration(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Configuration() As short
                | 
                |     Returns or sets the current configuration. Legal values: 1 to
                |     ConfigurationsNb.

        :rtype: int
        """

        return self.design_table.Configuration

    @configuration.setter
    def configuration(self, value: int):
        """
        :param int value:
        """

        self.design_table.Configuration = value

    @property
    def configurations_nb(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ConfigurationsNb() As short (Read Only)
                | 
                |     Returns the number of design table configurations.

        :rtype: int
        """

        return self.design_table.ConfigurationsNb

    @property
    def copy_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property CopyMode() As boolean
                | 
                |     Returns or sets whether the data contained in the file must be included
                |     inside the CATIA model.

        :rtype: bool
        """

        return self.design_table.CopyMode

    @copy_mode.setter
    def copy_mode(self, value: bool):
        """
        :param bool value:
        """

        self.design_table.CopyMode = value

    @property
    def file_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FilePath() As CATBSTR
                | 
                |     Returns or sets the path of the design table (read/write property).

        :rtype: str
        """

        return self.design_table.FilePath

    @file_path.setter
    def file_path(self, value: str):
        """
        :param str value:
        """

        self.design_table.FilePath = value

    def add_association(self, i_parameter: 'Parameter', i_sheet_column: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddAssociation(Parameter iParameter,
                | CATBSTR iSheetColumn)
                | 
                |     Adds an association between a parameter iParameter and a column of the
                |     design table. This method does nothing if the column does not exist or if the
                |     type of the parameter isn t compliant with the column
                |     type.
                | 
                |     Parameters:
                | 
                |         iParameter
                |             The parameter. 
                |         iSheetColumn
                |             The name of the column to be associated with the
                |             parameter.

        :param Parameter i_parameter:
        :param str i_sheet_column:
        :rtype: None
        """
        return self.design_table.AddAssociation(i_parameter.com_object, i_sheet_column)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_association'
        # # vba_code = """
        # # Public Function add_association(design_table)
        # #     Dim iParameter (2)
        # #     design_table.AddAssociation iParameter
        # #     add_association = iParameter
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_new_row(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddNewRow()
                | 
                |     Adds a row in the design table source file. The new row is filled in with values of associated
                |     parameters. ##### Since V5R14 ##### If the file contains at least one empty row between two not
                |     empty rows, the behavior of this method is the same for Excel and Text files : => the new row
                |     containing the current parameters values replaces the first empty row found from the beginning of
                |     the file. RQ : before R14, for text files, the new row was appended at the end of the file. The
                |     empty rows were never filed by this way, so that the new row was not visible in Design Table
                |     dialog.
                | 
                |     Returns:
                |         S_OK if succeeded, E_FAIL else.

        :rtype: None
        """
        return self.design_table.AddNewRow()

    def cell_as_string(self, i_row: int, i_column: int) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CellAsString(short iRow,
                | short iColumn) As CATBSTR
                | 
                |     Returns the content of a specific cell.
                | 
                |     Parameters:
                | 
                |         iRow
                |             the index of the row where the cell is located. 
                |         iColumn
                |             the index of the column where the cell is located.

        :param int i_row:
        :param int i_column:
        :rtype: str
        """
        return self.design_table.CellAsString(i_row, i_column)

    def remove_association(self, i_sheet_column: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveAssociation(CATBSTR iSheetColumn)
                | 
                |     Removes an existing association. This method does nothing if the column isn
                |     t associated or if it doesn t exist.
                | 
                |     Parameters:
                | 
                |         iSheetColumn
                |             The name of an associated column.

        :param str i_sheet_column:
        :rtype: None
        """
        return self.design_table.RemoveAssociation(i_sheet_column)

    def synchronize(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Synchronize()
                | 
                |     Synchronizes the design table with its source file. If the file is managed
                |     in Enovia LCA, copies this file on local disk, and synchronizes design table
                |     content

        :rtype: None
        """
        return self.design_table.Synchronize()

    def __repr__(self):
        return f'DesignTable(name="{self.name}")'
