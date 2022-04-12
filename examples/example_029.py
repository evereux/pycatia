#! /usr/bin/python3.6

"""

    Example 29

    Print the BOM of a product to XLS using the inbuilt AssemblyConvertor.

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
excel_file = Path("C:\\Users\\evereux\\Desktop\\my_bom.xls")

caa = catia()
document = caa.active_document
product = document.product

bom = product.get_item("BillOfMaterial")
assembly_convertor = AssemblyConvertor(bom.com_object)

details_top = ("Quantity", "Part Number", "Type", "Nomenclature", "Revision")
details_recap = ("Quantity", "Part Number")
assembly_convertor.set_current_format(details_top)
assembly_convertor.set_secondary_format(details_recap)

assembly_convertor.print(file_type, excel_file, product)


