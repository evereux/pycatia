#! /usr/bin/python3.9

"""

    Example - Assembly Convertor - 001

    Description:
        Print the BOM of a product to XLS using the inbuilt AssemblyConvertor.
        This can also be used to create TXT and HTML files.

    Requirements:
        - An open product document with parts inside.
        - MS EXCEL must be installed.

    Further information:
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

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################
from pathlib import Path

from pycatia import catia
from pycatia.product_structure_interfaces.assembly_convertor import AssemblyConvertor
from pycatia.product_structure_interfaces.product_document import ProductDocument

# file_type can be "TXT", "HTML" or "XLS".
file_type = "XLS"

caa = catia()
product_document: ProductDocument = caa.active_document
product = product_document.product

bom = product.get_item("BillOfMaterial")
assembly_convertor = AssemblyConvertor(bom.com_object)

details_top = ("Quantity", "Part Number", "Type", "Nomenclature", "Revision")
details_recap = ("Quantity", "Part Number")
# Note: Keep in mind that CATIA is language based when it comes to the bill of material format.
# So 'Part Number' in english will become 'Teilenummer' in german, and so on.
assembly_convertor.set_current_format(details_top)
assembly_convertor.set_secondary_format(details_recap)

# Define the absolute path for the excel file.
# In this example the excel file will be saved to the same folder as the product,
# from which the bill of material is created. The excel file will also have the
# same name as the product.
excel_path = Path(product.path().parent, product.name + ".xls")

# check if the file already exists. I recommend doing this in python for two
# reasons ....
# 1. If the file already exists the script will stop running awaiting user
# input in window pop up. This may not be desirable.
# 2. If you press "No" to overwrite subsequent runs of script will generate
# errors until CATIA is restarted.
# see github link above for more information.
# !! this will delete excel file if it exists !!
if excel_path.is_file():
    os.remove(excel_path)

assembly_convertor.print(file_type, excel_path, product)
# Important note:
# The print-method will fail if you try to export the bill-of-material-xls file
# to a location, where another process will access this file. Such process is
# for example OneDrive or Dropbox.
# One solution to avoid this problem is to export the bom to the current users
# temp folder and then move it to the desired destination using shutil.move(),
# see https://docs.python.org/3/library/shutil.html#shutil.move
# To this particular problem:
# Once the print-method had failed, it will continue to fail until you restart
# CATIA, even if you've changed the path to a 'save' location.
