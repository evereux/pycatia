from typing import Union

from pycatia.knowledge_interfaces.bool_param import BoolParam
from pycatia.knowledge_interfaces.free_parameter import FreeParameter
from pycatia.knowledge_interfaces.int_param import IntParam
from pycatia.knowledge_interfaces.list_parameter import ListParameter
from pycatia.knowledge_interfaces.parameter import Parameter
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
