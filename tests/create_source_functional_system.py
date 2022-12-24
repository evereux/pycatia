import os
from pathlib import Path

from pycatia.funct_system_interfaces.functional_document import FunctionalDocument
from tests.common_vars import caa
from tests.common_vars import test_files

source_functional_document = Path(os.getcwd(), test_files, "FunctionalSystem1.CATSystem")


def create_cat_functional_system():
    documents = caa.documents
    functional_document = documents.add("FunctionalSystem")
    functional_document = FunctionalDocument(functional_document.com_object)

    functional_document.current_description.name = "Functional Document Description"

    functional_document.save_as(source_functional_document)


def get_cat_functional_system():
    if not source_functional_document.exists():
        caa.logger.info(f"Creating {source_functional_document}.")
        create_cat_functional_system()
    return source_functional_document
