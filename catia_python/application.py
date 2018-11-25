#! /usr/bin/python3

from win32com.client import Dispatch


class Application:
    """

    ### FROM CAA V5 Visual Basic help ###
    CATIA products. The root object is the Application, which aggregates, or includes, Documents, a Document collection,
    and Windows, a Window collection. A collection is an object that gathers objects of the same type and is denoted as
    a plural name. Documents gathers Document objects and provides methods for managing individual documents in the
    collection.The documents belong to one of the four types, that is the PartDocument, the ProductDocument, the
    DrawingDocument and the AnalysisDocument. Windows gathers Window objects, and provides methods for managing
    individual windows in the collection.


    :return:
    """

    catia = Dispatch('CATIA.Application')

    def __repr__(self):
        """

        :return:
        """
        return f'Application object ()'
