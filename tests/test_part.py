#! /usr/bin/python3.6

from pycatia import CATIAApplication

catia = CATIAApplication()
cat_part = r'tests/CF_catia_measurable_part.CATPart'


def test_density_of_part():

    documents = catia.documents()
    documents.open(cat_part)
    document = catia.document()
    part = document.part

    assert part.density == 8216.0
    document.close()
