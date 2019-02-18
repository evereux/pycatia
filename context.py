#! /usr/bin/python3.6

import os
import warnings

from .catia_application import CATIAApplication
from .exceptions import CATIAApplicationException


class CATIADocHandler:

    def __init__(self, file_name=None, new_document=False):
        """
        A document handler to open a CATIA document and close upon exit.

        example:

        >>> catia_part = 'tests\\CF_catia_measurable_part.CATPart'
        >>> with CATIADocHandler(catia_part) as handler:
        >>>     document, documents, catia = handler

        New documents can also be created. new_document must be a string contraining: `Product` or `Part` or
        `Drawing`


        Also see example_7.py

        :param file_name:
        :param new_document:
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
