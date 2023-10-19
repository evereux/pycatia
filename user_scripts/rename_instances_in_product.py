#! /usr/bin/python3.9
# author: evereux
# contact: evereux@gmail.com

"""
    Rename Instances In Product

    Description
    ===========
    Renames the instances of the children of the selected product.

    When the script is run the user is prompted to select a product within
    their product tree.

    The script will only rename child products of the selected product. It will
    not traverse the product any deeper.

    Requirements
    ============
    python >= 3.9
    pycatia
    CATIA V5 running with your product open.

"""
##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

import random
import string

from pycatia import catia
from pycatia.cat_logger import create_logger
from pycatia.in_interfaces.application import Application
from pycatia.in_interfaces.document import Document
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.products import Products


def tmp_string(size=6, chars: str = string.ascii_letters) -> str:
    """

    :param size:
    :param chars:
    :return:
    """
    return ''.join(random.choice(chars) for _ in range(size))


def message_box(_caa: Application):
    """

    :param Application _caa:
    :return:
    """
    mb = _caa.message_box('Please select product whose children\'s instances you would '
                          'like renaming sequentially.',
                          buttons=1,
                          title='Select Product.')
    if mb == 2:  # 2 = Cancel button pressed. 1 = OK button pressed.
        logger.info('You have cancelled the script!\nExiting ...')
        sys.exit()


def get_selected_item(_document: Document):
    selection = _document.selection
    selection.clear()

    message_box(caa)

    message = 'Please select a Product.'
    logger.info(message)
    filter_ = ('Product',)

    try:
        selection.select_element2(
            filter_,
            message,
            True
        )
    except KeyboardInterrupt:
        # for cases when the use hits escape during selection.
        logger.info('Selection exited.')

    sel_item = selection.item2(1)

    return sel_item


def rename_products(
        reference_products: Products,
        tmp_name: str or False = False
):
    """

    :param Products reference_products:
    :param str or False tmp_name:
    :return:
    """
    collection_counter = {}
    for product in reference_products:
        part_number = product.part_number
        keys = collection_counter.keys()
        if part_number not in keys:
            collection_counter[part_number] = 1
        else:
            collection_counter[part_number] += 1
        new_name = part_number
        if tmp_name:
            new_name = new_name + '.' + tmp_name
        new_name = new_name + '.' + str(collection_counter[part_number])
        product.name = new_name


if __name__ == '__main__':
    logger = create_logger()

    caa = catia()
    document = caa.active_document

    selected_item = get_selected_item(document)

    # Get the reference product from the selected item
    reference = selected_item.reference
    value = selected_item.value
    product = Product(value.com_object)
    ref_product = product.reference_product

    ref_products = ref_product.products
    if ref_products.count == 0:
        logger.info('Product has no children. Exiting script.')
        sys.exit()

    tmp_str = tmp_string()

    # We need to run this function twice.
    # The first time renames the instances with temporary names.
    rename_products(ref_products, tmp_str)
    rename_products(ref_products)
