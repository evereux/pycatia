#! /usr/bin/python3.6

"""

    Example 7:

    Use the context manager to open CATIA documents and close

"""

import time

from pycatia import CATIADocHandler

catia_part = r'tests\cat_files\part_measurable.CATPart'

with CATIADocHandler(catia_part) as caa:
    document = caa.document
    # do some stuff.
    # save if you need to.
    time.sleep(5)  # don't do this, no need.
    # document is automatically closed. Lovely.
