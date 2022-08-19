#! /usr/bin/python3.6

"""

    Example - Asssembly Convetor - 001

    Print the BOM of a product to XLS using the inbuilt AssemblyConvertor. You
    must already have excel installed.

    This can also be used to create TXT and HTML files.

    See github issue https://github.com/evereux/pycatia/issues/110 with regards
    to file paths and saying "No" to overwriting existing files and file paths
    when using excel. These issues are mitigated using the code below by
    checking for an existing excel file and removing it and also using pythons
    pathlib.Path module.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################
from pathlib import Path

from pycatia import catia
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.assembly_convertor import AssemblyConvertor

# file_type can be "TXT", "HTML" or "XLS".
file_type = "XLS"
# full path to excel file.
# use pathlib.Path to prevent path related errors. See github link above.
excel_file = Path("C:\\Users\\evereux\\Desktop\\my_bom.xls")

# check that the parent folder exists
if not excel_file.parent.is_dir():
    raise NotADirectoryError(f'Directory "{excel_file.parent}" doesn\'t exist')

# check if the file already exists. I recommend doing this in python for two
# reasons ....
# 1. If the file already exists the script will stop running awaiting user
# input in window pop up. This may not be desirable.
# 2. If you press "No" to overwrite subsequent runs of script will generate
# errors until CATIA is restarted.
# see github link above for more information.
# !! this will delete excel file if it exists !!
if excel_file.is_file():
    os.remove(excel_file)


caa = catia()
document = caa.active_document
product = document.product
# not neccessary but will provide autocompletion in IDEs.
product = Product(product.com_object)

bom = product.get_item("BillOfMaterial")
assembly_convertor = AssemblyConvertor(bom.com_object)

details_top = ("Quantity", "Part Number", "Type", "Nomenclature", "Revision")
details_recap = ("Quantity", "Part Number")
assembly_convertor.set_current_format(details_top)
assembly_convertor.set_secondary_format(details_recap)

assembly_convertor.print(file_type, excel_file, product)


