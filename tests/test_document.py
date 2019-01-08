#! /usr/bin/python3.6

from datetime import datetime
import os

import pytest

from pycatia import CATIAApplication
from pycatia import HybridShapeFactory
from pycatia import CATIAApplicationException

catia = CATIAApplication()
documents = catia.documents()
now_string = datetime.now().strftime('%Y%m%d-%H%M%S')

cat_part = 'tests/CF_catia_measurable_part.CATPart'
cat_product = 'tests/CF_TopLevelAssy.CATProduct'

def test_document_exception():

    with pytest.raises(CATIAApplicationException):
        document = catia.document()

def test_open_document():
    assert documents.documents.Count == 0
    documents.open(cat_part)
    assert documents.documents.Count == 1
    document = catia.document()

    assert document.name in cat_part

    assert f'<Document> (name: {document.name})' == document.__repr__()

    document.close()

    with pytest.raises(FileNotFoundError):
        documents.open('lala')


def test_add_documents():
    documents.add('Part')
    document = catia.document()
    assert 'CATPart' in document.name
    document.close()

    documents.add('Product')
    document = catia.document()
    assert 'CATProduct' in document.name
    document.close()

    documents.add('Drawing')
    document = catia.document()
    assert 'CATDrawing' in document.name
    document.close()

    documents.add('Drawing')
    document = catia.document()
    assert 'CATDrawing' in document.name
    document.close()

    with pytest.raises(ValueError):
        documents.add('lala')


def test_product():
    documents.open(cat_product)
    document = catia.document()
    product = document.product
    assert product.name in cat_product
    assert document.is_product
    assert not document.is_part
    document.close()


def test_part():
    documents.open(cat_part)
    document = catia.document()
    part = document.part
    assert part.name in cat_part
    assert document.is_part
    assert not document.is_product
    document.close()


def test_is_saved():
    documents.open(cat_part)
    document = catia.document()
    document.is_saved()

    part = document.part

    # create a new geometrical set to add point.
    geometrical_set = part.part.HybridBodies.Add()
    geometrical_set.Name = 'lalalalalala'

    # just adding geometrical set isn't enough to trigger is_saved to be False
    # catia r21 bug?
    # so a new point is also added.
    hsf = HybridShapeFactory(part)
    hsf.add_new_point_coord(catia, geometrical_set, (0, 1, 2), 'Point.1')
    part.update()

    assert not document.is_saved()

    document.close()


def test_search_for_items():

    documents.open(cat_part)
    document = catia.document()

    # search for all points
    selection_items = document.search_for_items(document, ['Point', 'Line'])

    assert len(selection_items) == 16


def test_saving():

    new_filename = '__junk__/' + now_string + '.CATPart'

    documents.open(cat_part)
    document = catia.document()

    document.save_as(new_filename)
    document.save()

    assert os.path.isfile(new_filename)

    with pytest.raises(FileExistsError):
        document.save_as(new_filename)

    document.close()

    os.remove(new_filename)
