#! /usr/bin/python3.9

import pytest

from pycatia import CATIADocHandler
from pycatia.funct_system_interfaces.functional_description import FunctionalDescription
from pycatia.funct_system_interfaces.functional_document import FunctionalDocument
from tests.source_files import cat_functional_system


def test_current_description():
    with CATIADocHandler(cat_functional_system) as caa:
        document = caa.document
        assert document is not None

        functional_document = FunctionalDocument(document.com_object)
        assert functional_document.current_description.name == "Functional Document Description"


def test_original_description():
    with CATIADocHandler(cat_functional_system) as caa:
        document = caa.document
        assert document is not None

        functional_document = FunctionalDocument(document.com_object)
        assert functional_document.current_description.name == "Functional Document Description"
