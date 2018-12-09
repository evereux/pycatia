#! /usr/bin/python3.6


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

        self.document = catia.ActiveDocument

    @property
    def name(self):
        """

        :return:
        """

        return self.document.Name

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
            selected.append(selection.Item(i+1).Value)

        return selected

    def __repr__(self):
        return f'Document object (name: {self.name})'
