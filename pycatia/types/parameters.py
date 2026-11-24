from typing import Union

from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.bool_param import BoolParam
from pycatia.knowledge_interfaces.check import Check
from pycatia.knowledge_interfaces.design_table import DesignTable
from pycatia.knowledge_interfaces.dimension import Dimension
from pycatia.knowledge_interfaces.enum_param import EnumParam
from pycatia.knowledge_interfaces.formula import Formula
from pycatia.knowledge_interfaces.free_parameter import FreeParameter
from pycatia.knowledge_interfaces.int_param import IntParam
from pycatia.knowledge_interfaces.knowledge_activate_object import KnowledgeActivateObject
from pycatia.knowledge_interfaces.law import Law
from pycatia.knowledge_interfaces.length import Length
from pycatia.knowledge_interfaces.list import List
from pycatia.knowledge_interfaces.list_parameter import ListParameter
from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.knowledge_interfaces.rule import Rule
from pycatia.knowledge_interfaces.set_of_equation import SetOfEquation
from pycatia.knowledge_interfaces.str_param import StrParam
from pycatia.knowledge_interfaces.real_param import RealParam

AnyParameter = Union[
    BoolParam,
    FreeParameter,
    IntParam,
    ListParameter,
    Parameter,
    RealParam,
    StrParam,
]

parameter_and_relation_types = {
    'Angle': Angle,
    'BoolParam': BoolParam,
    'Check': Check,
    'DesignTable': DesignTable,
    'Dimension': Dimension,
    'EnumParam': EnumParam,
    'Formula': Formula,
    'IntParam': IntParam,
    'KnowledgeActivateObject': KnowledgeActivateObject,
    'Law': Law,
    'Length': Length,
    'List': List,
    'ListParameter': ListParameter,
    'Parameter': Parameter,
    'RealParam': RealParam,
    'Rule': Rule,
    'SetOfEquation': SetOfEquation,
    'StrParam': StrParam,
}
