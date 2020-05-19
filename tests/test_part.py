#! /usr/bin/python3.6

import pytest

from pycatia.base_interfaces.context import CATIADocHandler
from pycatia.exception_handling import CATIAApplicationException
from pycatia.mec_mod_interfaces.part import Part
from tests.source_files import cat_part_measurable
from tests.source_files import cat_product
from tests.source_files import cat_part_not_updated
from tests.source_files import cat_part_1


def test_activation():
    with CATIADocHandler(cat_part_measurable) as handler:
        part = handler.document.part()

        item = part.find_object_by_name('Point.1')

        assert not part.is_inactive(item)

        part.deactivate(item)

        assert part.is_inactive(item)


def test_axis_systems():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        axis_systems = part.axis_systems

        assert axis_systems.com_object.Item(1).name == 'Axis System.3'
        assert axis_systems.com_object.Item(2).name == 'Axis System.4'


def test_annotation_sets():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        annotation_sets = part.annotation_sets

        assert annotation_sets.com_object.Item(1).name == 'Annotation Set.1'


def test_bodies():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        bodies = part.bodies

        assert bodies.com_object.Item(1).Name == 'PartBody'
        assert bodies.com_object.Item(2).Name == 'AnotherPartBody'


def test_create_geometrical_set():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()
        hybrid_bodies = part.hybrid_bodies
        geometrical_set = hybrid_bodies.add()
        geometrical_set.name = 'lala'

        assert geometrical_set.name == 'lala'


def test_density_of_part():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        assert part.density == 8216.0


def test_file_name():
    with CATIADocHandler(cat_product) as handler:
        document = handler.document
        product = document.product()
        products = product.get_products()

        for product in products:
            if product.is_catpart():
                part = Part(product.product)
                assert part.file_name == cat_part_1.name


def test_find_object_by_name():
    with CATIADocHandler(cat_part_measurable) as handler:
        part = handler.document.part()

        item = part.find_object_by_name('Extrude.1')

        assert item.name == 'Extrude.1'


def test_full_name():
    with CATIADocHandler(cat_product) as handler:
        document = handler.document
        product = document.product()
        products = product.get_products()

        for product in products:
            if product.is_catpart():
                part = Part(product.product)
                assert part.full_name == str(cat_part_1)


def test_find_object_by_name():
    with CATIADocHandler(cat_part_measurable) as handler:
        document = handler.document
        part = document.part()

        body = part.find_object_by_name('AnotherPartBody')
        assert body.name == 'AnotherPartBody'

        body = part.find_object_by_name('lala')
        assert body is None


def test_in_work_object():
    part_body_name = 'AnotherPartBody'

    with CATIADocHandler(cat_part_measurable) as handler:
        part_body_name = 'AnotherPartBody'

        part = handler.document.part()

        bodies = part.bodies
        body = bodies.get_item_by_name(part_body_name)

        part.in_work_object = body

        assert part.in_work_object.name == part_body_name


def test_is_up_to_date():
    with CATIADocHandler(cat_part_measurable) as handler:
        part = handler.document.part()

        assert part.is_up_to_date(part)

    with CATIADocHandler(cat_part_not_updated) as handler:
        part = handler.document.part()

        assert not part.is_up_to_date(part)


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
