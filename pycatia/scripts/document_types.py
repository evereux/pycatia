from pycatia.exception_handling import CATIAApplicationException

allowed_document_types = {
    'part': 'Part',
    'product': 'Product',
    'drawing': 'Drawing',
    'functionalsystem': 'FunctionalSystem',
}


def get_document_type(dt: str) -> str:
    """

    This allows some flexibility regarding use of case.

    :Example - Add new document:

        >>> from pycatia import catia
        >>> caa = catia()
        >>> new_part = caa.documents.add('part')

        # this would be the same as

            :Example - Add new document:

        >>> from pycatia import catia
        >>> caa = catia()
        >>> new_part = caa.documents.add('Part')

    :param str dt:
    :return: str
    """
    if dt.lower() not in allowed_document_types:
        raise CATIAApplicationException(f'"{dt}" is not currently supported.')

    return allowed_document_types[dt.lower()]
