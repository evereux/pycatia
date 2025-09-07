#! /usr/bin/python3.9
import pytest

from pycatia.knowledge_interfaces.bool_param import BoolParam
from pycatia.knowledge_interfaces.int_param import IntParam
from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.knowledge_interfaces.str_param import StrParam
from pycatia.mec_mod_interfaces.body import Body
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.mec_mod_interfaces.shape import Shape
from tests.conftest import application
from tests.source_files import cat_part_measurable


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_parameters_name(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters

    first_parameter = parameters.item(1)

    assert first_parameter.name in [
        r"cat_part_measurable\PartBody\Pad.1\FirstLimit\Length",
        r"cat_part_measurable\Hauptkörper\Block.1\Begrenzung1\Länge",
    ]


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_all_parameters(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters

    all_parms = parameters.all_parameters()

    assert all_parms[0].name in [
        r"cat_part_measurable\PartBody\Pad.1\FirstLimit\Length",
        r"cat_part_measurable\Hauptkörper\Block.1\Begrenzung1\Länge",
    ]


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_create_boolean(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters

    new_boolean_parm = parameters.create_boolean("new_boolean", True)

    assert new_boolean_parm.name == rf"{part.name}\new_boolean"
    assert new_boolean_parm.value is True


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_create_dimension(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters

    new_dimension_parm = parameters.create_dimension("new_dimension", "length", 30.1)

    assert new_dimension_parm.name == rf"{part.name}\new_dimension"
    assert new_dimension_parm.value == 30.1


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_create_int(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters

    new_int_parm = parameters.create_integer("new_int", 30)

    assert new_int_parm.name == rf"{part.name}\new_int"
    assert new_int_parm.value == 30


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_create_list(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters

    new_list = parameters.create_list("new_list")

    assert new_list.name == r"new_list"


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_count_parameters(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters

    assert parameters.count == 117


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_create_real(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters

    new_list = parameters.create_real("new_real", 5.4)

    assert new_list.name == rf"{part.name}\new_real"
    assert new_list.value == 5.4


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_create_parameters_set(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters
    root_parameter_set = parameters.root_parameter_set
    parameters.create_set_of_parameters(root_parameter_set)
    parameter_sets = root_parameter_set.parameter_sets.items()
    assert parameter_sets[0].__repr__() in ['ParameterSet(name="Parameters.1")', 'ParameterSet(name="Parameter.1")']


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_create_string(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters

    new_string = parameters.create_string("new_string", "this is a string")

    assert new_string.name == rf"{part.name}\new_string"
    assert new_string.value == "this is a string"


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_get_name_to_use_in_relation(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters

    new_string = parameters.create_string("new_string", "this is a string")
    name_to_use = parameters.get_name_to_use_in_relation(new_string)

    assert name_to_use == "new_string.1"


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_has_parameters(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters

    assert parameters.has_parameters() > 0


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_item(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters
    bool_param = parameters.create_boolean("new_boolean", True)
    int_param = parameters.create_integer("new_integer", 10)
    str_param = parameters.create_string("new_string", "new_value")
    real_param = parameters.create_real("new_real", 10.1)

    assert type(bool_param) == BoolParam
    assert type(int_param) == IntParam
    assert type(str_param) == StrParam
    assert type(real_param) == RealParam


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_sub_list(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    body_item = part.main_body
    assert body_item is not None

    body = Body(body_item.com_object)
    shape_item = body.shapes.get_item_by_name("Pad.1") or body.shapes.get_item_by_name("Block.1")

    assert shape_item is not None

    shape = Shape(shape_item.com_object)
    parameters = part.parameters
    sub_list = parameters.sub_list(shape, True)
    assert sub_list.item(1).name in [
        r"cat_part_measurable\PartBody\Pad.1\FirstLimit\Length",
        r"cat_part_measurable\Hauptkörper\Block.1\Begrenzung1\Länge",
    ]


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_remove(document_open_test_close):
    part_document: PartDocument = application.active_document
    part = part_document.part
    parameters = part.parameters

    bool_name = "new-boolean"

    parameters.create_boolean(bool_name, True)
    all_params = parameters.all_parameters
    index = None
    # get all the parameters and find the index of the item called var name "bool_name".
    for i, p in enumerate(all_params()):
        if bool_name in p.name:
            # all calls to object.index() methods start at 1. so add 1.
            index = i + 1
    assert isinstance(index, int)

    parameters.remove(index)
    gone = any(bool_name in x.name for x in all_params())

    assert gone is False
