#! /usr/bin/python3.9

import pytest

from pycatia.funct_system_interfaces.functional_document import FunctionalDocument
from tests.conftest import application
from tests.source_files import cat_functional_system


@pytest.mark.parametrize('file_name', [cat_functional_system])
def test_current_description(document_close_all_open):
    functional_document: FunctionalDocument = application.active_document

    assert functional_document.current_description.name == "Functional Document Description"


@pytest.mark.parametrize('file_name', [cat_functional_system])
def test_original_description(document_open_test_close_all):
    functional_document: FunctionalDocument = application.active_document

    assert functional_document.original_description.name == "Functional Document Description"
