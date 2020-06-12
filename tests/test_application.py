#! /usr/bin/python3.6

from pycatia import catia
from tests.source_files import cat_part_measurable


def test_application():
    assert 'Application(name="CNEXT")' in catia.__repr__()


def test_refresh():
    documents = catia.documents
    documents.open(cat_part_measurable)
    document = catia.active_document

    catia.refresh_display = False
    assert catia.refresh_display is False

    catia.refresh_display = True
    assert catia.refresh_display is True

    document.close()


def test_visible():
    documents = catia.documents
    documents.open(cat_part_measurable)
    document = catia.active_document

    catia.visible = False
    assert catia.visible is False

    catia.visible = True
    assert catia.visible is True

    document.close()
