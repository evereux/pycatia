#! /usr/bin/python3.9

import pytest

from pycatia.exception_handling.exceptions import CATIAApplicationException
from pycatia.mec_mod_interfaces.part import Part
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument
from tests.conftest import application
from tests.source_files import cat_part_measurable
from tests.source_files import cat_product


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_activation(document_close_all_open):
    part_document: PartDocument = application.active_document
    part = part_document.part

    item = part.find_object_by_name("Point.1")

    assert not part.is_inactive(item)

    part.deactivate(item)

    assert part.is_inactive(item)


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_axis_systems(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part

    axis_systems = part.axis_systems

    assert axis_systems.com_object.Item(1).name == "Axis.1"


# todo: look into automation this.
# I haven't yet imported the module into pycatia that seems to handle annotation sets.
# def test_annotation_sets():
#     with CATIADocHandler(cat_part_measurable) as caa:
#         document = caa.document
#         part = document.part
#
#         annotation_sets = part.annotation_sets
#
#         assert annotation_sets.com_object.Item(1).name == 'Annotation Set.1'

@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_bodies(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part

    bodies = part.bodies

    assert bodies.com_object.Item(1).Name in ["PartBody", "Hauptkörper"]


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_create_geometrical_set(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    hybrid_bodies = part.hybrid_bodies
    geometrical_set = hybrid_bodies.add()
    geometrical_set.name = "lala"

    assert geometrical_set.name == "lala"


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_density_of_part(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part

    assert part.density == 1000.0


@pytest.mark.parametrize('file_name', [cat_product])
def test_file_name(document_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product

    for current_product in product.products:
        if current_product.is_catpart():
            part = Part(current_product.product)
            assert part.file_name == cat_part_measurable.name


@pytest.mark.parametrize('file_name', [cat_product])
def test_full_name(document_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product

    for current_product in product.products:
        if product.is_catpart():
            part = Part(current_product.product)
            assert part.full_name == str(cat_part_measurable)


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_find_object_by_name(document_close_all_open_test_close):
    part_document: PartDocument = application.active_document
    part = part_document.part
    part.main_body.name = "test_main_body_name"

    body = part.find_object_by_name("test_main_body_name")
    assert body.name == "test_main_body_name"

    with pytest.raises(CATIAApplicationException):
        part.find_object_by_name("lala")
        pass


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_in_work_object(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part

    bodies = part.bodies
    body = bodies.get_item_by_name("PartBody") or bodies.get_item_by_name("Hauptkörper")

    assert body is not None
    part.in_work_object = body

    assert part.in_work_object.name in ["PartBody", "Hauptkörper"]


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_is_up_to_date_1(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part

    assert part.is_up_to_date(part)


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_is_up_to_date_2(document_open_test_close):
    part_document: PartDocument = application.active_document
    part = part_document.part
    hsf = part.hybrid_shape_factory
    hbs = part.hybrid_bodies
    hb = hbs.add()
    point = hsf.add_new_point_coord(0, 0, 0)
    hb.append_hybrid_shape(point)

    assert not part.is_up_to_date(part)


@pytest.mark.parametrize('file_name', [cat_product])
def test_path(document_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product

    for current_product in product.products:
        if current_product.is_catpart():
            part = Part(current_product.product)
            assert part.path() == cat_part_measurable


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_repr(document_open_test_close_all):
    part_document: PartDocument = application.active_document
    part = part_document.part

    assert 'Part(name="cat_part_measurable")' == part.__repr__()
