#! /usr/bin/python3.6

"""

    Example 8:

    Open all CATParts in source directory and save to IGS in target directory.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

import os

from pycatia import CATIADocHandler

# make these directories the full pathname.
source_directory = 'tests/cat_files'
target_directory = '__junk__'

# if full paths are supplied above you should not do this.
source_directory = os.path.join(os.getcwd(), source_directory)
target_directory = os.path.join(os.getcwd(), target_directory)

# This loop assumes there are NO sub-directories.
for root, dirs, files in os.walk(source_directory):

    for file in files:

        # only convert CATParts.
        if os.path.splitext(file)[1] == '.CATPart':
            # create filename with path.
            file_name = os.path.join(source_directory, file)

            with CATIADocHandler(file_name) as caa:
                document = caa.document
                # create the full name of the target file, minus extension.
                target_file = os.path.join(target_directory, os.path.splitext(file)[0])
                # create the igs file in the __junk__ directory.
                document.export_data(target_file, 'igs')
