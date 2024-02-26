from typing import TypeVar, Type

from pycatia.knowledge_interfaces.bool_param import BoolParam
from pycatia.knowledge_interfaces.int_param import IntParam
from pycatia.knowledge_interfaces.str_param import StrParam
from pycatia.knowledge_interfaces.real_param import RealParam


"""
This is a doc comment.
"""

#: cat_variant The cat_variant type allows both int and string.
cat_variant = TypeVar('cat_variant', int, str)
list_str = TypeVar('list_str', list, str)
any_parameter = TypeVar('any_parameter', BoolParam, IntParam, StrParam, RealParam)

