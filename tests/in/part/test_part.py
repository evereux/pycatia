#! /usr/bin/python3.6

from pycatia import CATIADocHandler
from pycatia.mec_mod_interfaces.part import Part

from tests.source_files import cat_part_measurable
from tests.source_files import cat_product


def test_activation():
    with CATIADocHandler(cat_part_measurable) as caa:
        part = caa.document.part()

        item = part.find_object_by_name('Point.1')

        assert not part.is_inactive(item)

        part.deactivate(item)

        assert part.is_inactive(item)


def test_axis_systems():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        part = document.part()

        axis_systems = part.axis_systems

        assert axis_systems.com_object.Item(1).name == 'Axis.1'


# todo: look into automation this.
# I haven't yet imported the module into pycatia that seems to handle annotation sets.
# def test_annotation_sets():
#     with CATIADocHandler(cat_part_measurable) as caa:
#         document = caa.document
#         part = document.part()
#
#         annotation_sets = part.annotation_sets
#
#         assert annotation_sets.com_object.Item(1).name == 'Annotation Set.1'


def test_bodies():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        part = document.part()

        bodies = part.bodies

        assert bodies.com_object.Item(1).Name == 'PartBody'


def test_create_geometrical_set():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        part = document.part()
        hybrid_bodies = part.hybrid_bodies
        geometrical_set = hybrid_bodies.add()
        geometrical_set.name = 'lala'

        assert geometrical_set.name == 'lala'


def test_density_of_part():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        part = document.part()

        assert part.density == 1000.0


def test_file_name():
    with CATIADocHandler(cat_product) as caa:
        document = caa.document
        product = document.product()
        products = product.get_products()

        for product in products:
            if product.is_catpart():
                part = Part(product.product)
                assert part.file_name == cat_part_measurable.name


def test_full_name():
    with CATIADocHandler(cat_product) as caa:
        document = caa.document
        product = document.product()
        products = product.get_products()

        for product in products:
            if product.is_catpart():
                part = Part(product.product)
                assert part.full_name == str(cat_part_measurable)


def test_find_object_by_name():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        part = document.part()

        body = part.find_object_by_name('PartBody')
        assert body.name == 'PartBody'

        body = part.find_object_by_name('lala')
        assert body is None


def test_in_work_object():
    with CATIADocHandler(cat_part_measurable) as caa:
        part_body_name = 'PartBody'

        part = caa.document.part()

        bodies = part.bodies
        body = bodies.get_item_by_name(part_body_name)

        part.in_work_object = body

        assert part.in_work_object.name == part_body_name


def test_is_up_to_date():
    with CATIADocHandler(cat_part_measurable) as caa:
        part = caa.document.part()

        assert part.is_up_to_date(part)

    with CATIADocHandler(new_document="Part") as caa:
        part = caa.document.part()
        hsf = part.hybrid_shape_factory
        hbs = part.hybrid_bodies
        hb = hbs.add()
        point = hsf.add_new_point_coord(0, 0, 0)
        hb.append_hybrid_shape(point)

        assert not part.is_up_to_date(part)


def test_path():
    with CATIADocHandler(cat_product) as caa:
        document = caa.document
        product = document.product()
        products = product.get_products()

        for product in products:
            if product.is_catpart():
                part = Part(product.product)
                assert part.path() == cat_part_measurable


def test_repr():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        part = document.part()

        assert 'Part(name="cat_part_measurable")' == part.__repr__()
