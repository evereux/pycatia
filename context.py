#! /usr/bin/python3.6

import os
import warnings

from .catia_application import CATIAApplication
from .exceptions import CATIAApplicationException


class CATIADocHandler:

    def __init__(self, file_name=None, new_document=None):
        """
        A context manager to open or create a CATIA document. The CATIA document will be closed upon exit.

        basic example::

        >>> catia_part = 'tests\\CF_catia_measurable_part.CATPart'
        >>> with CATIADocHandler(catia_part) as handler:
        >>>     # create the CATIA() object.
        >>>     catia = handler.catia
        >>>     # create the documents object.
        >>>     documents = handler.documents
        >>>     # create the document object.
        >>>     document = handler.document
        >>>     # do some stuff

        example to create new CATPart document::

        >>>
        >>> with CATIADocHandler(new_document='Part') as handler:
        >>>     # create the CATIA() object.
        >>>     catia = handler.catia
        >>>     # create the documents object.
        >>>     documents = handler.documents
        >>>     # create the document object.
        >>>     document = handler.document

        :param file_name: (optional) path filename to file
        :param new_document: (option) string 'Part', 'Product' or 'Drawing'.
        """

        self.catia = CATIAApplication()
        self.documents = self.catia.documents()
        self.file_name = file_name
        self.new_document = new_document

        if self.file_name and not os.path.isfile(self.file_name):
            raise CATIAApplicationException(f'Could not find file: {file_name}')

    def __enter__(self):
        self.catia = CATIAApplication()
        self.documents = self.catia.documents()
        self.document = None

        if self.file_name:
            self.documents.open(self.file_name)
            self.document = self.catia.document()
        elif self.new_document:
            self.documents.add(self.new_document)
            self.document = self.catia.document()

        return self

    def __exit__(self, *args):

        if self.document:
            self.document.close()
        else:
            warnings.warn('The document handler could not detect a document to close.')
