#! /usr/bin/python36


class Document:

    def __init__(self, catia):
        """

        ### FROM CAA V5 Visual Basic help ###
        # The Document is the object which stores your catia_python data on disk. A document is either created
        # empty using the File->New command or using the Add method of the Documents collection, or opened
        # from a file using the File->Open command or using the Open method of the Documents collection.
        # CATIA provides access to four document types: the PartDocument, the ProductDocument, the
        # DrawingDocument and the AnalysisDocument. The Document abstract object gathers the properties and
        # methods common to all actual document types. When a document is created or opened, it is
        # automatically set as the active document and displayed in a window which automatically becomes
        # the active window. A document aggregates the current object or set of objects in the Selection
        # object, and Cameras, a camera collection.

        :param catia: catia com object
        :return:
        """

        self.document = catia.ActiveDocument

    @property
    def catia_document(self):
        """

        ### FROM CAA V5 Visual Basic help ###
        # The Document is the object which stores your catia_python data on disk. A document is either created
        # empty using the File->New command or using the Add method of the Documents collection, or opened
        # from a file using the File->Open command or using the Open method of the Documents collection.
        # CATIA provides access to four document types: the PartDocument, the ProductDocument, the
        # DrawingDocument and the AnalysisDocument. The Document abstract object gathers the properties and
        # methods common to all actual document types. When a document is created or opened, it is
        # automatically set as the active document and displayed in a window which automatically becomes
        # the active window. A document aggregates the current object or set of objects in the Selection
        # object, and Cameras, a camera collection.

        :return:
        """
        return self.document

    @property
    def name(self):
        """

        :return:
        """

        return self.document.Name

    def __repr__(self):
        return f'Document object (name: {self.name})'
