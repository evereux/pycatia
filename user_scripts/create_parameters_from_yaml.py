#! /usr/bin/python3.9
# author: evereux
# contact: evereux@gmail.com
# date:

"""

    Description
    ===========
    Reads the contents of a yaml file from which parameters and parameter sets
    are created.

    Not all parameter types are supported. Adding support for additional
    parameter types is fairly straight forward. See the function
    create_parameters().

    Requirements
    ============
    python >= 3.9
    pycatia
    pyyaml (pip install pyyaml)
    CATIA V5 running
    A valid YAML file for this script.

    YAML Structure
    ==============

    Your YAML file must be constructed thus:

    parameters:
      MaxDepth: # parameter name
        type: Length # parameter type
        value: 5 # value
      MinDepth: # parameter name
        type: Length # parameter type
        value: 3 # value
    sets:
      HorizontalStiffeners: # set name
        sets: # append new sets to parent HorizontalStiffeners
          Other: # set name
            parameters:
              Temp:
                type: Real
                value: 55
        parameters:
          UpperThickness:
            type: Length
            value: 5
          UpperHeight:
            type: Length
            value: 5


"""
##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pathlib import Path

import yaml

from pycatia import catia
from pycatia.knowledge_interfaces.parameter_set import ParameterSet
from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.mec_mod_interfaces.part import Part
from pycatia.product_structure_interfaces.product import Product

f = Path(os.getcwd(), 'user_scripts', 'create_parameters_from_yaml_support', 'parameters.yaml')

caa = catia()
application = caa.application
documents = application.documents
new_part = documents.add('Part').com_object
document = application.active_document

product = Product(document.product.com_object)
part = Part(document.part.com_object)


def get_yaml_file(yaml_file: Path) -> dict:
    """

    :param yaml_file:
    :return:
    """
    with open(yaml_file) as file:
        ps = yaml.safe_load(file)

    return ps


def create_parameters(parameters: Parameters, items: dict):
    """

    :param Parameters parameters:
    :param dict items:
    :return:
    """
    for parameter in items:
        name = parameter
        type_ = items[name]['type']
        value = items[name]['value']
        dimension_parameter_types = ['Length', 'Angle', 'Mass']
        if type_ in dimension_parameter_types:
            parameters.create_dimension(name, type_, value)
        if type_ == 'Real':
            parameters.create_real(name, value)
        if type_ == 'Bool':
            parameters.create_boolean(name, value)
        if type_ == 'String':
            parameters.create_string(name, value)


def do_the_loop(d: dict, parameter_parent: ParameterSet):
    """

    :param dict d:
    :param ParameterSet parameter_parent:
    :return:
    """
    for i in d:
        if i == "parameters":
            parameters_ = parameter_parent.direct_parameters
            create_parameters(parameters_, d[i])
        if i == 'sets':
            set_names = [k for k in d[i]]
            # create the set
            for name in set_names:
                p_set: ParameterSet = parameter_parent.parameter_sets.create_set(name)
                do_the_loop(d[i][name], p_set)


parameter_dict = get_yaml_file(f)
parameter_root = part.parameters.root_parameter_set
do_the_loop(parameter_dict, parameter_root)
