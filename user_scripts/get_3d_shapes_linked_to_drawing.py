"""
    Description
    ===========
    Get all the linked 3D shapes linked to a drawing.

    Requirements
    ============
    python >= 3.12
    pycatia >= 0.11
    CATIA V5 running with a drawing open.

    Running The Script
    ==================
    > python ./user_scripts/get_3d_shapes_linked_to_drawing.py

    Documentation
    =============
    https://pycatia.readthedocs.io

    More examples and user scripts can be found at:
    https://github.com/evereux/pycatia/tree/master/examples
    https://github.com/evereux/pycatia/tree/master/user_scripts

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.in_interfaces.application import Application
from pycatia.product_structure_interfaces.product import Product

skip_views = ['Main View', 'Background View']


def get_document_name_from_view(app: Application, view) -> str | None:
    product_full_name = None
    if view.name in skip_views:
        return None

    if view.is_generative:
        generative_behaviour = view.generative_behavior
        source_doc = generative_behaviour.document
        if app.vba_type_name(source_doc) == 'Product':
            product_full_name = Product(source_doc.com_object).full_name

    return product_full_name


def main():
    app = catia()
    document: DrawingDocument = app.active_document
    print(f'Active document: {document.name}')
    drawing = document.drawing_root
    sheets = drawing.sheets
    documents = []

    for sheet in sheets:

        if sheet.is_detail():
            continue

        print(f'Processing sheet: "{sheet.name}"')
        views = sheet.views

        for view in views:

            document_name = get_document_name_from_view(app, view)

            if document_name:
                documents.append(document_name)

    return set(documents)


if __name__ == "__main__":
    documents = main()
    print(documents)
