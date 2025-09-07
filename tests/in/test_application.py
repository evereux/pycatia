import pytest

from pycatia.mec_mod_interfaces.part_document import PartDocument

from tests.source_files import cat_part_measurable

from tests.conftest import application


def test_application():
    assert 'Application(name="CNEXT")' in application.__repr__()


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_active_document(document_close_all_open):
    documents = application.documents
    documents.open(cat_part_measurable)
    assert application.active_document.name == 'part_measurable.CATPart'


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_refresh(document_open):
    application.refresh_display = False
    assert application.refresh_display is False

    application.refresh_display = True
    assert application.refresh_display is True


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_visible(document_open_test_close_all):
    document = application.active_document

    application.visible = False
    assert application.visible is False

    application.visible = True
    assert application.visible is True

    document.close()
