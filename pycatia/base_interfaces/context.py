#! /usr/bin/python3.9

import os
from pathlib import Path
from typing import Union

from pycatia.base_interfaces.base_application import catia_application as catia
from pycatia.exception_handling.exceptions import CATIAApplicationException


class CATIADocHandler:
    """
    A context manager to open or create a CATIA document.

    .. warning::
        The CATIA document will be closed (and not automatically
        saved) upon exit.

    Only file_name __or__ new_document are required as one document is handled at a time.

    :Example - Open a CATPart:

        >>> from pycatia.base_interfaces.context import CATIADocHandler
        >>> catia_part = 'tests//CF_catia_measurable_part.CATPart'
        >>> with CATIADocHandler(catia_part) as handler:
        >>>     # create the documents object.
        >>>     documents = handler.documents
        >>>     # create the document object.
        >>>     document = handler.document
        >>>     # do some stuff
        >>>     # save document if you need to
        >>>     document.save()

    :Example - Create a new CATPart:

        >>> from pycatia.base_interfaces.context import CATIADocHandler
        >>> with CATIADocHandler(new_document='Part') as handler:
        >>>     # create the CATIA() object.
        >>>     catia = handler.application
        >>>     # create the documents object.
        >>>     documents = handler.documents
        >>>     # create the document object.
        >>>     document = handler.document
        >>>     # save document!
        >>>     document.save()

    :param str or Path file_name: (optional) path filename to file
    :param str new_document: (optional) 'Part', 'Product' or 'Drawing'.
    """

    def __init__(self, file_name: Union[Path, None] = None, new_document: Union[str, bool] = False):
        """
        :param Path file_name: (optional) path filename to file
        :param new_document: (optional) for example 'Part', 'Product' or 'Drawing'.
        :param bool close: (optional) if True, the document is closed.
        """
        self.application = catia()
        self.documents = self.application.documents
        self.file_name = file_name
        self.new_document = new_document

        if self.file_name and not os.path.isfile(self.file_name):
            raise CATIAApplicationException(f'Could not find file: {file_name}')
        else:
            if self.file_name:
                self.file_name = Path(self.file_name)

    def __enter__(self):
        self.documents = self.application.documents
        _document_names = [d.name for d in self.documents]
        _file_name = None
        if type(self.file_name) is Path:
            _file_name = self.file_name.name

        # if the document is already open, switch to that window.
        if _file_name in _document_names:
            window = self.application.windows.item(self.file_name.name)
            window.activate()

            self.document = self.application.active_document

            self.application.logger.info(f'Document {_file_name} already exists')

            return self

        self.document = None

        if self.file_name and self.new_document:
            raise CATIAApplicationException('Only new_document or file_name arguments should be used. Not both.')

        if self.file_name:
            self.document = self.documents.open(self.file_name)
        elif self.new_document:
            self.document = self.documents.add(self.new_document)

        return self

    def __exit__(self, *args):

        self.document.close()
