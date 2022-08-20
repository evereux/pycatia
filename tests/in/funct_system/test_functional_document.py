import pytest

from pycatia import CATIADocHandler
from pycatia.funct_system_interfaces.functional_document import FunctionalDocument
from pycatia.funct_system_interfaces.functional_description import FunctionalDescription
from tests.source_files import cat_functional_system


def test_current_description():
    with CATIADocHandler(cat_functional_system) as caa:
        functional_document = caa.document

        assert functional_document.current_description.name == "Functional Document Description"


def test_original_description():
    with CATIADocHandler(cat_functional_system) as caa:
        functional_document = caa.document

        assert functional_document.current_description.name == "Functional Document Description"
