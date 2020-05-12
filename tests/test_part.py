#! /usr/bin/python3.6

import pytest

from pycatia.base_interfaces import CATIAApplication
from pycatia.base_interfaces import CATIADocHandler
from pycatia.exception_handling import CATIAApplicationException
from pycatia.part_interfaces import Part
from tests.source_files import cat_part_measurable
from tests.source_files import cat_product
from tests.source_files import cat_part_not_updated
from tests.source_files import cat_part_1

catia = CATIAApplication()


def test_activation():
    with CATIADocHandler(cat_part_measurable) as handler:
        part = handler.document.part()

        item = part.find_object_by_name('Point.1')

        assert not part.is_inactive(item)

        part.deactivate(item)

        assert part.is_inactive(item)


def test_annotation_sets():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        annotation_sets = part.get_annotation_sets()

        assert annotation_sets.Item(1).name == 'Annotation Set.1'


def test_create_geometrical_set():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        geometrical_set = part.create_geometrical_set('lala')

        assert geometrical_set.name == 'lala'


def test_density_of_part():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        assert part.density == 8216.0


def test_find_object_by_name():
    with CATIADocHandler(cat_part_measurable) as handler:
        part = handler.document.part()

        item = part.find_object_by_name('Extrude.1')

        assert item.name == 'Extrude.1'


def test_file_name():
    with CATIADocHandler(cat_product) as handler:
        document = handler.document
        product = document.product()
        products = product.get_products()

        for product in products:
            if product.is_catpart():
                part = Part(product.product)
                assert part.file_name == cat_part_1.name


def test_full_name():
    with CATIADocHandler(cat_product) as handler:
        document = handler.document
        product = document.product()
        products = product.get_products()

        for product in products:
            if product.is_catpart():
                part = Part(product.product)
                assert part.full_name == str(cat_part_1)


def test_get_axes_names():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        axes_names = part.get_axes_names()

        assert axes_names[0] == 'Axis System.3'
        assert axes_names[1] == 'Axis System.4'


def test_get_axis_by_name():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        axis = part.get_axis_by_name('Axis System.4')

        assert axis.name == 'Axis System.4'

        axis = part.get_axis_by_name('lala')

        assert axis is None


def test_get_bodies_names():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        body_names = part.get_bodies_names()

        assert body_names[0] == 'PartBody'
        assert body_names[1] == 'AnotherPartBody'


def test_get_body_by_name():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        body = part.get_body_by_name('AnotherPartBody')

        assert body.name == 'AnotherPartBody'

        body = part.get_body_by_name('lala')

        assert body is None


def test_get_hybrid_bodies_names():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        hybrid_bodies_names = part.get_hybrid_bodies_names()

        assert hybrid_bodies_names == ['Arcs',
                                       'Axis_Systems',
                                       'Cylinders',
                                       'Lines',
                                       'Points',
                                       'Planes',
                                       'Sketches',
                                       'Splines',
                                       'Surfaces']


def test_get_hybrid_by_name():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        hybrid_body = part.get_hybrid_body_by_name('Arcs')

        assert hybrid_body.name == 'Arcs'

        with pytest.raises(CATIAApplicationException, match='Could not find hybrid_body name "name does not exist".'):
            hybrid_body = part.get_hybrid_body_by_name('name does not exist')

            assert hybrid_body.name == 'Arcs'


def test_is_updated():
    with CATIADocHandler(cat_part_measurable) as handler:
        part = handler.document.part()

        assert part.is_upated(part.part)

    with CATIADocHandler(cat_part_not_updated) as handler:
        part = handler.document.part()

        assert not part.is_upated(part.part)


def test_in_work_object():
    with CATIADocHandler(cat_part_measurable) as handler:
        part = handler.document.part()

        planes_hybrid_body = part.get_hybrid_body_by_name('Planes')

        part.in_work_object = planes_hybrid_body

        assert part.in_work_object.name == 'Planes'


def test_path():
    with CATIADocHandler(cat_product) as handler:
        document = handler.document
        product = document.product()
        products = product.get_products()

        for product in products:
            if product.is_catpart():
                part = Part(product.product)
                assert part.path() == cat_part_1


def test_repr():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        assert 'Part(name="CF_catia_measurable_part")' == part.__repr__()
