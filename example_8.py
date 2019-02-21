#! /usr/bin/python3.6

"""

    Example 8:

    Use the context manager to open CATIA documents and close.

    CATIA must already be running.

"""

import os

from pycatia import CATIADocHandler

# make these directories the full pathname.
source_directory = 'tests'
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

            with CATIADocHandler(file_name) as handler:
                document = handler.document
                # create the full name of the target file, minus extension.
                target_file = os.path.join(target_directory, os.path.splitext(file)[0])
                # create the igs file in the __junk__ directory.
                document.export_data(target_file, 'igs')
