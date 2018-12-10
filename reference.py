#! /usr/bin/python3.6


def create_reference(com_part, catia_object):
    """

    :param com_part:
    :param catia_object:
    :return:
    """
    return com_part.CreateReferenceFromObject(catia_object)
