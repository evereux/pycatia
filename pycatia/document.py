#! /usr/bin/python3.6

import os
from pywintypes import com_error

from .exceptions import CATIAApplicationException
from .part import Part
from .product import Product


class Documents:

    def __init__(self, catia):
        """
        ###
        # A collection of all the Document objects currently managed by the application.
        # These documents belong to one of the following types: PartDocument, ProductDocument, and Drawing.

        :param catia: CATIA COM object
        """

        self.documents = catia.Documents

    def open(self, file_name):
        """
        ### FROM CAA V5 Visual Basic help ###
        # * Func Open( CATBSTR  iFileName) As Document
        #
        # Opens a document stored in a file. Reads a document stored in a file, displays it in a new window, adds the
        # document to the documents collection and the window to the windows collection, and makes both the document
        # and the window the active ones.
        #
        # Parameters:
        #   iFileName
        #       The name of the file containing the document
        #   Returns:
        #       The retrieved document
        # Example:
        # The following example opens the Doc document contained in the FileToOpen file.
        #   FileToOpen = "e:/users/psr/Parts/ThisIsANicePart.CATPart"
        #   Dim Doc As Document
        #   Set Doc = Documents.Open(FileToOpen)

        :param file_name: full path to catia file.
        :type file_name: str()
        :return:
        """

        if not os.path.isfile(file_name):
            raise FileNotFoundError(f'Could not find file {file_name}.')

        # get the full path to the file
        file_name = os.path.abspath(file_name)

        self.documents.Open(file_name)


class Document:

    def __init__(self, catia):
        """

        ### FROM CAA V5 Visual Basic help ###
        # The Document is the object which stores your pycatia data on disk. A document is either created
        # empty using the File->New command or using the Add method of the Documents collection, or opened
        # from a file using the File->Open command or using the Open method of the Documents collection.
        # CATIA provides access to four document types: the PartDocument, the ProductDocument, the
        # DrawingDocument and the AnalysisDocument. The Document abstract object gathers the properties and
        # methods common to all actual document types. When a document is created or opened, it is
        # automatically set as the active document and displayed in a window which automatically becomes
        # the active window. A document aggregates the current object or set of objects in the Selection
        # object, and Cameras, a camera collection.

        The CATIA Document object is accessible using either self.document.

        :param catia: CATIA COM object.
        :return:
        """

        try:
            self.document = catia.ActiveDocument
        except com_error:
            message = "Could not activate document."
            raise CATIAApplicationException(message)

    @property
    def name(self):
        """

        :return:
        """

        return self.document.Name

    @property
    def product(self):
        """
        :return: Product()
        """

        try:
            return Product(self.document.Product)
        except AttributeError:
            return None

    @property
    def part(self):
        """
        :return: Part()
        """

        try:
            return Part(self.document.Part)
        except AttributeError:
            return None

    @property
    def is_product(self):

        if self.product:
            return True
        return False

    @property
    def is_part(self):

        if not self.is_product:
            return True

        return True

    @property
    def is_saved(self):
        """ Returns true if document is saved.

        ### FROM CAA V5 Visual Basic help ###
        # Property Saved( ) As boolean (Read Only)
        #
        # Returns whether the document has been modified, and thus needs to be saved.
        # This happens when the document has changed since either its creation or its last save.
        # True if the document has not been changed: the document doesn't need to be saved.
        # False if the document has been changed: the document needs to be saved.
        # Example:
        # This example retrieves in HasChanged whether the Doc document needs to be saved.
        #  HasChanged = NOT Doc.Saved

        :return: True or False
        :type: Boolean()
        """

        if self.document.Saved():
            return True

        return False

    def activate(self):
        """ Activates the document

        ### FROM CAA V5 Visual Basic help ###
        # o Sub Activate( )
        #
        # Activates the document. Activating a document means that this document is the one on which the end user is
        # now working on. This document possibly reconfigures the menu bar and toolbars with its own commands if its
        # type is different from the type of the previous active document. The first window in the window collection
        # which contains this document becomes the active one.
        # Example:
        # This example activates the Doc document.
        #  Doc.Activate()
        :return:
        """

        self.document.Activate()

    def close(self):
        """Closes the current document.

        ### FROM CAA V5 Visual Basic help ###
        # Sub Close( )
        #
        # Closes the document. This closes all the windows displaying the document. If the document needs to be saved,
        # the end user is prompted whether to save the document, or to close it anyway.
        # Example:
        # This example closes the Doc document
        #  Doc.Close()

        :return:
        """

        self.document.Close()

    def save(self):
        """ Save the current document.

        ### FROM CAA V5 Visual Basic help ###
        # Sub Save( )
        #
        # Saves the document.
        # Example:
        # This example saves the Doc document.
        #  Doc.Save()

        :return: None
        """

        self.document.Save()

    def save_as(self, file_name):
        """Save the document to a new name.

        ### FROM CAA V5 Visual Basic help ###
        # Sub SaveAs( CATBSTR  fileName)
        #
        # Saves the document with another name.
        #   Parameters:
        #       fileName
        #           The name to assign to the document
        # Example:
        # This example saves the Doc document with the NewName name.
        #  Doc.SaveAs("NewName")

        :param file_name: full pathname to new file_name
        :return: None
        """

        file_name = os.path.abspath(file_name)
        if os.path.isfile(file_name):
            raise FileExistsError(f'File: {file_name} already exists.')
        self.document.SaveAs(file_name)

    @staticmethod
    def search_for_items(document, selection_objects):
        """

        # todo: This search is currently restricted to GSD objects only.

        Selection objects is a list of items to search for.
        Example: selection_objects = ['Point', 'Line']

        Example query string to search for all lines and points
        "('Generative Shape Design'.Point + 'Generative Shape Design'.Line),in"

        :param document:
        :param selection_objects: list():
        :return Selected Automation Object:
        """

        gsd_items = [
            'Point',
            'Line'
        ]

        query_string = str()
        # build query string

        for counter, item in enumerate(selection_objects):
            boolean = str()
            if counter > 0 and not counter == len(selection_objects):
                boolean = ' + '
            if item in gsd_items:
                query_string = f"{query_string}{boolean}'Generative Shape Design'.{item}"

        query_string = f"({query_string}),in"

        selection = document.document.Selection
        selection.Search(query_string)

        selected = list()
        for i in range(0, selection.Count):
            selected.append(selection.Item(i + 1).Value)

        return selected

    def __repr__(self):
        return f'Document object (name: {self.name})'
