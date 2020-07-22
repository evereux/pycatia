#! /usr/bin/python3.6

from pycatia.in_interfaces.document import Document

def create_spa_workbench(document: Document):
    """

    :param document:
    :return: workbench com object
    """

    return document.GetWorkbench("SPAWorkbench")
