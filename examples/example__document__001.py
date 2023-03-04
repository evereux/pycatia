#! /usr/bin/python3.9

"""

    Example - Document - 001:

    Use the context manager to open CATIA documents and close

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

import time

from pycatia import CATIADocHandler

catia_part = r'tests\cat_files\part_measurable.CATPart'

with CATIADocHandler(catia_part) as caa:
    document = caa.document
    # do some stuff.
    # save if you need to.
    time.sleep(5)  # don't do this, no need.
    # document is automatically closed. Lovely.
