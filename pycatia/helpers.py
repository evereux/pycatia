from typing import Any, TYPE_CHECKING

from pycatia.types.hybrid_shapes import hybrid_shape_types
from pycatia.types.shapes import shape_types
from pycatia.types.bodies import body_types
from pycatia.types.parameters import parameter_and_relation_types
from pycatia.types.document import document_types

if TYPE_CHECKING:
    from pycatia.system_interfaces.any_object import AnyObject
    from pycatia.in_interfaces.application import Application


def return_real_object(application: 'Application', any_object: 'AnyObject') -> Any:
    TypeName = application.vba_type_name

    type_string = TypeName(any_object)

    if type_string in document_types:
        return document_types[type_string](any_object.com_object)

    if type_string in hybrid_shape_types:
        return hybrid_shape_types[type_string](any_object.com_object)

    if type_string in shape_types:
        return shape_types[type_string](any_object.com_object)

    if type_string in body_types:
        return body_types[type_string](any_object.com_object)

    if type_string in parameter_and_relation_types:
        return parameter_and_relation_types[type_string](any_object.com_object)

    # todo: add more types
    application.logger.info(
        f'Please add type string "{type_string}" to checks so correct type is returned.'
    )

    return any_object
