#! /usr/bin/python3.9
import pytest

from pycatia.mec_mod_interfaces.part_document import PartDocument
from tests.conftest import application
from tests.source_files import cat_part_measurable
from tests.source_files import design_table_1


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_count(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    relations = part.relations

    assert relations.count == 4


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_create_check(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters

    lower_mass = parameters.create_dimension("lower_mass", "MASS", 5)
    lm_name = parameters.get_name_to_use_in_relation(lower_mass)

    upper_mass = parameters.create_dimension("upper_mass", "MASS", 10)
    um_name = parameters.get_name_to_use_in_relation(upper_mass)

    relations = part.relations
    new_check = relations.create_check("mass-check", "this is the comment", f"{lm_name}<{um_name}")

    assert new_check.name == "mass-check"


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_create_design_table(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    relations = part.relations

    design_table = relations.create_design_table("new-design-table", "this is a comment", True, design_table_1)

    assert design_table.name == "new-design-table"


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_create_formula(document_open):
    name = "new-formula"
    comment = "this is a comment"

    part_document: PartDocument = application.active_document
    part = part_document.part

    parameters = part.parameters

    lower_mass = parameters.create_dimension("lower_mass", "MASS", 5)
    lm_name = parameters.get_name_to_use_in_relation(lower_mass)

    upper_mass = parameters.create_dimension("upper_mass", "MASS", 10)
    um_name = parameters.get_name_to_use_in_relation(upper_mass)

    target_parm = parameters.create_dimension("target_mass", "MASS", 0)

    relations = part.relations

    formula = relations.create_formula(name, comment, target_parm, f"{lm_name}+{um_name}")

    assert formula.name == "new-formula"


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_create_horizontal_design_table(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    relations = part.relations

    design_table = relations.create_horizontal_design_table(
        "new-design-table", "this is a comment", True, str(design_table_1)
    )

    assert design_table.name == "new-design-table"


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_create_law(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    relations = part.relations

    law = relations.create_law("new-law", "this is a comment", "/* code comments */")

    assert law.name == "new-law"


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_create_program(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    relations = part.relations

    program = relations.create_program("new-program", "this is a comment", "/* code comments */")

    assert program.name == "new-program"


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_create_rule_base(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    relations = part.relations

    rule_base = relations.create_rule_base("new-rule-base")

    assert rule_base.name == "new-rule-base"


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_create_set_of_equations(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters
    relations = part.relations

    dim_b = parameters.create_real("dim_b", 1.2)
    dim_b_name = parameters.get_name_to_use_in_relation(dim_b)
    result = parameters.create_real("result", 0)

    eq_set = relations.create_set_of_equations("new-eq-set", "some comment", f"{result}=={dim_b_name} + 4;")

    assert eq_set.name == "new-eq-set"


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_create_set_of_relations(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    relations = part.relations
    relations.create_set_of_relations(part)

    assert relations.name == "Relations"


# @pytest.mark.parametrize('file_name', [cat_part_measurable])
# def test_relations_generate_xml():
#     pass
#     todo: this test fails.
#
#     xml_name = Path(os.getcwd(), 'testxml.xml')
#     with CATIADocHandler(cat_part_3) as caa:
#         document = caa.document
#         part = PartDocument(document.com_object).part
#
#         parameters = part.parameters
#
#         lower_mass = parameters.create_dimension('lower_mass', 'MASS', 5)
#         lm_name = parameters.get_name_to_use_in_relation(lower_mass)
#
#         upper_mass = parameters.create_dimension('upper_mass', 'MASS', 10)
#         um_name = parameters.get_name_to_use_in_relation(upper_mass)
#
#         relations = part.relations
#         relations.create_check('mass-check', 'this is the comment', f"{lm_name}<{um_name}")
#
#         relations.generate_xml_report_for_checks(str(xml_name))
#
#         assert xml_name.is_file()


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_get_items(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part

    relations = part.relations
    items = relations.items()

    assert len(items) == 12


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_get_item_by_index(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part

    relations = part.relations
    item = relations.get_item_by_index(1)

    assert item.name == "formula_1"


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_get_item_names(document_close_all_open):
    part_document: PartDocument = application.active_document
    part = part_document.part

    relations = part.relations
    item_names = relations.get_item_names()

    ref_names = ["formula_1", "formula_2", "formula_3", "formula_5"]
    assert item_names == ref_names


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_item(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part

    relations = part.relations
    relation = relations.item(1)
    assert relation.name == "formula_1"


def test_relations_sub_list():
    # todo: add test fixture
    pass


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_relations_remove(document_open_test_close):
    part_document: PartDocument = application.active_document
    part = part_document.part

    relations = part.relations
    relation = relations.item(1)
    assert relation.name == "formula_1"

    relations.remove(1)
    relation = relations.item(1)
    assert relation.name != "formula_1"
