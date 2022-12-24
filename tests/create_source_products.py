import os
from pathlib import Path

from pywintypes import com_error

from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument
from tests.common_vars import caa
from tests.common_vars import test_files
from tests.create_source_parts import get_cat_part_measurable

source_cat_product = Path(os.getcwd(), test_files, "product_top.CATProduct")
source_cat_sub_1 = Path(os.getcwd(), test_files, "product_sub_1.CATProduct")
source_cat_sub_2 = Path(os.getcwd(), test_files, "product_sub_2.CATProduct")


def create_cat_products(file_name_top, file_name_sub_1, file_name_sub_2):
    documents = caa.documents

    # ####################### #
    # close all the documents #
    # ####################### #

    try:
        for document in documents.items():
            document.close()
    except com_error:
        # all documents must be closed.
        pass

    # ############################ #
    # Create the top level product #
    # ############################ #

    documents.add("Product")
    doc_root_prod = caa.active_document
    doc_root_prod.save_as(file_name_top)
    product_top = ProductDocument(doc_root_prod.com_object).product
    product_top.part_number = "cat_product_1"
    product_top.revision = "A.1"
    product_top.nomenclature = "pycatia product for testing"
    product_top.definition = "pycatia product for testing"

    products = product_top.products

    # ######################## #
    # Create the sub product 1 #
    # ######################## #

    documents.add("Product")
    doc_sub_1 = caa.active_document
    doc_sub_1.save_as(file_name_sub_1)
    product_sub_1 = ProductDocument(doc_sub_1.com_object).product
    product_sub_1.part_number = "cat_product_sub_1"
    product_sub_1.revision = "A.1"
    product_sub_1.nomenclature = "pycatia product for testing"

    products_sub_1 = product_sub_1.products
    cat_part_measurable = get_cat_part_measurable()
    documents.open(str(cat_part_measurable))
    doc_cat_part = PartDocument(caa.active_document.com_object)
    products_sub_1.add_component(doc_cat_part.product)

    doc_sub_1.save()

    # ######################## #
    # Create the sub product 2 #
    # ######################## #

    documents.add("Product")
    doc_sub_2 = caa.active_document
    doc_sub_2.save_as(file_name_sub_2)
    product_sub_2 = ProductDocument(doc_sub_2.com_object).product
    product_sub_2.part_number = "cat_product_sub_2"
    product_sub_2.revision = "A.1"
    product_sub_2.nomenclature = "pycatia product for testing"

    product_sub_2 = product_sub_2.products
    product_sub_2.add_component(doc_cat_part.product)

    doc_sub_2.save()

    # ########################### #
    # Add the sub products to top #
    # ########################### #

    products.add_component(product_sub_1)
    products.add_component(product_sub_1)
    products.add_component(product_sub_2)  # type: ignore

    # ################# #
    # Add new component #
    # ################# #

    # yes, the naming seems to arse backwards. ask Dassault why, not me. :-)
    products.add_new_product("ComponentReference")

    # ##################################################################### #
    # Add description instance text to the first product in the top product #
    # ##################################################################### #

    first_product = products.item(1)
    first_product.description_instance = "description instance text"

    doc_root_prod.save()

    # ####################### #
    # close all the documents #
    # ####################### #

    for document in documents.items():
        document.close()


def get_cat_product_top():
    if not source_cat_product.exists():
        caa.logger.info(f"Creating {source_cat_product}")
        create_cat_products(source_cat_product, source_cat_sub_1, source_cat_sub_2)
    return source_cat_product
