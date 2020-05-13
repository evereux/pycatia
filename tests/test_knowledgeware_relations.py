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

        assert relations.count() == 6


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
    # todo: add text fixture.
    pass
