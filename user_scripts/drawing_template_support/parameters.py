#! /usr/bin/python3.8

from pywintypes import com_error

from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.knowledge_interfaces.parameters import Parameters

from .settings import parameters


def create_parameters(drawing: DrawingDocument) -> Parameters:
    """

    :param drawing:
    :return:
    """

    drawing_parameters = drawing.parameters

    existing_parameters = drawing_parameters.all_parameters()

    for param in parameters:
        # if the method get_item fails, capture the exception and add the parameter.
        try:
            # see if the parameter already exists
            if drawing_parameters.get_item(f'Drawing\{param}'):
                pass
                # print(f'Parameter {param} already exists.')
        except com_error:
            drawing_parameters.create_string(param, parameters[param])

    return drawing.parameters
