#! /usr/bin/python3.9

import os
from pathlib import Path

import pytest

from pycatia import CatWorkModeType
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument
from tests.conftest import application
from tests.source_files import cat_part_measurable
from tests.source_files import cat_product


@pytest.mark.parametrize('file_name', [cat_product])
def test_analyze(document_close_all_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product
    product.activate_terminal_node(product.products)
    product.apply_work_mode(CatWorkModeType.DESIGN_MODE)

    assert 1.5 == product.analyze.mass
    assert 1500000.0 == product.analyze.volume
    assert 120000.0 == product.analyze.wet_area
    assert (50.0, 50.0, 25.0) == product.analyze.get_gravity_center()
    assert (
               1562.5000000000005,
               0.0,
               0.0,
               0.0,
               1562.5000000000005,
               0.0,
               0.0,
               0.0,
               2499.9999999999986,
           ) == product.analyze.get_inertia()


@pytest.mark.parametrize('file_name', [cat_product])
def test_attributes(document_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product

    attributes = (
        "(Product) Attributes... \n"
        "File Name:             product_top.CATProduct\n"
        "Name:                  cat_product_1\n"
        "Part Number:           cat_product_1\n"
        "Revision:              A.1\n"
        "Definition:            pycatia product for testing\n"
        "Nomenclature:          pycatia product for testing\n"
        "Description Instance:  \n"
        "Description Reference: \n"
        'Reference:             Product(name="cat_product_1")\n'
        "Is CATProduct:         True\n"
        "Is CATPart:            False"
    )

    assert product.attributes() == attributes


@pytest.mark.parametrize('file_name', [cat_product])
def test_count_children(document_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product
    assert product.count_children() == 4


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_definition(document_open):
    part_document: PartDocument = application.active_document
    product = part_document.product
    assert "pycatia part for testing" == product.definition
    product.definition = "new definition"
    assert "new definition" == product.definition


@pytest.mark.parametrize('file_name', [cat_product])
def test_description_instance(document_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product
    children = product.get_children()
    child = children[0]

    assert "description instance text" == child.description_instance

    new_instance_name = "description instance text.1"
    child.description_instance = new_instance_name

    assert new_instance_name == child.description_instance


@pytest.mark.parametrize('file_name', [cat_product])
def test_description_reference(document_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product
    children = product.get_children()
    child = children[0]

    assert "" == child.description_reference

    new_description_reference = "This is the definition for CF_SubProduct1 2"
    child.description_reference = new_description_reference

    assert new_description_reference == child.description_reference


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_file_name(document_open):
    part_document: PartDocument = application.active_document
    product = part_document.product
    assert cat_part_measurable.name == product.file_name


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_full_name(document_open):
    part_document: PartDocument = application.active_document
    product = part_document.product
    assert str(cat_part_measurable) == product.full_name


@pytest.mark.parametrize('file_name', [cat_product])
def test_get_child(document_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product
    child = product.get_child(0)
    assert child.part_number == "cat_product_sub_1"


@pytest.mark.parametrize('file_name', [cat_product])
def test_get_products(document_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product
    products = product.products
    assert 'Product(name="cat_product_sub_1.1")' == products[0].__repr__()


@pytest.mark.parametrize('file_name', [cat_product])
def test_has_children_product(document_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product
    assert product.has_children()


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_has_children_part(document_open):
    part_document: PartDocument = application.active_document
    product = part_document.product
    assert not product.has_children()


@pytest.mark.parametrize('file_name', [cat_product])
def test_is_catproduct_is_catpart(document_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product
    assert product.is_catproduct()
    assert not product.is_catpart()


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_is_catpart(document_open):
    part_document: PartDocument = application.active_document
    product = part_document.product
    assert product.is_catpart()
    assert not product.is_catproduct()


@pytest.mark.parametrize('file_name', [cat_product])
def test_move(document_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product

    product.activate_terminal_node(product.products)
    product.apply_work_mode(CatWorkModeType.DESIGN_MODE)

    # move the first child in parent.
    product = product.products[0]

    transformation = (1.000, 0, 0, 0, 0.707, 0.707, 0, -0.707, 0.707, 10.000, 20.000, 30.000)
    product.move.apply(transformation)

    assert (
               520.8333333333333,
               0.0,
               0.0,
               0.0,
               677.0833333333264,
               -156.24999999999818,
               0.0,
               -156.24999999999818,
               677.0833333333264,
           ) == product.analyze.get_inertia()


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_name(document_open):
    part_document: PartDocument = application.active_document
    product = part_document.product
    assert "cat_part_measurable" == product.name


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_nomenclature(document_open):
    part_document: PartDocument = application.active_document
    product = part_document.product
    assert "pycatia part for testing" == product.nomenclature

    new_nomenclature = "New Test Part"
    product.nomenclature = new_nomenclature
    assert new_nomenclature == product.nomenclature


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_part_number(document_close_all_open_test_close):
    part_document: PartDocument = application.active_document
    product = part_document.product
    assert "cat_part_measurable" == product.part_number

    product.part_number = "new_part_number"
    assert "new_part_number" == product.part_number


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_path(document_open):
    part_document: PartDocument = application.active_document
    product = part_document.product
    product_path = Path(os.getcwd(), cat_part_measurable)
    assert product_path == product.path()


def test_position():
    # todo: write test feature
    pass


def test_proudcts():
    # todo: write test feature
    pass


def test_publications():
    # todo: write test feature
    pass


@pytest.mark.parametrize('file_name', [cat_product])
def test_reference_product(document_open):
    product_document: ProductDocument = application.active_document
    product = product_document.product
    assert product.reference_product.name == "cat_product_1"


def test_relations():
    # todo: write test feature.
    pass


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_revision(document_open):
    part_document: PartDocument = application.active_document
    product = part_document.product
    assert "A.1" == product.revision
    product.revision = "B"
    assert "B" == product.revision


def test_activate_default_shape():
    # todo: write test feature
    pass


def test_activate_shape():
    # todo: write test feature
    pass


def test_add_master_shape_representation():
    # todo: write test feature
    pass


def test_add_shape_representation():
    # todo: write test feature
    pass


def test_connections():
    # todo: write test feature
    pass


def test_create_reference_from_name():
    # todo: write test feature
    pass


def test_desactivate_default_shape():
    # todo: write test feature
    pass


def test_desactivate_shape():
    # todo: write test feature
    pass


def test_extract_bom():
    # todo: write test feature
    pass


def test_get_active_shape_name():
    # todo: write test feature
    pass


def test_get_all_shape_names():
    # todo: write test feature
    pass


def test_get_children():
    # todo: write test feature
    pass


def test_get_default_shape_name():
    # todo: write test feature
    pass


def test_get_master_shape_representation():
    # todo: write test feature
    pass


def test_get_master_shape_representation_path_name():
    # todo: write test feature
    pass


def test_get_number_of_shapes():
    # todo: write test feature
    pass


def test_get_shape_path_name():
    # todo: write test feature
    pass


def test_get_shape_representation():
    # todo: write test feature
    pass


def test_get_technological_object():
    # todo: write test feature
    pass


def test_has_shape_representation():
    # todo: write test feature
    pass


def test_remove_master_shape_representation():
    # todo: write test feature
    pass


def test_remove_shape_representation():
    # todo: write test feature
    pass


def test_update():
    # todp: write test feature
    pass


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_repr(document_open):
    part_document: PartDocument = application.active_document
    product = part_document.product

    assert 'Product(name="cat_part_measurable")' == product.__repr__()
