# author: evereux
# contact: evereux@gmail.com

"""

    Save Child Parts To STP


    Description
    ===========

    Saves all CATParts within a CATProduct to STP to the directory C:\temp.

    If the STP file already exists, it will be overwritten.

    Warning: Please be aware that the entire product will be put into design mode.
    For extremely large assemblies you should be conscious of running into memory
    issues.


    Requirements
    ============

    python >= 3.9
    pycatia
    CATIA V5 running with a CATProduct open containing CATParts.


    Documentation
    =============

    https://pycatia.readthedocs.io

    More examples and user scripts can be found at:
    https://github.com/evereux/pycatia/tree/master/examples
    https://github.com/evereux/pycatia/tree/master/user_scripts

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pathlib import Path

from pycatia import catia, CatWorkModeType
from pycatia.product_structure_interfaces.product_document import ProductDocument

if __name__ == "__main__":

    target_folder = Path(r"C:\temp")
    if not target_folder.exists():
        raise FileNotFoundError("The target folder does not exist. Please create it.")

    application = catia()
    product_document: ProductDocument = application.active_document

    if not type(product_document) == ProductDocument:
        print("A CATProduct document must be the active document.")
        sys.exit()

    product = product_document.product
    product.activate_terminal_node(product.products)
    # put the product in design mode.
    product.apply_work_mode(CatWorkModeType.DESIGN_MODE)

    # get all the CATParts from the document collection object.
    part_documents = [catpart for catpart in application.documents if catpart.name.endswith('.CATPart')]

    for part_document in part_documents:
        file_type = 'stp'
        stp_name = Path(target_folder, part_document.name.rsplit('.', 1)[0] + f'.{file_type}')
        print('Saving STP to ' + str(stp_name))
        part_document.export_data(stp_name, file_type, overwrite=True)
