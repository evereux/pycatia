# ! /usr/bin/python3.6

def check_type(object_, type_):
    """
    
    Function to check the object type and raise an error if the wrong expected type is supplied.

    :param object_: Any python object.
    :param type_: Any python or pycatia type.
    """

    if not isinstance(object_, type_):
        raise TypeError(f'Wrong type. Expected type {type_}.')

    pass
