#! /usr/bin/python3.6

from win32com.client import Dispatch

from .document import Documents, Document


class CATIAApplication:
    """
    All pycatia scripts will start with the creation on the CATIAApplication() object.

    Usage::

        from pycatia import CATIAApplication
        catia = CATIAApplication()

    .. note::

        CAA V5 Visual Basic help

        CATIA products. The root object is the Application, which aggregates, or includes, Documents, a
        Document collection, and Windows, a Window collection. A collection is an object that gathers objects
        of the same type and is denoted as a plural name. Documents gathers Document objects and provides
        methods for managing individual documents in the collection.The documents belong to one of the four
        types, that is the PartDocument, the ProductDocument, the DrawingDocument and the AnalysisDocument.
        Windows gathers Window objects, and provides methods for managing individual windows in the collection.
    """

    catia = Dispatch('CATIA.Application')

    def documents(self):
        """
        :return: Documents()
        """

        return Documents(self.catia)

    def document(self):
        """

        :return: Document()
        """

        return Document(self.catia)

    def __repr__(self):
        return '<CATIAApplication object ()>'
