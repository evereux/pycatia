#! /usr/bin/python3.6

import os

import warnings


class Documents:
    """
    The Documents object is used to access multiple open documents in the catia session.

    Usage::

        >>> from pycatia.base_interfaces import CATIAApplication
        >>> from pycatia.base_interfaces import Document
        >>> catia = CATIAApplication()
        >>> documents = Document(catia.catia)

    .. note::
        CAA V5 Visual Basic help

        A collection of all the Document objects currently managed by the application.
        These documents belong to one of the following types:

            PartDocument,
            ProductDocument,
            Drawing.


    :param catia: CATIA COM object

    """

    def __init__(self, catia):

        self.documents = catia.Documents

    def add(self, document_type):
        """
        .. note::
            CATIA V5 Visual Basic Help

            Func Add( CATBSTR  docType) As Document

            Creates a Document object and adds it to the documents collection. This document becomes the active one,
            and a window is created to accomodate it which becomes the active window.

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

        self.documents.Add(document_type)

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
            |   FileToRead = "e:\\users\\psr\\Parts\\ThisIsANicePart.CATPart"
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
        self.documents.Open(file_name)

    def item(self, index):
        return self.documents.Item(index)

    def get_documents(self):

        items = []

        for index in range(1, self.documents.count):
            items.append(self.documents.Item(index))

        return items

    def get_documents_name(self):

        names = []

        for index in range(1, self.documents.count + 1):
            names.append(self.documents.Item(index).Name)

        return names

    def count(self, file_typ_list):
        """
        Returns the number of documents which presents special file extensions like:
            'catpart', 'catdrawing', 'catproduct', 'catmaterial', 'catalog', 'catfct'


        :param str (list) file_typ_list: filetyp(es) to count.
        :return: int()
        """

        items = self.get_documents_name()

        if not type(file_typ_list) == list:
            file_typ_list = [elem.lower() for elem in [file_typ_list]]
        else:
            file_typ_list = [elem.lower() for elem in file_typ_list]

        return len([True for name in items for typ in file_typ_list if name.lower().find(typ) > 0])
        
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
            'The COM object can return the incorrect number of documents open. \n'
            'For example, after a CATPart document is closed CATIA can keep'
            'the linked document `ABQMaterialPropertiesCatalog.CATfct` loaded in the session.'
        )

        warnings.warn(warning_string)
        return self.documents.Count
