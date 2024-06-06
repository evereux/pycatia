#! /usr/bin/python3.9

"""

    Example - Document - 001

    Description:
        Use the context manager to open CATIA documents and close

    Requirements:
        - CATIA running.
        - Tests already setup.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################
from pathlib import Path
import time

from pycatia import CATIADocHandler

catia_part = Path(os.getcwd(), r"tests\cat_files\part_measurable.CATPart")

with CATIADocHandler(catia_part) as caa:
    document = caa.document
    # do some stuff.
    # save if you need to.
    time.sleep(5)  # don't do this, no need.
    # document is automatically closed. Lovely.
