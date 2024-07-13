#! /usr/bin/python3.9

"""

    Example - Document - 002

    Description:
        Open all CATParts in source directory and save to IGS in target directory.

    Requirements:
        - CATIA running.
        - Tests already setup.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

from pycatia.mec_mod_interfaces.part_document import PartDocument

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

import os
from pathlib import Path

from pycatia import CATIADocHandler
from pycatia.in_interfaces.document import Document

# make these directories the full pathname.
source_directory = "tests/cat_files"
target_directory = "__junk__"

# if full paths are supplied above you should not do this.
source_directory = Path(Path(os.getcwd()).parent, source_directory)
target_directory = Path(Path(os.getcwd()).parent, target_directory)

# This loop assumes there are NO sub-directories.
for root, dirs, files in os.walk(source_directory):
    for file in files:
        print(f'Processing "{file}".')
        # only convert CATParts.
        if os.path.splitext(file)[1] == ".CATPart":
            # create filename with path.
            file_name = os.path.join(source_directory, file)

            with CATIADocHandler(file_name) as caa:
                file_ext = "igs"
                part_document: PartDocument = caa.document

                # create the full name of the target file, minus extension.
                target_file = Path(target_directory, os.path.splitext(file)[0] + "." + file_ext)

                # create the igs file in the __junk__ directory.
                part_document.export_data(target_file, file_ext, overwrite=True)
