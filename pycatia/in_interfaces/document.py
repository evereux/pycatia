#! /usr/bin/python3.6

from pathlib import Path
import warnings

from pywintypes import com_error

from pycatia.exception_handling import CATIAApplicationException
from pycatia.mec_mod_interfaces.part import Part
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.drafting_interfaces.drawing_root import DrawingRoot


class Document(AnyObject):
    """
    The Document object is used to access the currently active document in the catia session.

    If the document fails to activate try closing CATIA and killing any existing COM object
    processes in task manager.

    .. note::

        CAA V5 Visual Basic help

        The Document is the object which stores your pycatia data on disk. A document is either created
        empty using the File->New command or using the Add method of the Documents collection, or opened
        from a file using the File->Open command or using the Open method of the Documents collection.
        CATIA provides access to four document types: the PartDocument, the ProductDocument, the
        DrawingDocument and the AnalysisDocument. The Document abstract object gathers the properties and
        methods common to all actual document types. When a document is created or opened, it is
        automatically set as the active document and displayed in a window which automatically becomes
        the active window. A document aggregates the current object or set of objects in the Selection
        object, and Cameras, a camera collection.

    """

    def __init__(self, document_com_object):
        super().__init__(document_com_object)
        try:
            self.document = document_com_object
            self.catia = document_com_object
        except com_error:
            message = "Could not activate document. Is a document open?"
            raise CATIAApplicationException(message)

    @property
    def is_part(self):
        """
        Determine whether the active document is a CATPart.

        :return: bool
        """
        try:
            if self.part().part:
                return True
        except AttributeError:
            return False

    @property
    def is_product(self):
        """
        Determine whether the active document is a CATProduct.

        :return: bool
        """

        if self.product().is_catproduct():
            return True
        return False

    @property
    def is_saved(self):
        """
        Returns true if document is saved.

        .. note::
            CAA V5 Visual Basic help

            Property Saved( ) As boolean (Read Only)

            Returns whether the document has been modified, and thus needs to be saved.
            This happens when the document has changed since either its creation or its last save.
            True if the document has not been changed: the document doesn't need to be saved.
            False if the document has been changed: the document needs to be saved.

            | Example:
            | This example retrieves in HasChanged whether the Doc document needs to be saved.
            | HasChanged = NOT Doc.Saved

        :return: bool
        """

        return self.document.Saved

    @property
    def name(self):
        """

        :return: str - document name.
        """

        return self.document.Name

    @property
    def full_name(self):
        """

        .. note::
            CAA V5 Visual Basic help

            Property FullName( ) As CATBSTR (Read Only)

            | Returns the document's full file name, including its path.
            | Example:
            | This example retrieves in DocFullName the Doc document's full file name.
            |     DocFullName = Doc.FullName
            |
            | The returned value is like this:
            |     e:\\users\\psr\\Parts\\MyNicePart.CATPart


        :return: str - full path document name
        """

        return str(self.path())

    def drawing_root(self):
        """
        :return:
        """
        return DrawingRoot(self.document.DrawingRoot)

    def export_data(self, filename, filetype):

        """
        .. note::
            CAA V5 Visual Basic help

            Sub ExportData( CATBSTR  fileName, CATBSTR  format)

            | Exports the data contained in the document to another format.
            | Parameters:
            |   fileName
            |       The name of the exported file
            |   format
            |       The name of the format
            | Example:
            |   This example writes the Doc document in the IGES format under the IGESDoc name.
            |       Doc.ExportData("IGESDoc", "igs")


        :param str filename: filename including full path.
        :param str filetype: filetype is the extension of required filetype. The filetype must be supported by CATIA.
        :return:
        """

        self.document.ExportData(filename, filetype)

    def path(self):
        """

        Returns the pathlib.Path() object of the document fullname.

        example e:\\users\\psr\\Parts\\MyNicePart.CATPart
        >>> Document.path().name
        MyNicePart.CATPart
        >>> Document.path().parent
        e:\\users\\psr\\Parts\\
        >>> Document.path().suffix
        .CATPart

        :return: Path()
        """

        return Path(self.document.FullName)

    def part(self):
        """
        :return: Part()
        """

        return Part(self.document.Part)

    def product(self):
        """
        :return: :class:`Product()`
        """

        return Product(self.document.Product)

    def activate(self):
        """
        Activates the document

        .. note::
            CAA V5 Visual Basic help

            Sub Activate( )

            Activates the document. Activating a document means that this document is the one on which the end user is
            now working on. This document possibly reconfigures the menu bar and toolbars with its own commands if its
            type is different from the type of the previous active document. The first window in the window collection
            which contains this document becomes the active one.

            Example:
            | This example activates the Doc document.
            | Doc.Activate()

        """

        self.document.Activate()

    def close(self):
        """
        Closes the current document.

        .. note::
            CAA V5 Visual Basic help

            Sub Close( )

            Closes the document. This closes all the windows displaying the document. If the document needs to be saved,
            the end user is prompted whether to save the document, or to close it anyway.

            | Example:
            | This example closes the Doc document
            |  Doc.Close()

        """

        self.document.Close()

    def save(self):
        """
        Save the current document.

        .. note::
            CAA V5 Visual Basic help

            Sub Save( )

            Saves the document.
            | Example:
            | This example saves the Doc document.
            | Doc.Save()

        """

        self.document.Save()

    def save_as(self, file_name, overwrite=False):
        """
        Save the document to a new name.

        .. note::
            CAA V5 Visual Basic help

            Sub SaveAs( CATBSTR  fileName)

            Saves the document with another name.
            |  Parameters:
            |     fileName
            |         The name to assign to the document
            | Example:
            | This example saves the Doc document with the NewName name.
            | Doc.SaveAs("NewName")

        :param str file_name: full pathname to new file_name
        :param bool overwrite:
        """

        file_name = Path(file_name)
        if overwrite is False:
            if file_name.is_file():
                raise FileExistsError(f'File: {file_name} already exists.')
        else:
            if file_name.is_file():
                warnings.warn('File already exists. Click YES in CATIA V5.')
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
        :param list selection_objects:
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
            selected.append(AnyObject(selection.Item(i + 1).Value))

        return selected

    def __repr__(self):
        return f'Document(name="{self.name}")'
