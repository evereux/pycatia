#! /usr/bin/python3.6

from pycatia.base_interfaces import CATIADocHandler

from pycatia.knowledge_interfaces import Parameters
from pycatia.knowledge_interfaces import Relations
from tests.source_files import cat_part_3
from tests.source_files import cat_part_blank
from tests.source_files import cat_part_temp
from tests.source_files import design_table_1


def test_relations_count():
    with CATIADocHandler(cat_part_3) as handler:
        document = handler.document
        part = document.part()
        relations = Relations(part.relations_com_obj())

        assert relations.count == 6


def test_relations_create_check():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.parameters_com_obj())

        lower_mass = parameters.create_dimension('lower_mass', 'MASS', 5)
        lm_name = parameters.get_name_to_use_in_relation(lower_mass)

        upper_mass = parameters.create_dimension('upper_mass', 'MASS', 10)
        um_name = parameters.get_name_to_use_in_relation(upper_mass)

        relations = Relations(part.relations_com_obj())
        new_check = relations.create_check('mass-check', 'this is the comment', f"{lm_name}<{um_name}")

        assert new_check.name == 'mass-check'


def test_relations_create_design_table():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        relations = Relations(part.relations_com_obj())

        design_table = relations.create_design_table('new-design-table', 'this is a comment', True, design_table_1)

        assert design_table.name == 'new-design-table'


def test_relations_create_formula():
    with CATIADocHandler(cat_part_blank) as handler:
        name = "new-formula"
        comment = "this is a comment"

        document = handler.document
        part = document.part()

        parameters = Parameters(part.parameters_com_obj())

        lower_mass = parameters.create_dimension('lower_mass', 'MASS', 5)
        lm_name = parameters.get_name_to_use_in_relation(lower_mass)

        upper_mass = parameters.create_dimension('upper_mass', 'MASS', 10)
        um_name = parameters.get_name_to_use_in_relation(upper_mass)

        target_parm = parameters.create_dimension('target_mass', 'MASS', 0)

        relations = Relations(part.relations_com_obj())

        formula = relations.create_formula(name, comment, target_parm, f"{lm_name}+{um_name}")

        assert formula.name == 'new-formula'


def test_relations_create_horizontal_design_table():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        relations = Relations(part.relations_com_obj())

        design_table = relations.create_horizontal_design_table('new-design-table', 'this is a comment', True,
                                                                design_table_1)

        assert design_table.name == 'new-design-table'


def test_relations_create_law():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        relations = Relations(part.relations_com_obj())

        law = relations.create_law('new-law', 'this is a comment', '/* code comments */')

        assert law.name == 'new-law'


def test_relations_create_program():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        relations = Relations(part.relations_com_obj())

        program = relations.create_program('new-program', 'this is a comment', '/* code comments */')

        assert program.name == 'new-program'


def test_relations_create_rule_base():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        relations = Relations(part.relations_com_obj())

        rule_base = relations.create_rule_base('new-rule-base')

        assert rule_base.name == 'new-rule-base'


def test_relations_create_set_of_equations():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.parameters_com_obj())
        relations = Relations(part.relations_com_obj())

        dim_b = parameters.create_real("dim_b", 1.2)
        dim_b_name = parameters.get_name_to_use_in_relation(dim_b)
        result = parameters.create_real("result", 0)

        eq_set = relations.create_set_of_equations('new-eq-set', 'some comment', f'{result}=={dim_b_name} + 4;')

        assert eq_set.name == 'new-eq-set'


def test_relations_create_set_of_relations():
    # todo: add test fixture
    pass
    # with CATIADocHandler(cat_part_blank) as handler:
    #     document = handler.document
    #     part = document.part()
    #     relations = Relations(part.relations_com_obj())
    #     rel_set = relations.create_set_of_relations(relations.relations)
    #
    #     assert rel_set.relations.name == 'new-eq-set'


def test_relations_generate_xml():
    # todo: add test fixture
    pass


def test_relations_get_items():
    # todo: add test fixture
    pass


def test_relations_get_item_by_index():
    # todo: add test fixture
    pass


def test_relations_get_item_names():
    # todo: add test fixture
    pass


def test_relations_is_item():
    # todo: add test fixture
    pass


def test_relations_item():
    # todo: add test fixture
    pass


def test_relations_sub_list():
    # todo: add test fixture
    pass


def test_relations_remove():
    # todo: add test fixture
    pass
