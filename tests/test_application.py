#! /usr/bin/python3.6

from pycatia import CATIAApplication

catia = CATIAApplication()
cat_part = r'tests/CF_catia_measurable_part.CATPart'


def test_application():
    assert 'CATIAApplication' in catia.__repr__()


def test_refresh():

    documents = catia.documents()
    documents.open(cat_part)
    document = catia.document()

    catia.refresh_display(state=False)
    assert catia.refresh_display() is False

    catia.refresh_display(state=True)
    assert catia.refresh_display() is True

    document.close()


def test_visible():

    documents = catia.documents()
    documents.open(cat_part)
    document = catia.document()

    catia.visible(state=False)
    assert catia.visible() is False

    catia.visible(state=True)
    assert catia.visible() is True

    document.close()
