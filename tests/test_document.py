#! /usr/bin/python3.6

from datetime import datetime
import os

import pytest

from pycatia.base_interfaces import CATIAApplication
from pycatia.base_interfaces import CATIADocHandler
from pycatia.hybrid_shape_interfaces import HybridShapeFactory

now_string = datetime.now().strftime('%Y%m%d-%H%M%S')

cat_part = r'tests/CF_catia_measurable_part.CATPart'
cat_product = r'tests/CF_TopLevelAssy.CATProduct'


def test_no_such_file():
    with pytest.raises(FileNotFoundError):
        catia = CATIAApplication()
        documents = catia.documents()
        documents.open('lala')


def test_open_document():
    # This assertion has been removed as my version of CATIA keeps an open link to ABQMaterialPropertiesCatalog.CATfct
    # once the document is closed. I don't know if this is a CATIA bug or `feature` to keep the linked item loaded.
    # assert documents.documents.Count == 0

    with CATIADocHandler(cat_part) as handler:
        document = handler.document
        assert document.name in cat_part
        assert f'Document() name: {document.name}' == document.__repr__()


def test_add_documents():
    with CATIADocHandler(new_document='Part') as handler:
        document = handler.document
        assert 'CATPart' in document.name

    with CATIADocHandler(new_document='Part') as handler:
        document = handler.document
        assert 'CATPart' in document.name

    with CATIADocHandler(new_document='Part') as handler:
        document = handler.document
        assert 'CATPart' in document.name

    with pytest.raises(ValueError):
        with CATIADocHandler(new_document='lala'):
            pass


def test_product():
    with CATIADocHandler(cat_product) as handler:
        document = handler.document
        product = document.product()
        assert product.name in cat_product
        assert document.is_product
        assert not document.is_part


def test_part():
    with CATIADocHandler(cat_part) as handler:
        document = handler.document
        part = document.part()
        assert part.name in cat_part
        assert document.is_part
        assert not document.is_product


def test_is_saved():
    with CATIADocHandler(cat_part) as handler:
        catia = handler.catia
        document = handler.document
        assert document.is_saved

        part = document.part()

        # create a new geometrical set to add point.
        geometrical_set = part.part.HybridBodies.Add()
        geometrical_set.Name = 'lalalalalala'

        # just adding geometrical set isn't enough to trigger is_saved to be False
        # catia r21 bug?
        # so a new point is also added.
        hsf = HybridShapeFactory(part)
        hsf.add_new_point_coord(catia, geometrical_set, (0, 1, 2), 'Point.1')
        part.update()

        assert not document.is_saved


def test_search_for_items():
    with CATIADocHandler(cat_part) as handler:
        document = handler.document

        # search for all points
        selection_items = document.search_for_items(document, ['Point', 'Line'])

        assert len(selection_items) == 16


def test_saving():
    new_filename = '__junk__/' + now_string + '.CATPart'

    with CATIADocHandler(cat_part) as handler:
        document = handler.document

        document.save_as(new_filename)
        document.save()

        assert os.path.isfile(new_filename)

        with pytest.raises(FileExistsError):
            document.save_as(new_filename)

    os.remove(new_filename)


def test_activate_document():
    catia = CATIAApplication()
    documents = catia.documents()
    documents.open(cat_part)
    document_part = catia.document()
    documents.open(cat_product)
    document_product = catia.document()

    assert document_part.name == os.path.basename(cat_part)
    assert document_product.name == os.path.basename(cat_product)

    document_part.activate()
    document = catia.document()

    assert document.name == os.path.basename(cat_part)

    document_part.close()
    document_product.close()


def test_new_from():
    catia = CATIAApplication()
    documents = catia.documents()
    document = documents.new_from(cat_part)

    assert document.name is not os.path.basename(cat_part)

    document.close()

    with pytest.raises(FileNotFoundError):
        documents.new_from('lala')


def test_num_open():
    with CATIADocHandler(cat_part) as handler:
        documents = handler.documents
        # see warning in documentation for num_open()

        assert documents.num_open() == 2


def test_full_name():
    """

    TODO: make the assertion work whereever the respository is cloned to.

    :return:
    """
    with CATIADocHandler(cat_part) as handler:
        document = handler.document

        assert r'pycatia\tests\CF_catia_measurable_part.CATPart' in \
               document.full_name


def test_export_document():
    with CATIADocHandler(cat_part) as handler:
        document = handler.document

        export_type = 'igs'
        export_name = 'export_file'

        path = os.path.dirname(os.path.abspath(cat_part))
        export_name = os.path.join(path, export_name)

        document.export_data(export_name, export_type)

        assert os.path.isfile(f'{export_name}.igs')

        os.remove(f'{export_name}.igs')
