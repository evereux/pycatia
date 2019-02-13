#! /usr/bin/python3.6

from pycatia import CATIAApplication

def initialise():
    """

    :return:
    """
    catia = CATIAApplication()
    documents = catia.documents()

    return catia, documents
