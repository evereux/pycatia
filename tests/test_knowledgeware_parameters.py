#! /usr/bin/python3.6

from pycatia.base_interfaces import CATIADocHandler
from pycatia.knowledge_interfaces import Parameters
from pycatia.knowledge_interfaces import BoolParam
from pycatia.knowledge_interfaces import IntParam
from pycatia.knowledge_interfaces import StrParam
from pycatia.knowledge_interfaces import RealParam
from tests.source_files import cat_part_3
from tests.source_files import cat_part_blank
from tests.source_files import cat_part_temp


def test_parameters_name():
    with CATIADocHandler(cat_part_3) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)

        first_parameter = parameters.item(0)

        assert first_parameter.name == r'CF_Part3\PartBody\Pad.1\FirstLimit\Length'


def test_all_parameters():
    with CATIADocHandler(cat_part_3) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)

        all_parms = parameters.all_parameters()

        assert all_parms[0].name == r'CF_Part3\PartBody\Pad.1\FirstLimit\Length'


def test_create_boolean():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)

        new_boolean_parm = parameters.create_boolean('new_boolean', True)

        assert new_boolean_parm.name == r'CF_Part_Blank\new_boolean'
        assert new_boolean_parm.value == True


def test_create_dimension():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)

        new_dimension_parm = parameters.create_dimension('new_dimension', "length", 30.1)

        assert new_dimension_parm.name == r'CF_Part_Blank\new_dimension'
        assert new_dimension_parm.value == 30.1


def test_create_int():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)

        new_int_parm = parameters.create_integer('new_int', 30)

        assert new_int_parm.name == r'CF_Part_Blank\new_int'
        assert new_int_parm.value == 30


def test_create_list():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)

        new_list = parameters.create_list('new_list')

        assert new_list.name == r'new_list'


def test_count_parameters():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)

        assert parameters.count_parameters() == 5


def test_create_real():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)

        new_list = parameters.create_real('new_real', 5.4)

        assert new_list.name == r'CF_Part_Blank\new_real'
        assert new_list.value == 5.4


def test_create_parameters_set():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)
        root_parameter_set = parameters.root_parameter_set

        new_parm_set = parameters.create_set_of_parameters(root_parameter_set)

        assert new_parm_set.__repr__() == 'ParameterSet()'


def test_create_string():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)

        new_string = parameters.create_string('new_string', "this is a string")

        assert new_string.name == r'CF_Part_Blank\new_string'
        assert new_string.value == "this is a string"


def test_get_name_to_use_in_relation():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)

        new_string = parameters.create_string('new_string', "this is a string")
        name_to_use = parameters.get_name_to_use_in_relation(new_string)

        assert name_to_use == 'new_string'


def test_has_parameters():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)

        assert parameters.has_parameters() > 0


def test_item():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)
        bool_param = parameters.create_boolean('new_boolean', True)
        int_param = parameters.create_integer('new_integer', 10)
        str_param = parameters.create_string('new_string', 'new_value')
        real_param = parameters.create_real('new_real', 10.1)

        assert type(bool_param) == BoolParam
        assert type(int_param) == IntParam
        assert type(str_param) == StrParam
        assert type(real_param) == RealParam


def test_sub_list():
    with CATIADocHandler(cat_part_3) as handler:
        document = handler.document
        part = document.part()
        body = part.get_body_by_name('PartBody')
        pad = body.Shapes.Item('Pad.1')
        parameters = Parameters(part.part.Parameters)
        sub_list = parameters.sub_list(pad, True)

        assert sub_list.Item(1).Name == r'CF_Part3\PartBody\Pad.1\FirstLimit\Length'


def test_remove_item():
    with CATIADocHandler(cat_part_blank) as handler:
        document = handler.document
        part = document.part()
        parameters = Parameters(part.part.Parameters)

        bool_name = 'new-boolean'

        new_bool_param = parameters.create_boolean(bool_name, True)
        all_params = parameters.all_parameters
        index = None
        for i, p in enumerate(all_params()):
            if bool_name in p.name:
                index = i
        assert isinstance(index, int)

        parameters.remove_item(index)
        gone = any(bool_name in x.name for x in all_params())

        assert gone is False
