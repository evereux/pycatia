from typing import TypeVar, Type, Union

"""
This is a doc comment.
"""

#: CATVariant The CATVariant type allows both int and string.
CATVariant = Union[
    int, str
]

list_str = TypeVar('list_str', list, str)
