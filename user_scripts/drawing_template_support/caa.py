#! /usr/bin/python3.8
 
from pycatia import catia
from pycatia.in_interfaces.application import Application
from pycatia.in_interfaces.documents import Documents
from pycatia.drafting_interfaces.drawing_document import DrawingDocument


def get_caa() -> Application:
    """
    Get the catia application object
    :return:
    """

    caa_ = catia()

    return caa_


def get_documents(caa_) -> Documents:
    """

    :param caa_:
    :return:
    """

    documents_ = caa_.documents

    return documents_


def get_active_drawing(caa_) -> DrawingDocument:
    """

    :param caa_:
    :return:
    """

    active_document = caa_.active_document
    drawing_document = DrawingDocument(active_document.com_object)

    return drawing_document


caa = get_caa()
documents = get_documents(caa)
