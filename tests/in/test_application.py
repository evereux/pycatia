#! /usr/bin/python3.9
from pycatia.mec_mod_interfaces.part_document import PartDocument
from tests.common_vars import caa
from tests.source_files import cat_part_measurable


def test_application():
    assert 'Application(name="CNEXT")' in caa.__repr__()


def test_active_document():
    documents = caa.documents
    documents.open(cat_part_measurable)
    assert caa.active_document.name == 'part_measurable.CATPart'


def test_refresh():
    documents = caa.documents
    part_document: PartDocument = documents.open(cat_part_measurable)

    caa.refresh_display = False
    assert caa.refresh_display is False

    caa.refresh_display = True
    assert caa.refresh_display is True

    part_document.close()


def test_visible():
    documents = caa.documents
    part_document: PartDocument = documents.open(cat_part_measurable)
    document = caa.active_document

    caa.visible = False
    assert caa.visible is False

    caa.visible = True
    assert caa.visible is True

    document.close()
