#! /usr/bin/python3.6

from pycatia import CATIADocHandler

cat_part = r'tests/CF_catia_measurable_part.CATPart'
cat_product = r'tests/CF_TopLevelAssy.CATProduct'


def test_repr():
    with CATIADocHandler(cat_part) as handler:
        part = handler.document.product()

        assert '(Product) part_number: CF_catia_measurable_part, file_name: CF_catia_measurable_part.CATPart' == part.__repr__()


def test_name():
    with CATIADocHandler(cat_part) as handler:
        part_product = handler.document.product()

        assert 'CF_catia_measurable_part' == part_product.name


def test_file_name():
    with CATIADocHandler(cat_part) as handler:
        part_product = handler.document.product()

        assert 'CF_catia_measurable_part.CATPart' == part_product.file_name


def test_part_number():
    with CATIADocHandler(cat_part) as handler:
        part_product = handler.document.product()

        assert 'CF_catia_measurable_part' == part_product.part_number

        part_product.part_number = 'new_part_number'

        assert 'new_part_number' == part_product.part_number


def test_revision():
    with CATIADocHandler(cat_part) as handler:
        part_product = handler.document.product()

        assert 'A' == part_product.revision

        part_product.revision = 'B'

        assert 'B' == part_product.revision


def test_definition():
    with CATIADocHandler(cat_part) as handler:
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


def test_nomenclature():
    with CATIADocHandler(cat_part) as handler:
        part_product = handler.document.product()

        assert 'Test Part' == part_product.nomenclature

        new_nomenclature = 'New Test Part'

        part_product.nomenclature = new_nomenclature

        assert new_nomenclature == part_product.nomenclature


def test_reference_product():
    with CATIADocHandler(cat_product) as handler:
        part_product = handler.document.product()

        assert part_product.reference_product.name == 'CF_TopLevelAssy'


def test_is_catproduct_is_catpart():
    with CATIADocHandler(cat_product) as handler:
        product = handler.document.product()

        assert product.is_catproduct()
        assert not product.is_catpart()

    with CATIADocHandler(cat_part) as handler:
        part = handler.document.product()

        assert part.is_catpart()
        assert not part.is_catproduct()


def test_has_children():
    with CATIADocHandler(cat_product) as handler:
        product = handler.document.product()

        assert product.has_children()

    with CATIADocHandler(cat_part) as handler:
        part_product = handler.document.product()

        assert not part_product.has_children()


def test_get_products():
    with CATIADocHandler(cat_product) as handler:
        product = handler.document.product()
        products = product.get_products()

        assert '(Product) part_number: CF_SubProduct1, file_name: CF_SubProduct1.CATProduct' == products[0].__repr__()


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
                      'Reference:             <COMObject <unknown>>\n'
                      'Is CATProduct:         True\n'
                      'Is CATPart:            False')

        assert product.attributes() == attributes
