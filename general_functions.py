#! /user/bin/python3.6

from .catiaapplication import CATIAApplication
from .document import Document
from .part import Part


def create_measurable(spa_workbench, com_reference):
    """

    :param spa_workbench:
    :param com_reference:
    :return:
    """

    return spa_workbench.GetMeasurable(com_reference)


def get_document_part_object():
    """

    Initialises the CATIA Application object.

    :return: Document COM object, Part()
    """

    catia = CATIAApplication()
    document = Document(catia.catia).document
    part = Part(document)

    return document, part
