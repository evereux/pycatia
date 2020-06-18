#! /usr/bin/python3.6

import os
from pathlib import Path

from pycatia import CATIADocHandler
from pycatia.enumeration.enumeration_types import cat_work_mode_type
from pycatia.product_structure_interfaces.product import Product
from tests.source_files import cat_product
from tests.source_files import cat_part_measurable


def test_analyze():
    with CATIADocHandler(cat_product) as handler:
        product = handler.document.product()

        assert (
                0.3061919497633215 == product.analyze.mass and
                306191.9497633215 == product.analyze.volume and
                39341.17217653142 == product.analyze.wet_area and
                (65.39210812865413, -25.857059154544192, 0.0) == product.analyze.get_gravity_center() and
                (246.46031165305178, 137.67448741239653, 0.0,
                 137.67448741239653, 337.7416949626834, 0.0,
                 0.0, 0.0, 502.5508200121834) == product.analyze.get_inertia()
        )


def test_attributes():
    with CATIADocHandler(cat_product) as handler:
        product = handler.document.product()

        attributes = ('(Product) Attributes... \n'
                      'File Name:             CF_TopLevelAssy.CATProduct\n'
                      'Name:                  CF_TopLevelAssy\n'
                      'Part Number:           CF_TopLevelAssy\n'
                      'Revision:              A\n'
                      'Definition:            This is the definition for TopLevelAssy\n'
                      'Nomenclature:          This is the nomenclature for TopLevelAssy\n'
                      'Description Instance:  \n'
                      'Description Reference: This is the description for TopLevelAssy\n'
                      'Reference:             Product(name="CF_TopLevelAssy")\n'
                      'Is CATProduct:         True\n'
                      'Is CATPart:            False')

        assert product.attributes() == attributes


def test_count_children():
    with CATIADocHandler(cat_product) as handler:
        product = handler.document.product()

        assert product.count_children() == 5


def test_definition():
    with CATIADocHandler(cat_part_measurable) as handler:
        part_product = handler.document.product()

        assert 'No defintion declared.' == part_product.definition

        part_product.definition = 'new definition'

        assert 'new definition' == part_product.definition


def test_description_instance():
    with CATIADocHandler(cat_product) as handler:
        part_product = handler.document.product()
        children = part_product.get_children()
        child = children[0]

        assert 'Component Description of CF_SubProduct1.1' == child.description_instance

        new_instance_name = 'Component Description of CF_SubProduct11.1'
        child.description_instance = new_instance_name

        assert new_instance_name == child.description_instance


def test_description_reference():
    with CATIADocHandler(cat_product) as handler:
        part_product = handler.document.product()
        children = part_product.get_children()
        child = children[0]

        assert 'This is the definition for CF_SubProduct1' == child.description_reference

        new_description_reference = 'This is the definition for CF_SubProduct1 2'
        child.description_reference = new_description_reference

        assert new_description_reference == child.description_reference


def test_file_name():
    with CATIADocHandler(cat_part_measurable) as handler:
        part_product = handler.document.product()

        assert cat_part_measurable.name == part_product.file_name


def test_full_name():
    with CATIADocHandler(cat_part_measurable) as handler:
        part_product = handler.document.product()

        assert str(cat_part_measurable) == part_product.full_name


def test_get_child():
    with CATIADocHandler(cat_product) as handler:
        product = handler.document.product()
        child = product.get_child(0)
        assert child.part_number == 'CF_SubProduct1'


def test_get_products():
    with CATIADocHandler(cat_product) as handler:
        product = handler.document.product()
        products = product.get_products()

        assert 'Product(name="CF_SubProduct1.1")' == products[0].__repr__()


def test_has_children():
    with CATIADocHandler(cat_product) as handler:
        product = handler.document.product()

        assert product.has_children()

    with CATIADocHandler(cat_part_measurable) as handler:
        part_product = handler.document.product()

        assert not part_product.has_children()


def test_is_catproduct_is_catpart():
    with CATIADocHandler(cat_product) as handler:
        product = handler.document.product()

        assert product.is_catproduct()
        assert not product.is_catpart()

    with CATIADocHandler(cat_part_measurable) as handler:
        part = handler.document.product()

        assert part.is_catpart()
        assert not part.is_catproduct()


def test_move():
    with CATIADocHandler(cat_product) as handler:
        product = handler.document.product()

        product.apply_work_mode(cat_work_mode_type.index("DESIGN_MODE"))

        transformation = (
            1.000,
            0,
            0,
            0,
            0.707,
            0.707,
            0,
            -0.707,
            0.707,
            10.000,
            20.000,
            30.000
        )

        Product.activate_terminal_node(product.get_products())
        # move the first child in parent.
        product = product.get_products()[0]

        product.move.apply(transformation)

        assert ((65.41613484215364, 0.0, 0.0,
                 0.0, 68.97147661807078, -13.970786852103165,
                 0.0, -13.970786852103165, 68.97147661807078) == product.analyze.get_inertia())


def test_name():
    with CATIADocHandler(cat_part_measurable) as handler:
        part_product = handler.document.product()

        assert 'CF_catia_measurable_part' == part_product.name


def test_nomenclature():
    with CATIADocHandler(cat_part_measurable) as handler:
        part_product = handler.document.product()

        assert 'Test Part' == part_product.nomenclature

        new_nomenclature = 'New Test Part'

        part_product.nomenclature = new_nomenclature

        assert new_nomenclature == part_product.nomenclature


def test_part_number():
    with CATIADocHandler(cat_part_measurable) as handler:
        part_product = handler.document.product()

        assert 'CF_catia_measurable_part' == part_product.part_number

        part_product.part_number = 'new_part_number'

        assert 'new_part_number' == part_product.part_number


def test_path():
    with CATIADocHandler(cat_part_measurable) as handler:
        part_product = handler.document.product()

        product_path = Path(os.getcwd(), cat_part_measurable)

        assert product_path == part_product.path()


def test_position():
    # todo: write test feature
    pass


def test_proudcts():
    # todo: write test feature
    pass


def test_publications():
    # todo: write test feature
    pass


def test_reference_product():
    with CATIADocHandler(cat_product) as handler:
        part_product = handler.document.product()

        assert part_product.reference_product.name == 'CF_TopLevelAssy'


def test_relations():
    # todo: write test feature.
    pass


def test_revision():
    with CATIADocHandler(cat_part_measurable) as handler:
        part_product = handler.document.product()

        assert 'A' == part_product.revision

        part_product.revision = 'B'

        assert 'B' == part_product.revision


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


def test_repr():
    with CATIADocHandler(cat_part_measurable) as handler:
        part = handler.document.product()

        assert 'Product(name="CF_catia_measurable_part")' == part.__repr__()
