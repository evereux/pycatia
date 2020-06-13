#! /usr/bin/python3.6

import os
import warnings

from pywintypes import com_error

from pycatia.exception_handling import CATIAApplicationException
from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.collection import Collection


class Documents(Collection):
    """
    The Documents object is used to access multiple open documents in the catia session.

    Usage::

        >>> from pycatia import catia
        >>> documents = catia.documents

    .. note::
        CAA V5 Visual Basic help

        A collection of all the Document objects currently managed by the application.
        These documents belong to one of the following types:

            PartDocument,
            ProductDocument,
            Drawing.
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Document)
        self.documents = com_object

    def add(self, document_type):
        """
        .. note::
            CATIA V5 Visual Basic Help

            Func Add( CATBSTR  docType) As Document

            Creates a Document object and adds it to the documents collection. This document becomes the active one,
            and a window is created to accommodate it which becomes the active window.

            | Parameters:
            |   docType
            | The type of the document to create, chosen among:
            |   Part
            |       For PartDocument
            |   Product
            |       For ProductDocument
            |   Drawing
            |       For Drawing
            |   Returns:
            |       The created document
            | Example:
            | The following example creates a PartDocument document in the collection retrieved in PartDoc.
            |   Dim PartDoc As Document
            |   Set PartDoc = Documents.Add("Part")

        :param document_type:
        :return:
        """

        document_types = ['Part', 'Product', 'Drawing']
        if document_type not in document_types:
            raise ValueError(f'Document type must be in [{document_types}]')

        self.logger.info(f'Creating a new "{document_type}".')

        return self.child_object(self.documents.Add(document_type))

    def count_types(self, file_type_list):
        """
        Returns the number of documents which presents special file extensions like:
            'catpart', 'catdrawing', 'catproduct', 'catmaterial', 'catalog', 'catfct'


        :param str (list) file_type_list: filetype(s) to count.
        :return: int()
        """

        items = self.get_item_names()

        if not type(file_type_list) == list:
            file_type_list = [elem.lower() for elem in [file_type_list]]
        else:
            file_type_list = [elem.lower() for elem in file_type_list]

        return len([True for name in items for typ in file_type_list if name.lower().find(typ) > 0])

    def new_from(self, file_name):
        """

        .. note::
            CAA V5 Visual Basic help

            Creates a new document from a document stored in a file. Role: Reads a document stored in a file and
            creates a new document containing the resulting data, adds the new document to the document collection,
            displays it in a new window, adds the window to the window collection and activates both the document and
            the window.

            | Parameters:
            |   The name of the file containing the document.
            | Returns:
            |   The created document.
            | Example:
            | The following example creates a new Doc document from the contents of the FileToRead file.
            |   FileToRead = "e:////users////psr////Parts////ThisIsANicePart.CATPart"
            |   Dim Doc As Document
            |   Set Doc = Documents.NewFrom(FileToRead)


        :param str file_name:
        :return:

        """

        if not os.path.isfile(file_name):
            raise FileNotFoundError(f'Could not find file {file_name}.')

        # get the full path to the file
        file_name = os.path.abspath(file_name)

        return self.documents.NewFrom(file_name)

    def item(self, index):
        """
        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(CATVariant iIndex) As Document
                |
                | Returns a document using its index or its name from the documents
                | collection.


                | Parameters:
                | iIndex
                |    The index or the name of the document to retrieve frm
                |    the collection of documents.
                |    As a numeric, this index is the rank of the document
                |    in the collection.
                |    The index of the first document in the collection is 1, and
                |    the index of the last document is Count.
                |    As a string, it is the name you assigned to the document using
                |    the
                |
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property.
                |    Returns:
                |   The retrieved document


                | Examples:
                |
                |
                | This example retrieves in ThisDoc the fifth document
                | in the collection and in ThatDoc the document
                | named MyDoc.
                |
                | Dim ThisDoc As Document
                | Set ThisDoc = Documents.Item(5)
                | Dim ThatDoc As Document
                | Set ThatDoc = Documents.Item("MyDoc")
                |

        :param int|str index:
        :return Document COM object:
        """

        return self.child_object(self.documents.Item(index))

    def num_open(self):
        """
        Returns the number of open documents.

        .. warning::

            The COM object can return the incorrect number of documents open. After a document is closed CATIA can keep
            the linked document `ABQMaterialPropertiesCatalog.CATfct` open.

        :return: int()
        """

        # for i in range(0, self.documents.Count):
        #     print(self.documents.Item(i + 1).Name)

        warning_string = (
            'The COM object can return the incorrect number of documents open. //n'
            'For example, after a CATPart document is closed CATIA can keep'
            'the linked document `ABQMaterialPropertiesCatalog.CATfct` loaded in the session.'
        )

        warnings.warn(warning_string)
        return self.documents.Count

    def open(self, file_name):
        """
        Open CATIA document `file_name` in current CATIA session.

        .. note::
            CAA V5 Visual Basic help

            Func Open( CATBSTR  iFileName) As Document

            Opens a document stored in a file. Reads a document stored in a file, displays it in a new window, adds the
            document to the documents collection and the window to the windows collection, and makes both the document
            and the window the active ones.

            | Parameters:
            |   iFileName:
            |       The name of the file containing the document
            |   Returns:
            |       The retrieved document

            | Example:
            | The following example opens the Doc document contained in the FileToOpen file.
            | FileToOpen = "e:/users/psr/Parts/ThisIsANicePart.CATPart"
            | Dim Doc As Document
            | Set Doc = Documents.Open(FileToOpen)

        :param str file_name: full path to catia file.
        """

        if not os.path.isfile(file_name):
            raise FileNotFoundError(f'Could not find file {file_name}.')

        # get the full path to the file
        file_name = os.path.abspath(file_name)

        try:
            self.logger.info(f'Opening document "{file_name}".')
            self.documents.Open(file_name)
        except com_error:
            raise CATIAApplicationException(
                f'Could not open document "{file_name}". '
                'Check file type and ensure the version of CATIA it was created with is compatible.')

    def read(self, file_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | Read
                | o Func Read(    CATBSTR    iFileName) As Document
                |
                | Reads a document stored in a file. This method has to be used only for
                | Browse purpose, for instance to retrieve Product properties. Be
                | careful, it doesn't open any editor (no visualization, no undo/redo
                | capabilities...) As soon as you want to modify the V5 document, you
                | have to use  the VB Open method collection. If this solution is not
                | satisfactory because it opens an editor for every document, you have
                | to move to C++ and use the CAA methods CATDocumentServices::Open and
                | CATDocumentServices::SaveAs with the same file name as the initial
                | one.
                |
                | Parameters:
                | iFileName
                |    The name of the file containing the document
                |
                |
                |  Returns:
                |   The retrieved document
                |
                | Examples:
                |
                |
                | The following example reads the Doc document
                | contained in the FileToOpen file.
                |
                | FileToOpen = "e://users//psr//Parts//ThisIsANicePart.CATPart"
                | Dim Doc As Document
                | Set Doc = Documents.Read(FileToOpen)
                |
                |
                |
        """
        return self.documents.Read(file_name)

    def __repr__(self):
        return f'Documents(name="{self.name}")'
