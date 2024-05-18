from pycatia.exception_handling import CATIAApplicationException

allowed_document_types = {
    # 'catimmnavdoc': 'CATImmNavDoc', this wouldn't work for me
    'analysis': 'Analysis',
    'catalogdocument': 'CatalogDocument',
    'catmaterial': 'CATMaterial',
    'material': 'CATMaterial',
    'catprocess': 'CATProcess',
    'process': 'CATProcess',
    'cgm': 'cgm',
    'drawing': 'Drawing',
    'featuredictionary': 'FeatureDictionary',
    'gl': 'gl',
    'gl2': 'gl2',
    'hpgl': 'hpgl',
    'functionalsystem': 'FunctionalSystem',
    'part': 'Part',
    'product': 'Product',
    'processlibrary': 'ProcessLibrary',
}


def get_document_type(dt: str) -> str:
    """

    This allows some flexibility regarding use of case.

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
