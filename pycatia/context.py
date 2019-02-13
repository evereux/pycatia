#! /usr/bin/python3.6

import os

from .catia_application import CATIAApplication
from .exceptions import CATIAApplicationException


class CATIADocHandler:

    def __init__(self, file_name):
        """
        A document handler to open a CATIA document and close upon exit.

        example:

        >>> catia_part = 'tests\\CF_catia_measurable_part.CATPart'
        >>> with CATIADocHandler(catia_part) as handler:
        >>>     document, documents, catia = handler

        Also see example_7.py

        :param file_name:

        """

        self.catia = CATIAApplication()
        self.documents = self.catia.documents()
        self.file_name = file_name

        if self.file_name and not os.path.isfile(self.file_name):
            raise CATIAApplicationException(f'Could not find file: {file_name}')

    def __enter__(self):
        self.catia = CATIAApplication()
        self.documents = self.catia.documents()
        self.documents.open(self.file_name)
        self.document = self.catia.document()

        handler = dict()
        handler['document'] = self.document
        handler['documents'] = self.documents
        handler['catia'] = self.catia

        return handler

    def __exit__(self, *args):
        self.document.close()
