#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.document import Document


class CatalogDocument(Document):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Document
                |                         CatalogDocument
                | 
                | Represents the Document object for catalog.
                | Role: A catalog document references data (documents: CATPart..., features, etc)
                | organized as a tree: the nodes are called chapters and the leaves are called
                | descriptions. Each description may reference a document (CATPart...) and
                | couples of keyword + value. The keywords are defined at the parent chapter
                | level.
                | A catalog may reference parametric Parts. In that case, the Part is associated
                | with a Design Table. A Design Table is a file (text file, Excel document) that
                | contains named columns and rows. Each row corresponds to a description, and
                | each column may correspond to a keyword.
                | Refer to CATIA V5 Documentation, Component Catalog Editor and to CAA V5
                | Encyclopedia, Document, Catalog.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.catalog_document = com_object

    def create_catalog_from_library(self,
                                    i_library_path: str,
                                    i_project_path: str,
                                    i_catalog_path: str,
                                    i_table_path: str,
                                    i_conv_format: int,
                                    i_batch_mode: int) -> 'CatalogDocument':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateCatalogFromLibrary(CATBSTR iLibraryPath,
                | CATBSTR iProjectPath,
                | CATBSTR iCatalogPath,
                | CATBSTR iTablePath,
                | short iConvFormat,
                | short iBatchMode)
                | 
                |     Creates a catalog from a V4 library.
                | 
                |     Parameters:
                | 
                |         iLibraryPath
                |             The V4 library path. 
                |         iProjectPath
                |             The V4 project path. 
                |         iCatalogPath
                |             The new catalog path. 
                |         iTablePath
                |             The mapping table path. 
                |         iConvFormat
                |             0: As Specification
                |             1: As Result 
                |         iBatchMode
                |             0: As Specification
                |             1: As Result 
                |         iBatchMode
                |             0: Create the V5 documents
                |             1: Simulate: the V5 documents are not created
                |             2: If the previous migration has failed, continue since this
                |             point.

        :param str i_library_path:
        :param str i_project_path:
        :param str i_catalog_path:
        :param str i_table_path:
        :param int i_conv_format:
        :param int i_batch_mode:
        :rtype: None
        """
        return CatalogDocument(
            self.catalog_document.CreateCatalogFromLibrary(
                i_library_path,
                i_project_path,
                i_catalog_path,
                i_table_path,
                i_conv_format,
                i_batch_mode).com_object)

    def create_catalog_from_csv(self, i_init_data: str, i_new_catalog: str) -> 'CatalogDocument':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateCatalogFromcsv(CATBSTR iInitData,
                | CATBSTR iNewCatalog)
                | 
                |     Creates a catalog from a csv file.
                |     Refer to CATIA V5 Documentation, Component Catalog Editor, Creating a
                |     Catalog in Batch Mode.
                | 
                |     Parameters:
                | 
                |         iInitData
                |             The csv (Comma Separated Values) file path. 
                |         iNewCatalog
                |             The new catalog path.
                | 
                |             Example:
                |                 This example creates a catalog from a csv
                |                 file.
                | 
                |                    InputFile = "E:\\users\\Catalogs\\BatchCatalog.csv"
                |                    OutputFile = "E:\\users\\Catalogs\\Catalog_Result.catalog"
                |                    Dim Catalog As Document
                |                    Set Catalog=CATIA.Documents.Add("CatalogDocument")
                |                    Catalog.CreateCatalogFromcsv InputFile,
                |                    OutputFile

        :param str i_init_data:
        :param str i_new_catalog:
        :return: None
        :rtype: CatalogDocument
        """
        return self.catalog_document.CreateCatalogFromcsv(i_init_data, i_new_catalog)

    def create_chapter_from_design_table(self, i_chapter_name: str, i_document_containing_dt: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateChapterFromDesignTable(CATBSTR iChapterName,
                | CATBSTR iDocumentContainingDT)
                | 
                |     Creates a chapter in the current catalog document where keywords correspond
                |     to parameters of the Design Table and add the descriptions corresponding to
                |     whole configurations of the Design Table.
                |     Refer to CATIA V5 Documentation, Component Catalog Editor, Creating a
                |     Catalog in Batch Mode.
                | 
                |     Parameters:
                | 
                |         iChapterName
                |             The name of the new chapter. 
                |         iDocumentContainingDT
                |             The path of the Design Table.
                | 
                |             Example:
                |                 This example creates a catalog and a chapter is added from a
                |                 Design Table.
                | 
                |                    Chapter = "NewChapter"
                |                    DTFile = "E:\\users\\Catalogs\\DesignTable.xls"
                |                    Dim Catalog As Document
                |                    Set Catalog=CATIA.Documents.Add("CatalogDocument")
                |                    Catalog.CreateChapterFromDesignTable Chapter,
                |                    DTFile

        :param str i_chapter_name:
        :param str i_document_containing_dt:
        :rtype: None
        """
        return self.catalog_document.CreateChapterFromDesignTable(i_chapter_name, i_document_containing_dt)

    def __repr__(self):
        return f'CatalogDocument(name="{ self.name }")'
