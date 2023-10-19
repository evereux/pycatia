from pycatia.mec_mod_interfaces.part import Part
from pycatia.product_structure_interfaces.product import Product

from .constants import constants_length
from .constants import constants_angle
from .constants import constants_real


def create_parameters(part: Part, product: Product):
    """
    
    :param part: 
    :return: 
    """
    parameters = part.parameters

    for constant in constants_length:
        value = constants_length[constant]
        parameters.create_dimension(constant, 'Length', value)

    for constant in constants_angle:
        value = constants_angle[constant]
        parameters.create_dimension(constant, 'Angle', value)

    for constant in constants_real:
        value = constants_real[constant]
        parameters.create_real(constant, value)

    param_RATIO = parameters.get_item_by_name(f'{product.part_number}\\RATIO')
    relations = part.relations
    relations.create_formula("Formula.RATIO", "", param_RATIO, "`CHORD_LENGTH_WING_TIP`/`CHORD_LENGTH_ROOT`")

    return parameters
