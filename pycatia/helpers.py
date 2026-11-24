from typing import Any

from pycatia.types.hybrid_shapes import hybrid_shape_types
from pycatia.types.shapes import shape_types
from pycatia.types.bodies import body_types
from pycatia.types.parameters import parameter_and_relation_types


def return_real_object(application: 'Application', any_object: 'AnyObject') -> Any:
    TypeName = application.vba_type_name

    type_string = TypeName(any_object)

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
