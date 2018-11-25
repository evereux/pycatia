#! /user/bin/python36


def create_reference(com_part, catia_object):
    """

    :param com_part:
    :param catia_object:
    :return:
    """
    return com_part.CreateReferenceFromObject(catia_object)


def create_measurable(spa_workbench, com_reference):
    """

    :param spa_workbench:
    :param com_reference:
    :return:
    """

    return spa_workbench.GetMeasurable(com_reference)
